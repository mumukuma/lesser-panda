# 網站更新紀錄 Changelog

> 記錄**網站功能**的演進（新功能、改版、修正）。
> 小熊貓**資料**的異動請見 `wiki/log.md`；願望與規劃見 `ROADMAP.md`。
> 新的在最上面。

---

## 2026-08-15 ・官方來源分類器：埼玉県こども動物自然公園 FB

`build_db.py` 的 `OFFICIAL_FB_PAGES` 新增 `saitamazoo`——`facebook.com/saitamazoo` 由官網
`parks.or.jp/sczoo` 頁尾 SNS 連結指向，確認為園方官方專頁，故其貼文可列入個體頁「來源」區塊
並計入 `has_official_source`。首個用例：`kouta-2010-07-02`／`lily-2010-07-10` 的赴智利日期更正。

---

## 2026-08-15 ・ 統計頁性別細分：出生堆疊、歿齡金字塔、新增父獸產仔年齡

維護者點名「出生」與「歿齡」要分性別，順手收掉兩個既有 backlog。全部維持零 client JS。

- **每年出生數 → ♀ 左 ♂ 右金字塔**（與「年齡分布」同讀法：一年一列、年份置中、數字標兩側，
  最近年在最上）。第一版做成 ♀/♂ 堆疊直條，維護者當日改判「難讀」而重做；金字塔式手機
  完全不需橫向捲，先前列的 rtl 捲軸 backlog 也就此了結。性別待確認（全庫 15 筆）不入圖，
  tooltip 逐年拆分＋註腳交代（灰不能當第三類別色——dataviz 驗證器實測 vs ♂ 藍 ΔE 不足）。
  49 列嫌長（維護者同日再裁定）→ 預設只列**近 20 年**，1976–2006 收進原生 `<details>`
  「更早年份（共 n 隻）」，零 JS；兩段共用同一比例尺，展開後長條可直接互比。
- **歿齡分布 → ♀ 左 ♂ 右金字塔**（與「年齡分布」同讀法；2 歲一格、24+ 併格）。樣本 ♀ 206／
  ♂ 233、性別不明 0，不漏。註腳新增兩性中位數：**♀ 13.4 歲 vs ♂ 12.4 歲**——女生中位多活
  整整一歲；「歿齡組成非存活率」的原註腳照舊保留。
- **新增「父獸產仔年齡」**：與母獸並排雙卡（h2 改「產仔年齡」）。694 筆／176 位父獸，
  中位 6.0 歲、最年長 15.1 歲——對照母獸中位 5.1 歲、最年長 13.9 歲，公獸繁殖生涯長約一到兩年。
- i18n 新增 4 key ×5 語（stats_sec_parent_age／stats_sec_sire_age／stats_sire_age_note／
  stats_death_by_sex），check_i18n 現為 5×455。

驗收：6,362 頁 build ✅、check_i18n ✅、closed.test 68 pass ✅；三張新圖（zh 淺色）＋歿齡
金字塔（en 深色）＋手機版截圖皆過。

---

## 2026-08-15 ・「去了小熊星球」暖語＋年度回顧頁 /review/

兩個新東西，措辭一脈相承：在園頁把離別說得溫柔一點，再給全站一個逐年回望的地方。

**動物園頁「去了小熊星球」**（`Zoo.astro`）：在此園過世的孩子，「去了哪」不再只是
`🪽 歿日`，改顯示「去了小熊星球」——對齊首頁紀念日 `today_rainbow` 的既有措辭
（ja「レッサーパンダの星へ」、en「the red panda planet」、ko「레서판다 별나라로」）。

- 完整資料表的 chip ＝「🪽 去了小熊星球」，歿日改為 chip 下方小字（同「在園 n 年」款式），
  資訊不遺失；時間軸 tooltip ＝「🪽 去了小熊星球（歿日）」；圖例「歿於此園」同步換字。
- 無障礙維持事實描述：`aria-label` 仍是「已故」，暖語只是視覺文案；個體頁「逝世」欄位不動。
- i18n：`zoo_tl_died` 改為 `zoo_tl_star`＋`zoo_tl_star_date`（5 語）。

**年度回顧 `/review/`**（新頁，五語）：索引＋每個有事件的年份一頁（現有資料為 1973–2026
共 51 年），全部建置期由 `data.js` 新增的 `REVIEW` 算好、零 client JS。範圍＝**全球**。

- 年頁四格大數字：出生／去了小熊星球／搬家／年底在園頭數（年底頭數同時間軸 pop 原則：
  訖日不詳且非現居只算到起日當年）。
- 🐣 這一年出生的孩子（依園分組、含蘋果籽佔位，chip 同首頁新生樣式）；
  🪐 這一年去了小熊星球的孩子（名字＋日期＋享年＋所在園，享年只在生歿皆完整日期時計）；
  🚚 這一年的搬家（居住史相鄰兩段推得，**含跨國**——比 /moves/ 的日本限定放寬，跨國標 ✈️）；
  ✨ 這一年的小紀錄（最遠搬家、最多寶寶的園、陪伴最久的孩子——有資料才出現）。
- 當年度隨每日 build 更新、標「進行中」；年頁之間有前後年連結。
- 存疑（unverified）個體一律不計，與統計頁同原則。
- 入口：top-level 導覽已滿（2026-08-09 裁定），從首頁「紀念日」卡與 /stats/ 頁尾連入。
- **同日補：先不公開**（維護者裁定 Q3/Q4 再上）——`data.js` 的 `SHOW_REVIEW` 旗標
  （dev 模式＝開、正式 build＝關）同時鎖路由與兩個入口；正式站 6,102 頁不含 /review/、
  無任何連結，`pnpm dev` 可完整預覽。公開時把旗標改 `true` 一行即可。
- i18n 新增 `rv_*` 21 key ×5 語（check_i18n 現為 5×451）。

驗收：6,362 頁 build ✅、check_i18n 5 語 ✅、closed.test 68 pass ✅；
壽山（表格 chip＋小字歿日）、/review/ 索引、2026 年頁（zh 桌機＋手機）、2025 年頁（ja）、
2024 年頁（en 深色）截圖皆過。

---

## 2026-08-15 ・ 文件數字更新：條目破 1,000、jptree 主網近 700

`wiki/index.md` 頁首本日來到 **1,001** 筆，README 等文件仍寫著 2026-07 訂下的「900+」耐放寫法，
一併更新為 **1,000+**（維持「精確數以 `wiki/index.md` 頁首為準」的但書，不寫死實數）。

- `README.md` — 首段條目數 900+ → **1,000+**
- `CLAUDE.md` — 開頭主題敘述、以及五語系段「不必翻 900+ 條目」兩處同步
- `ROADMAP.md` — 已完成清單的「900+ 條目」同步

順帶修掉一個更嚴重的過時數字：README 的日本家系全圖寫「近 450 隻」，那是 `/jptree/` 剛上線時的規模。
**2026-08-14 的祖先線修正**（血緣邊改建在全部個體上、海外祖先不再讓整條祖先線斷掉）讓主網一口氣長大，
依本日重建後的 `pipeline/data/` 實算為 **692 個節點**（其中日本個體 598、繞經海外的祖先 94），
文件改寫為「近 700 隻，含繞經海外的祖先」。

> 註：`data/zoos.json` 的「350+ 座園」仍然準確（現為 353 座），未動。

---

## 2026-08-14 ・ 動物園頁「歷代居住個體」改版：居住時間軸＋在園頭數＋強化資料表

日本各園資料漸齊之後，歷代居住個體只有一張名字＋期間的列表可惜了。本次把該節改成
「時間軸為主、資料表為輔」，全部建置期算好、零 client JS（互動只用 title tooltip 與 CSS）。

**居住時間軸**：一列＝一隻、橫軸＝年份（該園最早有日期的起日那年 → 今年）。

