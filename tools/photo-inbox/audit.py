#!/usr/bin/env python3
"""photo-inbox-audit — compare the reader photo-submission inbox against the
current wiki, READ-ONLY. Prints a concise Chinese report and (optionally) a
findings JSON. It NEVER writes to the wiki, the Sheet, or git.

Inputs
------
--submissions  Path to either
                 (a) the RAW CSV/TSV text of the Google Sheet, dumped
                     verbatim from the Drive connector (preferred: no
                     hand-restructuring needed), or
                 (b) a JSON array of row objects (legacy format) with keys:
                     submission_id, respondent_id, submitted_at,
                     panda, url, slug, ig, is_self, marked_done
               Format is auto-detected (JSON if the file starts with [ or {).
               CSV columns are mapped by position A-I; a header row is
               detected and skipped automatically.
--wiki-dir     Directory containing the wiki <slug>.md files.
--json-out     Optional path to also dump the structured findings.

Auto-cleared duplicate hits (2026-08-07/08 maintainer rulings)
--------------------------------------------------------------
* dup a) "same page, same code" scans ONLY the `instagram:` block, not the
  whole frontmatter — a post listed in both `instagram:` and `sources:` is
  intentional, not a duplicate (full-repo check 2026-08-08: real dupes = 0).
* dup b)/d) groups where one side is the `log` page are dropped: log quotes
  post links by nature.
* dup b)/d) groups whose slugs are all one LITTER (same mother, fathers not
  conflicting, birthdays within 1 day) are dropped: one photo of a litter is
  deliberately attached to every cub. These codes are NOT held back from
  backfill anymore.
The report prints how many groups were auto-cleared so nothing is silent.
"""

import argparse
import csv
import datetime
import glob
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shortcodes import extract_shortcodes, has_ig_signal, canonical_post_url  # noqa: E402

