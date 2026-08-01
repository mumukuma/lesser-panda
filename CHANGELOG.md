# 網站更新紀錄 Changelog

> 記錄**網站功能**的演進（新功能、改版、修正）。
> 小熊貓**資料**的異動請見 `wiki/log.md`；願望與規劃見 `ROADMAP.md`。
> 新的在最上面。

---

## 2026-08-02 ・ 建檔政策：檔案卡的「性別必填」門檻放寬（有家系連結可留空）

處理都江堰小熊貓森林公園的讀者回報批次時撞到門檻：黑帥（父為心心）、年年（父為陽陽）兩隻有明確父系線索，卻因回報未提性別而被 `CLAUDE.md` 的「`sex` 必填」擋在 `cn-candidates.json`，結果心心・陽陽兩位種公的子女表殘缺、家系圖斷鏈。維護者裁定兩隻照建、性別留不詳，並要求把規則一併修進 `CLAUDE.md`。

- **`CLAUDE.md`「資料有限個體：檔案卡」章節**新增「性別門檻」小節：原則仍是性別已知才建檔，**例外是「父／母／子女／配偶其中一方已建條目」時性別可留空**。同時明訂性別留空的寫法（`sex:` 空白、tags 不加性別 tag、內文標「性別待確認」、index 寫「不詳」）與回補流程。
- **明訂由關係語推定性別的規則**：「父親是X」→ X ♂、「母親是Y」→ Y ♀、「Z 的老公」→ Z ♀ 且本人 ♂；但**關係語只描述對方時不可硬猜本人性別**，名字用字（帥／妹等）亦不足以推定。此批 心心・陽陽・圓圓・開開 四隻即依此推定性別建檔。
- **釐清與既有紅線的關係**：家系連結可替代「性別」門檻，但**永遠不能**替代「綁定已登記園」的硬門檻（2026-07-24 那條「親屬關係不能替代綁園」原文保留，另加註不衝突）。
- **`sources` 兩行慣例入典**：讀者回報經維護者採用者寫 `讀者回報（@帳號，佐證方式，YYYY-MM-DD）` ＋ `維護者提供（YYYY-MM-DD）`，前者記出處、後者記建檔依據，兩者皆無 host 故 `has_official_source` 仍為 false。
- **盤點指令**：`grep -l "^sex:$" wiki/*.md` 可列出性別留空的條目（含蘋果籽，以 tags 區分）。
- 無程式碼變更——資料模型本來就支援 `sex` 留空（蘋果籽佔位條目一直如此），`build_db` 記為 `sex: unknown`、不計入性別統計，總數與園頁照常顯示。

## 2026-07-27 ・ 來源判定：X（Twitter）園方官方帳號可列為官方來源

個體頁的「來源」區塊原本只顯示官網／政府公告／園報／微信，X 一律不顯示。但多數日本園以 X 為主要公告管道（出生・命名・雌雄鑑定・訃報常只發在 X、官網不另發稿），導致只有 X 來源的條目在站上顯示「未經官方佐證」。

- `tools/build_db.py` 新增 `OFFICIAL_X_ACCOUNTS` 白名單，比照既有 `OFFICIAL_FB_PAGES` 的做法：X 是共用網域不能整域列入，改比對 URL 路徑第一段的 handle。`_X_HOSTS` 涵蓋 `x.com`／`twitter.com`／`mobile.*`。
- 首批登記四個園方帳號：`nishiyama_zoo`、`nhdzoo`、`ichikawa_zoo`、`kumamotocityzoo`。個人／粉絲帳號（如 `0yDeN464cBT145p`）不列入。
- 影響：3 筆條目 `has_official_source` 由 false 轉 true（兩隻西山蘋果籽、熊本 `apple-seed-shin-fa`），另 4 筆條目來源區塊多顯示一條園方 X 連結。
- 日後新增園方 X 帳號只需把小寫 handle 補進該集合即自動生效。

## 2026-07-26 ・ 修正：iOS 上中文標題失去圓體、性別符號 ♀♂ 變彩色 emoji

維護者回報「iPhone 上字型都不見了，只有日文有吃到字型，而且性別 icon 跑版」。兩者都是同日 `:lang()` 字型改版的迴歸，Mac 上看不出來。

