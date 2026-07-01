# CLAUDE.md — 小熊貓家族 Wiki 操作手冊

本資料夾是一個依 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)運作的 Obsidian wiki：**LLM 負責撰寫與維護所有頁面，使用者負責提供資料來源與問問題**。

主題：小熊貓（red panda）個體檔案，目前 360+ 條目，多為日本（及部分海外）動物園個體。

## ⚠️ 資料來源原則（重要）

- **`wiki/*.md` 是唯一正本與權威來源**，由作者校訂。
- [Red Panda Finder](https://redpandafinder.com)（RPF）與 [redpanda-lineage](https://github.com/wwoast/redpanda-lineage) 只是**初期建立資料的基礎參考**，**非權威**。
- 兩者衝突時，**一律以 wiki（作者的校訂）為準**，不可用 RPF/lineage 覆蓋既有資料。
- `tools/audit.py`、`tools/apply_lineage_fixes.py` 與 lineage 的比對僅供**參考與補空白**；`apply_lineage_fixes` 只填空欄位、不覆蓋；audit 列出的「與 lineage 不符」是提示作者**檢視**，不代表 wiki 錯。
- 名稱（尤其中文名 `chinese`、暱稱、別名）以作者提供為準；RPF 的羅馬拼音僅作後備。
- **動物園名以 `data/zoos.json`（註冊表）為唯一事實來源**：每座園的正式名（`canonical`，採完整正式名）、中文名、座標、官網、logo、**地點（`location_ja`）** 只存這裡。wiki 條目（frontmatter `zoos:` 與內文居住史）一律寫 canonical 日文名；`build_db` 會精確比對，**寫了註冊表沒有的園名就報錯中止**（提示去登記或修正）。新增一座沒登記過的園 → 先在 `data/zoos.json` 加一筆，再寫條目。lineage 僅用來初次帶入座標，非權威。
- **地點（`location_ja`）也以 `data/zoos.json` 為準**：`gen_residence.py` **只補空白、永不覆寫**既有校訂值（2026-06-29 起）。要改某園地點 → 直接編輯 `data/zoos.json` 的 `location_ja` 再重建；內文居住史的「地點」欄由註冊表自動帶入，勿手改。

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
├── data/
│   └── zoos.json        ← 動物園註冊表（唯一事實來源，作者維護；園名/中文/座標/官網/別名）
├── tools/
│   ├── build_db.py      ← wiki/*.md → redpanda.db（建檔時把園名解析為註冊表 canonical，未登記報錯）
│   ├── zoo_registry.py  ← 載入 data/zoos.json 並提供園名比對 resolver
│   ├── gen_residence.py ← 由 frontmatter zoos: 自動生成內文「## 居住史」表格（勿手改該表）
│   ├── query.py         ← 家系查詢 CLI / Python API
│   ├── audit.py         ← 資料完整度檢查（與 redpanda-lineage 比對）；--strict 時僅內部錯誤（如 rpf_id 重複）回傳非零
│   ├── check_twins.py   ← 多胞胎稽核（同生群同父母／生日±1天／群大小）；E 級錯誤回傳 1
│   ├── verify.sh        ← 驗證單一關卡：lineage 更新 + audit --strict + check_twins（只讀；已掛 pre-push）
│   ├── apply_lineage_fixes.py ← 依 lineage 保守補齊空白欄位
│   ├── resolve_zoo.py   ← 簡稱／部分名 → 註冊表 canonical 的省核輔助 CLI（不改 wiki）
│   ├── schema.sql       ← SQLite schema
│   └── art/             ← 吉祥物／sprite 圖像生成腳本（與資料管線無關，不進 rebuild）
├── pipeline/
│   ├── scripts/export_json.py ← redpanda.db → pipeline/data/*.json（網站資料）
│   └── src/i18n/        ← 四語介面字串（zh-TW／ja／en／ko）
├── web/                 ← Astro + Tailwind 網站前端（見 web/README.md）
└── wiki/
    ├── index.md         ← 目錄（依家族分類），含條目總數
    ├── log.md           ← append-only 變更日誌
    └── [slug].md        ← 個體條目（每隻一頁）
```

**真相來源是 `wiki/*.md`**；`redpanda.db`、`pipeline/data/*.json`、網站都是衍生資料。
改完 wiki 後重建：`python3 tools/gen_residence.py`（依 `zoos:` 重生居住史表格）→ `python3 tools/build_db.py`（DB）→ `python3 pipeline/scripts/export_json.py`（網站資料）。一鍵版：在 repo 根目錄執行 `bash rebuild.sh` 即依序跑完這三步。
`gen_residence.py` **以 frontmatter `zoos:` 為居住史唯一來源**（2026-06-29 起）：有 `zoos:` 就以它為準（解析完整日期），內文「## 居住史」表格純為衍生、自動重生。守門以 frontmatter 園集合為基準自我比對，重生後若掉了任何園（如解析失敗）就中止；故**更正／更換居住地只需改 `zoos:` 一處**再重建，不用動內文表格。（早期版本曾以內文表格為來源，已修正。）
網站本身由 GitHub Actions 自動建置部署；本地預覽見 `web/README.md`。

**網站語系（2026-07-01 起四語）**：介面支援 `zh-TW`／`ja`／`en`／`ko`（韓語）。語系定義集中在 `web/src/lib/data.js` 的 `LOCALES` 與 `i18n`；每語一份 `pipeline/src/i18n/<code>.json`，四份 key 必須一致（新增字串要四份都補）。加語系＝新增一份 json＋在 `data.js` 註冊＋`web/public/js/lang.js` 加瀏覽器偵測。因網站為資料驅動、個體頁無敘述文，加語系只翻 UI 字串、不必翻 360+ 條目。韓語的設計取捨：**動物園名暫用英文**（`data/zoos.json` 已預留 `ko_name` 欄，補了即自動生效）、**個體名走羅馬拼音**、**回報表單維持三語**（下方表單章節；ko 自動 fallback 到三語表單）。

**push 前驗證（單一關卡，2026-06-29 起）**：`bash tools/verify.sh` 會依序跑「更新 redpanda-lineage → `audit.py --strict` → `check_twins.py`」。已掛 `.git/hooks/pre-push`，**push 前自動跑、未通過即中止 push**。擋關原則符合資料來源原則：只有「真正的 wiki 整合性錯誤」會擋（`audit` 的 `rpf_id` 重複、`check_twins` 的 E 級——連錯隻／同生群生日差>±1天／群過大）；與 lineage 的「不符」、缺欄位、單邊缺父母等只列提示、**永不擋**。離線時自動略過 lineage 比對，wiki 自身檢查照跑。緊急要略過：`git push --no-verify`。注意 hook 在 `.git/hooks/` 內、**不進版控**，換機器需重裝（`verify.sh` 本身有進版控）。

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
- **內容結構**：標題 → 引言區塊（性別/生日/現居）→ 一句話家族背景 → `## 居住史`（**自動生成表格，勿手改**）→ `## 家族`（父母/雙胞胎/兄弟姊妹/子女）。
- **居住史唯一來源是 frontmatter `zoos:`**，格式 `園名 (起 – 訖)`，起訖可用 `YYYY-MM-DD`／`YYYY`／現居留空（訖寫「現在」或空）。內文 `## 居住史` 表格由 `tools/gen_residence.py` 從此生成（含地點、🐣出生地、🏡現居），改居住史一律改 `zoos:` 再重跑該工具。
- **wikilink**：對方已有條目才用 `[[slug]]`，否則純文字。已故加 🌈。½ 表半血緣。
- **語言**：條目內文用中文，動物園名沿用日文原名。

### 檔名與消歧（重要）

**slug 一律為「名字-生日」**（2026-06-18 起，全部條目適用）。小熊貓名字極常重複，生日是個體本身的屬性、比父名穩定，故用生日當固定後綴：

- 格式：`slugify(name)` + `-` + 生日。生日用完整 `YYYY-MM-DD`；只知年份則用 `YYYY`。
  - 例：`yan-yan-2014-06-22.md`、`akebi-2020-06-29.md`、`tian-1999.md`（只知年份）
- slugify：全小寫、空白/底線換連字號、去除 `'`、`()`、`.`；**重音字母轉為對應基本拉丁字母（不可整個刪掉）**，作法為 NFKD 正規化後去掉組合附加符號（é→e、ó→o、ú→u、ñ→n…）。例：`Ke Song`→`ke-song`、`Pu'erh`→`puerh`、`Réra`→`rera`、`Miró`→`miro`、`Kelú`→`kelu`。
- **撞名（同名又同生日）才加第三層消歧 = 媽媽的名字**（slug），**不用父名**。
  - 例：兩隻 Sora 都生於 2008-06-16 → `sora-seina-2008-06-16`（母 seina）、`sora-nami-2008-06-16`（母 nami）
- 佔位名字（如未正式命名的 `Baby`）同樣用「名字-媽媽名-生日」，待正式命名後再改 slug。
- 同名並存時，條目內仍加 `⚠️ 注意同名` 提示。
- slug 可由 `name`+`born` 機械重建；日後若校訂某隻生日，需一併更名並修正所有 `[[wikilink]]`。

---

## 新增成員流程

1. 從 RPF 抓資料（用 Claude in Chrome，詳見 `rpf-wiki-SKILL.md` 第二步；RPF 不標性別，需從 Mother/Father/daughters/sons 推斷）
2. 建立 `wiki/[slug].md`
3. **自動補齊直系親屬**：父、母、雙胞胎、子女、兄弟姊妹、祖父母，若無條目一律建立（順序：主角→父→母→雙胞胎→子女）
4. 回頭把相關既有條目的純文字親屬改成 `[[wikilink]]`
5. 更新 `wiki/index.md`：加入適當分類、更新頁首「最後更新」與「條目總數」
6. 在 `wiki/log.md` 末端 append 一筆記錄
7. 重跑 `python3 tools/build_db.py`
8. 跑 `python tools/audit.py` 檢查資料完整度（缺欄位、與 lineage 不符等）；網站資料則重跑 `python3 pipeline/scripts/export_json.py`

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

## 社群回報表單（Tally → Google Sheets 收件匣）

讀者可透過 Tally 表單回報資料更正、或回報圖鑑缺漏的小熊貓／動物園。**這些回報屬「收件匣」性質、非權威**——原則上由作者查證後，才依上方流程更新 `wiki/*.md`（wiki 仍是唯一正本）。**例外（2026-07-01 起）見下方「官方來源可直接採用」。**

每個主題各為**單一張三語表單（中／日／英並列）**，分別接到作者 Google 帳號（washimumukuma@gmail.com）的一張 Google Sheet：

| 主題 | Tally 表單 | 公開連結 | Google Sheet 收件匣 |
| --- | --- | --- | --- |
| 資料更正 | 回報資料更正（`ODr777`） | https://tally.so/r/ODr777 | 小熊貓資料回報收件匣 |
| 圖鑑缺漏 | 回報缺少的小熊貓或動物園資料（`2EVJlb`） | https://tally.so/r/2EVJlb | 圖鑑缺漏回報收件匣 |

（原本每個主題有中／日／英三張獨立表單，已於 2026-06-22 合併為單張三語表單；舊的純日／純英表單已退役刪除。）

**處理流程**：累積一批回報後 → 從對應的 Google Sheet 拉資料 → 依需要正規化「類型」下拉的混語值（例：`生日／誕生日／Birthday` 視為同一類）→ 查證 → 採用者照「新增成員流程」更新 wiki。

### 官方來源可直接採用（2026-07-01 起，作者授權）

**若回報者附上官方／一手來源，Claude 可直接採用該筆資料更新 wiki，不需再逐筆等作者確認**（仍須照常記 `sources`、更新 `log.md`、重建）。所謂官方／一手來源包括：

- 動物園官網、園方新聞稿、園報（例：日本平動物園〈でっきぶらし〉）、園方個體名單／家系圖
- 政府或官方機構公告（自治體新聞、blood registry 官方頁）
- 上述官方內容之忠實轉載（例：4travel 旅行記整段轉載多摩動物公園個體名單）——視同官方資料，但轉載可能有筆誤，發現明顯矛盾仍需判斷

**但下列情形仍須保守、標 `🚧 待查證` 或先問作者**：

- 來源為 **RPF、redpanda-lineage、個人部落格、社群貼文（X/IG）、fan wiki** 等非官方管道 → 僅作參考、不逕行覆蓋既有校訂
- 回報**未附任何來源**，或來源打不開／無法核對
- 官方來源之間、或官方來源與既有 wiki 校訂**彼此衝突**時：**以官方／園方資料為準**更新（並在 `log.md` 註明原值與改動理由）；若連官方來源都彼此打架，才留待作者裁定
- 羅馬拼音、暱稱、中文名等「命名」仍以作者提供為準（官方來源僅供拼音後備）

> 判準：Claude 開得了、且是官方或官方轉載的來源 → 可直接採用並更正（含更正既有 wiki，如 2026-07-01 緑之介歿年依多摩名單由 2019-03-12 改為 2018-03-12）。開不了或非官方 → 標待查證、必要時問作者。

注意事項：

- 表單題目與選項採三語並列，故 Sheet 的欄位標題也是三語長字串；自由填答欄位的內容語言由填答者自行決定（中／日／英混雜屬正常）。
- 改完 Tally 表單內容後，需在 Tally 按 **Publish** 才會對線上生效（編輯本身只是草稿）。
- 表單由作者經 Tally 介面維護；Claude 若要改表單需用 Claude in Chrome 操作。

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
