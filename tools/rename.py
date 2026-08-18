#!/usr/bin/env python3
"""
rename.py — 個體條目改名（slug 遷移）機械化工具

背景：本 wiki 的 slug（檔名）＝ `slugify(name)-生日`，同時是全站 [[wikilink]]、
家系邊（build_db 由父母行／子女表／雙胞胎行解析 wikilink）、網站 URL 的主鍵。
改名不是換標籤，而是一次主鍵遷移；本工具把「機械可做」的部分一次做完：

    1. 撞名檢查（wiki/ 與 wiki/_hidden/ 皆查）
    2. 改檔名（wiki/old.md → wiki/new.md）
    3. 全站 [[wikilink]] 更換（含 [[slug|別名]]；wiki/ 與 _hidden/，
       log.md／log-archive/ 依規範禁 wikilink，故排除、僅檢查回報）
    4. frontmatter `siblings:` 清單裡的 slug 同步更換
    5. index.md 頁首「最後更新」日期更新（wikilink 已由步驟 3 涵蓋）
    6. wiki/log.md 末端 append 一筆 `rename` 記錄（舊 slug 用 backtick，禁 wikilink）

工具「不做」的（編輯性工作，仍需人工／LLM 判斷）：
    - frontmatter `name`／`japanese`／`chinese`／tags 等內容變更
      （`--name` 可順手改 `name:` 一欄，其餘不碰）
    - 條目標題、引言、內文敘述裡的舊名字（跑完會列出含舊 slug 純文字的檔案供檢查）
    - rebuild（跑完請自行 `bash rebuild.sh`）

用法（在 repo 根目錄）：
    python3 tools/rename.py <old-slug> <new-slug> [--name "New Name"]
                            [--reason "一句話原因"] [--dry-run]

    --dry-run   只列出將發生的變更，不寫任何檔案
    --name      同時把 frontmatter 的 `name:` 改為此值
    --reason    寫進 log 的一句話原因（預設「slug 更名」；log 骨架僅供起頭，
                建議事後補充完整脈絡）

注意：
    - 本工具只動 wiki/*.md 與 wiki/_hidden/*.md 的文字，純 stdlib、可在
      掛載資料夾上直接跑（改檔名走 rename、不刪檔）。
    - 跑完必做：`bash rebuild.sh`（gen_residence → build_db → export_json →
      check_twins）。網站舊網址 /p/<old-slug>/ 會失效，log 記錄裡已附提醒。
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_io import parse_frontmatter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
HIDDEN = WIKI / "_hidden"
INDEX = WIKI / "index.md"
LOG = WIKI / "log.md"
LOG_ARCHIVE = WIKI / "log-archive"

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


# ── slugify（照 CLAUDE.md「檔名與消歧」規則） ──────────────────
def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower()
    s = re.sub(r"['().]", "", s)
    s = re.sub(r"[\s_]+", "-", s.strip())
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def wikilink_pattern(slug: str) -> re.Pattern:
    """比對 [[slug]] 與 [[slug|別名]]（容忍前後空白；大小寫不敏感——
    build_db 解析時本就正規化為小寫）。"""
    return re.compile(r"\[\[\s*" + re.escape(slug) + r"\s*(\||\]\])", re.IGNORECASE)


def sibling_line_pattern(slug: str) -> re.Pattern:
    """frontmatter block list 項：`  - slug`（整行、精確比對）。"""
    return re.compile(r"^(\s*-\s*)" + re.escape(slug) + r"(\s*)$", re.MULTILINE)


def frontmatter_span(text: str) -> tuple[int, int]:
    """回傳 frontmatter 區塊（含首尾 ---）在 text 中的 [start, end)；無則 (0, 0)。"""
    if not text.startswith("---"):
        return (0, 0)
    end = text.find("\n---", 3)
    if end == -1:
        return (0, 0)
    return (0, end + 4)


def list_entry_files() -> list[Path]:
    """所有條目檔（wiki/ 非遞迴 ＋ _hidden/），排除 index／log。"""
    files = [p for p in sorted(WIKI.glob("*.md")) if p.name not in ("index.md", "log.md")]
    if HIDDEN.is_dir():
        files += sorted(HIDDEN.glob("*.md"))
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description="個體條目改名（slug 遷移）")
    ap.add_argument("old_slug")
    ap.add_argument("new_slug")
    ap.add_argument("--name", help="同時把 frontmatter 的 name: 改為此值")
    ap.add_argument("--reason", default="slug 更名", help="log 記錄裡的一句話原因")
    ap.add_argument("--dry-run", action="store_true", help="只預覽、不寫檔")
    args = ap.parse_args()

    old, new = args.old_slug.strip().lower(), args.new_slug.strip().lower()
    problems: list[str] = []

    # ── 0. 基本驗證 ─────────────────────────────────────────
    if old == new:
        print("❌ 新舊 slug 相同，無事可做")
        return 1
    if not SLUG_RE.match(new):
        print(f"❌ 新 slug `{new}` 不合法（僅允許小寫英數與連字號）")
        return 1

    old_path = WIKI / f"{old}.md"
    in_hidden = False
    if not old_path.exists():
        alt = HIDDEN / f"{old}.md"
        if alt.exists():
            old_path, in_hidden = alt, True
        else:
            print(f"❌ 找不到條目：wiki/{old}.md（_hidden/ 也沒有）")
            return 1

    # 撞名檢查：wiki/ 與 _hidden/ 皆不可已存在
    for cand in (WIKI / f"{new}.md", HIDDEN / f"{new}.md"):
        if cand.exists():
            print(f"❌ 撞名：{cand.relative_to(ROOT)} 已存在。"
                  f"同名同生日請依規則加媽媽名消歧（如 `sora-seina-2008-06-16`）")
            return 1

    new_path = old_path.with_name(f"{new}.md")

    # ── 1. 讀本尊、驗 slug 與 name/born 的一致性（僅警告不擋） ──
    text = old_path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
    name_for_check = args.name or str(fm.get("name") or "")
    born = str(fm.get("born") or "").strip()
    if name_for_check:
        base = slugify(name_for_check)
        expected = f"{base}-{born}" if born else None
        ok = new == expected if expected else new.startswith(base + "-") or new == base
        if expected and new != expected and new.startswith(base + "-"):
            ok = True  # 母名消歧（name-mother-born）或園簡稱 fallback
        if not ok:
            problems.append(
                f"⚠️ 新 slug `{new}` 與 name+born 推導值不符（預期 `{expected or base + '-…'}`）。"
                f"若是刻意消歧可忽略；否則請確認 frontmatter `name:`／`born:` 是否也要改"
                f"（name 可用 --name 順手改）")

    # ── 2. 掃描全站引用 ─────────────────────────────────────
    link_pat = wikilink_pattern(old)
    sib_pat = sibling_line_pattern(old)
    changes: list[tuple[Path, str, int, int]] = []  # (path, new_text, n_links, n_sibs)

    for p in list_entry_files() + [INDEX]:
        t = p.read_text(encoding="utf-8")
        src = new_path if p == old_path else p  # 本尊等下會換路徑
        n_links = len(link_pat.findall(t))
        n_sibs = 0
        t2 = link_pat.sub(lambda m: f"[[{new}{m.group(1)}", t)
        # siblings: 只在 frontmatter 區塊內動
        fs, fe = frontmatter_span(t2)
        if fe and sib_pat.search(t2[fs:fe]):
            fixed_fm, n_sibs = sib_pat.subn(rf"\g<1>{new}\g<2>", t2[fs:fe])
            t2 = fixed_fm + t2[fe:]
        if n_links or n_sibs:
            changes.append((src if p != old_path else old_path, t2, n_links, n_sibs))

    # log 檔按規範禁 wikilink——若裡面竟有舊 slug 的 wikilink，回報但不動
    log_files = ([LOG] if LOG.exists() else []) + \
        (sorted(LOG_ARCHIVE.glob("*.md")) if LOG_ARCHIVE.is_dir() else [])
    for p in log_files:
        if link_pat.search(p.read_text(encoding="utf-8")):
            problems.append(f"⚠️ {p.relative_to(ROOT)} 內含 `[[{old}]]` wikilink——"
                            f"log 禁 wikilink，這是既有違規，請人工處理（本工具不動 log 歷史）")

    # 純文字殘留（backtick 提及、docs 等）僅回報
    plain_hits: list[str] = []
    for p in list_entry_files() + [INDEX]:
        t = p.read_text(encoding="utf-8")
        t_nolink = sib_pat.sub("", link_pat.sub("", t))
        if old in t_nolink:
            plain_hits.append(str(p.relative_to(ROOT)))
    docs_files = sorted((ROOT / "docs").glob("**/*.md")) if (ROOT / "docs").is_dir() else []
    for p in docs_files:
        if old in p.read_text(encoding="utf-8"):
            plain_hits.append(str(p.relative_to(ROOT)))

    # ── 3. 預覽 ─────────────────────────────────────────────
    today = _dt.date.today().isoformat()
    print(f"改名計畫：`{old}` → `{new}`" + ("（條目在 _hidden/）" if in_hidden else ""))
    print(f"  檔案：{old_path.relative_to(ROOT)} → {new_path.relative_to(ROOT)}")
    if args.name:
        print(f"  frontmatter name: → {args.name}")
    touched = [(p, nl, ns) for (p, _, nl, ns) in changes if p != old_path]
    print(f"  引用更新：{len(touched)} 檔"
          f"（wikilink {sum(nl for _, nl, _ in touched)} 處、siblings {sum(ns for _, _, ns in touched)} 處）")
    for p, nl, ns in touched:
        det = "、".join(x for x in (f"wikilink ×{nl}" if nl else "", f"siblings ×{ns}" if ns else "") if x)
        print(f"    - {p.relative_to(ROOT)}（{det}）")
    for w in problems:
        print(w)
    if plain_hits:
        print(f"  ℹ️ 以下檔案含舊 slug 純文字（backtick 提及等），不自動改、請人工檢視：")
        for h in plain_hits:
            print(f"    - {h}")

    if args.dry_run:
        print("\n（--dry-run：未寫任何檔案）")
        return 0

    # ── 4. 套用 ─────────────────────────────────────────────
    # 4a. 本尊：換 wikilink（若有自引用）＋（選）改 name → 改檔名
    self_new = next((t2 for (p, t2, _, _) in changes if p == old_path), text)
    if args.name:
        fs, fe = frontmatter_span(self_new)
        fm_txt, rest = self_new[fs:fe], self_new[fe:]
        fm_txt, n = re.subn(r"(?m)^name:\s*.*$", f"name: {args.name}", fm_txt, count=1)
        if n == 0:
            problems.append("⚠️ frontmatter 找不到 `name:` 行，--name 未生效")
        self_new = fm_txt + rest
    old_path.write_text(self_new, encoding="utf-8")
    old_path.rename(new_path)

    # 4b. 其他檔案
    for p, t2, _, _ in changes:
        if p == old_path:
            continue
        p.write_text(t2, encoding="utf-8")

    # 4c. index.md 頁首「最後更新」
    if INDEX.exists():
        it = INDEX.read_text(encoding="utf-8")
        it2, n = re.subn(r"(> 最後更新：)\d{4}-\d{2}-\d{2}", rf"\g<1>{today}", it, count=1)
        if n:
            INDEX.write_text(it2, encoding="utf-8")
        else:
            problems.append("⚠️ index.md 找不到「最後更新」行，日期未更新")

    # 4d. log.md append（禁 wikilink，slug 一律 backtick）
    idx_counts = next((nl for p, _, nl, _ in changes if p == INDEX), 0)
    upd_lines = "\n".join(
        f"- `{p.relative_to(WIKI)}` — wikilink" +
        (f" ×{nl}" if nl else "") + (f"、siblings ×{ns}" if ns else "")
        for p, _, nl, ns in changes if p not in (old_path, INDEX)) or "- （無其他條目引用）"
    entry = f"""

