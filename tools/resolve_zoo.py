#!/usr/bin/env python3
"""簡稱／部分名 → 動物園註冊表 canonical 的解析輔助工具。

用途：使用者回報轉園時常只寫簡稱（例：只寫 `tama`、`東山`、`nasu`），
而 `data/zoos.json` 的比對是「正規化後精準比對」，簡稱對不到。
這支工具做寬鬆的子串比對，幫你在省核時把簡稱對到正確的 canonical，
不確定時列出候選讓你挑，零命中時提示要先登記新園。

⚠️ 這只是「省核輔助」，不改任何 wiki。它的輸出是建議，最終 canonical
由作者決定後寫進條目 frontmatter `zoos:`，再由 build_db.py 的嚴格比對把關。

用法：
  # 解析簡稱，列出候選
  python tools/resolve_zoo.py tama
  python tools/resolve_zoo.py 東山

  # 確認後把這個簡稱補進該園的 aliases（愈用愈準；下次就精準命中）
  python tools/resolve_zoo.py --add tama 多摩動物公園

回傳碼：精準/單一候選命中回 0，多候選或零命中回 1（方便接其他腳本）。
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

# 重用註冊表的正規化與載入邏輯（唯一事實來源仍是 data/zoos.json）
from zoo_registry import ZooRegistry, REGISTRY_PATH, norm, preclean

_TOKEN_SPLIT = re.compile(r"[\s　（）()【】\[\]「」、,，･・'’\"&\-–—~〜/]+")
_HAS_CJK = re.compile(r"[぀-ヿ㐀-鿿]")


def name_keys(rec: dict) -> list[str]:
    """名稱類欄位（比對主力）：canonical、英、中、別名。"""
    keys = [rec.get("canonical"), rec.get("en"), rec.get("zh")]
    keys += rec.get("aliases") or []
    return [k for k in keys if k]


def loc_keys(rec: dict) -> list[str]:
    """地點欄位（次要、寬鬆比對用）。"""
    return [k for k in (rec.get("location_ja"), rec.get("location_en")) if k]


def _strong_hit(query: str, keys: list[str]) -> bool:
    """高信心比對：拉丁字以「詞」為單位（避免 tama ⊂ saitama 誤判）；CJK 用子串。"""
    q = norm(query)
    if not q:
        return False
    cjk = bool(_HAS_CJK.search(query))
    for k in keys:
        # 拉丁：切詞後比對「整詞相等」或「詞首相符」（query 至少 3 字）
        for tok in _TOKEN_SPLIT.split(k):
            nt = norm(tok)
            if not nt:
                continue
            if nt == q or (len(q) >= 3 and nt.startswith(q)):
                return True
        # CJK：query 含中日文且至少 2 字，用子串（東山 ⊂ 東山動植物園）
        if cjk and len(q) >= 2 and q in norm(k):
            return True
    return False


def _loose_hit(query: str, keys: list[str]) -> bool:
    """寬鬆比對：任一方向的子串。"""
    q = norm(query)
    if not q:
        return False
    return any(q in norm(k) or norm(k) in q for k in keys)


def find_candidates(reg: ZooRegistry, query: str) -> tuple[list[dict], str]:
    """回 (候選清單, 命中種類)。種類：exact / strong / loose / location / none。"""
    q = norm(preclean(query))
    if not q:
        return [], "none"

    # 0) 精準（含括號日英並列、emoji 等，交給 registry 既有邏輯）
    rec = reg.resolve(query)
    if rec:
        return [rec], "exact"

    # 依信心由高到低分層，取第一個非空層
    strong = [r for r in reg.records if _strong_hit(query, name_keys(r))]
    if strong:
        return strong, "strong"
    loose = [r for r in reg.records if _loose_hit(query, name_keys(r))]
    if loose:
        return loose, "loose"
    location = [r for r in reg.records if _loose_hit(query, loc_keys(r))]
    if location:
        return location, "location"
    return [], "none"


def label(rec: dict) -> str:
    extra = rec.get("en") or rec.get("zh") or ""
    extra = f"  ({extra})" if extra and extra != rec["canonical"] else ""
    loc = rec.get("location_ja") or rec.get("location_en") or ""
    loc = f"  〔{loc}〕" if loc else ""
    return f"{rec['canonical']}{extra}{loc}"


def cmd_resolve(query: str) -> int:
    reg = ZooRegistry.load()
    cands, kind = find_candidates(reg, query)

    if kind == "exact":
        print(f"✅ 精準命中（信心高）：{label(cands[0])}")
        print(f"   → frontmatter zoos: 請寫 canonical：{cands[0]['canonical']}")
        return 0

    caution = "（寬鬆比對，務必核對地點再採用）" if kind in ("loose", "location") else ""

    if len(cands) == 1:
        r = cands[0]
        print(f"🟡 單一候選（請確認）{caution}：{label(r)}")
        print(f"   → 確認無誤後寫 canonical：{r['canonical']}")
        print(f"   → 順手補別名（下次就精準命中）：")
        print(f"        python tools/resolve_zoo.py --add {query} {r['canonical']}")
        return 0

    if cands:
        print(f"🟡 多個候選（{len(cands)} 筆，請挑一個）{caution}：")
        for r in cands:
            print(f"   - {label(r)}")
        print("   → 挑定後寫該園 canonical；可用 --add 把簡稱補進它的 aliases。")
        return 1

    print(f"🔴 查無此園：{query!r}")
    print("   → 可能是簡稱我們沒收過，或這是一座還沒登記的新園。")
    print("   → 若確認是新園，先在 data/zoos.json 加一筆（canonical 日文全名／")
    print("      zh／座標 lat,lng／website／logo），再寫條目，否則 build_db 會報錯中止。")
    return 1


def cmd_add(alias: str, canonical: str) -> int:
    """把 alias 補進指定 canonical 那一筆的 aliases[]，並存回 zoos.json。"""
    path = Path(REGISTRY_PATH)
    data = json.loads(path.read_text(encoding="utf-8"))

    target = None
    for r in data:
        if r.get("canonical") == canonical:
            target = r
            break
    if target is None:
        # 容錯：用 resolver 再試一次（也許傳的是別名而非 canonical）
        reg = ZooRegistry.load()
        rec = reg.resolve(canonical)
        if rec:
            for r in data:
                if r.get("canonical") == rec["canonical"]:
                    target = r
                    break
    if target is None:
        print(f"🔴 註冊表裡找不到 canonical：{canonical!r}")
        print("   → 請用完整 canonical（如「多摩動物公園」）。先跑解析確認名稱。")
        return 1

    aliases = target.setdefault("aliases", [])
    if any(norm(a) == norm(alias) for a in aliases):
        print(f"ℹ️  「{alias}」已在 {target['canonical']} 的 aliases，未重複加入。")
        return 0

    aliases.append(alias)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"✅ 已把別名「{alias}」加進「{target['canonical']}」。")
    print("   下次 `resolve_zoo.py" + f" {alias}` 就會精準命中。")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) >= 1 and argv[0] == "--add":
        if len(argv) != 3:
            print("用法：python tools/resolve_zoo.py --add <簡稱> <canonical>")
            return 2
        return cmd_add(argv[1], argv[2])

    if len(argv) != 1 or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    return cmd_resolve(argv[0])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
