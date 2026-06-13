#!/usr/bin/env python3
"""
query.py — 常用查詢工具

使用方式（在 red-panda-wiki/ 下執行）：
    python tools/query.py ancestors taofa        # 列出所有已知祖先
    python tools/query.py descendants kiki       # 列出所有已知後代
    python tools/query.py common taofa franken   # 共同祖先偵測
    python tools/query.py profile kiki           # 個體完整資料
    python tools/query.py zoo "Nagano"           # 某動物園的個體
    python tools/query.py pairing ako            # 配對候選分析（異性、無子女、血緣夠遠）

或直接 import 在 Jupyter / Claude session 中使用：
    from tools.query import RedPandaDB
    db = RedPandaDB()
    db.ancestors("taofa")
"""

import sqlite3, json, sys
from pathlib import Path

DB_CANDIDATES = [
    Path(__file__).parent.parent / "redpanda.db",
    Path("/tmp/redpanda.db"),
]

def get_db_path():
    for p in DB_CANDIDATES:
        if p.exists() and p.stat().st_size > 0:
            return p
    raise FileNotFoundError(
        "找不到 redpanda.db，請先執行: python tools/build_db.py"
    )


class RedPandaDB:
    def __init__(self, db_path=None):
        self.path = db_path or get_db_path()
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row

    # ── 個體查詢 ──────────────────────────────────────────────
    def profile(self, slug: str):
        """個體完整資料 + 父母 + 子女 + 雙胞胎"""
        p = self.conn.execute("SELECT * FROM pandas WHERE slug=?", (slug,)).fetchone()
        if not p:
            print(f"找不到: {slug}")
            return
        print(f"{'='*50}")
        print(f"  {p['name']}（{p['japanese'] or '-'}）{' 🌈' if p['died'] else ''}")
        print(f"  slug: {slug}  |  RPF: #{p['rpf_id']}")
        print(f"  性別: {p['sex']}  |  生: {p['born']}  |  歿: {p['died'] or '現存'}")
        print(f"  物種: {p['species']}")
        # 父母
        parents = self.conn.execute("""
            SELECT pc.parent_type, p2.name, p2.slug
            FROM parent_child pc JOIN pandas p2 ON p2.slug=pc.parent_slug
            WHERE pc.child_slug=?
        """, (slug,)).fetchall()
        for par in parents:
            print(f"  {par['parent_type']}: {par['name']} ({par['slug']})")
        # 雙胞胎
        twins = self.conn.execute("""
            SELECT p2.name, p2.slug FROM twins t
            JOIN pandas p2 ON p2.slug = CASE WHEN t.slug_a=? THEN t.slug_b ELSE t.slug_a END
            WHERE t.slug_a=? OR t.slug_b=?
        """, (slug, slug, slug)).fetchall()
        if twins:
            print(f"  雙胞胎: {', '.join(r['name'] for r in twins)}")
        # 子女
        children = self.conn.execute("""
            SELECT p2.name, p2.born, p2.sex, p2.slug FROM parent_child pc
            JOIN pandas p2 ON p2.slug=pc.child_slug
            WHERE pc.parent_slug=?
            ORDER BY p2.born
        """, (slug,)).fetchall()
        if children:
            print(f"  子女 ({len(children)}):")
            for c in children:
                print(f"    - {c['name']} ({c['sex']}, {c['born'] or '?'}) [{c['slug']}]")
        # 居住史
        res = self.conn.execute("""
            SELECT zoo_name, start_year, end_year FROM residences
            WHERE slug=? ORDER BY start_year
        """, (slug,)).fetchall()
        if res:
            print(f"  居住史:")
            for r in res:
                end = r['end_year'] or '現在'
                print(f"    {r['start_year']}–{end}  {r['zoo_name']}")

    # ── 祖先追溯 ──────────────────────────────────────────────
    def ancestors(self, slug: str, max_depth: int = 6) -> dict[str, int]:
        """回傳 {ancestor_slug: generation}，1=父母，2=祖父母..."""
        result: dict[str, int] = {}
        queue = [(slug, 0)]
        visited = {slug}
        while queue:
            cur, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for r in self.conn.execute(
                "SELECT parent_slug FROM parent_child WHERE child_slug=?", (cur,)
            ):
                p = r['parent_slug']
                if p not in visited:
                    visited.add(p)
                    result[p] = depth + 1
                    queue.append((p, depth + 1))
        if result:
            rows = self.conn.execute(
                f"SELECT slug, name, born, died FROM pandas WHERE slug IN ({','.join('?'*len(result))})",
                list(result)
            ).fetchall()
            name_map = {r['slug']: r for r in rows}
            gen_labels = {1:"父母",2:"祖父母",3:"曾祖父母",4:"高祖父母",5:"玄祖父母",6:"來祖父母"}
            print(f"\n{slug} 的已知祖先（{len(result)} 隻）：")
            for gen in sorted(set(result.values())):
                gens = [s for s,g in result.items() if g==gen]
                print(f"\n  [{gen_labels.get(gen,f'第{gen}代')}]")
                for s in gens:
                    r = name_map.get(s)
                    if r:
                        died = f"🌈{r['died']}" if r['died'] else '現存'
                        print(f"    {r['name']} ({r['born'] or '?'}–{r['died'] or ''}) [{s}]")
        else:
            print(f"{slug} 無已知祖先記錄")
        return result

    # ── 後代追蹤 ──────────────────────────────────────────────
    def descendants(self, slug: str, max_depth: int = 6) -> dict[str, int]:
        """回傳 {descendant_slug: generation}"""
        result: dict[str, int] = {}
        queue = [(slug, 0)]
        visited = {slug}
        while queue:
            cur, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for r in self.conn.execute(
                "SELECT child_slug FROM parent_child WHERE parent_slug=?", (cur,)
            ):
                c = r['child_slug']
                if c not in visited:
                    visited.add(c)
                    result[c] = depth + 1
                    queue.append((c, depth + 1))
        if result:
            rows = self.conn.execute(
                f"SELECT slug, name, born, died FROM pandas WHERE slug IN ({','.join('?'*len(result))})",
                list(result)
            ).fetchall()
            name_map = {r['slug']: r for r in rows}
            print(f"\n{slug} 的已知後代（{len(result)} 隻）：")
            by_gen: dict[int, list] = {}
            for s, g in result.items():
                by_gen.setdefault(g, []).append(s)
            gen_labels = {1:"子女",2:"孫",3:"曾孫",4:"玄孫",5:"來孫"}
            for gen in sorted(by_gen):
                label = gen_labels.get(gen, f"第{gen}代")
                print(f"\n  [{label}] {len(by_gen[gen])} 隻")
                for s in sorted(by_gen[gen]):
                    r = name_map.get(s)
                    if r:
                        died = " 🌈" if r['died'] else ""
                        print(f"    {r['name']}{died} ({r['born'] or '?'}) [{s}]")
        else:
            print(f"{slug} 無已知後代記錄")
        return result

    # ── 共同祖先偵測 ──────────────────────────────────────────
    def common_ancestors(self, slug_a: str, slug_b: str, max_depth: int = 8) -> list[str]:
        """偵測兩隻個體的共同祖先，並估算近親程度"""
        anc_a = self.ancestors(slug_a, max_depth)
        anc_b = self.ancestors(slug_b, max_depth)
        common = set(anc_a) & set(anc_b)

        pa = self.conn.execute("SELECT name FROM pandas WHERE slug=?", (slug_a,)).fetchone()
        pb = self.conn.execute("SELECT name FROM pandas WHERE slug=?", (slug_b,)).fetchone()
        name_a = pa['name'] if pa else slug_a
        name_b = pb['name'] if pb else slug_b

        print(f"\n共同祖先分析：{name_a} × {name_b}")
        if not common:
            print("  ✅ 無共同已知祖先（資料範圍內）")
            return []

        rows = self.conn.execute(
            f"SELECT slug, name FROM pandas WHERE slug IN ({','.join('?'*len(common))})",
            list(common)
        ).fetchall()
        name_map = {r['slug']: r['name'] for r in rows}

        print(f"  ⚠️  找到 {len(common)} 個共同祖先：")
        for s in sorted(common, key=lambda x: anc_a.get(x,99) + anc_b.get(x,99)):
            ga = anc_a.get(s, '?')
            gb = anc_b.get(s, '?')
            print(f"    {name_map.get(s, s)}：對 {name_a} 是第{ga}代，對 {name_b} 是第{gb}代")
        return list(common)

    # ── 動物園查詢 ────────────────────────────────────────────
    def zoo(self, keyword: str):
        """依關鍵字搜尋動物園，列出曾居住的個體"""
        rows = self.conn.execute("""
            SELECT p.name, p.sex, p.born, p.died, r.zoo_name, r.start_year, r.end_year
            FROM residences r JOIN pandas p ON p.slug=r.slug
            WHERE r.zoo_name LIKE ?
            ORDER BY r.start_year, p.name
        """, (f"%{keyword}%",)).fetchall()
        if not rows:
            print(f"找不到含「{keyword}」的動物園記錄")
            return
        zoo_name = rows[0]['zoo_name']
        print(f"\n{zoo_name}（搜尋: {keyword}）— {len(rows)} 筆記錄")
        for r in rows:
            end = r['end_year'] or '現在'
            status = "🌈" if r['died'] else "◎"
            print(f"  {status} {r['name']} ({r['sex']}, {r['born']}): {r['start_year']}–{end}")

    # ── 配對候選 ─────────────────────────────────────────────
    def _ancestors_set(self, slug: str, max_depth: int = 2) -> set[str]:
        """回傳所有祖先 slug 的集合（不含自身）"""
        result: set[str] = set()
        queue = [(slug, 0)]
        visited = {slug}
        while queue:
            cur, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for r in self.conn.execute(
                "SELECT parent_slug FROM parent_child WHERE child_slug=?", (cur,)
            ):
                p = r["parent_slug"]
                if p not in visited:
                    visited.add(p)
                    result.add(p)
                    queue.append((p, depth + 1))
        return result

    def _descendants_set(self, slug: str, max_depth: int = 6) -> set[str]:
        """回傳所有後代 slug 的集合（不含自身）"""
        result: set[str] = set()
        queue = [(slug, 0)]
        visited = {slug}
        while queue:
            cur, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for r in self.conn.execute(
                "SELECT child_slug FROM parent_child WHERE parent_slug=?", (cur,)
            ):
                c = r["child_slug"]
                if c not in visited:
                    visited.add(c)
                    result.add(c)
                    queue.append((c, depth + 1))
        return result

    def pairing_candidates(
        self,
        slug: str,
        min_age: int = 2,
        max_age: int = 13,
        exclude_gen: int = 2,
        current_year: int = 2026,
    ) -> list[dict]:
        """
        為任意個體找出配對候選名單。

        篩選條件：
          1. 異性
          2. 現存（未歿）
          3. 年齡在 min_age ~ max_age 之間
          4. 無已知子女（避免壓縮後代的配對空間）
          5. 無共同祖先（在 exclude_gen 代以內）

        exclude_gen=2 表示：排除共享祖父母者（表兄弟姊妹及更近的親屬）。

        用法：
            db.pairing_candidates("ako")
            db.pairing_candidates("shin-fa", min_age=3, max_age=10)
        """
        target = self.conn.execute(
            "SELECT * FROM pandas WHERE slug=?", (slug,)
        ).fetchone()
        if not target:
            print(f"找不到: {slug}")
            return []

        opposite_sex = "female" if target["sex"] == "male" else "male"

        # ── 建立排除名單：共享 exclude_gen 代以內祖先的所有個體 ──
        target_anc = self._ancestors_set(slug, max_depth=exclude_gen)
        excluded: set[str] = {slug}
        excluded |= target_anc
        excluded |= self._descendants_set(slug)   # 自身後代也排除
        for anc in target_anc:
            excluded |= self._descendants_set(anc)  # 所有祖先的後代 = 親戚

        # ── 掃描候選 ──────────────────────────────────────────
        all_opposite = self.conn.execute(
            "SELECT slug, name, born, died, species FROM pandas WHERE sex=? AND died IS NULL",
            (opposite_sex,),
        ).fetchall()

        results = []
        for cand in all_opposite:
            if cand["slug"] in excluded:
                continue

            # 年齡
            born_year = int(str(cand["born"])[:4]) if cand["born"] else None
            if not born_year:
                continue
            age = current_year - born_year
            if not (min_age <= age <= max_age):
                continue

            # 無子女
            n_children = self.conn.execute(
                "SELECT COUNT(*) AS cnt FROM parent_child WHERE parent_slug=?",
                (cand["slug"],),
            ).fetchone()["cnt"]
            if n_children > 0:
                continue

            # 現居地（最近一筆）
            res = self.conn.execute(
                "SELECT zoo_name FROM residences WHERE slug=? ORDER BY start_year DESC LIMIT 1",
                (cand["slug"],),
            ).fetchone()
            zoo = res["zoo_name"] if res else "?"

            # 父母名稱
            parents = self.conn.execute(
                """SELECT p2.name FROM parent_child pc
                   JOIN pandas p2 ON p2.slug=pc.parent_slug
                   WHERE pc.child_slug=?""",
                (cand["slug"],),
            ).fetchall()

            results.append(
                {
                    "slug": cand["slug"],
                    "name": cand["name"],
                    "born": born_year,
                    "age": age,
                    "zoo": zoo,
                    "parents": [p["name"] for p in parents],
                    "species": cand["species"] or "",
                }
            )

        # 依年齡排序（最佳繁殖年齡優先），同齡時依名字字母排序
        results.sort(key=lambda x: (abs(x["age"] - 7), x["name"].lower()))

        # ── 輸出 ──────────────────────────────────────────────
        t_name = target["name"]
        t_born = target["born"] or "?"
        t_zoo_row = self.conn.execute(
            "SELECT zoo_name FROM residences WHERE slug=? ORDER BY start_year DESC LIMIT 1",
            (slug,),
        ).fetchone()
        t_zoo = t_zoo_row["zoo_name"] if t_zoo_row else "?"

        print(f"\n{'='*60}")
        print(f"  配對候選分析：{t_name}（{slug}）")
        print(f"  性別: {target['sex']}  |  生: {t_born}  |  現居: {t_zoo}")
        print(f"  篩選條件：異性、現存、無子女、年齡 {min_age}–{max_age} 歲、")
        print(f"            與對象無共同祖先（{exclude_gen} 代以內）")
        print(f"{'='*60}")

        if not results:
            print("  （無符合條件的候選）")
        else:
            print(f"  找到 {len(results)} 隻候選（依繁殖年齡最佳化排序）：\n")
            print(f"  {'名稱':<18} {'生年':>4} {'年齡':>4}  {'父母':<30}  {'現居'}")
            print(f"  {'-'*18} {'-'*4} {'-'*4}  {'-'*30}  {'-'*30}")
            for r in results:
                parents_str = " × ".join(r["parents"][:2]) if r["parents"] else "?"
                print(
                    f"  {r['name']:<18} {r['born']:>4} {r['age']:>3}歲  "
                    f"{parents_str:<30}  {r['zoo']}"
                )

        return results

    def close(self):
        self.conn.close()


# ── CLI ──────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    db = RedPandaDB()
    cmd = sys.argv[1]

    if cmd == "profile" and len(sys.argv) >= 3:
        db.profile(sys.argv[2])
    elif cmd == "ancestors" and len(sys.argv) >= 3:
        db.ancestors(sys.argv[2])
    elif cmd == "descendants" and len(sys.argv) >= 3:
        db.descendants(sys.argv[2])
    elif cmd == "common" and len(sys.argv) >= 4:
        db.common_ancestors(sys.argv[2], sys.argv[3])
    elif cmd == "zoo" and len(sys.argv) >= 3:
        db.zoo(sys.argv[2])
    elif cmd == "pairing" and len(sys.argv) >= 3:
        db.pairing_candidates(sys.argv[2])
    else:
        print(__doc__)

    db.close()
