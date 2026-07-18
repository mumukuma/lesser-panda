# 網站更新紀錄 Changelog

> 記錄**網站功能**的演進（新功能、改版、修正）。
> 小熊貓**資料**的異動請見 `wiki/log.md`；願望與規劃見 `ROADMAP.md`。
> 新的在最上面。

---

## 2026-07-18 ・ 網站：蘋果籽個體頁改「{媽媽}的蘋果籽」＋icon 改用 🍎 emoji

- 背景：作者偏好首頁新生 chip 的「杏花的蘋果籽」表示法，蘋果籽內頁標題比照辦理；原創 apple seed icon 取消、全站改用內建 emoji 🍎
- `web/src/lib/data.js`：首頁 `newbornLabel` 邏輯抽成 `placeholderMotherName()`（非佔位＝`displayName`、無母資料退回原佔位名、多胞胎保留號碼，i18n `placeholder_of_mother(_n)` 五語既有）；`Home.astro` chip、`Panda.astro` 標題（`primary`）、`[...path].astro` 頁面 `<title>` 三處共用
- icon → 🍎（tooltip 仍帶 `placeholder_badge`）：`Panda.astro` 徽章＋親屬 `link()`、`Zoo.astro` `link()`、`search.js` 搜尋卡、`jptree.js` 節點右上角（SVG `<image>` 改 `<text>`，沿用既有 text 的 LOD 顯隱）＋資訊卡；`JpTree.astro` 移除 `image` 專用 LOD 選擇器
- 刪除 `web/public/img/apple-seed.svg`；資料管線與 `placeholder` 欄不動
- 驗證：node 直跑 `placeholderMotherName` 抽查 10 筆佔位個體五語輸出＋非佔位 passthrough；`/tmp` 全量 build 通過（4042 頁），五語內頁標題／`<title>`／🍎 皆確認進產出、dist 無 apple-seed.svg 殘留

## 2026-07-18 ・ 網站：四季主題（色調＋季節粒子＋冬季全站飄雪）

- 背景：原配色固定為秋天暖色系，希望隨季節有四季氛圍、冬季飄雪
- 季節決定：新增 `web/public/js/season.js`（與 theme.js 同款、`<head>` 同步執行防閃爍）——預設依日期自動（3–5 春、6–8 夏、9–11 秋、12–2 冬），header 新增季節按鈕（🌸🌻🍂❄️）手動循環切換（auto → 春夏秋冬 → auto）並記 localStorage（`rpw-season`）；自動模式圖示稍淡作區別
- 色調（`global.css`，以 `:root[data-season=…]` 覆寫變數）：秋＝品牌預設不動；春／夏／冬各調 `--sky-*`／`--leaf*`（淺、深色模式各一套，冬夜偏藍、春夜偏粉紫），品牌鏽橘與森林背景圖不動；冬季另對 `forest-floor` 降飽和提亮做霜化、hero 天空加季節淡染
- 季節粒子：hero 既有 `.leaf` 依季節變身——春＝粉色花瓣（inline SVG 兩色）、夏＝螢火蟲微光（下往上飄＋忽明忽滅）、秋＝原落葉、冬＝收起改用全站飄雪層（`.snowfall`，season.js 動態生成隨機雪花、z-index 低於 header、pointer-events none）；reduced-motion 一律不生成＋CSS 保險絲
- i18n：五語各補 6 個 `season_*` 字串（`season_toggle`／`season_auto`／四季名）
- 驗證：`/tmp` 全量 build 通過（4042 頁），CSS/JS/五語字串皆確認進產出

## 2026-07-18 ・ 網站：日本園假名讀音可搜尋（ja_kana）

- 背景：動物園搜尋只索引漢字園名（canonical）／英文／中文，日文使用者打「のげやま」找不到「横浜市立野毛山動物園」，必須打漢字
- `data/zoos.json`：68 座日本園新增 `ja_kana` 欄（平假名讀音，Claude 草擬、待作者核對）
- `pipeline/scripts/export_json.py`：`load_zoo_master` 傳遞 `ja_kana` 進 `pipeline/data/zoos.json`
- `web/src/components/Zoos.astro`：`data-search` 納入 `z.ja_kana`（動物園頁文字過濾＋地圖連動皆生效）
- 另產 `docs/english-variants-audit.md`：454 個 RPF 帶入的 `english_variants` 依搜尋影響分四類，待作者圈選後批次清理

