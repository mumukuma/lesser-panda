# CLAUDE.md — 小熊貓家族 Wiki 操作手冊

本資料夾是一個依 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)運作的 Obsidian wiki：**LLM 負責撰寫與維護所有頁面，使用者負責提供資料來源與問問題**。

主題：小熊貓（red panda）個體檔案，以 Taofa（桃花）為起點逐步彙整，目前 360+ 條目，多為日本（及部分海外）動物園個體。

## ⚠️ 資料來源原則（重要）

- **`wiki/*.md` 是唯一正本與權威來源**，由站長校訂。
- [Red Panda Finder](https://redpandafinder.com)（RPF）與 [redpanda-lineage](https://github.com/wwoast/redpanda-lineage) 只是**初期建立資料的基礎參考**，**非權威**。
- 兩者衝突時，**一律以 wiki（站長的校訂）為準**，不可用 RPF/lineage 覆蓋既有資料。
- `tools/audit.py`、`tools/apply_lineage_fixes.py` 與 lineage 的比對僅供**參考與補空白**；`apply_lineage_fixes` 只填空欄位、不覆蓋；audit 列出的「與 lineage 不符」是提示站長**檢視**，不代表 wiki 錯。
- 名稱（尤其中文名 `chinese`、暱稱、別名）以站長提供為準；RPF 的羅馬拼音僅作後備。

---

## 目錄結構

```
red-panda-wiki/
├── CLAUDE.md            ← 本文件（操作手冊）
├── SCHEMA.md            ← 頁面格式與標籤規範（權威來源）
├── README.md            ← 專案總覽（對外）
├── ROADMAP.md           ← 願望池與路線規劃
├── rpf-wiki-SKILL.md    ← RPF 抓取資料 → 建立條目的詳細 skill
├── redpanda.db          ← 由 wiki/*.md 產生的 SQLite（衍生品，可重建）
├── tools/
│   ├── build_db.py      ← wiki/*.md → redpanda.db
│   ├── query.py         ← 家系查詢 CLI / Python API
│   ├── audit.py         ← 資料完整度檢查（與 redpanda-lineage 比對）
│   ├── apply_lineage_fixes.py ← 依 lineage 保守補齊空白欄位
│   └── schema.sql       ← SQLite schema
├── site/
│   ├── scripts/export_json.py ← redpanda.db → site/data/*.json（網站資料）
│   └── src/i18n/        ← 三語介面字串
├── web/                 ← Astro + Tailwind 網站前端（見 web/README.md）
└── wiki/
    ├── index.md         ← 目錄（依家族分類），含條目總數
    ├── log.md           ← append-only 變更日誌
    └── [slug].md        ← 個體條目（每隻一頁）
```

**真相來源是 `wiki/*.md`**；`redpanda.db`、`site/data/*.json`、網站都是衍生資料。
改完 wiki 後重建：`python3 tools/build_db.py`（DB）→ `python3 site/scripts/export_json.py`（網站資料）。
網站本身由 GitHub Actions 自動建置部署；本地預覽見 `web/README.md`。

---

## 任何工作開始前

1. 讀 `SCHEMA.md`（格式規範）
2. 讀 `wiki/index.md`（確認條目是否已存在，避免重複）
3. 讀 `wiki/log.md` 最後幾筆（了解近況與日誌格式）

**先讀後寫**：條目已存在就用 Edit 更新（log 記為 `update`），絕不覆蓋。

---

## 條目格式重點

完整規範見 `SCHEMA.md` 與 `rpf-wiki-SKILL.md`，關鍵摘要：

- **YAML frontmatter** 必填：`name`、`sex`、`born`、`species`、`zoos`、`rpf_id`、`rpf_url`、`tags`、`sources`；`japanese`、`nicknames`、`english_variants`、`died` 視情況。
- **內容結構**：標題 → 引言區塊（性別/生日/現居）→ 一句話家族背景 → `## 居住史`（表格）→ `## 家族`（父母/雙胞胎/兄弟姊妹/子女）。
- **wikilink**：對方已有條目才用 `[[slug]]`，否則純文字。已故加 🌈。½ 表半血緣。
- **語言**：條目內文用中文，動物園名沿用日文原名。

### 檔名與消歧（重要）

slug 全小寫、空格換連字號。小熊貓名字極常重複：

- 名字常見（Yan-Yan、Fu-Fu、Ten-Ten…）→ 加父名：`yan-yan-franken.md`
- 同名並存 → 必須消歧，條目內加 `⚠️ 注意同名` 提示
- 名字夠獨特 → 單名即可（`akebi.md`）
- 不確定時優先加父名

---

## 新增成員流程

1. 從 RPF 抓資料（用 Claude in Chrome，詳見 `rpf-wiki-SKILL.md` 第二步；RPF 不標性別，需從 Mother/Father/daughters/sons 推斷）
2. 建立 `wiki/[slug].md`
3. **自動補齊直系親屬**：父、母、雙胞胎、子女、兄弟姊妹、祖父母，若無條目一律建立（順序：主角→父→母→雙胞胎→子女）
4. 回頭把相關既有條目的純文字親屬改成 `[[wikilink]]`
5. 更新 `wiki/index.md`：加入適當分類、更新頁首「最後更新」與「條目總數」
6. 在 `wiki/log.md` 末端 append 一筆記錄
7. 重跑 `python3 tools/build_db.py`
8. 跑 `python tools/audit.py` 檢查資料完整度（缺欄位、與 lineage 不符等）；網站資料則重跑 `python3 site/scripts/export_json.py`

### ⚠️ log.md 絕對禁止 `[[wikilink]]`

否則 Obsidian graph 會把 log 變成中心節點。名字一律用 backtick：`` `yuuta` ``。`#72`、`RPF #23` 等數字寫法安全，可放心使用。

log 格式：

```markdown
## [YYYY-MM-DD] add | 說明

**來源**：
- https://redpandafinder.com/#profile/XXX (名字)

**新增條目**：
- `slug.md` — 名字 日文名（RPF #XXX），生於 YYYY-MM-DD，現居 動物園

**更新條目**：
- `index.md` — 新增 XXX；條目總數更新為 N
```

---

## 查詢

- 簡單查詢：先看 `wiki/index.md`，再開個別條目
- 家系/血緣查詢用 SQLite 工具（在 wiki 根目錄執行）：

```bash
python3 tools/build_db.py              # 重建 DB（改過 wiki 後必跑）
python tools/query.py profile kiki    # 個體完整資料
python tools/query.py ancestors taofa # 所有祖先
python tools/query.py descendants kiki
python tools/query.py common taofa franken  # 共同祖先（近親偵測）
python tools/query.py zoo "Nagano"    # 某動物園的個體
python tools/query.py pairing ako     # 配對候選分析
```

DB 寫入若失敗（沙盒掛載不支援 SQLite lock），build_db.py 會自動 fallback 到 `/tmp/redpanda.db`。

---

## 注意事項

- 日期一律 ISO（YYYY-MM-DD）；只知年份就只寫年份
- RPF 的 Other Names 記得填入 `japanese` / `english_variants`
- 性別推斷不確定時留空並備注「待確認」
- 不要動 `.obsidian/`；`test.db`、`Untitled.canvas` 為雜物，可忽略
- 條目總數以 `ls wiki/*.md | wc -l` 減去 `index.md`、`log.md` 驗證，別只憑 index 頁首數字
