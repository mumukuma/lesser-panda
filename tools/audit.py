#!/usr/bin/env python3
"""
audit.py — wiki 資料完整度檢查 + 與 redpanda-lineage 比對

設計理念：不重爬 RPF（JS 動態網站、慢且脆弱）。改用 redpanda-lineage
（RPF 的底層開源資料庫）的整包文字檔做本地比對，一次 clone、秒跑、可重複。

用法（在 wiki 根目錄）：
    # 取得/更新 lineage 主檔（第一次或想刷新時才需要）
    git clone --depth 1 https://github.com/wwoast/redpanda-lineage /tmp/redpanda-lineage

    python tools/audit.py                 # 印報告
    python tools/audit.py -o audit.md     # 同時輸出 Markdown 報告

無 lineage 時仍可跑「wiki 自身」那幾項檢查。
"""

from __future__ import annotations  # 相容舊版 Python

import re
import sys
import glob
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINEAGE = Path("/tmp/redpanda-lineage")

KANJI_RE = re.compile(r"[一-鿿々]")
KANA_RE = re.compile(r"[぀-ヿ]")


# ── 極簡 frontmatter 解析（只取需要的欄位）─────────────────────
def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else text[3:]
    fm, key = {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("["):
                fm[key] = [x.strip() for x in val.strip("[]").split(",") if x.strip()]
            elif val in ("", "~", "null"):
                fm[key] = None
            else:
                fm[key] = val
        elif line.lstrip().startswith("- ") and key:
            fm.setdefault(key, [] if not isinstance(fm.get(key), list) else fm[key])
            if not isinstance(fm[key], list):
                fm[key] = []
            fm[key].append(line.lstrip()[2:].strip())
    return fm


def norm_date(s):
    if not s:
        return None
    s = str(s).replace("/", "-")
    parts = s.split("-")
    if len(parts) == 3:
        return f"{int(parts[0]):04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    return s  # 只有年份


# ── lineage 載入 ──────────────────────────────────────────────
def load_lineage() -> dict:
    if not LINEAGE.exists():
        return {}
    idx = {}
    for f in glob.glob(str(LINEAGE / "pandas/**/*.txt"), recursive=True):
        d = {}
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            if ":" in line and not line.startswith("photo"):
                k, _, v = line.partition(":")
                d[k.strip()] = v.strip()
        if d.get("_id", "").isdigit():
            idx[int(d["_id"])] = d
    return idx


# ── 主流程 ────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", help="輸出 Markdown 報告到檔案")
    args = ap.parse_args()

    files = sorted(WIKI.glob("*.md"))
    entries = {}
    for f in files:
        if f.name in ("index.md", "log.md"):
            continue
        entries[f.name] = read_frontmatter(f)

    lineage = load_lineage()
    R = []  # (嚴重度, 類別, 訊息)

    # 1) wiki 自身缺漏
    seen_rpf = {}
    for name, fm in entries.items():
        rpf = fm.get("rpf_id")
        url = fm.get("rpf_url") or ""
        if not rpf:
            R.append(("warn", "缺 rpf_id", name))
        else:
            seen_rpf.setdefault(int(rpf) if str(rpf).isdigit() else rpf, []).append(name)
        if "#query/" in url:
            R.append(("warn", "用 #query 連結（未爬 profile）", name))
        if not fm.get("born"):
            R.append(("warn", "缺生日", name))
        if not fm.get("sources"):
            R.append(("info", "缺 sources", name))
        if not fm.get("zoos"):
            R.append(("info", "缺居住地 zoos", name))

    # 2) rpf_id 重複
    for rid, names in seen_rpf.items():
        if len(names) > 1:
            R.append(("error", f"rpf_id {rid} 重複", " / ".join(names)))

    # 3) 與 lineage 比對
    cross = 0
    if lineage:
        for name, fm in entries.items():
            rpf = fm.get("rpf_id")
            if not (rpf and str(rpf).isdigit()):
                continue
            d = lineage.get(int(rpf))
            if not d:
                R.append(("info", "lineage 查無此 rpf_id", f"{name} (#{rpf})"))
                continue
            cross += 1
            # 生日
            wb, lb = norm_date(fm.get("born")), norm_date(d.get("birthday"))
            if wb and lb and len(wb) == 10 and wb != lb:
                R.append(("error", "生日與 lineage 不符", f"{name}: wiki={wb} lineage={lb}"))
            # 日文/漢字：lineage 有漢字但 wiki japanese 無漢字
            ja = fm.get("japanese") or ""
            lin_ja = " ".join([d.get("ja.name", ""), d.get("ja.othernames", "")])
            lin_kanji = [w for w in re.split(r"[ ,，、/]+", lin_ja)
                         if KANJI_RE.search(w) and not KANA_RE.search(w)]
            if lin_kanji and not KANJI_RE.search(ja):
                R.append(("warn", "lineage 有漢字名、wiki 未收", f"{name}: {lin_kanji[0]}"))
            # 生卒狀態
            wiki_dead = bool(fm.get("died"))
            lin_dead = bool(d.get("death"))
            if lin_dead and not wiki_dead:
                R.append(("warn", "lineage 標示已歿、wiki 未標", f"{name}: {d.get('death')}"))

    # ── 輸出 ──
    order = {"error": 0, "warn": 1, "info": 2}
    R.sort(key=lambda x: (order[x[0]], x[1]))
    icon = {"error": "🔴", "warn": "🟡", "info": "⚪"}

    lines = [f"# Wiki 資料完整度報告", ""]
    lines.append(f"條目數：{len(entries)}　|　lineage 比對："
                 + (f"{cross} 筆" if lineage else "未啟用（無 /tmp/redpanda-lineage）"))
    lines.append("")
    cats = {}
    for sev, cat, msg in R:
        cats.setdefault((sev, cat), []).append(msg)
    if not R:
        lines.append("✅ 沒有發現問題。")
    for (sev, cat), msgs in sorted(cats.items(), key=lambda x: order[x[0][0]]):
        lines.append(f"## {icon[sev]} {cat}（{len(msgs)}）")
        for m in msgs:
            lines.append(f"- {m}")
        lines.append("")

    report = "\n".join(lines)
    print(report)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"\n（已寫入 {args.out}）")

    n_err = sum(1 for s, _, _ in R if s == "error")
    print(f"\n摘要：🔴 {n_err}　🟡 {sum(1 for s,_,_ in R if s=='warn')}　"
          f"⚪ {sum(1 for s,_,_ in R if s=='info')}")


if __name__ == "__main__":
    main()
