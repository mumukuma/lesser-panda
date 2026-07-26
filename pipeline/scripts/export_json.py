#!/usr/bin/env python3
"""
export_json.py — 從 redpanda.db 匯出網站所需的 JSON

用法（在 wiki 根目錄執行）：
    python tools/build_db.py          # 先重建 DB
    python pipeline/scripts/export_json.py

輸出（pipeline/data/）：
    pandas.json   — 所有個體完整資料（含居住史、現居）
    family.json   — 親子邊 + 雙胞胎邊 + 已宣告手足邊（家系圖／個體頁用）
    zoos.json     — 動物園（含座標），及各園現居個體
    report.json   — 匯出統計與未匹配動物園名（除錯用）

動物園主檔來源：data/zoos.json（作者維護的唯一事實來源）。
canonical 即對外主名；logo、中文名、座標皆取自此註冊表。
"""

from __future__ import annotations  # 相容舊版 Python（str | None 等延後解析）

import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent.parent  # red-panda-wiki/
OUT_DATA = ROOT / "pipeline" / "data"
LINEAGE = Path("/tmp/redpanda-lineage")
DB_CANDIDATES = [ROOT / "redpanda.db", Path("/tmp/redpanda.db")]
REGISTRY = ROOT / "data" / "zoos.json"   # 動物園唯一事實來源（作者維護）
sys.path.insert(0, str(ROOT / "tools"))
from zoo_registry import preclean as zpreclean, norm as znorm  # noqa: E402


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
        tokens = re.split(r"[\s/／（）()、,，｜|・･]+", japanese)
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
    """從唯一事實來源 data/zoos.json 載入動物園。canonical 即對外主名。"""
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    zoos, synth = [], 9000
    for r in reg:
        zid = r["lineage_id"]
        if zid is None:
            synth += 1
            zid = synth
        zoos.append({
            "id": zid,
            "ja_name": r["canonical"],          # canonical 為對外顯示主名
            "ja_kana": r.get("ja_kana"),        # 假名讀音（日本園；供日文使用者搜尋）
            "en_name": r.get("en"),
            "location_ja": r.get("location_ja"),
            "location_en": r.get("location_en"),
            "location_zh": r.get("location_zh"),  # 中文地點（正本繁體；缺則前端退回 location_ja）
            "closed_ja": r.get("closed_ja"),    # 休園日（官網原文精簡；選填，缺則不顯示）
            "closed_rule": r.get("closed_rule"),  # 休園日機器可讀規則（衍生欄；人讀正本為 closed_ja，改制需同步）
            "country": r.get("country"),
            "lat": r.get("lat"), "lng": r.get("lng"),
            "map": r.get("map"), "website": r.get("website"),
            "name_zh": r.get("zh"),
            "logo": r.get("logo"),
            "_aliases": r.get("aliases") or [],
        })
    print(f"  動物園註冊表：{len(zoos)} 座（data/zoos.json）")
    return zoos


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
    """精確比對（canonical / en / aliases）。不再模糊猜；建檔時園名已是 canonical。"""
    index = {}
    for z in zoos:
        for key in filter(None, [z["ja_name"], z["en_name"], *z["_aliases"]]):
            index.setdefault(znorm(key), z)

    def match(raw: str):
        cleaned = zpreclean(raw)
        candidates = [
            znorm(re.split(r"[（(]", cleaned)[0]),
            znorm(cleaned),
            znorm(re.sub(r"[（(][^（）()]*[）)]", "", cleaned)),
        ]
        for n in candidates:
            if n and n in index:
                return index[n]
        return None

    return match


# ── 主流程 ────────────────────────────────────────────────────

