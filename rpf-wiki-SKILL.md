---
name: rpf-wiki
description: >
  為小熊貓 Obsidian wiki 新增或更新條目，資料來源為 Red Panda Finder（redpandafinder.com）。
  當使用者提供 Red Panda Finder 的 URL 或 profile ID，並要求「產生 wiki」、「加到 wiki」、
  「建立條目」、「按照現有 wiki 格式」時，一定要使用此 skill。
  即使使用者只說「幫我做 wiki」或「加這隻」也應該觸發。
  此 skill 確保所有檔案格式、YAML frontmatter、wikilink、index 與 log 更新都正確無誤。
---

# RPF → Wiki Skill

幫使用者從 [Red Panda Finder](https://redpandafinder.com)（RPF）抓取小熊貓資料，
並按照 Obsidian wiki 的 SCHEMA.md 規範，產生正確格式的 wiki 條目。

> ⚠️ **RPF 已降為「線索」（2026-07-14 起，詳見 `CLAUDE.md` 資料來源原則）**：新條目 `sources`
> 以園方公告等官方一手來源優先、RPF 為輔；由 RPF/lineage 帶入而無官方佐證的關鍵資料標 `🚧 待查證`；
> 與既有 wiki 校訂衝突時一律以 wiki 為準，不可用 RPF 覆蓋。

---

## 第一步：讀取現有 wiki 結構

在做任何事之前，先讀：

1. `SCHEMA.md`（在 wiki 根目錄）— 了解 frontmatter 欄位、檔案命名、wikilink 慣例
2. `wiki/index.md` — 確認哪些條目已存在，避免重複
3. `wiki/log.md` — 了解日誌格式（只需看最後幾筆記錄即可）

如果找不到 SCHEMA.md，請告知使用者，wiki 根目錄可能不對。

---

## 第二步：從 RPF 抓取資料

使用 **Claude in Chrome** 瀏覽以下頁面，每頁都用 `get_page_text` 擷取內容：

1. **Profile 頁**：`https://redpandafinder.com/#profile/<ID>`
   - 取得：英文名、日文名（Other Names）、生日、物種、居住地點列表、家族關係
   
2. **用 JavaScript 取得親屬 profile ID**（在 profile 頁執行）：
   ```javascript
   Array.from(document.querySelectorAll('a[href]'))
     .map(a => ({href: a.href, text: a.textContent.trim()}))
     .filter(x => x.href.includes('profile'))
   ```

> 💡 另有全站資料集可抓：`https://redpandafinder.com/export/redpanda.json`（扁平 key 如 `v['en.name']`、
> 動物園 `_id` 為負數）。舊的 `window.Pandas` 全域變數已不存在，勿再依賴。

### 性別：讀名字前的性別 icon（勿從子女反推）

RPF **有**標示性別——是名字前的 icon 圖片，`get_page_text` 會把它濾掉、看起來像沒標，其實有。用 DOM 讀取：

- **本尊**：`document.querySelector('.gender.profile img').alt`（`male`／`female`）。
- **親屬卡**：各卡的 `.gender img` 的 **`alt` 不可靠**（曾出現整頁親屬都是 `alt="male"`），改讀 img **`src` 檔名**（`male.svg`／`female.svg`）。一次抓全家：
  ```javascript
  Array.from(document.querySelectorAll('a[href*="profile"]')).map(a=>{const i=a.querySelector('img[src*=".svg"]');return {h:a.getAttribute('href'),t:a.textContent.trim().replace(/\s+/g,' '),s:i?i.src.split('/').pop():null}})
  ```
- **嚴禁從 Mother/Father/daughters/sons 等關係反推本人性別**（不可靠、作者已明令禁止）。
- 若仍不確定，留空並備注「待確認」。

---

## 第三步：決定要建立哪些條目（範圍有上限）

### ⛔ 展開深度上限＝一圈（2026-08-25 起）

**只從主角展開一圈，新建出來的親屬不再各自展開第二圈。** 這是硬上限，不是建議值。

| 關係（相對於**主角**） | 建？ | 說明 |
|---|---|---|
| 父、母 | ✅ | |
| 同胎手足 | ✅ | |
| 非同胎兄弟姊妹 | ✅ | |
| 子女 | ✅ | |
| 配偶 | ✅ | 子女的另一位親本；不建的話網站會把全血緣手足判成 ½（見 `SCHEMA.md`〈幽靈親代〉） |
| 祖父母 | ❌ **不再自動建** | 這一格是舊規則爆炸的來源。寫成純文字＋RPF ID 即可 |
| 上述新建條目的父母／子女／手足 | ❌ | 一律純文字，**不遞迴** |

> **為什麼改**：舊規則「父母／手足／子女／祖父母一律自動建立」沒有終止條件——
> 主角 → 子女 → 子女的另一位親本 → 那位親本的父母 → ⋯⋯ 一路展開不會停。
> 同一份回報在不同時間做，範圍會不一樣。改為深度上限 1 之後，
> 「這次要建幾隻」在讀完主角的 profile 當下就是確定的。

### 每一隻的建檔門檻（兩項皆需，缺一不建）

1. **`born` 有可寫成 slug 的粒度**——完整 `YYYY-MM-DD` 或至少年份 `YYYY`。
   完全查不到生日就不建（中國個體的檔案卡制度另有 `slugify(name)-園簡稱` fallback，見 `CLAUDE.md`）。
2. **有名字**——佔位名（`Baby`／`赤ちゃん`／`(無名)`）不建個體條目；
   當季未命名寶寶走蘋果籽制度，其餘依〈幼逝寶寶收錄原則〉處理。

門檻沒過的親屬 → `## 家族` 寫純文字（`- 父：Moshu（#413，2011-06-20 生，無條目）`），
並在回報裡列出來，**不要因為「規則說要自動建」就硬湊資料建檔**。

### 範圍外的發現一律回報、不擅自擴張

查證過程常會撈到範圍外但值得建的個體（祖父母、新出生的一胎、同園的其他隻）。
**列進最後的回報問維護者，不要順手建。** 建了就等於這次的範圍又變成不確定的。

建立順序：主角 → 父 → 母 → 同胎手足 → 子女 → 配偶。
若某親屬**已有 wiki 條目**，跳過建立、改為在雙方條目補上 `[[wikilink]]`。

---

## 第四步：建立個別 wiki 條目

對每一隻需要建立頁面的小熊貓，在 `wiki/` 資料夾建立 `[slug].md`。

### ⚠️ 動筆前先定生日——slug 上唯一高成本的欄位（2026-08-25 起）

`born` 是 slug 的一部分。**寫錯 `born` 要走 `tools/rename.py` 做全站 slug 遷移**
（改檔名＋全 wiki `[[wikilink]]`＋`siblings:`＋index＋log，還要人工補標題／引言／內文的舊名字），
而其他任何欄位寫錯都只是原地改一行。所以 `born` 與別的欄位不同級，**建檔前先把它釘死**：

1. **先問「這個生日最強的來源是誰」**，再開檔。優先序：
   1. **出生園在事發當時發布的一手來源**（出生／命名新聞稿、園報、官方社群公告）
   2. 收容園／現居園**日後撰寫**的動物介紹頁
   3. RPF／lineage（線索）
2. **回報者或現居園給的生日，先找出生園的公告核對一次再落檔。** 找不到就照用，
   並在 `## 備注` 註明「僅 X 為據」。
   - **找的順序**（前一層沒有才往下一層）：
     1. 出生園的**現行官網／官方社群**
     2. 該園的**既有來源管道**——園報（王子《はばたき》、天王寺《なきごえ》、日本平《でっきぶらし》…）、
        staff blog、年度存檔。逐園的路徑多半已記在 `CLAUDE.md`／`OFFICIAL_HOSTS` 註解與 memory
     3. **Wayback**——頁面 404／CMS 改版整批下架／園已閉園時的**正規手段，不是最後手段**。
        既有先例：茶臼山 `/zukan/zukan/YYYY` 年度存檔、池田訃報、のいち舊個體頁、平川舊 blog、静岡市舊 PDF。
        ⚠️ Wayback 快照**仍算官方一手、佐證權重照舊**（只是連結僅 dev 顯示，見 `SCHEMA.md`）
   - **⛔ 可以直接跳過不搜的，只有兩種**：
     1. **出生園不詳**——連要搜哪一座園都不知道，沒有搜索目標
     2. **該園在該個體出生的年代確實沒有任何對外紀錄管道，且專案先前已確認過**
        （memory／`docs/` 有記，如釧路《あゆみ》未數位化、安佐飼育記録集掃描無文字層）。
        **第一次遇到某座園不算**——先照上面搜一輪，得出結論後把它記進 memory，下次才能據以跳過
   - **⛔ 年代不是判準**：**別用「19XX 年前就不用查」這種年代線一刀切。**
     全庫有 200 筆條目以 Wayback 為來源，其中 169 筆生年在 2000 年之前——年代早**正是**要翻 Wayback 的理由。
     反過來，2020 年代的中國個體也可能完全沒有公告。年份跟「有沒有一手紀錄」沒有必然關係。
   - **成本上限**（接回 `CLAUDE.md`〈查證省時原則〉）：上面三層**各搜一輪**，沒有就停，
     照現有最強來源落檔並在 `## 備注` 寫「僅 X 為據」。**不做第二輪。**
3. **兩個官方來源打架時，先分辨誰在場、誰在事後轉述**——不要因為「兩邊都是官方」
   就直接套用 `CLAUDE.md`「官方之間衝突留待維護者裁定」。那條是給**同級**來源用的；
   一手 vs 事後轉述並非同級，可以自行判斷並把差異寫進備注。
   - 實例（2026-08-25）：Pavitra 的生日，ZooMontana 官網動物頁記 `June 1, 2023`，
     出生園 San Diego Zoo Wildlife Alliance 的命名新聞稿記 `born June 9`。採 6/9。
4. 只有 `born` 需要這道。`died`、居住史日期、家系連結等寫錯都可原地更正，不必為它們卡住流程。

### 檔案命名規則（2026-06-18 起，slug＝名字-生日）

**slug 一律為「名字-生日」**（詳見 `CLAUDE.md`「檔名與消歧」）：

1. 格式：`slugify(name)` + `-` + 生日。生日用完整 `YYYY-MM-DD`；只知年份則用 `YYYY`。
   - 例：`yan-yan-2014-06-22.md`、`akebi-2020-06-29.md`、`tian-1999.md`
2. slugify：全小寫、空白/底線換連字號、去除 `'`、`()`、`.`；重音字母以 NFKD 轉為基本拉丁字母（é→e、ñ→n…，不可整個刪掉）。
3. **撞名（同名又同生日）才加第三層消歧＝媽媽的名字**（slug），**不用父名**：
   - 例：`sora-seina-2008-06-16`、`sora-nami-2008-06-16`
4. 佔位名字一律用「名字-媽媽名-生日」；當季未命名寶寶用「蘋果籽」制度（`apple-seed-媽媽slug-生日`，見 `CLAUDE.md`）。
5. 同名並存時，條目內加 `⚠️ 注意同名` 提示。
6. 完全無生日的檔案卡個體（多為中國個體）fallback：`slugify(name)-園簡稱`（如 `xiao-bai-shanghai`），查到生日再照 rename 流程改回標準 slug。

建檔前先搜尋 `wiki/index.md` 確認同名條目是否已存在，避免重複。

### YAML frontmatter 格式

```yaml
---
name: 英文名
chinese: 中文名                     # 台灣／中國個體的正式中文名；若無則省略
japanese: 日文名（漢字 / 假名）      # ⚠️ 僅「有日本居住史」的個體才填（RPF 的 ja.name 是機械轉寫，歐美個體勿抄）
nicknames: [暱稱1, 暱稱2]          # 若無則省略
english_variants: [變體1, 變體2]   # 若無則省略
sex: female | male
born: YYYY-MM-DD
died: YYYY-MM-DD                   # 若健在則省略
species: Ailurus fulgens styani | Ailurus fulgens fulgens   # 亞種不詳→整行省略（勿寫 Ailurus fulgens）
zoos:
  - 動物園名稱 (起 – 訖)            # 園名須為 data/zoos.json 註冊表 canonical（未登記 build 報錯）；起訖可 YYYY-MM-DD／YYYY，現居訖留空或寫「現在」

> **遇到沒登記過的園要先加進 `data/zoos.json`**，此時地點三欄一欄一語、**不可混填**（詳見 CLAUDE.md）：
> `location_ja`＝當地語言（日本園日文新字体「神奈川県横浜市」、中港台韓園日文可讀漢字「上海市長寧区」；
> **非漢字圈的園留空 `null`**，ja 語系自動退回英文），`location_zh`＝繁體中文正本（「紐約州水牛城」），
> `location_en`＝英文。RPF／lineage 帶出的地點多半是繁中或英文，**落地前先分流**，別整串丟進 `location_ja`；
> 也順手看語序有沒有顛倒（lineage 會給「佐世保市長崎県」這種值）。
rpf_id: 數字
rpf_url: https://redpandafinder.com/#profile/數字
tags: [styani或fulgens, female或male, zoo:動物園名]
sources:                           # 官方一手來源優先，RPF 為輔
  - https://redpandafinder.com/#profile/數字
---
```

完整欄位規範（`instagram:`、`youtube:`、`extra_sources`、`last_seen`、`birth_zoo`、`siblings` 等選填欄）見 `SCHEMA.md`。

### 條目內容結構

```markdown
# 名字（日文名）

> **小熊貓** ♀/♂ | Ailurus fulgens styani  
> 生日：YYYY 年 M 月 D 日（X 歲）  
> 現居：動物園名（地點）

一句話介紹（父母、雙胞胎等關鍵背景）。
如有 wiki 條目的親屬，用 [[wikilink]] 連結。

---

## 居住史

（此表格**由 `tools/gen_residence.py` 依 frontmatter `zoos:` 自動生成，勿手改**——
含地點、🐣出生地、🏡現居標記。建檔時可先留空段落，跑 `bash rebuild.sh` 即自動填入。）

---

## 家族

- 母：[[母親wikilink]] 或純文字（若無條目）
- 父：[[父親wikilink]] 或純文字
- 雙胞胎：名字（[[wikilink]]）
- 兄弟姊妹：列表

### 子女

| 姓名 | 出生年 | 另一方親本 |
|------|--------|-----------|
| [[子女wikilink]] | 2020 | [[另一方]] |
```

### Wikilink 規則
- 若對方**已有 wiki 條目**：用 `[[檔名]]` 格式（不含副檔名）
- 若對方**尚無 wiki 條目**：純文字即可，不用強行建立
- 已故成員在名稱後加 🪽

---

## 第五步：更新 index.md

在 `wiki/index.md` 的適當分類下新增條目。
- 更新頁首的「最後更新」日期與「條目總數」
- 找到最適合的既有類別，或新增類別
- 格式與現有條目保持一致（表格欄位、wikilink 格式）

---

## 第六步：更新 log.md

在 `wiki/log.md` **最末端** append 一筆新記錄：

```markdown
## [YYYY-MM-DD] add | 說明

**來源**：
- https://redpandafinder.com/#profile/XXX (名字)

**新增條目**：
- `slug.md` — 簡短說明（RPF #XXX），生於 YYYY-MM-DD，現居 動物園

**更新條目**：
- `index.md` — 新增 XXX 條目，條目總數更新為 N
```

### ⚠️ log.md 格式限制（Obsidian graph view）

**log.md 裡面絕對禁止使用 `[[wikilink]]`。**

原因：Obsidian 只要看到 `[[wikilink]]` 就會在 graph view 中建立連線，無論該檔案的用途是什麼。如果 log.md 出現了 `[[yuuta]]`，就會在 graph 中顯示 `log ─── yuuta` 這條連線，讓 log 成為一個中心節點。這是錯誤的行為——log 是 changelog，不是關係圖的實體。

**正確格式**：用 backtick 包住名字即可，例如：

| ❌ 禁止 | ✅ 正確 |
|---------|---------|
| `[[yuuta]]` | `` `yuuta` `` |
| `[[fuuka]]🪽 的雙胞胎` | `` `fuuka`🪽 的雙胞胎 `` |

**`#{id}` 的數字 tag 安全**：Obsidian tag 必須以字母開頭，`#72`、`#199`、`RPF #23` 等純數字或文字後接數字的寫法**不是**合法 Obsidian tag，不會在 graph 中產生節點，可以安心使用。

---

## 注意事項

- **先讀後寫**：永遠先用 Read 工具確認現有檔案，再用 Write/Edit
- **不要覆蓋**：若條目已存在，改用 Edit 更新，並在 log 記錄為 `update`
- **清理錯誤檔案**：若之前在錯誤位置建立了格式錯誤的檔案（如 wiki 根目錄下的 .md），詢問使用者是否要刪除
- **親屬展開只做一圈**：父、母、同胎手足、兄弟姊妹、子女、配偶（見第三步）；**祖父母與更外圈不自動建**，寫純文字並在回報裡列出
- **先定生日再開檔**：`born` 決定 slug，寫錯要全站遷移；務必先核出生園的一手來源（見第四步）
- **日文名**：若 RPF 顯示 Other Names，記得填入 frontmatter 的 `japanese` 欄位（**僅日本個體**——歐美等非日本個體的 ja.name 若含漢字，多半實為中文名，經作者確認後放 `chinese`）
- **建檔後重建**：`bash rebuild.sh`（gen_residence → build_db → export_json → check_twins）
