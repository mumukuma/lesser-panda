#!/usr/bin/env python3
"""photo-inbox-audit backfill — write the CLEAN 待補 links into each slug's
`instagram:` frontmatter list. Deliberately conservative:

  * Only writes items from findings["to_add"] (unmarked + missing = clean gap).
  * HOLDS (never writes, only lists) any shortcode that is flagged for review:
      - dup b) same code across different wiki pages
      - dup d) same code submitted to different slugs
    plus everything the audit already parked outside to_add: anomaly, data
    issues, missing-file, and "可補標" (wiki already has it).
  * Never touches the Google Sheet, never git-commits.
  * Only edits a file when the `instagram:` block list can be located cleanly;
    anything ambiguous is reported for manual handling instead of guessed at.

Consumes the findings JSON produced by `audit.py --json-out`.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shortcodes import extract_shortcodes, canonical_post_url  # noqa: E402

FM_KEY_RE = re.compile(r"^(\s*)instagram:\s*(.*)$")
ITEM_RE = re.compile(r"^(\s*)-\s+\S")


def review_held_codes(findings):
    """Shortcodes we must NOT auto-write because they need a human look."""
    held = set()
    for x in findings["dupes"]["b_cross_page"]:
        held.add(x["shortcode"])
    for x in findings["dupes"]["d_inbox_cross_slug"]:
        held.add(x["shortcode"])
    return held


def frontmatter_bounds(lines):
    """Return (start, end) line indices of the frontmatter body, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    for j in range(1, len(lines)):
        if lines[j].strip() == "---":
            return (1, j)
    return None


def insert_into_instagram(text, urls):
    """Return (new_text, status). status is 'written' | 'no-key' | 'inline'."""
    lines = text.split("\n")
    b = frontmatter_bounds(lines)
    if b is None:
        return text, "no-frontmatter"
    start, end = b

    key_idx = None
    for i in range(start, end):
        m = FM_KEY_RE.match(lines[i])
        if m:
            key_idx = i
            key_indent = m.group(1)
            inline_val = m.group(2).strip()
            break

    if key_idx is None:
        return text, "no-key"
    # An inline list (instagram: [..]) or inline scalar we won't rewrite blindly.
    if inline_val and inline_val not in ("|", ">", "[]"):
        return text, "inline"

    # Find contiguous list items following the key.
    last_item = key_idx
    item_indent = key_indent + "  "
    saw_item = False
    for i in range(key_idx + 1, end):
        if ITEM_RE.match(lines[i]):
            saw_item = True
            last_item = i
            item_indent = ITEM_RE.match(lines[i]).group(1)
        elif lines[i].strip() == "":
            # blank line inside the block: keep scanning but don't move anchor
            continue
        else:
            break

    new_lines = [f"{item_indent}- {u}" for u in urls]
    anchor = last_item if saw_item else key_idx
    result = lines[: anchor + 1] + new_lines + lines[anchor + 1:]
    return "\n".join(result), "written"


def backfill(findings, wiki_dir, dry_run):
    held_codes = review_held_codes(findings)
    written = {}     # slug -> [urls]
    held = {}        # slug -> [shortcodes]  (held for review)
    problems = []    # human-readable manual-handling notes

    for slug, items in sorted(findings["to_add"].items()):
        path = os.path.join(wiki_dir, f"{slug}.md")
        if not os.path.isfile(path):
            problems.append(f"`{slug}`：wiki 檔不存在，無法回填")
            continue

        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        present = set(extract_shortcodes(text))

        to_write, held_here = [], []
        for it in items:
            code = it["shortcode"]
            if code in held_codes:
                held_here.append(code)
            elif code in present:
                continue  # already there, nothing to do
            else:
                to_write.append(code)

        if held_here:
            held[slug] = held_here
        if not to_write:
            continue

        urls = [canonical_post_url(c) for c in to_write]
        new_text, status = insert_into_instagram(text, urls)
        if status == "written":
            if not dry_run:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
            written[slug] = urls
        elif status == "no-key":
            problems.append(f"`{slug}`：frontmatter 無 `instagram:` 欄位，需手動新增後再補")
        elif status == "inline":
            problems.append(f"`{slug}`：`instagram:` 為行內格式，未動，請手動補：" + "、".join(urls))
        else:
            problems.append(f"`{slug}`：frontmatter 格式異常（{status}），未動")

    return written, held, problems


def render(written, held, problems, findings, dry_run):
    L = []
    mode = "（DRY RUN，未實際寫入）" if dry_run else ""
    L.append(f"# 照片投稿回填結果 {mode}\n")

    L.append("## 已補進 wiki")
    if not written:
        L.append("（無）")
    else:
        for slug, urls in written.items():
            L.append(f"- `{slug}`：+{len(urls)} → " + "、".join(urls))
    L.append("")

    L.append("## 跳過：需複查（未自動補）")
    any_review = held or findings["anomaly"] or findings["dupes"]["b_cross_page"] \
        or findings["dupes"]["d_inbox_cross_slug"]
    if not any_review:
        L.append("（無）")
    else:
        for slug, codes in held.items():
            L.append(f"- `{slug}`：{ '、'.join(codes) } — 該碼跨頁/跨隻，疑一圖兩隻或投錯隻，請人工判斷")
        for it in findings["anomaly"]:
            L.append(f"- `{it['slug']}`（submission {it['submission_id']}）："
                     f"I 欄已標但 wiki 缺 {'、'.join(it['missing'])} — 疑投錯隻，未動")
    L.append("")

    L.append("## 資料問題（未動，需你補正式貼文 URL）")
    if not findings["data_issues"]:
        L.append("（無）")
    else:
        for it in findings["data_issues"]:
            L.append(f"- submission {it['submission_id']}（slug `{it['slug']}`）：{it['raw']}")
    L.append("")

    if problems:
        L.append("## 需手動處理")
        for p in problems:
            L.append(f"- {p}")
        L.append("")

    L.append("---")
    L.append("已補的請自行檢查後 git 上版；收件匣 I 欄「已補進」標記請自行用 Claude in Chrome 操作。")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Backfill clean 待補 links into wiki frontmatter")
    ap.add_argument("--findings", required=True, help="audit.py 的 --json-out 產物")
    ap.add_argument("--wiki-dir", default="./wiki")
    ap.add_argument("--dry-run", action="store_true", help="只預覽不寫入")
    args = ap.parse_args()

    with open(args.findings, encoding="utf-8") as fh:
        findings = json.load(fh)
    if not os.path.isdir(args.wiki_dir):
        print(f"⚠️ 找不到 wiki 目錄：{args.wiki_dir}", file=sys.stderr)
        sys.exit(2)

    written, held, problems = backfill(findings, args.wiki_dir, args.dry_run)
    print(render(written, held, problems, findings, args.dry_run))


if __name__ == "__main__":
    main()