def main():
    conn, db_path = get_db()
    print(f"讀取 {db_path}")
    OUT_DATA.mkdir(parents=True, exist_ok=True)

    zoos_master = load_zoo_master()
    match_zoo = build_zoo_matcher(zoos_master)

    pandas = {}
    for r in conn.execute("SELECT * FROM pandas"):
        tags = json.loads(r["tags"] or "[]")
        pandas[r["slug"]] = {
            "slug": r["slug"],
            "name": r["name"],
            "japanese": clean_japanese(r["japanese"]),
            "korean": r["korean"],
            "chinese": r["chinese"],
            "kanji": extract_kanji(r["japanese"], r["rpf_id"]),
            "nicknames": json.loads(r["nicknames"] or "[]"),
            "english_variants": json.loads(r["english_variants"] or "[]"),
            "sex": r["sex"],
            "born": r["born"],
            "died": r["died"],
            # 檔案卡：最後確認在世／在園日期（動向不明個體；網站可顯示「最後確認」）
            "last_seen": r["last_seen"],
            # 存疑個體（tags 含 unverified）：網站據此排除統計、現存篩選並顯示待查證標記
            "unverified": "unverified" in tags,
            # 蘋果籽佔位條目（tags 含 apple-seed）：網站顯示「尚未命名的寶寶」icon 標記
            "placeholder": "apple-seed" in tags,
            # 資料有限個體檔案卡（tags 含 limited-profile）：配合 has_official_source 判斷是否顯示
            # 「維護者提供・未經官方佐證」標記——避免誤觸大量以 RPF 為來源、本就無官方的一般條目
            "limited_profile": "limited-profile" in tags,
            "species": r["species"],
            "rpf_id": r["rpf_id"],
            "rpf_url": r["rpf_url"],
            "instagram": json.loads(r["instagram"] or "[]"),
            # 僅官方來源（園方/政府/園報/官方微信）；分類於 build_db.official_sources
            "sources": json.loads(r["sources"] or "[]"),
            # 佐證軸（自動推導，非手動 tag）：官方來源清單非空 → 有官方背書。
            # 為空（如僅「維護者提供（…）」無 host）→ 網站顯示「維護者提供・未經官方佐證」標記。
            # 補進官方來源後自動轉 true、標記自動消失。與在世軸 unverified 獨立、勿混用。
            "has_official_source": bool(json.loads(r["sources"] or "[]")),
            # 其他補充資料（展牌實拍等一手非官方鏈結佐證；網站另區塊顯示，待實作）
            "extra_sources": json.loads(r["extra_sources"] or "[]"),
            "residences": [],
            "current_zoo": None,   # zoo master id
            "current_zoo_raw": None,
            "mother": None,
            "father": None,
            "twins": [],
            "children": [],
            # 已宣告手足（父母不詳、無法由共同父母推導）；網站顯示為未分血緣度的「兄弟姊妹」列
            "declared_siblings": [],
        }

    # 居住史 + 現居
    unmatched = {}
    # 起年不明（start_year NULL，如「? – 2003-04-07」）以訖年代排，避免 NULL 被排到最前。
    # 起訖「都」不明（如「? – 現在」：只知道現在在這座園、不知何時抵達）再退到 9999 排最後——
    # 這種筆本質是「最新一站」，若跟著 NULL 排到最前，會讓下方的現居判定（由後往前找 end IS NULL）
    # 誤取到前一站有起年的園（實例：ki-ki-1996 多摩 1996 → 墨西哥 ? – 現在，曾誤判現居多摩）。
    # 同鍵時以 id（＝frontmatter 順序，即維護者寫的時序）為序。
    for r in conn.execute("SELECT * FROM residences ORDER BY slug, COALESCE(start_year, end_year, 9999), id"):
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
    declared_siblings = []
    for r in conn.execute("SELECT * FROM declared_siblings"):
        a, b = r["slug_a"], r["slug_b"]
        if a in pandas and b in pandas:
            pandas[a]["declared_siblings"].append(b)
            pandas[b]["declared_siblings"].append(a)
            declared_siblings.append([a, b])
    for p in pandas.values():
        p["children"].sort(key=lambda s: pandas[s]["born"] or "9999")

    # 各園現居個體
    used_zoo_ids = {p["current_zoo"] for p in pandas.values() if p["current_zoo"]}
    all_res_ids = {r["zoo_id"] for p in pandas.values() for r in p["residences"] if r["zoo_id"]}
    # 動物園 logo、中文名皆來自註冊表（data/zoos.json）；logo 缺則用官網 favicon
    def zoo_logo(z):
        if z.get("logo"):
            return z["logo"]
        host = urlparse(z["website"] or "").netloc
        return f"https://www.google.com/s2/favicons?domain={host}&sz=64" if host else None

    zoos_out = []
    for z in zoos_master:
        if z["id"] not in all_res_ids:
            continue
        residents = sorted(
            [s for s, p in pandas.items() if p["current_zoo"] == z["id"]],
            key=lambda s: pandas[s]["born"] or "9999")
        rec = {k: v for k, v in z.items() if k != "_aliases"}
        rec.update({"logo": zoo_logo(z), "name_zh": z.get("name_zh"), "residents": residents})
        zoos_out.append(rec)
    zoos_out.sort(key=lambda z: (-len(z["residents"]), z["id"]))

    # 輸出
    out = {
        "pandas.json": {"generated_from": "wiki/*.md via redpanda.db",
                        "count": len(pandas), "pandas": pandas},
        "family.json": {"parent_child": edges, "twins": twins,
                        "declared_siblings": declared_siblings},
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
        (OUT_DATA / fname).write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"  ✅ pipeline/data/{fname}")
    print(f"完成：{len(pandas)} 個體 / {len(edges)} 親子邊 / {len(zoos_out)} 動物園"
          f"（未匹配園名 {len(unmatched)} 種）")


if __name__ == "__main__":
    main()
