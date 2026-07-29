#!/usr/bin/env python3
"""
build_db.py — Red Panda Wiki → SQLite

從 wiki/*.md 解析 YAML frontmatter + 家族 section，
輸出 redpanda.db（SQLite）。

使用方式：
    cd red-panda-wiki/
    python tools/build_db.py

每次新增 wiki 條目後重跑即可更新 DB。
"""

from __future__ import annotations  # 相容舊版 Python（str | None 等延後解析）

import os
import re
import json
import sqlite3
import sys
from pathlib import Path

# ── 路徑設定 ──────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).parent
WIKI_DIR    = SCRIPT_DIR.parent / "wiki"
SCHEMA_FILE = SCRIPT_DIR / "schema.sql"
# 優先嘗試放在 tools/ 旁；若掛載資料夾不支援 SQLite（如 Cowork sandbox），
# 自動 fallback 到 /tmp/redpanda.db
DB_PATH     = SCRIPT_DIR.parent / "redpanda.db"
DB_FALLBACK = Path("/tmp/redpanda.db")

# ── YAML frontmatter parser：共用實作在 tools/wiki_io.py ────────
# （re-export 供 check_twins.py 等既有 `from build_db import parse_frontmatter` 使用）
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_io import parse_frontmatter  # noqa: E402


# ── 官方來源分類器（個體頁只顯示官方連結）──────────────────────
# 政策（作者裁定 2026-07-07，最嚴）：個體頁的「來源」區塊只顯示園方官網／政府
# （自治體）公告／園報／中國園官方微信公眾號。RPF、redpanda-lineage、個人部落格、
# 新聞媒體、社群貼文、wiki、web.archive 等一律不顯示（仍保留在 frontmatter sources
# 供校訂與稽核，只是不對外呈現）。
#
# 判定＝白名單 host（精確比對，去掉開頭 www.）＋政府網域 pattern。名單外一律非官方。
# ⚠️ 日後新增園方官網時，把 host 補進 OFFICIAL_HOSTS 即會自動顯示。
OFFICIAL_HOSTS = {
    # 日本園方官網／營運協會
    "tokyo-zoo.net", "nhdzoo.jp", "tohoku-safaripark.co.jp", "tobezoo.com",
    "asazoo.jp", "omutacityzoo.org", "hama-midorinokyokai.or.jp",
    "kobe-ojizoo.jp", "ojizoo.jp",  # 神戸市立王子動物園（現行官網＋舊官方網域）
    "tennojizoo.jp",  # 天王寺動物園（含園報《なきごえ》/nakigoe/ 與 ZOO DIARY，官方一手）
    "hirakawazoo.jp",  # 鹿児島市平川動物公園（含園方「飼育員の日記」等 staff blog）
    # 日本自治體（園區隸屬市府）
    "city.ichikawa.lg.jp", "city.asahikawa.hokkaido.jp", "city.kawasaki.jp",
    "soumu.metro.tokyo.lg.jp", "city.sapporo.jp",  # 札幌市円山動物園
    # 台灣／港澳
    "zoo.gov.taipei", "gov.taipei", "macaotourism.gov.mo", "gcs.gov.mo",
    # 中國園方官網／官方微信公眾號（無官網者以微信文章為官方，見 CLAUDE.md）
    "shanghaizoo.cn", "nbzoo.com", "shwzoo.com", "enjoyland.cn",
    "swap-shendi.com", "lyhylj.liuzhou.gov.cn", "mp.weixin.qq.com",
    "wuhanzoo.com.cn",
    # 小紅書：園方官方帳號亦於此發布（如柳州動物園）。與微信同為共用平台、整域列入，
    # ⚠️ sources 只放官方帳號貼文；粉絲轉載請勿放 sources（會被誤判官方）。xhslink 為短連結轉址域。
    "xiaohongshu.com", "xhslink.com",
    # 其他國家園方官網
    "drusillas.co.uk", "witheverland.com", "chiangmai.zoothailand.org", "sriayuthayalionpark.com",
}