- 顏色沿用全站 `--female`／`--male`（性別不明＝`--ink-soft`）；🐣＝在此出生（＝第一段
  居住史，與「該園出生」同一定義）、🪽＝歿於此園；同一列斷成兩段＝轉出後又回來。
- 起日或訖日不詳的段落用 `mask-image` 淡出漸層表示，不畫實線硬撐；起日不詳時從生日
  （再不行從圖首）淡入。tooltip 一律顯示原始日期字串，看得出精度。
- 上方細條圖＝該園**逐年在園頭數**（每年年底、最後一年＝今天；訖日不詳且非現居只算到
  起日當年，不無限延伸灌水），整座園的興衰與世代交替一眼看完，標題附高峰年。
- 排序由上而下＝舊到新（起日不詳者以訖日、再以生日代位）；與 /japan/ 年度圖同讀向。
- 窄螢幕沿用 /japan/ 的 rtl 捲軸技巧初始停在最右（今天）；名字欄 `position:sticky`
  不會跟著捲走。年份格線每 5 年一條，貼近「今天」線的年份標籤讓位（**以像素計**——
  用百分比在短年距的園會失準，壽山 25 年跨距曾出現 2025 疊「今天」）。
- 「性別不明」灰在淺色底對比不足（色盲檢驗 CVD 分離 pass、對比 WARN），靠下方資料表
  作後備即合規；表格同時是螢幕閱讀器的主要讀法。

**強化資料表**（收進 `<details>`，時間軸畫不出來的園自動展開改當主體）：期間欄加總
在園年數；新增「從哪來／去了哪」兩欄，🐣 在此出生、🪽 歿於此園（含日期）、現居，
來源與去向的園連到對方園頁。排序維持新到舊。

全部段落都沒有可解析起日的園（僅剩 raw 園名的老紀錄）不畫圖、只出表格，自我保護。
i18n 新增 14 key ×5 語（`zoo_tl_*`×11、`zoo_tbl_more`、`th_from`、`th_to`）。

---

## 2026-08-14 ・ /jptree/ 修正：祖先線繞出日本就被切斷（真血親被判「無已知血緣」）

**症狀**：在家系圖上比對 森森（`shin-shin-1992`）與 Franken（`franken-2012-06-11`）——
兩隻其實是曾祖父與曾孫——關係卡卻顯示「無已知血緣（資料範圍內）」。

**成因**：`japanTreeData()` 舊版**先砍掉非日本個體再建血緣邊**：

```js
for (const p of Object.values(pandas)) {
  if (!isJP[p.slug]) continue;              // ← 節點過濾
  for (const m of [p.mother, p.father]) {
    if (m && isJP[m] && pandas[m]) { ... }  // ← 邊也跟著被過濾
```

Franken 之父 Zeyar 只住過 Calgary Zoo（`isJP=false`），於是
`森森 → ポンタ → Zeyar → Franken` 中間兩條邊同時消失。Franken 本人因 2016 年來多摩而留在圖上，
但祖先線斷頭，`jptree.js` 走 `D.edges` 自然找不到共同祖先。
全庫掃描：**4 隻**日本個體有非日本親代（`franken-2012-06-11`／`holly-2016-06-02`／
`homer-2012-06-11`／`ke-song-2017-06-11`），全是「海外出生後輸入日本」的個體。

**修法**：血緣邊改建在**全部個體**上，再取「**日本個體最多**」的連通元件（不是節點最多，
免得挑到與日本無關的純海外大群）。海外個體照樣進圖，節點索引新增第 11 欄 `overseas`，
以中性灰虛線、`opacity:.5` 弱化呈現（聚焦／共同祖先時恢復不透明），圖例新增一列
`ft_overseas`（五語）。

**數字**：畫出 686 節點＝日本 592 ＋ 海外脈絡 94，11 個世代。
介紹文的 `{n}`、`/japan/` 卡片與右上角 `ft_stat` 一律改用新回傳的 `jpCount`（＝592），
維持「隻數只算日本個體」的語意；`{g}` 則是實際畫出的世代數。

**動到**：`web/src/lib/data.js`（`japanTreeData`）、`web/src/components/JpTree.astro`
（介紹文＋圖例＋`.ft-node.os` 樣式）、`web/src/components/Japan.astro`（`treeSize`）、
`web/public/js/jptree.js`（節點 class＋`ft_stat`）、`pipeline/src/i18n/*.json`（`ft_overseas` ×5）。

---

## 2026-08-11 ・ 來源分類器新增第三類：官方但不對外呈現（ISB）

維護者裁定：ISB《International Red Panda Studbook》（Rotterdam Zoo／Diergaarde Blijdorp 編）
**是官方來源、佐證權重很高**，但**不要呈現在網頁上**——原檔 2012 年已由園方下架，
公開可指的只剩 Wayback 快照。原本（2026-08-09）把 `rotterdamzoo.nl` 加進 `OFFICIAL_HOSTS`
之後，該連結會直接出現在 24 筆條目的「來源」區塊，本次修正。

- `tools/build_db.py` 新增 `NON_PUBLIC_HOSTS`（`rotterdamzoo.nl`／`diergaardeblijdorp.nl`）
  與 `is_public_source()`／`split_sources()`：官方來源拆成「可公開展示」與「官方但不公開」兩份。
  Wayback 形式比對**內層 host**，與 `is_official_source` 同一套拆法。
- `tools/schema.sql` 的 `pandas` 新增 `sources_private` 欄；`sources` 欄自此只放可公開展示者。
- `pipeline/scripts/export_json.py`：`sources` 照舊輸出（已不含 ISB），
  **`sources_private` 刻意不匯出**（`pandas.json` 隨網站一起發佈，連結進了 JSON 就等於上站），
  但 `has_official_source` 改取**兩者聯集**——ISB 權重不變，
  僅以 ISB 佐證的 18 筆條目**不會**因此被標成「維護者提供・未經官方佐證」。
- ⚠️ **`rotterdamzoo.nl` 仍留在 `OFFICIAL_HOSTS`**，不可移除：「官方但不公開」與「非官方」
  是兩件事，移除會讓 `audit.py` 把它列為非官方 host、也會讓那 18 筆掉旗標。
- 驗證：重建後 `pipeline/data/pandas.json` 全文 `rotterdamzoo` 出現 **0 次**、`sources_private` 未匯出；
  24 筆 ISB 條目 `has_official_source` 全為 `true`；`tools/verify.sh` 通過（🔴 0）。
- 政策同步寫進 `SCHEMA.md`〈sources 與 extra_sources 的分工〉與 `CLAUDE.md`「官方來源可直接採用」段。

## 2026-08-11 ・ 來源分類器：池田動物園進白名單

- `tools/build_db.py` 的 `OFFICIAL_HOSTS` 新增 `ikedazoo.jp`（池田動物園，岡山市；訃報等公告發於 `/news/`），
  `OFFICIAL_X_ACCOUNTS`／`OFFICIAL_IG_ACCOUNTS` 新增 `love_ikedazoo`（官網頁尾社群連結指向此二帳號）。
- ⚠️ **該園舊訃報會自站上下架**：`陸`（RPF #139）那篇 2024-04-27 發布，2025-01-11 的 Wayback 快照已是 404，
  `/news/` 六頁列表也翻不到；站內搜尋 `?s=` 回空 body、`wp-json` 回 403。故該園的 `sources` 一律走
  Wayback 快照（`_unwrap_wayback` 會遞迴判內層 host 為官方，比照茶臼山與 rotterdamzoo 的做法）。
  查該園個體的可行路徑：X 搜日期區間找官方公告推文 → 拿推文附的 URL 去 Wayback。

## 2026-08-09 ・ 首頁「國際小熊貓日」倒數橫幅

