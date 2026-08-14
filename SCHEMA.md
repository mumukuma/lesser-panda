# 小熊貓家族 Wiki — Schema

> 本文件依照 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)設計。  
> LLM 負責撰寫與維護所有 wiki 頁面；你負責提供資料來源與問問題。

---

## 目錄結構

```
red-panda-wiki/
├── SCHEMA.md          ← 本文件（架構說明）
└── wiki/
    ├── index.md       ← 所有條目的目錄（依類別列出）
    ├── log.md         ← 新增記錄的 append-only 日誌
    └── [name]-[born].md ← 各個小熊貓的個人條目（slug = 名字-生日）
```

> **命名規則（2026-06-18 起）**：slug 一律為 `slugify(name)-生日`（生日用 `YYYY-MM-DD`，只知年份用 `YYYY`）。撞名（同名同生日）才加第三層消歧 = **媽媽的名字**（不用父名）。詳見 `CLAUDE.md`「檔名與消歧」。
>
> **當季未命名寶寶（2026-07-14 起）**：以「蘋果籽」佔位建檔——`name: Apple Seed`、`chinese: 蘋果籽`、slug **一律含媽媽名** `apple-seed-媽媽slug-生日`（同胎多隻加序號 `apple-seed-1-…`＝蘋果籽1號）、tags 必含 `apple-seed`。資格與轉正流程詳見 `CLAUDE.md`「當季寶寶佔位條目：蘋果籽」。
>
> **資料有限個體＝檔案卡（2026-07-17 起，主要用於中國個體）**：有官方來源確認存在、但生日等基本資料不明者，可建「檔案卡級」條目——`born` 只填有據的粒度（`YYYY` 或留空）、tags 必含 `limited-profile`、以 `last_seen` 記最後確認日期。**完全無生日時 slug fallback = `slugify(name)-園簡稱`**（首次確認所在園的英文簡稱，慣例用城市名，如 `xiao-bai-shanghai`）；日後查到生日即照 rename 流程改回標準 `名字-生日` slug。詳見 `CLAUDE.md`「資料有限個體：檔案卡」。

---

## 頁面格式（YAML frontmatter + Markdown）

每個個人條目的開頭必須有 YAML frontmatter：

```yaml
---
name: 英文名稱
chinese: 中文名稱        # 台灣／中國出生個體的正式中文名；中文介面優先顯示（如 可忻、丫丫）
japanese: 日文名稱（漢字 / 假名）
nicknames: [暱稱1, 暱稱2]
english_variants: [變體拼法1, 變體拼法2]
sex: female | male
born: YYYY-MM-DD
died: YYYY-MM-DD   # 若健在則省略
last_seen: YYYY-MM-DD  # 選填（檔案卡用）：最後一次由來源「確認在世／在園」的日期，粒度隨來源（YYYY-MM-DD／YYYY-MM／YYYY）。動向不明個體以此誠實記錄，不猜 died
species: Ailurus fulgens styani | Ailurus fulgens fulgens   # 亞種不詳（如走私查獲個體）→ 整行省略此欄；勿寫種名層級的 `Ailurus fulgens`，build_db 的字串比對會判成 fulgens 亞種
origin: wild | confiscated  # 選填（2026-08-13 起）：非園內出生的出身。`wild`＝野生出身（含野生捕獲與野生救護）｜`confiscated`＝走私查獲。**個體頁會在「物種」與「現居」之間多一列「出身」顯示**；園內出生者一律省略此欄、該列不出現。白名單外的值 build_db 會警告並忽略。內文措辭仍照下方〈野生／來源不明出身個體〉的三級分寸寫，不因本欄只有兩個值而放寬
zoos:                      # 居住史唯一來源（frontmatter 為準）；內文「## 居住史」表格純衍生，由 tools/gen_residence.py 自動生成、勿手改
  - 動物園名稱 (起 – 訖)     # 園名須為 data/zoos.json 註冊表 canonical（未登記 build 報錯）；起訖可用 YYYY-MM-DD / YYYY / 現居留空。更正居住地只改這裡再重建；地點欄由 data/zoos.json 的 location_ja 自動帶入
birth_zoo: unknown         # 選填：明示「首站不是出生園／出生園不詳」。居住史首站起始日不詳時本來一律被標 🐣 出生地，來源若明寫「出自不明」（如多摩個體名單的華華・中中）標了就與來源矛盾，填 unknown 即不標 🐣。查到出生園後移除此欄
mother_ref: "isb:8758"     # 選填（2026-08-14 起）：⚠️ 見下方〈幽靈親代〉。親代身分已確認、但依收錄原則
father_ref: "isb:92137"    #   不建條目（多為終生未命名者）時填此欄。值為 `isb:<番號>`（優先）或 `rpf:<id>`，
                           #   **不是 slug**。與 mother:／父：行互斥——有條目的親代一律寫在 `## 家族` 的父/母行。
