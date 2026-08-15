#!/usr/bin/env python3
"""isb_audit.py — wiki × International Red Panda Studbook (ISB) 常設對帳。

取代一次性的 `sources/isb-red-panda/studbook_id-對帳-2026-08-09.csv`。
那份 CSV 是快照，wiki 一補新的 `studbook_id` 就過期（2026-08-14 實測：
CSV 記 285 筆，實際已能對上 335 筆），故改為每次重新解析、不落地中間檔。

**直接解析 `sources/isb-red-panda/ISB-2008.txt`（pdftotext -layout 的輸出），
不讀 register.csv。** 理由：register.csv 沒有 generator script、且已知漏 11 筆——
解析器碰到「生日欄＝`????`」（初代野生捕獲，園方連推定年都沒登録）
或「表頭行折行、事件跑到次行」就整筆丟掉。其中 8535（hoa-hoa-1982-06-15）
與 8856（chou-chou-1986）是 wiki 正在用、且是一大票個體的父母。

解析覆蓋率：本模組抽出 **2729 筆**，ISB 自己的 TOTALS 行寫 `1205.1233.292 (2730)`
（♂1205／♀1233／不詳292），即**少 1 筆 ♀**；register.csv 為 2703 筆。
那 1 筆的表頭行推測被 pdftotext 破壞到認不出來，尚未定位——**故本工具不是無損的**，
要主張「ISB 全簿查無某隻」時仍應回 `ISB-2008.txt` 或 PDF 原檔 grep 一次確認。

報告分段：
  §1 覆蓋率        層級 A/B/C/D
  §2 待裁定        生日／歿日／性別／亞種 與 ISB 不符
  §3 可補 sources  對得上 ISB 但條目未列 ISB 連結（層級 B）
  §4 親子對帳      ISB sire/dam vs 條目父/母行；ISB 子女 vs 條目子女表
  §5 番號候選      無 studbook_id、但（生日＋出生園＋性別）在 ISB 唯一命中

⚠️ 本工具「只讀、只報」：不動 wiki、不寫 DB、不碰 git。
   ISB 與 wiki 不符屬「待裁定」而非整合性錯誤（同 audit.py 的定位），
   故 **exit code 恆為 0**，掛進 verify.sh 也不會擋建置。

用法：
    python3 tools/isb_audit.py                 # 全段報告
    python3 tools/isb_audit.py --section 2     # 只看某段（1–5，可重複）
    python3 tools/isb_audit.py --md > out.md   # Markdown（表格化，供存 docs/）
    python3 tools/isb_audit.py --not-in-csv    # 只列尚未登記於 08-09 對帳 CSV 的
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_io import parse_frontmatter  # noqa: E402
from build_db import parse_family, official_sources  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
ISB_TXT = os.path.join(ROOT, "sources", "isb-red-panda", "ISB-2008.txt")
OLD_CSV = os.path.join(ROOT, "sources", "isb-red-panda",
                       "studbook_id-對帳-2026-08-09.csv")
OVERRIDES = os.path.join(ROOT, "data", "isb-overrides.json")

ISB_HOST_HINT = ("rotterdamzoo", "Red%20Panda%20Studbook", "Red Panda Studbook")

MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}

EVENTS = ("Birth", "Transfer", "Capture", "Release", "Death")

# 一筆紀錄的表頭：番號 性別 生日 父 母 [事件…]
#   生日三型：`17 Jun 1977` / `~ 1982` / `~ Jun 1994` / `????`
#   父母三型：番號 / WILD / UNK
# 生日四型：`17 Jun 1977` / `~17 Jun 2004`（推定精確日，波折號緊貼）/ `~ 1982`
#           `~ Jun 1994` / `????`
# ⚠️ 母番號後可能直接黏上園代碼（pdftotext 欄位撞行，如 `8318UTICA`），
#    故 dam 後用 lookahead 而非強制空白，否則整筆會被丟掉。
REC_RE = re.compile(
    r"^\s*(?P<stud>[A-Z]?\d{2,5})\s+"
    r"(?P<sex>[MF?])\s+"
    r"(?P<birth>\?{4}|~\s*(?:\d{1,2}\s+)?(?:\w{3}\s+)?\d{4}"
    r"|\d{1,2}\s+\w{3}\s+\d{4})\s+"
    r"(?P<sire>WILD|UNK|\d{2,5})\s+"
    r"(?P<dam>WILD|UNK|\d{2,5})(?=\s|[A-Z]|$)"
    r"(?P<rest>.*)$")

# 事件行（含表頭行的 rest）：園 日期 localID 事件 [名字] [地區簿] [亞種]
EV_RE = re.compile(
    r"^\s*(?P<inst>[A-Z][A-Z0-9 .'&/-]*?)?\s*"
    r"(?P<date>\?{4}|~\s*(?:\d{1,2}\s+)?(?:\w{3}\s+)?\d{4}"
    r"|\d{1,2}\s+\w{3}\s+\d{4})\s+"
    r"(?P<local>\S+)?\s*"
    r"(?P<ev>Birth|Transfer|Capture|Release|Death)"
    r"(?P<tail>.*)$")

TAXON_RE = re.compile(r"\b(styani|fulgens)\s*$")
# 地區血統簿尾段。⚠️ pdftotext 常把 local ID 與 `JAZGA` 黏成一串
#（如 `SHIC081-01JAZGA 288C`），故不加 \b 前界、且吃掉其後全部。
REGBOOK_RE = re.compile(r"(?:JAZGA?|AZA|ESB)\b.*$")
# 「名字」欄若含數字，幾乎都是 local ID 撞進來的碎片（如 `04`），不可當名字採用
NAME_UNRELIABLE_RE = re.compile(r"\d")


def norm_isb_date(raw: str):
    """→ (值, 是否推定)。`????` → (None, True)；`~ 1982` → ('1982', True)。"""
    raw = (raw or "").strip()
    if not raw or raw.startswith("?"):
        return None, True
    approx = raw.startswith("~")
    s = raw.lstrip("~").strip()
    m = re.match(r"^(\d{1,2})\s+(\w{3})\s+(\d{4})$", s)
    if m:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2)], int(m.group(1))), approx
    m = re.match(r"^(\d{1,2})\s+(\w{3})\s+(\d{4})$", s)   # 已由上式處理；保留防禦
    if m:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2)], int(m.group(1))), approx
    m = re.match(r"^(\w{3})\s+(\d{4})$", s)          # `~ Jun 1994`
    if m:
        return "%s-%02d" % (m.group(2), MONTHS[m.group(1)]), True
    m = re.match(r"^(\d{4})$", s)
    if m:
        return m.group(1), True
    return None, True


def _split_tail(tail: str):
    """事件行尾段 → (名字, 亞種)。名字欄常空；`JAZGA 136C` 是地區簿號不是名字。"""
    t = (tail or "").rstrip()
    taxon = None
    m = TAXON_RE.search(t)
    if m:
        taxon = m.group(1)
        t = t[:m.start()].rstrip()
    m = REGBOOK_RE.search(t)
    if m:
        t = t[:m.start()].rstrip()
    name = t.strip() or None
    if name and (NAME_UNRELIABLE_RE.search(name) or len(name) < 2):
        name = None          # local ID 碎片，不是名字
    return name, taxon


def parse_isb(path: str) -> dict:
    """→ {stud: {...}}。逐行掃；表頭行後的事件行歸屬前一筆。"""
    recs: dict[str, dict] = {}
    cur = None
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.replace("\f", " ").rstrip("\n")
        if not line.strip():
            continue
        if line.lstrip().startswith("[Death by:"):
            if cur:
                cause = line.strip()[len("[Death by:"):].rstrip("]").strip()
                cur["death_cause"] = re.sub(r"\s{2,}", " / ", cause)
            continue
        m = REC_RE.match(line)
        if m and not re.match(r"^\s*(TOTALS|Page)\b", line):
            stud = m.group("stud")
            birth, approx = norm_isb_date(m.group("birth"))
            cur = {
                "stud": stud, "sex": m.group("sex"),
                "birth": birth, "birth_approx": approx,
                "birth_raw": m.group("birth").strip(),
                "sire": m.group("sire"), "dam": m.group("dam"),
                "name": None, "taxon": None, "birth_inst": None,
                "death": None, "death_cause": None, "events": [],
            }
            recs[stud] = cur
            rest = m.group("rest") or ""
            if rest.strip():
                _absorb_event(cur, rest)
            continue
        if cur is not None:
            _absorb_event(cur, line)
    return recs


def _absorb_event(rec: dict, line: str) -> None:
    m = EV_RE.match(line)
    if not m:
        return
    date, _ = norm_isb_date(m.group("date"))
    ev = m.group("ev")
    inst = (m.group("inst") or "").strip() or None
    name, taxon = _split_tail(m.group("tail"))
    rec["events"].append({"inst": inst, "date": date, "ev": ev})
    if name and not rec["name"]:
        rec["name"] = name
    if taxon and not rec["taxon"]:
        rec["taxon"] = taxon
    if ev in ("Birth", "Capture") and inst and not rec["birth_inst"]:
        rec["birth_inst"] = inst
    if ev == "Death" and date:
        rec["death"] = date


def load_wiki() -> dict:
    out = {}
    for path in sorted(glob.glob(os.path.join(WIKI, "*.md"))):
        base = os.path.basename(path)
        if base in ("index.md", "log.md"):
            continue
        slug = base[:-3]
        text = open(path, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        srcs = list(fm.get("sources") or []) + list(fm.get("extra_sources") or [])
        out[slug] = {
            "slug": slug, "fm": fm, "body": body,
            "sid": str(fm.get("studbook_id") or "").strip() or None,
            "born": str(fm.get("born") or "").strip() or None,
            "died": str(fm.get("died") or "").strip() or None,
            "sex": (fm.get("sex") or "").strip().lower() or None,
            "species": (fm.get("species") or "").strip() or None,
            "zoos": list(fm.get("zoos") or []),
            "fam": parse_family(body),
            "cites_isb": any(h in str(u) for u in srcs for h in ISB_HOST_HINT),
        }
    return out


PARENT_LINE_RE = {
    "father": re.compile(r"^\s*[-*]\s*父[：:](.*)$", re.M),
    "mother": re.compile(r"^\s*[-*]\s*母[：:](.*)$", re.M),
}


def parent_line_raw(body: str, key: str):
    """回傳 `- 父：…` 行的原文（不含前綴），沒有則 None。

    用途：parse_family 只認 wikilink，父母寫成純文字（如 `父：Chun-Chun 🪽（RPF #733）`）
    或寫成**表格**時會回 None，但那是「漏做 wikilink → build_db 建不出親子邊」，
    跟「真的沒查到父母」是兩件完全不同的事，報告要分開講。
    """
    m = PARENT_LINE_RE[key].search(body)
    return m.group(1).strip() if m else None


def sex_letter(v):
    return {"female": "F", "male": "M"}.get(v)


def taxon_short(v):
    if not v:
        return None
    return "styani" if "styani" in v else ("fulgens" if "fulgens" in v else None)


def first_zoo(entry):
    """居住史首站園名（frontmatter zoos: 的最後一項＝最早，依既有慣例由前往後掃）。"""
    for z in entry["zoos"]:
        m = re.match(r"^\s*(.+?)\s*[（(]", str(z))
        if m:
            return m.group(1).strip()
    return None


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--section", action="append", type=int, default=None)
    ap.add_argument("--md", action="store_true")
    ap.add_argument("--not-in-csv", action="store_true")
    args = ap.parse_args()
    want = set(args.section or [1, 2, 3, 4, 5])

    isb = parse_isb(ISB_TXT)
    wiki = load_wiki()

    # 已裁定清單：{(stud, field): 該筆裁定}。用 JSON 而非 YAML —— data/ 全是 JSON，
    # 且本 repo 的 frontmatter parser 刻意不依賴 PyYAML，不為一個小檔引進新相依。
    ov, ov_pending = {}, []
    if os.path.exists(OVERRIDES):
        import json
        with open(OVERRIDES, encoding="utf-8") as f:
            data = json.load(f)
        for r in data.get("resolved", []):
            if r.get("verdict") in ("wiki", "isb"):
                ov[(str(r["stud"]), r["field"])] = r
        ov_pending = data.get("pending", [])

    old = set()
    if os.path.exists(OLD_CSV):
        with open(OLD_CSV, encoding="utf-8") as f:
            old = {r["studbook_id"] for r in csv.DictReader(f)}

    # ISB 反向索引：某番號的子女
    kids = defaultdict(list)
    for r in isb.values():
        for p in (r["sire"], r["dam"]):
            if p and p not in ("WILD", "UNK"):
                kids[p].append(r["stud"])

    sid2slug = {e["sid"]: s for s, e in wiki.items() if e["sid"]}

    A, B, C, D = [], [], [], []
    for slug, e in sorted(wiki.items()):
        if e["sid"] and e["sid"] in isb:
            (A if e["cites_isb"] else B).append(slug)
        elif e["sid"]:
            C.append(slug)
        else:
            D.append(slug)

    P = print
    h1 = (lambda s: P("\n## " + s + "\n")) if args.md else (lambda s: P("\n" + s + "\n" + "=" * 60))
    h2 = (lambda s: P("\n### " + s + "\n")) if args.md else (lambda s: P("\n-- " + s))

    if args.md:
        P("# ISB 對帳報告（tools/isb_audit.py）\n")
        P("資料源：`sources/isb-red-panda/ISB-2008.txt`（收錄至 2008-12-31）")
        P("本報告由工具即時產生，勿手改；重跑即更新。\n")

    if 1 in want:
        h1("§1 覆蓋率")
        rows = [
            ("A", "對得上 ISB，且條目 sources 已列 ISB", len(A)),
            ("B", "對得上 ISB，但條目未列 ISB", len(B)),
            ("C", "有 studbook_id，ISB 2008 查無（多為 2009+ 出生）", len(C)),
            ("D", "無 studbook_id", len(D)),
        ]
        if args.md:
            P("| 層級 | 定義 | 筆數 |\n|---|---|---|")
            for k, d, n in rows:
                P(f"| {k} | {d} | {n} |")
            P(f"| | **A+B ＝ 已與 ISB 逐欄對過** | **{len(A)+len(B)}** |")
            P(f"| | 條目總數 | {len(wiki)} |")
        else:
            for k, d, n in rows:
                P(f"  {k}  {d:<46} {n:>4}")
            P(f"      {'A+B ＝ 已與 ISB 逐欄對過':<46} {len(A)+len(B):>4}")
            P(f"      {'條目總數':<46} {len(wiki):>4}")
        P(f"\nISB 解析到 {len(isb)} 筆紀錄（ISB TOTALS 行為 2730，差 1 筆 ♀ 未定位；"
          "見本檔 docstring——主張『ISB 查無』前請回原檔確認）。")
        newly = sorted(s for s in (A + B) if wiki[s]["sid"] not in old)
        if old:
            P(f"其中 {len(newly)} 筆尚未登記於 08-09 對帳 CSV（該 CSV 有 {len(old)} 筆，已過期）。")
        if args.not_in_csv or (newly and 1 in want):
            h2(f"尚未登記於舊 CSV 的 {len(newly)} 筆")
            for s in newly:
                r = isb[wiki[s]["sid"]]
                P(f"  {wiki[s]['sid']:<7} {s:<32} ISB born={r['birth_raw']:<12} died={r['death'] or '—'}")

    if 2 in want:
        h1("§2 待裁定：與 ISB 不符")
        buckets = defaultdict(list)
        settled = []

        def is_settled(sid, field):
            r = ov.get((sid, field))
            if r:
                settled.append((sid, field, r))
                return True
            return False

        for slug in A + B:
            e, r = wiki[slug], isb[wiki[slug]["sid"]]
            sid = e["sid"]
            if e["born"] and r["birth"] and not is_settled(sid, "birth"):
                if r["birth_approx"]:
                    if e["born"][:4] != r["birth"][:4]:
                        buckets["生日（ISB 為推定值，多為野生捕獲的登録年 vs 推定生年，通常非衝突）"].append(
                            (sid, slug, e["born"], r["birth_raw"]))
                elif len(e["born"]) == 4 and len(r["birth"]) == 10:
                    # wiki 只到年、ISB 有精確日 → 不是衝突，是可精確化
                    if e["born"] != r["birth"][:4]:
                        buckets["生日"].append((sid, slug, e["born"], r["birth_raw"]))
                    else:
                        buckets["生日（wiki 只到年，ISB 有精確日，可補）"].append(
                            (sid, slug, e["born"], r["birth_raw"]))
                elif len(r["birth"]) == 10 and e["born"] != r["birth"]:
                    buckets["生日"].append((sid, slug, e["born"], r["birth_raw"]))
            if (e["died"] and r["death"] and e["died"] != r["death"]
                    and not is_settled(sid, "death")):
                buckets["歿日"].append((sid, slug, e["died"], r["death"]))
            ws, rs = sex_letter(e["sex"]), r["sex"]
            if ws and rs and rs != "?" and ws != rs and not is_settled(sid, "sex"):
                # ⚠️ 既有裁定：ISB 的幼獸性別視為「出生時暫記」，不據此改 wiki
                #    （見 docs/ISB-2008-對帳-2026-08-09.md §4 與 0438／0500 兩例）。
                #    多數本段項目應已裁定過，此處列出僅供覆核，非待辦。
                buckets["性別（⚠️ ISB 幼獸性別視為出生時暫記，既有裁定為不改 wiki）"].append(
                    (sid, slug, ws, rs))
            wt, rt = taxon_short(e["species"]), r["taxon"]
            if wt and rt and wt != rt and not is_settled(sid, "taxon"):
                buckets["亞種"].append((sid, slug, wt, rt))
        if not buckets:
            P("  （無）")
        for k in sorted(buckets):
            h2(f"{k}：{len(buckets[k])} 筆")
            if args.md:
                P("| ISB | slug | wiki | ISB |\n|---|---|---|---|")
                for sid, slug, w, i in buckets[k]:
                    P(f"| `{sid}` | `{slug}` | {w} | **{i}** |")
            else:
                for sid, slug, w, i in buckets[k]:
                    P(f"  {sid:<7} {slug:<32} wiki={w:<12} ISB={i}")
        if settled:
            h2(f"已裁定、不再列入待辦：{len(settled)} 筆（見 data/isb-overrides.json）")
            for sid, field, r in settled:
                P(f"  {sid:<7} {field:<6} 採{r['verdict']}：{r['why'][:70]}")

    if 3 in want:
        h1(f"§3 可補 sources：對得上 ISB 但條目未列（{len(B)} 筆）")
        P("補進 frontmatter `sources:` 即可——`rotterdamzoo.nl` 同時在 OFFICIAL_HOSTS 與")
        P("NON_PUBLIC_HOSTS，故 has_official_source 轉 true，但個體頁不會顯示該連結。\n")
        for i in range(0, len(B), 4):
            P("  " + "  ".join(f"{wiki[s]['sid']:>6} {s:<28}" for s in B[i:i + 4]).rstrip())

    if 4 in want:
        h1("§4 親子對帳")
        pmis, cmis, psettled = [], [], []
        for slug in A + B:
            e, r = wiki[slug], isb[wiki[slug]["sid"]]
            for role, key, num in (("父", "father", r["sire"]), ("母", "mother", r["dam"])):
                if num in ("WILD", "UNK") or not num:
                    continue
                dec = ov.get((e["sid"], "sire" if key == "father" else "dam"))
                if dec:
                    psettled.append((e["sid"], slug, role, dec))
                    continue
                exp = sid2slug.get(num)
                got = e["fam"].get(key)
                if exp and got and exp != got:
                    pmis.append((e["sid"], slug, role, got, f"{num} {exp}", "不符"))
                elif exp and not got:
                    raw = parent_line_raw(e["body"], key)
                    expname = str(wiki[exp]["fm"].get("name") or "")
                    if raw and expname and expname.lower() in raw.lower():
                        kind = "未做成 wikilink"
                        shown = raw[:40]
                    elif raw:
                        kind = "行存在但無連結"
                        shown = raw[:40]
                    else:
                        kind = "條目未記"
                        shown = "—"
                    pmis.append((e["sid"], slug, role, shown, f"{num} {exp}", kind))
            isb_kids = kids.get(e["sid"], [])
            if not isb_kids:
                continue
            listed = set(e["fam"].get("children") or [])
            miss = []
            for k in isb_kids:
                ks = sid2slug.get(k)
                if ks and ks in listed:
                    continue
                if ks:
                    miss.append(f"{k}→{ks}（有條目卻未列）")
                elif f"`{k}`" in e["body"] or k in e["body"]:
                    continue          # 無條目但內文已敘述（多為未命名夭折）
                else:
                    kr = isb[k]
                    miss.append(f"{k}（{kr['birth'] or '?'}，歿 {kr['death'] or '—'}）")
            if miss:
                cmis.append((e["sid"], slug, len(isb_kids), miss))
        by_kind = defaultdict(list)
        for row in pmis:
            by_kind[row[5]].append(row)
        NOTE = {
            "不符": "條目與 ISB 指向不同個體 → 需裁定",
            "未做成 wikilink": "⚠️ 父母寫成純文字或表格，build_db 只讀 `- 父：[[…]]` → "
                               "**這些條目目前根本沒有親子邊**，血緣圖與近親偵測都漏算",
            "行存在但無連結": "父／母行有寫，但抓不到 wikilink，需人工看一眼",
            "條目未記": "ISB 有父母、條目完全沒記 → 可補",
        }
        for kind in ("不符", "未做成 wikilink", "行存在但無連結", "條目未記"):
            rows = by_kind.get(kind) or []
            if not rows:
                continue
            h2(f"父／母：{kind}（{len(rows)} 筆）— {NOTE[kind]}")
            for sid, slug, role, got, exp, _ in rows:
                P(f"  {sid:<7} {slug:<32} {role}：條目={got:<40} ISB={exp}")
        if psettled:
            h2(f"父／母：已裁定、不再列入待辦（{len(psettled)} 筆）")
            for sid, slug, role, dec in psettled:
                P(f"  {sid:<7} {slug:<32} {role}：採{dec['verdict']}（ISB={dec['isb']} / wiki={dec['wiki']}）")
        h2(f"子女表漏 ISB 有載的：{len(cmis)} 筆")
        for sid, slug, tot, miss in cmis:
            P(f"  {sid:<7} {slug:<32} ISB 記 {tot} 隻，缺 {len(miss)}：")
            for m in miss:
                P(f"          - {m}")

    if 5 in want:
        h1("§5 番號候選：無 studbook_id，但（生日＋出生園＋性別）在 ISB 唯一命中")
        # 由已確認的 A+B 自舉出 ISB 園代碼 → wiki canonical 園名
        code2zoo = defaultdict(lambda: defaultdict(int))
        for slug in A + B:
            e, r = wiki[slug], isb[wiki[slug]["sid"]]
            z = first_zoo(e)
            if r["birth_inst"] and z:
                code2zoo[r["birth_inst"]][z] += 1
        # ⚠️ CHINA／ASIA 等不是動物園，是「野生捕獲來源地」，會對到一堆不相干的園；
        #    另有真歧義（OKAYAMA 同時對到池田動物園與とべ）。兩者都必須排除，
        #    否則 §5 會憑錯誤的園對應給出假命中。
        PSEUDO = {"CHINA", "ASIA", "WILD", "NONE", "UNK", "UNKNOWN"}
        code_of, dropped, thin = {}, [], set()
        for code, cnt in code2zoo.items():
            if code in PSEUDO:
                dropped.append((code, "非動物園（野生來源地）"))
                continue
            ranked = sorted(cnt.items(), key=lambda kv: -kv[1])
            top, n1 = ranked[0]
            n2 = ranked[1][1] if len(ranked) > 1 else 0
            # 只對到一個園 → 無歧義（即使只有 1 筆佐證，標 thin 供覆核）；
            # 對到多園 → 要求首位有壓倒性優勢，否則排除。
            if len(ranked) > 1 and n1 < 2 * n2:
                dropped.append((code, f"對應不明確 {dict(cnt)}"))
                continue
            code_of[code] = top
            if n1 == 1:
                thin.add(code)
        P(f"  由 {len(A)+len(B)} 筆已確認紀錄自舉出 {len(code_of)} 個可信的 ISB 園代碼對應"
          f"（另排除 {len(dropped)} 個）。")
        for code, why in sorted(dropped):
            P(f"    排除 {code:<12} {why}")
        P("")
        used = set(sid2slug)
        by_key = defaultdict(list)
        for r in isb.values():
            if r["stud"] in used or not r["birth"] or len(r["birth"]) != 10:
                continue
            zoo = code_of.get(r["birth_inst"])
            if zoo:
                by_key[(r["birth"], zoo, r["sex"])].append(r["stud"])
        P("  信心標記：`名`＝ISB 名字欄與 slug 相符（最強）｜"
          "`thin`＝該園代碼只有 1 筆佐證，園對應本身待覆核\n")
        hits = []
        for slug in D:
            e = wiki[slug]
            z, sx = first_zoo(e), sex_letter(e["sex"])
            if not (e["born"] and len(e["born"]) == 10 and z and sx):
                continue
            cand = by_key.get((e["born"], z, sx), [])
            if len(cand) == 1:
                r = isb[cand[0]]
                flags = []
                base = re.split(r"-\d{4}", slug)[0].replace("-", "")
                if r["name"] and r["name"].lower().replace("-", "") == base.lower():
                    flags.append("名")
                if r["birth_inst"] in thin:
                    flags.append("thin")
                hits.append((slug, cand[0], e["born"], z, r["name"] or "—",
                             r["death"] or "—", ",".join(flags) or "-"))
        P(f"  唯一命中 {len(hits)} 筆（仍須人工核對移動史／歿日後才可寫入 studbook_id）：\n")
        for slug, sid, born, zoo, nm, dd, fl in hits:
            P(f"  [{fl:<8}] {slug:<30} → ISB {sid:<7} {born}  {zoo:<22} ISB名={nm:<10} 歿={dd}")

    if ov_pending:
        h1(f"⏳ 已知缺漏、尚未處理（{len(ov_pending)} 項，來自 data/isb-overrides.json）")
        for r in ov_pending:
            P(f"  [{r.get('date','')}] {r.get('what','')}")
            for line in re.findall(r".{1,88}(?:\s|$)", r.get("detail", "")):
                if line.strip():
                    P(f"        {line.strip()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
