#!/usr/bin/env python3
"""
apply_lineage_fixes.py — 依 audit 結果，把可從 redpanda-lineage 補回的欄位寫入 wiki

保守原則：只填空白欄位；japanese 僅在「有假名無漢字」時於尾端補漢字；
絕不覆蓋既有非空值。需要 /tmp/redpanda-lineage。

用法：
    python tools/apply_lineage_fixes.py --dry-run   # 預覽要改什麼（不寫檔）
    python tools/apply_lineage_fixes.py             # 實際寫入
"""
import re
import sys
import glob
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINEAGE = Path("/tmp/redpanda-lineage")
KANJI_RE = re.compile(r"[一-鿿々]")
KANA_RE = re.compile(r"[぀-ヿ]")


def load_lineage_pandas():
    idx = {}
    for f in glob.glob(str(LINEAGE / "pandas/**/*.txt"), recursive=True):
        d = {}
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            if ":" in line and not line.startswith("photo"):
                k, _, v = line.partition(":"); d[k.strip()] = v.strip()
        if d.get("_id", "").isdigit():
            idx[int(d["_id"])] = d
    return idx


def load_zoo_names():
    names = {}
    for f in glob.glob(str(LINEAGE / "zoos/**/*.txt"), recursive=True):
        d = {}
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            if ":" in line:
                k, _, v = line.partition(":"); d[k.strip()] = v.strip()
        if d.get("_id", "").isdigit():
            names[int(d["_id"])] = d.get("ja.name") or d.get("en.name") or f"zoo#{d['_id']}"
    return names


def iso(s):
    if not s:
        return None
    p = str(s).replace("/", "-").split("-")
    return f"{int(p[0]):04d}-{int(p[1]):02d}-{int(p[2]):02d}" if len(p) == 3 else s


def lineage_kanji(d):
    cand = " ".join([d.get("ja.name", ""), d.get("ja.othernames", "")])
    toks = [w for w in re.split(r"[ ,，、/]+", cand) if KANJI_RE.search(w) and not KANA_RE.search(w)]
    return toks[0] if toks else None


def build_zoos(d, zoo_names, born, died):
    """從 lineage location.* / zoo 重建居住史，格式：名稱 (起–訖)。"""
    locs = []
    for k, v in d.items():
        m = re.match(r"location\.(\d+)$", k)
        if m and v:
            parts = [x.strip() for x in v.split(",")]
            zid = int(parts[0]) if parts[0].isdigit() else None
            yr = None
            if len(parts) > 1:
                ym = re.match(r"(\d{4})", parts[1].replace("/", "-"))
                yr = ym.group(1) if ym else None
            if zid:
                locs.append((int(m.group(1)), zid, yr))
    locs.sort()
    if not locs and d.get("zoo", "").isdigit():
        locs = [(1, int(d["zoo"]), born[:4] if born else None)]
    out = []
    for i, (_, zid, yr) in enumerate(locs):
        end = locs[i + 1][2] if i + 1 < len(locs) else (died[:4] if died else "現在")
        start = yr or ""
        span = f"（{start}–{end}）" if start else ""
        out.append(f"{zoo_names.get(zid, f'zoo#{zid}')} {span}".strip())
    return out


def patch(text, fm_changes):
    """在 frontmatter 內做最小修改：替換/插入指定欄位，body 原樣保留。"""
    end = text.find("\n---", 3)
    head, body = text[:end], text[end:]
    lines = head.splitlines()  # 含開頭 '---'

    def find(key):
        for i, ln in enumerate(lines):
            if re.match(rf"^{key}:", ln):
                return i
        return None

    for key, action in fm_changes.items():
        kind, value = action
        if kind == "scalar":
            i = find(key)
            if i is not None:
                lines[i] = f"{key}: {value}"
            else:  # 插在 name 之後或檔頭後
                ni = find("name")
                lines.insert((ni + 1) if ni is not None else 1, f"{key}: {value}")
        elif kind == "block":  # value 為 list
            i = find(key)
            block = [f"{key}:"] + [f"  - {v}" for v in value]
            if i is not None:
                # 移除原 key 行及其下方既有 '  - ' 子項
                j = i + 1
                while j < len(lines) and lines[j].lstrip().startswith("- "):
                    j += 1
                lines[i:j] = block
            else:
                ni = find("species") or find("born") or find("name") or 0
                lines[ni + 1:ni + 1] = block
    return "\n".join(lines) + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not LINEAGE.exists():
        sys.exit("需要 /tmp/redpanda-lineage，請先 git clone")

    pandas = load_lineage_pandas()
    zoo_names = load_zoo_names()
    changed = 0

    for f in sorted(WIKI.glob("*.md")):
        if f.name in ("index.md", "log.md"):
            continue
        text = f.read_text(encoding="utf-8")
        end = text.find("\n---", 3)
        head = text[:end]
        get = lambda k: (re.search(rf"^{k}:\s*(.*)$", head, re.M) or [None, ""])[1].strip() \
            if re.search(rf"^{k}:\s*(.*)$", head, re.M) else None
        rpf = get("rpf_id")
        if not (rpf and rpf.isdigit()):
            continue
        d = pandas.get(int(rpf))
        if not d:
            continue

        ja_raw = re.search(r"^japanese:\s*(.*)$", head, re.M)
        ja_val = ja_raw.group(1).strip() if ja_raw else ""
        ja_val = "" if ja_val in ("~", "null") else ja_val
        born = get("born")
        died_present = bool(re.search(r"^died:\s*\S", head, re.M))
        zoos_present = bool(re.search(r"^\s*-\s+\S", head[head.find("zoos:"):], re.M)) if "zoos:" in head else False

        changes, notes = {}, []

        # 漢字：有假名無漢字 → 尾端補；完全無 → 設為漢字
        lk = lineage_kanji(d)
        if lk and (not ja_val or not KANJI_RE.search(ja_val)):
            new_ja = f"{ja_val} / {lk}" if (ja_val and KANA_RE.search(ja_val)) else lk
            changes["japanese"] = ("scalar", new_ja); notes.append(f"japanese→{new_ja}")

        # 已歿
        if d.get("death") and not died_present:
            changes["died"] = ("scalar", iso(d["death"])); notes.append(f"died→{iso(d['death'])}")

        # 生日
        if not born and d.get("birthday"):
            changes["born"] = ("scalar", iso(d["birthday"])); notes.append(f"born→{iso(d['birthday'])}")

        # 居住地
        if not zoos_present:
            zlist = build_zoos(d, zoo_names, iso(d.get("birthday")), iso(d.get("death")))
            if zlist:
                changes["zoos"] = ("block", zlist); notes.append(f"zoos→{len(zlist)}筆")

        if changes:
            changed += 1
            print(f"{f.name}: {', '.join(notes)}")
            if not args.dry_run:
                f.write_text(patch(text, changes), encoding="utf-8")

    print(f"\n{'[dry-run] 將' if args.dry_run else '已'}修改 {changed} 個條目")


if __name__ == "__main__":
    main()