- **中文標題失去圓體**：改版把 `--font-display` 的後備鏈拆成 `--font-cjk-round`，中文只留 `Yuanti TC／SC`。**Yuanti 是 macOS 專屬字型、iOS 沒有內建**，於是 iPhone 上中文標題整條後備鏈落空、退回 `--font-body` 的 PingFang TC 黑體；日文因為 `Hiragino Maru Gothic ProN` iOS 有內建而不受影響，看起來就像「只有日文吃到字型」。改版前的鏈末端本來就有 Hiragino Maru 兜底，拆分時漏掉。**修法**：中文的 `--font-cjk-round` 末端補回 `'Hiragino Maru Gothic ProN'`。代價是 iOS 中文**標題**的漢字為日文字形（內文仍走正確的 PingFang），這是刻意取捨——iOS 沒有任何內建的中文圓體，維護者選擇保留圓體調性。
- **♀♂ 變彩色 emoji**：U+2640／U+2642 在 Apple 平台屬「可 emoji 化」碼位，字型鏈裡沒有任何字型收錄它時會退到 **Apple Color Emoji**，字寬變大、基線偏移、且吃不到 `text-female`／`text-male` 的顏色，就是「跑版」。起因是中文鏈改以 PingFang TC 打頭而 PingFang 沒收這兩個符號（鏈中其餘 Noto／JhengHei／Heiti 在 iOS 上都不存在）；改版前 `Hiragino Sans` 打頭時它有收，所以一直正常。**修法**：新增 `unicode-range: U+2640, U+2642` 的 `@font-face 'RPW Symbols'`，用 `local()` 只對這兩個碼位借一套確定有收錄的系統字（日文字型自 JIS X 0208 起皆含 ♀♂），並置於五條 `--font-body` 之首。不下載任何檔案、其餘文字完全不受影響；`local()` 在 WebKit 比對家族名、Blink 比對 full/PostScript name，故兩種都列，比對不到就自然落空、不會比現況更糟。此法一次涵蓋所有出現處（i18n 的 `sex_f`／`sex_m`、Stats、JpTree、search.js、jptree.js），毋須逐處插入 U+FE0E，也不影響 satori 產的 OG 卡。
- 驗證：沙盒 `pnpm build` 通過，4327 頁；抽驗產物 CSS 確認 `@font-face` 的 `local()` 與 `unicode-range` 經 minify 後完整保留、五條 `--font-body` 都以 `RPW Symbols` 打頭、中文 `--font-cjk-round` 末端有 Hiragino Maru。

## 2026-07-26 ・ 修正：CJK 字型改依 `lang` 切換（漢字統一造成的字形錯置）

維護者問「站上有各國文字，是否該改用 Noto 字型」。**結論是不自架 Noto**，但查證過程發現一個既有的實際缺陷並修掉。

- **不自架 Noto 的理由**：`--font-body` 原本就把 Noto 列在 stack 裡，只是沒有 `@font-face`，所以只有本來裝了 Noto 的裝置（Android／Linux）吃得到。自架的代價是 Noto Sans TC/SC/JP/KR 每套完整 woff2 數 MB；即使用 unicode-range 分片，一頁 CJK 內容仍要抓 300KB–1MB。缺字不是問題（各家系統都內建完整 CJK＋諺文），這個代價換不到相稱的效果，與 mobile-first 原則衝突。
- **真正的缺陷**：`--font-body` 全站固定以 `'Hiragino Sans'` 打頭。因**漢字統一（Han unification）**，同一碼位在中／日字型下字形不同（骨・直・海・每・令…），所以 Apple 裝置上**中文頁的漢字一律被渲染成日文字形**。這不是換成 Noto 能解的——同一頁同時有中文 UI 與日文園名／個體名，單一字型本來就無法兩者都對。
- **修法（零位元組成本）**：`global.css` 改用 `:lang()` 指定各語系的系統字順序，Noto 一律留在第二順位當後備。zh-Hant → PingFang TC；**zh-Hans → PingFang SC／Noto Sans SC／Microsoft YaHei**（簡體先前完全沒有對應字型、跟繁體共用同一組 stack，Windows 上會拿到繁體字形）；ja → Hiragino Sans；**ko → Apple SD Gothic Neo／Noto Sans KR／Malgun Gothic**（先前 stack 裡沒有任何諺文字型，靠 `system-ui` 兜底）；en → system-ui。選擇器**不加 `:root` 前綴**是刻意的——這樣才能同時作用於 `<html>` 與頁內個別標了 `lang` 的元素。
- **頁內混排的日文名加 `lang="ja"`**：`Panda.astro` 的副名列從 `altNames.join(' · ')` 改為逐項帶語系的 `altEntries`（`p.name`→en、`p.japanese`→ja、`p.korean`→ko）；`search.js` 的 `altOf` 在副名等於日文名且非日文頁時補 `lang="ja"`；語系下拉的 `<option>` 帶 `lang`。`:lang()` 沿 DOM 繼承，故這些元素在中文頁也會拿到日文字形。
- **未動的部分**：園名不需處理——`zooName` 對中文語系走 `zh` 欄位，344 座園全部有值；`ja`／`en`／`ko` 頁各走自己的欄位。家系圖（`tree.js`／`jptree.js`）的節點名走 `displayName(p, locale)`，本來就是該語系的名字。
- 驗證：沙盒 `pnpm build` 通過，4302 頁；抽驗產物確認五語 `<html lang>` 正確（zh-Hant／zh-Hans／ja／en／ko）、CSS 五條 `:lang()` 規則都在、`yuuta-2006-06-02` 的日文名在 zh-Hant／zh-Hans／ko 頁都帶 `lang="ja"`，在 ja 頁則因等於主名而正確被濾除。