# Facebook 是共用網域，不能整域列白名單（旅遊/粉絲轉載粉專也在同域）。
# 僅認「園方/機構官方專頁」——比對 URL 路徑第一段（vanity 或數字 page id）。
# 新增官方園方 FB 專頁時，把其 vanity（小寫）補進這裡即會自動顯示。
OFFICIAL_FB_PAGES = {
    "thecalgaryzoo",   # The Calgary Zoo 官方專頁（page id 100064839398464）
    "zounokuni",       # ぞうの国 官方專頁
}
_FB_HOSTS = {"facebook.com", "m.facebook.com", "web.facebook.com", "fb.com"}

# X（舊 Twitter）同為共用網域，比照 Facebook 只認「園方官方帳號」——比對 URL 路徑
# 第一段的 handle（小寫、不含 @）。多數日本園以 X 為主要公告管道（出生・命名・雌雄
# 鑑定・訃報常只發在這裡），故列為官方來源。
# ⚠️ 只放園方自己的帳號；粉絲／個人拍攝帳號請勿加入（會被誤判官方）。
OFFICIAL_X_ACCOUNTS = {
    "nishiyama_zoo",    # 鯖江市西山動物園
    "nhdzoo",           # 静岡市立日本平動物園（同 nhdzoo.jp）
    "ichikawa_zoo",     # 市川市動植物園（同 city.ichikawa.lg.jp）
    "kumamotocityzoo",  # 熊本市動植物園（ezooko.jp）
}
_X_HOSTS = {"x.com", "twitter.com", "mobile.twitter.com", "mobile.x.com"}

# Instagram 同為共用網域，比照 X／FB 只認「園方官方帳號」——比對 URL 路徑第一段的
# 帳號（小寫、不含 @）。⚠️ 僅認含帳號的完整形式 /帳號/p/XXXX/；IG「複製連結」給的
# 短形式 /p/XXXX/ 無從判斷發文者，一律視為非官方（sources 請存完整形式）。
# ⚠️ 只放園方自己的帳號；同好／個人拍攝帳號請勿加入（會被誤判官方）。
OFFICIAL_IG_ACCOUNTS = {
    "kumamoto_doushokubutsuen",  # 熊本市動植物園（ezooko.jp）
}
_IG_HOSTS = {"instagram.com", "m.instagram.com"}
_IG_NON_ACCOUNT_SEGS = {"p", "reel", "reels", "tv", "stories", "explore"}

def _host(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).netloc.lower().split("@")[-1].split(":")[0].removeprefix("www.") \
        if "//" in url else ""

def is_official_source(url: str) -> bool:
    """僅園方官網／政府公告／園報／官方微信視為官方。名單外＋非 gov pattern＝False。"""
    if not isinstance(url, str) or not url.startswith("http"):
        return False
    host = _host(url)
    if not host:
        return False
    if host in OFFICIAL_HOSTS:
        return True
    # Facebook：僅特定園方/機構官方專頁（比對路徑第一段 vanity / page id）
    if host in _FB_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower()
        return seg in OFFICIAL_FB_PAGES
    # X（Twitter）：僅特定園方官方帳號（比對路徑第一段 handle）
    if host in _X_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower().lstrip("@")
        return seg in OFFICIAL_X_ACCOUNTS
    # Instagram：僅特定園方官方帳號（比對路徑第一段帳號；短形式 /p/… 不算官方）
    if host in _IG_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower().lstrip("@")
        if seg in _IG_NON_ACCOUNT_SEGS:
            return False
        return seg in OFFICIAL_IG_ACCOUNTS
    # 政府網域 pattern（未來新自治體/政府站自動涵蓋）
    # ⚠️ 這條也涵蓋 J-STAGE（jstage.jst.go.jp）。園方自行編輯登載的《安佐動物公園飼育記録集》
    # （https://www.jstage.jst.go.jp/article/asazoo/…，Online ISSN 2759-6567）即靠這條被認列為
    # 官方園報，符合 CLAUDE.md「園報視為官方」。副作用：J-STAGE 上**其他**期刊（非園方編輯的
    # 學術論文）也會被判為官方；日後若要收緊，改成只認 /article/asazoo/ 等園方刊物路徑。
    if host.endswith((".lg.jp", ".go.jp", ".gov", ".gov.tw", ".gov.cn",
                      ".gov.mo", ".gov.taipei")):
        return True
    if ".gov." in host:
        return True
    return False