siblings:                  # 選填：維護者確認為兄弟姊妹、但共同父母不詳（無法由 ## 家族 的父/母推導）時才用。列對方 slug；對稱（單邊列出即可，工具自動雙向）。網站顯示為未分血緣度的「兄弟姊妹」列。父母已知者勿用此欄——手足由共同父母自動推導
  - 對方-slug
rpf_id: RedPandaFinder 的 profile ID
rpf_url: https://redpandafinder.com/#profile/XXX
studbook_id: "94102"      # 選填（2026-08-09 起）：RPF 資料集 `/export/redpanda.json` 的 `studbook.id` 欄位（RPF 網頁 UI 不顯示）。**號碼本身已證實即國際血統登録書（ISB）番號**（2026-08-09，以 8935／8936、9177、9441／9442 三組錨點交叉驗證；ISB 2008 年版原檔存 `sources/isb-red-panda/`，對帳見 `docs/ISB-2008-對帳-2026-08-09.md`）。RPF 欄位本身仍只是索引，**佐證一律引 ISB 原檔、不引 RPF**；網站不顯示此欄。一律加引號（有前導零，如 `"0992"`）。規律：番號前兩碼＝出生年後兩碼（887 筆中 884 筆吻合）；**但野生捕獲／海外引進個體是登録年、不是出生年**（如 `taisyu-1987`／`rin-rin-1987` 為連號 8935／8936＝1989 入園年，ISB 記其生年為 `~1987`），推定生年時只能當「不晚於該年出生」的下限
tags: [標籤]
instagram:                # 選填：同好的公開 IG 貼文連結，網站以官方 embed 展示（自動署名、連回原貼文）
  - https://www.instagram.com/帳號/p/XXXXXXXXX/ 2025-06-01   # 建議用含「帳號」的完整形式；可在連結後加貼文日期，網站依日期新到舊排序；超過 6 篇自動「顯示更多」
youtube:                  # 選填（2026-08-05 起）：值得「展示」的公開 YouTube 影片。個體頁「照片與影片」區的影片分頁以縮圖卡片顯示、點擊才載入播放器
  - https://www.youtube.com/watch?v=XXXXXXXXXXX 2012-03-25   # watch／youtu.be／shorts 形式皆可；可在連結後加影片日期（新到舊排序）；行末 YAML 註解記標題／頻道
sources:
  - https://redpandafinder.com/#profile/XXX
extra_sources:           # 選填：其他參考資料——非官方但值得留存的線索，與官方 sources 分開管理。網站個體頁於「來源」下方另闢「其他參考資料」區塊顯示（2026-08-02 起）
  - https://xxx.exblog.jp/12345678/  # 同好部落格、YouTube 影片等：**只放可點的 URL**，行末以 YAML 註解記標題／日期／看點
  # ⚠️ 2026-08-05 起：無法線上核對的一手佐證（讀者實拍展牌、實體園報掃描等）**不寫進 extra_sources**，
  #    改寫在條目內文／「## 備注」段落（含展牌原文引述）。個體頁的「其他參考資料」只呈現 URL；
  #    非 URL 項目會被 web/src/components/Panda.astro 過濾掉、不顯示。
