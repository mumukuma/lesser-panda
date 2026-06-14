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

# ── YAML frontmatter parser（不依賴 PyYAML）────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """返回 (frontmatter_dict, body)。無 frontmatter 則回傳 ({}, text)。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    return _parse_simple_yaml(yaml_block), body


def _parse_simple_yaml(yaml_text: str) -> dict:
    """最小化 YAML parser，支援：scalar、quoted scalar、inline list、block list。"""
    result: dict = {}
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # 跳過空行與純縮排
        if not line.strip() or line.startswith("  "):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()

        # inline list: [a, b, c]
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1]
            items = [s.strip().strip('"').strip("'") for s in inner.split(",")]
            result[key] = items
            i += 1
            continue

        # block list：接下來行以 "  - " 開頭
        if rest == "":
            block_items = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("  - "):
                block_items.append(lines[j][4:].strip())
                j += 1
            if block_items:
                result[key] = block_items
                i = j
                continue

        # scalar
        result[key] = rest.strip('"').strip("'")
        i += 1
    return result


# ── Wikilink 抽取 ─────────────────────────────────────────────
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")

def extract_wikilinks(text: str) -> list[str]:
    """取出所有 [[slug]] 中的 slug，並正規化為 kebab-lowercase。"""
    return [m.group(1).strip().lower() for m in WIKILINK_RE.finditer(text)]

def first_wikilink(text: str) -> str | None:
    m = WIKILINK_RE.search(text)
    return m.group(1).strip().lower() if m else None


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
            result["mother"] = first_wikilink(stripped)
            continue

        # 父
        if re.match(r"^-\s*父[：:]", stripped):
            result["father"] = first_wikilink(stripped)
            continue

        # 雙胞胎（可能有多人，取所有 wikilinks）
        # 也匹配「雙胞胎姊妹：」「雙胞胎兄弟：」「雙胞胎哥哥：」等變體
        if re.match(r"^-\s*雙胞胎[^：:]{0,4}[：:]", stripped):
            result["twins"].extend(extract_wikilinks(stripped))

    return result


# ── 居住史解析（從 YAML zoos 欄位）──────────────────────────
ZOO_YEAR_RE = re.compile(r"^(.+?)\s*\((\d{4})\s*[–—-]\s*(\d{4}|現在|今|)?\s*\)$")

