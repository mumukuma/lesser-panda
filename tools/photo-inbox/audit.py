#!/usr/bin/env python3
"""photo-inbox-audit — compare the reader photo-submission inbox against the
current wiki, READ-ONLY. Prints a concise Chinese report and (optionally) a
findings JSON. It NEVER writes to the wiki, the Sheet, or git.

Inputs
------
--submissions  Path to a JSON file the caller built from the Google Sheet.
               A JSON array of row objects. Recognized keys (all optional
               except `slug` and `ig`):
                 submission_id, respondent_id, submitted_at,
                 panda, url, slug, ig, is_self, marked_done
               `ig`         = the raw "IG 連結" cell (may hold up to ~10
                              links separated by newlines/spaces).
               `marked_done`= the I-column "已補進 wiki" status. Truthy =
                              marked. Accepts true/1/"yes"/"是"/"✅"/"done".
--wiki-dir     Directory containing the wiki <slug>.md files
               (default: ./wiki, fallback used by the skill).
--json-out     Optional path to also dump the structured findings.

The Sheet itself is fetched by Claude via the Google Drive connector; this
script only consumes the already-extracted rows.
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shortcodes import extract_shortcodes, has_ig_signal, canonical_post_url  # noqa: E402

TRUTHY = {"true", "1", "yes", "y", "是", "✅", "done", "已補", "已補進", "ok"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Latin "test" only when it is its own token, so real shortcodes like
# "EscTest_1" or names like "greatest" are NOT mistaken for test rows.
TEST_LATIN_RE = re.compile(r"(?<![a-z])test(?![a-z])", re.IGNORECASE)
TEST_CJK = ("測試", "テスト")
# Fields a human types a nickname / description into. Deliberately EXCLUDES
# `ig` (URLs & shortcodes) to avoid false positives inside a shortcode.
TEST_FIELDS = ("panda", "respondent_id", "url", "slug")


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def is_test_row(row):
    """A row is a test row if a human-entered field looks like a test entry.
    Checks nickname/description fields only — never the IG-link cell."""
    blob = " ".join(str(row.get(k, "")) for k in TEST_FIELDS)
    if any(tok in blob for tok in TEST_CJK):
        return True
    return bool(TEST_LATIN_RE.search(blob))


def is_marked(row):
    return str(row.get("marked_done", "")).strip().lower() in TRUTHY


def wiki_frontmatter(text):
    """Return the frontmatter block text, or the whole file if none found."""
    m = FRONTMATTER_RE.search(text)
    return m.group(1) if m else text


def load_wiki(wiki_dir):
    """slug -> {'shortcodes': [...], 'path': ...}. Shortcodes come from the
    frontmatter (where `instagram:` lives); duplicates are preserved."""
    wiki = {}
    for path in sorted(glob.glob(os.path.join(wiki_dir, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        codes = extract_shortcodes(wiki_frontmatter(text))
        wiki[slug] = {"shortcodes": codes, "path": path}
    return wiki


# --------------------------------------------------------------------------- #
# Audit
# --------------------------------------------------------------------------- #
def audit(submissions, wiki):
    findings = {
        "counts": {},
        "to_add": {},          # slug -> [ {shortcode, url, submission_id} ]
        "can_mark": [],        # {slug, submission_id, shortcodes}
        "anomaly": [],         # {slug, submission_id, missing}
        "data_issues": [],     # {submission_id, slug, raw}
        "missing_file": [],    # {slug, submission_id}
        "done": [],            # {slug, submission_id}
        "dupes": {"a_same_page": [], "b_cross_page": [],
                  "c_inbox_reingest": [], "d_inbox_cross_slug": []},
    }

    inbox_seen = {}          # (slug, code) -> count
    inbox_code_slugs = {}    # code -> set(slug)

    for row in submissions:
        sid = row.get("submission_id", "?")
        slug = str(row.get("slug", "")).strip()
        ig_raw = row.get("ig", "")
        codes = extract_shortcodes(ig_raw)

        # --- data problem: something in the cell but no usable post URL ---
        if not codes:
            if has_ig_signal(ig_raw) or str(ig_raw).strip():
                findings["data_issues"].append(
                    {"submission_id": sid, "slug": slug,
                     "raw": str(ig_raw).strip()[:200]})
            continue

        # track inbox dupes (normalized, dedupe within-row first for c/d)
        for code in set(codes):
            inbox_seen[(slug, code)] = inbox_seen.get((slug, code), 0) + 1
            inbox_code_slugs.setdefault(code, set()).add(slug)

        # --- missing wiki file ---
        if slug not in wiki:
            findings["missing_file"].append({"slug": slug, "submission_id": sid})
            continue

        wiki_codes = set(wiki[slug]["shortcodes"])
        sub_codes = list(dict.fromkeys(codes))  # unique, keep order
        missing = [c for c in sub_codes if c not in wiki_codes]
        marked = is_marked(row)

        if not missing:
            if marked:
                findings["done"].append({"slug": slug, "submission_id": sid})
            else:
                findings["can_mark"].append(
                    {"slug": slug, "submission_id": sid, "shortcodes": sub_codes})
        else:
            if marked:
                findings["anomaly"].append(
                    {"slug": slug, "submission_id": sid, "missing": missing})
            else:
                bucket = findings["to_add"].setdefault(slug, [])
                already = {i["shortcode"] for i in bucket}
                for cc in missing:
                    if cc not in already:
                        bucket.append(
                            {"shortcode": cc, "url": canonical_post_url(cc),
                             "submission_id": sid})
                        already.add(cc)

    # --- dup a) same page same code > 1 (within a wiki file) ---
    for slug, info in wiki.items():
        seen = {}
        for c in info["shortcodes"]:
            seen[c] = seen.get(c, 0) + 1
        for c, n in seen.items():
            if n > 1:
                findings["dupes"]["a_same_page"].append(
                    {"slug": slug, "shortcode": c, "count": n})

    # --- dup b) same code across different wiki pages ---
    wiki_code_slugs = {}
    for slug, info in wiki.items():
        for c in set(info["shortcodes"]):
            wiki_code_slugs.setdefault(c, set()).add(slug)
    for c, slugs in wiki_code_slugs.items():
        if len(slugs) > 1:
            findings["dupes"]["b_cross_page"].append(
                {"shortcode": c, "slugs": sorted(slugs)})

    # --- dup c) inbox: same slug + same code submitted more than once ---
    for (slug, code), n in inbox_seen.items():
        if n > 1:
            findings["dupes"]["c_inbox_reingest"].append(
                {"slug": slug, "shortcode": code, "count": n})

    # --- dup d) inbox: same code submitted to different slugs ---
    for code, slugs in inbox_code_slugs.items():
        if len(slugs) > 1:
            findings["dupes"]["d_inbox_cross_slug"].append(
                {"shortcode": code, "slugs": sorted(slugs)})

    findings["counts"] = {
        "new_submissions": len(submissions),
        "to_add_slugs": len(findings["to_add"]),
        "can_mark": len(findings["can_mark"]),
        "anomaly": len(findings["anomaly"]),
        "data_issues": len(findings["data_issues"]),
        "missing_file": len(findings["missing_file"]),
        "done": len(findings["done"]),
    }
    return findings


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def _empty(items):
    return "（無）" if not items else None


def render(findings, filtered_test):
    today = datetime.date.today().isoformat()
    L = []
    c = findings["counts"]
    L.append(f"# 照片投稿比對報告（{today}）\n")
    L.append(f"新投稿數：{c['new_submissions']}（已過濾測試列 {filtered_test} 筆）\n")

    # 待補
    L.append("## 待補（依 slug 合併）")
    if not findings["to_add"]:
        L.append("（無）")
    else:
        for slug in sorted(findings["to_add"]):
            parts = [f"{i['shortcode']}（{i['url']}）" for i in findings["to_add"][slug]]
            L.append(f"- `{slug}`：缺 " + "、".join(parts))
    L.append("")

    # 可補標
    L.append("## 可補標（wiki 已有、I 欄未標）")
    if not findings["can_mark"]:
        L.append("（無）")
    else:
        for it in findings["can_mark"]:
            L.append(f"- `{it['slug']}`（submission {it['submission_id']}）："
                     + "、".join(it["shortcodes"]))
    L.append("")

    # 異常
    L.append("## 異常／需查證")
    if not findings["anomaly"]:
        L.append("（無）")
    else:
        for it in findings["anomaly"]:
            L.append(f"- `{it['slug']}`（submission {it['submission_id']}）："
                     f"I 欄已標為已補，但 wiki 缺 " + "、".join(it["missing"])
                     + " — 疑投錯隻？")
    L.append("")

    # 資料問題
    L.append("## 資料問題")
    if not findings["data_issues"]:
        L.append("（無）")
    else:
        for it in findings["data_issues"]:
            L.append(f"- submission {it['submission_id']}（slug `{it['slug']}`）："
                     f"無可用貼文 URL（只填帳號或非貼文連結）→ 需補正式貼文連結；"
                     f"原內容：{it['raw']}")
    L.append("")

    # 缺檔
    L.append("## 缺檔")
    if not findings["missing_file"]:
        L.append("（無）")
    else:
        for it in findings["missing_file"]:
            L.append(f"- `{it['slug']}`：wiki 檔不存在（submission {it['submission_id']}）")
    L.append("")

    # 重複檢查
    d = findings["dupes"]
    L.append("## 重複檢查")
    L.append("- a) 同頁同碼>1：" + (
        "（無）" if not d["a_same_page"] else
        "；".join(f"`{x['slug']}` 的 {x['shortcode']}×{x['count']}" for x in d["a_same_page"])))
    L.append("- b) 同碼跨不同隻（複查，可能一圖兩隻）：" + (
        "（無）" if not d["b_cross_page"] else
        "；".join(f"{x['shortcode']} → {', '.join(x['slugs'])}" for x in d["b_cross_page"])))
    L.append("- c) 收件匣重投（同 slug+同碼）：" + (
        "（無）" if not d["c_inbox_reingest"] else
        "；".join(f"`{x['slug']}` 的 {x['shortcode']}×{x['count']}" for x in d["c_inbox_reingest"])))
    L.append("- d) 收件匣同碼投不同隻（複查）：" + (
        "（無）" if not d["d_inbox_cross_slug"] else
        "；".join(f"{x['shortcode']} → {', '.join(x['slugs'])}" for x in d["d_inbox_cross_slug"])))
    L.append("")

    # 無待辦判定
    nothing_todo = (
        not findings["to_add"] and not findings["can_mark"]
        and not findings["anomaly"] and not findings["data_issues"]
        and not findings["missing_file"]
        and not any(d.values())
    )
    if nothing_todo:
        L.append("✅ 無待辦（全部已補齊、已標記，且無重複）")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Read-only photo inbox vs wiki audit")
    ap.add_argument("--submissions", required=True)
    ap.add_argument("--wiki-dir", default="./wiki")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    with open(args.submissions, encoding="utf-8") as fh:
        rows = json.load(fh)
    if isinstance(rows, dict) and "rows" in rows:
        rows = rows["rows"]

    kept = [r for r in rows if not is_test_row(r)]
    filtered = len(rows) - len(kept)

    if not os.path.isdir(args.wiki_dir):
        print(f"⚠️ 找不到 wiki 目錄：{args.wiki_dir}", file=sys.stderr)
        sys.exit(2)

    wiki = load_wiki(args.wiki_dir)
    findings = audit(kept, wiki)
    findings["_filtered_test_rows"] = filtered

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(findings, fh, ensure_ascii=False, indent=2)

    print(render(findings, filtered))


if __name__ == "__main__":
    main()