## 2026-07-26 ・ 修正：圖鑑篩選改為 faceted counts（數字與狀態不一致）

維護者回報「filter 的狀態跟數字不一致」。確認是同日新增數量顯示時留下的缺陷，非狀態管理函式庫的問題。

- **症狀**：下拉的數量在初始化時對全庫 702 算一次就寫進 DOM 文字，之後任何條件變動都不重算。選「地區＝中國（88）」後，性別仍寫 ♀ 356／♂ 333（實際是 ♀ 56／♂ 29／未定 3），年齡仍寫「12 歲以上（122）」而中國那 88 隻其實是 **0**——點下去得到空結果。
- **另兩個衍生的不一致**：(1) 只有動物園下拉會跟著地區連動，其餘三顆完全不動，看起來像隨機行為——因為 `apply()` 直接從各 DOM 讀值、數字烙在 init，缺少一條「狀態 → 全部重算」的路徑，加連動時只手動接了一顆。(2) 同一排下拉數字的分母不同：性別三項加總 702，年齡五層加總只有 327（年齡隱含現存且需完整生日），資料三項本就重疊，使用者無法從數字反推它在算什麼。
- **修法**：`search.js` 重構為單一流程 `readState() → refreshFacets() → 算結果 → draw()`，**不引入任何函式庫**。每顆下拉的數量＝套用「其他所有條件、但不含自己」後的數量（`matches(p, s, except)`），所以數字恆等於「點下去會得到幾筆」；少了 except 自己這一步，選了某項後該顆下拉會塌成只剩該項。
- **0 的選項**：短清單（性別／年齡／資料／地區）保留並顯示（0）＋`disabled`（「條件存在但現在沒有」本身是資訊；目前選中的那項不 disable，免得鎖死）；動物園 121 項太長，0 的直接不列——**原本手寫的「地區連動篩減園清單」因此可整段刪除**，不屬於所選地區的園自然算出 0。原選的園若歸零仍退回「全部」。
- 連帶簡化：刪除 `fillZoos()`／`annotate()`／`zooRegion`／`zooEntries`；`regions[].c`（建置期算的地區園數）不再寫進標籤，改由 client 端 faceted 重算；`?zoo=` 參數改在第一輪 `apply()` 之後才設（選項是動態產生的）。
- **效能**：每次重算掃 5 個 facet × 702 隻，實測平均 **0.3ms**（連打 20 次共 7ms），初始化含首次 render 8ms。不需要 debounce。
- 驗證：以假 DOM 載入真實 `search.js` 跑過八種情境——地區切換後三顆下拉數字與資料層獨立計算相符；自己那顆不會塌（中國×♀ 仍顯示 ♂ 29）；選了園之後園清單不塌（仍 13 座）；地區改日本後原選的中國園自動退回「全部」；「無居住史」時園清單 0 座、地區全部變灰。五語各跑一遍無 `undefined`／`NaN`。

## 2026-07-26 ・ 網站：圖鑑加「年齡」與「資料」兩個篩選

同日「地區」篩選之後的第二批。維護者從候選清單挑了這兩個。