## 2026-07-17 ・ 制度：資料有限個體「檔案卡」（limited-profile）＋ `last_seen` 欄位

- 背景：中國園常無公告即轉移個體、不公布生日／家系／死亡，「資料齊才建檔」等於永遠不建；多年後條目又因無死訊而變雜訊。改採「證據快照」模式：記錄確認過什麼、何時確認
- 制度（SCHEMA.md＋CLAUDE.md 新章節「資料有限個體：檔案卡」）：
  - 建檔門檻＝官方來源確認存在＋至少對得上一座已登記園；不夠格的先記候補名單 `data/cn-candidates.json`（新檔，僅線索池、不進 DB 不上站）
  - 新 frontmatter 欄位 `last_seen`（檔案卡必填）：最後確認在世／在園日期，動向不明不猜 `died`；動向不明（約 2 年以上無法佐證現存）再加既有 `unverified` tag，沿用網站的排除統計＋待查證標記
  - 新 tag `limited-profile`（檔案卡追蹤／盤點用）；`zoos:` 起始一律填「首次確認年份」不留空（避免 gen_residence 誤標 🐣 出生地）
  - slug fallback：完全無生日 → `slugify(name)-園簡稱`（城市名，前例 `xiao-bai-shanghai`）；查到生日再照 rename 流程改回標準 slug
- 工具：`schema.sql`／`build_db.py`／`export_json.py` 貫通 `last_seen` 欄（pandas.json 帶出，網站顯示為後續工作）；`audit.py` 對 limited-profile 條目把「缺生日／缺 rpf_id」降為 info，新增「檔案卡缺 last_seen」warn。擋關（--strict）項目不變

## 2026-07-15 ・ 網站：家系圖支援近親迴圈（節點去重）

- 背景：中山市紫馬嶺動物園出現父女配對（窩窩頭同時是米糕之父、與米糕育有貝果），使 pedigree 出現迴圈；`tree.js` 原本假設家系為樹，會把同一隻畫成兩個框（貝果頁的窩窩頭、窩窩頭頁的貝果各重複一次、連線交叉）
- `web/public/js/tree.js`：`addNode` 改為以 slug 去重（每隻只畫一次）；祖先改逐層（BFS）放置，確保直系父母落在父母列；祖先／後代遇已放置節點時，改補一條 `loop` 連線指向既有節點，不再重複畫框或重展開
- `web/src/styles/global.css`：新增 `.tree-link.loop` 樣式（洋紅虛線）標示近親迴圈連線，與雙胞胎（琥珀）、半血緣（褐）區分
- 手足推導防呆：`data.js`（明細頁全血／半血手足）與 `tree.js`（家系圖手足節點）新增規則——**自己的直系子女／父母永不列為手足**。父女配對下子女會與親代共用一位親本而被誤判（如貝果被列為母親米糕的半血手足、米糕被列為女兒貝果的半血手足），已排除
- 純渲染／推導修正，資料與 DB／JSON 不受影響；一般（無迴圈）個體的家系圖與手足清單不變

- 背景：蘋果籽的 `japanese` 依規則留空（園方「赤ちゃん」非正式名）、ko 個體名走羅馬拼音，導致 ja/ko/en 介面都 fallback 到英文 Apple Seed，只有中文顯示「蘋果籽」；作者裁定 ja/ko 採直譯
- 純**顯示層**處理，資料正本不動（`japanese` 仍留空，轉正後自動走正式名）
- i18n：五語各補 `placeholder_name`／`placeholder_name_n`（多胞胎編號模板 `{n}`：りんごのタネ{n}号／사과씨 {n}호）
- `web/src/lib/data.js`：新增 `placeholderName()`；`displayName` 對 `placeholder` 個體在 ja/ko 回傳直譯名（覆蓋個體頁、動物園頁、日本家系圖）；`searchDataFor` ja 的 `j`／ko 的 `n` 換直譯名（原英文名移入 `en` 保持可搜尋）；`subGraph` 家族樹節點同步（ja index 1／ko index 0）
- 驗證：node 直跑 data.js 抽查 6 筆佔位個體五語輸出、search/subGraph/japanTreeData 皆正確（沙盒無法跑 Astro build，CI 建置時生效）

