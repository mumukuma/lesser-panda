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

## 第三步：決定要建立哪些條目

### 自動建立範圍

拿到主角資料後，**自動為以下直系親屬建立 wiki 頁面**（若該條目尚不存在）：

| 關係 | 自動建立？ | 說明 |
|------|-----------|------|
| 父、母 | ✅ 是 | 先抓各自的 RPF profile |
| 雙胞胎 | ✅ 是 | 同批出生、關係最密切 |
| 子女 | ✅ 是 | 每一隻都建立個別頁面 |
| 兄弟姊妹（非雙胞胎） | ✅ 是 | 先抓各自的 RPF profile |
| 祖父母 | ✅ 是 | 先抓各自的 RPF profile |

若某親屬**已有 wiki 條目**，跳過建立、改為在相關條目中補上 `[[wikilink]]`。

建立順序建議：主角 → 父 → 母 → 雙胞胎 → 子女（由近到遠）。

---

## 第四步：建立個別 wiki 條目

對每一隻需要建立頁面的小熊貓，在 `wiki/` 資料夾建立 `[slug].md`。

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
- 已故成員在名稱後加 🪐

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
| `[[fuuka]]🪐 的雙胞胎` | `` `fuuka`🪐 的雙胞胎 `` |

**`#{id}` 的數字 tag 安全**：Obsidian tag 必須以字母開頭，`#72`、`#199`、`RPF #23` 等純數字或文字後接數字的寫法**不是**合法 Obsidian tag，不會在 graph 中產生節點，可以安心使用。

---

## 注意事項

- **先讀後寫**：永遠先用 Read 工具確認現有檔案，再用 Write/Edit
- **不要覆蓋**：若條目已存在，改用 Edit 更新，並在 log 記錄為 `update`
- **清理錯誤檔案**：若之前在錯誤位置建立了格式錯誤的檔案（如 wiki 根目錄下的 .md），詢問使用者是否要刪除
- **自動補齊所有親屬**：父、母、雙胞胎、子女、兄弟姊妹、祖父母一律自動建立（若尚無條目）
- **日文名**：若 RPF 顯示 Other Names，記得填入 frontmatter 的 `japanese` 欄位（**僅日本個體**——歐美等非日本個體的 ja.name 若含漢字，多半實為中文名，經作者確認後放 `chinese`）
- **建檔後重建**：`bash rebuild.sh`（gen_residence → build_db → export_json → check_twins）