def official_sources(sources_raw) -> list[str]:
    if not sources_raw:
        return []
    if isinstance(sources_raw, str):
        sources_raw = [sources_raw]
    seen, out = set(), []
    for u in sources_raw:
        u = (u or "").strip()
        if u and is_official_source(u) and u not in seen:
            seen.add(u); out.append(u)
    return out


# ── Wikilink 抽取 ─────────────────────────────────────────────
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")

def extract_wikilinks(text: str) -> list[str]:
    """取出所有 [[slug]] 中的 slug，並正規化為 kebab-lowercase。"""
    return [m.group(1).strip().lower() for m in WIKILINK_RE.finditer(text)]

def first_wikilink(text: str) -> str | None:
    m = WIKILINK_RE.search(text)
    return m.group(1).strip().lower() if m else None

# 消歧警語標記：父/母 行常見「（⚠️ 勿與 [[另一隻]] 混淆）」。這些警語裡的
# wikilink 不是父母本身，必須在抽取父母前切掉，否則 first_wikilink 會誤抓警語連結。
WARNING_RE = re.compile(r"⚠|勿與|請勿與|不要與|混淆|注意同名|不同個體")

def parent_link(text: str) -> str | None:
    """從 父/母 行取真正的父母 slug：先切掉消歧警語子句再取第一個 wikilink。
    若真正父母以純文字書寫（無條目），切掉警語後即無連結 → 回 None（不建錯邊）。"""
    head = WARNING_RE.split(text, maxsplit=1)[0]
    return first_wikilink(head)


# ── 家族 section 解析 ─────────────────────────────────────────
def parse_family(body: str) -> dict:
    """
    回傳:
        mother: str | None
        father: str | None
        twins:  list[str]
        children: list[str]   ← 從子女 table 抽取
    """
    result = {"mother": None, "father": None, "twins": [], "children": []}

    # 找 ## 家族 或 ## 家族關係 section
    section_re = re.compile(r"^##\s+家族", re.MULTILINE)
    m = section_re.search(body)
    if not m:
        return result
    section_text = body[m.start():]

    # section 結束於下一個 ## （非 ###）
    next_section = re.search(r"\n##\s+(?!#)", section_text[3:])
    if next_section:
        section_text = section_text[: next_section.start() + 3]

    # --- 解析每一行 ---
    in_children_table = False
    for line in section_text.splitlines():
        stripped = line.strip()

        # 進入子女表格
        if re.match(r"^#{2,3}\s+子女", stripped):
            in_children_table = True
            continue

        # 離開子女表格（碰到另一個 header 或非表格行後不再是 table）
        if stripped.startswith("#") and not re.match(r"^#{2,3}\s+子女", stripped):
            in_children_table = False

        # 子女 table row（以 | [[ 開頭的行）
        if in_children_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            if cells:
                child = first_wikilink(cells[0])
                if child:
                    result["children"].append(child)
            continue

        # 母
        if re.match(r"^-\s*母[：:]", stripped):
            result["mother"] = parent_link(stripped)
            continue

        # 父
        if re.match(r"^-\s*父[：:]", stripped):
            result["father"] = parent_link(stripped)
            continue

        # 多胞胎（雙胞胎／三胞胎／四胞胎…，可能有多人，取所有 wikilinks）
        # 也匹配「雙胞胎姊妹：」「三胞胎兄弟：」「三胞胎妹妹：」等變體
        # 同一資料模型存為兩兩配對；網站再依同生群人數決定顯示「雙胞胎／三胞胎…」
        # 數字開頭者（如「2013 雙胞胎：」）屬「子女」區描述其子女的同生群，不算本人的，故排除
        if re.match(r"^-\s*[二兩雙三四五六]胞胎[^：:]{0,4}[：:]", stripped):
            # 先去除消歧義／警語註記裡的 wikilink（如「⚠️ 非 [[X]] 亦非 [[Y]]」），
            # 那是在說明「不是這幾隻」，不可當成同生群成員
            cleaned = re.sub(r"[（(][^（）()]*[非⚠][^（）()]*[）)]", "", stripped)
            cleaned = re.sub(r"(?:亦)?非\s*\[\[[^\]]+\]\]", "", cleaned)
            result["twins"].extend(extract_wikilinks(cleaned))

    return result