TRUTHY = {"true", "1", "yes", "y", "是", "✅", "done", "已補", "已補進", "ok"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LOG_SLUG = "log"

# Latin "test" only when it is its own token, so real shortcodes like
# "EscTest_1" or names like "greatest" are NOT mistaken for test rows.
TEST_LATIN_RE = re.compile(r"(?<![a-z])test(?![a-z])", re.IGNORECASE)
TEST_CJK = ("測試", "テスト")
# Latin check: nickname/slug only. `url` is deliberately EXCLUDED — real
# submission URLs may contain a standalone "test" path segment. `ig` is
# excluded to avoid matching inside shortcodes.
TEST_LATIN_FIELDS = ("panda", "slug")
TEST_CJK_FIELDS = ("panda", "url", "slug", "respondent_id")

CSV_KEYS = ["submission_id", "respondent_id", "submitted_at", "panda",
            "url", "slug", "ig", "is_self", "marked_done"]


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def load_rows(path):
    """Auto-detect JSON (legacy) vs raw CSV/TSV dumped from the connector."""
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()
    head = text.lstrip()
    if head.startswith("[") or head.startswith("{"):
        rows = json.loads(text)
        if isinstance(rows, dict) and "rows" in rows:
            rows = rows["rows"]
        return rows

    first_line = text.splitlines()[0] if text.splitlines() else ""
    delim = "\t" if "\t" in first_line else ","
    raw = [r for r in csv.reader(io.StringIO(text), delimiter=delim)
           if any(c.strip() for c in r)]
    if raw and _is_header(raw[0]):
        raw = raw[1:]
    rows = []
    for r in raw:
        r = list(r) + [""] * (len(CSV_KEYS) - len(r))
        rows.append(dict(zip(CSV_KEYS, r[:len(CSV_KEYS)])))
    return rows


def _is_header(row):
    joined = " ".join(row).lower()
    return ("submission" in joined or "respondent" in joined
            or "ig 連結" in " ".join(row) or "已補進" in " ".join(row))


def is_test_row(row):
    """A row is a test row if a human-entered field looks like a test entry."""
    cjk_blob = " ".join(str(row.get(k, "")) for k in TEST_CJK_FIELDS)
    if any(tok in cjk_blob for tok in TEST_CJK):
        return True
    latin_blob = " ".join(str(row.get(k, "")) for k in TEST_LATIN_FIELDS)
    return bool(TEST_LATIN_RE.search(latin_blob))


def is_marked(row):
    return str(row.get("marked_done", "")).strip().lower() in TRUTHY


def wiki_frontmatter(text):
    """Return the frontmatter block text, or the whole file if none found."""
    m = FRONTMATTER_RE.search(text)
    return m.group(1) if m else text


def instagram_block(text):
    """Return ONLY the `instagram:` list block inside the frontmatter
    (key line + its contiguous `- ` items). Used for dup a) so links that
    also appear in `sources:` are not miscounted as same-page dupes."""
    fm = wiki_frontmatter(text)
    lines = fm.split("\n")
    out, in_block = [], False
    for line in lines:
        if re.match(r"^\s*instagram:\s*(.*)$", line):
            in_block = True
            out.append(line)
            continue
        if in_block:
            if re.match(r"^\s*-\s+\S", line) or line.strip() == "":
                out.append(line)
            else:
                in_block = False
    return "\n".join(out)


def load_wiki(wiki_dir):
    """slug -> {'shortcodes': [...], 'ig_shortcodes': [...], 'path': ...}.
    `shortcodes` = whole frontmatter (presence check, conservative);
    `ig_shortcodes` = instagram: block only (dup a) check)."""
    wiki = {}
    for path in sorted(glob.glob(os.path.join(wiki_dir, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        wiki[slug] = {
            "shortcodes": extract_shortcodes(wiki_frontmatter(text)),
            "ig_shortcodes": extract_shortcodes(instagram_block(text)),
            "path": path,
            "_text": text,
        }
    return wiki


# --------------------------------------------------------------------------- #
# Litter (同生群) detection — 2026-08-07 maintainer ruling
# --------------------------------------------------------------------------- #
BORN_RE = re.compile(r"^born:\s*['\"]?(\d{4}(?:-\d{2}){0,2})", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def parse_bio(wiki, slug, cache):
    """(born, mother, father) for a slug, from frontmatter `born:` and the
    body's 父/母 lines (first wikilink on the line). Missing pieces -> None."""
    if slug in cache:
        return cache[slug]
    born = mother = father = None
    info = wiki.get(slug)
    if info:
        text = info["_text"]
        m = BORN_RE.search(text)
        if m:
            born = m.group(1)
        for line in text.split("\n"):
            stripped = line.strip().lstrip("-*|>").strip().strip("*").strip()
            if father is None and re.match(r"^父\s*[：:]", stripped):
                mm = WIKILINK_RE.search(line)
                if mm:
                    father = mm.group(1).strip()
            elif mother is None and re.match(r"^母\s*[：:]", stripped):
                mm = WIKILINK_RE.search(line)
                if mm:
                    mother = mm.group(1).strip()
    cache[slug] = (born, mother, father)
    return cache[slug]


def _same_birthday(b1, b2):
    if not b1 or not b2:
        return False
    try:
        d1 = datetime.date.fromisoformat(b1)
        d2 = datetime.date.fromisoformat(b2)
        return abs((d1 - d2).days) <= 1
    except ValueError:
        return b1 == b2  # partial dates: exact match only


def same_litter(bio1, bio2):
    """Same mother (both known & equal), fathers not conflicting,
    birthdays within 1 day. Anything unknown that matters -> NOT a litter
    (kept for human review — the safe direction)."""
    born1, mo1, fa1 = bio1
    born2, mo2, fa2 = bio2
    if not _same_birthday(born1, born2):
        return False
    if not mo1 or not mo2 or mo1 != mo2:
        return False
    if fa1 and fa2 and fa1 != fa2:
        return False
    return True


def filter_group(slugs, wiki, bio_cache, cleared):
    """Apply the log + litter auto-clear rules to a dup b)/d) slug group.
    Returns the surviving slug list (may be empty => drop the group)."""
    rest = [s for s in slugs if s != LOG_SLUG]
    if len(rest) < len(slugs):
        cleared["log"] += 1
    if len(rest) < 2:
        return []
    bios = {s: parse_bio(wiki, s, bio_cache) for s in rest}
    all_litter = all(
        same_litter(bios[a], bios[b])
        for i, a in enumerate(rest) for b in rest[i + 1:]
    )
    if all_litter:
        cleared["litter"] += 1
        return []
    return rest


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
        "auto_cleared": {"log": 0, "litter": 0},
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

    bio_cache = {}
    cleared = findings["auto_cleared"]

    # --- dup a) same code > 1 inside one page's instagram: block ---
    for slug, info in wiki.items():
        if slug == LOG_SLUG:
            continue
        seen = {}
        for c in info["ig_shortcodes"]:
            seen[c] = seen.get(c, 0) + 1
        for c, n in seen.items():
            if n > 1:
                findings["dupes"]["a_same_page"].append(
                    {"slug": slug, "shortcode": c, "count": n})

    # --- dup b) same code across different wiki pages (auto-clears apply) ---
    wiki_code_slugs = {}
    for slug, info in wiki.items():
        for c in set(info["shortcodes"]):
            wiki_code_slugs.setdefault(c, set()).add(slug)
    for c, slugs in sorted(wiki_code_slugs.items()):
        if len(slugs) > 1:
            kept = filter_group(sorted(slugs), wiki, bio_cache, cleared)
            if kept:
                findings["dupes"]["b_cross_page"].append(
                    {"shortcode": c, "slugs": kept})

    # --- dup c) inbox: same slug + same code submitted more than once ---
    for (slug, code), n in inbox_seen.items():
        if n > 1:
            findings["dupes"]["c_inbox_reingest"].append(
                {"slug": slug, "shortcode": code, "count": n})

    # --- dup d) inbox: same code submitted to different slugs (auto-clears) ---
    for code, slugs in sorted(inbox_code_slugs.items()):
        if len(slugs) > 1:
            kept = filter_group(sorted(slugs), wiki, bio_cache, cleared)
            if kept:
                findings["dupes"]["d_inbox_cross_slug"].append(
                    {"shortcode": code, "slugs": kept})

    # _text is only needed internally; keep findings JSON light
    for info in wiki.values():
        info.pop("_text", None)

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
def render(findings, filtered_test):
    today = datetime.date.today().isoformat()
    L = []
    c = findings["counts"]
    L.append(f"# 照片投稿比對報告（{today}）\n")
    L.append(f"投稿列數：{c['new_submissions']}（已過濾測試列 {filtered_test} 筆）\n")

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
    ac = findings.get("auto_cleared", {})
    L.append("## 重複檢查")
    L.append("- a) 同頁 instagram: 區塊同碼>1：" + (
        "（無）" if not d["a_same_page"] else
        "；".join(f"`{x['slug']}` 的 {x['shortcode']}×{x['count']}" for x in d["a_same_page"])))
    L.append("- b) 同碼跨不同隻（複查，可能投錯隻）：" + (
        "（無）" if not d["b_cross_page"] else
        "；".join(f"{x['shortcode']} → {', '.join(x['slugs'])}" for x in d["b_cross_page"])))
    L.append("- c) 收件匣重投（同 slug+同碼）：" + (
        "（無）" if not d["c_inbox_reingest"] else
        "；".join(f"`{x['slug']}` 的 {x['shortcode']}×{x['count']}" for x in d["c_inbox_reingest"])))
    L.append("- d) 收件匣同碼投不同隻（複查）：" + (
        "（無）" if not d["d_inbox_cross_slug"] else
        "；".join(f"{x['shortcode']} → {', '.join(x['slugs'])}" for x in d["d_inbox_cross_slug"])))
    if ac.get("log") or ac.get("litter"):
        L.append(f"- 已自動放行（依 2026-08-07/08 裁定）：log 相關 {ac.get('log', 0)} 組、"
                 f"同生群 {ac.get('litter', 0)} 組")
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
    ap.add_argument("--submissions", required=True,
                    help="raw CSV/TSV dump of the Sheet, or legacy JSON rows")
    ap.add_argument("--wiki-dir", default="./wiki")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    rows = load_rows(args.submissions)

    kept = [r for r in rows if not is_test_row(r)]
    filtered = len(rows) - len(kept)

    if not os.path.isdir(args.wiki_dir):
        print(f"⚠️ 找不到 wiki 目錄：{args.wiki_dir}", file=sys.stderr)
        sys.exit(2)

    wiki = load_wiki(args.wiki_dir)
    findings = audit(kept, wiki)
    findings["_filtered_test_rows"] = filtered

    if args.json_out:
        slim = dict(findings)
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(slim, fh, ensure_ascii=False, indent=2)

    print(render(findings, filtered))


if __name__ == "__main__":
    main()
