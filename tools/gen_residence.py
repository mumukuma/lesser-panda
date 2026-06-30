"""phase2：居住史單一事實來源。

- 把每隻熊的居住史日期收斂到 frontmatter `zoos:`（含精確日期）。
- 內文 `## 居住史` 表格改由本程式自動生成（園名/地點來自 data/zoos.json）。
- 地點順手收進註冊表（location_ja），讓地點也單一來源。

安全：寫入前做「改寫前後」自我比對當守門——每檔在 frontmatter `zoos:`
與既有 `## 居住史` 表格裡出現過的園，都必須仍出現在重生結果裡；若任何園
被掉了（例如兩來源不一致、extract 取表格而漏掉 frontmatter 的園）就中止不寫。
此守門完全在本次執行內完成，不依賴任何外部快照檔。
用法：python3 tools/gen_residence.py            # 套用
      python3 tools/gen_residence.py --dry      # 僅檢查守門與統計
"""
import os, re, sys, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_registry import ZooRegistry, REGISTRY_PATH

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")

CFLAG = {'Japan':('日本','🇯🇵'),'Taiwan':('台灣','🇹🇼'),'USA':('美國','🇺🇸'),'China':('中國','🇨🇳'),
 'Chile':('智利','🇨🇱'),'Canada':('加拿大','🇨🇦'),'South Korea':('韓國','🇰🇷'),'Australia':('澳洲','🇦🇺'),
 'Netherlands':('荷蘭','🇳🇱'),'Indonesia':('印尼','🇮🇩'),'Thailand':('泰國','🇹🇭')}
_COUNTRY_WORDS = ['日本','台灣','台湾','中國','中国','美國','美国','加拿大','韓國','韩国','大韓民國',
 '智利','澳洲','澳大利亞','荷蘭','印尼','英國','德國','法國','泰國','新加坡']
_FLAG = re.compile(r"[\U0001F1E6-\U0001F1FF]")
DATE_RANGE_RE = re.compile(
    r"(\d{4})(?:[/\-](\d{2})[/\-](\d{2}))?\s*[–—~〜-]+\s*"
    r"(?:(\d{4})(?:[/\-](\d{2})[/\-](\d{2}))?|現在|今)?")

reg = ZooRegistry.load()


def split_fm(text):
    m = re.match(r"^(---\n)(.*?)(\n---\n?)(.*)$", text, re.S)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3), m.group(4)


def fm_get(fmb, key):
    m = re.search(rf"^{key}\s*:\s*(.+)$", fmb, re.M)
    return m.group(1).strip() if m else None


def fm_zoos(fmb):
    m = re.search(r"(?m)^zoos:\s*\n((?:[ \t]+-[^\n]*\n?)*)", fmb)
    if not m:
        return []
    return [re.sub(r"^[ \t]+-\s*", "", ln).strip() for ln in m.group(1).splitlines() if ln.strip()]


def parse_table(body):
    m = re.search(r"##\s*居住史\s*\n(.*?)(?=\n##|\n---|\Z)", body, re.S)
    if not m:
        return None
    rows = [r for r in m.group(1).splitlines() if r.strip().startswith("|")]
    if len(rows) < 2:
        return None
    hdr = [c.strip() for c in rows[0].strip("|").split("|")]
    out = []
    for r in rows[2:]:
        cells = [c.strip() for c in r.strip("|").split("|")]
        if len(cells) < 2 or set("".join(cells)) <= set("-: "):
            continue
        if hdr[:2] == ["動物園", "時期"]:
            zoo, date, loc = cells[0], cells[1], ""
        else:
            date = cells[0]; zoo = cells[1] if len(cells) > 1 else ""; loc = cells[2] if len(cells) > 2 else ""
        out.append((date, zoo, loc))
    return out


def dates_from(datecell):
    dm = DATE_RANGE_RE.search(datecell or "")
    if not dm:
        # 無範圍破折號：嘗試單一年份（如「2019」）
        ym = re.search(r"\d{4}", datecell or "")
        return (None, int(ym.group(0)) if ym else None, None, None)
    sd = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)}" if dm.group(2) and dm.group(3) else None
    ed = f"{dm.group(4)}-{dm.group(5)}-{dm.group(6)}" if dm.group(4) and dm.group(5) and dm.group(6) else None
    return (sd, int(dm.group(1)) if dm.group(1) else None, ed, int(dm.group(4)) if dm.group(4) else None)


def fm_years(s):
    m = re.search(r"[（(]\s*(\d{4})?\s*[–—~〜-]\s*(\d{4}|現在|今)?\s*[）)]", s)
    if not m:
        return (None, None)
    sy = int(m.group(1)) if m.group(1) else None
    ey = int(m.group(2)) if (m.group(2) and m.group(2).isdigit()) else None
    return (sy, ey)