# ── 居住史解析（從 YAML zoos 欄位，唯一事實來源）──────────────
# 格式：「<園名> (<起> – <訖>)」；起訖可為 YYYY-MM-DD / YYYY / 現在(訖留空)
ZOO_RANGE_RE = re.compile(
    r"^(.+?)\s*[（(]\s*"
    r"((?:\d{4}-\d{2}-\d{2})|(?:\d{4}))?\s*[–—~〜-]\s*"
    r"((?:\d{4}-\d{2}-\d{2})|(?:\d{4})|現在|今)?\s*[）)]\s*$")

def _ymd(s):
    if not s:
        return (None, None)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return (s, int(s[:4]))
    if re.fullmatch(r"\d{4}", s):
        return (None, int(s))
    return (None, None)

def parse_zoos(zoos_raw) -> list[dict]:
    """YAML zoos 欄位（字串列表）→ [{zoo_name, start_year, end_year, start_date, end_date}, ...]"""
    if not zoos_raw:
        return []
    if isinstance(zoos_raw, str):
        zoos_raw = [zoos_raw]
    results = []
    for entry in zoos_raw:
        entry = entry.strip()
        m = ZOO_RANGE_RE.match(entry)
        if m:
            zoo_name = m.group(1).strip()
            sd, sy = _ymd(m.group(2))
            end_raw = m.group(3)
            ed, ey = (None, None) if (not end_raw or end_raw in ("現在", "今")) else _ymd(end_raw)
            results.append({"zoo_name": zoo_name, "start_year": sy, "end_year": ey,
                            "start_date": sd, "end_date": ed})
        else:
            # 無括號日期，至少記下動物園名
            results.append({"zoo_name": entry, "start_year": None, "end_year": None,
                            "start_date": None, "end_date": None})
    return results


# ── 主流程 ────────────────────────────────────────────────────
def species_short(species_str: str | None) -> str | None:
    if not species_str:
        return None
    if "styani" in species_str:
        return "styani"
    if "fulgens" in species_str:
        return "fulgens"
    return species_str