- 首頁數字徽章上方新增倒數橫幅（`Home.astro` 的 `#irpd-banner`）：每年 **8/16 起**顯示
  「距離國際小熊貓日還有 N 天！」（天數放大強調），活動當天（**9 月第三個週六**，2026 年為
  9/19）換「🎉 今天是國際小熊貓日！」，隔天自動收起。
- 樣式融入四季主題：平時底色吃季節變數（`--sky-2`／`--leaf`，夏天＝清爽天空綠），活動當天
  `.is-today` 才切琥珀慶祝色（9 月中站上已入秋、色調相合）；兩側彩色紙屑圓點、右側 logo
  尾巴（左右翻轉、`anim-bob` 時長 3.4s 與 header 的 2.6s 錯開節奏，當天搖快一倍）。
- 比照「新鮮的寶寶」季節區塊的取捨：活動日與顯示區間由 **client 端逐年計算**（`today.js`；
  deploy 無每日 cron，建置期算日期會卡在最後一次 push）；預設 `hidden`、不加 `reveal`、no-JS 不顯示。
- i18n 新增 3 鍵 × 5 語：`home_irpd_countdown`／`home_irpd_today`／`home_irpd_note`
  （副標「每年 9 月第三個週六・今年是 {d}」，日期 client 端代入）。樣式 `.irpd-banner` 在
  `global.css`，慶祝動畫有 reduced-motion 降級。
- **本機日期預覽開關**：localhost 限定，網址帶 `?today=YYYY-MM-DD` 即可假裝是那一天，
  `today.js` 所有依日期的區塊（新寶寶／IRPD 倒數／今日生日／小熊星球）一起吃到；正式站忽略。
  配套：`lang.js` 語系轉址改為保留 query 與 hash（順帶讓正式站的 UTM 參數不再被吃掉）。

## 2026-08-09 ・ `/species/` 氣候段重寫：氣候不是幼獸存活的主導軸

維護者對「幼獸存活取決於出生園氣候」這段一直有疑慮（「現在都有冷氣」），分兩步處理。

**① 查 Princée & Glatston 2016（Zoo Biology 35(2):104–110）到底寫了什麼**

- **摘要支持的**只有質性結論：全球血統書資料顯示出生地氣候明顯影響新生（neonatal/infant）存活，
  該文並自陳是首次檢定「小熊貓怕熱」這個長年假說。
- **查無出處的**：①「繁殖季溫暖潮濕的國家第一年死亡率 36%」——摘要無任何數字、全文付費牆
  （Wiley 403／PubMed CAPTCHA／Semantic Scholar 的 abstract 被出版社抽掉）；
  ②「母獸因熱緊迫而較常離巢」——摘要與所有二手引用皆無此機制；
  ③ neonatal ≠「第一年死亡率」，用詞放大。三者皆已刪除。
- 唯一量化的二手轉述（Animals 13(5):846 稱門檻約為平均氣溫 19 °C）未見一手全文，**刻意不寫入**。

**② 用 ISB 自己重算，維護者的直覺被證實**

新增 `sources/isb-red-panda/first-year-mortality.py`（可重跑）。世代為有確切生日、
生於 2007-12-31 前者，n=2,368。第一年死亡率：

| 出生地區 | 1980s | 1990s | 2000s | 全期 |
|---|---|---|---|---|
| 日本 | 15% | 32% | 26% | **28.1%**（n=544） |
| 北美 | 50% | 47% | 37% | **43.3%**（n=736） |
| 歐洲 | 39% | 38% | 36% | **37.3%**（n=812） |
| 大洋洲 | 35% | 20% | 20% | **26.7%**（n=131） |
| 南非 | — | 30% | 26% | **27.6%**（n=58） |

夏季濕熱的日本、乾熱的澳洲、南非全在 26–28%，**溫帶的北美反而最差**。再切進同一飼育文化內部：
北美南部濕熱 45.2%／中緯度 38.5%／**北方高緯冷涼 54.4%**（2000 年代仍是冷涼組最差 46.7%）；
日本亦同（北日本 40.2% ＞ 西南日本 30.1% ＞ 關東中部 24.3%）。方向與「越熱越糟」相反。
真正動起來的是**年代**（全球 1980s 39.6% → 2000s 32.1%）與**各園做法**。

**③ 但最後沒有把重算結果寫上站**

一度改成「日本 28% vs 北美 43%，所以氣候不是主導軸」，隨即自我否決：跨地區比較會被**死亡登錄完整度**
汙染（登錄最認真的地區看起來最差），這個偏差對該結論是致命的；不受此影響的是**同一飼育文化內部**
那組（北美冷涼園 54.4% vs 南部濕熱 45.2%、北日本 40.2% vs 關東中部 24.3%），但那同樣是未控制的粗切，
不適合寫成面向大眾的斷言。而且「現代園舍有空調涼房」是無來源的機制解釋——正是本輪刪掉
「母獸熱緊迫離巢」的同一種毛病。

最終 `sp_health_p2b` 五語**瘦成純事實**：第一年是最大的關卡，全球平均約三成五，
**且隨年代下降（1980s 近四成 → 2000s 三成出頭）**，能不能撐過去看各園的育幼經驗與飼育做法。
年代趨勢是重算結果中唯一乾淨的一項——同一批園、同一批登錄習慣前後比，不吃跨區漏報偏差。
氣候與熱的部分整個交還給前一段 `sp_health_p2`（成都研究：夏季高溫高濕引發呼吸道與腸道感染），
那裡本來就有一手來源。參考資料仍保留 Princée & Glatston 2016（該頁的參考資料為延伸閱讀性質、非逐句引用）。

**限制（引用時要一起講）**：血統書死亡登錄完整度各地不一，漏報會讓該地看起來較好
（中國 24 筆記到 0% 死亡即為鐵證）；未控制園、胎仔數、母獸經驗與 founder 效應；
園區氣候分組為依城市手工粗分。本站解析度不足以推翻 Princée（該文用園級氣候變數＋模型），
只能說「在地區層級看不到單純的越熱越糟」。
---

## 2026-08-09 ・ `/species/` 補三處內容：氣候×幼獸存活、EEP 數字、兩物種說的保育意涵

查證「喜馬拉雅亞種存活率比中華亞種低」這個說法時翻出的文獻，**該說法查無來源**（詳見下方「不採用」），
但過程中撈到兩篇可用的，補進物種介紹頁：

- **「換毛與健康」新增一段**（`sp_health_p2b`）：圈養幼獸的存活與**出生園所在地的氣候**高度相關——
  繁殖季高溫多濕的國家第一年死亡率達 **36%**，推測是母獸熱緊迫而離巢（Princée & Glatston 2016，
  分析全球血統書）。接在既有「夏季高溫高濕引發感染」那段之後，正好補上因果的另一半。
- **「保育現況」新增一段**（`sp_consv_p4`）：域外保種本來只有抽象敘述，補上 EEP 的實際軌跡——
  1979 年國際血統書成立時繁殖不佳、1985 年 EEP 啟動後隨飼育技術改良才穩定成長，
  **2019 年底 407 隻／182 家機構**（Kappelhof & Weerman 2020）。
- **「一種還是兩種？」補一句**（`sp_two_p3`）：主張兩物種的同一批學者指出，若成立兩個物種，
  兩者的**受脅程度必須分別評估**——讓分類爭議連上實際的保育意涵，而不只是懸而未決的命名之爭。
- 參考資料加兩筆（Zoo Biology 2016、International Zoo Yearbook 2020）；五語 i18n 各加 2 key，總數 353。

**刻意不採用**：Delaski et al. 2015（北美死亡回顧）確實有「亞種 × 死亡年齡」的顯著關聯
（AFF 新生死亡佔比 44.9%、AFS 高齡佔 43.6%），但那是**死亡個體的年齡組成**、不是存活率——
生得多的族群本來就會產生較多新生死亡，且未控制園區氣候（正是 Princée 找到的主因）。
拿來寫「喜馬拉雅存活率較低」是誤讀，故不寫。

