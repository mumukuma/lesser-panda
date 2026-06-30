#!/usr/bin/env python3
"""
ig_audit.py — 盤點 wiki 裡所有 instagram: 連結，列出問題供人工複查。

設計理念（對齊 ROADMAP 圖片集「作者層」收尾）：
  - 靜態站不知連結死活，這支腳本半自動列清單給作者人工清理；**不自動改任何 wiki**。
  - IG 反爬嚴格（oEmbed 需 token、HEAD 常被擋、會跳登入牆），**不追求完美偵測**：
    寧可標「疑似」讓人複查，也不擅自判死。
  - 預設只做「離線」事：列出全部連結 + 標出「未含帳號形式」（依新 SCHEMA 建議回填）。
    加 --check 才連網做 best-effort 活性檢查。

用法（在 wiki 根目錄）：
    python tools/ig_audit.py                 # 只列表 + 格式檢查（離線、秒回）
    python tools/ig_audit.py --no-account    # 只列「未含帳號形式」的連結（回填清單）
    python tools/ig_audit.py --check         # 額外連網 best-effort 檢查疑似失效（慢）
    python tools/ig_audit.py --check --only-suspect   # 連網，只印疑似失效
    python tools/ig_audit.py -o ig_audit.md  # 同時輸出 Markdown 報告
    python tools/ig_audit.py --json          # 機器可讀輸出

退出碼：永遠 0（純提示、不擋關，符合「wiki 為唯一正本、工具只提示」原則）；
        僅腳本自身錯誤回非零。
"""

from __future__ import annotations

import re
import sys
import json
import glob
import time
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

