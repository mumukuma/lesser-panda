#!/usr/bin/env python3
"""
check_i18n.py — 五語介面字串一致性檢查（pipeline/src/i18n/*.json）

檢查三件事，任一不過即 exit 1（CI 與手動皆可跑）：
  1. 各語系 key 集合與 zh-TW（正本）完全一致（缺 key／多 key 都算錯）
  2. 同一檔內無重複 key（JSON 重複 key 會被靜默蓋掉，肉眼難察）
  3. 值不得為空字串（漏翻通常是留空），且不得含 U+FFFD 替換字元（mojibake 徵兆）

用法（repo 根目錄）：python3 tools/check_i18n.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "pipeline" / "src" / "i18n"
BASE = "zh-TW"


def load_checked(path: Path):
    """載入 JSON，同時偵測重複 key。"""
    dups = []

    def hook(pairs):
        seen = {}
        for k, v in pairs:
            if k in seen:
                dups.append(k)
            seen[k] = v
        return seen

    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)
    return data, dups


def main() -> int:
    files = sorted(I18N.glob("*.json"))
    if not files:
        print(f"🔴 找不到 i18n 檔（{I18N}）")
        return 1
    data, problems = {}, []
    for f in files:
        d, dups = load_checked(f)
        data[f.stem] = d
        for k in dups:
            problems.append(f"{f.name}: 重複 key「{k}」（後值蓋前值）")
        for k, v in d.items():
            if isinstance(v, str) and not v.strip():
                problems.append(f"{f.name}: key「{k}」值為空")
            if isinstance(v, str) and "\ufffd" in v:
                problems.append(f"{f.name}: key「{k}」含替換字元 U+FFFD（mojibake？）")
    if BASE not in data:
        print(f"🔴 缺正本語系 {BASE}.json")
        return 1
    base_keys = set(data[BASE])
    for name, d in sorted(data.items()):
        if name == BASE:
            continue
        missing = base_keys - set(d)
        extra = set(d) - base_keys
        for k in sorted(missing):
            problems.append(f"{name}.json: 缺 key「{k}」（{BASE} 有）")
        for k in sorted(extra):
            problems.append(f"{name}.json: 多出 key「{k}」（{BASE} 沒有）")

    langs = "／".join(sorted(data))
    if problems:
        print(f"🔴 i18n 檢查未通過（{len(problems)} 筆；語系：{langs}）")
        for m in problems:
            print(f"  - {m}")
        return 1
    print(f"✅ i18n 一致：{len(files)} 語系（{langs}）× {len(base_keys)} key，無重複、無空值。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
