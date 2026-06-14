-- ============================================================
-- Red Panda Wiki — SQLite Schema
-- 從 wiki/*.md 抽取的結構化資料
-- ============================================================

PRAGMA foreign_keys = ON;

-- 每次重建乾淨（DB 為衍生品）；先 drop 參照方再 drop 被參照的 pandas
DROP VIEW  IF EXISTS mates;
DROP VIEW  IF EXISTS full_siblings;
DROP TABLE IF EXISTS parent_child;
DROP TABLE IF EXISTS twins;
DROP TABLE IF EXISTS residences;
DROP TABLE IF EXISTS pandas;

-- ── 1. 個體基本資料 ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS pandas (
    slug        TEXT PRIMARY KEY,   -- 檔名（不含.md），e.g. "kiki", "mii-mii-371"
    name        TEXT NOT NULL,      -- 英文名
    japanese    TEXT,               -- 日文名（漢字/假名）
    chinese     TEXT,               -- 中文名（台灣／中國出生個體的正式中文名，優先用於中文介面）
    nicknames   TEXT,               -- JSON array，e.g. '["Beans","Forehead"]'
    english_variants TEXT,          -- JSON array，英文拼法變體
    sex         TEXT CHECK(sex IN ('male','female','unknown')),
    born        TEXT,               -- ISO date YYYY-MM-DD（或只有 YYYY）
    died        TEXT,               -- NULL = 現存
    species     TEXT,               -- "styani" | "fulgens"
    rpf_id      INTEGER,            -- Red Panda Finder profile ID
    rpf_url     TEXT,
    tags        TEXT,               -- JSON array，原始 tags
    instagram   TEXT,               -- JSON array，公開 IG 貼文連結（curate，官方 embed 展示）
    is_alive    INTEGER  -- 0=已歿, 1=現存（由 build_db.py 填入）
);

-- ── 2. 親子關係 ─────────────────────────────────────────────
-- 每一筆代表「child 的 mother/father 是 parent」
-- parent_type: 'mother' | 'father'
-- confidence:  'confirmed' | 'inferred'（從兄弟姊妹反推的）
CREATE TABLE IF NOT EXISTS parent_child (
    child_slug   TEXT NOT NULL REFERENCES pandas(slug),
    parent_slug  TEXT NOT NULL REFERENCES pandas(slug),
    parent_type  TEXT NOT NULL CHECK(parent_type IN ('mother','father')),
    confidence   TEXT DEFAULT 'confirmed',
    PRIMARY KEY (child_slug, parent_slug, parent_type)
);

-- ── 3. 雙胞胎關係 ────────────────────────────────────────────
-- 無方向性，slug_a < slug_b（字母順序）避免重複
CREATE TABLE IF NOT EXISTS twins (
    slug_a  TEXT NOT NULL REFERENCES pandas(slug),
    slug_b  TEXT NOT NULL REFERENCES pandas(slug),
    PRIMARY KEY (slug_a, slug_b),
    CHECK (slug_a < slug_b)
);

-- ── 4. 居住史 ────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS residences (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    slug        TEXT NOT NULL REFERENCES pandas(slug),
    zoo_name    TEXT NOT NULL,      -- 原始動物園名（英文或日文）
    start_year  INTEGER,
    end_year    INTEGER,            -- NULL = 仍在此動物園
    start_date  TEXT,               -- ISO date，若有精確日期
    end_date    TEXT                -- ISO date，若有精確日期
);

-- ── 5. 便利 View：親本配對（mate pairs）────────────────────
CREATE VIEW IF NOT EXISTS mates AS
SELECT
    m.parent_slug AS mother_slug,
    f.parent_slug AS father_slug,
    COUNT(*)      AS offspring_count,
    MIN(p.born)   AS first_born,
    MAX(p.born)   AS last_born
FROM parent_child m
JOIN parent_child f ON m.child_slug = f.child_slug
JOIN pandas p       ON p.slug = m.child_slug
WHERE m.parent_type = 'mother'
  AND f.parent_type = 'father'
GROUP BY m.parent_slug, f.parent_slug;

-- ── 6. 便利 View：全血緣兄弟姊妹 ───────────────────────────
CREATE VIEW IF NOT EXISTS full_siblings AS
SELECT DISTINCT
    a.child_slug AS slug_a,
    b.child_slug AS slug_b
FROM parent_child a
JOIN parent_child b
  ON a.child_slug <> b.child_slug
JOIN parent_child am ON am.child_slug = a.child_slug AND am.parent_type = 'mother'
JOIN parent_child bm ON bm.child_slug = b.child_slug AND bm.parent_type = 'mother'
JOIN parent_child af ON af.child_slug = a.child_slug AND af.parent_type = 'father'
JOIN parent_child bf ON bf.child_slug = b.child_slug AND bf.parent_type = 'father'
WHERE am.parent_slug = bm.parent_slug   -- same mother
  AND af.parent_slug = bf.parent_slug   -- same father
  AND a.child_slug < b.child_slug;