---
```

> `instagram` 為選填。只放**公開**貼文連結；網站用 Instagram 官方 embed 顯示，會自動標註原作者並連回原貼文（不複製圖片檔）。新增後重跑 `build_db.py` → `export_json.py` 即生效。
>
> `youtube` 為選填（2026-08-05 起）。放**值得展示的**公開 YouTube 影片；網站在個體頁「照片與影片」區的**影片分頁**以縮圖卡片顯示（點擊才載入 youtube-nocookie 播放器，連回原影片、顯示頻道署名）。兩種來源都有才顯示分頁列；只有一種就顯示單一區塊。**與 `extra_sources` 的分工**：`youtube:` 是「展示用影像」，`extra_sources` 是「佐證／參考資料」——僅作佐證、不值得 embed 的 YT 連結（畫質差、只拍到告示牌等）仍放 `extra_sources`。同一支影片兩種身分兼具時放 `youtube:` 即可，不必重複列。
>
> **連結請盡量用含帳號的完整形式** `https://www.instagram.com/帳號/p/XXXXXXXXX/`（而非僅 `/p/XXXXXXXXX/`）。網站會從 URL 解析出發文帳號，在照片卡片上額外顯示「📷 @帳號」並連回該 IG profile（embed 兩種形式都吃，含帳號不影響顯示）。沒帶帳號的連結仍可正常 embed，只是不會多顯示這行攝影者署名。IG 的「複製連結」常給不含帳號的短形式，curate 時請改存完整形式。

---

## 野生／來源不明出身個體（2026-08-13 起）

早期由中國輸入的初代個體多無父母登録，出身該怎麼寫要看**國際血統登録書（ISB）的實際欄位**，不可一律寫成「野生捕獲」。

### ⚠️ 用詞三級（ISB 的 WILD ≠ 野捕）

ISB 的 `sire`／`dam` 只有兩種非數字值，含義完全不同：

| ISB 判定 | 2008 年版筆數 | 可以怎麼寫 |
|---|---|---|
| `sire/dam = WILD` **且**有 `Capture` 事件 | 130 | 「**中國野生捕獲**」（如 `taisyu-1987` 的 `CHINA ???? NONE Capture`） |
| `sire/dam = WILD` 但**無** `Capture` 事件 | 109 | 只能寫「**野生出身**／雙親無登録紀錄」（如 `tan-tan-1978`／`yui-yui-1980`，ISB 只記入日本平的 Transfer） |
| `sire/dam = UNK` | 53 | 只能寫「**出身不詳**」，**與野生無關**（如 `ton-ton-1994`＝ISB `94102`） |

`WILD` 的定義是「雙親不在登録簿」，**不等於在野外捕獲**——中國 1970–80 年代輸出的個體有園內繁殖但雙親未登録者。實證：`chou-chou-1986` RPF／ISB 均記 wild，家系圖證實實為 1986 年生於青島市動物園。故 ISB 記 WILD 時仍應先查園報／家系圖，查不到才用上表的保守措辭。

### 逐欄寫法

- **`origin:`**（上站用）：`wild`＝野生出身（含野生捕獲與野生救護）／`confiscated`＝走私查獲。個體頁的「出身」列由此欄驅動（`field_origin`／`origin_wild`／`origin_confiscated`，五語）。**只有兩個值是刻意的**——頁面上不區分「野捕／雙親無登録／救護」，那層分寸留在內文措辭；ISB 判為 `UNK`、或出身純屬不詳者**不填此欄**（頁面不出現該列，「不詳」由父母行表達）。⚠️ `hana-2023`／`hashi-2022`／`qiu-qiu-kaohsiung` 另有早期的 `rescue` tag，該 tag 未接進任何管線、純為 grep 標記，`origin:` 才是正本。
- **`born:`**：只採 ISB 的 `~ YYYY` 年份、**永不補月日**；slug 用該年（如 `taisyu-1987`）。引言固定寫「生年：約 YYYY 年（生年不詳・野生出身，依國際血統登録書推定）」。備注順帶記「番號前兩碼＝登録年非出生年」，避免日後由番號反推錯生年（8935 ≠ 1989 年生）。
- **`birth_zoo: unknown`**：**必填**。否則 `gen_residence.py` 會把居住史首站標成 🐣 出生地。
- **`zoos:`** 依佐證決定首站：
  - 來源園有一手佐證（園報／家系圖指名）→ 記為首站、**起始留空** `園名 ( – 出園日)`，如 `西安秦嶺野生動物園 ( – 1980-09-16)`、`石家莊市動物園 ( – 1985-03-19)`
  - 只知「中國」→ **不編造**，首站＝日本園、起始＝入園日（如 `到津の森公園 (1989-10-11 – …)`），來源國寫在內文
  - **絕不可**把「野生」「WILD」當園名塞進 `zoos:`（未登記於 `data/zoos.json` 會被 `build_db.py` 直接擋掉）
  - ⚠️ **ISB 對中國野捕個體不記來源園**：捕獲列只填到**國別** `CHINA`（欄位序為 `Location | Date | Local ID | Event`，故 `????`＝捕獲日不詳、`NONE`＝Local ID 欄無值，**不是**「無前置機構」之意），且捕獲列與入園列之間沒有任何中間機構。ISB 這個格式**本來記得下**中間持有者（歐美早期個體常見動物商 `ZEEHANDLR`／`V.D.BRINK` 獨立一列），但 90 筆 `CHINA` 捕獲個體全部直接跳到目的園 → 中國來源園在 ISB 是**真的缺**、非格式限制。「中國哪一園來的」只能靠園報／家系圖／園方年表
