#!/usr/bin/env python3
"""
export_json.py — 從 redpanda.db 匯出網站所需的 JSON

用法（在 wiki 根目錄執行）：
    python tools/build_db.py          # 先重建 DB
    python site/scripts/export_json.py

輸出（site/data/）：
    pandas.json   — 所有個體完整資料（含居住史、現居）
    family.json   — 親子邊 + 雙胞胎邊（家系圖用）
    zoos.json     — 動物園（含座標），及各園現居個體
    report.json   — 匯出統計與未匹配動物園名（除錯用）

動物園主檔來源：/tmp/redpanda-lineage（若存在則重新解析並快取），
否則使用既有快取 site/data/zoos-master.json。
"""

import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent.parent  # red-panda-wiki/
SITE_DATA = ROOT / "site" / "data"
LINEAGE = Path("/tmp/redpanda-lineage")
DB_CANDIDATES = [ROOT / "redpanda.db", Path("/tmp/redpanda.db")]


def get_db():
    # 兩個候選位置都可能存在（沙盒會 fallback 到 /tmp），取最新的那份
    found = [p for p in DB_CANDIDATES if p.exists() and p.stat().st_size > 0]
    if not found:
        sys.exit("找不到 redpanda.db，請先執行 python tools/build_db.py")
    p = max(found, key=lambda x: x.stat().st_mtime)
    conn = sqlite3.connect(p)
    conn.row_factory = sqlite3.Row
    return conn, p


# ── 動物園主檔 ────────────────────────────────────────────────

# ── 漢字名抽取（供中文介面「漢字→英文」顯示規則）─────────────
_KANJI_RE = re.compile(r"[一-鿿々]")   # CJK 統一漢字 + 々
_KANA_RE = re.compile(r"[぀-ヿ]")          # 平假名 + 片假名

# 從 redpanda-lineage 的 ja.othernames 救回、wiki japanese 欄位缺漏的漢字名
# （以 rpf_id 為鍵；未來可逐步併回 wiki frontmatter 的 japanese 欄位）
KANJI_BY_RPF = {
    319: "暁", 318: "曙", 317: "旭", 295: "明日葉", 71: "福福", 947: "和",
    359: "美美", 1450: "最中", 946: "令", 364: "怜怜", 82: "龍", 288: "六堡",
    171: "緑之介", 304: "杏花", 164: "陽陽",
}


def clean_japanese(japanese: str | None) -> str | None:
    """濾掉只有標點/波浪號等雜訊的 japanese 欄位（無假名也無漢字者視為無）。"""
    if japanese and (_KANA_RE.search(japanese) or _KANJI_RE.search(japanese)):
        return japanese
    return None


def extract_kanji(japanese: str | None, rpf_id=None) -> str | None:
    """回傳可供中文顯示的漢字名；無漢字則 None（中文介面將退回英文名）。"""
    if japanese:
        tokens = re.split(r"[\s/／（）()、,，｜|]+", japanese)
        pure = [t for t in tokens if t and _KANJI_RE.search(t) and not _KANA_RE.search(t)]
        if pure:
            return pure[0]
    return KANJI_BY_RPF.get(rpf_id)


def _to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def parse_zoo_file(path: Path) -> dict:
    d = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line or line.startswith("photo"):
            continue
        k, _, v = line.partition(":")
        d[k.strip()] = v.strip()
    return {
        "id": int(d.get("_id", 0)),
        "ja_name": d.get("ja.name") or None,
        "en_name": d.get("en.name") or None,
        "location_ja": d.get("ja.location") or None,
        "location_en": d.get("en.location") or None,
        "country": d.get("flag") or path.parent.name,
        "lat": _to_float(d.get("latitude")),
        "lng": _to_float(d.get("longitude")),
        "map": d.get("map") or None,
        "website": d.get("website") or None,
    }


