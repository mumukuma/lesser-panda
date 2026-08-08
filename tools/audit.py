#!/usr/bin/env python3
"""
audit.py — wiki 資料完整度檢查（+ 可選的 redpanda-lineage 比對）

⚠️ 2026-07-14 起 lineage 比對改為 opt-in：wiki 經作者大量校訂後可信度已高於
RPF/lineage（雜訊多、僅為「線索」，見 CLAUDE.md 資料來源原則），預設只跑
wiki 自身檢查，加 --lineage 才做比對。

設計理念：不重爬 RPF（JS 動態網站、慢且脆弱）。改用 redpanda-lineage
（RPF 的底層開源資料庫）的整包文字檔做本地比對，一次 clone、秒跑、可重複。

用法（在 wiki 根目錄）：
    python tools/audit.py                 # 印報告（僅 wiki 自身檢查）
    python tools/audit.py --lineage       # 加跑 lineage 比對（線索用，先 clone：
                                          #   git clone --depth 1 https://github.com/wwoast/redpanda-lineage /tmp/redpanda-lineage）
    python tools/audit.py -o audit.md     # 同時輸出 Markdown 報告
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

# frontmatter 解析與日期正規化：與 build_db 共用同一套（tools/wiki_io.py），
# 確保稽核看到的資料 = 建檔看到的資料
sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_io import read_frontmatter, norm_date  # noqa: E402
from zoo_registry import ZooRegistry  # noqa: E402
# 來源官方性判定：直接用建檔同一支分類器，稽核才不會與網站顯示脫節
from build_db import is_official_source, _host  # noqa: E402
from urllib.parse import urlparse  # noqa: E402


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
    ap.add_argument("--strict", action="store_true",
                    help="僅當有 wiki 內部整合性錯誤（如 rpf_id 重複）時以 exit 1 結束；"
                         "與 lineage 比對的『不符』屬提示、永不影響 exit code")
    ap.add_argument("--lineage", action="store_true",
                    help="啟用與 redpanda-lineage 的比對（2026-07-14 起預設不跑；"
                         "lineage 僅為線索、非權威）")
    args = ap.parse_args()

    files = sorted(WIKI.glob("*.md"))
    entries = {}
    for f in files:
        if f.name in ("index.md", "log.md"):
            continue
        entries[f.name] = read_frontmatter(f)

    lineage = load_lineage() if args.lineage else {}
    reg = ZooRegistry.load()
    R = []  # (嚴重度, 類別, 訊息)

    # 1) wiki 自身缺漏
    seen_rpf = {}
    for name, fm in entries.items():
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        # 檔案卡（limited-profile）：缺生日/rpf_id 屬預期狀態，降為 info 免噪音
        limited = "limited-profile" in tags
        rpf = fm.get("rpf_id")
        url = fm.get("rpf_url") or ""
        # RPF 降為「線索」、非權威（2026-07-14 原則）：缺 rpf_id 不是資料缺陷
        # （中國個體、蘋果籽佔位、官方來源建檔者本就常無 RPF profile），
        # 故一律列為 ⚪ info、不當黃燈警告，避免把 RPF 覆蓋率誤當成專案指標。
        if not rpf:
            R.append(("info", "缺 rpf_id", name))
        else:
            seen_rpf.setdefault(int(rpf) if str(rpf).isdigit() else rpf, []).append(name)
        if "#query/" in url:
            R.append(("warn", "用 #query 連結（未爬 profile）", name))
        if not fm.get("born"):
            R.append(("info" if limited else "warn", "缺生日", name))
        if limited and not fm.get("last_seen"):
            R.append(("warn", "檔案卡缺 last_seen（必填）", name))
        if not fm.get("sources"):
            R.append(("info", "缺 sources", name))
        if not fm.get("zoos"):
            R.append(("info", "缺居住地 zoos", name))

    # 2) rpf_id 重複
    for rid, names in seen_rpf.items():
        if len(names) > 1:
            R.append(("error", f"rpf_id {rid} 重複", " / ".join(names)))

    # 2.5) sources 裡的非官方 host（2026-08-03 新增）
    # 依 SCHEMA.md〈sources 與 extra_sources 的分工〉，`sources` 只放官方／一手來源。
    # 故 `sources` 出現 is_official_source() 判 False 的 host，必為以下兩者之一，都要處理：
    #   (a) 確實是園方官網／官方帳號，但漏掛 build_db 的 OFFICIAL_HOSTS/IG/FB/X 白名單
    #       → 該條目的「來源」區塊會整個空掉、網站顯示「未經官方佐證」（曾兩度發生）
    #   (b) 本來就非官方（新聞、部落格、NGO）→ 應搬到 `extra_sources`
    # RPF／lineage 是全 wiki 通用的線索來源、本就不該算官方，屬預期值故排除不報。
    _EXPECTED_NON_OFFICIAL = {"redpandafinder.com", "github.com"}
    src_hosts = {}
    for name, fm in entries.items():
        for u in (fm.get("sources") or []):
            u = str(u).split()[0]
            if not u.startswith("http"):
                continue
            if is_official_source(u):
                continue
            h = _host(u)
            if not h or h in _EXPECTED_NON_OFFICIAL:
                continue
            # IG/FB/X 共用網域：連帳號一起報，才看得出是哪個帳號沒掛白名單
            if h in ("instagram.com", "facebook.com", "x.com", "twitter.com"):
                seg = urlparse(u).path.strip("/").split("/")[0].lower().lstrip("@")
                h = f"{h}/@{seg}"
            src_hosts.setdefault(h, []).append(name)
    for h, names in sorted(src_hosts.items(), key=lambda kv: -len(kv[1])):
        R.append(("warn", "sources 有非官方 host（漏掛白名單或該進 extra_sources）",
                  f"{h} ×{len(names)}：{', '.join(sorted(names)[:4])}"
                  + ("…" if len(names) > 4 else "")))

    # 2.7) index.md 對帳（2026-08-08 新增；🔴 整合性錯誤，--strict 會擋）
    # 不變量：① index 的每個 [[wikilink]] 都對應存在的條目檔；② 每個條目檔至少
    # 在 index 出現一次；③ 頁首「條目總數：N」== 實際檔數（wiki/*.md 扣 index/log）。
    # 同一條目在多個家族表重複出現屬正常（交叉引用），不檢查唯一性。
    idx_text = (WIKI / "index.md").read_text(encoding="utf-8")
    idx_set = set(re.findall(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]", idx_text))
    file_set = {Path(n).stem for n in entries}
    for slug in sorted(idx_set - file_set):
        R.append(("error", "index 對帳：index 連到不存在的條目",
                  f"[[{slug}]]（條目改名/下架後 index 未同步？）"))
    for slug in sorted(file_set - idx_set):
        R.append(("error", "index 對帳：條目未列入 index", f"{slug}.md"))
    m_cnt = re.search(r"條目總數：(\d+)", idx_text)
    if not m_cnt:
        R.append(("error", "index 對帳：頁首缺「條目總數：N」", "index.md"))
    elif int(m_cnt.group(1)) != len(entries):
        R.append(("error", "index 對帳：頁首總數與實際檔數不符",
                  f"index 寫 {m_cnt.group(1)}、實際 {len(entries)}"))

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
            # 日文/漢字：lineage 有漢字但 wiki japanese 無漢字。
            # ⚠️ 僅對「有日本居住史」的個體提示：lineage/RPF 對每隻個體（含歐美）都
            # 機械附 ja.name 轉寫，非日本個體不採（其漢字多半實為中文名，屬 chinese 欄）。
            ja = fm.get("japanese") or ""
            lin_ja = " ".join([d.get("ja.name", ""), d.get("ja.othernames", "")])
            lin_kanji = [w for w in re.split(r"[ ,，、/]+", lin_ja)
                         if KANJI_RE.search(w) and not KANA_RE.search(w)
                         and "無名" not in w and not re.search(r"[（()）]", w)]  # 排除「(無名)」佔位值
            if lin_kanji and not KANJI_RE.search(ja) \
                    and "Japan" in reg.countries(fm.get("zoos")):
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
                 + (f"{cross} 筆" if lineage else
                    ("未啟用（無 /tmp/redpanda-lineage）" if args.lineage
                     else "未啟用（預設略過，加 --lineage 啟用；lineage 僅為線索）")))
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

    # --strict：只把「wiki 內部整合性錯誤」當作擋關依據（排除與 lineage 的比對，
    # 因 lineage 非權威，依 CLAUDE.md「不符」僅提示作者檢視、不代表 wiki 錯）。
    if args.strict:
        n_internal = sum(1 for s, c, _ in R if s == "error" and "lineage" not in c)
        if n_internal:
            print(f"\n🔴 wiki 內部整合性錯誤 {n_internal} 筆（--strict 擋下）。"
                  "lineage 不符不計入。")
            sys.exit(1)


if __name__ == "__main__":
    main()
