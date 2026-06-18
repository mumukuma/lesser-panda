"""動物園註冊表（唯一事實來源）載入與比對。

權威來源：data/zoos.json（作者維護）。每筆：
  canonical（對外顯示主名，必須唯一）、lineage_id、en、zh、country、
  location_ja/en、lat、lng、map、website、logo、aliases[]

用法：
  reg = ZooRegistry.load()
  rec = reg.resolve("Tama Zoological Park（多摩動物公園）🐣")   # → 該園 dict 或 None
  name = rec["canonical"] if rec else None
"""
from __future__ import annotations
import json, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "data" / "zoos.json"

_FLAG = re.compile(r"[\U0001F1E6-\U0001F1FF]")
_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿️]")
_YEARPAREN = re.compile(r"[（(][^（）()]*(?:現在|今|–|—|-|~|〜|\d{4})[^（）()]*[）)]")
_NOTES = ("出生地", "終老之地", "終焉の地", "終焉", "終居", "終老", "出生", "現居", "🏡", "🐣", "🌈")


def preclean(s: str) -> str:
    """去掉園名上的註記：國旗、emoji、年份括號、出生地/終老等尾綴。"""
    s = _FLAG.sub("", s)
    s = _YEARPAREN.sub("", s)
    for n in _NOTES:
        s = s.replace(n, "")
    s = _EMOJI.sub("", s)
    return s.strip()


def norm(s: str) -> str:
    """比對用正規化：NFKC、去空白與常見標點、小寫。"""
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[\s　（）()【】\[\]「」、,，･・'’\"&\-–—~〜]", "", s)
    return s.lower()


class ZooRegistry:
    def __init__(self, records: list[dict]):
        self.records = records
        self._by_canon: dict[str, dict] = {}
        self._index: dict[str, dict] = {}   # norm(key) → record
        for r in records:
            self._by_canon[r["canonical"]] = r
            for key in [r["canonical"], r.get("en"), r.get("zh"), *(r.get("aliases") or [])]:
                if key:
                    self._index.setdefault(norm(key), r)

    @classmethod
    def load(cls, path: Path = REGISTRY_PATH) -> "ZooRegistry":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(data)

    def resolve(self, raw: str) -> dict | None:
        """園名（可能含日英並列、括號、emoji、年份）→ 註冊表記錄；查不到回 None。"""
        if not raw:
            return None
        cleaned = preclean(raw)
        # 候選：括號前段、去括號全段、原樣
        cands = [
            norm(re.split(r"[（(]", cleaned)[0]),
            norm(cleaned),
            norm(re.sub(r"[（(][^（）()]*[）)]", "", cleaned)),
        ]
        for n in cands:
            if n and n in self._index:
                return self._index[n]
        return None

    def canonical(self, raw: str) -> str | None:
        rec = self.resolve(raw)
        return rec["canonical"] if rec else None


if __name__ == "__main__":
    reg = ZooRegistry.load()
    print(f"註冊表載入：{len(reg.records)} 座園")
    for t in ["Tama Zoological Park（多摩動物公園）🐣", "茶臼山動物園",
              "Taipei Zoo（台北市立動物園、台北市文山區）🏡 🇹🇼", "未知動物園"]:
        r = reg.resolve(t)
        print(f"  {t!r:45} -> {r['canonical'] if r else None}")