def build_db():
    md_files = sorted(WIKI_DIR.glob("*.md"))
    skip = {"index.md", "log.md"}
    md_files = [f for f in md_files if f.name not in skip]

    print(f"找到 {len(md_files)} 個 wiki 條目")

    # ── 初始化 DB ──────────────────────────────────────────────
    # 嘗試主路徑，失敗時 fallback 到 /tmp
    actual_db = DB_PATH
    try:
        if actual_db.exists():
            actual_db.unlink()
        conn = sqlite3.connect(actual_db)
        conn.execute("CREATE TABLE _test (x)")
        conn.execute("DROP TABLE _test")
    except Exception:
        actual_db = DB_FALLBACK
        if actual_db.exists():
            actual_db.unlink()
        conn = sqlite3.connect(actual_db)
        print(f"  ℹ️  掛載資料夾不支援 SQLite，改用: {actual_db}")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    with open(SCHEMA_FILE, encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()

    # ── Pass 1：插入 pandas 基本資料 ──────────────────────────
    all_slugs: set[str] = set()
    panda_rows: list[dict] = []
    declared_sib_raw: dict[str, list[str]] = {}  # slug -> frontmatter siblings 列出的 slug

    for md_path in md_files:
        slug = md_path.stem.lower()
        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        if not fm.get("name"):
            print(f"  ⚠️  跳過（無 name）: {md_path.name}")
            continue

        sex_raw = fm.get("sex", "")
        if sex_raw in ("female", "male"):
            sex = sex_raw
        else:
            sex = "unknown"

        tags_raw = fm.get("tags", [])
        if isinstance(tags_raw, str):
            tags_raw = [tags_raw]

        nicknames = fm.get("nicknames", [])
        if isinstance(nicknames, str):
            nicknames = [nicknames]

        english_variants = fm.get("english_variants", [])
        if isinstance(english_variants, str):
            english_variants = [english_variants]

        instagram = fm.get("instagram", [])
        if isinstance(instagram, str):
            instagram = [instagram]

        extra_sources = fm.get("extra_sources", [])
        if isinstance(extra_sources, str):
            extra_sources = [extra_sources]

        # 韓文名可為單值或多值（list）；正規化為以逗號分隔的字串（比照 japanese 多值寫法）
        korean = fm.get("korean")
        if isinstance(korean, list):
            korean = ", ".join(str(x) for x in korean) if korean else None

        row = {
            "slug":             slug,
            "name":             fm.get("name", ""),
            "japanese":         fm.get("japanese"),
            "korean":           korean,
            "chinese":          fm.get("chinese"),
            "nicknames":        json.dumps(nicknames, ensure_ascii=False) if nicknames else None,
            "english_variants": json.dumps(english_variants, ensure_ascii=False) if english_variants else None,
            "sex":              sex,
            "born":             fm.get("born"),
            "died":             fm.get("died"),
            "last_seen":        fm.get("last_seen"),
            "species":          species_short(fm.get("species")),
            "rpf_id":           int(fm["rpf_id"]) if fm.get("rpf_id") else None,
            "rpf_url":          fm.get("rpf_url"),
            "tags":             json.dumps(tags_raw, ensure_ascii=False),
            "instagram":        json.dumps(instagram, ensure_ascii=False) if instagram else None,
            "is_alive":         0 if fm.get("died") else 1,
            "sources":          json.dumps(official_sources(fm.get("sources")), ensure_ascii=False),
            "extra_sources":    json.dumps(extra_sources, ensure_ascii=False) if extra_sources else None,
        }
        panda_rows.append((slug, body, row))
        all_slugs.add(slug)

        # 已宣告手足（父母不詳、無法由共同父母推導時使用）；正規化為 kebab-lowercase
        siblings_raw = fm.get("siblings", [])
        if isinstance(siblings_raw, str):
            siblings_raw = [siblings_raw]
        if siblings_raw:
            declared_sib_raw[slug] = [str(s).strip().lower() for s in siblings_raw if str(s).strip()]

    cur.executemany("""
        INSERT OR REPLACE INTO pandas
          (slug, name, japanese, korean, chinese, nicknames, english_variants,
           sex, born, died, last_seen, species, rpf_id, rpf_url, tags, instagram, is_alive, sources, extra_sources)
        VALUES
          (:slug,:name,:japanese,:korean,:chinese,:nicknames,:english_variants,
           :sex,:born,:died,:last_seen,:species,:rpf_id,:rpf_url,:tags,:instagram,:is_alive,:sources,:extra_sources)
    """, [r for _, _, r in panda_rows])
    conn.commit()
    print(f"  ✅ 插入 {len(panda_rows)} 筆個體資料")

    # ── Pass 2：解析家族關係 ───────────────────────────────────
    parent_child_rows: list[tuple] = []   # (child, parent, type)
    twin_pairs: set[frozenset] = set()
    child_rows: list[tuple] = []          # (parent_slug, child_slug) from 子女 table

    for slug, body, _ in panda_rows:
        fam = parse_family(body)

        # 母
        if fam["mother"] and fam["mother"] in all_slugs:
            parent_child_rows.append((slug, fam["mother"], "mother", "confirmed"))

        # 父
        if fam["father"] and fam["father"] in all_slugs:
            parent_child_rows.append((slug, fam["father"], "father", "confirmed"))

        # 雙胞胎
        for twin in fam["twins"]:
            if twin in all_slugs and twin != slug:
                pair = frozenset([slug, twin])
                twin_pairs.add(pair)

        # 子女（從 table 抽取）→ 反向變成 parent_child
        for child_slug in fam["children"]:
            if child_slug in all_slugs and child_slug != slug:
                child_rows.append((slug, child_slug))

    # 子女 table 的關係：知道的是 parent_slug 是誰，child_slug 是誰，
    # 但不知道是 mother 還是 father → 看 parent 的 sex
    slug_to_sex = {slug: row["sex"] for slug, _, row in panda_rows}
    for parent_slug, child_slug in child_rows:
        ptype = "mother" if slug_to_sex.get(parent_slug) == "female" else \
                "father"  if slug_to_sex.get(parent_slug) == "male"   else None
        if ptype:
            rec = (child_slug, parent_slug, ptype, "confirmed")
            if rec not in parent_child_rows:
                parent_child_rows.append(rec)

    # 去重
    parent_child_unique = list({(c,p,t): (c,p,t,conf)
                                 for c,p,t,conf in parent_child_rows}.values())

    cur.executemany("""
        INSERT OR IGNORE INTO parent_child (child_slug, parent_slug, parent_type, confidence)
        VALUES (?,?,?,?)
    """, parent_child_unique)
    conn.commit()
    print(f"  ✅ 插入 {len(parent_child_unique)} 筆親子關係")

    # 多胞胎為「群」屬性：取連通分量的傳遞閉包，補上群內所有兩兩配對。
    # （即使各條目未互相完整列出，例如三胞胎中 Chao 列了 Ren、Nana，
    #   但 Ren／Nana 只列 Chao，仍能讓三隻彼此互為同生群。）
    adj: dict[str, set[str]] = {}
    for pair in twin_pairs:
        a, b = tuple(pair)
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen: set[str] = set()
    for node in list(adj):
        if node in seen:
            continue
        comp, stack = [], [node]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x); comp.append(x)
            stack.extend(adj[x] - seen)
        for i in range(len(comp)):
            for j in range(i + 1, len(comp)):
                twin_pairs.add(frozenset([comp[i], comp[j]]))

    # 雙胞胎
    twin_rows = []
    for pair in twin_pairs:
        a, b = sorted(pair)
        twin_rows.append((a, b))
    twin_rows.sort()  # set 迭代順序不定；排序讓 DB 內容可重現、利於 dump 比對
    cur.executemany("INSERT OR IGNORE INTO twins (slug_a, slug_b) VALUES (?,?)", twin_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(twin_rows)} 組雙胞胎關係")

    # ── 已宣告手足（frontmatter siblings:）───────────────────────
    # 只在共同父母不詳、無法由 parent_child 推導時使用。對稱（單邊列出即可），
    # 兩隻都須有條目才建邊。
    declared_pairs: set[frozenset] = set()
    for slug, sibs in declared_sib_raw.items():
        for sib in sibs:
            if sib in all_slugs and sib != slug:
                declared_pairs.add(frozenset([slug, sib]))
    declared_rows = sorted((tuple(sorted(pair)) for pair in declared_pairs))
    cur.executemany(
        "INSERT OR IGNORE INTO declared_siblings (slug_a, slug_b) VALUES (?,?)",
        declared_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(declared_rows)} 組已宣告手足關係")

    # ── Pass 3：居住史 ─────────────────────────────────────────
    # 居住史唯一來源 = frontmatter zoos（含精確日期）；內文 ## 居住史 表格由
    # tools/gen_residence.py 自動生成，僅供顯示，不再被解析。
    zoo_rows: list[dict] = []
    for slug, body, row in panda_rows:
        fm_text = (WIKI_DIR / (slug + ".md")).read_text(encoding="utf-8")
        fm2, _ = parse_frontmatter(fm_text)
        for z in parse_zoos(fm2.get("zoos", [])):
            zoo_rows.append({"slug": slug, **z})

    # 園名解析為註冊表 canonical（唯一事實來源）；未登記 → 報錯中止
    from zoo_registry import ZooRegistry
    reg = ZooRegistry.load()
    errors = []
    for zr in zoo_rows:
        rec = reg.resolve(zr["zoo_name"])
        if rec is None:
            errors.append((zr["slug"], zr["zoo_name"]))
        else:
            zr["zoo_name"] = rec["canonical"]
    if errors:
        print(f"\n  ❌ {len(errors)} 筆居住史園名不在註冊表 data/zoos.json：")
        for slug, nm in errors:
            print(f"     {slug}: 「{nm}」")
        print("  → 請先在 data/zoos.json 登記該園（或修正拼法），再重建。")
        sys.exit(1)

    cur.executemany("""
        INSERT INTO residences (slug, zoo_name, start_year, end_year, start_date, end_date)
        VALUES (:slug, :zoo_name, :start_year, :end_year, :start_date, :end_date)
    """, zoo_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(zoo_rows)} 筆居住史")

    conn.close()
    print(f"\n✅ 完成！資料庫儲存於: {actual_db}")


if __name__ == "__main__":
    build_db()