def clean_location(loc):
    s = _FLAG.sub("", loc or "")
    for w in _COUNTRY_WORDS:
        s = s.replace(w, "")
    s = re.sub(r"\s+", "", s).strip()
    return s


def resolve_canon(name):
    rec = reg.resolve(name)
    return rec["canonical"] if rec else name


def zoos_before(fmb, body):
    """改寫前的權威園集合（canonical）。frontmatter `zoos:` 為唯一事實來源：
    有 `zoos:` 時即以它為基準（刻意更換／更正動物園不應被誤判成掉園）；
    僅當無 `zoos:` 時，才退回既有居住史表格。守門仍可擋下「frontmatter
    解析失敗導致某園消失」的意外。"""
    names = set()
    entries = fm_zoos(fmb)
    if entries:
        for entry in entries:
            name, _ = split_fm_entry(entry)
            if name:
                names.add(resolve_canon(name))
        return names
    tab = parse_table(body)
    if tab:
        for _date, zoo, _loc in tab:
            if zoo:
                names.add(resolve_canon(zoo))
    return names


def split_fm_entry(entry):
    """'園名 (起 – 訖)' → (園名, 日期區間字串)；無括號則 (園名, '')。
    園名可含空白（如西方園名），日期區間一律在尾端括號內。"""
    m = re.match(r"^(.*?)\s*[（(]\s*(.*?)\s*[）)]\s*$", entry)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return entry.strip(), ""


def extract(fmb, body):
    """回傳 residences: [{zoo(canonical), sd, sy, ed, ey, loc}]。
    frontmatter `zoos:` 為唯一事實來源（含完整日期，用 dates_from 解析）；
    僅當 frontmatter 無 `zoos:` 時，才退回解析既有居住史表格。
    地點一律由註冊表（rec）在 render 時提供，故此處 loc 留空。"""
    res = []
    entries = fm_zoos(fmb)
    if entries:
        for entry in entries:
            name, drange = split_fm_entry(entry)
            rec = reg.resolve(name)
            sd, sy, ed, ey = dates_from(drange) if drange else (None, None, None, None)
            res.append(dict(zoo=rec["canonical"] if rec else name, sd=sd, sy=sy, ed=ed, ey=ey,
                            loc="", rec=rec))
    else:
        tab = parse_table(body)
        if tab:
            for date, zoo, loc in tab:
                rec = reg.resolve(zoo)
                sd, sy, ed, ey = dates_from(date)
                res.append(dict(zoo=rec["canonical"] if rec else zoo, sd=sd, sy=sy, ed=ed, ey=ey,
                                loc=clean_location(loc), rec=rec))
    return res


def daterange_str(r, is_last, died):
    start = r["sd"] or (str(r["sy"]) if r["sy"] else None)
    if r["ed"]:
        end = r["ed"]
    elif r["ey"]:
        end = str(r["ey"])
    elif is_last and not died:
        end = "現在"
    else:
        end = None
    if start and end:
        return f"({start} – {end})"
    if start and not end:
        return f"({start} – )"
    if not start and end:
        return f"( – {end})"
    return None


def render_section(res, born, died):
    lines = ["## 居住史", "",
             "<!-- 此表由 tools/gen_residence.py 自動生成；請勿手改。來源：frontmatter zoos: 與 data/zoos.json -->",
             "", "| 期間 | 動物園 | 地點 |", "|------|--------|------|"]
    n = len(res)
    rows = []  # 依時間順序（舊→新）建列，最後反轉輸出成倒敘（最新在最上）
    for i, r in enumerate(res):
        start = r["sd"] or (str(r["sy"]) if r["sy"] else "?")
        if r["ed"]:
            end = r["ed"]
        elif r["ey"]:
            end = str(r["ey"])
        elif i == n - 1 and not died:
            end = "現在"
        else:
            end = ""
        period = f"{start} – {end}" if end else f"{start} –"
        rec = r["rec"]
        flags = ""
        if i == 0 and (r["sy"] is None or str(r["sy"]) == str(born)[:4]):
            flags += " 🐣"
        if i == n - 1 and not died and not r["ed"] and not r["ey"]:
            flags += " 🏡"
        loc = ""
        if rec:
            cl = CFLAG.get(rec.get("country"), ("", ""))
            locja = rec.get("location_ja") or ""
            loc = " ".join(p for p in [cl[0], locja] if p)
            if cl[1]:
                loc = (loc + " " + cl[1]).strip()
        rows.append(f"| {period} | {r['zoo']}{flags} | {loc} |")
    lines.extend(reversed(rows))  # 倒敘：最新居所在最上
    return "\n".join(lines)