def parse_zoos(zoos_raw) -> list[dict]:
    """
    輸入：YAML zoos 欄位（字串列表）
    輸出：[{zoo_name, start_year, end_year}, ...]
    """
    if not zoos_raw:
        return []
    if isinstance(zoos_raw, str):
        zoos_raw = [zoos_raw]
    results = []
    for entry in zoos_raw:
        entry = entry.strip()
        m = ZOO_YEAR_RE.match(entry)
        if m:
            zoo_name  = m.group(1).strip()
            start_yr  = int(m.group(2))
            end_raw   = m.group(3)
            end_yr    = None if (not end_raw or end_raw in ("現在","今")) else int(end_raw)
            results.append({"zoo_name": zoo_name, "start_year": start_yr, "end_year": end_yr})
        else:
            # 無法解析年份，至少記下動物園名
            results.append({"zoo_name": entry, "start_year": None, "end_year": None})
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

        row = {
            "slug":             slug,
            "name":             fm.get("name", ""),
            "japanese":         fm.get("japanese"),
            "nicknames":        json.dumps(nicknames, ensure_ascii=False) if nicknames else None,
            "english_variants": json.dumps(english_variants, ensure_ascii=False) if english_variants else None,
            "sex":              sex,
            "born":             fm.get("born"),
            "died":             fm.get("died"),
            "species":          species_short(fm.get("species")),
            "rpf_id":           int(fm["rpf_id"]) if fm.get("rpf_id") else None,
            "rpf_url":          fm.get("rpf_url"),
            "tags":             json.dumps(tags_raw, ensure_ascii=False),
            "instagram":        json.dumps(instagram, ensure_ascii=False) if instagram else None,
            "is_alive":         0 if fm.get("died") else 1,
        }
        panda_rows.append((slug, body, row))
        all_slugs.add(slug)

    cur.executemany("""
        INSERT OR REPLACE INTO pandas
          (slug, name, japanese, nicknames, english_variants,
           sex, born, died, species, rpf_id, rpf_url, tags, instagram, is_alive)
        VALUES
          (:slug,:name,:japanese,:nicknames,:english_variants,
           :sex,:born,:died,:species,:rpf_id,:rpf_url,:tags,:instagram,:is_alive)
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

    # 雙胞胎
    twin_rows = []
    for pair in twin_pairs:
        a, b = sorted(pair)
        twin_rows.append((a, b))
    cur.executemany("INSERT OR IGNORE INTO twins (slug_a, slug_b) VALUES (?,?)", twin_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(twin_rows)} 組雙胞胎關係")

    # ── Pass 3：居住史 ─────────────────────────────────────────
    zoo_rows: list[dict] = []
    for slug, body, row in panda_rows:
        # 嘗試從 markdown 居住史表格解析精確日期
        precise = parse_residence_table(body, slug)
        if precise:
            zoo_rows.extend(precise)
        else:
            # fallback：從 YAML zoos 欄位
            fm_text = (WIKI_DIR / (slug + ".md")).read_text(encoding="utf-8")
            fm2, _ = parse_frontmatter(fm_text)
            for z in parse_zoos(fm2.get("zoos", [])):
                zoo_rows.append({"slug": slug, **z, "start_date": None, "end_date": None})

    cur.executemany("""
        INSERT INTO residences (slug, zoo_name, start_year, end_year, start_date, end_date)
        VALUES (:slug, :zoo_name, :start_year, :end_year, :start_date, :end_date)
    """, zoo_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(zoo_rows)} 筆居住史")

    conn.close()
    print(f"\n✅ 完成！資料庫儲存於: {actual_db}")


# ── 居住史表格解析（精確日期）──────────────────────────────────
DATE_RANGE_RE = re.compile(
    r"(\d{4})[/\-](\d{2})[/\-](\d{2})"   # start date
    r"\s*[–—-]+\s*"
    r"(?:(\d{4})[/\-](\d{2})[/\-](\d{2})|現在|今|)"  # end date or 現在
)
ZOO_CELL_CLEAN_RE = re.compile(r"[🐣🌈🏡]|\（[^）]*）|\([^)]*\)")

def parse_residence_table(body: str, slug: str) -> list[dict]:
    """從 markdown 居住史 table 解析精確日期。"""
    # 找到 ## 居住史 section
    m = re.search(r"^##\s+居住", body, re.MULTILINE)
    if not m:
        return []
    section = body[m.start():]
    next_sec = re.search(r"\n##\s+", section[3:])
    if next_sec:
        section = section[: next_sec.start() + 3]

    results = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or stripped.startswith("| 期間") or set(stripped) <= set("|-: "):
            continue
        cells = [c.strip() for c in stripped.split("|") if c.strip()]
        if len(cells) < 2:
            continue
        date_cell = cells[0]
        zoo_cell  = cells[1] if len(cells) > 1 else ""

        dm = DATE_RANGE_RE.search(date_cell)
        if not dm:
            continue

        start_date = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)}"
        if dm.group(4):
            end_date = f"{dm.group(4)}-{dm.group(5)}-{dm.group(6)}"
        else:
            end_date = None

        # 清理動物園名稱：去掉 emoji、括號補充
        zoo_clean = ZOO_CELL_CLEAN_RE.sub("", zoo_cell).strip()
        zoo_clean = re.sub(r"\s+", " ", zoo_clean).strip()
        if not zoo_clean:
            zoo_clean = zoo_cell

        results.append({
            "slug":       slug,
            "zoo_name":   zoo_clean,
            "start_year": int(dm.group(1)),
            "end_year":   int(dm.group(4)) if dm.group(4) else None,
            "start_date": start_date,
            "end_date":   end_date,
        })
    return results


if __name__ == "__main__":
    build_db()