---

## 2026-08-09 ・ `/japan/` 加「族群變化」：逐年出生・死亡・在園頭數與年齡結構

維護者原本問「日本的出生死亡年紀逐年怎麼變」。我第一版判斷 2023–2025 出生（2／2／5 隻）
是收錄斷點、做了一份 67 筆的「待補清單」——**維護者指出那是事實**：日本的繁殖由 JAZA 集中
管理，園內有育齡雌雄不等於會配對繁殖，清單的判定前提因此不成立，已作廢。曲線是真的。

- **資料層** `JP_TREND`（data.js，建置期算）：1996–今年逐年的日本出生數、在日本園內的死亡數、
  **年底**仍住在日本園的頭數（含年齡中位數與 12 歲以上占比）。當年度未結束者算到今天並標記。
  只有年份、無月日的歿日無法定位在某一天，故不計入存量（計死亡數時仍以年份計）。
- **兩張純 CSS 圖**：①「每年出生與死亡」上下發散長條，上下**共用同一個像素比例**才能直接比高度；
  ②「年底在園頭數與年齡結構」堆疊長條（下＝未滿 12 歲、上＝12 歲以上），一張圖同時看到族群
  大小與高齡化。窄螢幕橫向捲，容器用 `direction:rtl`（內層轉回 ltr）讓初始位置停在**最右端**，
  手機一打開看到的就是最近幾年，不必先滑。
- **看到的事**：在園頭數 2020 年 275 隻的高點 → 現在 230 隻；年齡中位數 2016 年 5.5 歲 → 11.1 歲；
  12 歲以上比例 16% → 44%；出生 2013 年 30 隻 → 2023、2024 各 2 隻。
- **⚠️ 死亡數天生偏低**寫進頁尾：夭折幼獸園方多半不公布，日本個體中死於一歲前的紀錄僅個位數
  （298 筆完整生歿裡 4 筆），故頁面用語一律是「已長大的個體」，不寫成壽命或幼獸存活率。
- **12 歲這條分界線的依據**（維護者問「為什麼是 12 歲」後補上頁內說明 `jp_why_12`）：不是隨手挑的，
  是用自家資料驗出來的**繁殖生涯實質終點**——日本出生紀錄中母獸生產年齡中位數 5 歲，滿 12 歲之後
  才生下的只佔 **1%**（父獸 4%，n=482／451）。所以深色那截＝幾乎不會再有寶寶、但活到 1 歲以上者
  12 歲後仍有中位 5.4 年可活的個體。`JP_TREND.senior` 建置期算，資料長大會自己更新。
- **「柱子變矮、紅色變厚」那句**（`jp_trend_shape`，維護者指定加入）：總數的變化會蓋掉真相——
  2020 年高點至今總數只少 45 隻，卻是未滿 12 歲**少了 86 隻**、12 歲以上**反而多了 41 隻**相抵的結果。
  ⚠️ 這句話綁在目前的形狀上，資料長大有可能反轉，故加 `showShape` 條件（總數減少 ∧ 年輕減少 ∧
  高齡增加）三者皆成立才渲染，不成立就整句不出現，避免哪天變成錯誤敘述。
- ⚠️ 同一句裡出現兩次的佔位符要用 `replaceAll`——`{age}` 用 `.replace` 只換掉第一個，頁面會露出 `{age}`。
- **與物種介紹頁雙向互連**（維護者提議）：`/japan/` 的「為什麼切在 12 歲」連到〈繁殖與寶寶〉
  `#breeding`、死亡但書連到〈換毛與健康〉`#health`——後者正好補上本站缺的那塊：文獻裡
  未滿 30 天的新生兒佔全部死亡四成、成都研究七成幼獸死於頭 15 天，說明「為什麼 wiki 幾乎
  看不到夭折」。反向 `/species/` 保育段新增 `sp_consv_p5`：歐洲 EEP 從 1979 年的不穩定到
  2019 年 407 隻／182 機構是成長的樣本，日本則是同一套域外保種**相反方向**的樣本，連到
  `/japan/` 族群變化。`Species.astro` 補 `#health`／`#conservation` 錨點、`link()` 加 `{japan}`。
- 連結文字一律重用對方的節標題 i18n key（`sp_breed_title`／`sp_health_title`／`jp_sec_trend`），
  五語不必再翻一份標籤；中文正本 `red-panda-intro.md` 已同步新增該段。
- **`/japan/` 加「亞種分布」＋與 `#fulgens` 互連**（維護者指定）：現居日本 230 隻中中華小熊貓 222、
  喜馬拉雅小熊貓 **8 隻且全部在熱川バナナワニ園一處**。比例條＋兩句話，亞種名連 `/species/` 的
  `#styani`／`#fulgens`，園名連園頁；反向 `sp_fulgens_p3` 從指名亞種段連到 `/japan/#subspecies`。
  ⚠️ 措辭跟著資料走：只有在 `fulgensZoos.length === 1` 時才敢說「日本唯一看得到的地方」，
  分散到多園會自動改用列表版（`jp_sub_many`），不寫死。`JP_SUMMARY` 增 `species`／`fulgensZoos`。
- 版面順序調整：亞種分布放在摘要數字之後、「日本專屬視圖」之前（先講「這裡住的是誰」再給入口與趨勢），
  順帶讓從 `/species/#fulgens` 過來的錨點落在頁面中段而不是被頂到頁尾。
- `pipeline/src/i18n/*.json` 五語各加 19 key，總數 372。

---

## 2026-08-09 ・ 導覽列收成「日本」群組＋新落地頁 `/japan/`

加了 `/moves/` 之後導覽列有 7 項，**已經擠到站名換行**（量測：header 內層固定 `max-w-4xl`＝896px，
nav 佔 632px，英文站名被壓成 3 行、日文 2 行）。把兩個「只涵蓋日本」的頁收進群組：

- **`/japan/` 落地頁**（`Japan.astro`，五語）：日本總覽四格（收錄 589／現存 230／動物園 67／
  園間移動 451）＋家系圖與搬園紀錄兩張卡。**群組父項本身是連結**，手機與觸控裝置沒有 hover，
  點下去一定要落到有內容的一頁。日本專屬數字（如 61 座園有現居個體）本來無處可放，現在有家。
- **導覽列**改為 6 項：首頁／圖鑑搜尋／動物園地圖／統計／物種介紹／**日本 ▾**（日本群組放最後、緊鄰語言切換）。`nav` 陣列第三個
  元素存在即視為群組。桌機以 `:hover` ＋ `:focus-within` 純 CSS 展開浮層（鍵盤 Tab 到父項即展開，
  Esc 由 nav.js 把焦點移出）；手機不浮出，子項以左側細線縮排直接列在群組下方——手機清單是置中的，
  光靠 padding-left 看不出階層。站在 `/jptree/`／`/moves/` 時父項也顯示 active。
- 量測結果：nav 632→499px（en），站名 en 3 行→2 行、ja 2 行→1 行，zh／ko 無變化。
- **命名決策**：不用「日本統計」——會與既有的全站「統計」在同一列撞名，且家系圖不是統計。
  站上 [[ui-region-not-country]] 的「用地區不用國家」是針對**分類器標籤**，此處「日本」是
  資料範圍不是分類器，故不衝突；日後若出現「中國」「北美」群組要再議。
- `pipeline/src/i18n/*.json` 五語各加 11 key（`nav_japan`＋`jp_*`），總數 351。

---

## 2026-08-09 ・ 新頁 `/moves/`：搬園紀錄（園間移動統計）

日本國內的「園間移動」是既有居住史裡一直沒被用過的一塊資料。新增 `/moves/` 五語頁：

