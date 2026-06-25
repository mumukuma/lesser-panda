---
name: report-intake
description: >
  處理社群「資料回報」收件匣（Tally → Google Sheets），把回報分流成可核可的清單，
  再交給 rpf-wiki / CLAUDE.md「新增成員流程」寫回 wiki。
  當使用者說「處理回報」、「Tally 收到回覆」、「看一下收件匣」、「有人回報資料更正」、
  「圖鑑缺漏回報」、「處理 Google Sheet 的回報」時，一定要使用此 skill。
  此 skill 只做「收件 → 查證 → 分流」，不直接改 wiki；採用的項目才交棒給寫入流程。
---

# 社群回報收件匣 → 分流 Skill

讀者透過 Tally 三語表單回報「資料更正」與「圖鑑缺漏」，回應自動進到作者
（washimumukuma@gmail.com）的 Google Sheet 收件匣。本 skill 負責把這些**非權威**的回報
拉出來、查證、整理成逐筆核可清單。**`wiki/*.md` 永遠是唯一正本；任何回報都不會自動寫進
wiki，一律經作者核可後才動。**

---

## 最高原則（呼應 CLAUDE.md 與 DATA-CORRECTION-PLAN.md，不可違反）

1. **收件匣 = 提案，不是事實。** wiki 與回報衝突時，一律以 wiki（作者校訂）為準，除非回報
   附的來源明確更可靠。
2. **來源必查。** 回報者填的「正確值」要對照其附的來源**逐筆查證**，不可照單全收。回報者常
   填錯（例：把移動年填成 2021，來源其實是 2017）——以來源為準，並在清單註記出入。
3. **永不自動寫入。** 本 skill 產出的是「建議動作清單」，交作者核可。採用者才走寫入流程。
4. **每次採用都寫 `wiki/log.md`**（記為 `fix`），並遵守 log「禁止 `[[wikilink]]`、名字用 backtick」。

---

## 第一步：先讀 wiki 規範

動工前先讀（同 CLAUDE.md「任何工作開始前」）：

1. `CLAUDE.md` —「社群回報表單」章節（兩個主題、兩張 Sheet、處理流程）
2. `SCHEMA.md` — frontmatter 與 slug 規範
3. `wiki/index.md`、`wiki/log.md` 末幾筆

---

## 第二步：拿到收件匣資料（Google Drive 連接器）

收件匣 Sheet 在 **washimumukuma@gmail.com** 名下，用 **Google Drive 連接器**讀取
（授權時要選這個帳號，不是登入帳號）。

| 主題 | Sheet 標題（current） | 對應 Tally |
| --- | --- | --- |
| 資料更正 | `回報資料更正` | https://tally.so/r/ODr777 |
| 圖鑑缺漏 | `回報缺少的小熊貓或動物園…` | https://tally.so/r/2EVJlb |

⚠️ **只讀現用的三語表。** Drive 裡還躺著已退役的純英／純日舊表（如 `Report a correction`、
`データ修正のご報告`），現在是空的，**一律忽略**（CLAUDE.md 記載 2026-06-22 已合併為單張三語表）。

用 `search_files`（`mimeType = 'application/vnd.google-apps.spreadsheet'`）找到後，
用 `read_file_content` 讀整張表。

---

## 第三步：清洗與正規化

1. **過濾測試投稿**：暱稱／補充欄出現「テスト送信」「測試」「test」等字樣者，先標為「疑似測試」，
   除非作者指示當真回報處理。
2. **欄位映射**：Sheet 欄標題是三語超長字串，映射成穩定欄名：
   - 關於哪一隻（名字／網址）、個體連結、想回報什麼問題（類型）、正確應該是什麼、
     來源／證據、暱稱（致謝）。
   - 「資料更正」表另有結構化欄：轉到哪一園、生效日期、過世日期、寶寶生日。