## 2026-07-14 ・ 網站：蘋果籽佔位條目全站標示 apple seed icon

- 目的：讓訪客一眼看出「這是當季寶寶，只是還沒有名字」（配合蘋果籽佔位制度）
- 原創 icon：`web/public/img/apple-seed.svg`（手繪風深紅棕籽身＋粗描邊＋白高光；參考讀者提供的庫存圖風格重繪，無版權疑慮）
- 資料管線：`export_json.py` 依 tags 含 `apple-seed` 輸出 `placeholder` 欄（比照 `unverified` 模式），轉正移除 tag 後重建即自動消失
- 顯示位置：
  - **個體頁**：標題旁 icon＋「尚未命名的寶寶」徽章（`Panda.astro`；i18n key `placeholder_badge`，五語皆補）；家族區塊親屬連結（`link()`）名字後掛小 icon
  - **搜尋結果**：卡片名字旁小 icon（`searchDataFor` 新增 `ap` 欄＋`search.js`）
  - **動物園頁**：現居／歷代／出生名單名字後掛小 icon（`Zoo.astro`）
  - **日本家系圖**：節點右上角掛 icon、資訊卡列徽章（`japanTreeData` 節點陣列第 10 欄＋`jptree.js`；遠景 LOD 隨方塊一起隱藏）
- 已於沙盒完成 Astro build（3842 頁）驗證五語頁面皆正常

## 2026-07-14 ・ 資料來源：RPF／redpanda-lineage 降為「線索」

- 背景：wiki 經作者大量校訂後可信度已高於 RPF/lineage（雜訊多），依作者裁定降低其權重
- 定位（CLAUDE.md 資料來源原則改寫）：不再是「初期基礎參考」，僅無官方來源時當線索；未經官方佐證的採用標 `🚧 待查證`；新條目 `sources` 官方公告優先、RPF 為輔
- `tools/audit.py`：lineage 比對改 **opt-in**（`--lineage` 才跑，預設僅 wiki 自身檢查）；`--strict` 擋關項目（rpf_id 重複）不變
- `tools/verify.sh`（pre-push）：移除 lineage clone/pull 步驟，收斂為 audit --strict + check_twins 兩步
- `tools/apply_lineage_fixes.py`：保留，但**僅作者明確要求時執行**（docstring 加警語，Claude 不主動跑）

## 2026-07-14 ・ 流程：當季寶寶「蘋果籽」佔位條目制度

- 出生季（夏季）新寶寶在園方命名前即可建檔佔位、直接上站。資格：父母皆確認＋生日確認（完整 YYYY-MM-DD）＋尚在世＋尚未命名
- 命名：`name: Apple Seed`／`chinese: 蘋果籽`，slug 一律含媽媽名 `apple-seed-媽媽slug-生日`；同胎多隻編號（蘋果籽1號＝`apple-seed-1-…`，序依園方公布、未公布依 RPF ID）；`japanese` 留空（「赤ちゃん」屬泛稱不入欄）
- 追蹤：tags 必含 `apple-seed`，每年 10 月起季末盤點；正式命名後轉正（改 slug、換全站 wikilink、移除 tag、補性別）；佔位期間夭折照 2026-07-02 慣例移 `wiki/_hidden/`
- 規範落地：CLAUDE.md「當季寶寶佔位條目：蘋果籽」新節、SCHEMA.md 命名規則與標籤表（`apple-seed`）

## 2026-07-13 ・ 工具重構（不影響網站與資料）