- **資料層** `web/src/lib/data.js` 新增 `MOVES`（建置期算完、零客戶端 JS）：由每隻個體
  居住史的**相鄰兩段**推得一次移動，只計起訖園皆為 Japan 且皆有 `zoo_id` 者，存疑個體不列入
  → 451 筆移動、326 對園、66 座園；距離用 haversine 直線距離（中位 298 km、累計 182,318 km）。
- **頁面** `Moves.astro` 六節：① 摘要四格 ② 搬家季 vs 出生季（兩序列**各自**以自身最大值
  正規化——出生 270／搬家 80 量級差三倍，共用刻度會把搬家壓成一條線）③ 交流最頻繁的園對
  ④ 送出／接收（左右分流長條）⑤「相親」成功率 ⑥ 距離紀錄＋首次搬家年齡。
- **發現**：搬家集中 3 月（80 次）、8 月僅 4 次，出生則 100% 落在 5–9 月且六七月佔 95%
  ——兩季完全互補。搬家後三年內在新園生下寶寶者 140／427＝33%。首次搬家年齡中位 2.5 歲
  （呼應物種介紹頁「約 18 個月性成熟」）。
- 導覽列新增「搬園紀錄」（統計之後、物種介紹之前）；`Species.astro` 繁殖節加 `id="breeding"`
  供本頁深連結。`pipeline/src/i18n/*.json` 五語各加 31 key（`mv_*`＋`nav_moves`），總數 340。
- 統計基準寫在頁尾：月份／年齡／成功率只採日期完整（年月日）的移動（427／451）。
- 🐛 同日修正手機版跑版：「距離紀錄」兩張卡是 grid item、預設 `min-width:auto`，內含 `truncate`
  （`white-space:nowrap`）的路線行會把格子撐開，整頁橫向溢出 135–151px（四語皆中）。卡片補
  `min-w-0`；路線行改成手機換行、桌機才 `sm:truncate`（截掉一半目的地園名等於資訊消失），
  日期加 `whitespace-nowrap` 免得斷在半途。已驗 320／360／390／414／640px × 五語皆無溢出。
- 🐛 順手修兩個既有的窄螢幕溢出：`/jptree/` 的園別 `select` 內建寬度跟著最長 option 走
  （英／韓園名 466px），320px 溢出 162px → `.ft-tools select` 加 `max-width:100%; min-width:0`；
  `/stats/` 長壽排行與子女數排行的並排卡與上面同一個 grid item `min-width:auto` 問題 → 補 `min-w-0`。
  （已知未修：`/pandas/` 篩選列在 640px 寬會溢出 47–134px，成因是園別／地區 `select` 帶 `sm:flex-none`、
  寬度跟著最長 option 撐開；要修得替下拉設寬度上限，會動到桌機工具列外觀，待維護者決定。）

---

## 2026-08-08 ・ 致謝頁升級為「關於本站」＋首頁短版宣言小卡

維護者提供本站宣言（非營利同好專案、把喜歡化成對真實小熊貓的關注），經潤飾後：

- `/thanks/` 頁升級：上半新增「關於本站」兩段宣言（i18n `about_p1`／`about_p2`），
  下半保留貢獻者致謝名單（原內容不動）；頁標題與 `<title>` 改用 `about_title`。
  **URL 維持 /thanks/ 不變**，不另開新頁。
- 首頁最下方新增短版小卡（`home_about_text`）＋「關於本站 →」連結到 /thanks/。
- footer 連結文字 `thanks_footer_link` 五語改為「關於本站與致謝」系（About & Thanks…）。
- `pipeline/src/i18n/*.json`：五語各加 4 key（`about_title`／`about_p1`／`about_p2`／
  `home_about_text`）＋改 1 值，總數 309。
- 位置決策記錄：刻意**不放物種介紹頁**（科普正文與站務宣言分離）、不新開 /about/（內容
  單薄且 footer 已有入口）。

---

## 2026-08-08 ・ 物種介紹頁再擴充：「換毛與健康」節＋FAQ 第五題

`/species/` 頁新增「換毛與健康」一節（維護者提議加換毛與死因科普）：

- **換毛**：春季換毛約 4 月起、6 月初穩定，從臉頰／額頭／尾根開始掉、外觀變瘦變邋遢
  ——依桐生が岡動物園官方專文〈レッサーパンダの換毛事情〉（該園已在官方來源白名單）。
  另加 FAQ 第五題「夏天怎麼毛稀稀疏疏」對應遊客常見誤會。
- **死因**：幼獸關卡（北美 366 例解剖統計：<30 天新生兒佔全部死亡 40%；成都研究近七成幼獸
  死於頭 15 天、夏季高溫高濕引發感染）；成體／高齡以心血管疾病最常見、次為腎臟與消化道
  ——與園方訃報常見「心臓疾患」「腎不全」互相印證；犬瘟熱幾乎絕症、含 1976 活毒疫苗致死
  案例（動物園用死毒／重組疫苗），呼應保育節的流浪犬威脅。
- 壓力掉毛刻意不寫：文獻僅個案且原因常不明（Captive Red Panda Medicine 章節），科普頁不採。
- `pipeline/src/i18n/*.json`：五語各加 7 key（`sp_health_*`＋`sp_faq_q5/a5`），總數 302；
  正本 `red-panda-intro.md` 同步；參考資料補桐生換毛文、JZWM 2015、BMC Vet Res 2022、
  JAVMA 1976 四筆。

---

## 2026-08-08 ・ 物種頁內容更新：換毛用詞、腸套疊、甜味 FAQ

- 換毛 FAQ 用詞：「又瘦又邋遢」→「又瘦又潦草」（維護者指定；zh-TW／zh-CN 與正本）。
- 「換毛與健康」死因段補**急性消化道疾患**：胃擴張扭轉（GDV）有獸醫期刊病例報告（*Veterinary Surgery* 2014）；腸套疊（腸重積）查無小熊貓專屬論文（PubMed 0 筆），以**園方官方訃報**為據——天王寺動物園メル（2025-04-06，「腸重積に伴う循環不全」）。
- 新增 FAQ「小熊貓喜歡吃什麼？聽說牠們嚐得出甜味？」：主食竹＋動物園蘋果零食；甜味受體 *Tas1r2* 功能完整、行為測試偏好天然糖與阿斯巴甜等人工甜味劑（受測食肉目唯一），佐證 Li & Glaser et al. (2009) *J Hered* 100(S1):S90–S100。
- 五語 i18n 同步（sp_faq_q6/a6 新 key、sp_health_p3 追加）；參考資料清單＋3 筆；中文正本 `red-panda-intro.md` 同步。

## 2026-08-08 ・ 統計頁新增「物種」區塊（連結物種介紹頁）

- `/stats/` 摘要徽章下方新增「物種」卡片：中華（styani）／喜馬拉雅（fulgens）占比條（主題色 rust／amber，深色模式自動成立、零 JS），兩個亞種名稱直連 `/species/#styani`／`#fulgens`（與個體頁「物種」欄同一連結慣例），另有「亞種不詳 N 隻」與「物種介紹 →」入口。
- i18n 新增 `stats_species_unknown`（五語）；`check_i18n.py` 加測 U+FFFD 替換字元（mojibake 偵測）。

## 2026-08-08 ・ 驗證進 CI＋index.md 自動對帳（架構補強）

- **CI 驗證關卡**：`deploy.yml` 建置前新增 gate——`tools/verify.sh`（audit --strict＋check_twins）、新工具 `tools/check_i18n.py`（五語 i18n key 一致性：缺 key／多 key／重複 key／空值即擋）、`node web/tests/closed.test.mjs`。未通過即不部署；本機沒裝 pre-push hook 或 `--no-verify` 繞過時，壞資料仍會被擋在上線前。
- **index.md 對帳**：`audit.py` 新增整合性檢查（🔴、--strict 擋）——index 的 wikilink 必須都對應存在的條目、每個條目至少列入 index 一次、頁首「條目總數」須等於實際檔數。同條目跨家族表重複出現屬正常、不檢查唯一性。