- **`## 家族` 固定句式**：`- 出身：中國野生捕獲（ISB 記推定生年 ~YYYY、捕獲日不詳、YYYY-MM-DD 入○○）` ＋ `- 父母：無登録紀錄（ISB sire／dam＝WILD）`。**勿寫「父：不詳」那種行**——會踩父母行的 wikilink 陷阱（該行任何 `[[link]]` 都會被當成父母）。
- **捕獲地可記**：ISB 的 locality code 比「野生」有資訊量（CHINA 90／NEPAL 6／GANGTOK 6＝錫金／DARJEELIN 4），寫進內文即可。

---

## 幽靈親代 `mother_ref` / `father_ref`（2026-08-14 起）

小熊貓早期族群裡有不少**身分明確、但終生未命名**的親代（多為 1980–90 年代自中國輸入的野生捕獲個體）。
依〈幼逝寶寶收錄原則〉與既有慣例，未命名者**不建條目**——但這會造成一個純技術性的副作用：

> 網站判全血／半血是比 `p.father === q.father`。父親兩邊都是 `undefined` 時比較為偽，
> **同父同母的全血緣手足（連雙胞胎都算）會被顯示成 ½ 兄弟姊妹。**
> 2026-08-14 全庫盤點：38 隻個體、58 組配對受影響（如ロンロン×ミンミン 雙胞胎、仙台 1993 三胞胎）。

`mother_ref` / `father_ref` 就是為此而設：**只記「是同一隻」，不建個體**。

- **值的格式**：`isb:<番號>` 優先（ISB 是官方一手、番號唯一且穩定，連 RPF 沒收的個體也有號），
  ISB 查不到而 RPF 有的才退回 `rpf:<id>`。**一律加引號**（`isb:0099` 這種有前導零的值）。
- **與 `mother:`／`father:` 互斥**：親代有條目就走 `## 家族` 的父/母行，別重複填 ref。
- **不進 `parent_child` 表、不建節點、不上家系圖、不進任何統計**——它唯一的作用是
  `web/src/lib/data.js` 判血緣度時的親代識別碼。個體頁不顯示此欄。
- **內文仍要寫清楚那隻是誰**：`## 家族` 的「父：」行照舊用純文字敘述
  （`- 父：無名個體（ISB \`92137\`，中國野生捕獲…）`）。⚠️ 該行**不可放任何 `[[wikilink]]`**——
  父/母行的任何連結都會被當成親代。
- **限制**：ref 不會讓手足「被發現」。手足清單仍靠有條目的那一位親代的 `children` 反查；
  若兩隻的**雙親都**只有 ref，彼此不會出現在對方的手足列，那種情形請改用 `siblings:` 欄位。

範例（ロンロン／ミンミン 雙胞胎，父為 ISB `92137`、終生未命名故無條目）：

```yaml
father_ref: "isb:92137"
```

---

## 家族連結慣例

- 使用 `[[wiki-link]]` 格式互相連結（Obsidian 相容）
- 已故成員在名稱後加 🪽 標記
- ½ 代表同父異母或同母異父的半血緣兄弟姊妹

---

## 資料來源