- **年齡層**（`#f-age`）：未滿 1 歲（16）／1–3（33）／4–7（63）／8–11（93）／12 歲以上（122）。**選了任一層即隱含現存**——已故個體的年齡是享壽、不是現齡，混在一起會讓「12 歲以上」同時撈出在世高齡與早逝已故者，語意不成立。「現存」定義與既有 `#f-alive` 一致（`!died && !unverified`），故 383 隻現存中 56 隻無生日者落不進任何層、只在「全部」看得到。高齡 12+ 竟是最大組。
- **資料狀態**（`#f-data`，維護用途）：待查證 `unverified`（8）／缺完整生日（94）／無居住史（3）。把資料不完整的個體撈出來盤點——本日補 `ki-ki-1996` 等七隻的居住史全靠手動 grep，有這顆按鈕會快很多。三個判準都用既有前端欄位（`uv`／`born`／`zoo`）算，**未改管線**。此下拉對讀者也可見（與站上既有的 🚧／待查證標記一致的透明度）；若要改成僅維護者可見，可加 URL 參數閘門。
- **既有的性別下拉一併帶上數量，並補第三個選項「? 性別未定」**（♀ 356／♂ 333／未定 13＝702）。緣由：把 `f-sex` 從獨立一行搬進「性別＋年齡」並排容器後，它在 diff 裡整行變成 `+`、看起來像本次新加的功能（實際上自 `8f75968` Astro 遷移就存在），維護者因此詢問；確認保留並改為「標籤（數量）」樣式。**接著發現顯示數量會暴露一個既有缺口**：`build_db.py` 把空白 `sex` 正規化為字串 `"unknown"`（10 隻蘋果籽性別待園方公布＋`bei-bei`／`te-xiang-bao`／`you-you` 三隻中國個體未公布），這 13 隻原本只有選「性別：全部」才撈得到，♀＋♂ 也加不到總數。補上 `filter_sex_unknown`（五語）後三項加總 = 702。此選項對維護者另有用途：蘋果籽季末盤點性別可直接列出。
- 三個下拉的**數量都在 client 端算**（`annotate()`），不寫進 i18n 標籤——標籤只放文字，數字永遠跟著資料走。註記：`annotate` 的呼叫必須在 `ageOf` 定義之後（`var` 函式表達式不會提前可用）。
- **手機排版**：控制列從 7 個元件變 9 個，若沿用每顆 `w-full` 會堆成九行。改把下拉兩兩包成一列（地區＋動物園、性別＋年齡，各 `flex-1 sm:flex-none`），桌機外觀不變。
- i18n 五語各補 10 個 key（`filter_age`、`age_baby`／`1_3`／`4_7`／`8_11`／`senior`、`filter_data`、`data_unverified`／`no_birthday`／`no_residence`），233 keys 一致。
- 驗證：以假 DOM 載入真實 `search.js`，五個年齡層與三個資料選項的結果數與資料層獨立計算完全相符；交叉條件（日本 × 12 歲以上 × ♀ = 59）正常；確認已故者不會混入年齡層。Astro compiler 編譯零 diagnostics。
- **未採納的候選**：出生月份 filter——小熊貓 92% 生於 6 月（327）與 7 月（244），兩個選項就吃掉全部，做成 filter 沒有篩選力。這個偏態本身適合放進統計頁當圖表。其餘候選（亞種 styani 664／fulgens 35、跨國移居 81、出生園、有雙胞胎 352、有子女 290、只住過一座園 275）維護者本次未選，留待日後。

## 2026-07-26 ・ 修正：中文介面露出日文地點、現居誤判、註冊表重複登記

由 `ki-ki-1996`（生於多摩、後移居墨西哥，日期不詳）一筆資料連帶查出的三個問題。

- **中文介面顯示日文地點**：`zooLocation` 對中文語系是 `location_zh || location_ja || …`，而 `location_zh` 多數園留空——日本園退回 `location_ja` 是刻意的（漢字中文讀者可讀），但**非日本園的 `location_ja` 是片假名**，中文介面就會直接吐日文。全庫 3 座園中此症：チャプルテペック動物園（メキシコ・メキシコシティ）、Buin Zoo（チリレヒオン・メトロポリターナ州ブイン）、大崎公園（さいたま市，日本園、0 現居未上架）。前兩座補上 `location_zh`（墨西哥墨西哥城／智利首都大區布因）。**園名本身無此問題**（`name_zh` 有值）；另有 96 座園無 `name_zh`、中文介面顯示日文或英文名，屬既有取捨、未動。
- **`export_json.py` 現居誤判**：居住史排序原為 `COALESCE(start_year, end_year), id`，起訖「都」不明的一筆（`? – 現在`：只知現在在此、不知何時抵達）會被 NULL 排到最前，導致「由後往前找 `end IS NULL`」的現居判定取到前一站。實例：`ki-ki-1996` 多摩 1996 → 墨西哥 `? – 現在`，現居誤判為多摩、地區跟著誤標日本。改為 `COALESCE(start_year, end_year, 9999)` 讓這種筆排最後；**全庫比對只有 `ki-ki-1996` 一隻的現居判定改變**（其餘 701 隻不動）。
- **`data/zoos.json` 重複登記**：`Chapultepec Zoo`（`lineage_id` 66）與 `チャプルテペック動物園` 是同一座園。保留後者（wiki 條目實際在用、有 `location_ja`／中文名／五個 aliases），承接前者的 `lineage_id` 66 與 map；註冊表 345 → 344 座。隱含風險已解：英文那筆存在時，日後誤寫成它不會報錯、會靜靜裂成兩座園。**副作用**：無 `lineage_id` 的園走 9000+ 合成 ID、依陣列順序編號，故刪一筆會讓其後的合成 ID 平移——ID 僅為建置期內部識別（網址走 slug），重建後自洽，但編輯註冊表時要知道合成 ID 不穩定。
- **`gen_residence.py` 國旗表補齊**：`CFLAG` 缺 Mexico／Macau／Singapore／New Zealand，居住史表格對這些園不顯示國名與國旗。補四國並同步 `_COUNTRY_WORDS`（地點去重前綴用）。

