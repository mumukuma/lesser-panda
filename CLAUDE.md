# CLAUDE.md — 小熊貓家族 Wiki 操作手冊

本資料夾是一個依 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)運作的 Obsidian wiki：**LLM 負責撰寫與維護所有頁面，使用者負責提供資料來源與問問題**。

主題：小熊貓（red panda）個體檔案，目前 600+ 條目（精確數以 `wiki/index.md` 頁首為準），多為日本（及部分海外）動物園個體。

## ⚠️ 資料來源原則（重要）

- **`wiki/*.md` 是唯一正本與權威來源**，由作者校訂。
- **RPF/lineage 降為「線索」（2026-07-14 起）**：[Red Panda Finder](https://redpandafinder.com)（RPF）與 [redpanda-lineage](https://github.com/wwoast/redpanda-lineage) 雜訊多，wiki 經作者大量校訂後可信度已**高於**兩者。它們不再是「基礎參考」，僅在**無官方來源時**當線索用；由 RPF/lineage 帶入而未經官方佐證的關鍵資料標 `🚧 待查證`。新條目 `sources` 以園方公告等官方來源優先，RPF 為輔。
- 兩者衝突時，**一律以 wiki（作者的校訂）為準**，不可用 RPF/lineage 覆蓋既有資料；與 lineage 的「不符」不代表 wiki 錯、不需逐筆處理。
- 工具配套（2026-07-14 起）：`audit.py` **預設不跑 lineage 比對**（加 `--lineage` 才比對）；`verify.sh`（pre-push）不再抓取 lineage、只跑 wiki 自身檢查；`apply_lineage_fixes.py` **僅作者明確要求時才執行**（只填空欄位、不覆蓋，補入值視同線索）。**`audit.py` 的「缺 rpf_id」列為 ⚪ info、非黃燈警告（2026-07-20 起）**：RPF 為線索非指標，中國個體／蘋果籽佔位／官方來源建檔者本就常無 RPF profile，缺 rpf_id 不是資料缺陷、不應被當成專案覆蓋率指標；真正擋 push 的仍只有「rpf_id 重複」（🔴 整合性錯誤）與 `check_twins` 的 E 級。
- 名稱（尤其中文名 `chinese`、暱稱、別名）以作者提供為準；RPF 的羅馬拼音僅作後備。
- **lineage/RPF 的 `ja.name` 是機械轉寫、每隻個體都有（不論來源地），僅「有日本居住史」的個體才採用為 `japanese`**（2026-07-13 起）：歐美等非日本個體一律不抄——其 `ja.name` 若含漢字，多半實為中文名（例：Hui Hu 的「火狐」），應由作者確認後放 `chinese`，而非 `japanese`。工具已內建此規則：`audit.py` 的「lineage 有漢字名、wiki 未收」提示與 `apply_lineage_fixes.py` 的補漢字，都只對 frontmatter `zoos:` 解析出含日本園（`data/zoos.json` 的 `country == "Japan"`）的個體生效；`zoos:` 空白無法確認國別時保守不補。
- **動物園名以 `data/zoos.json`（註冊表）為唯一事實來源**：每座園的正式名（`canonical`，採完整正式名）、中文名、座標、官網、logo、**地點（`location_ja`）**、**休園日（`closed_ja`，選填，照官網原文精簡一行、僅官方來源可填，缺值園頁不顯示；另有機器可讀衍生欄 `closed_rule` 供首頁「今日休園」計算——`closed_ja` 是人讀正本，某園休園制度改了兩欄必須同步改，不定休／営業カレンダー制與年中無休的園不編 `closed_rule`）** 只存這裡。wiki 條目（frontmatter `zoos:` 與內文居住史）一律寫 canonical 日文名；`build_db` 會精確比對，**寫了註冊表沒有的園名就報錯中止**（提示去登記或修正）。新增一座沒登記過的園 → 先在 `data/zoos.json` 加一筆，再寫條目。lineage 僅用來初次帶入座標，非權威。
- **地點（`location_ja`）也以 `data/zoos.json` 為準**：`gen_residence.py` **只補空白、永不覆寫**既有校訂值（2026-06-29 起）。要改某園地點 → 直接編輯 `data/zoos.json` 的 `location_ja` 再重建；內文居住史的「地點」欄由註冊表自動帶入，勿手改。

---

## 目錄結構

```
red-panda-wiki/
├── CLAUDE.md            ← 本文件（操作手冊）
├── SCHEMA.md            ← 頁面格式與標籤規範（權威來源）
├── README.md            ← 專案總覽（對外）
├── ROADMAP.md           ← 願望池與路線規劃
├── CHANGELOG.md         ← 專案層級變更（工具／流程；wiki 內容變更記 wiki/log.md）
├── rpf-wiki-SKILL.md    ← RPF 抓取資料 → 建立條目的詳細 skill
├── report-intake-SKILL.md ← 社群回報（Tally→Sheet）處理 skill
├── redpanda.db          ← 由 wiki/*.md 產生的 SQLite（衍生品，可重建）
├── data/
│   └── zoos.json        ← 動物園註冊表（唯一事實來源，作者維護；園名/中文/座標/官網/別名）
├── docs/                ← 作業文件（回報處理 SOP、表單藍圖、計劃等）
├── sources/             ← 官方一手資料的本地留存（如園報、家系名單）
├── tools/
│   ├── wiki_io.py       ← 共用讀取層：frontmatter 解析＋日期正規化（唯讀解析一律用這裡，勿自造 parser）
│   ├── build_db.py      ← wiki/*.md → redpanda.db（建檔時把園名解析為註冊表 canonical，未登記報錯）
│   ├── zoo_registry.py  ← 載入 data/zoos.json 並提供園名比對 resolver
│   ├── gen_residence.py ← 由 frontmatter zoos: 自動生成內文「## 居住史」表格（勿手改該表）
│   ├── query.py         ← 家系查詢 CLI / Python API
│   ├── audit.py         ← 資料完整度檢查；缺 rpf_id 列為 ⚪ info（非警告，RPF 為線索非指標）；--strict 時僅內部錯誤（如 rpf_id 重複）回傳非零；--lineage 才比對 lineage（預設不跑）
│   ├── check_twins.py   ← 多胞胎稽核（同生群同父母／生日±1天／群大小）；E 級錯誤回傳 1
│   ├── ig_audit.py      ← 盤點 instagram: 連結（格式／活性提示，只報不改，exit 恆 0）
│   ├── verify.sh        ← 驗證單一關卡：audit --strict + check_twins（只讀；已掛 pre-push；不再抓 lineage）
│   ├── apply_lineage_fixes.py ← 依 lineage 保守補齊空白欄位
│   ├── resolve_zoo.py   ← 簡稱／部分名 → 註冊表 canonical 的省核輔助 CLI（不改 wiki）
│   ├── schema.sql       ← SQLite schema
│   └── art/             ← 吉祥物／sprite 圖像生成腳本（與資料管線無關，不進 rebuild）
├── pipeline/
│   ├── scripts/export_json.py ← redpanda.db → pipeline/data/*.json（網站資料）
│   └── src/i18n/        ← 五語介面字串（zh-TW／zh-CN／ja／en／ko）
├── web/                 ← Astro + Tailwind 網站前端（見 web/README.md）
└── wiki/
    ├── index.md         ← 目錄（依家族分類），含條目總數
    ├── log.md           ← append-only 變更日誌（只留近期月份，舊月份封存至 log-archive/）
    ├── log-archive/     ← log.md 按月封存（log-YYYY-MM.md；glob 非遞迴自動排除）
    ├── _hidden/         ← 暫時下架的條目（不計數、不上站；glob 非遞迴自動排除）
    └── [slug].md        ← 個體條目（每隻一頁）
```

**真相來源是 `wiki/*.md`**；`redpanda.db`、`pipeline/data/*.json`、網站都是衍生資料。
改完 wiki 後重建：`python3 tools/gen_residence.py`（依 `zoos:` 重生居住史表格）→ `python3 tools/build_db.py`（DB）→ `python3 pipeline/scripts/export_json.py`（網站資料）。一鍵版：在 repo 根目錄執行 `bash rebuild.sh` 即依序跑完這三步。
`gen_residence.py` **以 frontmatter `zoos:` 為居住史唯一來源**（2026-06-29 起）：有 `zoos:` 就以它為準（解析完整日期），內文「## 居住史」表格純為衍生、自動重生。守門以 frontmatter 園集合為基準自我比對，重生後若掉了任何園（如解析失敗）就中止；故**更正／更換居住地只需改 `zoos:` 一處**再重建，不用動內文表格。（早期版本曾以內文表格為來源，已修正。）
網站本身由 GitHub Actions 自動建置部署；本地預覽見 `web/README.md`。

**網站語系（2026-07-05 起五語）**：介面支援 `zh-TW`／`zh-CN`（簡體）／`ja`／`en`／`ko`（韓語）。語系定義集中在 `web/src/lib/data.js` 的 `LOCALES` 與 `i18n`；每語一份 `pipeline/src/i18n/<code>.json`，五份 key 必須一致（新增字串要五份都補）。加語系＝新增一份 json＋在 `data.js` 註冊＋`web/public/js/lang.js` 加瀏覽器偵測。因網站為資料驅動、個體頁無敘述文，加語系只翻 UI 字串、不必翻 600+ 條目。韓語的設計取捨：**動物園名暫用英文**（`data/zoos.json` 已預留 `ko_name` 欄，補了即自動生效）、**個體名走羅馬拼音**、**回報表單維持三語**（下方表單章節；ko 自動 fallback 到三語表單）。簡體的設計取捨（2026-07-05）：**純顯示層轉換、資料正本一律維持繁體**——個體中文名、園中文名於建置時用 `opencc-js`（繁→簡，`data.js` 的 `toHans`）轉換，前端內嵌資料（SEARCH_DATA 的 `k`、GRAPH_DATA 的 `d[5]`、ZOOS_DATA 的 `name_zh_hans`）也在建置時預轉，客戶端不帶 OpenCC；UI 字串為手工翻譯的 `zh-CN.json`（用語照大陸慣例：搜索／链接／帖子…）；**回報表單 fallback 到三語表單**；語言偵測 IP=CN→zh-CN、瀏覽器 zh-cn/zh-sg/zh-my/zh-hans→zh-CN、其餘 zh→zh-TW。

**push 前驗證（單一關卡，2026-06-29 起；2026-07-14 簡化）**：`bash tools/verify.sh` 依序跑「`audit.py --strict` → `check_twins.py`」（不再抓取／比對 lineage；要比對請手動 `python3 tools/audit.py --lineage`）。已掛 `.git/hooks/pre-push`，**push 前自動跑、未通過即中止 push**。擋關原則符合資料來源原則：只有「真正的 wiki 整合性錯誤」會擋（`audit` 的 `rpf_id` 重複、`check_twins` 的 E 級——連錯隻／同生群生日差>±1天／群過大）；缺欄位、單邊缺父母等只列提示、**永不擋**。緊急要略過：`git push --no-verify`。注意 hook 在 `.git/hooks/` 內、**不進版控**，換機器需重裝（`verify.sh` 本身有進版控）。

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
- **wikilink**：對方已有條目才用 `[[slug]]`，否則純文字。已故加 🪐。½ 表半血緣。
- **語言**：條目內文用中文，動物園名沿用日文原名。

### 檔名與消歧（重要）

**slug 一律為「名字-生日」**（2026-06-18 起，全部條目適用）。小熊貓名字極常重複，生日是個體本身的屬性、比父名穩定，故用生日當固定後綴：

- 格式：`slugify(name)` + `-` + 生日。生日用完整 `YYYY-MM-DD`；只知年份則用 `YYYY`。
  - 例：`yan-yan-2014-06-22.md`、`akebi-2020-06-29.md`、`tian-1999.md`（只知年份）
- slugify：全小寫、空白/底線換連字號、去除 `'`、`()`、`.`；**重音字母轉為對應基本拉丁字母（不可整個刪掉）**，作法為 NFKD 正規化後去掉組合附加符號（é→e、ó→o、ú→u、ñ→n…）。例：`Ke Song`→`ke-song`、`Pu'erh`→`puerh`、`Réra`→`rera`、`Miró`→`miro`、`Kelú`→`kelu`。
- **撞名（同名又同生日）才加第三層消歧 = 媽媽的名字**（slug），**不用父名**。
  - 例：兩隻 Sora 都生於 2008-06-16 → `sora-seina-2008-06-16`（母 seina）、`sora-nami-2008-06-16`（母 nami）
- 佔位名字**一律**用「名字-媽媽名-生日」，待正式命名後再改 slug。當季新生寶寶的佔位用「蘋果籽」制度（見下節）；早期少數條目用 `Baby`（如 `_hidden/` 內幼逝者），沿用不改。
- 同名並存時，條目內仍加 `⚠️ 注意同名` 提示。
- slug 可由 `name`+`born` 機械重建；日後若校訂某隻生日，需一併更名並修正所有 `[[wikilink]]`。

### 當季寶寶佔位條目：蘋果籽（2026-07-14 起）

每年夏天是北半球小熊貓寶寶出生季，園方多半公布出生後隔一陣子才命名。命名前可先建「**蘋果籽**」佔位條目，**直接上站**，讓訪客看得到當季新寶寶。

**建檔資格（四項全符合才建）**：

1. **父母皆已確認**（母、父都對得上既有條目，或可依新增成員流程一併建檔）
2. **生日已確認**（完整 `YYYY-MM-DD`，以園方公告或 RPF 為據）
3. **尚在世**（公告時已夭折者不建蘋果籽；佔位期間夭折 → 照 2026-07-02 慣例補 `died`＋`deceased` 後移入 `wiki/_hidden/`）
4. **尚未正式命名**（已有正式名就直接用正式名建檔，不經蘋果籽）

**命名與 slug**：

- `name: Apple Seed`、`chinese: 蘋果籽`；`japanese` **留空**（園方的「赤ちゃん」是泛稱、非名字，正式命名後才填）
- slug **一律含媽媽名**：`apple-seed-媽媽slug-生日`（所有蘋果籽同名，直接套佔位名消歧規則）。例：`apple-seed-kiku-2026-06-20`
- **同胎多隻**同時佔位才編號：`chinese` 寫 `蘋果籽1號`、`蘋果籽2號`…、`name: Apple Seed 1`…，slug 為 `apple-seed-1-媽媽slug-生日`。序號依園方公布順序；未公布則依 RPF ID 由小到大。單胎不編號。

**frontmatter 其他欄位**：

- `sex:` 留空、tags 不加性別，內文備注「性別待確認」；之後園方公布性別即回補（`sex`＋性別 tag）
- `zoos:` 出生園 `(生日 – )`（現居，訖留空）
- `rpf_id`／`rpf_url`：RPF 已建檔就填；還沒有就先缺（audit 只提示不擋），之後補上
- `tags:` **必含 `apple-seed`**（佔位追蹤用，轉正時移除）
- `sources:` 園方公告優先（官方來源可直接採用），RPF 為輔

**內文**：標題 `# 蘋果籽（Apple Seed）— [[媽媽]] × [[爸爸]] 之寶寶`，引言區塊前加：

> ⚠️ 佔位條目：寶寶尚未正式命名、性別待確認，暫以「蘋果籽」稱之，園方公布正式名後改名。

其餘照一般條目結構；index、log、親屬雙向 wikilink、rebuild 均照「新增成員流程」。

**轉正流程（園方公布正式名後）**：

1. 依正式名重命名 slug 為 `名字-生日`（撞名才留媽媽名），全 wiki `[[wikilink]]` 同步更換
2. frontmatter 更新 `name`／`japanese`（日本個體）／`chinese` 等，**移除 `apple-seed` tag**；性別已公布則一併補 `sex` 與性別 tag
3. 內文移除佔位提示、改寫標題與引言；更新 `index.md`；`log.md` 記一筆 `rename`（舊 slug 用 backtick，禁 wikilink）
4. `bash rebuild.sh`

**季末盤點**：每年 10 月起以 `grep -l "apple-seed" wiki/*.md` 盤點尚未轉正的蘋果籽，逐隻查園方是否已公布名字；跨年仍未命名者留佔位、不強改。

### 資料有限個體：檔案卡（2026-07-17 起，主要用於中國個體）

中國園常無公告即轉移個體、不公布生日與家系、也不公告死亡，等資料齊全再建檔等於永遠不建。改採「**證據快照**」模式：記錄「確認過什麼、何時確認」，不宣稱全貌。

**建檔門檻（兩項皆符合才建）**：

1. **官方來源確認存在**（園方官網／官方微信公眾號文章等，見「官方來源可直接採用」標準）——至少一筆可核對的來源。**例外（2026-07-17 作者裁定）**：讀者實拍的**園方展牌**等一手實體資料（作者可於回報收件匣核對附件）亦可滿足此要件，但屬「其他補充資料」、記入 `extra_sources` 欄（與官方鏈結的 `sources` 分開），不進個體頁官方來源區塊
2. **至少對得上一座園**（該園須已登記於 `data/zoos.json`）

只有名字、一次目擊、來源開不了的 → 不建條目，先記入候補名單 `data/cn-candidates.json`（見下），累積到符合門檻再轉正。

**frontmatter 規則**：

- `born:` 只填有據的粒度：`YYYY-MM-DD`／`YYYY`／完全未知就**留空**（audit 只提示不擋）
- `last_seen:` **必填**——最後一次由來源確認在世／在園的日期（粒度隨來源：`YYYY-MM-DD`／`YYYY-MM`／`YYYY`），佐證放 `sources`。**動向不明不猜 `died`**，用 `last_seen` 誠實記錄；日後查到死訊再補 `died` 並移除過時描述
- `tags:` **必含 `limited-profile`**（檔案卡追蹤用）；若**動向不明**（最後確認距今約 2 年以上、無法佐證現存）**再加 `unverified`**——網站會排除現存統計並顯示待查證標記，避免「看似現居、實則失聯」誤導
- `zoos:` 只登**有佐證**出現過的園；**起始年一律填「首次確認年份」、不可留空**（留空會被 `gen_residence` 誤標 🐣 出生地）。確知是出生園才可用出生年。動向不明者現居訖可留空（配合 `unverified`），已確認離園（他園目擊）則訖填該園最後確認年
- `rpf_id`／`rpf_url`：中國個體 RPF 覆蓋率低，通常缺（audit 提示不擋），之後有再補
- `sex:` 不確定就留空並備注「待確認」（照既有慣例）

**slug**：

- 有生日（含只知年份）→ 照標準規則 `名字-生日`
- **完全無生日 → `slugify(name)-園簡稱`**：園簡稱用首次確認所在園的英文簡稱（慣例用城市名，如 `xiao-bai-shanghai`）；同園撞名再加序號或其他消歧。查到生日後照 rename 流程改回標準 slug（改檔名＋全 wiki `[[wikilink]]`＋log 記 `rename`）
- 中文名繁簡並列照既有慣例（`chinese` 單值、標題引言寫 繁／简）

**內文**：照一般條目結構，引言區塊加一行「**最後確認**：YYYY-MM（來源），其後動向不明」（動向不明者）；家系不明就在 `## 家族` 寫「父母不詳（園方未公布）」，勿從 RPF/lineage 腦補。

**盤點**：不定期以 `grep -l "limited-profile" wiki/*.md` 盤點，逐隻搜園方微信有無新目擊／死訊／轉園；有新確認就更新 `last_seen`（log 記 `update`）。

**候補名單 `data/cn-candidates.json`**：不夠格建條目的線索池，格式為陣列，每筆
`{"name": "中文名", "zoo": "canonical 園名", "seen": "YYYY-MM-DD", "source": "URL", "note": "備注"}`；
轉正建檔後把該筆刪除。此檔僅為工作用線索、不進 DB、不上站。

---

## 新增成員流程

1. 從 RPF 抓資料（用 Claude in Chrome，詳見 `rpf-wiki-SKILL.md` 第二步；RPF 不標性別，需從 Mother/Father/daughters/sons 推斷）。RPF 僅為線索：有官方來源的欄位以官方為準，`sources` 官方優先
2. 建立 `wiki/[slug].md`
3. **自動補齊直系親屬**：父、母、雙胞胎、子女、兄弟姊妹、祖父母，若無條目一律建立（順序：主角→父→母→雙胞胎→子女）
4. 回頭把相關既有條目的純文字親屬改成 `[[wikilink]]`
5. 更新 `wiki/index.md`：加入適當分類、更新頁首「最後更新」與「條目總數」
6. 在 `wiki/log.md` 末端 append 一筆記錄
7. 重跑 `python3 tools/build_db.py`
8. 跑 `python tools/audit.py` 檢查資料完整度（缺欄位等；lineage 比對預設不跑，需要時加 `--lineage`）；網站資料則重跑 `python3 pipeline/scripts/export_json.py`

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

**處理流程**：累積一批回報後 → 從對應的 Google Sheet 拉資料 → 依需要正規化「類型」下拉的混語值（例：`生日／誕生日／Birthday` 視為同一類）→ 查證 → 採用者照「新增成員流程」更新 wiki → **最後一步（勿漏）：補致謝名單**——凡本批「已採用」的回報，回報者若留了暱稱（表單「你的暱稱（想列入致謝可留）」欄，留名視同同意署名），檢查 `data/contributors.json`，尚未在名單者加一筆（`name` 必填，`note` 註明回報內容與年月）；已在名單者不重複列。未留名或未採用者不加。

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
>
> **查證省時原則（2026-07-06 起）**：回報所附來源**非官方**（或未附來源）時，**不必花時間自行搜尋替代佐證**——直接標 `🚧 待查證` 列出即可。只有回報本身附了官方來源、但連結打不開時，才值得順手搜官方替代（如官媒轉載）；搜一輪沒有就停。

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
- RPF 的 Other Names 記得填入 `japanese`（**僅日本個體**，見資料來源原則）/ `english_variants`
- 性別推斷不確定時留空並備注「待確認」
- 不要動 `.obsidian/`
- **log.md 按月封存**：`wiki/log.md` 只留近期月份，過往月份移至 `wiki/log-archive/log-YYYY-MM.md`（換月後擇機搬移；append 一律仍寫 log.md 末端，封存檔同樣禁 wikilink）
- 條目總數以 `ls wiki/*.md | wc -l` 減去 `index.md`、`log.md` 驗證，別只憑 index 頁首數字
- **⏰ 內嵌日期表續期（到期前要更新）**：`web/public/js/closed.js` 的日本祝日表只涵蓋 **2026–2030**（表外年份視為無祝日，「今日休園」的祝日順延會失準）——**2030 年內要續期**：用 `pip install jpholiday` 重新產生後續年份（含振替休日・国民の休日）、對照内閣府等官方來源抽驗，加進 `HOLIDAYS` 並跑 `node web/tests/closed.test.mjs`。另 `web/public/js/season.js` 的節氣表涵蓋 2026–2035（表外借最近一年、僅 UI 換色，較不急），2035 年前擇機續期。
- **幼逝寶寶收錄原則（2026-07-14 起）**：出生後未滿一歲即夭折的個體，**只要有正式命名就照常收錄、上站**（如 `takeru`、`tsubasa`、`wu-tan`）；唯有從未取名、僅以佔位名（如 `Baby`／`赤ちゃん`）登錄者，才移入 `wiki/_hidden/` 暫藏。此規則**取代** 2026-07-02「未滿一歲一律暫藏」的舊做法。（注意：因其他原因暫藏者不受此規則影響，如資料未經核實的 `sokka`。）