- **共用 frontmatter 解析層 `tools/wiki_io.py`**：原本 `build_db.py`／`audit.py`／`ig_audit.py` 各自實作 frontmatter parser，邊角行為（引號、inline list、空值）不一致，稽核工具與建檔工具可能看到不同資料 → 抽出單一實作，三支工具（含 `apply_lineage_fixes.py` 的日期正規化）一律 import `wiki_io`；`check_twins.py` 原本就借用 build_db 的解析，不受影響。已驗證重構前後 DB dump 內容、audit／check_twins／ig_audit 輸出完全一致
- **刪除 build_db.py 死碼**：`parse_residence_table`（2026-06-29 改以 frontmatter `zoos:` 為居住史唯一來源後即無人呼叫）
- **twins 寫入排序**：原以 set 迭代順序寫入、每次重建 DB dump 順序不同 → 排序後寫入，DB 內容可重現、利於比對
- **新規則：非日本個體不採 lineage 的 `ja.name`**：lineage/RPF 對每隻個體（含歐美）都機械附日文轉寫，僅「有日本居住史」（`zoos:` 含 `country == "Japan"` 的園）的個體才採用為 `japanese`（案例：Hui Hu 的「火狐」實為中文名）。`zoo_registry.py` 新增 `countries()` 判斷；`audit.py` 漢字提示與 `apply_lineage_fixes.py` 補漢字皆加此 guard，`zoos:` 空白時保守不補；原則記入 CLAUDE.md。順帶修掉 lineage 佔位值被當真值的問題：`(無名)` 不再被建議為漢字名、`born`／`died` 僅接受 YYYY 或 YYYY-MM-DD（排除 "unknown"）
- **文件歸位**：`DATA-CORRECTION-PLAN.md`、`_西山まとめ_對帳/` 移入 `docs/`；CLAUDE.md 校正條目數（360+→600+）並補齊目錄樹（wiki_io.py、ig_audit.py、docs/、sources/、CHANGELOG.md、report-intake-SKILL.md、wiki/_hidden/、五語 i18n）

## v0.10.1 — 2026-07-06 ・ 修正：手機版 header icon 顏色不一致

- **右上角 icon 統一顏色**：語言切換的地球 icon 原本多掛 `text-ink-soft`（淺灰棕），與深色模式切換（月亮）、漢堡選單的 `--ink` 不一致，手機版三顆並排特別明顯 → 移除該 class，改與其他 icon 一樣繼承 `.nav-link` 的 `currentColor`，深淺色模式都一致

## v0.10 — 2026-06-30 ・ 照片投稿 CTA + 圖片集隨機

- **照片投稿**：圖片集區塊新增「想幫 ○○ 補照片嗎？」CTA，點按鈕才載入 Tally 投稿表單（三語「幫忙補照片」`lb5zVv`，由 `ODr777` 複製改造，保留 `panda/slug/url` hidden fields）。**CTA 一律顯示**，零照片的個體也鼓勵投稿；表單 ID 接在 `web/src/lib/feedback.js` 的 `PHOTO_FORMS`／`photoFormId`
- **單次上限 10**：投稿表單以一個多行欄位「IG 連結（一行一個，最多 10 個）」承接（軟性上限，作者逐筆 triage；屬非權威收件匣）
- **圖片集隨機呈現**：`Panda.astro` 加 client-side 混合隨機（釘最新 1 張、其餘每次造訪 Fisher–Yates 洗牌）。只洗佔位卡順序、lazy-load 不變、不重建 iframe，效能等同原本，並讓不同投稿者照片分散
- 新增三語字串 `photos_cta`／`photos_cta_btn`（`pipeline/src/i18n/*.json`）

## v0.9 — 2026-06-30 ・ 圖片集 facade 載入 + 攝影者署名

- **圖片集改方案 C**：facade ＋ lazy-load（IntersectionObserver）。開頁只有零 iframe 的骨架卡，捲到視窗附近才換成真 IG embed；超過 6 篇「顯示更多」。對少照片個體零負擔、多照片也不爆
- **攝影者署名**：`instagram:` 改建議存含帳號的完整形式 `instagram.com/帳號/p/XXX/`，照片載入前的 facade 卡顯示 `@帳號`（載好後由 embed 自身帳號接手，不重複）。既有 6 隻連結已回填帳號
- **修正**：embed.js 只認 `/p/SHORTCODE/`，含帳號的 URL 會載不出 → 餵 embed 時正規化 permalink，資料與「點照片開原貼文」仍保留完整含帳號形式
- **新增 `tools/ig_audit.py`**：列出所有 `instagram:` 連結、標「未含帳號形式」與（`--check`）「疑似失效」供人工複查

## v0.8 — 2026-06-14 ・ 家系圖手足視覺 + 中文名欄位