3. **正規化「類型」下拉的混語值**：表單選項三語並列，視為同一類。常見對應：
   - 名字／名前／Name｜生日／誕生日／Birthday｜居住史／移動｜家族關係｜性別｜卒日／死亡｜其他/その他/Other
   - 自由填答欄語言由填答者決定（中／日／英混雜屬正常），照原文保留。

---

## 第四步：逐筆查證（核心）

對每一筆：

1. 用名字／連結在 `wiki/` 找到對應條目（slug = 名字-生日；同名看媽媽名消歧）。沒有條目者
   → 屬「新增」，走第五步交棒。
2. 比對「回報值」vs「wiki 現值」vs「回報附的來源」。
   - 開來源連結查證（RPF、redpandapedia、動物園官網、新聞、IG）。來源頁是 JS 動態網站、
     WebFetch 只拿到外殼時，改用 Claude in Chrome `get_page_text`。
   - **回報者的數值要對著來源再確認**，不一致時以來源為準並記下出入。
3. 判定 **建議動作**，四選一：
   - `採用` — 來源可信且與 wiki 不衝突（或來源明顯更可靠）。
   - `需補件` — 無來源或來源不足，（若留暱稱）請補。
   - `退回` — 與 wiki 衝突且來源不夠可靠。
   - `保留待確認` — 牽涉重大改動（家族關係、跨國移動、需新增動物園註冊）或語意不明，交作者定奪。
4. **居住史 / 出生園**特別注意：出生園 🐣 改動要連動 frontmatter `zoos:` 第一段；
   家族關係改動成本最高（要同時改雙方頁面 + wikilink + 重建 DB），預設標 `保留待確認`。

### 產出：分流清單

整理成一張表給作者核可，欄位：個體（slug）｜類型｜回報內容｜wiki 現值｜來源查證結果｜
建議動作｜備註。先**不動任何檔案**，等作者點頭。

---

## 第五步：採用者交棒寫入（不在本 skill 內重做）

作者核可後，採用的項目依既有流程處理，本 skill 不重寫規則：

- **新增個體** → 交給 `rpf-wiki` skill（含自動補直系親屬、回頭把純文字親屬改 wikilink）。
- **既有條目修正** → 依 CLAUDE.md「新增成員流程／條目格式」直接 Edit：
  - 改**居住史**一律改 frontmatter `zoos:`（格式 `園名 (起 – 訖)`，精確日期）。
    ⚠️ 注意 `gen_residence.py` 解析時**優先讀內文 `## 居住史` 表格**，且 frontmatter 的
    fallback 只認年份、不認 ISO 日期；故精確日期修正要同步改**表格列**（date 用 `YYYY-MM-DD – YYYY-MM-DD`），
    🐣 標出生園、🏡 標現居。園名須是 `data/zoos.json` 的 canonical；沒登記的園先加註冊表。
  - 寫了註冊表沒有的園名，`build_db` 會報錯中止。
- 重建（在 wiki 根目錄）：
  ```
  python3 tools/build_db.py          # 讀 frontmatter；沙盒會 fallback 到 /tmp/redpanda.db
  python tools/audit.py              # sanity check（0 問題）
  python3 pipeline/scripts/export_json.py
  ```
  > 是否要跑 `gen_residence.py`：它會**順手把全 wiki 的地點字串正規化**（重寫數百檔）。
  > 若只想改動目標條目、不想擴大 diff，就手改該條目的表格＋frontmatter，**跳過** gen_residence；
  > 想做全站正規化再單獨跑、單獨 commit。
- 在 `wiki/log.md` append 一筆 `fix`（backtick 名字、無 wikilink、附來源連結）。

---

## 第六步（選填）：回覆回報者

回報者留了暱稱／聯絡時，告知「已採用／未採用＋原因」，並可列入致謝（`data/contributors.json`）。

---

## 邊界

- 本 skill **不**直接改 wiki、**不**自動寫入、**不**改 Tally 表單（要改表單用 Claude in Chrome，
  改完按 Publish 才生效）。
- 本 skill 做的是「把收件匣變成一張可核可的分流清單」。寫入永遠經作者最終核可。