## 2026-08-08 ・ 已故標記統一為 🪽（wiki 正本跟進網站）

- 依維護者裁定，已故標記全面統一用翅膀：wiki 正本（標題／引言／index／內文家族段，含 `_hidden/` 與 `log-archive/`）🪐 → 🪽，共 732 檔 7,976 處，與網站顯示（2026-07-19 起 🪽）一致。
- 工具同步：`tools/query.py` CLI 輸出改 🪽；`tools/zoo_registry.py` 的註記過濾清單加入 🪽。
- 首頁「今日前往小熊星球」（i18n `today_rainbow`）維持 🪐 星球意象，不在此次範圍。

## 2026-08-08 ・ 專案文件盤點更新（過時資訊修正）

- README／CLAUDE.md／ROADMAP／SCHEMA：條目數改「900+」耐放寫法、註冊表 350+ 座園、五語字串、補物種介紹頁與照片與影片等新功能描述；ROADMAP 補記 7/20 後完成項。
- `rpf-wiki-SKILL.md` 大修：slug 改為現行「名字-生日」規則（撞名用媽媽名）、性別改讀 RPF 性別 icon（嚴禁從子女反推）、RPF 降為線索、居住史表格由 gen_residence 自動生成。
- `report-intake-SKILL.md`：gen_residence 舊行為描述更正（frontmatter `zoos:` 為唯一來源）。
- docs：批次 1–4 SOP 與 Tally 藍圖補「三語表已合併」現況與 audit 預設不比對 lineage；三份歷史計劃（資料校訂、回報校正、中國個體放寬）補「已實作／已覆蓋」狀態註記。

## 2026-08-08 ・ 物種介紹頁擴充：繁殖與寶寶／保育現況／FAQ 三節

`/species/` 頁（昨日上線）續作，對應 `docs/red-panda-intro-PLAN.md` 的 P2 部分範圍＋計劃外的 FAQ：

- **繁殖與寶寶**：季節性繁殖（北半球 1–3 月交配、5–7 月出生）、延遲著床（懷孕紀錄 93–156 天，
  依 Smithsonian National Zoo）、一胎 1–4 隻以雙胞胎最常見、幼獸成長時程、壽命。段落內嵌站內
  連結呼應既有功能：家系圖雙胞胎標記、統計頁「長壽排行」「每年出生數」、首頁「新鮮的寶寶」
  季節窗——i18n 字串用 `{tree}`/`{longevity}`/`{newborns}`/`{stats}` placeholder，
  `Species.astro` 建置時替換成 `pageUrl` 連結、連結文字重用既有 key（各語不必再翻標籤）。
- **保育現況**：IUCN 瀕危與族群數字（減幅寫 40–50%，Smithsonian 40% vs RPN 50% 取區間）、
  CITES 附錄一、三大威脅＋犬瘟熱、保育作為（棲地／社區型／域外保種與血統書配對，
  點出本圖鑑居住史與家系即其縮影）。
- **FAQ** 四題：能不能養（不行）、與浣熊的關係、Firefox 名字由來、會不會冬眠（不會）。
- `pipeline/src/i18n/*.json`：五語各加 19 個 key（`sp_breed_*`／`sp_consv_*`／`sp_faq_*`），
  總數 295；正本 `red-panda-intro.md` 同步加三節；參考資料補 Smithsonian National Zoo。
---

## 2026-08-07 ・ 新頁面「物種介紹」（/species/）＋個體頁物種欄連結

新增全站第一個敘述型頁面：介紹「什麼是小熊貓」與兩個亞種（喜馬拉雅小熊貓 *Ailurus fulgens
fulgens*／中華小熊貓 *Ailurus fulgens styani*）怎麼分，含快速分辨比較表與精簡參考文獻
（Hu et al. 2020、Glatston 2021、IUCN、RPN）。範圍為 `docs/red-panda-intro-PLAN.md` 的 P1；
分界河流已查證：2020 全基因體研究將兩者分界由怒江修正為雅魯藏布江。

- 中文正本：repo 根目錄 `red-panda-intro.md`（不放 `wiki/`，避免被管線當個體條目解析）。
- `web/src/components/Species.astro`：新元件，`#fulgens`／`#styani` 段落錨點（scroll-mt 配合
  浮動 header）；學名與文獻連結為語系無關常數，其餘內容全走 i18n。
- `pipeline/src/i18n/*.json`：五語各加 32 個 `sp_*` key＋`nav_species`（zh-TW 正本、zh-CN 大陸
  用語手譯、ja／en／ko 翻譯）；段落含斜體學名者存 `<i>` 標記、以 `set:html` 渲染（比照
  `footer_note` 慣例）。印度分布刻意只寫「錫金、西孟加拉一帶」。
- `web/src/pages/[...path].astro`：新 kind `species`（五語 ×1 路由）；`Layout.astro` 導覽列
  加「物種介紹」（置於統計之後）。
- `web/src/components/Panda.astro`：`speciesCell` 的亞種俗名改為連結 → `/species/#<亞種>`，
  個體頁可一鍵查兩亞種差別；亞種不詳（顯示「-」）與俗名缺 key（純學名）情形不變。
- 圖鑑立場不變：仍採亞種寫法（`species` 欄值域 `fulgens`／`styani`），兩物種說（*A. styani*）
  於頁內說明；用詞照 `SCHEMA.md`「中華小熊貓」。

---

## 2026-08-07 ・ 官方來源白名單新增三座美國園＋兩個官方 IG；註冊表補八園地點

處理兩筆「圖鑑缺漏」回報（Doofah × Sisu 一家）時查證到的官方管道，`tools/build_db.py` 補上：

- `OFFICIAL_HOSTS`：`potterparkzoo.org`（抵園・出生公告發於官網新聞稿）、`potawatomizoo.org`、
  `rosamondgiffordzoo.org`（含 `www.` 一筆，host 為完全比對）。
- `OFFICIAL_IG_ACCOUNTS`：`zooknoxville`（同 zooknoxville.org；抵園・出産公告發於此，本次以瀏覽器實讀
  2021-03 Doofa 抵園、2025-09 Sisu 兩則）、`potawatomizoo`（同 potawatomizoo.org；生日・送別公告發於此）。

另補 `data/zoos.json` 的地點欄（原為 null，個體頁居住史表格因此只顯示「美國 🇺🇸」）：Charles Paddock、
Fort Wayne Children's、Hamilton、Memphis、Potawatomi、Potter Park、Rosamond Gifford、Sunset 八園補
`location_ja`＋`location_zh`，セントラルパーク動物園補 `location_zh`。重跑 `gen_residence.py` 後
另有 9 個既有條目的居住史表格順帶補上地點（willa、itsuki、nima 等）。

相關資料異動見 `wiki/log.md` 2026-08-07 一筆。

---

## 2026-08-06 ・ 官方來源白名單新增兩座園（Columbus Zoo、Zoo sauvage de Saint-Félicien）

處理讀者回報時查證到兩座園的官方公告管道，`tools/build_db.py` 的官方來源分類器補上：

- `OFFICIAL_HOSTS`：`columbuszoo.org`（出生・命名公告發於官網 /news/）、`zoosauvage.org`。
- `OFFICIAL_FB_PAGES`：`columbuszoo`（官網頁尾 Facebook 連結指向此專頁，實測確認）。
- `OFFICIAL_IG_ACCOUNTS`：`columbuszoo`（同上，官網頁尾 Instagram 連結）、`zoosauvageofficiel`
  （Zoo sauvage de Saint-Félicien；貼文內文連回 `zoosauvage.org/evenements/`，到園與個體介紹公告發於此。
  ⚠️ 官網頁尾未實際核對——沙盒 web_fetch 回 520、Chrome 該網域未授權；日後有機會請補驗）。