## 2026-07-26 ・ 網站：動物園地圖與圖鑑加「地區」篩選

- 背景：兩頁原本只能靠文字搜尋或動物園下拉找園／找個體，沒有「先收窄到某個地區」這一層。動物園頁 107 座園、圖鑑頁 121 座園的下拉都太長。
- **措辭刻意用「地區」不用「國家」**（i18n key `filter_region`；地区／地域／Region／지역）。台灣、香港、澳門在 `data/zoos.json` 的 `country` 欄與各國並列，掛「國家」標籤會讓部分讀者讀成主權主張；「地區」不表態（同 Apple／Google 的 Country or Region 慣例）。**資料欄名維持 `country`**（正本欄名不動），只換顯示層用詞——故 `data.js` 的 `countryKey`／`countryName`／`countryOptions` 命名對齊資料來源。維護者一度考慮整個撤掉此功能，改標籤後保留。
- **地區譯名表**：`data.js` 的 `COUNTRY_NAMES`，涵蓋 `data/zoos.json` 目前全部 39 個國家值 × 五語，以小寫 key 查表（歷史資料有 `france`／`Germany` 大小寫不一）；查不到原樣顯示英文，不致漏園。zh-CN **不走 `toHans` 機器轉**——國名大陸慣用譯名常整詞不同（義大利→意大利、紐西蘭→新西兰、澳洲→澳大利亚），逐筆手寫。
- **動物園頁**（`Zoos.astro`／`js/zoos.js`）：卡片加 `data-country`，下拉與排序併成一列（手機各佔一半）。選了地區後**地圖一起過濾並縮放**——沿用既有 `zoo-filter` 事件，把 `detail.q` 由「有搜尋字串」擴充為「有任何過濾生效」。17 個地區選項（僅列有現居個體的園）。
- **圖鑑頁**（`Search.astro`／`js/search.js`）：18 個地區選項（多一個阿根廷——有已故個體最後居住於此）。`searchDataFor` 每隻加 `r` 欄＝代表園的地區 key，**認定沿用既有 `zoo` 欄邏輯**（在世＝現居園、已故＝最後居住園），兩個 filter 才不會互相矛盾。**地區連動篩減動物園下拉**：選日本後園清單 121→66，原選的園若不屬新地區則退回「全部」，同地區內重建則保留；新增 `?region=` URL 參數（須在 `?zoo=` 之前套用）。代價：`searchDataFor` 同時餵首頁 `TODAY_DATA`，`r` 欄使首頁內嵌資料多約 8 KB（148→156 KB，gzip 後更少），未拆函式。
- **`gen_residence.py` 新增 `birth_zoo: unknown` 旗標**（連帶 SCHEMA.md）：居住史首站起始日不詳時本來一律標 🐣 出生地，但來源明寫「出自不明」的個體（多摩名單的華華・中中）標了就與來源矛盾。填此欄即不標 🐣，**既有 70 個靠「起始留空 → 🐣」的條目行為不變**（多為中國檔案卡）。
- 驗證：五語 i18n key 一致（223 keys）；`countryOptions` 覆蓋全部 107 座上架園、無落回英文原字；`searchDataFor` 702 隻中 692 隻有地區（無地區的 10 隻本來在動物園 filter 也濾不到，非新盲區——同日補了 6 隻，見 `wiki/log.md`）；園名→地區一對一無衝突（連動的前提）；以假 DOM 載入真實 `search.js` 跑過連動的四種邊界；Astro compiler 編譯 `Zoos.astro`／`Search.astro` 零 diagnostics。**未跑整站 build**（沙盒限制），待本機 `pnpm build` 覆核。

## 2026-07-24 ・ 流程：中國個體檔案卡建檔門檻放寬（階段 A 政策）