## [{today}] rename | `{old}` → `{new}`（{args.reason}）

（本記錄由 tools/rename.py 產生，僅機械變更；脈絡與原因請視需要補充。）

**改名**：

- `{old}.md` → **`{new}.md`**{f"（name: → {args.name}）" if args.name else ""}

**更新條目**（wikilink／siblings 同步更換；其餘資料未動）：

{upd_lines}
- `index.md` — wikilink ×{idx_counts}；「最後更新」改 {today}；條目總數不變

**備注**：舊網址 /p/{old}/ 將失效。
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)

    # ── 5. 收尾檢查 ─────────────────────────────────────────
    residue = [str(p.relative_to(ROOT)) for p in list_entry_files() + [INDEX]
               if link_pat.search(p.read_text(encoding="utf-8"))]
    if residue:
        problems.append("❌ 事後檢查：仍有檔案含舊 wikilink（不應發生）：" + "、".join(residue))

    print("\n✅ 完成。後續請務必：")
    print("  1. 人工處理：條目標題／引言／內文與其他條目敘述裡的舊「名字」文字"
          "（上方 ℹ️ 清單）、frontmatter japanese/chinese/tags 等編輯性欄位")
    print("  2. 補充 log.md 這筆記錄的脈絡（原因、來源）")
    print("  3. `bash rebuild.sh`（gen_residence → build_db → export_json → check_twins）")
    print(f"  4. 留意舊網址 /p/{old}/ 失效")
    for w in problems:
        print(w)
    return 2 if any(w.startswith("❌") for w in problems) else 0


if __name__ == "__main__":
    sys.exit(main())