相關資料異動見 `wiki/log.md` 2026-08-06 一筆。

---

## 2026-08-05 ・ 個體頁「照片」改版為「照片與影片」分頁（IG＋YouTube）

個體頁照片區塊新增 YouTube 影片支援，改為分頁設計：第一分頁 Instagram（預設、內容照舊），
第二分頁 YouTube。資料來源為 frontmatter 新選填欄位 `youtube:`（格式同 `instagram:`——
「URL 日期」、新到舊排序；規範與 `extra_sources` 的分工見 `SCHEMA.md`）。首例個體為
`qiu-qiu-kaohsiung`（壽山球球，0 IG＋2 YT）。

- `tools/schema.sql`／`tools/build_db.py`／`pipeline/scripts/export_json.py`：pandas 表新增
  `youtube` 欄（JSON array），frontmatter → DB → `pandas.json` 全線比照 `instagram`；
  行末 YAML 註解（自製 parser 不剝）於 build 時去除，只存「URL 日期」。
- `web/src/components/Panda.astro`：
  - 分頁列只在**兩種來源都有**時顯示（九成以上條目只有 IG，避免多一層無意義 UI）；
    只有一種來源時照舊顯示單一區塊。IG 空而 YT 非空 → 直接顯示影片分頁（球球即此例）。
  - YouTube 採 facade：開頁只放官方縮圖（`i.ytimg.com`，免 API key）＋播放鍵，點擊才載入
    `youtube-nocookie.com` 播放器（16:9 grid，autoplay）。與 IG 骨架卡同哲學，開頁零 iframe。
  - 切回 IG 分頁時觸發 `resize`（比照 `refit()`）——IG embed 在 `hidden` 期間量不到寬度，
    不重算會壓扁。URL 支援 watch／youtu.be／shorts／live 形式，統一解析 video ID。
  - hero 照片 chip 與區塊標題數字改為 IG＋YT 合計。
- `web/src/lib/data.js`：搜尋頁 `ph`（「只顯示有照片／影片」篩選、排序、卡片 badge）改為
  IG＋YT 合計——球球這類只有影片的個體也能被篩出。
- i18n 五語系：`sec_photos` 改「照片與影片」，新增 `videos_note`（YT 版權說明）、`videos_play`、
  `tab_instagram`／`tab_youtube`；`filter_has_photos`／`sort_photos` 措辭同步改。

---

## 2026-08-05 ・ 來源分類器：補 Prospect Park Zoo 官方 IG 帳號

處理 `leah-2019-05-17` 的原名回報時，佐證雙胞胎 `Rose` 現居紐約布魯克林的一手來源是該園官方
IG 影片（2022-11，影片以 Rose 之名介紹園內小熊貓）。

- `tools/build_db.py`：`OFFICIAL_IG_ACCOUNTS` 新增 `prospectparkzoo`。佐證＝官網
  `prospectparkzoo.com` 頁尾 Instagram 連結指向此帳號。
- 影響：更名後的 `rose-2019-05-17` 個體頁「來源」區塊顯示該 IG 貼文（判為官方）。
  資料異動詳見 `wiki/log.md`。

---

## 2026-08-05 ・ 來源分類器：補 Cincinnati Zoo 官方網域與官方社群帳號

處理 `linus-2018-06-23` 家系回報時發現，辛辛那提動物園（全球中華小熊貓亞種繁殖數第一、
wiki 內已有 Rover／Bailey／Harold／Kelly／Hazel／Lin／Kora／Linus 等 8 筆以上出身個體）
的官方管道完全不在白名單，導致該園所有官方來源都被判為非官方。

- `tools/build_db.py`：
  - `OFFICIAL_HOSTS` 新增 `cincinnatizoo.org`（園方官網；出生・命名・訃告公告皆發於此，
    如 `/remembering-red-panda-lin/`、`/red-panda-cubs-born-at-cincinnati-zoo/`）。
  - `OFFICIAL_X_ACCOUNTS` 新增 `cincinnatizoo`（官方 X；2018 年 Linus・Kora 幼獸期的家系資訊
    只發在 X，官網未另發稿）。
  - `OFFICIAL_FB_PAGES` 新增 `cincinnatizoo`（官方 FB 專頁，同園同名）。
- 影響：`lin-2013-06-16`、`kora-2018-06-23`、`linus-2018-06-23`、`kola-2015-08-24` 四筆的
  `has_official_source` 轉為 true，個體頁「來源」區塊改為顯示園方連結、
  移除「未經官方佐證」標記。資料異動詳見 `wiki/log.md`。

⚠️ 順帶記錄一項工具面事實：`x.com` 在沙盒 `web_fetch` 回 `ROBOTS_DISALLOWED`、抓不到內容，
但 **Claude in Chrome（`navigate` + `get_page_text`）讀得到貼文全文、發文帳號與精確發文時間**，
核對回報所附的 X 來源可走這條路，不必再擱置待維護者告知。

---

## 2026-08-05 ・ `extra_sources` 只放 URL；純文字佐證改寫進條目備注

維護者裁定：個體頁的「其他參考資料」區塊**只呈現可點的連結**，純文字說明不顯示。

- `web/src/components/Panda.astro`：`extraSources` 加 `.filter()` 只留 `http(s)://` 開頭者，
  移除原本「非 URL 就原樣顯示為純文字」的分支（舊資料誤填也不會被渲染）。
- `SCHEMA.md`：frontmatter 範例與〈sources 與 extra_sources 的分工〉表格改寫——
  `extra_sources` 只列 URL；無法線上核對的一手佐證（讀者實拍展牌、實體園報掃描、園內公告牌）
  改寫在條目內文／`## 備注`（可引述展牌原文），`sources` 記 `維護者提供（YYYY-MM-DD：…）`。
- `CLAUDE.md`：〈非官方連結一律留存為「其他參考資料」〉一段補上此覆蓋規則。
- 既有資料清理：6 個條目的純文字 `extra_sources` 項目移除
  （`hajime-1991-07-27`、`ouji-kobe`、`pei-pei`、`mi-duo-dalian`、`nuo-mi-dalian`、`xi-ning-dalian`；
  後四者移除後 `extra_sources` 已空、整個欄位一併刪除）。**內容無遺失**——這 6 筆的說明原本就都已
  寫在各自的內文或備注段（如 `ouji-kobe` 備注已完整引述剥製展示解說牌原文）。

---

## 2026-08-05 ・ 來源分類器：補官方網域 `kagoshima-hiroba.jp`

- `tools/build_db.py`：`OFFICIAL_HOSTS` 新增 `kagoshima-hiroba.jp`。該站為**鹿児島市広報課**的
  「鹿児島市広報デジタルアーカイブ」，封存廣報紙《かごしま市民のひろば》《市民フォト鹿児島》的官方 PDF
  （站台自述見 <http://kagoshima-hiroba.jp/>，鹿児島市官網 `city.kagoshima.lg.jp/shise/koho/hiroba/` 亦以此為廣報紙頁）。
  因網域非 `.lg.jp`，不會被既有的自治體 pattern 涵蓋，故個別列入。
- 用途：平川動物公園初代小熊貓（紅紅・咪咪）條目引用《かごしま市民のひろば》2012 年 3 月號
  「平川動物公園のあゆみ」年表（載「昭和63年7月 中国・長沙市からレッサーパンダ来園」）作為官方來源。

---

## 2026-08-05 ・ 來源分類器：補 IG 官方帳號 `assiniboineparkzoo`