- 背景：中國個體常無官方公告，現行檔案卡門檻要求「至少一筆官方／一手來源」，導致許多有名有姓、綁得上園的個體卡在候補名單。實務上 `xiao-xiao-bai-nanjing` 等早已以「維護者提供、無官方佐證」建檔——本次把既成實務正式寫進政策。完整分析與執行計劃見 `docs/中國個體建檔放寬-計劃.md`。
- **新門檻（放寬）**：名字＋性別已知、**綁定 ≥1 已登記園（硬門檻）**、有官方／讀者展牌／**維護者親自確認**任一佐證即可建檔；**官方來源不再必要**。紅線：嚴禁僅憑 RPF/lineage 機械資料無人確認就建檔（續留 `cn-candidates.json`）；親屬關係不能替代綁園。
- **兩軸分工**：佐證軸＝`has_official_source`（由 `build_db` 官方來源分類自動推導，不新增手動 tag，待階段 B 於 `export_json` 輸出旗標）；在世軸＝`unverified`（維持只表動向不明，禁為觸發標記而濫掛）。
- 本次僅動政策文件：`CLAUDE.md`「資料有限個體：檔案卡」章節改寫。階段 B（`export_json` 加 `has_official_source`）、階段 C（網站「維護者提供・未經官方佐證」標記＋五語字串）另行執行。
- 另：即日起指稱維護者一律用「維護者」，不再用「作者」（歷史文字不追改）。

## 2026-07-21 ・ 修正：神戸市立王子動物園官網未列入官方來源白名單

- 症狀：`太郎`（tarou-1989-07-01）條目的來源（王子動物園官網 `ojizoo.jp`、園報 `はばたき` PDF `kobe-ojizoo.jp`）皆為官方，但個體頁「來源」區塊空白。
- 原因：`tools/build_db.py` 的 `OFFICIAL_HOSTS` 白名單漏收此園兩個網域，`is_official_source` 判為非官方而濾除。連帶影響所有以 `kobe-ojizoo.jp` 為來源的王子動物園個體（如 `ten-ten-1991-06-29` 之訃報頁）皆未顯示來源。
- 修正：`OFFICIAL_HOSTS` 補入 `kobe-ojizoo.jp`（現行官網）與 `ojizoo.jp`（舊官方網域）。重建後 `太郎` 兩筆來源、`ten-ten` 訃報頁來源皆正常顯示。（`jazz`／`gaia`／`nohana` 仍空白，因其來源為 RPF 等非官方管道，屬正確過濾。）

## 2026-07-19 ・ 網站：首頁「今日休園」欄（休園日規則引擎）

- 背景：園頁已標 🗓️ 休園日（同日稍早），首頁再加「今天哪些園休園」一眼看。client 端以 JST 判斷（deploy 無 cron，比照今日生日／新鮮的寶寶模式）；今日無休園整個區塊隱藏。位置在「今天」區塊下方，**取代原「從這裡開始」區塊**（與 footer 資訊重複，作者裁定移除；孤兒 key `home_featured`／`home_intro` 五語同步移除）。配套：原「今天」區塊標題與「今日休園」語意重複，`today_title` 改為**「紀念日」**（纪念日／記念日／Anniversaries／기념일，作者裁定）
- **資料**：`data/zoos.json` 新增選填欄 **`closed_rule`**（機器可讀規則陣列，任一命中即休園），43 園依已查證 `closed_ja` 文字草擬。**維護原則：`closed_ja` 為人讀正本、`closed_rule` 為衍生欄，某園休園制度改了兩欄必須同步改**（已註記 CLAUDE.md）。schema 涵蓋：`weekly`（週休＋祝日處理 none／open／next_day〈連續祝日跳過〉／next_weekday〈直後平日〉，可加 `months` 季節窗、`skip_nth`、`suspend` 無休窗）、`nth_weekly`（第 N 週型：大牟田第2・4月曜、富山第1・3火曜；`shift` 表「指定日開園翌日休園」熊本第4月曜型）、`week_of_nth_dow`（円山「4月・11月の第2水曜を含む週の平日」型）、`range`（每年重複，from>to 跨年）／`date`（宮崎 12/31、東武元日）、`range_abs`（長期休園：甲府整修〜2027-03-31、野毛山 2027-01-07 起）
- **不編規則**（永不出現在今日休園）：不定休／営業カレンダー制 11 園（那須王国、AWS、東北サファリ、姫セン、ひらパー、市原ぞうの国、神戸どうぶつ王国、桐生が岡、かみね＋**旭山**〈夏冬期間切替もカレンダー告知，同列〉＋**池田**〈作者複核改列カレンダー制〉）、年中無休 10 園
- 模糊語處理（不腦補原則）：「春休み／GW／夏休み／年末年始／繁忙期は無休・開園」類無休窗採**慣例日期窗**（3/25–4/7、4/29–5/5、7/20–8/31、12/28–1/4）抑制該週休規則，rule 的 `note` 標「慣例窗，非官方日期」——寬鬆抑制、寧可漏列不誤列；官方未給日期的「年末年始」（市川、江戸川、到津）不編進規則、`note` 註明未編碼
- **祝日表**：`closed.js` 內嵌 2026–2030 日本祝日（jpholiday 產生，含振替休日・国民の休日；抽驗對照官方／曆法來源：2026 銀週 9/21–23＋GW 5/6 振替、2028 春分 3/20・秋分 9/22、2029 振替 2/12・4/30 皆符）——比照 season.js 內嵌節氣表前例；表外年份視為無祝日（規則退化為照字面曜日休）
- 管線／前端：`export_json.py` 傳遞 `closed_rule`；`data.js` 新增 `closedDataFor(locale)`（園名依語系、chip 連 `z/<slug>/`）；**`js/closed.js`** ＝規則引擎＋首頁渲染（共用處；node 可直接載入計算核心供測試）；`Home.astro` 新增 `#today-closed-wrap` 獨立區塊
- i18n：五語加 `today_closed`（🗓️ 今日休園／今日闭园／本日休園／Closed today／오늘 휴원）＋ `today_closed_note`（依通常時間表推算，臨時開閉園以官網公告為準）
- 驗證：`web/tests/closed.test.mjs` 68 條斷言全過（祝日月曜順延、GW 連續祝日翌平日跳到 5/7、第 N 週、季節窗邊界 11/30↔12/7、年末年始跨年、甲府休園中、円山週平日、熊本第4月曜、suspend 慣例窗、大森山「1–2月土日祝のみ開園」、年中無休／不定休不出現）；假日期抽查（2026 7/20 海の日・7/21 順延日・7/22 水曜・2027 元日・11/24 振替翌日）園單與 `closed_ja` 文意一致；`/tmp` 全量 Astro build 通過、五語首頁抽查