| 來源 | 說明 |
|------|------|
| 園方官網／公告／園報等官方一手來源 | **優先採用**；`sources` 以官方為主 |
| [RedPandaFinder](https://redpandafinder.com) | 家系、居住地、別名——2026-07-14 起降為「線索」、非權威 |
| [Red Panda Lineage Project](https://github.com/wwoast/redpanda-lineage) | 底層血統資料庫——同上，僅供參考，衝突以 wiki 為準 |

### sources 與 extra_sources 的分工（2026-08-02 起）

| 欄位 | 放什麼 | 網站顯示 |
|------|--------|----------|
| `sources` | **官方／一手來源**：園方官網、園報、飼育日誌、政府公告、園方官方社群帳號（分類器 `OFFICIAL_HOSTS` 見 `tools/build_db.py`） | 個體頁「來源」區塊；同時決定 `has_official_source` 旗標 |
| `extra_sources` | **其他參考資料**：同好部落格、YouTube 影片（佐證用）、新聞報導、fan wiki 等非官方鏈結。**只放 URL**。值得展示的 YT 影片改放 `youtube:` 欄位（見上） | 個體頁「其他參考資料」區塊（列在「來源」下方，並註明非官方）；非 URL 項目一律過濾不顯示 |
| （條目內文／`## 備注`） | **無法線上核對的一手佐證**：讀者實拍展牌、實體園報掃描等。連同原文引述寫成敘述（2026-08-05 起，取代舊的「在 `extra_sources` 寫純文字說明」做法） | 隨內文顯示 |

- **官方但不對外呈現的來源（2026-08-11 維護者裁定）**：ISB《International Red Panda Studbook》（Rotterdam Zoo／Diergaarde Blijdorp 編）**是官方一手來源、佐證權重照舊**（`has_official_source` 照算、🚧 解除照舊），但**個體頁不列出連結**——原檔 2012 年已由園方下架，公開可指的只剩 Wayback 快照，不宜對外呈現。連結原封不動留在 frontmatter `sources:` 供校訂稽核，原檔存 `sources/isb-red-panda/`。實作：`tools/build_db.py` 的 `NON_PUBLIC_HOSTS`（比對 Wayback 內層 host）→ 拆進 DB 的 `sources_private` 欄，`export_json.py` **刻意不匯出**該欄（`pandas.json` 隨網站發佈，連結進了 JSON 就等於上站），只把它併入 `has_official_source`。⚠️ 這是「官方但不公開」，與「非官方」是兩回事，**勿把 `rotterdamzoo.nl` 從 `OFFICIAL_HOSTS` 移除**。
- **部落格／影片等非官方連結一律進 `extra_sources`、不進 `sources`**，避免污染官方來源判定。
- **`extra_sources` 只列 URL**（2026-08-05 起）：純文字佐證說明不列在此，改寫進條目內文／`## 備注`。網站個體頁的「其他參考資料」區塊只呈現連結。
- 由這類來源帶入、無官方佐證的關鍵資料（生卒日、家系）仍照 `CLAUDE.md` 標 `🚧 待查證`；把連結留在 `extra_sources` 是為了讓讀者能自行追溯，不等於採信。
- 連結行末可加 YAML 註解（`# 標題（日期）`）記錄出處與看點，註解不會進 DB、僅供維護者參考。

---

## 操作流程

### 新增成員
1. 在 `wiki/` 下建立 `[name]-[born].md`（slug = 名字-生日）
2. 填入 YAML frontmatter
3. 撰寫條目內容（基本資料 → 別名 → 居住史 → 家族 → 備注）
4. 更新 `wiki/index.md`
5. 在 `wiki/log.md` 新增一筆記錄

### 更新現有條目
1. 直接編輯對應的 `[name].md`
2. 在 `wiki/log.md` 新增 update 記錄

### 查詢
- 先讀 `wiki/index.md` 找到相關條目
- 再讀取個別頁面取得詳細資料

---

## 標籤體系

| 標籤 | 說明 |
|------|------|
| `styani` | 中華小熊貓亞種 |
| `fulgens` | 喜馬拉雅小熊貓亞種 |
| `female` / `male` | 性別 |
| `deceased` | 已過世 |
| `apple-seed` | 當季未命名寶寶的佔位條目（正式命名轉正時移除） |
| `limited-profile` | 檔案卡：資料有限個體（缺生日／家系不明等），詳見 `CLAUDE.md` |
| `unverified` | 存疑／動向不明：網站據此排除統計與現存篩選、顯示待查證標記 |
| `zoo:多摩動物公園` | 所在動物園 |
| `taofa-family` | Taofa 直系家族成員 |

---

*本 wiki 收錄小熊貓個體檔案，涵蓋相關家族成員與動物園個體。*