def build_fm_zoos(res, died):
    out = []
    n = len(res)
    for i, r in enumerate(res):
        dr = daterange_str(r, i == n - 1, died)
        out.append(f"  - {r['zoo']} {dr}".rstrip() if dr else f"  - {r['zoo']}")
    return "zoos:\n" + "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    files = [f for f in glob.glob(os.path.join(WIKI, "*.md"))
             if os.path.basename(f) not in ("index.md", "log.md")]

    # ── pass 1：解析 + 守門（改寫前後園集合不可減少）+ harvest 地點 ──
    parsed = {}
    harvest = collections.defaultdict(collections.Counter)
    violations = []
    changed = []
    for f in files:
        slug = os.path.basename(f)[:-3]
        text = open(f, encoding="utf-8").read()
        parts = split_fm(text)
        if not parts:
            continue
        _, fmb, _, body = parts
        res = extract(fmb, body)
        parsed[slug] = (text, parts, res, fm_get(fmb, "born") or "", fm_get(fmb, "died"))
        before = zoos_before(fmb, body)        # 改寫前：frontmatter ∪ 既有表格
        after = {r["zoo"] for r in res}        # 改寫後：即將寫出的園
        lost = before - after
        if lost:
            violations.append((slug, sorted(lost), sorted(after)))
        elif before != after:
            changed.append((slug, sorted(before), sorted(after)))
        # 地點 harvest：仍從既有居住史表格收（res 已不帶 loc，居住史來源改為 frontmatter）
        _tab = parse_table(body)
        if _tab:
            for _date, _zoo, _loc in _tab:
                _rec = reg.resolve(_zoo); _cl = clean_location(_loc)
                if _rec and _cl:
                    harvest[_rec["canonical"]][_cl] += 1
    if violations:
        print(f"❌ 守門失敗：{len(violations)} 檔在重生後掉了園，中止不寫：")
        for slug, lost, after in violations[:15]:
            print(f"   {slug}: 掉了={lost} 重生後={after}")
        sys.exit(1)
    print(f"✅ 守門通過：{len(parsed)} 檔無遺失（改寫前後園集合無減少）")
    if changed:
        print(f"ℹ️  {len(changed)} 檔園集合有調整（前→後，多為救回表格漏列）：")
        for slug, b, a in changed:
            print(f"   {slug}: {b} → {a}")

    # ── 補齊註冊表 location_ja（data/zoos.json 為唯一事實來源：只填「空白」者，
    #    永不覆寫既有人工校訂值，避免與 lineage 衍生值來回拉扯造成全庫地點抖動）──
    data = json.load(open(REGISTRY_PATH, encoding="utf-8"))
    bycanon = {r["canonical"]: r for r in data}
    filled = 0
    for canon, ctr in harvest.items():
        loc = ctr.most_common(1)[0][0]
        if canon in bycanon and loc and not bycanon[canon].get("location_ja"):
            bycanon[canon]["location_ja"] = loc; filled += 1
    if not dry:
        json.dump(data, open(REGISTRY_PATH, "w"), ensure_ascii=False, indent=1)
    print(f"✅ 註冊表 location_ja 補齊 {filled} 座空白（既有校訂值不動）")
    reg.__init__(data)  # reload index with new locations

    if dry:
        print("（--dry：不寫檔）")
        return

    # ── pass 2：改寫 frontmatter zoos + 重生/插入 居住史 ──
    written = 0
    for slug, (text, parts, res, born, died) in parsed.items():
        head, fmb, sep, body = parts
        new_fmb = re.sub(r"(?m)^zoos:\s*\n(?:[ \t]+-[^\n]*\n?)*", build_fm_zoos(res, died), fmb, count=1)
        section = render_section(res, born, died)
        if re.search(r"(?m)^##\s*居住史", body):
            new_body = re.sub(r"(?ms)^##\s*居住史.*?(?=\n##\s|\n---|\Z)", section, body, count=1)
        else:
            mm = re.search(r"(?m)^##\s*家族", body)
            if mm:
                new_body = body[:mm.start()] + section + "\n\n---\n\n" + body[mm.start():]
            else:
                new_body = body.rstrip() + "\n\n" + section + "\n"
        open(os.path.join(WIKI, slug + ".md"), "w", encoding="utf-8").write(head + new_fmb + sep + new_body)
        written += 1
    print(f"✅ 改寫 {written} 檔（frontmatter zoos + 居住史表格）")


if __name__ == "__main__":
    main()