## 2026-07-19 ・ 網站：二十四節氣主題（色彩微調＋首頁節氣標示）

- 背景：四季主題之上再依二十四節氣做「季內 6 段」的輕量色彩漸變，讓常訪的讀者感覺網站跟著時序活著；背景圖等重資產仍走四季、不增加
- **日期表**：`season.js` 內嵌 2026–2035 年 JST 節氣日期表（sxtwl 天文計算預產，驗證立春 2/4、夏至 6/21 等；含 2026 雨水因 JST 時差落 2/19 的邊界）；表外年份借最近一年（節氣逐年僅 ±1 天，UI 無妨）。手動切季映射該季月份窗第一個節氣（春=驚蟄、夏=芒種、秋=白露、冬=大雪）
- **CSS**：`data-jieqi`（24 值）淺色覆寫 `--sky-1/--sky-2/--leaf/--leaf-deep` 並新增節氣點綴色 `--jq-ac`／`--jq-ink`（色票參考日本傳統色：春分櫻粉、芒種紫陽花、冬至柚子黃…）；深色天空過暗微調無感、只換提亮版點綴色。區塊置四季覆寫後（同特異度後者勝）、深色四季（0,3,0）仍壓過淺色節氣值；no-JS 無 `data-jieqi` 自然退回
- **首頁節氣標示**（hero、印章式）：明朝體大字（依語系）＋英文小 caps（設計元素、全語系同、藏在 season.js 不進 i18n）；文字由 season.js 填入、no-JS 保持 hidden。原設計另有直排「入節日」行（中日=漢字數字、韓=N월 N일、英=JUL 7），上線後整個節氣期間都顯示同一日、易誤讀為今日日期，7/20 作者裁定移除（殼／填字碼／CSS 三處清除，字型重新子集化剔除漢字數字 47→35 字，需要時再加回）
- **字型**：`fonts/jieqi-mincho.woff2` = Noto Serif CJK TC Light 子集（節氣用字＋和製漢字＋簡體變體共 35 字、17KB，僅首頁用到才下載）；韓文名退回系統明朝系 serif。重新子集化流程：git sparse clone notofonts/noto-cjk 取 OTF → pyftsubset（沙盒 Google Fonts API 被擋）
- **i18n**：五語各補 24 個 `jq_*` key（日文用啓蟄／小満／処暑、韓文한글、簡體手工惊蛰／谷雨／处暑，en 印章大字沿用繁體漢字）；dev 季節鈕 title 附當前節氣
- **家系圖色系共用化**（同日追加）：兩個家系圖原有寫死色碼、吃不到主題——拉出共用變數 `--canvas`（畫布底，摻 26% 當前 `--sky-1`，深色摻 12%）與 `--edge`（連線暖褐），`.ft-stage`／`#tree-box`／`.ft-edge`／`.tree-link` 改走變數並刪除各自的深色覆寫；`jptree.js` 世代色帶由寫死 `hsl(22 55% 48%)` 改 `fill: var(--jq-ac)`＋`fill-opacity`，色相隨節氣。標示落點也修正：讓過 fixed header 後改置探頭吉祥物正下方（right 7% 對齊、桌機再左移 14px、字級 28/22px）；文字改**白字＋節氣色光暈**（墨影 `--jq-ink` 保底可讀、光暈 `--jq-ac` 隨節氣換色，淺深模式同一套）
- 驗證：節氣判定 8 個 edge case（年頭回去年冬至、表外年份、雨水 JST 邊界）全過；五語 json key 一致（214 keys）；`/tmp` 全量 build（4042 頁）通過，五語首頁皆有標示殼與字串、CSS 48 條節氣規則、字型進 dist