- `tools/build_db.py`：`OFFICIAL_IG_ACCOUNTS` 新增 `assiniboineparkzoo`。佐證＝官網
  `assiniboinepark.ca/zoo` 頁尾「Follow us」的 Instagram 連結指向此帳號（同 `facebook.com/assiniboineparkzoo`），
  比照 `kiryuzoo`／`hertfordshirezoo` 的認列標準。
- 觸發原因：Assiniboine Park Zoo 2026-06-08 出生的小熊貓寶寶，園方**只在 IG 公告**
  （官網 `/stories/` 與 `/media/` 都沒有這則），該貼文是唯一的一手來源；不列白名單就無法在個體頁「來源」區塊顯示。
- 新聞轉載（Classic107／CHVN／CTV Winnipeg）照舊放 `extra_sources`，不入白名單。

## 2026-08-04 ・ 來源分類器：補 `assiniboinepark.ca`

- `tools/build_db.py`：把 Assiniboine Park Conservancy 官網 `assiniboinepark.ca` 列入 `OFFICIAL_HOSTS`
  （該站 `/stories/` 為 Assiniboine Park Zoo 園方一手公告，比照既有的 `torontozoo.com`／`gvzoo.com`）。
  觸發原因：處理 2026-08-04 社群回報時以該站兩篇公告佐證 `suva`・`kelly`・`mei-mei` 的居住史，
  audit 報「sources 有非官方 host」。新聞媒體轉載（Classic 107）不入白名單、改放 `extra_sources`。

## 2026-08-03 ・ 來源分類器：補非日本園白名單，並讓 `audit.py` 自動抓漏

2026-08-02 那次盤點只掃了日本個體，**非日本園同樣有漏**——建 `dusk-2004-06-02` 時發現 Calgary Zoo 官方訃告
沒顯示在個體頁，查出 `calgaryzoo.com` 根本不在 `OFFICIAL_HOSTS`（諷刺的是其 FB 專頁 `thecalgaryzoo` 早就在
`OFFICIAL_FB_PAGES`，同一家園三個管道只認一個）。

- **`OFFICIAL_HOSTS`** 補 `calgaryzoo.com`、`zooknoxville.org`、`mandai.com`（新加坡動物園營運方）、
  `grandpark.seoul.go.kr`（首爾大公園；`.go.kr` 不在 gov pattern 內）、`oceanpark.com.hk` 與
  `corporate.oceanpark.com.hk`。⚠️ host 是**完全比對**，子網域要各自列一筆。
- **`OFFICIAL_IG_ACCOUNTS`** 補 `calgaryzoo`／`thecalgaryzoo`（兩帳號皆官方）、`edmontonvalleyzoo`、`safariniagara`。
- 追加 `buildingourzoo.com`＝Valley Zoo Development Society，Edmonton Valley Zoo 的官方支援團體
  （動物資訊由園方提供、以第一人稱發布），比照 Calgary 的 Wilder Institute 認列官方。
- **`OFFICIAL_FB_PAGES`** 補 `oceanparkhk`（香港海洋公園官方專頁）。同時把 `li-zi-2008-06-15` 的
  `?fbid=` 形式網址改存含 vanity 的 `facebook.com/oceanparkhk/photos/<fbid>`——兩種形式指向同一則貼文，
  但只有後者帶得出專頁識別、分類器才認得。**日後存 FB source 一律用含 vanity 的形式。**
- 影響 **11 筆條目**恢復顯示官方來源、`has_official_source` 由 false 轉 true：`dusk-2004-06-02`、
  `udaya-2019-06-20`、`aahana-2023-06-18`、Udaya 三隻蘋果籽、`kiki-2019-06-07`、`karma-2012-12-20`、
  `lincoln-2013-07-26`、`ravi-2022-06-14`、`rou-rou-2008-07-09`。

**根治：`audit.py` 新增「sources 有非官方 host」檢查（🟡）。** 依 `SCHEMA.md` 的分工，`sources` 只放官方／
一手來源，故其中任何被 `is_official_source()` 判 false 的 host 必是「漏掛白名單」或「該搬到 `extra_sources`」，
兩者都需處理——直接由稽核逐 host 列出（RPF／lineage 屬預期線索來源，排除不報）。稽核改為 import
`build_db.is_official_source`，確保「稽核看到的官方性 = 網站顯示的官方性」。此檢查為警告、不擋 push。

跑出的 16 個 host 逐一判定後**全屬「應搬 `extra_sources`」**（新聞媒體、保育 NGO、園方支援團體、
非園方粉專轉載），已於同日搬移完畢——26 筆條目、31 條連結，連結全數留存並補上出處註解，
稽核此項現為 0。資料異動詳見 `wiki/log.md` 同日 `fix` 條目。

## 2026-08-02 ・ 來源分類器：補園方白名單，並新增「官方轉載」逐條 URL 認列

承上一則「其他參考資料」上站後盤點日本個體，發現有些**確實是官方**的來源被 `is_official_source` 判為 false、
在個體頁被丟棄。分兩類補上：

- **`tools/build_db.py` `OFFICIAL_HOSTS`** 補 `hamurazoo.jp`（羽村市動物公園）、`city.sabae.fukui.jp`
  （鯖江市西山動物園，園頁掛在市府站 `/nishiyama_zoo/`，非 `.lg.jp` 故 gov pattern 抓不到）。
- **`OFFICIAL_IG_ACCOUNTS`** 補 `hamurazoo.official`、`maruyamazoo_official`、`seoulgrandpark`。相應地把
  wiki 內這三家的 IG 短形式 `/p/XXXX/` 改回含帳號的完整形式（短形式無從判斷發文者，一律非官方）。
- **新增 `OFFICIAL_URLS`（逐條 URL 白名單）**：`CLAUDE.md` 早有「官方內容之忠實轉載視同官方」，但轉載常落在
  共用平台（旅遊網站、新聞稿代發、個人部落格），整域列白名單會把同域的個人遊記一起誤判。改為逐條認列，目前三筆——
  多摩動物公園官方個體名單（4travel 轉載）、横浜八景島官方新聞稿（PR TIMES）、東北サファリパーク園內家系圖照片。
  比對時去掉 fragment 與尾斜線。新增前須先確認轉載內容確為園方一手。

配套的 wiki 資料異動（把誤置 `sources` 的非官方連結移入 `extra_sources` 等）記於 `wiki/log.md` 同日條目。

## 2026-08-02 ・ 「其他參考資料」上站：部落格／影片等非官方連結不再丟棄

處理アーヤ・アーニャ姊妹時，維護者提供了兩篇同好部落格與一支 YouTube 影片。這類連結不能當 `sources`（會被誤判官方、污染 `has_official_source`），過去多半就此丟失，但它們往往是唯一留下當年模樣的紀錄。改為一律留存於 `extra_sources` 並在網站另闢區塊顯示。

- **`web/src/components/Panda.astro`** 新增「其他參考資料」區塊，列於「來源」下方。`extra_sources` 兩種型態混存皆支援：值為 URL 者顯示網域並連結（`rel="noopener nofollow"`），純文字說明（如讀者實拍展牌、實體園報掃描）原樣顯示、不做連結。區塊附註明「非官方、未經園方佐證」。
- **`pipeline/src/i18n/*.json`** 五語各補 `sec_extra_sources`、`extra_sources_note`。資料管線無須改動——`build_db` 與 `export_json` 本就有 `extra_sources` 欄，只是先前「網站另區塊顯示（待實作）」。
- **`SCHEMA.md`** 新增〈sources 與 extra_sources 的分工〉對照表；**`CLAUDE.md`** 於「官方來源可直接採用」補一則：**能佐證即進 `sources`，只能參考就進 `extra_sources`，兩者都不是才丟棄**。由非官方來源帶入的關鍵資料仍照舊標 `🚧 待查證`——留連結不等於採信。

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