- 家系圖：半血手足以淡虛線區分（全血實線、雙胞胎琥珀虛線），全血在前排列，節點縮小較不擁擠
- 新增 `chinese` frontmatter 欄位：台灣／中國出生個體的中文名，中文介面優先顯示（先補齊台北可○系列：可忻、可玥、可麗餅、可頌、可樂果、可麗露）
- 套用於家系圖、個體頁、搜尋、家族列表

## v0.7 — 2026-06-14 ・ 家系圖手足、IG 排序分頁、樣式修正

- **家系圖顯示手足**：個體頁家系圖現在會在同列畫出全血／半血手足（例如 Yaffa 頁可見弟弟 Yammy），連回共享的父母
- **IG 多貼文**：可在 frontmatter 連結後加貼文日期，依貼文時間新到舊排序；超過 6 篇以「顯示更多」延後載入
- **修正**：Tailwind 未掃描 `public/js`，導致搜尋結果等前端渲染的名字樣式跑掉（擠在一起）；搜尋卡片副名簡化、去除重複

## v0.6 — 2026-06-14 ・ 動物園名稱在地化

- 動物園名稱依語系顯示：中文＝中文名→日文漢字→英文；日文＝日文名；英文＝英文
- 新增 22 個非日本動物園的中文名（`pipeline/data/zoo-names.json`，可手動增修），例如台北、首爾、鹿特丹
- 卡片、地圖彈窗、個體頁居住史皆套用

## v0.5 — 2026-06-14 ・ IG 照片展示 + 個體網址改版

- 個體頁新增**照片區**：讀 wiki frontmatter 的 `instagram:` 連結，用 Instagram 官方 embed 顯示（自動署名、連回原貼文，不複製圖片檔）
  - 維護方式：在條目 frontmatter 加 `instagram:` 公開貼文連結 → 重建即顯示
  - 首批：`yaffa` 加入作者拍攝的貼文
- **個體網址加上生日**：`/p/shin-fa/` → `/p/shin-fa-2019-06-19/`，避免同名混淆（slug 仍為資料主鍵）
- （後續：開放同好投稿照片的表單，寄作者審核後收錄）

## v0.4 — 2026-06-14 ・ 改用 Astro + Tailwind

- 網站從第一版純 HTML 生成器，遷移到 **Astro + Tailwind CSS**（`web/`），元件化、好維護
- **深色模式**：以系統設定為優先，導覽列可手動切換並記住
- PWA 改用成熟的 vite-pwa（Workbox），更新與快取更穩定
- 改用 **pnpm**；GitHub Actions 同步調整
- 修正：首頁搜尋／動物園按鈕對齊
- 資料管線（`tools/`、`pipeline/scripts/export_json.py`）與 wiki 完全不變

## v0.3 — 2026-06-13 ・ 內容與體驗

- **今天的小熊貓**：首頁顯示當日生日與當日「前往小熊星球」（🌈）
- **語系名字顯示**：中文＝漢字（無則退英文）、日文＝日文名、英文＝英文
- **動物園 logo**：用官網 favicon，可在 `pipeline/data/zoo-logos.json` 手動覆蓋
- **資料完整度檢查工具**（`tools/audit.py`）：與 redpanda-lineage 本地比對，不重爬 RPF
- 家系圖手機體驗：雙指縮放、拖曳平移、載入置中於焦點
- 全站手機版 RWD 調整

## v0.2 — 2026-06-13 ・ 多語系、上線

- **三語系**：中文／日文／英文；首訪依瀏覽器語言自動切換，可手動選（下拉選單）
- 推上 **GitHub Pages**，GitHub Actions 自動建置部署
- 動物園地圖改本地化 Leaflet（無 CDN 依賴）、資料內嵌，離線可用
- 修正地圖跑版

## v0.1 — 2026-06-13 ・ 初版 MVP

- 由 `wiki/*.md` 自動生成的靜態圖鑑網站
- 個體檔案頁（生日、物種、居住史、家族關係）
- 圖鑑搜尋（名字／動物園／性別／在世篩選）
- 動物園地圖（Leaflet + OpenStreetMap，含路線導航）
- 互動家系圖（祖先／後代展開、雙胞胎）
- i18n 與 PWA 骨架