# 解析 instagram URL：發文帳號（選填）、類型（p/reel/tv）、shortcode
IG_RE = re.compile(
    r"instagram\.com/(?:([^/?#]+)/)?(p|reel|tv)/([^/?#]+)", re.IGNORECASE
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# IG 路徑保留字：出現在帳號位置時其實代表「沒帳號」
RESERVED = {"p", "reel", "tv", "explore", "stories", "tv"}


def collect_instagram(path: Path) -> list[str]:
    """從單一 .md 的 frontmatter 取出 instagram 清單（每項為原始字串，可能含日期後綴）。"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else text[3:]
    out: list[str] = []
    in_ig = False
    for line in block.splitlines():
        stripped = line.strip()
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            in_ig = key == "instagram"
            # 單行形式 instagram: <url>
            if in_ig and val and not val.startswith("["):
                out.append(val)
                in_ig = False
            continue
        if in_ig and stripped.startswith("- "):
            out.append(stripped[2:].strip())
    return out


def parse_entry(raw: str) -> dict:
    """把一條 instagram 字串拆成 url / date / account / shortcode / kind。"""
    parts = raw.split()
    url = parts[0] if parts else ""
    date = next((p for p in parts[1:] if DATE_RE.match(p)), "")
    account, kind, shortcode = "", "", ""
    m = IG_RE.search(url)
    if m:
        acc, kind, shortcode = m.group(1), m.group(2).lower(), m.group(3)
        if acc and acc.lower() not in RESERVED:
            account = acc
    return {
        "raw": raw,
        "url": url,
        "date": date,
        "account": account,
        "kind": kind,
        "shortcode": shortcode,
        "has_account": bool(account),
        "is_ig": bool(m),
    }


def check_live(url: str, timeout: float) -> tuple[str, str]:
    """Best-effort 活性檢查。回 (status, note)；status ∈ ok/suspect/blocked/error。

    不依賴外部套件（只用 stdlib urllib）；IG 常擋，blocked 不代表連結壞。
    """
    import urllib.request
    import urllib.error

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            final = resp.geturl()
            body = resp.read(60000).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "suspect", "HTTP 404（貼文可能已刪）"
        if e.code == 429:
            return "blocked", "HTTP 429 限流，稍後再試"
        return "blocked", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001 — 網路類錯誤一律歸 error
        return "error", f"連線失敗：{type(e).__name__}"

    low = body.lower()
    if "/accounts/login" in final or "loginform" in low:
        # 登入牆：多數公開貼文也會被擋，無法判定 → blocked
        return "blocked", "被登入牆擋下，無法判定（多為正常）"
    if any(s in body for s in (
        "Sorry, this page isn't available",
        "頁面無法使用",
        "ページは利用できません",
    )):
        return "suspect", "頁面顯示『無法使用』（已刪／轉私密）"
    # 抓得到 og:title 通常代表貼文還在
    if 'property="og:title"' in low or "instagram" in low:
        return "ok", "頁面正常回應"
    return "blocked", "回應無法判定"


def main() -> int:
    ap = argparse.ArgumentParser(description="盤點 wiki 的 instagram: 連結")
    ap.add_argument("--check", action="store_true", help="連網 best-effort 檢查活性（慢）")
    ap.add_argument("--no-account", action="store_true",
                    help="只列『未含帳號形式』的連結（回填清單）")
    ap.add_argument("--only-suspect", action="store_true",
                    help="搭配 --check：只印 suspect/error")
    ap.add_argument("--timeout", type=float, default=8.0, help="每筆連網逾時秒數")
    ap.add_argument("--sleep", type=float, default=1.0,
                    help="--check 時每筆之間的禮貌間隔秒數")
    ap.add_argument("-o", "--out", help="另存 Markdown 報告到檔案")
    ap.add_argument("--json", action="store_true", help="輸出 JSON")
    args = ap.parse_args()

    rows: list[dict] = []
    for fp in sorted(glob.glob(str(WIKI / "*.md"))):
        name = Path(fp).stem
        if name in ("index", "log"):
            continue
        for raw in collect_instagram(Path(fp)):
            e = parse_entry(raw)
            e["slug"] = name
            rows.append(e)

    # 連網檢查
    if args.check:
        n = len(rows)
        for i, e in enumerate(rows, 1):
            if not e["is_ig"] or not e["shortcode"]:
                e["status"], e["note"] = "skip", "非標準 IG 貼文連結"
                continue
            # embed/檢查都用正規化短連結
            canon = f"https://www.instagram.com/{e['kind']}/{e['shortcode']}/"
            print(f"  [{i}/{n}] 檢查 {e['slug']} … {e['shortcode']}",
                  file=sys.stderr)
            e["status"], e["note"] = check_live(canon, args.timeout)
            if i < n and args.sleep:
                time.sleep(args.sleep)

    # 篩選
    view = rows
    if args.no_account:
        view = [e for e in rows if e["is_ig"] and not e["has_account"]]
    if args.check and args.only_suspect:
        view = [e for e in view if e.get("status") in ("suspect", "error")]

    if args.json:
        print(json.dumps(view, ensure_ascii=False, indent=2))
        return 0

    # 統計
    total = len(rows)
    no_acc = [e for e in rows if e["is_ig"] and not e["has_account"]]
    not_ig = [e for e in rows if not e["is_ig"]]
    lines: list[str] = []
    lines.append(f"# IG 連結稽核（共 {total} 筆，{len({e['slug'] for e in rows})} 隻）\n")
    lines.append(f"- 未含帳號形式（建議回填）：**{len(no_acc)}**")
    if not_ig:
        lines.append(f"- 非標準 IG 連結（請檢查）：**{len(not_ig)}**")
    if args.check:
        from collections import Counter
        c = Counter(e.get("status", "?") for e in rows)
        lines.append(
            "- 活性：ok {ok}／疑似失效 {s}／被擋無法判定 {b}／連線錯誤 {er}".format(
                ok=c.get("ok", 0), s=c.get("suspect", 0),
                b=c.get("blocked", 0), er=c.get("error", 0),
            )
        )
        lines.append("  （『被擋』多為 IG 反爬正常現象，非連結壞）")
    lines.append("")

    if not view:
        lines.append("（無符合條件的項目）")
    else:
        lines.append("| 個體 | 帳號 | 連結 | 日期 | 狀態 |")
        lines.append("|---|---|---|---|---|")
        for e in view:
            acc = "@" + e["account"] if e["account"] else "⚠️ 無帳號"
            status = ""
            if args.check:
                badge = {"ok": "✅ ok", "suspect": "❌ 疑似失效",
                         "blocked": "🔒 被擋", "error": "⚠️ 連線錯誤",
                         "skip": "—"}.get(e.get("status", ""), e.get("status", ""))
                status = f"{badge}（{e.get('note', '')}）" if e.get("note") else badge
            lines.append(
                f"| `{e['slug']}` | {acc} | {e['url']} | {e['date'] or '—'} | {status or '—'} |"
            )

    report = "\n".join(lines)
    print(report)
    if args.out:
        Path(args.out).write_text(report + "\n", encoding="utf-8")
        print(f"\n→ 已寫入 {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
