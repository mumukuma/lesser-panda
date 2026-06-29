#!/usr/bin/env python3
"""多胞胎（雙胞胎／三胞胎…）資料稽核。

直接讀 wiki/*.md（唯一正本），用與 build_db 相同的解析（parse_family，含消歧義
過濾）建出同生群，再驗證幾條不變量：

  E1 同生群成員生日須一致（容差 ±1 天；超過視為錯誤——多半是連錯隻或同名混淆）
  E2 同生群成員須同父同母（雙方都有父母卻不同 → 錯誤）
  E3 同生群大小 2–4（≥5 視為錯誤，通常是誤連擴散）
  W1 單邊缺父或缺母（資料待補，警告）
  W2 條目寫「雙／三／四胞胎」字面與實際連到的人數不符（警告，多為漏連或對方無條目）

說明：此工具「只讀、只報」，不會更動任何資料；認雙胞胎一律以條目標註為準，
生日只用來抓可疑連結，永不據此排除既有關係。

用法：python3 tools/check_twins.py        # 有 E 級錯誤回傳 1，僅警告回傳 0
"""
import os, re, sys, glob
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_db import parse_frontmatter, parse_family  # 與建檔同一套解析

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")

# 字面 → 預期同生群人數
WORD_N = {"二": 2, "兩": 2, "雙": 2, "三": 3, "四": 4, "五": 5, "六": 6}
LINE_RE = re.compile(r"^-\s*([二兩雙三四五六])胞胎[^：:]{0,4}[：:]", re.M)


def _d(s):
    try:
        y, m, dd = map(int, s.split("-"))
        return date(y, m, dd)
    except Exception:
        return None


def main():
    born, parents, label_n, raw_tw = {}, {}, {}, {}
    twin_pairs = set()
    slugs = set()

    for f in glob.glob(os.path.join(WIKI, "*.md")):
        b = os.path.basename(f)
        if b in ("index.md", "log.md"):
            continue
        slug = b[:-3]
        slugs.add(slug)
        text = open(f, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        born[slug] = fm.get("born")
        fam = parse_family(body)
        parents[slug] = (fam.get("mother"), fam.get("father"))
        raw_tw[slug] = [t for t in fam["twins"] if t and t != slug]
        m = LINE_RE.search(body)
        if m:
            label_n[slug] = WORD_N[m.group(1)]

    # 只保留兩端都存在條目的配對
    for slug in slugs:
        for tw in raw_tw[slug]:
            if tw in slugs:
                twin_pairs.add(frozenset([slug, tw]))

    # 傳遞閉包 → 連通分量（同生群），與 build_db 一致
    adj = {}
    for p in twin_pairs:
        a, b = tuple(p)
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen, groups = set(), []
    for n in list(adj):
        if n in seen:
            continue
        comp, st = [], [n]
        while st:
            x = st.pop()
            if x in seen:
                continue
            seen.add(x); comp.append(x); st += list(adj[x] - seen)
        groups.append(sorted(comp))

    errors, warns = [], []

    for g in groups:
        # E3 群大小
        if len(g) < 2:
            errors.append(f"E3 同生群大小異常（{len(g)}）：{g}")
        elif len(g) > 4:
            errors.append(f"E3 同生群過大（{len(g)}，疑似誤連擴散）：{g}")
        # E1 生日一致（±1 天）
        ds = {s: _d(born.get(s)) for s in g}
        valid = [v for v in ds.values() if v]
        if valid:
            span = (max(valid) - min(valid)).days
            if span > 1:
                detail = ", ".join(f"{s}({born.get(s)})" for s in g)
                errors.append(f"E1 同生群生日相差 {span} 天：{detail}")
        # E2 / W1 父母
        ps = {s: parents.get(s, (None, None)) for s in g}
        moms = {ps[s][0] for s in g}
        dads = {ps[s][1] for s in g}
        if len([m for m in moms if m]) > 1:
            errors.append(f"E2 同生群母不同：" + ", ".join(f"{s}母={ps[s][0]}" for s in g))
        elif None in moms and any(moms - {None}):
            warns.append(f"W1 同生群單邊缺母：" + ", ".join(f"{s}母={ps[s][0]}" for s in g))
        if len([d for d in dads if d]) > 1:
            errors.append(f"E2 同生群父不同：" + ", ".join(f"{s}父={ps[s][1]}" for s in g))
        elif None in dads and any(dads - {None}):
            warns.append(f"W1 同生群單邊缺父：" + ", ".join(f"{s}父={ps[s][1]}" for s in g))

    # W2a 多胞胎行連到「不存在的條目」（slug 打錯或對方頁面已改名）
    for slug in sorted(slugs):
        bad = [t for t in raw_tw[slug] if t not in slugs]
        for t in bad:
            warns.append(f"W2a {slug} 的多胞胎行連到不存在的條目 [[{t}]]（slug 可能打錯）")

    # W2b 已在同生群內、但字面人數 > 實際群大小（群內缺一名已建檔成員）
    size_of = {s: len(g) for g in groups for s in g}
    for slug, n in label_n.items():
        actual = size_of.get(slug, 1)
        if actual >= 2 and n > actual:
            warns.append(f"W2b {slug} 標「{n}胞胎」但群內只有 {actual} 隻已建檔成員（疑似缺連或對方無條目）")

    print(f"同生群：{len(groups)} 組（雙胞胎 {sum(1 for g in groups if len(g)==2)}、"
          f"三胞胎 {sum(1 for g in groups if len(g)==3)}、"
          f"四+ {sum(1 for g in groups if len(g)>=4)}）")
    for w in warns:
        print("  ⚠️ " + w)
    for e in errors:
        print("  ❌ " + e)
    if errors:
        print(f"\n❌ 稽核失敗：{len(errors)} 項錯誤、{len(warns)} 項警告")
        sys.exit(1)
    print(f"\n✅ 稽核通過：0 錯誤、{len(warns)} 項警告（警告為資料待補，不阻擋建置）")


if __name__ == "__main__":
    main()