## 2026-07-19 ・ 網站：園頁標出休園日（日本園 64 座全數）

- 背景：訪客規劃探訪時最需要「哪天別去」，園頁名牌新增 🗓️ 休園日一行
- 資料：`data/zoos.json` 新增**選填欄 `closed_ja`**（照官網原文精簡一行；「年中無休」「不定休（公式カレンダーで告知）」等特殊型照實記），缺值不顯示；內容維持日文原文、不翻譯
- 管線：`export_json.py` 的 `load_zoo_master()` 傳遞 `closed_ja`（zoos_out 帶全部欄位、自動上稿）
- 前端：`Zoo.astro` 名牌 📍 下加一行 `🗓️ {zoo_closed}：{closed_ja}`＋小字註記；五語 i18n 加 `zoo_closed`／`zoo_closed_note`（休園日／闭园日／休園日／Closed／휴원일）
- 67 座日本園逐園查官網（園方或自治體官方頁）：64 座填入、3 座已歇業園（みさき公園、あやめ池、宝塚FL）不填。特殊型照實記：冬季休園（大森山、茶臼山、釧路、富山FP）、營業カレンダー制（那須王国、AWS、東北サファリ、姫セン、ひらパー、市原ぞうの国）、夏冬開園制（旭山）、月別指定制（かみね、桐生が岡）、整修長期休園（甲府遊亀 〜2027-03；野毛山 2027-01-07 起）
- 官方頁 JS 渲染抓不到的 4 座由作者手動複核定案：八景島＝年中無休（確認）、池田＝水曜中心の不定休（営業カレンダー制，修正原搜尋索引值）、到津の森＝火曜（祝日は開園し翌日休）＋年末年始、天王寺＝原值正確＋補臨時開園註記；`website` 一併更新：池田→ikedazoo.jp、福知山→fukuchiyamazoo.jp、天王寺→tennojizoo.jp
- 驗證：export 後 64 園 `closed_ja` 進 `pipeline/data/zoos.json`；`/tmp` 全量 build（4042 頁）通過，五語園頁抽查皆正常、無資料園不顯示該行

## 2026-07-19 ・ 流程：wiki/log.md 按月封存＋repo 清理

- 背景：log.md 已達 5,100+ 行（412KB）且只增不減，每次讀寫都變重；另 `.git` 累積 1,003 個中斷殘留的暫存物件（FUSE 掛載下 git 操作被中斷所致）
- **log 按月封存**：新增 `wiki/log-archive/`（子目錄、glob 非遞迴自動排除，不影響 build/audit），2026-05（49 筆）、2026-06（71 筆）移入 `log-2026-05.md`／`log-2026-06.md`，`log.md` 只留當月起（146 筆）。分桶依**逐筆日期**而非行序（原檔有少數日期交錯）；append 流程不變、封存檔同樣禁 wikilink。換月後擇機搬移（規則已記入 CLAUDE.md）
- **repo 清理**：`.git` 垃圾物件清除＋repack（garbage 2.15MiB→0）；刪根目錄雜物 `test.db`、`test.db-journal`、`Untitled.canvas`、`_tmp_*` 空檔與各處 `.DS_Store`（均本已 ignore）
- **rebuild.sh**：步驟編號修正（[1/3][2/3]→[1/4][2/4]，與實際四步一致）
- 驗證：三檔筆數 49+71+146=266 與原檔一致、日期範圍各自乾淨、bare wikilink 0；`verify.sh` 與 `build_db` 照常通過

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