def load_zoo_master() -> list[dict]:
    cache = SITE_DATA / "zoos-master.json"
    if LINEAGE.exists():
        zoos = []
        for f in sorted(LINEAGE.glob("zoos/*/*.txt")):
            try:
                z = parse_zoo_file(f)
                if z["ja_name"] or z["en_name"]:
                    zoos.append(z)
            except Exception as e:
                print(f"  ⚠️ 解析失敗 {f.name}: {e}")
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(zoos, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  動物園主檔：{len(zoos)} 筆（已快取 zoos-master.json）")
        return zoos
    if cache.exists():
        zoos = json.loads(cache.read_text(encoding="utf-8"))
        print(f"  動物園主檔：{len(zoos)} 筆（來自快取）")
        return zoos
    print("  ⚠️ 無 lineage 資料夾也無快取，動物園座標將全部缺漏")
    return []


def norm(s: str) -> str:
    """正規化名稱以利匹配：NFKC、去空白與標點、小寫"""
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[\s（）()【】\[\]・･'’\"&-]", "", s)
    return s.lower()


def preclean(s: str) -> str:
    """去掉 wiki 居住史園名的註記尾綴：出生地、終老之地、國旗 emoji、(–2016) 等"""
    s = re.sub(r"[\U0001F1E6-\U0001F1FF]", "", s)          # 國旗
    s = re.sub(r"[（(][–\-—~〜]?\s*\d{0,4}[）)]", "", s)     # (–2016) 之類
    for suffix in ("出生地", "終老之地", "出生", "終老"):
        s = s.replace(suffix, "")
    return s.strip()


# wiki 慣用名 → lineage 正式名（皆以 norm 後字串比對）
ZOO_ALIASES = {
    "西山動物公園": "鯖江市西山動物園",
    "のんほいパーク": "豊橋総合動植物公園",
    "八木山動物公園フォレスタ": "セルコホームズーパラダイス八木山",
    "八木山動物公園": "セルコホームズーパラダイス八木山",
    "秋吉台サファリランド": "秋吉台自然動物公園サファリランド",
    "石川動物園": "いしかわ動物園",
    "ソウル大公園動物園": "seoulzoo",
    "日立かみね動物園": "日立市かみね動物園",
    "safariniagara": "safariniagra",  # lineage 原始資料拼字如此
    "fukuokamunicipalzoologicalandbotanicalgarden": "fukuokamunicipalzooandbotanicalgarden",
    "九十九島動植物園森きらら": "西海国立公園九十九島動植物園",
    "横浜市立金沢動物園zoorasia": "よこはま動物園ズーラシア",
}


def build_zoo_matcher(zoos: list[dict]):
    index = {}
    for z in zoos:
        for key in filter(None, [z["ja_name"], z["en_name"]]):
            index[norm(key)] = z
    keys = sorted(index.keys(), key=len, reverse=True)

    aliases = {norm(a): norm(c) for a, c in ZOO_ALIASES.items()}

    def match(raw: str):
        """wiki 居住史的園名（可能含日英並列、括號註記）→ 動物園記錄"""
        cleaned = preclean(raw)
        candidates = [norm(re.split(r"[（(]", cleaned)[0]), norm(cleaned)]
        for n in candidates:
            n = aliases.get(n, n)
            if n in index:
                return index[n]
        for n in candidates:
            for k in keys:  # 子字串雙向包含（取最長 key 優先）
                if len(k) >= 4 and len(n) >= 4 and (k in n or n in k):
                    return index[k]
        return None

    return match


# ── 主流程 ────────────────────────────────────────────────────

def main():
    conn, db_path = get_db()
    print(f"讀取 {db_path}")
    SITE_DATA.mkdir(parents=True, exist_ok=True)

    zoos_master = load_zoo_master()
    match_zoo = build_zoo_matcher(zoos_master)

    pandas = {}
    for r in conn.execute("SELECT * FROM pandas"):
        pandas[r["slug"]] = {
            "slug": r["slug"],
            "name": r["name"],
            "japanese": clean_japanese(r["japanese"]),
            "kanji": extract_kanji(r["japanese"], r["rpf_id"]),
            "nicknames": json.loads(r["nicknames"] or "[]"),
            "english_variants": json.loads(r["english_variants"] or "[]"),
            "sex": r["sex"],
            "born": r["born"],
            "died": r["died"],
            "species": r["species"],
            "rpf_id": r["rpf_id"],
            "rpf_url": r["rpf_url"],
            "residences": [],
            "current_zoo": None,   # zoo master id
            "current_zoo_raw": None,
            "mother": None,
            "father": None,
            "twins": [],
            "children": [],
        }

    # 居住史 + 現居
    unmatched = {}
    for r in conn.execute("SELECT * FROM residences ORDER BY slug, start_year, id"):
        p = pandas.get(r["slug"])
        if not p:
            continue
        z = match_zoo(r["zoo_name"])
        if z is None:
            unmatched[r["zoo_name"]] = unmatched.get(r["zoo_name"], 0) + 1
        p["residences"].append({
            "zoo_raw": r["zoo_name"],
            "zoo_id": z["id"] if z else None,
            "start": r["start_date"] or (str(r["start_year"]) if r["start_year"] else None),
            "end": r["end_date"] or (str(r["end_year"]) if r["end_year"] else None),
        })
    for p in pandas.values():
        if p["died"]:
            continue
        res = p["residences"]
        cur = next((x for x in reversed(res) if x["end"] is None), res[-1] if res else None)
        if cur:
            p["current_zoo"] = cur["zoo_id"]
            p["current_zoo_raw"] = cur["zoo_raw"]

    # 家族關係
    edges = []
    for r in conn.execute("SELECT * FROM parent_child"):
        c, par = pandas.get(r["child_slug"]), pandas.get(r["parent_slug"])
        if not c or not par:
            continue
        c[r["parent_type"]] = r["parent_slug"]
        par["children"].append(r["child_slug"])
        edges.append({"child": r["child_slug"], "parent": r["parent_slug"],
                      "type": r["parent_type"], "confidence": r["confidence"]})
    twins = []
    for r in conn.execute("SELECT * FROM twins"):
        a, b = r["slug_a"], r["slug_b"]
        if a in pandas and b in pandas:
            pandas[a]["twins"].append(b)
            pandas[b]["twins"].append(a)
            twins.append([a, b])
    for p in pandas.values():
        p["children"].sort(key=lambda s: pandas[s]["born"] or "9999")

    # 各園現居個體
    used_zoo_ids = {p["current_zoo"] for p in pandas.values() if p["current_zoo"]}
    all_res_ids = {r["zoo_id"] for p in pandas.values() for r in p["residences"] if r["zoo_id"]}
    # 動物園 logo：手動覆蓋（zoo-logos.json）優先，否則用官網 favicon
    overrides = {}
    ov_path = SITE_DATA / "zoo-logos.json"
    if ov_path.exists():
        overrides = {int(k): v for k, v in json.loads(ov_path.read_text(encoding="utf-8")).items()}

    def zoo_logo(z):
        if z["id"] in overrides:
            return overrides[z["id"]]
        host = urlparse(z["website"] or "").netloc
        return f"https://www.google.com/s2/favicons?domain={host}&sz=64" if host else None

    zoos_out = []
    for z in zoos_master:
        if z["id"] not in all_res_ids:
            continue
        residents = sorted(
            [s for s, p in pandas.items() if p["current_zoo"] == z["id"]],
            key=lambda s: pandas[s]["born"] or "9999")
        zoos_out.append({**z, "logo": zoo_logo(z), "residents": residents})
    zoos_out.sort(key=lambda z: (-len(z["residents"]), z["id"]))

    # 輸出
    out = {
        "pandas.json": {"generated_from": "wiki/*.md via redpanda.db",
                        "count": len(pandas), "pandas": pandas},
        "family.json": {"parent_child": edges, "twins": twins},
        "zoos.json": {"count": len(zoos_out), "zoos": zoos_out},
        "report.json": {
            "pandas": len(pandas),
            "edges": len(edges),
            "twins": len(twins),
            "zoos_used": len(zoos_out),
            "zoos_with_coords": sum(1 for z in zoos_out if z["lat"]),
            "unmatched_zoo_names": unmatched,
        },
    }
    for fname, data in out.items():
        (SITE_DATA / fname).write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"  ✅ site/data/{fname}")
    print(f"完成：{len(pandas)} 個體 / {len(edges)} 親子邊 / {len(zoos_out)} 動物園"
          f"（未匹配園名 {len(unmatched)} 種）")


if __name__ == "__main__":
    main()
