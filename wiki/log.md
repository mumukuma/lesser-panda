# Wiki 變更日誌 Log

> 格式：`## [YYYY-MM-DD] 操作類型 | 說明`  
> 此為 append-only 日誌，記錄 wiki 的演進歷程；禁止 wikilink（名字一律 backtick）。  
> 過往月份定期封存至 `wiki/log-archive/log-YYYY-MM.md`（本檔只留近期月份）。

---

## [2026-08-11] update | `yun-yun`（雲雲・アドベンチャーワールド）2026 年初妊娠與死産；`yosaku` 搬入日校正

アドベンチャーワールド官方トピックス兩則（維護者提供，園方一手新聞稿）：2026-06-27 公告雲雲（ユンユン）
經超音波確認妊娠，為該園自 2018 年以來約 8 年首次的小熊貓新生命，園方載明「9 歳での初妊娠という国内
最高齢での事例」；配對對象為 2025-03-17 自ひらかたパーク搬入的 `yosaku`（与作），前一年（2025）的交尾
以「偽妊娠」告終。2026-07-11 續報：數日前超音波已無法確認胎兒心跳，7 月 8 日確認**死産**；母獸健康狀況
無異常，園方以雲雲體況恢復為優先。公告未載胎兒數、性別與死因。

**未建立寶寶條目**：本胎為死産、從未出生存活，無生日／性別／名字，依 CLAUDE.md「當季寶寶佔位條目：
蘋果籽」資格第 3 條（公告時已夭折者不建蘋果籽）不另建佔位條目；紀錄存於雲雲與与作兩頁備注。個體總數不變。

**`yosaku` 搬入日校正**：原記 2025-03-16（出自 RPF #345），園方公告明載「２０２５年３月１７日 ひらかた
パークより搬入」，依官方一手優先改為 2025-03-17（ひらかたパーク 訖日同步、居住史表重生）。

**來源**：
- https://www.aws-s.com/topics/detail?id=top4646 （アドベンチャーワールド 官方：8 年ぶりの妊娠確認、2026-06-27）
- https://www.aws-s.com/topics/detail?id=top4658 （アドベンチャーワールド 官方：赤ちゃんの死産について、2026-07-11）

**更新條目**：
- `yun-yun-2016-06-28.md` — 引言補配對與妊娠／死産一句；`家族` 加配偶列；新增 `## 備注`（妊娠確認、死産、未建蘋果籽的理由）；`sources` 加兩則官方公告
- `yosaku-2018-07-15.md` — `zoos:` 搬入日 2025-03-16 → 2025-03-17；引言補配對與死産一句；`家族` 加配偶列；新增 `## 備注`；`sources` 加兩則官方公告
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `aws-s.com`（アドベンチャーワールド 官網；園方新聞稿即計為官方來源）。⚠️ 該站新聞稿 PDF 為全形數字排版，自動文字擷取會誤讀日期（實測把出生日「６月２８日」讀成「６月１８日」），日期一律以 HTML topics 頁核對

## [2026-08-07] update | 移除 `kabosu` 的別名 `Komikan`／`こみかん`

維護者校訂：`kabosu`（RPF #255）並無 `Komikan`／`こみかん` 這兩個名字（原由 RPF 別名欄帶入）。移除
frontmatter `nicknames:` 整行與別名表的該兩筆，日文僅留 `かぼす`。續 2026-06-25 移除中文名「臭橙」
那筆校訂。

**更新條目**：
- `kabosu-2018-06-28.md` — 移除 `nicknames: [Komikan, こみかん]`；別名表日文改為僅 `かぼす`、刪「英文別名」列

## [2026-08-05] update | `qiu-qiu-kaohsiung`（球球・壽山）補兩支 YouTube 影片

網站個體頁「照片」區改版為「照片與影片」分頁（IG／YouTube，功能面見 `CHANGELOG.md`），frontmatter
新增選填欄位 `youtube:`（規範見 `SCHEMA.md`）。首例為壽山球球——該園史上唯一小熊貓，兩支同好實拍
影片經 YouTube oEmbed 核對標題與頻道，確屬本個體：

**來源**：
- https://www.youtube.com/watch?v=kmYvW8R8IRY （「1010325 壽山動物園 小貓熊」，李岱岱；標題民國日期＝2012-03-25，作排序日期）
- https://www.youtube.com/watch?v=BRw_Y6I80Uw （「寿山動物園～可愛賣萌小貓熊！」，azusakawa；上傳日期不詳、未填排序日期）

**更新條目**：
- `qiu-qiu-kaohsiung.md` — frontmatter 加 `youtube:` 兩筆（展示用影像；佐證性質的新聞連結仍在 `extra_sources` 不動）

## [2026-08-05] update | `kotarou-2005-07-08`（琥太郎）過世

大島公園動物園官方 X（`@ooshimashicho`＝東京都大島支庁，該園管理單位）2026-08-05 公告：飼育中的雄性小熊貓「琥太郎（コタロウ）」於 2026-07-29 死亡、21 歲，2007 年來園。官方帳號屬園方主管單位，比照官方訃告直接採用（園方訃告未載死因）。補 `died: 2026-07-29`、tags 加 `deceased`、`zoos` 訖改 2026-07-29；標題／引言加 🪽、歿記與得年（享年 21 歲），內文改過去式並補辭世一句。檔案續留 `wiki/`，`index.md` 該列補 🪽、享年段改 `2005–2026 🪽`（總數不變、仍上站）。父／母／姊妹／配偶／子女等既有條目對 `kotarou-2005-07-08` 的 wikilink 一併補 🪽。`tools/build_db.py` 的 `OFFICIAL_X_ACCOUNTS` 新增 `ooshimashicho`，此 X 訃告即計為官方來源。

**來源**：
- https://x.com/ooshimashicho/status/2084882090672197737 （東京都大島支庁 官方 X：琥太郎 2026-07-29 死亡、21 歲、2007 年來園）

**更新條目**：
- `kotarou-2005-07-08.md` — 補 `died`／`deceased`／X 來源；標題引言 🪽＋享年 21 歲；內文改過去式、補辭世
- `luna-2006-07-10.md`／`airi-2006-06-20.md`／`kojirou-2012-06-18.md`／`anko-2013-06-22.md`／`you-you-2002-06-21.md`／`buna-2000-07-17.md`／`marimo-2008-06-24.md`／`kotarou-2006-06-22.md` — 對 `kotarou-2005-07-08` 的 wikilink 補 🪽（`you-you`／`buna` 子女表另改「現居」→「終居」）
- `index.md` — `kotarou-2005-07-08` 該列補 🪽、享年段 `2005–2026 🪽`；`kotarou-2006-06-22` 列勿混淆註記補 🪽

**工具**：
- `tools/build_db.py` — `OFFICIAL_X_ACCOUNTS` 新增 `ooshimashicho`（東京都大島支庁＝大島公園動物園）

---

## [2026-07-27] update | `duo-duo-hangzhou` 確認為 `ma-tuan-2023-06-16`（麻團）之母

維護者提供：朵朵為麻團之母。麻團與月餅（`yue-bing-2023-06-16`）為同日同園雙胞胎（父同為山竹），故一併補上朵朵為月餅之母。三份條目 `家族` 欄位互相補上雙向 wikilink，移除原先「母：不詳（待查證）」；朵朵條目補列子女。家系無官方公告，`sources` 註明維護者提供（2026-07-27）。

**更新條目**：
- `duo-duo-hangzhou.md` — 家族補列子 `[[ma-tuan-2023-06-16]]`（麻團）、女 `[[yue-bing-2023-06-16]]`（月餅）
- `ma-tuan-2023-06-16.md` — 母改為 `[[duo-duo-hangzhou]]`（朵朵）
- `yue-bing-2023-06-16.md` — 母改為 `[[duo-duo-hangzhou]]`（朵朵）

---

## [2026-07-24] add | 柳州市動物園 大臉・小紅・熊大・洛克（維護者提供，中國個體檔案卡）

維護者提供柳州市動物園四隻小熊貓，比照中國個體「檔案卡」（`limited-profile`）模式建檔（2026-07-24 放寬門檻：綁已登記園＋維護者親自確認即可，無官方來源亦建檔）。四隻皆無具體出生日期、家系不明，`born` 留空、slug 採「名字-園簡稱」= `名字-liuzhou`（查得生日後再更名）。`大臉` 已於 2026-02-22 離世（記 `died`＋`deceased` tag，不用 `unverified`）——同園憨憨訃告（官方小紅書）文中亦悼念大臉先前離世，可為佐證；歿日由維護者提供。`小紅`♀・`熊大`♂・`洛克`♂ 現居在世，`last_seen` 記 2026-07-24、不掛 `unverified`。`洛克` 為 `luo-xi`（洛茜）之兄，雙向補手足 wikilink。四隻 `sources` 皆為 `維護者提供（2026-07-24）`（無 host、非官方來源，`has_official_source` 自動為 false）。

**來源**：
- 維護者提供（2026-07-24）
- http://xhslink.com/o/9vwtYcEd7P4 （柳州動物園官方小紅書訃告，文中悼念大臉先前離世；佐證大臉存在與死亡）

**新增條目**：
- `da-lian-liuzhou.md` — 大臉（大脸）Da Lian ♀，柳州市動物園，2026-02-22 離世（`limited-profile`＋`deceased`；生年・父母不詳）
- `xiao-hong-liuzhou.md` — 小紅（小红）Xiao Hong ♀，現居柳州市動物園（`limited-profile`；生年・父母不詳）
- `xiong-da-liuzhou.md` — 熊大 Xiong Da ♂，現居柳州市動物園（`limited-profile`；生年・父母不詳）
- `luo-ke-liuzhou.md` — 洛克 Luo Ke ♂，現居柳州市動物園、`luo-xi`（洛茜）之兄（`limited-profile`；生年・父母不詳）

**更新條目**：
- `luo-xi.md` — 補手足 `[[luo-ke-liuzhou]]`（洛克・兄）雙向 wikilink
- `index.md` — 柳州區塊新增四列、引言補述；條目總數更新為 683

---

## [2026-07-24] add | 瞬瞬（シュンシュン，RPF #597）— 瞬平之父、平川動物公園首例繁殖

讀者回報（回報者：楊桃）補齊 `shun-pei` 與 `fuumi` 中一直以純文字掛著的父親「Shun-Shun #597」。此瞬瞬與既有 `shun-shun-2001-06-28`（純純 #222）為不同個體。官方來源佐證：鹿児島経済新聞（2011-11-30）載瞬平命名由來、母風美、父瞬瞬因多臟器衰竭於 11/16 過世、歿時「まだ4歳」；平川動物公園園報〈gaiyo_h28.pdf〉沿革載「平成21年3月 瞬瞬（オス）来園（1歳）」「平成23年11月 レッサーパンダ（オス・瞬瞬）死亡」。生日 `2007-07-01` 與出生園 池田動物園：wiki 既在 `toku-toku`（#596，池田）條目載明瞬瞬生於池田、為 toku-toku 之子（RPF #596/#597 相鄰），官方「4歳」「1歳」亦與 2007 年生吻合；粉絲部落格為輔證，經作者確認採用 2007-07-01。父確定為 [[toku-toku]]（非回報所填「不詳」），母不詳。移園月份 2009-03 見園報，因居住史工具僅存年粒度、月份保留於內文。

**來源**：
- https://kagoshima.keizai.biz/headline/237/ （鹿児島経済新聞：瞬平命名式・瞬瞬歿）
- https://hirakawazoo.jp/wp/wp-content/uploads/2022/09/gaiyo_h28.pdf （平川動物公園園報，沿革頁）
- https://redpandafinder.com/#profile/597 （瞬瞬 RPF）

**新增條目**：
- `shun-shun-2007-07-01.md` — 瞬瞬 シュンシュン（RPF #597）♂，生於 2007-07-01 池田動物園，2009-03 移居鹿児島市平川動物公園，2011-11-16 歿（多臟器衰竭，享年 4 歲）；父 `toku-toku`、與 `fuumi` 育有 `shun-pei`

**更新條目**：
- `toku-toku-2001-07-21.md`／`shun-pei-2011-07-04.md`／`fuumi-2007-07-11.md` — 原純文字「Shun-Shun #597」改為 `[[shun-shun-2007-07-01]]` 雙向連結
- `index.md` — 心心家族新增「Toku-Toku 之子」小節列入瞬瞬、Sora 家族半血緣兄弟標頭改 wikilink；條目總數 672 → 673

---

## [2026-07-24] add | 柳州市動物園 憨憨（成年轉入個體、2026-07-18 離世）

柳州動物園官方小紅書發訃告悼念離世小熊貓，作者提供該貼文；貼文官方留言回覆載明憨憨來園日期與享年（官方來源，直接採用）。憨憨資料有限，比照中國個體「檔案卡」（`limited-profile`）模式建檔：來園時已成年、無具體出生日期、父母不詳，故 `born` 留空、`sex` 留空（性別不詳）；死訊明確故記 `died`、不用 `unverified`。因無生日，slug 採「名字-園簡稱」= `han-han-liuzhou`（查得生日後再更名為 `han-han-生日`）。同訃告提及同園「大脸」亦於此前約半年內離世，惟資料更少、暫不建檔（僅內文純文字帶過）。

**來源**：
- http://xhslink.com/o/9vwtYcEd7P4 （柳州動物園官方小紅書：〈柳州动物园的夏天，小熊猫化作了星星。〉訃告＋官方留言回覆）

**新增條目**：
- `han-han-liuzhou.md` — 憨憨 Han Han ♂，2020-12-18 來園（已成年）、生年不詳，2026-07-18 離世（估享年約 15 歲）；父母不詳（`limited-profile`＋`deceased`）

**更新條目**：
- `index.md` — 柳州區塊新增憨憨、引言補成年個體一句；條目總數 671 → 672

**追記（同日）**：作者補憨憨性別為 ♂；補 `sex: male`＋`male` tag，index／引言／內文同步。

---

## [2026-07-23] rename | `leanne` → `lian`（リアン／리안）＋補韓文名、名字由來

作者本人回報：`leanne` 的正式羅馬拼音應為 `Lian`，取自母親 `himawari`（ひまわり，向日葵）學名 Helianthus 當中的「lian」；韓文名 리안 見於園方公布出生的官方 IG 貼文（同一貼文亦佐證 `ravi` 韓文名 라비）。依此更名、補韓文名並補名字由來。

**更名**：
- `leanne-2020-07-20.md` → `lian-2020-07-20.md`（`name` Leanne → Lian；舊拼音 Leanne 留 `english_variants`；移除舊變體 Leeane／Lee-Anne／Leeanne／Leane；引言補名字由來、母親改 wikilink、家族「母」列改 wikilink；`sources` 補官方 IG）
- `apple-seed-1-leanne-2026-06-19.md` → `apple-seed-1-lian-2026-06-19.md`（母 slug 隨改）
- `apple-seed-2-leanne-2026-06-19.md` → `apple-seed-2-lian-2026-06-19.md`（同上）

**更新條目**：
- `ravi-2022-06-14.md` — 補 `korean: 라비`（官方 IG 佐證）、`sources` 補該 IG；配偶／子女／內文 wikilink 由 `leanne` 改 `lian`
- `fran-2020-07-20.md`／`himawari-2017-07-13.md`／`kanoko-2016-06-24.md`／`franken-2012-06-11.md`／`index.md` — 所有 `[[leanne-2020-07-20]]` 與蘋果籽舊 slug 改 `lian`；顯示名 Leanne → Lian

---

## [2026-07-23] fix | Subaru 來園日修正 2013-03-13 → 2013-05-14（平川動物公園官網）

讀者（`楊桃`）回報 `subaru`（スバル）轉入鹿児島市平川動物公園的日期有誤。平川動物公園官網訃告〈レッサーパンダの死亡について〉載明「来園年月日 ２０１３年５月１４日」，屬園方官方來源，直接採用更正（原 2013-03-13 疑為 RPF/lineage 帶入）。

**來源**：
- https://hirakawazoo.jp/2025/09/19/レッサーパンダの死亡について-2/ （平川動物公園官網訃告，載來園日 2013-05-14、生年月日 2010-06-26、死亡 2025-09-17）

**更新條目**：
- `subaru-2010-06-26.md` — `zoos:` 兩段轉園日 2013-03-13 → 2013-05-14（長野茶臼山訖、平川起）；居住史表格同步；sources 補平川動物公園官網訃告（官方來源）

---

## [2026-07-21] update | 夏娃 出身補記：自常州淹城野生動物世界轉入

作者提供 `xia-wa`（夏娃）由**常州淹城野生動物世界**轉入南京市紅山森林動物園（年份不詳），與配偶 `xiao-xiao-bai-nanjing`（小小白）同源。出身無官方連結，標 🚧 待查證。此補記亦修正原居住史誤將紅山標為出生地（🐣）——現改標於淹城（轉入前所在，是否為出生園待查）。

**更新條目**：
- `xia-wa.md` — `zoos` 前置 `常州淹城野生動物世界`（年份不詳）、tags 加 `zoo:常州淹城野生動物世界`、sources 加作者提供註記；引言補「出身」行、更新 🚧 待查證；居住史重生（淹城 🐣、紅山改僅 🏡）

---

## [2026-07-21] update | 柳州 白桃 2026 年夭折

作者回報 `bai-tao-2025-06-16`（白桃）於 2026 年夭折（僅知年份，確切日期待查證）。白桃有正式名，依幼逝寶寶收錄原則續留 wiki、照常上站（僅標 🪽）。

**更新條目**：
- `bai-tao-2025-06-16.md` — 補 `died: 2026`、tags 加 `deceased`、`zoos` 訖改 2026；標題／引言／基本資料加 🪽、歿記與得年（約一歲）
- `xiao-bai.md`／`xi-bao.md` — 父母子女表白桃列加 🪽、生卒改 2025–2026
- `mu-shu-2026-06-12.md`／`liang-shu-2026-06-20.md` — 同父異母手足白桃加 🪽
- `index.md` — 白桃列加 🪽、生卒 2025–2026、說明補「2026 年夭折」（總數不變）

---

## [2026-07-21] add | 柳州市動物園 2026 新生幼崽 木薯・凉薯（已命名）＋母親 麗莎・洛茜

**來源**：
- http://xhslink.com/o/4g1ZO8bso7S （柳州動物園官方小紅書：〈你好，初次见面，介绍一下〉，介紹兩隻新生幼崽）

柳州動物園官方小紅書公告 2026 年兩隻新生幼崽並已命名（官方來源，直接採用）。兩隻同父（`xi-bao` 喜寶）、母親不同，屬同父異母 ½ 半血緣；非同胎、故不編蘋果籽序號，直接以正式名建檔。母親 `li-sha`（麗莎）、`luo-xi`（洛茜）為新面孔、除名字與現居園外資料不詳，比照 `xi-bao`／`hao-chi-gui` 之柳州親代 stub 建檔（bare slug、待查證）。

**新增條目**：
- `mu-shu-2026-06-12.md` — 木薯 Mu Shu ♂，2026-06-12 生於柳州市動物園（深色款）；父 `xi-bao`・母 `li-sha`
- `liang-shu-2026-06-20.md` — 凉薯 Liang Shu ♀，2026-06-20 生於柳州市動物園（浅色款）；父 `xi-bao`・母 `luo-xi`
- `li-sha.md` — 麗莎 Li Sha ♀，生年不詳，木薯之母（出身／父母待查證）
- `luo-xi.md` — 洛茜 Luo Xi ♀，生年不詳，凉薯之母（出身／父母待查證）

**更新條目**：
- `xi-bao.md` — 引言與子女表補 木薯、凉薯（喜寶現與小白・麗莎・洛茜三隻雌性各有後代）
- `bai-tao-2025-06-16.md` — 家族補同父異母手足 木薯・凉薯
- `index.md` — 柳州區塊新增 4 列、引言補 2026 幼崽；條目總數 667 → 671

---

## [2026-07-21] add | 首爾大公園 Leanne × Ravi 雙胞胎（蘋果籽佔位，韓國國內首次繁殖）

**來源**：
- https://www.instagram.com/p/DbCa2XdETd3/ （seoulgrandpark 首爾大公園官方 IG）

讀者回報：`leanne` × `ravi` 於 ソウル大公園動物園 產下雙胞胎寶寶。園方官方 IG 公告 2026-06-19 出生，由母 `leanne`（리안）與父 `ravi`（라비）自然交配（자연번식）所生，稱為大韓民國**國內首次**小熊貓繁殖成功。兩隻健康、於非公開空間 24 小時照護中，預計約 11 月分階段亮相。尚未命名、性別未公布 → 依蘋果籽佔位規則建檔，直接上站。

**新增條目**：
- `apple-seed-1-leanne-2026-06-19.md` — 蘋果籽1號，生於 2026-06-19，現居 ソウル大公園動物園（性別待確認、序號暫編、RPF 待建檔）
- `apple-seed-2-leanne-2026-06-19.md` — 蘋果籽2號，同上

**更新條目**：
- `leanne-2020-07-20.md` — 引言與 `## 家族` 補配偶 `ravi`、子女雙胞胎雙向 wikilink
- `ravi-2022-06-14.md` — 引言與 `## 家族` 補配偶 `leanne`、子女雙胞胎雙向 wikilink
- `index.md` — Ravi 一家區塊新增兩列、引言補雙胞胎；條目總數 665 → 667

---

## [2026-07-03] update | 處理「回報資料更正」收件匣＋補繁繁生日

**來源**：
- https://www.tokyo-zoo.net/topics/news/tama/739_28260_2023-11-01.html （多摩動物公園官方公告，`sei` 移動）
- https://www.zoo.gov.taipei/News_Content.aspx?n=BD065B2FA7782989&sms=72544237BBE4C5F6&s=E0159F1BC3487BED （臺北市立動物園新聞稿，`chen-chen` 抵臺）

**更新條目**：
- `sei-2019-07-02.md` — 依多摩官方公告修正轉園：Seoul 移居日 2023-11-23 → **2023-11-27**，並補上經多摩動物公園檢疫轉運（2023-11-22 – 11-27）之中繼；居住史由兩園改三園（埼玉こども → 多摩 → ソウル大公園）；`sources` 補官方連結
- `chen-chen-2022-07-05.md` — 依臺北動物園新聞稿，抵臺日由年份 `2026` 精確為 **2026-03-16**（旭山 → 台北）；`sources` 補官方連結
- `fan-fan-2023.md` → **改名 `fan-fan-2023-05-02.md`** — 作者提供繁繁生日 2023-05-02，`born`／`zoos` 起日／內文一併更新；`index.md`、`tian-tian-2024-06-23.md` 之 wikilink 同步改指新 slug
- `shiryu-2007-06-26.md` — 補中文名「石榴」（`chinese: 石榴`、標題與名稱表）；回報來源雖為個人部落格，但中文名命名以作者為準，**經作者確認後採用**

**備注**：多摩動物公園已登記於 `data/zoos.json`。繁繁生日、shiryu 中文名皆由作者直接確認，屬權威來源。

---

## [2026-07-03] fix | 清理別名重複＋修 build_db 空清單解析

**問題**：個體頁「別名」欄（= `nicknames` + `english_variants`）出現重複，例如 `ran-fa-2018-06-02` 的 Ranfa／Ranhowa 同時列於兩欄。

**更新條目（去除重複別名）**：
- 跨欄重複：`ran-fa-2018-06-02`（Ranfa、Ranhowa 併入 `english_variants`，清空 `nicknames`）、`lemon-2013-07-07`／`mulan-2019-06-07`（暱稱 Milky／Princess Moomoo 保留於 `nicknames`，自 `english_variants` 移除）
- 欄內重複：`nohana-2017-07-31`（`english_variants` Norin×2 → ×1）
- 別名與本名／日文／漢字重複：`akatsuki`／`akebono`／`asahi`（移除暱稱 暁／曙／旭）、`ashitaba`／`monaka`（移除與本名相同的變體）、`ron-2005-06-23`（移除與日文漢字相同的 龍）

**工具修正**：
- `tools/build_db.py` `_parse_simple_yaml` — 空 inline 清單 `[]` 原被解析為 `[""]`（`"".split(",")` 之故），會在別名產生一個幽靈頓號；已修正為正確空清單，連帶清掉 `ron-ron-2002-06-28`、`shin-fa-2019-06-19`、`shiryu` 的空字串別名
- `web/src/components/Panda.astro` — 別名渲染加上 `new Set` 去重並濾除與主名／別名相同者，防止日後再現

**備注**：各條目內文「## 別名」表格原本即已分欄清楚、無重複，未更動。

---

## [2026-07-01] update | 照片投稿：批次補 IG 連結（27 隻，98 筆）

首批「幫忙補照片」Tally 投稿（表單 `lb5zVv`）經查證後採用，把讀者/同好提供的公開 IG 貼文連結寫入對應個體 frontmatter 的 `instagram:`。連結已正規化（去除 `igsh`／`img_index` 追蹤參數、統一為 `/p|reel|tv/SHORTCODE/`）並去重。多為短連結不含帳號，`ig_audit.py` 會標「⚠️ 無帳號」（可正常 embed，僅不顯示 @攝影者）。

**來源**：
- 照片投稿收件匣（Google Sheet「幫忙補照片 写真を投稿する Submit a photo」）

**更新條目**（+新增連結數）：
- `yaffa-2015-06-22`(+13)、`keyue-2015-06-20`(+11)、`sora-2014-06-12`(+10)、`maruko-2018-07-11`(+10)、`kexin-2015-06-20`(+7)、`rifa-2018-06-07`(+7)、`tiara-2015-07-06`(+6)、`keleguo-2019-06-08`(+5)、`crepe-2017-06-11`(+4)、`ke-song-2017-06-11`(+3)、`canele-2021-07-06`(+3)、`mei-fa-2019-06-19`(+3)、`ako-2023-06-01`(+2)
- 各 +1：`mametaro-2016-06-24`、`kanoko-2016-06-24`、`futa-2003-07-05`、`gao-gao-2015-06-27`、`kaede-2022-06-27`、`chiita-2008-06-27`、`akebi-2020-06-29`、`natsume-2018-06-27`、`hinata-2021-06-21`、`nico-2017-06-23`、`huanhuan-2007-07-03`、`monaka-2025-07-11`、`taofa-2015-06-14`、`shin-fa-2019-06-19`
- 重建 `redpanda.db` 與 `pipeline/data/*.json`

---

## [2026-07-01] update | 資料更正批次（Tally 表單 `ODr777`，6 筆採用）

讀者回報經對照東京動物園協會（tokyo-zoo.net）官方公告逐筆查證後採用。回報者：`Aoi Ajisai`、`楊桃`。

**來源**：
- 回報資料更正收件匣（Google Sheet「小熊貓資料回報收件匣」）
- https://www.tokyo-zoo.net/topics/news/tama/7619_8350_2008-02-08.html （緑太郎 死亡）
- https://www.tokyo-zoo.net/topics/news/tama/127_29351_2025-10-09.html （タオファ 死亡）
- https://www.tokyo-zoo.net/topics/news/tama/8767_222_2002-10-25.html （2002 命名公告：イクラ×淡々→カツオ・マグロ）
- https://www.tokyo-zoo.net/topics/news/tama/437_28574_2024-08-01.html （カイト 移動）
- https://www.tokyo-zoo.net/topics/news/tama/1516_27248_2022-02-10.html （メイファ 移動）
- https://www.tokyo-zoo.net/topics/news/oshima/6834_13391_2009-12-23.html （コタロウ 來自江戸川区）

**更新條目**：
- `ryutarou-1999-07-27.md` — 歿日 2009-02-04 → 2008-02-04（官方：8歲6個月）；享年 9 → 8；父緑々・母寧々經官方確認無誤
- `taofa-2015-06-14.md` — 歿日 2025-10-05 → 2025-10-07（10/5 為發病日、7 日晨確認死亡）
- `katsuo-2002-07-02.md` — 母 `fan-fan` → イクラ（Ikura，無條目）；與 `maguro` 雙胞胎（同父淡々）；補家族父母欄
- `maguro-2002-07-02.md` — 雙胞胎/兄弟姊妹 Katsuo 純文字改 `[[katsuo-2002-07-02]]`；父改 `[[tan-tan-1998-06-29]]`
- `kaito-2022-06-27.md` — 居住史補多摩動物公園檢疫段：西山(–2024-06-03)→多摩(2024-06-03–2024-07-31)→Batu(2024-07-31–)
- `mei-fa-2019-06-19.md` — 出生地更正為多摩動物公園（2019-06-19 生），2022-03-16 以繁殖借出移居九十九島；zoos 增多摩段
- `kotarou-2005-07-08.md` — 出生地更正為江戸川区自然動物園（2005 生），2007 年移居大島公園；zoos 增江戸川区段
- `index.md` — Ryutarou 生卒 1999–2009 → 1999–2008；最後更新 2026-07-01

**暫緩（待作者裁定）**：
- `kusu-1991-06-24.md` — 回報稱母親名為「麗麗」（1986-07-05～1995-10-24），來源為 code4fukui 開放資料（非官方）；且與 wiki 既有編註「無正式名」牴觸，暫不套用，留待查證。

---

## [2026-07-01] add | 補建風太之父風々一脈（圖鑑缺漏回報）

處理「圖鑑缺漏回報收件匣」中回報者 Aoi Ajisai（2026-06-30）的缺漏小熊貓：風太（`futa`）之父 `fu-fu`（風々／フウフウ）及其父母、三胞胎、手足、同母異父手足。經既有條目（`nene`、`you-you`、`boo-boo`、`tan-tan` 等）與 RPF 交叉查證後補建；查證中發現部分個體早已有 RPF 編號（`ran-ran` #551＝淡々雙胞胎、`hana` #308、`nana` #216），故不採回報「存疑」記法而用實證資料。

**來源**：
- https://redpandafinder.com/#profile/50 (Fu-Fu 風々)、#960 (Ryu-Ryu 緑々)、#549 (Kou-Kou 光々)、#551 (Ran-Ran 蘭々)、#308 (Hana)、#216 (Nana)
- https://www.nhdzoo.jp/red-panda/kakeizu/index.html (日本平動物園小熊貓家系圖)
- https://www.tokyo-zoo.net/topics/news/tama/8780_199_2002-08-30.html
- 回報收件匣：Google Sheet「回報缺少的小熊貓或動物園資料」submission `aOEzG62`

**新增條目**：
- `fu-fu-1997-06-20.md` — Fu-Fu 風々／フウフウ（RPF #50），♂，1997-06-20 – 2003-06-12，多摩→釧路→日本平動物園；`futa` 之父（⚠️ 同名 `fu-fu-2014-06-22`）
- `ryu-ryu-1990.md` — Ryu-Ryu 緑々（RPF #960），♂，1990–1999，多摩動物公園；風々之父、`nene` 之配偶
- `kou-kou-1997-06-20.md` — Kou-Kou 光々（RPF #549），♂，1997-06-20，三胞胎（⚠️ 同名航航 `kou-kou-2003-07-15`）
- `ran-ran-1998-06-29.md` — Ran-Ran 蘭々（RPF #551），♀，1998-06-29，`tan-tan` 雙胞胎（性別待查證）
- `ki-ki-1996.md` — Ki-Ki 希々，♂，1996?（存疑，待查證）
- `naka-naka.md` — Naka-Naka 中々，♂，緑々之父（讀音／資料待查證）
- `hana-hana.md` — Hana-Hana 華々，♀，緑々之母（讀音／資料待查證）
- `hana-2001-07-13.md` — Hana ハナ（RPF #308），♀，2001，`nana` 雙胞胎（母 `nene`、父 `boo-boo`）
- `nana-2001-07-13.md` — Nana ナナ（RPF #216），♀，2001 – 2018-02-09，`hana` 雙胞胎
- `noa-2004.md` — Noa ノア，♂，2004? – 2010-03-24（生年存疑，待查證）

**更新條目**：
- `futa-2003-07-05.md` — 父 Fu-Fu 純文字改 `[[fu-fu-1997-06-20]]`
- `nene-1993-07-11.md` — 子女表改依父別（緑々／ブーブー）分組並全數改 wikilink，補配偶欄
- `you-you-1997-06-20.md` — 父母與三胞胎（Fu-Fu／Kou-Kou）純文字改 wikilink
- `ryutarou-1999-07-27.md`／`ryuunosuke-1999-07-27.md` — 父母改 `[[ryu-ryu-1990]]`／`[[nene-1993-07-11]]`，補兄姊；`ryuunosuke` 補家族區
- `tan-tan-1998-06-29.md` — 父「不明」改 `[[ryu-ryu-1990]]`（回報，待查證）、雙胞胎改 `[[ran-ran-1998-06-29]]`、補兄弟
- `boo-boo-1997-07-13.md` — 子女表 Hana／Nana／Nono／Nami／Non 改 wikilink、母欄標為 `nene`、補 Noa
- `index.md` — 新增「風太之父：風々一脈」區塊；條目總數 448 → 458

**回報中未採用**：
- submission `YjYoo7N`（Aoi Ajisai）為功能建議「指定動物園時查不到已逝小熊貓」，屬網站篩選功能、非資料缺漏，另行評估。

---

## [2026-07-01] add | 資料更正批次：補建 Kusu／Sui-Sui 之母 Lili 條目（RPF #776）

承前「資料更正」批次，回報者 `Aoi Ajisai` 指出先前記為「無名母（無正式名）」的 RPF #776 實名為「麗麗」，並提供生卒日。經作者採用，補建獨立條目並回填雙向連結。羅馬拼音經作者確認採 `Lili`。

**來源**：
- 回報資料更正收件匣（Google Sheet「小熊貓資料回報收件匣」）
- https://code4fukui.github.io/lesserpanda-opendata/
- https://redpandafinder.com/#profile/776

**新增條目**：
- `lili-1986-07-05.md` — Lili（麗麗／リーリー，RPF #776），♀🌈，1986-07-05 – 1995-10-24，西山動物園出生、後移天王寺動物園；配偶 `yuu-yuu-1987-05-31`，子女 `sui-sui-1989-06-29`・`kusu-1991-06-24`（轉園年份暫記 1993、待考）

**更新條目**：
- `kusu-1991-06-24.md` — 母「無名母 #776」改為 `[[lili-1986-07-05]]`（內文＋家族）
- `sui-sui-1989-06-29.md` — 母「無名母 #776」改為 `[[lili-1986-07-05]]`（內文＋家族）
- `yuu-yuu-1987-05-31.md` — 子女表 Sui-Sui／Kusu 之母欄「無名母 #776」改為 `[[lili-1986-07-05]]`
- `index.md` — 新增 `lili-1986-07-05` 行、母註連結化；條目總數更新為 459

---

## [2026-07-01] update | 風々一脈：核對回報者原始連結後之更正

依作者要求，實際開啟回報者（`Aoi Ajisai`）於「圖鑑缺漏」submission `aOEzG62` 提供的連結逐一查證。**日本平動物園園報〈でっきぶらし〉156 號**與 **多摩動物公園官方個體名單（經 4travel 旅行記轉載）** 為關鍵一手／半官方來源，據以修正先前僅憑回報文字建檔的數處：

**已開啟並採用的連結**：
- https://www.nhdzoo.jp/sp/newspaper/naka.php?newspaper_uid=1536 （日本平園報 #156「風太くん誕生！」）
- https://www.nhdzoo.jp/red-panda/kakeizu/index.html （日本平家系頁；JS 動態、僅列現役個體）
- https://www.tokyo-zoo.net/topics/news/tama/8780_199_2002-08-30.html （多摩 2002 繁殖公告）
- https://4travel.jp/travelogue/11691476 （轉載多摩官方個體名單，含全家系生卒與轉園）

**無法開啟的連結**（受限或需 JS，未採為依據）：
- web.archive 靜岡市 PDF（`000788080.pdf`）— 於本工具屬封鎖網域
- x.com/i/status/1738847365413683482、x.com/i/status/1725063793070518510 — Twitter/X，無法擷取

**主要更正**：
- `fu-fu-1997-06-20.md` — **移除「釧路市動物園」中繼站**：園報明載風々由多摩直接來日本平（2002/3），回報之釧路疑為與釧路出生的イクラ混淆；居住史改多摩(1997-06-20–2002-03-23)→日本平(–2003-06-12)；補園報敘事（風太之名取自父フウフウ的「風」字）與園報來源
- `kou-kou-1997-06-20.md` — 官方名單記光々「死亡」→ 補 `deceased`／🌈（歿日不詳）
- `tan-tan-1998-06-29.md` — 官方名單確認父為「緑々×寧々」→ 父欄由「不明」更正為 `[[ryu-ryu-1990]]`（去除待查證）
- `ran-ran-1998-06-29.md` — 性別 ♀ 經作者確認（去除性別待查證）；註記蘭々未見於多摩官方名單、僅據 RPF #551 與既有條目
- `hana-2001-07-13.md` — 官方名單標「？」（狀況不明、非確認死亡）並移居墨西哥チャプルテペック動物園 → **移除誤標的 `deceased`／🌈**，改註狀況待查
- `nana-2001-07-13.md` — 居住史更正為多摩→秋田市大森山動物園ミルヴェ（2018-02-09 於該園歿）；轉出年暫記 2003（待查）
- `noa-2004.md` — 居住史更正為多摩→仙台市八木山動物公園（名單註在該園時名サクラ，待查；2010-03-24 歿）；轉出年暫記 2005（待查）
- `nene-1993-07-11.md`／`boo-boo-1997-07-13.md`／`index.md` — 同步上述 Hana（去🌈）、Nana（大森山）、Noa（八木山）之標註；`ryutarou` 生卒於 index 由 1999–2009 更正為 1999–2008（與 frontmatter 2008-02-04 一致）

**仍待作者裁定**：`緑之介` 歿年 wiki 記 2019-03-12，多摩名單記 2018-03-12（不符，未動 wiki）；墨西哥チャプルテペック動物園尚未登記於 `data/zoos.json`，故 Hana 居住史暫僅列出生地。

---

## [2026-07-01] update | 作者裁定：緑之介歿年、Chapultepec 登記、採用政策

承上，作者就前述待裁定事項給出決定：

- **`ryuunosuke-1999-07-27.md`（緑之介）** — 歿年改採多摩動物公園個體名單所載 **2018-03-12**（原 RPF 2019-03-12 不採）；更新 `died`、とべ動物園居住段訖日、內文加裁定註記；`index.md` 生卒改 1999–2018
- **`data/zoos.json`** — 新增 **チャプルテペック動物園**（Zoológico de Chapultepec，墨西哥メキシコシティ，lat/lng 約略、aliases 含西/英/中/日名）；動物園總數 98 → 99
- **`hana-2001-07-13.md`** — 居住史補上 多摩(2001-07-13–2003 約略)→チャプルテペック動物園(2003–)；轉出年待查
- **`CLAUDE.md`** — 新增「官方來源可直接採用」政策小節：回報者若附官網／新聞稿／園報／園方名單等官方或官方轉載來源，Claude 可直接採用更新 wiki、與既有校訂衝突時以園方為準，不需逐筆等作者確認；非官方來源（RPF／lineage／部落格／社群／無來源）仍標待查證

---

## [2026-07-01] update | 修正錯誤投稿：兩則 IG 照片由 `keyue` 移至 `crepe`

兩則 IG 貼文原被錯歸於 `keyue`（可玥），實為 `crepe`（可麗餅）的照片，予以更正：

- `https://www.instagram.com/p/C4omQ03B_dT/`
- `https://www.instagram.com/p/C1irAyBPVP-/`

**更新條目**：
- `keyue-2015-06-20.md` — `instagram:` 移除上述兩則
- `crepe-2017-06-11.md` — `instagram:` 加入上述兩則

---

## [2026-07-01] update | 讀者投稿 IG 照片補進 3 隻條目

照片投稿收件匣（幫忙補照片 Google Sheet）新增 3 筆本人投稿，查證發文帳號後以含帳號完整形式補進對應條目的 `instagram:`：

**來源**：
- https://www.instagram.com/washimumu/p/DWIaNc0EWWW/ (`huanhuan`，帳號 washimumu)
- https://www.instagram.com/kinusayaffa/p/DaPGjQSEqCE/ (`ke-song`，帳號 kinusayaffa)
- https://www.instagram.com/kinusayaffa/reel/DaG-qfbvqxy/ (`mirai`，帳號 kinusayaffa)

**更新條目**：
- `huanhuan-2007-07-03.md` — `instagram:` 加入 washimumu 該則
- `ke-song-2017-06-11.md` — `instagram:` 加入 kinusayaffa 該則
- `mirai-2019-07-05.md` — 新增 `instagram:` 欄（原無），加入 kinusayaffa 該 reel

---

## [2026-07-01] add | 新增 Ikura 家族 3 條目 + 更正 Tan-Tan 子女母親

**來源**：
- https://redpandafinder.com/#profile/656 (Ikura)
- https://redpandafinder.com/#profile/375 (Konta)
- https://redpandafinder.com/#profile/731 (Cha)

**新增條目**：
- `ikura-1996-07-09.md` — Ikura イクラ（RPF #656），生於 1996-07-09、歿 2006-02-12，釧路市動物園 → 多摩動物公園 → 福岡市動植物園；`tan-tan` 之配偶，`maguro`／`katsuo`／`konta` 之母。性別依作者告知（♀，日文名イクラ）
- `konta-2004-07-10.md` — Konta コンタ（RPF #375），生於 2004-07-10、歿 2014-08-05，福岡市動植物園 → 仙台市八木山動物公園；`ikura` × `tan-tan` 之三子
- `cha-1997-07-27.md` — Cha チャ（RPF #731），生於 1997-07-27、歿 2016-03-27，釧路市動物園 → 浜松市動物園；`ikura` 之妹（注意與既有 `cha-cha-1997-06-17` #223 非同一隻）

**更新條目**：
- `maguro-2002-07-02.md`、`katsuo-2002-07-02.md` — 母由純文字「Ikura（無條目）」改為 `[[ikura-1996-07-09]]` wikilink；maguro 兄弟欄 Konta 改為 wikilink
- `tan-tan-1998-06-29.md` — **更正**：子女表原將 Maguro（2002）／Katsuo（2002）／Konta（2004）之母記為 `fan-fan-1999-07-09`，據 RPF #656・#375 及 maguro／katsuo 條目、且 `fan-fan` 本身條目未列此三隻，更正為母 = `ikura-1996-07-09`；Run-Run／Mei-Mei（2007）之母仍為 `fan-fan`
- `index.md` — 新增「Ikura × Tan-Tan 一脈」小節（Ikura／Konta／Cha）；條目總數 459 → 462

---

## [2026-07-01] update | 官方來源確認 Ikura 親子關係（多摩命名公告）

**來源**：
- https://www.tokyo-zoo.net/topics/news/tama/8767_222_2002-10-25.html （多摩動物公園官方 2002-10-25 命名公告）

官方公告明載 2002 年 6〜7 月三對親代所生 5 仔的命名：「母イクラ × 父淡々」→ 雄性雙胞胎「カツオ」「マグロ」（魚介類名）；「母花々 × 父緑太郎」→ 女兒「タンポポ」；「母寧々 × 父ブーブー」→「ノノ」（♂）「ナミ」（♀）。此為 `maguro`／`katsuo` 之母為 `ikura`（非 `fan-fan`）的一手官方佐證，前一筆更正確立無誤。

**更新條目**：
- `ikura-1996-07-09.md` — `sources:` 加入官方連結；內文加註官方命名確認
- `maguro-2002-07-02.md`、`katsuo-2002-07-02.md` — `sources:` 加入官方連結

**備注（已結案，2026-07-01）**：作者裁示以官方公告為準。查證 `fin-fin-2002-06-20` 條目本已記錄別名タンポポ（`japanese: フィンフィン, タンポポ`／`english_variants: [Finfin, Tanpopo]`），且母 Fan-Fan × 父 Ryutarou、2002-06-20 多摩生、2003 遷池田動物園，與公告完全吻合——確認 Tampopo 與 Fin-Fin 為同一隻（出生官方名タンポポ，後名 Fin-Fin）。已將官方公告補入 `fin-fin-2002-06-20.md` 的 `sources:` 並於內文加註官方確認。主名維持 Fin-Fin（RPF／池田通用名、既有 wikilink 穩定）；如需改以タンポポ為主名再另行更名。

---

## [2026-07-01] remove | 下架非本人投稿照片（讀者投稿收件匣）

依作者指示，將投稿收件匣中標記「非本人投稿（同好的公開貼文）」的 6 筆，其 IG 連結自對應條目 `instagram:` frontmatter 移除（**僅移除該筆非本人連結，保留同一隻的本人投稿連結**）；並同步移除 Google Sheet 收件匣對應 6 列。

**更新條目**：
- `sora-2014-06-12.md` — 移除 10 筆非本人 IG 連結，保留本人投稿 2 筆
- `rifa-2018-06-07.md` — 移除 7 筆，保留本人投稿 5 筆
- `maruko-2018-07-11.md` — 移除 10 筆，保留本人投稿 5 筆
- `futa-2003-07-05.md` — 移除 1 筆（唯一連結，皆非本人），`instagram` 欄整個移除
- `tiara-2015-07-06.md` — 移除 6 筆（皆非本人），`instagram` 欄整個移除
- `mochi-2015-06-24.md` — 移除 7 筆（皆非本人），`instagram` 欄整個移除

重建：`build_db` + `export_json`（沙盒 /tmp shim）已更新 `pipeline/data/*.json`（沙盒無法跑 `web/` Astro build，網站由 CI 部署）。

---

## [2026-07-01] add | 新增 Ryuu 及其手足（Hanabi × Sou-Sou 子女）

**來源**：
- https://redpandafinder.com/#profile/957 (Ryuu)
- https://redpandafinder.com/#profile/958 (Sei)
- https://redpandafinder.com/#profile/80 (Miyabi)
- https://redpandafinder.com/#profile/242 (Rin)

**新增條目**：
- `ryuu-2019-07-02.md` — Ryuu リュウ（RPF #957），生於 2019-07-02，`sei` 之雙胞胎；暱稱歌舞伎（Kabuki）；埼玉こども→東北サファリパーク
- `sei-2019-07-02.md` — Sei セイ／세이（RPF #958），生於 2019-07-02，`ryuu` 之雙胞胎；埼玉こども→ソウル大公園動物園 🇰🇷
- `miyabi-2017-06-25.md` — Miyabi ミヤビ／雅（RPF #80），生於 2017-06-25、歿於 2022-10-02🌈；埼玉こども→Chilean National Zoo 🇨🇱
- `rin-2018-06-24.md` — Rin リン／Lynn（RPF #242），生於 2018-06-24，現居埼玉県こども動物自然公園

**更新條目**：
- `hanabi-2011-07-09.md` — 母；4 名子女純文字改為 wikilink
- `sou-sou-2012-07-08.md` — 父🌈；子女表改為 wikilink，`sei` 註記現居韓國
- `index.md` — 新增「Hanabi × Sou-Sou 子女」小節；條目總數更新為 466

**備注**：性別依四隻手足頁的 sibling 敘述交叉推定——Miyabi、Rin 為 ♀，Sei、Ryuu 為 ♂。父母條目本已存在，故僅補雙向 wikilink。

## [2026-07-02] fix | 讀者回報資料更正（居住史／轉園日；官方來源直採）

依「回報資料更正」收件匣 4 筆有效回報（1 筆為重複），經官方來源查證後更正居住史與轉園日。均為官方一手來源，依 2026-07-01 授權直接採用。

**來源**：
- https://www.soumu.metro.tokyo.lg.jp/documents/d/soumu/2026ressapandaairi_pdf-1- （大島公園動物園 アイリ死亡公告，載明来園日 2009-03-27）
- https://www.tokyo-zoo.net/topics/news/tama/8705_314_2003-04-18.html （東京ズーネット：ナナ 2003-04-23 往秋田大森山）
- https://www.tokyo-zoo.net/topics/news/tama/8758_237_2002-11-29.html （ハナ 2002-11-29 往上野）
- https://www.tokyo-zoo.net/topics/news/ueno/8737_269_2003-01-31.html （ハナ 2003-01-27 隨リンリン往墨西哥チャプルテペック）

**更新條目**：
- `airi-2006-06-20.md` — 大島公園動物園来園日由 2007-07-18 更正為 **2009-03-27**（官方死亡公告）；茶臼山居住期間隨之延至 2009-03-27
- `nana-2001-07-13.md` — 多摩→秋田大森山轉園日由約略 2003 精確為 **2003-04-23**；生日 2001-07-13 亦經官方新聞確認，移除 🚧 待查證與 `unverified` 標籤
- `hana-2001-07-13.md` — 補入中繼居住 **恩賜上野動物園**（2002-11-29 – 2003-01-27）；多摩→上野→チャプルテペック轉園日精確化；チャプルテペック抵達後現況仍不明、維持不標歿

**未異動（僅確認、無需修改）**：
- `nyan-nyan-2001-07-09.md` — 回報稱母朝朝、父陽陽，與現有 frontmatter 完全一致，無需更動（回報者所附來源為西山動物園家系圖，與本個體居住園（旭山／市川）不符，僅記備注）

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-02] add | 補建娘娘（Nyan-Nyan）雙親條目（讀者回報 BEDVNK4）

讀者回報 `nyan-nyan-2001-07-09` 之母為朝朝（チャオチャオ）、父為陽陽（ヤンヤン），來源為西山動物園家系圖。經 RPF 交叉確認：兩隻皆生於鯖江市西山動物園、1993-04-22 移居旭川市旭山動物園並在該園繁殖娘娘一脈。原條目雖已於內文列出父母姓名，但因無對應條目、非 wikilink，網站顯示「父母不詳」；此次補建雙親條目並雙向連結，網站家系即可顯示父母。

**來源**：
- https://redpandafinder.com/#profile/598 (Chao-Chao 朝朝)
- https://redpandafinder.com/#profile/822 (Yan-Yan 陽陽)
- 西山動物園家系圖（讀者回報 BEDVNK4）

**新增條目**：
- `chao-chao-1991-06-18.md` — Chao-Chao 朝朝（RPF #598），♀，1991-06-18 生於鯖江市西山動物園、2013-07-30 歿🌈；娘娘之母
- `yan-yan-1992-06-19.md` — Yan-Yan 陽陽（RPF #822），♂，1992-06-19 生於鯖江市西山動物園、2010-07-04 歿🌈；娘娘之父（⚠️ 同名多隻）

**更新條目**：
- `nyan-nyan-2001-07-09.md` — 父母純文字改為 `[[chao-chao-1991-06-18]]`／`[[yan-yan-1992-06-19]]` wikilink
- `index.md` — 新增「曾祖父母（Nyan-Nyan 娘娘 的父母）」小節；條目總數更新為 468

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-02] hide | 暫時隱藏 5 筆幼逝（未滿一歲）條目

依作者指示，將 5 筆「出生後未滿一歲即夭折」的條目**暫時隱藏、非刪除**：移入 `wiki/_hidden/` 子資料夾。因 `build_db.py`／`gen_residence.py` 均以 `wiki/*.md`（非遞迴）掃描，子資料夾內檔案自動排除於 DB、`pipeline/data/*.json` 與網站之外；原始 `.md` 完整保留於 repo，日後移回即復原。

**隱藏條目（移入 `wiki/_hidden/`）**：
- `baby-luna-2022-06-17.md` — Baby 赤ちゃん，存活 13 天（周南市徳山動物園）
- `baby-kiku-2021-06-10.md` — Baby 赤ちゃん，存活 48 天（よこはま動物園ズーラシア）
- `wu-tan-2018-06-21.md` — Wu-Tan ウータン，存活 38 天（京都市動物園）
- `takeru-2015-07-29.md` — Takeru タケル，存活 141 天（静岡市立日本平動物園）
- `tsubasa-2017-07-08.md` — Tsubasa つばさ，存活 208 天（熱川バナナワニ園）

**連動更新**：
- 30 個相關條目：將指向上述 5 隻的 `[[wikilink]]` 改為純文字（避免 Obsidian 斷連、網站家系少列該子女）
- `index.md` — 移除該 5 列；條目總數 468 → 463（`_hidden/` 不計入）

**備注**：`_hidden/` 內檔案若要一併從 Obsidian 檔案總管／搜尋隱藏，可於 Obsidian 設定 → 檔案與連結 → 排除的檔案 加入 `_hidden/`（未代改 `.obsidian/`）。重建：`build_db` + `export_json`（未跑 gen_residence，因無居住史異動）。

## [2026-07-02] update | kodama/kagayaki 補註三胞胎第三隻已隱藏

在 `kodama-2017-07-08.md`、`kagayaki-2017-07-08.md` 的「三胞胎」欄補一句說明：第三隻 Tsubasa 幼逝、條目暫存 `wiki/_hidden/`，故 check_twins 的「W2b：3 胞胎僅 2 隻」屬刻意隱藏、非漏連。純文字註記、不影響 DB/網站；check_twins 仍為 0 錯誤 2 警告（不阻擋）。

## [2026-07-02] add | 新增香港海洋公園個體 Tai-Shan（泰山）

依讀者提供的 RPF #930 建立條目。Tai-Shan（泰山）♂、styani、2008-06-14 生於成都大熊貓繁育研究基地，2009-03-22 移居香港海洋公園至今。RPF 家族頁標記 🚧、未收錄父母／雙胞胎／子女，故本次僅建主角一筆、無親屬補建。香港海洋公園原已登記於 `data/zoos.json`（本次順手補齊其 `zh`＝香港海洋公園、`location_ja`＝香港南区黄竹坑）。

**來源**：
- https://redpandafinder.com/#profile/930 (Tai-Shan 泰山)

**新增條目**：
- `tai-shan-2008-06-14.md` — Tai-Shan 泰山（RPF #930），♂，生於 2008-06-14（成都大熊貓繁育研究基地），現居香港海洋公園

**更新條目**：
- `data/zoos.json` — 補齊 Ocean Park Hong Kong 的 `zh`／`location_ja`／`location_en`
- `index.md` — 新增「海外個體（香港）」小節；條目總數更新為 464

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-02] add | 新增心心（シンシン #801）及其母遊優、三胞胎優貴、½ 兄トクトク

讀者提供多摩動物公園官方新聞稿（2008 交換、2009 移出）與 4travel 旅行記（官方轉載性質之目擊記錄），官方來源可直接採用；並與 redpanda-lineage 比對一致。`hei` 條目原「子女（母不詳）」三隻（#202/#452/#801）之母確認為遊優（#373）。

**來源**：
- https://redpandafinder.com/#profile/801 (Shin-Shin 心心)
- https://redpandafinder.com/#profile/373 (You-You 遊優)
- https://redpandafinder.com/#profile/452 (Yuuki 優貴)
- https://redpandafinder.com/#profile/596 (Toku-Toku)
- https://www.tokyo-zoo.net/topics/news/tama/7509_9215_2008-05-23.html （官方：徳山⇔多摩交換，載明母遊優、父平）
- https://www.tokyo-zoo.net/topics/news/tama/6913_12692_2009-10-10.html （官方：2009-10-20 移ひらかたパーク）
- https://4travel.jp/travelogue/10738421 （2012-12-11 ひらかた→宮崎、與スイカ對調）
- https://4travel.jp/travelogue/10781265 （2013-04-07 歿）

**新增條目**：
- `shin-shin-2003-07-15.md` — Shin-Shin 心心 シンシン（RPF #801），♂🌈，生於 2003-07-15 徳山動物園，2008-05-28 移多摩（與コタロウ交換）、2009-10-20 移ひらかたパーク、2012-12-11 移宮崎市フェニックス自然動物園，2013-04-07 歿（9 歲）
- `you-you-1994-07-04.md` — You-You 遊優 ユウユウ（RPF #373），♀🌈，生於 1994-07-04 ひらかたパーク，2000-02-14 移徳山，2011-07-12 歿；五子之母
- `yuuki-2003-07-15.md` — Yuuki 優貴 ユーキ（RPF #452），♂🌈，`shin-shin` `kou-kou` 三胞胎，2005-07-08 移阿根廷 Buenos Aires Eco-Park，2019-07-01 歿
- `toku-toku-2001-07-21.md` — Toku-Toku トクトク（RPF #596），♂🌈，`shuu-shuu` 雙胞胎（母遊優 × 父 Chou-Chou #886），2004-05-20 移池田動物園，2008-02-04 歿；Shun-Shun #597 之父

**更新條目**：
- `hei-1995-07-18.md` — 「子女（母不詳）」改為「與遊優所生三胞胎」並補 wikilink
- `kou-kou-2003-07-15.md` — 母／父／三胞胎／`toku-toku` 補 wikilink
- `shuu-shuu-2001-07-21.md` — 母／雙胞胎補 wikilink、補 ½ 弟三胞胎
- `you-you-1997-06-20.md`、`you-you-2002-06-21.md` — 同名注意補 #373
- `shin-shin-1986.md`、`shin-shin-2000-06-30.md`、`shin-shin-2010-06-24.md` — 同名注意補齊四隻互列
- `yuuki-2013-07-04.md` — 新增同名注意（#452）
- `index.md` — 新增「Shin-Shin 心心家族」段；條目總數更新為 468
- `data/zoos.json` — Buenos Aires Eco-Park 補 `location_ja`＝布宜諾斯艾利斯（原為空白）
- `tools/gen_residence.py` — CFLAG 補 Argentina 🇦🇷／Hong Kong 🇭🇰；`location_ja` 已含國名時不重複前綴（修 `tai-shan` 居住史「香港 香港南区黄竹坑」重複）

**重建**：`gen_residence` + `build_db`（/tmp shim）+ `export_json`；`audit --strict`＝0 錯誤、`check_twins`＝0 錯誤 2 既知警告

## [2026-07-02] add | 新增暢暢（Chuihowa 菊花 #206）及其 6 隻手足

讀者提供 RPF profile 連結，建立 `yueshi-1999-07-08` × `ten-ten-1997-06-18` 之女 Chuihowa（菊花），並依 skill 補齊尚無條目的 6 隻手足。父母（遊優之外的月食 Yueshi、Ten-Ten）與 3 隻手足（Tashan、Xianchi、Shiryu）原已存在。父方半血緣手足之母為 Rishi（日食，Yueshi 雙胞胎）。多為移居海外之個體。

**來源**：
- https://redpandafinder.com/#profile/206 (Chuihowa 菊花)
- https://redpandafinder.com/#profile/858 (Shaoen 小燕)
- https://redpandafinder.com/#profile/353 (Rouge)
- https://redpandafinder.com/#profile/354 (Tarrei 稲妻)
- https://redpandafinder.com/#profile/356 (Shi-Ren 詩人)
- https://redpandafinder.com/#profile/355 (Foa-Foa)
- https://redpandafinder.com/#profile/405 (Shan-Tou)

**新增條目**：
- `chuihowa-2010-07-10.md` — Chuihowa 菊花 チュイホワ（RPF #206），♀，生於 2010-07-10，現居東北サファリパーク
- `shaoen-2002-06-20.md` — Shaoen 小燕 シャオエン（RPF #858），♂🌈，2002-06-20 – 2008-12-31，`rouge` 雙胞胎；2008 移ソウル大公園動物園歿
- `rouge-2002-06-20.md` — Rouge ルージュ／チャーファ（RPF #353），♀🌈，2002-06-20 – 2019-12-30，`shaoen` 雙胞胎；2004 移加拿大 Assiniboine Park Zoo
- `tarrei-2002-07-01.md` — Tarrei 稲妻 ターレイ（RPF #354），♂🌈，2002-07-01 – 2021-12-20，`tashan` 雙胞胎；歷辛辛那提／Lincoln Park／Henry Vilas Zoo
- `shi-ren-2004-06-29.md` — Shi-Ren 詩人 シーレン（RPF #356），♂，生於 2004-06-29，`foa-foa` 雙胞胎；現居那須ワールドモンキーパーク
- `foa-foa-2004-06-29.md` — Foa-Foa ファーファ（RPF #355），♀🌈，2004-06-29 – 2022-07-29，`shi-ren` 雙胞胎；2008 移ソウル大公園動物園歿
- `shan-tou-2005-05-10.md` — Shan-Tou シャントゥ／リーファ（RPF #405），♀🌈，2005-05-10 – 2015-11-12；2007 移 Red River Zoo（別名 Rifa，勿與 `rifa` 混淆）

**更新條目**：
- `yueshi-1999-07-08.md` — 子女表補 `tarrei`／`shi-ren`／`foa-foa`／`chuihowa` wikilink、父欄補 Ten-Ten
- `rishi-1999-07-08.md` — 補子女 `shaoen`／`rouge`／`shan-tou` wikilink
- `tashan-2002-07-01.md` — 雙胞胎 `tarrei` 及同父母／半血緣手足補 wikilink
- `index.md` — 新增 7 筆；條目總數更新為 475

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-02] fix | 結構稽核修正：slug 消歧、log wikilink 清除

專案結構稽核後修正三處明顯問題（不涉資料內容變更，僅命名／格式規範）。

**更新條目**：
- `hana.md` → `hana-2023.md` — 依「名字-生日」規則改名（born 2023）；補 `species: Ailurus fulgens`；內文與 `index.md` 的 `[[hana]]`／`[[hashi]]` 參照改為 `[[hana-2023]]`／`[[hashi-2022]]`；加「⚠️ 注意同名」提示（另有 `hana-2001-07-13`／`hana-2005-06-21`）
- `hashi.md` → `hashi-2022.md` — 同上改名（born 2022）、補 `species`、修參照
- `index.md` — 更新 `hana`／`hashi` 兩列 wikilink 為新 slug
- `log.md` — 清除 3 處未包 backtick 的示意／記錄用 `[[...]]`（行 2295／2399／2987），避免污染 Obsidian graph

**備註**：`shan-tou-2005-05-10` 原為 dangling link，本次稽核時該條目已存在（作者先前補齊 Chuihowa 家族批次），dangling 現為 0。

## [2026-07-02] update | 讀者回報：蘭々／光々歿日補入（RPF 佐證，待官方確認）

Tally 資料更正表單 2 筆回報（回報者 `A`，2026-07-02），皆為過世回報、來源 Red Panda Finder。與 redpanda-lineage 核對一致，屬「補空白」（原歿日皆待查證），依保守原則補入並保留 🚧 待官方來源確認註記。

**來源**：
- Tally 回報 RWYqALJ／jeW8jkY（小熊貓資料回報收件匣）
- https://redpandafinder.com/#profile/551 (Ran-Ran)
- https://redpandafinder.com/#profile/549 (Kou-Kou)

**更新條目**：
- `ran-ran-1998-06-29.md` — 補 `died: 1999-07-20`（歿於多摩動物公園，得年 1 歲）；zoos 訖日、deceased tag、標題加 🌈；未見於多摩官方名單之待查證註記保留
- `kou-kou-1997-06-20.md` — 補 `died: 2000-01-28`；居住史補 1999-12-03 移居釧路市動物園（lineage location.2），歿於釧路
- `fu-fu-1997-06-20.md`／`nene-1993-07-11.md`／`ryu-ryu-1990.md`／`tan-tan-1998-06-29.md`／`index.md` — `ran-ran` 參照加 🌈；index 年份改 1998–1999

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-02] add | 圖鑑缺漏回報：Drusillas Park 一家（英國）＋搜尋別名補強

處理「圖鑑缺漏」收件匣 5 筆回報。缺園回報 drusillas park（園已在註冊表，缺的是個體條目）：據 RPF 與 Drusillas 園方官網新聞稿建立 5 條目（官方來源可直採）。另 2 筆搜尋別名建議直接補入 frontmatter；1 筆網站功能建議記入 ROADMAP；佑佑（銀基動物王國）標保留待確認。

**來源**：
- https://redpandafinder.com/#profile/1169 (Mulan)
- https://redpandafinder.com/#profile/1170 (Maja)
- https://www.drusillas.co.uk/news/panda-pair-arrive-at-zoo-in-sussex （Tibao/Mulan 抵園）
- https://www.drusillas.co.uk/news/new-year-brings-new-red-panda-to-the-zoo （Tibao 來歷）
- https://www.drusillas.co.uk/news/red-pandas-babies-are-named-at-drusillas （Mya/Anmar 命名、父母）
- https://www.drusillas.co.uk/red-panda-joins-pack （Maja 抵園）

**新增條目**：
- `mulan-2012-07-09.md` — Mulan ムーラン（RPF #1169），♀，生於 2012-07-09 Paignton Zoo，2013-03 移居 Drusillas Park；⚠️ 與 `mulan-2019-06-07`（東北サファリ）同名互註
- `maja.md` — Maja マージャ（RPF #1170），♂，生日不詳，約 2020 自匈牙利抵 Drusillas Park（🚧 抵園年依 RPF 收錄時間推定）
- `tibao-2011.md` — Tibao，♂，約 2011 生（依園方報導 18 個月大推算），2012-07 自法國 Asson Zoo 抵 Drusillas；Mya/Anmar 之父；後續去向待查證（zoos 暫留空）
- `mya-2014-06-16.md` — Mya，♀，2014-06-16 生於 Drusillas（該園首胎），`mulan`×`tibao` 之女；去向待查證
- `anmar-2014-06-16.md` — Anmar，♂，`mya` 雙胞胎；去向待查證

**更新條目**：
- `tian-2011.md` — japanese 補「ティエン」（讀者回報：八木山の天希望能以ティエン搜尋）
- `himawari-2017-07-13.md` — japanese 補片假名「ヒマワリ」（讀者回報：多摩ヒマワリ原僅平假名可搜）
- `mulan-2019-06-07.md` — 加 ⚠️ 注意同名（新增英國 Mulan）
- `index.md` — 新增「海外個體（英國・Drusillas Park）」段落；條目總數更新為 480
- `ROADMAP.md` — 願望池新增「動物園篩選納入曾居／已逝個體」（讀者回報，Aoi Ajisai）

**保留待確認**：
- 佑佑（銀基動物王國，河南鄭州）— 回報來源為 YouTube short（非官方）；媒體報導可佐證該園有小熊貓（佑佑、貝貝等 6 隻），但無生日／個體資料、園未登記註冊表，暫不建檔，待作者定奪

**重建**：`gen_residence` + `build_db` + `export_json`

---

## [2026-07-03] add | 讀者回報補建 `kaguya`（多摩・上海生，官方來源查證）

**來源**：
- https://www.tokyo-zoo.net/topics/news/tama/5349_21451_2013-03-21.html （多摩動物公園官方訃報：性別・生日・上海生・野毛山來園・心不全歿）
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php （野毛山動物園官方部落格：2001 年上海一對「きんた・かぐや」來園）
- 讀者回報（圖鑑缺漏收件匣，回報者：楊桃）

**新增條目**：
- `kaguya-2000-06-29.md` — Kaguya カグヤ／かぐや，♀🌈，生於 2000-06-29 上海動物園，2001 與 `kinta` 同批來日野毛山，2004-04-12 移多摩動物公園，2013-03-21 心不全歿（享年 12 歲 8 個月）；父母不詳、無 RPF

**更新條目**：
- `kinta-2000-06-08.md` — 家族欄補「同批來日」`kaguya` 交叉連結（2001 年一同自上海來野毛山）
- `index.md` — 於 `kinta` 後新增 `kaguya` 一列；條目總數更新為 481

**備注**：官方來源（多摩・野毛山）可直接採用；`kaguya` 與 `kinta` 為同批送來、外觀酷似，但親緣關係官方未載，暫不視為手足。

**重建**：`gen_residence` + `build_db` + `export_json`

---

## [2026-07-03] add | 新增 `carson`（森林公園動物園，RPF #311）

**來源**：
- https://redpandafinder.com/#profile/311 (Carson)

**新增條目**：
- `carson-2014-07-01.md` — Carson カーソン（RPF #311），♂，Ailurus fulgens fulgens，生於 2014-07-01 Lincoln Children's Zoo，2016-02-17 起現居森林公園動物園（Woodland Park Zoo，西雅圖）；母 `sophia`🌈（#528）、父 `duli`（#526）、雙胞胎 `willa`🌈（#527）；另有 10 半血緣手足（僅內文列出，未建條目）；IG @carsontheredpanda

**更新條目**：
- `index.md` — 「海外個體（美國）」新增 `carson` 一列；條目總數更新為 482

**備注**：依使用者要求僅補 Carson 本人。父母、雙胞胎與半手足多為北美個體、涉及數座尚未登記於 `data/zoos.json` 的美國動物園（如 Zoo Montana 已在、但 Denver／Mill Mountain／Zoo Knoxville／Franklin Park／Toledo／Charles Paddock／Chattanooga 等未登記），故暫以內文文字記錄，待需要時再建檔並登記園名。

**重建**：`gen_residence` + `build_db` + `export_json`

---

## [2026-07-03] add | 補建 `carson` 的父母與雙胞胎（Lincoln Children's Zoo 一脈，RPF #526/#527/#528）

**來源**：
- https://redpandafinder.com/#profile/528 (Sophia，母)
- https://redpandafinder.com/#profile/526 (Duli，父)
- https://redpandafinder.com/#profile/527 (Willa，雙胞胎)

**新增條目**：
- `sophia-2002-06-20.md` — Sophia ソフィア（RPF #528），♀🌈，fulgens，2002-06-20 生於 Zoo Knoxville、2019-10-01 歿於 Lincoln Children's Zoo；`carson`・`willa` 之母、`duli` 配偶（Zoo Knoxville→Mill Mountain→Denver→Lincoln）
- `duli-2011-07-05.md` — Duli ドゥリ（RPF #526），♂，fulgens，2011-07-05 生於 Franklin Park Zoo，現居 Zoo Montana；`carson`・`willa` 之父、`sophia` 配偶（Franklin Park→Lincoln→Zoo Montana）
- `willa-2014-07-01.md` — Willa ウィラ（RPF #527），♀🌈，fulgens，2014-07-01 生於 Lincoln、2025-06-18 歿於 Chattanooga Zoo；`carson` 之雙胞胎姊妹（Lincoln→Toledo→Charles Paddock→Chattanooga）

**更新條目**：
- `carson-2014-07-01.md` — 父母・雙胞胎由純文字改為 `sophia`／`duli`／`willa` wiki 連結；備注更新（父母＋雙胞胎已建檔，10 半手足仍未建）
- `index.md` — 「海外個體（美國）」新增「Carson 一家（Lincoln Children's Zoo 一脈）」子區塊（4 筆）；條目總數更新為 485

**備注**：8 座相關美國動物園（Zoo Knoxville／Mill Mountain／Denver／Lincoln Children's／Franklin Park／Zoo Montana／Toledo／Charles Paddock／Chattanooga）皆已在 `data/zoos.json` 註冊，未新增園。10 隻半血緣手足暫未建檔。

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-03] update | 照片投稿：`chen-chen-2022-07-05` 補 1 筆 IG 連結

作者直接提供（網友 `r.star.bao` 投稿），寫入 frontmatter `instagram:`，採含帳號完整形式（佔位卡可顯示 @署名）。

**來源**：
- https://www.instagram.com/r.star.bao/p/DaSqFy8AckC/

**更新條目**：
- `chen-chen-2022-07-05.md` — 茜茜（RPF #1370）`instagram:` +1（共 2 筆）
- 重建 `redpanda.db` 與 `pipeline/data/*.json`

## [2026-07-04] update | 回報查證：修正網站誤把 `ron-ron-2002-06-28` 列為 `umi-2002-06-24` 之父

讀者（楊桃）回報：海（2002-06-24 生）之父不可能是 2002-06-28 生的 Ron-Ron。查證結果：wiki 內文本已注明兩者為不同個體，但「父」行的消歧注記含 `[[wikilink]]`、又未帶 build_db 認得的警語字樣，被誤抓成親子邊，導致網站顯示錯誤父親。

**修正**：
- `umi-2002-06-24.md` — 「父」行消歧注記改為「⚠️ …為不同個體，勿混淆」格式，讓 build_db 警語防護正確切掉
- `tools/build_db.py` — `WARNING_RE` 增列「不同個體」，防止未來同型誤抓
- 重建後確認 `family.json` 已無 `umi-2002-06-24 → ron-ron-2002-06-28` 假邊；audit --strict、check_twins 均通過

**待作者裁定（同批回報，來源非官方或無法開啟，未採用）**：
- `ten-ten-1997-06-18` 轉入東北サファリパーク精確日 1999-12-28（來源：mamepandaworld fc2 部落格，無法開啟核對）
- `ron-ron-2002-06-28` 轉入東北サファリパーク精確日 2010-11-28（4travel 遊記可證「2010 年 11 月」，精確日僅見於同一 fc2 部落格）

**重建**：`build_db`（/tmp shim）+ `export_json`（未動 zoos:，免跑 gen_residence）

## [2026-07-04] update | 照片投稿回填：`futa-2003-07-05` +1、`yaffa-2015-06-22` +2

photo-inbox-audit 比對收件匣 11 筆新投稿：9 筆 wiki 已有（僅待標 I 欄）、2 slug 共 3 連結乾淨待補，已回填 `instagram:` frontmatter；無異常、無缺檔、無資料問題。

**來源**：
- https://www.instagram.com/p/CuanKstheGA/ (Futa，投稿 Z9Y4Yo0，已獲原作者同意)
- https://www.instagram.com/p/DaAZewBPvt2/ (Yaffa，投稿 rDdyVg2，本人)
- https://www.instagram.com/p/DaANg5dRlnt/ (Yaffa，投稿 rDdyVg2，本人)

**更新條目**：
- `futa-2003-07-05.md` — 風太 `instagram:` +1（共 3 筆）
- `yaffa-2015-06-22.md` — `instagram:` +2（共 9 筆）
- 重建 `redpanda.db`（/tmp shim）與 `pipeline/data/*.json`；`ig_audit` 無重複、無錯誤

## [2026-07-04] update | 採用回報：`ron-ron-2002-06-28`、`ten-ten-1997-06-18` 轉入東北サファリパーク精確日

作者確認 mamepandaworld 部落格照片為園內製作之家系圖（官方資訊之忠實轉載），前一筆「待裁定」兩項改為採用（回報者：楊桃）。

**來源**：
- https://mamepandaworld.blog.fc2.com/blog-entry-1311.html (園內家系圖照片)
- https://4travel.jp/travelogue/10756505 (Ron-Ron 2010 年 11 月到園佐證)

**更新條目**：
- `ron-ron-2002-06-28.md` — `zoos:` 精確化：とべ (2002-06-28 – 2010-11-28)、東北サファリ (2010-11-28 – 2021-12-13)；sources +2
- `ten-ten-1997-06-18.md` — `zoos:` 精確化：茶臼山 (1997-06-18 – 1999-12-28)、東北サファリ (1999-12-28 – 2016-07-21)；sources +2
- 重建 `redpanda.db`（/tmp shim）與 `pipeline/data/*.json`；audit --strict 通過

## [2026-07-04] update | 動物園註冊表：中山市紫馬嶺動物園升級校訂

依使用者提供資料，把 lineage 帶入的殘缺條目 `Zhongshan ZiMaLing Zoo`（lineage #300）升級為校訂版。園方無官網（以微信公眾號為主要管道），`website` 留空。

**來源**：
- https://baike.baidu.com/item/中山市紫马岭动物园/22463975 (百度百科，參考)
- 使用者提供地址：广东省中山市 紫马岭公园（西南側）

**更新條目**：
- `data/zoos.json` — canonical＝中山市紫馬嶺動物園、en＝Zhongshan Zimaling Zoo、zh＝中山市紫马岭动物园、location_ja＝広東省中山市東区；舊英文名與繁簡別名全數入 aliases。座標與 map 沿用 lineage 值；新增選填欄位 `wechat`＝中山市紫马岭动物园（無官網之官方管道，經作者同意新設此欄位）。尚無條目引用此園，未重建亦不影響現有資料（build_db 已驗證通過）。

## [2026-07-04] add | 採用回報（楊桃）：新增 タラ・チャチャ・ソラ・アイ 四筆缺漏個體

讀者（楊桃，同批「沒看到小熊貓」回報）回報 タラ・チャチャ・ソラ 三筆均附來源，另一筆 アイ（上野）未附來源但經同批官方新聞查得，一併建檔。

**來源**：
- https://www.tokyo-zoo.net/topics/news/ueno/8737_269_2003-01-31.html (官方：タラ・ハナ 2003-01-27 隨リンリン贈往墨西哥)
- https://www.zenryoku.net/tokyo/20030125160745/ (都議活動報告：タラ 雄、時年 7 歲)
- https://kosaru323.blog.fc2.com/blog-entry-563.html (愛好者整理釧路開園 40 周年記念誌《あゆみ》：タラ 1995-07-04 生、父サバタロウ × 母あゆみ、2001 移上野)
- https://www.tokyo-zoo.net/topics/news/ueno/8197_4316_2006-04-21.html (官方：チャチャ 1992-07 徳山生・宝塚育・2003-04 來上野；アイ 1991-06 池田動物園生・安佐育・2001-02 來上野)
- https://www.tokyo-zoo.net/topics/events/ueno/3117_15855_2010-09-10.html (官方：チャチャ上野來園日 2003-04-17)
- https://www.tokyo-zoo.net/topics/news/ueno/6257_18037_2011-04-09.html (官方追悼文：チャチャ 2011-03-25 老衰歿、アイ 2009 老衰歿)
- https://popncall.com/jp/photos/takarazuka/takarazuka.html (宝塚ファミリーランド 2003-04-07 閉園、園內小熊貓移往上野・徳島)
- https://omutacityzoo.org/news/?p=3734 (官方：ソラ 2002-06-24 生、2007-03-23 來園、2022-04-06 惡性腫瘍轉移歿)
- https://4travel.jp/travelogue/10886326 (海＆ソラ雙胞胎、群馬サファリパーク出生佐證)

**新增條目**：
- `tara-1995-07-04.md` — タラ ♂，生於釧路市動物園（`ikura`・`cha` 之兄），2001 移上野，2003-01-27 與 `hana`（#308）贈往墨西哥チャプルテペック動物園（現況待查，比照 `hana` 不標歿）；生日精確日 1995-07-04 依愛好者考據 🚧 待查證
- `cha-cha-1992-07-17.md` — チャチャ ♂，徳山生、宝塚ファミリーランド育、2003-04-17 來上野，2011-03-25 老衰歿（享年 18 歲 8 個月）；生日精確日 7/17 依回報 🚧 待查證（官方僅記 1992 年 7 月）
- `sora-2002-06-24.md` — ソラ ♀，群馬サファリパーク生、`umi`（海）之雙胞胎妹，2007-03-23 移大牟田市動物園，2022-04-06 歿（享年 19 歲）
- `ai-1991.md` — アイ ♀，1991-06 池田動物園生、安佐育、2001-02 來上野，2009 老衰歿（生歿精確日不詳）

**更新條目**：
- `umi-2002-06-24.md` — 雙胞胎 `sora` 由純文字改為連結
- `ikura-1996-07-09.md`・`cha-1997-07-27.md` — 手足列具名：`tara` 連結、マリモ（1995，タラ雙胞胎）、クロ（1997，チャ雙胞胎）
- `hana-2001-07-13.md` — 內文 タラ 補連結
- `data/zoos.json` — 新增 宝塚ファミリーランド（兵庫県宝塚市，2003-04-07 閉園）；園數 → 335
- `index.md` — Ikura 一脈補 `tara`；Kiku 祖父母表補 `sora`；新增「恩賜上野動物園 パンダ舎個體」區塊（`ai`・`cha-cha` 1992）；條目總數 +4（同日另有 `bagel` 條目，合計 490）

**回報值與官方不符處（已依官方）**：チャチャ上野來園日回報 2003-04-07，官方記 2003-04-17（4/7 實為宝塚閉園日）。**僅記內文未建檔**：タラ父母 サバタロウ・あゆみ、手足 マリモ・クロ（愛好者考據）。

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] add | 貝果（中山市紫馬嶺動物園首筆條目）

依使用者提供資料建檔（♀、2024-07-12 生），官方來源為中山日報「中山Plus」一歲生日報導（園方發布消息之官方轉載），生日與使用者所述吻合。羅馬化名經作者確認採 `Bagel`（依名字含義，同 `canele` 前例）。無 RPF 條目。出生地推測園內（待查證）、父母待確認。

**來源**：
- https://zsrbapp.zsnews.cn/home/content/newsContent/532/676560 (中山日報・中山Plus 生日報導)
- https://m.sohu.com/a/912632157_120046696 (搜狐轉載生日活動報導)

**新增條目**：
- `bagel-2024-07-12.md` — 貝果 Bagel（無 RPF），生於 2024-07-12，現居 中山市紫馬嶺動物園；園內共 5 隻小熊貓、其為人氣明星

**更新條目**：
- `index.md` — 新增分類「海外個體（中國・中山市紫馬嶺動物園）」；條目總數依實際檔數校正為 490（作者同時段亦在新增條目）

## [2026-07-04] add | 廣州動物園升級校訂＋新增野生救護個體 霈霈

依使用者提供資料：升級 lineage 帶入的殘缺園條目 `Guangzhou Zoo`（lineage #297），並新增園內野生救護個體 `pei-pei`（霈霈）。lineage 廣州動物園既有 8 隻（xixi、kangkang、duoduo 等）均無霈霈，故無 RPF 資料。

**來源**：
- 使用者提供：廣州動物園地址 广东省广州市越秀区先烈中路120号（邮编 510070）；霈霈 ♀、野生救護、生日不詳
- https://www.gzzoo.com/ (官網，JS 渲染)

**新增條目**：
- `pei-pei.md` — 霈霈 Pei Pei，♀，野生救護個體，生日不詳，現居廣州動物園；出生年／救護／入園時間均 🚧 待查證。slug 例外不帶生日（生年連估計值都無，經作者確認），日後查得估計生年再更名 `pei-pei-YYYY`

**更新條目**：
- `data/zoos.json` — canonical＝廣州動物園、en＝Guangzhou Zoo、zh＝广州动物园、location_ja＝広東省広州市越秀区；website 由 service.aspx 改為根網址；舊英文 canonical 與繁簡名入 aliases
- `index.md` — 新增「海外個體（中國・廣州動物園）」區塊；條目總數 490 → 491

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] update | 註冊表新增 上海野生動物園

依使用者提供官網新增動物園註冊資料。與既有 `上海動物園`（長寧区）為不同園。

**來源**：
- https://www.swap-shendi.com/ (官網；地址 上海市浦东新区南六公路178号，電話 021-58036000)

**更新條目**：
- `data/zoos.json` — 新增 canonical＝上海野生動物園、en＝Shanghai Wild Animal Park、zh＝上海野生动物园、location_ja＝上海市浦東新区、website＝官網；座標為近似值。lineage 無此園（lineage_id null）；園數 → 336

## [2026-07-04] add | 新增上海動物園個體 高高、阿扁

依作者提供資料新增兩隻上海動物園現居個體。兩隻同為 2020-07-06 生，是否同胎待查證（作者確認暫不標同胎）。非 RPF 收錄個體，略過 `rpf_id`／`rpf_url`。

**來源**：
- 作者提供（高高 ♀ 2020-07-06、阿扁 ♀ 2020-07-06）
- http://www.shanghaizoo.cn/ (上海動物園)

**新增條目**：
- `gao-gao-2020-07-06.md` — 高高 Gao Gao（♀，無 RPF），生於 2020-07-06，現居 上海動物園；父母待查證
- `a-bian-2020-07-06.md` — 阿扁 A Bian（♀，無 RPF），生於 2020-07-06，現居 上海動物園；父母待查證

**更新條目**：
- `index.md` — 「海外個體（中國・上海動物園）」新增 `gao-gao`、`a-bian`；條目總數更新為 493
- `gao-gao-2015-06-27.md` — 加「⚠️ 注意同名」提示（與上海 `gao-gao-2020-07-06` 同名並存）

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] fix | 網站居住史排序：起年不明的居所被排到最前

讀者頁 `cha-cha-1992-07-17` 居住史順序錯誤（宝塚ファミリーランド排在出生地徳山之前）。原因：`export_json.py` 以 `ORDER BY slug, start_year, id` 排序，「起不明、訖已知」（如宝塚 `( – 2003-04-07)`）的 `start_year` 為 NULL，SQLite 將 NULL 排最前。

**修正**：
- `pipeline/scripts/export_json.py` — 排序改為 `ORDER BY slug, COALESCE(start_year, end_year), id`；起年不明者以訖年定位
- 受影響條目僅 `cha-cha-1992-07-17`（徳山→宝塚→上野 ✅）與 `ai-1991`（池田→安佐→上野 ✅）；其餘 6 筆 NULL-start 均為單一居住地、不受影響
- 重跑 `export_json` 更新 `pipeline/data/*.json`

## [2026-07-04] add | 上海野生動物園個體 毛毛

依使用者提供資料新增上海野生動物園個體 `mao-mao`（毛毛）。除名字、性別、現居園外均不詳，比照 `pei-pei` 前例 slug 例外不帶生日。

**來源**：
- 作者提供（2026-07-04；官方來源待補）

**新增條目**：
- `mao-mao.md` — 毛毛 Mao Mao，♀，生日／出身／入園時間均不詳 🚧 待查證，現居上海野生動物園；日後查得生年再更名 `mao-mao-YYYY`

**更新條目**：
- `index.md` — 新增「海外個體（中國・上海野生動物園）」區塊；條目總數依實數校正 493 → 495（含並行新增）

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] update | チャチャ補齊 RPF #889：徳山訖日、宝塚起日、雙胞胎タンタン建檔

讀者指出網站 `cha-cha-1992-07-17` 居住史仍顯示「徳山 1992-07-17 ~ 現在」，並提供 RPF 徳山段（1992-07-17 – 1994-03-13）。查 redpanda-lineage 發現チャチャ其實有收錄（RPF #889，先前未查到），生日 1992-07-17、上野來園 2003-04-17 均與官方吻合；一併帶出雙胞胎タンタン（RPF #888）。

**來源**：
- https://redpandafinder.com/#profile/889 (チャチャ：徳山 1992-07-17 – 1994-03-13、1994-03-13 移往 unknown＝宝塚、上野 2003-04-17)
- https://redpandafinder.com/#profile/888 (タンタン：チャチャ雙胞胎，1994-03-19 移居到津，1997-01-28 歿)

**新增條目**：
- `tan-tan-1992-07-17.md` — タンタン ♂（RPF #888），チャチャ雙胞胎，生於徳山，1994-03-19 移居到津遊園（今到津の森公園），1997-01-28 歿（⚠️ 與淡々 #379 同名）

**更新條目**：
- `cha-cha-1992-07-17.md` — 補 rpf_id 889；`zoos:` 徳山訖日 1994-03-13、宝塚起日 1994-03-13；生日 7/17 註記由「待查證」改為 RPF 佐證；補雙胞胎連結
- `tan-tan-1998-06-29.md` — 補 ⚠️ 同名注記（タンタン #888）
- `index.md` — パンダ舎區塊補 `tan-tan-1992-07-17` 列與 RPF 編號
- `web/src/components/Panda.astro`・`Zoo.astro` — 訖日缺值只在「最後一段居所且在世」顯示「現在」，中途段（如 `ai-1991` 池田→安佐轉園日不明）顯示「?」

**重建**：`build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins 通過（雙胞胎 +1 組）

## [2026-07-04] add | 上海野生動物園個體 希希

依使用者提供資料新增上海野生動物園個體 `xi-xi-2023-07-01`（希希）。

**來源**：
- 作者提供（2026-07-04；官方來源待補）

**新增條目**：
- `xi-xi-2023-07-01.md` — 希希 Xi Xi，生於 2023-07-01，性別待確認（依規範 sex 留空、不加性別 tag），出生地／父母 🚧 待查證，現居上海野生動物園

**更新條目**：
- `index.md` — 「海外個體（中國・上海野生動物園）」區塊補 希希；條目總數 495 → 496

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] add | 上海動物園 富富・美美（壯壯 × 妞妞 之女，雙胞胎）

依使用者提供資料新增上海動物園雙胞胎姊妹 `fu-fu-2023-06-24`・`mei-mei-2023-06-24`，父 `zhuang-zhuang`（壯壯）× 母 `niu-niu`（妞妞），為 `tian-tian-2024-06-23`（甜甜）之姊。

**來源**：
- 作者提供（2026-07-04；官方來源待補）

**新增條目**：
- `fu-fu-2023-06-24.md` — 富富 Fu Fu，♀，2023-06-24 生於上海動物園，與美美雙胞胎；⚠️ 同名注意（另有 1997、2014 兩隻 Fu Fu）
- `mei-mei-2023-06-24.md` — 美美 Mei Mei，♀，2023-06-24 生於上海動物園，與富富雙胞胎；⚠️ 同名注意（另有 1999、2007 兩隻 Mei Mei）

**更新條目**：
- `zhuang-zhuang.md`・`niu-niu.md` — 子女表補 富富・美美
- `tian-tian-2024-06-23.md` — 新增兄弟姊妹段（富富・美美）
- `index.md` — 「海外個體（中國・上海動物園）」補兩筆；條目總數依實數校正 496 → 498（含並行新增）

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] update | タラ標記已歿（歿日待查證）：`tara-1995-07-04`

作者確認タラ應已過世，要求查證。查得：redpanda-lineage 收錄タラ為チャプルテペック動物園無名個體 #728（♂，1995-07-04 生於釧路、2001 移上野、2003-01-27 移墨西哥；death 欄 unknown）；生於 1995 年，以小熊貓壽命（約 15、最長約 19 年）推算現已確定過世。惟查無官方指名之歿日。Sopitas 動物園死亡回顧載「2011 年 3 月チャプルテペック一隻小熊貓因心臟衰竭死亡」，當時該園小熊貓僅タラ與 `hana`（#308）兩隻，該筆可能為其一，但報導未指名、ハナ亦為候選，故**不逕採為タラ歿日**（作者裁定：標歿、日期待查證）。

**來源**：
- https://redpandafinder.com/#profile/728 (タラ＝無名 #728：釧路→上野 2001-01-16→チャプルテペック 2003-01-27)
- https://www.sopitas.com/noticias/recuento-especies-muertas-zoologico-chapultepec/ (2011-03 チャプルテペック小熊貓因心衰死亡，未指名個體)

**更新條目**：
- `tara-1995-07-04.md` — 加 `died: "?"`（歿日不詳 sentinel；網站顯示「逝世：? 🌈」、居住史尾段顯示「? 」而非「現在」、時間軸／壽命統計優雅退場）；tags +deceased；標題／引言加 🌈；補歿日待查證說明與 2011-03 線索、RPF #728；sources +2
- `ikura-1996-07-09.md`・`cha-1997-07-27.md`・`hana-2001-07-13.md`・`index.md` — タラ提及處補 🌈；index 生卒改「1995–? 🌈」

**重建**：`gen_residence` + `build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins 通過

## [2026-07-04] update | 照片投稿回填：`a-bian-2020-07-06` +1、`gao-gao-2020-07-06` +1

收件匣 2 筆新投稿（皆本人貼文），兩條目原無 `instagram:` 欄位，新增後補入；無異常、無重複。

**來源**：
- https://www.instagram.com/washimumu/p/DWgiYfnFJpP/ (阿扁，投稿 q5K5DQ7，本人)
- https://www.instagram.com/washimumu/p/DWgg1SUFChd/ (高高，投稿 LDJD72G，本人)

**更新條目**：
- `a-bian-2020-07-06.md` — 阿扁 `instagram:` 新增欄位（1 筆）
- `gao-gao-2020-07-06.md` — 高高 `instagram:` 新增欄位（1 筆）
- 重建 `redpanda.db`（/tmp shim）與 `pipeline/data/*.json`

## [2026-07-04] add | 廣州動物園 6 筆：迪迪・霏霏・逸逸・遙遙・晞晞・小白脸

依使用者提供資料新增廣州動物園個體 迪迪（母霏霏）、逸逸・遙遙雙胞胎（母晞晞），並依「自動補齊直系親屬」建母親霏霏、晞晞與外祖母小白脸。比對 lineage 發現晞晞即 RPF #1319（xixi，2020-06-23 生於廣州、母 #1322 小白脸、歿 2024-04-30），採 RPF 值補空白並標待查證。

**來源**：
- 作者提供（2026-07-04）：迪迪 ♂ 2022-06-30 母霏霏；逸逸 ♂・遙遙 ♀ 2023-06-28 雙胞胎 母晞晞
- https://redpandafinder.com/#profile/1319 (晞晞，生歿與母子關係，愛好者資料 🚧)
- https://redpandafinder.com/#profile/1322 (小白脸)

**新增條目**：
- `di-di-2022-06-30.md` — 迪迪 Di Di ♂，2022-06-30 生於廣州動物園，母 `fei-fei`，父不詳
- `fei-fei.md` — 霏霏 Fei Fei ♀，迪迪之母，生年不詳（slug 比照 pei-pei 前例暫不帶生日）
- `yi-yi-2023-06-28.md` — 逸逸 Yi Yi ♂，2023-06-28 生，與遙遙雙胞胎，母晞晞
- `yao-yao-2023-06-28.md` — 遙遙 Yao Yao ♀，2023-06-28 生，與逸逸雙胞胎，母晞晞
- `xi-xi-2020-06-23.md` — 晞晞 Xi Xi ♀（RPF #1319），2020-06-23 生於廣州、歿 2024-04-30（生歿均依 RPF 🚧 待官方確認），母小白脸；⚠️ 與上海野生動物園 希希（xi-xi-2023-07-01）拼音同名
- `xiao-bai-lian.md` — 小白脸 Xiao Bai Lian ♀（RPF #1322），晞晞之母，生年不詳，暱稱小白／董事长／白女士／咪咪

**更新條目**：
- `xi-xi-2023-07-01.md` — 補 ⚠️ 同名提示（晞晞）
- `index.md` — 廣州動物園區塊補 6 筆；條目總數 498 → 504

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-04] add | 南京市紅山森林動物園個體 嘟嘟

依使用者提供資料新增南京市紅山森林動物園個體 `du-du`（嘟嘟）。lineage 紅山僅有 可乐（Coke #1333），無嘟嘟，故無 RPF 資料；比照 `pei-pei` 前例 slug 暫不帶生日。

**來源**：
- 作者提供（2026-07-04；官方來源待補）

**新增條目**：
- `du-du.md` — 嘟嘟 Du Du，♀，生日／出身／父母均不詳 🚧 待查證，現居南京市紅山森林動物園；日後查得生年再更名 `du-du-YYYY`

**更新條目**：
- `index.md` — 新增「海外個體（中國・南京市紅山森林動物園）」區塊；條目總數 504 → 505

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-05] update | 回報資料更正查證：`cha-cha` `kaguya` `katsuo` 轉園日補正；`xi-xi`（希希）性別暫不採用

處理「回報資料更正」收件匣 4 筆（皆 2026-07-04 提交）。3 筆附官方來源、查證相符，依「官方來源可直接採用」直採；1 筆來源無法核對，標待查證。

**來源**：
- https://www.tokyo-zoo.net/topics/events/ueno/3117_15855_2010-09-10.html (チャチャ 2003-04-17 上野来園，官方長壽動物看板)
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php (野毛山官方：きんた・かぐや 2001 年同批自上海來園)
- https://www.city.kawasaki.jp/530/cmsfiles/contents/0000021/21712/yumemi-news-11.pdf (夢見ヶ崎園報 Vol.11：カツオ 2009-01-26 自市川來園)

**更新條目**：
- `cha-cha-1992-07-17.md` — 宝塚ファミリーランド訖日 2003-04-07 → 2003-04-17（回報 gb7eX9P：4/7 為閉園日，実移動日 4/17 = 上野官方來園日；居住地銜接無縫）
- `kaguya-2000-06-29.md` — 野毛山到園日 2001 → 2001-04-05（回報 5XGjLb6：官方載與 Kinta 同批來園，精確日期採 Kinta 來園日 RPF #125 推得，條目內註明推定依據）
- `katsuo-2002-07-02.md` — 市川訖／夢見ヶ崎起 2009 → 2009-01-26（回報 xVPM4Qr：官方園報明載）；sources +1
- `xi-xi-2023-07-01.md` — 回報 kb7e5N6 稱希希為 ♀，惟來源連結僅導向園方官網首頁、無個體記載，網搜亦無官方性別資訊 → 暫不採用，於待查證註記線索

**重建**：`build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins

## [2026-07-05] add | 柳州市動物園登記 + 個體 荔枝

新增動物園「柳州市動物園」至註冊表，並依使用者提供資料新增個體 `lizhi-2025`（荔枝）。lineage/RPF 均無柳州記錄，故無 RPF 資料。性別與「2025 年 6 月下旬生」為作者提供；官方文章僅載育幼室亮相，未載生日／性別／父母。因僅知年月，born 依規範暫記 2025、slug 用 `lizhi-2025`，查得完整生日再更名。

**來源**：
- http://lyhylj.liuzhou.gov.cn/xwzx/ylwh/dwsj/202510/t20251013_3677219.shtml (柳州市林業和園林局：小熊猫"荔枝"亮相柳州动物园育幼室，2025-10-13)
- 作者提供（2026-07-05：♀、2025 年 6 月下旬生）

**新增條目**：
- `lizhi-2025.md` — 荔枝 Lizhi，♀，2025 年 6 月下旬生（確切日期待查證 🚧），現居柳州市動物園；父母、出生地待查證

**更新條目**：
- `data/zoos.json` — 登記 柳州市動物園（広西チワン族自治区柳州市柳南区航銀路89號；座標取自作者提供 Google Maps 連結；官網無，lineage_id 無）
- `index.md` — 新增「海外個體（中國・柳州市動物園）」區塊；條目總數 505 → 506

**重建**：`gen_residence` + `build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins

## [2026-07-05] add+update | 柳州市動物園：荔枝生日更正・白桃與四位親代新增

依作者提供資料更正 `lizhi`：生日由「2025 年 6 月下旬（暫記 2025）」更正為 **2025-07-07**，slug `lizhi-2025` → `lizhi-2025-07-07`；父 `dan-dan`（蛋蛋）、母 `hao-hong`（好紅）。另新增同園 2025-06-16 出生之 `bai-tao`（白桃，父 `xi-bao` 喜寶、母 `xiao-bai` 小白），並依「自動補齊直系親屬」建四位親代條目（生年均不詳，slug 暫不帶生日，查得後更名）。白桃與荔枝父母不同、無血緣。

**來源**：
- 作者提供（2026-07-05：兩隻 ♀ 幼崽生日與父母）

**新增條目**：
- `bai-tao-2025-06-16.md` — 白桃 Bai Tao ♀，2025-06-16 生於柳州市動物園，父喜寶・母小白
- `xi-bao.md` — 喜寶 Xi Bao ♂，白桃之父，生年不詳 🚧
- `xiao-bai.md` — 小白 Xiao Bai ♀，白桃之母，生年不詳 🚧；⚠️ 與廣州 `xiao-bai-lian` 暱稱「小白」同名，已互加提示
- `dan-dan.md` — 蛋蛋 Dan Dan ♂，荔枝之父，生年不詳 🚧
- `hao-hong.md` — 好紅 Hao Hong ♀，荔枝之母，生年不詳 🚧

**更新條目**：
- `lizhi-2025.md` → `lizhi-2025-07-07.md` — 生日更正為 2025-07-07、slug 更名、補父母 wikilink
- `xiao-bai-lian.md` — 加 ⚠️ 同名提示（柳州 小白）
- `index.md` — 柳州市動物園區塊補齊 6 筆；條目總數 506 → 511

**重建**：`gen_residence` + `build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins

## [2026-07-05] add | 上海動物園個體 湯圓、阿狸

依作者提供資料新增上海動物園個體 `tang-yuan`（湯圓／汤圆）與 `a-li`（阿狸，♂）。兩隻生日均不詳，slug 比照 `xiao-bai` 前例暫不帶生日；作者另提及「小白」（生日、母名均不詳，與柳州 `xiao-bai` 撞名無法消歧），依作者指示暫不建立、待補資料。

**來源**：
- 作者提供（2026-07-05；官方來源待補）

**新增條目**：
- `tang-yuan.md` — 湯圓 Tang Yuan，性別／生日／出身／父母均不詳 🚧 待查證，現居上海動物園；日後查得生年再更名 `tang-yuan-YYYY`
- `a-li.md` — 阿狸 A Li ♂，生日／出身／父母不詳 🚧 待查證，現居上海動物園；日後查得生年再更名 `a-li-YYYY`

**更新條目**：
- `index.md` — 上海動物園區塊 +2；條目總數 511 → 513

**重建**：`build_db`（/tmp shim）+ `export_json`

## [2026-07-05] add | 廣州動物園個體 康康、雪雪；補逸逸・遙遙父親

依作者提供資料新增廣州動物園個體 `kang-kang`（康康，♂，逸逸之父）與 `xue-xue`（雪雪，♀）。兩隻生日均不詳，slug 暫不帶生日。作者提供「康康是逸逸的爸爸」；`yao-yao` 與 `yi-yi` 為同窩雙胞胎，故遙遙之父亦記為康康（依雙胞胎關係推定，條目內註明）。

**來源**：
- 作者提供（2026-07-05；官方來源待補）

**新增條目**：
- `kang-kang.md` — 康康 Kang Kang ♂，生日／出身／父母不詳 🚧 待查證，現居廣州動物園；晞晞配偶、逸逸・遙遙之父；日後查得生年再更名 `kang-kang-YYYY`
- `xue-xue.md` — 雪雪 Xue Xue ♀，生日／出身／父母不詳 🚧 待查證，現居廣州動物園；日後查得生年再更名 `xue-xue-YYYY`

**更新條目**：
- `yi-yi-2023-06-28.md` — 父 不詳 → `kang-kang`；待查證僅剩官方來源
- `yao-yao-2023-06-28.md` — 父 不詳 → `kang-kang`（依雙胞胎關係推定）
- `xi-xi-2020-06-23.md` — 子女表另一方親本補 `kang-kang`；家族補配偶
- `index.md` — 廣州動物園區塊 +2、逸逸／遙遙說明補父；條目總數 513 → 515

**重建**：`build_db`（/tmp shim）+ `export_json`

## [2026-07-05] add | 中山市紫馬嶺動物園 4 筆：窩窩頭・麵包・米糕・大佬

依作者提供資料新增紫馬嶺個體 4 筆（生年均不詳，slug 暫不帶生日，查得後更名）。含既有 `bagel-2024-07-12` 園內 5 隻到齊。窩窩頭為貝果之父（作者補充）；麵包為米糕之母。lineage/RPF 均無此 4 隻記錄。

**來源**：
- 作者提供（2026-07-05）

**新增條目**：
- `wo-wo-tou.md` — 窩窩頭 Wo Wo Tou ♂，貝果之父，生年不詳 🚧
- `mian-bao.md` — 麵包 Mian Bao ♀，米糕之母，生年不詳 🚧
- `mi-gao.md` — 米糕 Mi Gao ♀，麵包之女，生年不詳 🚧
- `da-lao.md` — 大佬 Da Lao ♀，出身不詳 🚧

**更新條目**：
- `bagel-2024-07-12.md` — 父補為 窩窩頭（wikilink），母仍待確認；tags 的 zoo 值由英文名改為註冊表 canonical（中山市紫馬嶺動物園），與其他條目一致
- `index.md` — 紫馬嶺區塊補 4 筆、貝果說明更新；條目總數 511 → 515

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-05] update | 米糕生日補正 2021-06-05、slug 更名

依作者提供補米糕生日：`mi-gao` → `mi-gao-2021-06-05`（born: 2021-06-05）；出生地與父仍待查證。同步修正 `mian-bao.md` 與 `index.md` 的 wikilink。另註：index 條目總數依實際檔數校正為 519（含並行作業新增的 `a-li` `kang-kang` `tang-yuan` `xue-xue` 4 筆）。

**來源**：
- 作者提供（2026-07-05）

**更新條目**：
- `mi-gao.md` → `mi-gao-2021-06-05.md` — 補生日、slug 更名
- `mian-bao.md` — 子女表補出生年、wikilink 更名
- `index.md` — 米糕列更新；條目總數校正 515 → 519

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-05] update | 阿狸生日 2020-06-27；slug 更名 `a-li` → `a-li-2020-06-27`

作者補充上海動物園阿狸生日為 2020-06-27。依命名規則將 slug 由暫定 `a-li` 更名為 `a-li-2020-06-27`，並修正 index wikilink（無其他條目連結）。出生園仍不詳，居住史起日維持待查證。

**來源**：
- 作者提供（2026-07-05：生日 2020-06-27）

**更新條目**：
- `a-li.md` → `a-li-2020-06-27.md` — 補 `born: 2020-06-27`；待查證縮至出身／父母／官方來源
- `index.md` — wikilink 與生年欄同步更新

**重建**：`build_db`（/tmp shim）+ `export_json`

## [2026-07-06] update | 讀者回報更正 3 筆：Nanako 生日、Teru 來園日、希希性別

處理「回報資料更正」收件匣 6 筆：`cha-cha-1992-07-17`、`kaguya-2000-06-29`、`katsuo-2002-07-02` 三筆先前已依同來源處理過，無需變動；其餘 3 筆均附官方來源，直接採用。

**來源**：
- https://www.nhdzoo.jp/sp/event/naka.php?id=615 （日本平動物園：ななこ成長記「令和8年7月7日で1才」）
- https://www.city.ichikawa.lg.jp/site/zoo/2822.html （市川市動植物園個體頁：テル 2018年2月1日来園）
- https://www.swap-shendi.com/index.do?newsDetail&id=4594 （上海野生動物園官網：希希為展区年紀最小雌性、園內出生半人工育幼）

**更新條目**：
- `nanako-2025-07-14.md` → `nanako-2025-07-07.md` — 生日依園方由 2025-07-14 更正為 2025-07-07（RPF #1451 原值有誤），slug 更名；同步修正 `nico-2017-06-23.md`、`kazu-2019-07-02.md`、`emi-2023-07-09.md`、`kazunoko-2021-08-04.md`、`index.md` 之 wikilink 與生日欄（回報：Aoi Ajisai）
- `teru-2010-07-10.md` — 市川來園日由 2018-02-27（RPF）更正為 2018-02-01（園方個體頁＋広報いちかわ年表）；補來源（回報：楊桃）
- `xi-xi-2023-07-01.md` — 性別確認 ♀、出生園確認為上海野生動物園（半人工育幼），居住史起日補 2023-07-01；補官方來源；`index.md` 說明同步更新（回報：Ariel）

## [2026-07-06] add | 圖鑑缺漏回報 15 筆處理：新增 14 條目、2 動物園

處理「圖鑑缺漏回報」收件匣：已存在者（`ai-1991` 上野アイ、`xi-xi-2023-07-01` 希希、Drusillas Park 個體）免建；官方可核者直接採用；來源開不了或非官方者建條目標 🚧 或列待查證。`data/zoos.json` 新增 銀基動物王國、寧波野生動物園（座標待補）。

**來源**：
- https://www.city.ichikawa.lg.jp/site/zoo/2822.html ＋ 広報いちかわ 22158.pdf ＋ 官方 X（市川三胞胎）
- https://hkcd.com/content_p/2025-01/06/content_182122.html （銀基六隻小熊貓亮相報導）
- https://shwzoo.com/index.do?id=4517&newsDetail= （上海野生動物園官網：二宝、二帅）
- https://turnto10.com/news/local/red-panda-kits-at-roger-williams-moving-to-different-zoos ＋ WPRI／Boston Globe（RWP 雙胞胎）
- https://redpandafinder.com/#profile/2 #6 #7 #932 #1171 #433（lineage 比對）
- 讀者回報（2026-07-01～07-05：Mikeson、nn、Ariel、楊桃 等）

**新增條目**：
- `meito-2013-06-20.md` — 明登 メイト ♂（RPF #2），市川三胞胎，人工哺育；`rifa-2013-06-20.md` — 梨花 リーファ ♀（RPF #7）；既有 `yuufa-2013-06-20.md` 補三胞胎 wikilink 與官方來源。同步把 `mei-fa-2006-06-23`、`raichi-2005-06-25`、`ichimaru-2009-07-04` 的純文字改 wikilink；`rifa-2018-06-07.md` 加同名注意
- `cong-cong-2008-06-11.md` — 聰聰 ♂（RPF #932），2008 成都生、2009 與泰山同批赴香港海洋公園；`tai-shan-2008-06-14.md` 補 wikilink
- `katara-2025-07-04.md`、`sokka-2025-07-04.md`、`zan-2020-05-25.md`、`kendji-2015-06-22.md` — Roger Williams Park Zoo 一家；Katara 2026 春依 SSP 移居新園（讀者稱 Toledo，官方未公布 → 待查證，暫不寫入居住史）
- `er-bao-2015.md` — 二寶 ♀，2015 上海野生動物園生（官網文章）
- `you-you.md`、`bei-bei.md` — 佑佑、貝貝，銀基動物王國 2025-01 亮相（香港商報）🚧 性別生日待查；佑佑加同名注意（日本 ユウユウ ×3）
- `zhong-xia-2025-07-17.md`、`meng-xia-2025-07-17.md`、`xia-wa.md` — 紅山 仲夏 ♂・孟夏 ♀（2025-07-17 雙胞胎）與母夏娃 🚧 微信官方文開不了、暫依回報
- `nan-nan-2024-07-02.md` — 囡囡，寧波野生動物園人工育幼第三隻 🚧

**更新條目**：
- `index.md` — 新增 銀基、寧波 兩區塊；上海野生／紅山／香港／美國／Milk 家族各補列；條目總數 519 → 533

**待查證（未建條目，留作者裁定）**：
- 天津動物園＋图图（♂父）/小宝（♀母）/团团（♀ 2023-06-06 生）— 回報未附任何來源
- 都江堰小熊貓森林公園 — 無官網（僅小紅書/YouTube），園資料不足
- 上野 アイ回報未附來源，但 `ai-1991` 已存在，視為已收錄

## [2026-07-06] update | 照片投稿回填 2 筆（chen-chen、arata）

比對照片投稿收件匣 13 筆新投稿：11 筆 wiki 已有（僅待 Sheet I 欄補標），2 筆待補已回填 instagram frontmatter。

**更新條目**：
- `chen-chen-2022-07-05.md` — instagram +1（DaagK3ij2kM）
- `arata-2019-07-05.md` — 新增 instagram 欄位 +1（DaZWk96EaOm）

## [2026-07-06] update | 紅山三條目補官方佐證（荔枝新聞）；圖鑑缺漏批次重建

為 `zhong-xia-2025-07-17`、`meng-xia-2025-07-17`、`xia-wa` 補上荔枝新聞（2026-01-04，轉自 @南京市紅山森林動物園）佐證：雙胞胎、2025 年 7 月生、母 `xia-wa` 第二胎、`zhong-xia` 為兄（♂）且 3 月齡時肺炎康復、高黎貢展區。原「微信文開不了、暫依回報」的 🚧 範圍縮小為：精確生日 2025-07-17、孟夏性別 ♀、父不詳。另補記：天津動物園回報（图图/小宝/团团）經網路查證仍無官方來源，維持待查證。

**來源**：
- https://finance.sina.com.cn/jjxw/2026-01-04/doc-inhfeeek7361107.shtml （荔枝新聞轉載）

**更新條目**：
- `zhong-xia-2025-07-17.md`、`meng-xia-2025-07-17.md`、`xia-wa.md` — 補來源與 📝 佐證說明

**重建**：`build_db`（/tmp shim）+ `export_json`；audit --strict、check_twins

## [2026-07-06] update | 致謝名單補 Ariel、nn；處理流程加「補致謝」固定步驟

本批已採用回報中留名者：楊桃、Aoi Ajisai、Mikeson（已在名單）；新增 Ariel（希希更正＋二寶/囡囡/聰聰）、nn（紅山仲夏/孟夏）至 `data/contributors.json`。`CLAUDE.md` 回報處理流程末尾新增固定最後一步：採用回報後檢查留名者是否已列致謝名單。

**更新條目**：
- `data/contributors.json` — +2（Ariel、nn）
- `CLAUDE.md` — 處理流程補「最後一步：補致謝名單」

## [2026-07-06] update | 囡囡補性別（雌）

依作者指正，`nan-nan-2024-07-02`（囡囡）為雌性。frontmatter `sex: female`、tags 加 `female`、引言標 ♀，並自 🚧 待查證移除「性別」（父母、正式名仍待查證）。

**更新條目**：
- `nan-nan-2024-07-02.md` — 補 sex: female

**重建**：`build_db`（/tmp shim）+ `export_json`

## [2026-07-06] hide | 隱藏 Katara（Roger Williams Park Zoo）

依作者指示，`katara-2025-07-04`（Katara，Roger Williams Park Zoo 雙胞胎之一）資料未經核實，先隱藏（非刪除）：移至 `wiki/_hidden/`，退出 DB／`pipeline/data`／網站；原檔保留於 repo，需要時移回即復原。移居 Toledo Zoo 一說僅來自 2026-07-05 讀者回報、無官方公布，原本即標 🚧 未寫入居住史，未經查證。雙胞胎 `sokka-2025-07-04` 與父母 `zan`／`kendji` 保留。

**更新條目**：
- 移至 `_hidden/`：`katara-2025-07-04.md`
- 去除指向 katara 的 `[[wikilink]]`（改純文字 Katara）：`zan-2020-05-25.md`、`sokka-2025-07-04.md`、`kendji-2015-06-22.md`、`index.md`
- `index.md` — 移除 Katara 列，區塊改名「Sokka 一家」

**重建**：`build_db` + `export_json`（已驗證 pandas.json／family.json 不含 katara）

## [2026-07-06] hide | 隱藏 Sokka（Roger Williams Park Zoo）

依作者指示，一併隱藏雙胞胎另一隻 `sokka-2025-07-04`（同批未經核實資料）。移至 `wiki/_hidden/`，退出 DB／`pipeline/data`／網站；原檔保留。去除指向 sokka 的 `[[wikilink]]`（改純文字 Sokka）：`zan-2020-05-25.md`、`kendji-2015-06-22.md`、`index.md`。index 區塊改名「Zan × Kendji 一家」、移除 Sokka 列並註明兩隻雙胞胎資料未核實暫隱藏。父母 `zan`／`kendji` 保留。

**重建**：`build_db` + `export_json`（已驗證 pandas.json／family.json 不含 katara／sokka；條目數 → 531）

## [2026-07-06] remove | 移除「保種優先」（/breeding）功能與頁面

依作者指示，移除網站的保種優先繁殖重點功能與整個 `/breeding` 分頁。

**刪除檔案**：
- `web/src/components/Breeding.astro`（頁面元件）
- `tools/build_priority_page.py`、`tools/lineage_risk.py`、`tools/kinship.py`（保種遺傳指標／排名腳本）
- `珍貴血緣繁殖重點.html`、`珍貴血緣繁殖重點.md`（舊產物報告）
- `PLAN-endangerment.md`（規劃筆記）

**更新檔案**：
- `web/src/lib/data.js` — 移除 `SHOW_BREEDING` guard 與 `breedingPriority()` 演算法
- `web/src/pages/[...path].astro` — 移除 breeding 路由、import、標題、渲染
- `web/src/layouts/Layout.astro` — 移除導覽列 breeding 連結
- `web/src/components/Stats.astro` — 移除指向 breeding 的互導連結
- `pipeline/src/i18n/*.json ×5` — 移除 `nav_breeding` 與所有 `breeding_*` 鍵（各 165 → 135，五語一致）

**驗證**：全新安裝＋`astro build` 通過（3292 頁、無錯誤）；dist 無 `/breeding` 路由、五語 stats 頁與其餘頁面正常。

## [2026-07-07] update | 查證讀者回報資料更正（回報資料更正 Sheet）：採用 6 筆官方來源、3 筆待查證、1 筆待作者裁定

依「官方來源可直接採用」原則處理本批 10 筆回報。

**已採用（官方來源）**：
- `ai-1991.md` → 更名 `ai-1991-06-20.md`：生日 1991 → **1991-06-20**、歿日 2009 → **2009-07-13**（享年 18）、補原名 **愛愛２／アイアイツー**、安佐→上野移動日 **2001-02-20**。依安佐動物公園平成 22 年年報（`asazoo.jp` 官方 PDF：愛愛２ ♀ 1991/06/20，2001/02/20 貸出上野）與上野動物園 2009 慰霊祭官方公告（死亡 2009/07/13、18 歲、飼育 8 年 5 個月、原名愛愛２）。同步更名並修正 `[[wikilink]]`（`index.md`、`cha-cha-1992-07-17.md`）。出生地池田動物園一說官方來源未載，維持既有校訂並標 🚧。回報者：`楊桃`（已在致謝名單）。
- `jin-jin-2022-07-05.md`（菫菫 ジンジン）：性別 雌 → **雄**。依旭山動物園令和4年官方紀錄「菫菫（ジンジン）♂」。
- `rin-rin-2020-06-29.md`（桜桜 リンリン）：性別 雄 → **雌**。依旭山令和2年官方紀錄與園報だより271（メス：桜桜）。
- `ren-ren-2020-06-29.md`（蓮蓮 レンレン）：性別 雌 → **雄**。同上（オス：蓮蓮）。※ 上兩隻原資料性別對調，已一併修正父母條目 `yuu-yuu`、`puerh` 之子女表與雙胞胎互指。
- `rii-rii-2018-07-11.md`（梨梨）：旭山→羽村移居日 2021-02-03 → **2022-02-03**。依旭山令和4年（2022）官方紀錄「梨梨（リーリー）移動（2月3日）」。
- `shou-shou-2017-07-15.md`（守守）：旭山→豊橋移居日補精確 2020 → **2020-01-29**。依旭山令和2年官方紀錄。

**待查證（來源非官方，暫不採用）**：
- `shin-fa-2002-06-29`：回報稱 2003-05-11 移市川市動植物園。來源為個人部落格（`mamepandaworld.blog.fc2.com`），非官方 → 🚧 待查證。
- `tian-2011`：回報稱生日 2011-06-13、2012-12-22 移仙台八木山。同一部落格來源，非官方 → 🚧 待查證。
- `charmin-2011-07-17`：回報稱 2014-02-03 移旭山。來源為旭山官方網域但 Sheet 內連結被截斷、無法核對確切頁面 → 🚧 待查證（僅為現有 2014 年份補日精度、風險低）。

**待作者裁定（官方來源互相衝突）**：
- `ryuunosuke-1999-07-27`（緑之介）：回報稱歿於 2019-03-13。查愛媛県立とべ動物園（實際終老／死亡園）官方死亡公告載「2019 年 3 月 12 日老衰死亡」（公告日 3/13）。此與 wiki 現值 **2018-03-12**（作者依多摩動物公園個體名單裁定、曾明確否決 2019 說）衝突。屬官方來源互相打架，依原則留待作者裁定；提請作者參酌：とべ動物園為死亡地之一手來源，歿日應為 2019-03-12。

**更新條目**：
- `index.md` — Ai 連結改為 `ai-1991-06-20`、說明補原名愛愛２

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-07] update | 緑之介歿日依とべ動物園官方公告更正 2018-03-12 → 2019-03-12

承前一則「待作者裁定」，作者裁定採官方。`ryuunosuke-1999-07-27` 歿日由 **2018-03-12** 改為 **2019-03-12**（老衰、時年 19 歲；公告日 2019-03-13），依愛媛県立とべ動物園（死亡地）官方死亡報告。居住史迄日同步更新；`sources` 補入 とべ動物園官方連結（保留原多摩名單 4travel 轉載連結供對照）。原值係遊客轉載之多摩個體名單，年份較可能為筆誤。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-07] feat | 個體頁新增「來源／出典／Sources」區塊（只顯示官方來源）

讀者回報常附官方連結；個體頁新增來源區塊呈現，政策（作者裁定，最嚴）＝**只顯示園方官網／政府（自治體）公告／園報／中國園官方微信**；RPF、redpanda-lineage、個人部落格、新聞媒體、社群、wiki、web.archive 一律不顯示（仍保留於 frontmatter `sources` 供校訂稽核）。

**管線／前端改動**：
- `tools/build_db.py` — 新增 `OFFICIAL_HOSTS` 白名單＋政府網域 pattern＋`is_official_source()`／`official_sources()`；Pass 1 讀 `sources` 並過濾為官方後存入 pandas。**日後新增園方官網 → 補進 `OFFICIAL_HOSTS` 即自動顯示。**
- `tools/schema.sql` — pandas 表加 `sources TEXT`（JSON array，官方過濾後）
- `pipeline/scripts/export_json.py` — 輸出 `sources` 到 pandas.json
- `web/src/components/Panda.astro` — 新增來源區塊（mobile-first，連結文字用網域；`sources` 為空則不渲染）
- `pipeline/src/i18n/*.json ×5` — 新增 `sec_sources`／`sources_note`（五語一致）

**驗證**：全站 63/531 個體有官方來源、0 筆非官方殘留；全新安裝＋`astro build` 通過（3292 頁）；抽查 ryuunosuke（僅とべ官方）、ai（tokyo-zoo＋asazoo）、shin-fa（僅 RPF→正確無來源區塊）、五語標籤（來源／出典／Sources）皆正常。

## [2026-07-07] update | Shin-Fa（杏花）補轉園日 2003-05-11（市川市動植物園）

回報 RWJYvLP 附市川市動植物園**園內紙本家系圖**（園方一手確認），採用轉園日：`shin-fa-2002-06-29` 居住史 東北サファリパーク→市川市動植物園 之異動日補為 **2003-05-11**（市川迄日一併補其歿日 2008-10-05）。依作者指示，回報所附之 blog 連結僅為佐證出處、**不列入 frontmatter `sources`**（紙本家系圖無線上官方連結，故頁面來源區塊不變）。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-07] update+fix | Shin-Fa 日文名官方更正、Tian 補生日/轉園（改 slug）、搜尋支援羅馬拼音折疊

**Shin-Fa（杏花）**：`shin-fa-2002-06-29` 日文名依官方由 `シンファ` 改為 **`シーンファ`**（漢字 杏花 不變）。

**Tian（天）採用回報 yXEvGl8**：來源同 Shin-Fa（市川園紙本家系圖等園方一手確認，blog 僅佐證出處、不入 `sources`）。生日 2011 → **2011-06-13**、東北サファリパーク→仙台市八木山動物公園異動日補為 **2012-12-22**。因生日補齊為完整日期，slug 依規則改名 `tian-2011` → **`tian-2011-06-13`**，並修正 14 個條目內的 `[[tian-2011]]` wikilink。

**搜尋修復（web/public/js/search.js）**：中文介面（及各語系）以 `sinfa`／`sin-fa` 搜不到 Shin-Fa。主因：搜尋正規化只做小寫＋去空白/連字號，`shin-fa`→`shinfa` 可中，但使用者以訓令式拼音（無 h）輸入不中；英文名本就跨語系索引，非語系問題。加入 `romajiFold`（Hepburn↔訓令式：sh/si、ch/ti、tsu/tu、fu/hu、ji/zi，及 L/R、V/B、長音壓縮），查詢與索引套同一折疊、只增命中不漏。實測 `shinfa`／`sinfa`／`sin-fa`／`shin-fa`／`杏花` 皆命中。

**驗證**：`gen_residence`＋`build_db`＋`export_json` 重建；audit --strict、check_twins exit 0；全新安裝＋`astro build` 通過（3292 頁），新 slug 頁面生成、舊 slug 移除、search.js 折疊進 dist。

## [2026-07-07] fix | 繁繁／甜甜 台北來源改為官方新聞稿（原僅園首頁）

`fan-fan-2023-05-02`、`tian-tian-2024-06-23` 的 `sources` 原只填台北市立動物園首頁 `https://www.zoo.gov.taipei/`（泛用首頁、非個體資訊，視同無效來源）。依作者提供之園方新聞稿改為實際文章 `News_Content.aspx?...s=41319415ED5BFF7D`（〈上海動物園小貓熊報到〉，2026-06-06 發布），該稿即記述此對小貓熊由上海動物園移入台北，為兩隻共用之官方一手來源。上海動物園首頁保留為原園參照。

**重建**：`build_db` + `export_json`；頁面來源區塊改顯示該新聞稿。

## [2026-07-07] update | 美可（Meike）補官方歿訊來源

`meike-2008-07-22` 歿日 2024-05-01（享年 15）原已記錄、但 `sources` 僅有 RPF。補上台北市立動物園官方新聞稿〈老齡小貓熊「美可」不幸離世〉（`News_Content.aspx?...s=5DE1638C6A059102`，2024-05-08 發布，證實 5/1 因心臟衰竭離世）。yaya（丫丫）歿訊 2024-07-12 之官方新聞稿先前已在 `sources`，無需變動。

**重建**：`build_db` + `export_json`。

## [2026-07-07] update | Yaffa（奇奇）搬家來源改為園方官方新聞稿

`yaffa-2015-06-22` 移居新加坡動物園（2026-06-11）居住史已正確。來源原為市府彙整版 `www.gov.taipei/...s=7AF1E4A8EA022440`，改為台北市立動物園自家新聞稿〈小貓熊「Yaffa奇奇」前往新加坡動物園〉`www.zoo.gov.taipei/...s=7AF1E4A8EA022440`（2026-06-11 發布，同一篇之園方正本）。

**重建**：`build_db` + `export_json`。

## [2026-07-08] update | 接受 IG 投稿：Nanako（ななこ）

讀者直接投稿（未經 Sheet）：`nanako-2025-07-07` frontmatter 新增 `instagram:`，補入 https://www.instagram.com/p/DafVsR5j3Ld/（正規化、去 query）。全 wiki 無重複。

## [2026-07-08] update | Charmin（チャーミン）轉園日補為 2014-02-03（官方訃報）

回報附旭山動物園官方訃報頁（園方一手來源，直接採用）：來歷載明「2014年2月3日 鯖江市西山動物園から来園」。`charmin-2011-07-17` 居住史 鯖江市西山動物園→旭川市旭山動物園 異動日由僅年份 2014 補為 **2014-02-03**；官方訃報 URL 補入 `sources`。

**來源**：
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/news-blog/osirase/d073787.html (レッサーパンダ「チャーミン」の訃報)

**重建**：`gen_residence` + `build_db` + `export_json`。

## [2026-07-08] add | 圖鑑缺漏回報 7/7 新進 6 筆處理：新增 13 條目（含直系親屬）

處理「圖鑑缺漏回報」收件匣 07-07 新進 6 筆（皆附來源）。逐筆開連結查證：官方來源可核者直接採用；官方頁生日疑佔位、或親屬線索無官方佐證者標 🚧。親屬資料以 RPF／lineage 為初期基礎參考補齊（非權威）。

**來源（官方）**：
- https://www.kobe-ojizoo.jp/info/detail/?id=25 （王子動物園訃報：天天，回報 0VJ0vGN，楊桃）
- http://ojizoo.jp/html/oj-07-166.htm （王子動物園追悼頁：洋洋，回報 RWJejad，楊桃）
- https://www.zooknoxville.org/animals/red-panda/ （Zoo Knoxville 動物頁：Lincoln，回報 PRX40V5）
- https://www.witheverland.com/427712 （Everland 官方部落格：레아 七歲生日，回報 Arq08G0）
- https://grandpark.seoul.go.kr/story/view/ko/S001006001003.do?bbs_no=120&pageIndex=2 （首爾大公園官方頁：라비 2023-11 抵園，回報 J1Jx8zX）
- https://gvzoo.com/news/greater-vancouver-zoo-celebrates-global-conservation-success-with-the-birth-of-red-panda-twins 、 https://gvzoo.com/news/red-panda-cubs-1st-birthday （GVZoo 官方新聞：Arun 一家，回報 e57pgBq）

**新增條目（13）**：
- `ten-ten-1991-06-29.md` — 天天 てんてん，♂ styani 🌈，1991-06-29 安佐生，1992-04-24 移王子，2012-07-20 歿（21 歲、國內第三長壽）；官方訃報完全吻合回報
- `yan-yan-1985-05-31.md` — 洋洋 ヤンヤン，♀ styani 🌈，1985-05-31 京都市動物園生，1986-03-10 移王子，2007-10-25 歿（22 歲、當時國內最高齡）；官方頁另載 1987-07-07 產一女（名字不詳，未建檔）
- `lincoln-2013-07-26.md` — Lincoln（RPF #529），♂ fulgens，Lincoln Children's Zoo 生，2014-01-24 移 Zoo Knoxville；生日採 RPF 2013-07-26，🚧 官方頁列 2013-01-01（與 Willow 同為 1/1、疑佔位）
- `leah-2019-05-17.md` — Leah 레아，♀，現居 Everland；生日 2019-05-17 依官方部落格七歲生日反推；🚧 出生園／亞種／父母待查證（RPF 無檔）
- `ravi-2022-06-14.md` — Ravi ラビ／라비（RPF #1397），♂ styani，Calgary 生，2023-11-20 移首爾大公園；🚧 回報稱生日 2022-06-11（無官方佐證，採 RPF 6/14）；與 `sei`、`leanne` 同批抵韓
- `sundari-2022-06-14.md` — Sundari（RPF #1396），♀，Ravi 雙胞胎，現居 Calgary；舊名 Sunsari
- `linus-2018-06-23.md` — Linus（RPF #1000），♂，Ravi/Sundari 之父，Cincinnati 生、2019 移 Calgary
- `udaya-2019-06-20.md` — Udaya（RPF #1081），♀，Ravi/Sundari 之母、`sakura`（#445）之女；舊名 Aduya
- `arun-2014-06-28.md` — Arun（RPF #432），♂ styani，Assiniboine 生，2015-05-28 移 GVZoo（官方新聞證實；回報誤植 5/28 為出生）；🚧 回報稱 2025-11-17 移回 Assiniboine，僅 IG 來源，暫不寫入居住史
- `rakesh-2014-06-28.md` — Rakesh（RPF #449），♂ 🌈，Arun 雙胞胎，2015-08-17 歿（1 歲）
- `sakura-2013-07-01.md` — Sakura（RPF #445），♀ 🌈，Granby 生→Calgary→GVZoo→Toronto，2024-08-22 歿；Udaya/Maple/Mei-Mei 之母；🚧 GVZoo/Toronto 移動日與歿日精確度依 lineage 標記不確定；lineage 另載 2024 多倫多双子 Baby🌈/Poppy，出生地資料矛盾（載為廣島安佐、顯誤），未建檔待查證
- `maple-2022-06-14.md` — Maple 松楓（RPF #1405），♂，BC 省首胎雙胞胎之一，2024-01-29 移 Granby（🚧 日期精確度）；別名 Moose
- `mei-mei-2022-06-14.md` — Mei-Mei（RPF #1404），♀，BC 省首胎雙胞胎之一，現居 GVZoo

**更新條目**：
- `ten-ten-1998-07-07.md`、`yan-yan-1992-06-19.md`、`mei-mei-2023-06-24.md` — 同名注意補列新條目
- `index.md` — 新增「王子動物園 早期個體（神戸）」「海外個體（加拿大・Arun × Sakura 一家）」「海外個體（加拿大 → 韓國・Ravi 一家）」「海外個體（韓國・Everland）」四區塊；美國區塊補 Lincoln；條目總數更新為 **544**（註：以 `ls wiki/*.md` 實數為準；前值 533 與實數 531 差 2，本次一併校正）

**收件匣其他筆數**：
- 已處理過免動作：Drusillas Park（07-02 批）、銀基動物王國・アイ（07-06 批）
- 維持 🚧 待查證：都江堰小熊貓森林公園（無官網）、天津動物園 图图/小宝/团团（無來源）
- ⚠️ Katara（回報 OQJ70va）：回報稱「目前 11 歲、今年 5 月移 Toledo」，與已隱藏之 `katara-2025-07-04`（1 歲）年齡矛盾——回報者所指可能為另一隻約 2014–15 年生的 Katara，留待作者定奪

**致謝**：楊桃（已在 contributors 名單，不重複列）

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-08] unhide+update | Katara（Roger Williams）解隱藏：回報 OQJ70va 經查證為本隻

追查 07-05 缺漏回報「Katara，11 歲，5 月初移 Toledo」：RPF／lineage／全網查無任何 11 歲（2014–15 年生）Katara；而 Roger Williams Park Zoo 於 2026-06-04 官方宣布 `katara-2025-07-04` 依 SSP「已移居新園、地點待新園就緒後公布」（NBC 10 WJAR／WPRI 轉述園方聲明），Toledo Zoo 官方 FB 亦有 Katara 內容，時間點與回報完全吻合。判定回報之「11 歲」為「11 個月」之誤，所指即本隻。經作者確認後：

- `katara-2025-07-04.md` — 自 `wiki/_hidden/` 移回 `wiki/`；離園（2026 春）依園方聲明記錄，居住史訖寫 2026；**去向 Toledo 仍標 🚧**（兩園官網均未正式公布），待官方來源確認後補
- `zan-2020-05-25.md`、`kendji-2015-06-22.md` — Katara 恢復 `[[wikilink]]`、子女表補移居備注
- `index.md` — Zan × Kendji 區塊補 Katara 列與說明；條目總數 544 → **545**（_hidden 剩 6 筆，Sokka 續藏）

**來源**：
- https://turnto10.com/news/local/red-panda-kits-at-roger-williams-moving-to-different-zoos （NBC 10，2026-06-04，轉述園方聲明）
- https://www.wpri.com/news/local-news/providence/twin-red-pandas-leaving-roger-williams-park-zoo/ （WPRI，同）

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-08] update | 照片投稿回填 6 筆（本人投稿）

照片收件匣新進 6 筆（同一投稿者，均為本人貼文），比對無重複、無疑慮，全數回填 `instagram:` frontmatter（6 檔原無此欄位，一併新增）：

- `kabosu-2018-06-28` — DaH-uuwTmta
- `ron-ron-2013-07-19` — DSHu6mKEoQG
- `a-li-2020-06-27` — DWgkQZ1FNYY（原投稿缺尾斜線，已正規化）
- `takenoko-2024-06-14` — DLpLyTzBHjv
- `hama-2025-06-25` — DaAcWfLzr9z
- `daifuku-2020-07-18` — DSHD2ZikaGt

Sheet I 欄「已補進」標記待作者手動處理。

**重建**：`build_db` + `export_json`

## [2026-07-08] add+update | Leah＝RPF #1252（Rose）確認，補齊加拿大家系 6 條目

作者確認 RPF #1252（主名 Rose）即 Everland 的 `leah-2019-05-17`，解掉原「出生園待查證 🚧」：Assiniboine Park Zoo 生（2019-05-17）、2022-12-01 移居 Everland。依新增成員流程自動補齊直系親屬（父、母、雙胞胎、祖父母；外祖母 `sachi-2012-06-18` 已存在）。

**來源**：
- https://redpandafinder.com/#profile/1252 (Rose/Leah)
- https://redpandafinder.com/#profile/438 (Tanvi)、#431 (Zorro)、#1253 (Poppy)、#435 (Tango)、#446 (Kayah)、#440 (Koko)、#433 (Kendji)、#89 (Seina)

**新增條目**：
- `tanvi-2017-06-13.md` — Tanvi タンヴィ（RPF #438），生於 2017-06-13，現居 Assiniboine Park Zoo；Leah・Poppy 之母
- `zorro-2013-07-01.md` — Zorro ゾロ（RPF #431），生於 2013-07-01（Granby），現居 Assiniboine Park Zoo；Leah・Poppy 之父
- `poppy-2019-05-17.md` — Poppy ポッピー（RPF #1253），生於 2019-05-17，現居 Assiniboine Park Zoo；Leah 雙胞胎
- `tango-2015-07-30.md` — Tango タンゴ（RPF #435），生於 2015-07-30，現居 Edmonton Valley Zoo；Tanvi 之父
- `kayah-2007-06-11.md` — Kayah カヤ（RPF #446），生於 2007-06-11，現居 Granby Zoo；Zorro 之母、`franken` 的 ½ 姊
- `koko-2000-06-25.md` — Koko 虎虎／ココ（RPF #440），茶臼山生、歿於 Granby（2017-07-05）；Zorro 之父、`seina` 雙胞胎。⚠️ RPF 記生日 2000-06-23，與雙胞胎 `seina-2000-06-25`（wiki 校訂）差兩天，暫從 Seina 的 6/25、條目內留 🚧 備注待作者裁定

**更新條目**：
- `leah-2019-05-17.md` — 補 rpf_id 1252、species styani、出生園與居住史、日文名 ローズ、英名 Rose/Lea、家族全補；去除 unverified
- `kendji-2015-06-22.md` — 解掉 🚧：出生園 Granby（2015-06-22）、經 Cincinnati（2016-10-27 – 2023-10-26）抵 Roger Williams（2023-10-26）；父母 Kayah × Koko、雙胞胎 Madeline（#444）；Micu 補 🌈
- `sakura-2013-07-01.md` — 母/父「不詳」補為 Kayah × Koko；補三胞胎 Zorro・Xia
- `sachi-2012-06-18.md` — 子女表 Tanvi 改 wikilink、註明配偶 Tango；引言補 Leah 外祖母
- `seina-2000-06-25.md` — 雙胞胎 Koko、父母 Liuxing・Yuu-Yuu 改 wikilink
- `liuxing-1997-06-16.md`、`yuu-yuu-1990-06-25.md` — 子女表 Koko 改 wikilink、性別 ♂ 補上
- `rina-2012-08-02.md` — 子女 Tango 改 wikilink（RPF #435 補上）
- `malikha-2004-06-08.md`、`franken-2012-06-11.md` — Kayah 改 wikilink
- `index.md` — 新增「海外個體（加拿大・Zorro × Tanvi 一家 → 韓國 Leah）」區塊（6 條目）；Leah・Sachi・Sakura 列更新；條目總數 545 → **551**
- `tools/build_db.py` — OFFICIAL_HOSTS 補 `witheverland.com`（Everland 官方部落格，Leah 來源上站）；並修 `_host()` 用 `lstrip("www.")`（按字元剝除）的 latent bug——`www.witheverland.com` 被剝成 `itheverland.com`，改用 `removeprefix("www.")`

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] update | 補 `kotarou-2005-07-08` 中文名 琥太郎

**來源**：
- 作者提供

**更新條目**：
- `kotarou-2005-07-08.md` — frontmatter 補 `chinese: 琥太郎`；標題改為 `# Kotarou（琥太郎）`

**重建**：`gen_residence` + `build_db` + `export_json`

---

## [2026-07-09] add | 補西山早期母獸 `ran-ran-1987-07-26`（蘭蘭），接上既有子女

**來源**：
- https://redpandafinder.com/#profile/774 (Ran-Ran)
- redpanda-lineage（#774：生 1987-07-26、歿 2009-06-03、♀、出生及終居西山；子女 #769/#772/#495/#598/#732/#733；配偶 #763 Yuu-Yuu）
- 社群整理「西山まとめ」(gid=1439000613) 指其為 `chao-chao-1991` 之母，經 lineage 核對屬實

**新增條目**：
- `ran-ran-1987-07-26.md` — Ran-Ran 蘭蘭（RPF #774），生於 1987-07-26，一生居鯖江市西山動物園，2009-06-03 老衰歿

**更新條目**：
- `chao-chao-1991-06-18.md` — 家族欄 母改 `[[ran-ran-1987-07-26]]`、父改 `[[yuu-yuu-1987-05-31]]`（原純文字）
- `yuu-yuu-1987-05-31.md` — 子女表 6 筆（Ten-Ten、Hana、Chao-Chao、Kaori、Chun-Chun、無名）母欄補 `[[ran-ran-1987-07-26]] #774`；Chao-Chao 改 wikilink
- `index.md` — Nyan-Nyan 家系新增 `ran-ran-1987-07-26`；條目總數 551 → **552**

**待查證**：蘭蘭雙親（西山まとめ 記為北京始祖 慶慶 × 秀秀）lineage 無記錄，暫未建父母條目。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] add | 補蘭蘭 × Yuu-Yuu 的 5 名子女（lineage 核對後建檔）

**來源**：
- redpanda-lineage 逐隻核對生日／居住史／血緣：`ten-ten`#769、`hana`#772、`kaori`#495、`sabatarou`#732（lineage 無名，名稱採「西山まとめ」）、`chun-chun`#733；皆為 #774 Ran-Ran × #763 Yuu-Yuu 之子女

**新增條目**：
- `ten-ten-1989-06-26.md` — 天天（RPF #769），西山→徳山，1989–2004
- `hana-1990-06-29.md` — 花（RPF #772），西山→大森山，1990–2005
- `kaori-1991-06-18.md` — 香（RPF #495），Chao-Chao 雙胞胎，西山→秋吉台，1991–2003
- `sabatarou-1992-06-22.md` — サバタロウ（RPF #732，lineage 無名），春春雙胞胎，西山→釧路，1992–2000
- `chun-chun-1992-06-22.md` — 春春（RPF #733），西山→池田，1992–2010

**更新條目**：
- `ran-ran-1987-07-26.md`、`yuu-yuu-1987-05-31.md` — 子女表 5 筆改 wikilink
- `chao-chao-1991-06-18.md` — 雙胞胎 Kaori 改 `[[kaori-1991-06-18]]`
- `index.md` — 新增 5 條目；條目總數 552 → **557**

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] add | 補平平血系 4 隻（lineage 核對後建檔），接上既有 Yan-Yan・Lala・Chata

**來源**：
- redpanda-lineage 逐隻核對：`pin-pin`#887（徳山→西山）、`takashi`#839、`hisashi`#773、`kou-kou`#1346（あやめ池→安佐→西山）
- 親子邊：#887→#822(Yan-Yan)/#839(Takashi)…；#839→#341(Lala)/#168(Chata)（母 #223 Cha-Cha）

**新增條目**：
- `pin-pin-1989-06-28.md` — 平平（RPF #887），西山種公，Yan-Yan(1992)・Takashi 之父，1989–2008
- `takashi-1993-07-19.md` — たかし（RPF #839），Pin-Pin 之子，與 Cha-Cha 育 Lala/Chata，1993–2012
- `hisashi-1993-06-30.md` — ヒサシ（RPF #773），西山，1993–2011
- `kou-kou-1988-06-22.md` — 好好（RPF #1346），あやめ池→安佐→西山，1988–2008

**更新條目**：
- `yan-yan-1992-06-19.md` — 父 `Pin-Pin` 改 `[[pin-pin-1989-06-28]]`
- `lala-2000-06-27.md`、`chata-2002-06-25.md` — 父 `Takashi #839` 改 `[[takashi-1993-07-19]]`；chata 全兄弟 Lala 改 wikilink
- `index.md` — 新增 4 條目；條目總數 557 → **561**

**待查證**：平平／たかし之母獸別、ヒサシ之母（鈴鈴 #777，lineage 無名）等尚待查證，暫以純文字記。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] add | 補西山血系 10 隻（lineage 核對後建檔），血系連結大致補齊

**來源**：redpanda-lineage 逐隻核對生日／居住史／血緣。

**新增條目**：
- `you-you-1987-07-26.md` — 陽陽（RPF #775），Ran-Ran 同胎手足，西山→茶臼山種公，1987–2007
- `rin-rin-1986-07-05.md` — 鈴鈴（RPF #777，lineage 無名），Hisashi 之母、Lili 同日出生，1986–2006
- `kozue-1991-07-04.md` 梢#891、`sai-sai-1992-06-19.md` 西西#885、`ryou-1992-07-13.md` 涼#892、`kouhei-1992-07-13.md` 康平#893（lineage 記♀）、`shimajirou-1993-07-19.md` しまじろう#840、`tomy-1995-06-24.md` トミー#894 — 皆 Pin-Pin 之子女
- `kousei-2000-06-27.md` コウセイ#128 — Takashi × Cha-Cha 之子、Lala 雙胞胎
- `kirara-2002-06-29.md` キララ#333 — Hisashi 之女

**更新條目**：
- `pin-pin-1989-06-28.md` — 子女表 6 筆改 wikilink
- `takashi-1993-07-19.md` — 子女 Kousei 改 wikilink
- `hisashi-1993-06-30.md` — 母改 `[[rin-rin-1986-07-05]]`、子女 Kirara 改 wikilink
- `ran-ran-1987-07-26.md` — 補同胎手足 `[[you-you-1987-07-26]]`
- `index.md` — 新增 10 條目；條目總數 561 → **571**

**未建（無法查證）**：北京始祖 秀秀／慶慶／胖胖，及誕誕・遊遊・愛愛・美美・吉吉・マリモ 等（lineage 無對應生日）；2026 韓國 レモン(ミルキー) lineage 尚無。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] fix+add | 更正：試算表有「生日」欄，先前誤讀成歿日

**背景**：作者指出「西山まとめ」有獨立的**生年月日欄（col2）**與**死亡日欄（col3）**；先前擷取誤取 col3 當生日，導致把有生日的個體誤列「無法查證」。經以生日欄＋redpanda-lineage 重新核對後補建。

**新增條目**：
- `chii-chii-1989-06-30.md` — 吉吉（RPF #771，lineage 名 Chii-Chii），Yuu-Yuu × Rin-Rin 之子，西山→甲府遊亀，1989–1995
- `marimo-1995-07-04.md` — マリモ（RPF #729，lineage 無名），Sabatarou 之女、Kou-Kou 之配偶，釧路→西山→姫路，1995–2008
- `aiai-1988-06-25.md` — 愛愛（生日依西山まとめ、lineage 無、RPF/父母待查），Pin-Pin 之配偶、平平血系 6 子之母，1988–2006

**更新條目**：
- `yuu-yuu-1987-05-31.md` — Chii-Chii 改 `[[chii-chii-1989-06-30]]`
- `rin-rin-1986-07-05.md` — 子女 チイチイ 改 wikilink
- `sabatarou-1992-06-22.md` — 補子女 `[[marimo-1995-07-04]]`
- `kou-kou-1988-06-22.md` — 補配偶 `[[marimo-1995-07-04]]`
- `pin-pin-1989-06-28.md` — 補配偶 `[[aiai-1988-06-25]]`
- `kozue`/`ryou`/`kouhei`/`shimajirou`/`tomy`/`takashi` 6 隻 — 母欄補 `[[aiai-1988-06-25]]`
- `index.md` — 新增 3 條目；條目總數 571 → **574**

**修正前述紀錄**：上一批日誌誤稱「レモン lineage 尚無」——實際 `lemon-2013-07-07`（旧名ミルキー）早在 wiki 且正確。

**仍未建**：北京始祖 秀秀／慶慶／胖胖（無生日）、メイメイ美美（生日欄空、lineage 無）；誕誕・遊遊（生日欄為 1986-07-05 疑共用值，待決定 slug）。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] add | 補 遊遊・誕誕（生日欄 1986-07-05，雙胞胎佐證）

**新增條目**：
- `yuyu-1986-07-05.md` — 遊遊（♀，慶慶×胖胖之女、Rin-Rin 雙胞胎妹、Ai-Ai 之姉），西山→神戸市立王子動物園，1986–2005；生日依西山まとめ、與 `rin-rin-1986-07-05`(lineage #777 確認同日)一致；lineage 無獨立記錄、RPF/父母待查；slug 採 `yuyu-` 以別於 you-you(陽陽)／yuu-yuu(友友)
- `tan-tan-1986-07-05.md` — 誕誕（性別待確認，慶慶×秀秀之子女、Lili 同日手足），幼逝於西山 1986–1987；生日依西山まとめ、lineage 無、RPF/父母待查

**更新條目**：
- `rin-rin-1986-07-05.md` — 補雙胞胎 `[[yuyu-1986-07-05]]`
- `ran-ran-1987-07-26.md`、`you-you-1987-07-26.md` — 補兄 `[[tan-tan-1986-07-05]]`
- `lili-1986-07-05.md` — 補同日手足 `[[tan-tan-1986-07-05]]`
- `index.md` — 新增 2 條目；條目總數 574 → **576**

**仍未建（無生日）**：北京始祖 秀秀／慶慶／胖胖、メイメイ美美。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] add | 補北京始祖三頭＋メイメイ（作者提供暫定生年），血系接到頂

**背景**：作者裁示——暫定生日＋待查證是本 wiki 既有作法（`YYYY` slug 合規），可先建再確認；並提供生年與性別。

**新增條目**：
- `shuu-shuu-1981.md` — 秀秀（♀，始祖母；生年 1981 作者暫定），北京動物園→西山，1981–1988
- `kei-kei-1982.md` — 慶慶（♂，始祖父；生年 1982 暫定、歿日不詳），北京動物園→西山
- `pan-pan-1983.md` — 胖胖（♀，始祖母；生年 1983 **推定**暫定），北京動物園→西山，1983–1990
- `mei-mei-1989-06-19.md` — 美美（♀；生日 1989-06-19 暫定、另說 1988），八木山→西山→江戸川，1989–2007

**更新條目**：
- `tan-tan-1986-07-05.md` — 性別補 ♂（作者提供）；父母接 `[[kei-kei-1982]]`／`[[shuu-shuu-1981]]`
- `lili-1986-07-05`、`ran-ran-1987-07-26`、`you-you-1987-07-26` — 補父母（慶慶×秀秀）
- `yuyu-1986-07-05`、`rin-rin-1986-07-05`、`aiai-1988-06-25` — 補父母（慶慶×胖胖）
- `sai-sai-1992-06-19.md` — 母補 `[[mei-mei-1989-06-19]]`
- `index.md` — 新增 4 條目；條目總數 576 → **580**

> 北京始祖血系自此接到頂（慶慶×秀秀、慶慶×胖胖兩系）；始祖生年皆為暫定、待園方 studbook／官方家系精確化，屆時只需改 slug 年份並修 wikilink。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-09] update | 補讀者投稿 IG 貼文一則（Fan-Fan 繁繁）

**背景**：讀者透過三語表單投稿照片，勾選「本人拍攝／本人貼文」，視同同意刊登。投稿未留暱稱，致謝名單不動。

**更新條目**：
- `fan-fan-2023-05-02.md` — instagram frontmatter 新增 `https://www.instagram.com/p/DajytwrkT-t/`（去除 `?igsh=` 追蹤參數、正規化為 `/p/<shortcode>/`；未含帳號，日後可用 `ig_audit.py --no-account` 補齊）

**重建**：`build_db` + `export_json`

---

## [2026-07-09] add | 圖鑑缺漏回報三筆：Karma（新加坡）＋ Fred・George（加拿大 Edmonton 雙胞胎）

**背景**：讀者透過三語表單回報三隻缺漏個體。Karma 附官方來源（Mandai 官網 Stars of Mandai）→ 直接採用。`Fred`／`George` 回報僅附 IG 貼文（非官方），但經 CBC News 與該園募款夥伴 Valley Zoo Development Society 佐證，且 `tango-2015-07-30` 條目原已列此二子（母欄記「另一母」）→ 補為正式條目並補齊母名。

**來源**：
- https://www.mandai.com/en/discover-mandai/events/stars-of-mandai/karma.html (Karma)
- https://www.cbc.ca/news/canada/edmonton/edmonton-valley-zoo-debuts-endangered-red-panda-cubs-fred-and-george-1.7385267 (Fred, George)
- https://www.buildingourzoo.com/red-pandas/ (Fred, George)

**新增動物園註冊表**：
- `data/zoos.json` — 新增 `河川生態園`（River Wonders，新加坡萬禮野生動物世界；canonical 河川生態園、en River Wonders）

**新增條目**：
- `karma-2013.md` — Karma（♂，喜馬拉雅亞種 fulgens），生於 2013-12，現居河川生態園；家系待查證
- `fred-2024-07-07.md` — Fred（♂，styani），生於 2024-07-07，Edmonton Valley Zoo；父 `tango`、母 `Kiki`、`george` 雙胞胎
- `george-2024-07-07.md` — George（♂，styani），生於 2024-07-07，Edmonton Valley Zoo；父 `tango`、母 `Kiki`、`fred` 雙胞胎

**更新條目**：
- `tango-2015-07-30.md` — 子女表 `George`／`Fred` 改為 wikilink、母欄由「另一母」補為 `Kiki`；引言補 2024 雙胞胎
- `index.md` — 新增「海外個體（新加坡・河川生態園）」分類收 `karma`；Edmonton 家族表補 `fred`／`george`；條目總數 580 → **583**

> ⚠️ Edmonton 母 `Kiki` 與日本個體 `kiki-2000-07-04`（♂）為同名不同隻，條目內已加注意同名。`Kiki` 目前無生日等資料，暫以純文字記錄、未建條目；祖父 `Kalden`（RPF #480）同。Karma 的 RPF id 未知，`rpf_id` 留空。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-11] update | 資料更正回報：Riku 歿日 2014-10-08 → 2015-11-08

**背景**：讀者（`楊桃`）透過三語表單回報 `riku-2004-07-13` 歿日有誤，附秋田市大森山動物園官方園報〈大森山コミュニケーション vol.105・特集レッサーパンダ〉。原歿日 2014-10-08 僅來源於 RPF（非權威）；官方園報為一手來源，依「官方來源可直接採用」原則採納並更正。

**來源**：
- https://www.city.akita.lg.jp/_res/projects/default_project/_page_/001/037/648/105p6.pdf (秋田市大森山動物園 官方園報 vol.105)

**更新條目**：
- `riku-2004-07-13.md` — `died` 2014-10-08 → `2015-11-08`；`zoos:` 居住訖日同步；引言歿日與享年（10→11 歲）、內文離世年（2014→2015）更新；`sources:` 新增官方園報 PDF

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-11] add | 圖鑑缺漏回報：新增 4 隻（官方來源）

**背景**：讀者透過三語「圖鑑缺漏」表單回報多筆缺少個體。經比對後，`Fred`／`George`／`Karma` 已在圖鑑（重複，不新增）；`アイ`（上野，無來源）與動物園「都江堰小熊貓森林公園」「天津动物园」（非官方／未附來源）標待查證。本批採納 4 筆**附官方一手來源**者，依「官方來源可直接採用」原則建立條目。回報者 `楊桃` 已在致謝名單，不重複列。

**來源**：
- https://www.city.kushiro.lg.jp/zoo/shoukai/1001527/1001528/1001554.html (釧路市動物園 官方個體介紹；コーアイ)
- https://www.city.akita.lg.jp/_res/projects/default_project/_page_/001/037/648/105p6.pdf (秋田市大森山動物園 官方園報 vol.105；飲飲・風)
- https://www.facebook.com/zounokuni/posts/686909551385606/ (市原ぞうの国 官方 Facebook；一郎)

**新增條目**：
- `koai-2004-06-10.md` — Koai コーアイ（♀，styani，RPF #25），生於 2004-06-10 よこはま動物園ズーラシア，2006-06-07 移居釧路市動物園現居；母 `pam`、父 `mii-mii`（美美 #359）、`gaia` 雙胞胎
- `in-in-2005-07-07.md` — In-In 飲飲（♀，styani），2005-07-07 生～2009-07-09 歿於秋田市大森山動物園ミルヴェ；母 `nana`、父 `Jen-Jen`（官方名單作「健健」，待作者確認）、與 `an-an`／`ma-ma` 同胎
- `kaze-2004-07-13.md` — Kaze 風（♂，styani），2004-07-13 生～2006-11-06 歿於秋田市大森山動物園ミルヴェ；母 `nana`、父同上、`riku` 雙胞胎
- `ichiro-2014-07-06.md` — Ichiro 一郎（♂，styani），2014-07-06 生於市原ぞうの国現居；父母待查證

**更新條目**：
- `gaia-2004-06-10.md`、`mii-mii-1994-06-26.md`、`pam-1997-06-26.md` — 子女／雙胞胎欄的 `Ko-ai` 純文字改為 `koai-2004-06-10` wikilink
- `riku-2004-07-13.md` — 雙胞胎 `Kaze` 純文字改為 `kaze-2004-07-13` wikilink
- `an-an-2005-07-07.md`、`ma-ma-2005-07-07.md` — 同胎補列 `in-in-2005-07-07`（原記為雙胞胎，實為同胎三手足）
- `index.md` — Sayuri 家族補 `kaze`；補漏新增段補 `in-in`／`koai`；新增「市原ぞうの国（一郎）」段收 `ichiro`；條目總數 583 → **587**；最後更新 2026-07-11

**待查證（未採用，非官方／資訊不足）**：
- `アイ`（恩賜上野動物園）— 無來源、無生日，且已有 `ai-1991-06-20`（上野のアイ），疑重複或資訊不足
- 動物園「都江堰小熊貓森林公園」— 僅小紅書／YouTube，無官網
- 動物園「天津动物园」— 未附來源連結（提及 `圖圖`／`小宝`／`团团`）
- `Katara`（→ Toledo Zoo）— 官方 FB 證實 2026/6 有三隻母個體進駐，但回報僅「11 歲」無確切生日，且與現有 `katara-2025-07-04`（另一隻幼獸）撞名，待補生日再建

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-11] update | 一郎 補家系（RPF #300 參考）

**背景**：作者提供 https://redpandafinder.com/#profile/300 供參考。RPF 為非權威來源，僅用於補空白家系；名稱仍從園方官方之「一郎」（RPF 誤記日文名為「一路」，不採）。

**更新條目**：
- `ichiro-2014-07-06.md` — 補 `rpf_id` 300、`rpf_url`、RPF 來源；家族補父 `kojirou-2010-07-14`（wikilink）、母 `Tomato`（無條目）、雙胞胎 `Ichiko`（無條目）；japanese 補 `イチロウ`；移除「父母待查證」，改標 RPF 參考待查證
- `kojirou-2010-07-14.md` — 子女表 `Ichiro` 由「RPF；無條目」改為 `ichiro-2014-07-06` wikilink
- `index.md` — 一郎行補父 `kojirou-2010-07-14` × `Tomato`、`Ichiko` 雙胞胎（RPF #300）

**重建**：`build_db` + `export_json`；audit --strict、check_twins

## [2026-07-11] add | 一郎家系補建：Tomato（母）、Ichiko（雙胞胎）

**背景**：接續一郎補家系，依作者指示建立其母與雙胞胎條目。資料來源為 Red Panda Finder（非權威，僅補空白、待官方佐證）。

**來源**：
- https://redpandafinder.com/#query/Tomato
- https://redpandafinder.com/#query/Ichiko

**新增條目**：
- `tomato-2007-07-21.md` — Tomato トマト（♀，styani），2007-07-21 生～2018-01-01 歿，市原ぞうの国；母 Choco-Choco、父 Min-Min（RPF 待查證）、與 `kojirou-2010-07-14` 育有 `ichiro`／`ichiko`；½ 手足連結既有 `ann`／`cafe`／`hanabi`／`latte`
- `ichiko-2014-07-06.md` — Ichiko イチコ（♀，styani），2014-07-06 生～2014-07-11 夭折，市原ぞうの国；父 `kojirou-2010-07-14`、母 `tomato-2007-07-21`、`ichiro` 雙胞胎

**更新條目**：
- `ichiro-2014-07-06.md` — 母 Tomato、雙胞胎 Ichiko 由純文字改為 `tomato-2007-07-21`／`ichiko-2014-07-06` wikilink
- `kojirou-2010-07-14.md` — 子女表 Ichiko 改 wikilink，補母 Tomato 連結
- `ann-2010-06-15.md`、`cafe-2013-06-11.md`、`hanabi-2011-07-09.md`、`latte-2013-06-11.md` — ½ 手足 `Tomato` 純文字改為 `tomato-2007-07-21` wikilink
- `index.md` — 「市原ぞうの国（一郎 一家）」段補 `ichiko`／`tomato`；條目總數 587 → **589**

> ⚠️ Tomato 出生園未明（RPF 僅載市原）；母 Choco-Choco、父 Min-Min、同胎 Banana（2007，非 `banana-1996-08-09`）、胞弟 Potato 及其餘子女 Miruku／Kurumi／Nako／Nana 皆待查證、暫無條目。

**重建**：`build_db` + `export_json`；audit --strict、check_twins

## [2026-07-12] add | 紫馬嶺新生龍鳳胎：飯糰、鬆餅

**背景**：作者提供——中山市紫馬嶺動物園 2026-06-05 誕生龍鳳胎，父 `wo-wo-tou`（窩窩頭）、母 `mian-bao`（麵包）。

**來源**：
- 作者提供（2026-07-12）

**新增條目**：
- `fan-tuan-2026-06-05.md` — 飯糰 Fan Tuan（♂，styani），生於 2026-06-05 中山市紫馬嶺動物園現居；與 `song-bing` 龍鳳胎；½ 姊 `bagel`（同父）、`mi-gao`（同母）
- `song-bing-2026-06-05.md` — 鬆餅 Song Bing（♀，styani），生於 2026-06-05 中山市紫馬嶺動物園現居；與 `fan-tuan` 龍鳳胎；½ 姊 `bagel`（同父）、`mi-gao`（同母）

**更新條目**：
- `wo-wo-tou.md` — 引言與子女表補 `fan-tuan`、`song-bing`（另一方親本 麵包）
- `mian-bao.md` — 引言與子女表補 `fan-tuan`、`song-bing`（另一方親本 窩窩頭）
- `index.md` — 紫馬嶺段補兩筆、園內隻數 5 → 7、父母說明更新；條目總數 589 → **591**；最後更新 2026-07-12

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-12] update | 讀者回報：貝果之母為米糕（作者確認採用）

**背景**：「圖鑑缺漏」收件匣 2026-07-11 其他建議回報「貝果的媽媽是米糕」（未附來源、未留名）。經作者確認後直接採用。

**更新條目**：
- `bagel-2024-07-12.md` — 母由「待確認」改為 `mi-gao-2021-06-05`（米糕）wikilink，補祖母（母方）`mian-bao`；sources 補作者確認（2026-07-12）
- `mi-gao-2021-06-05.md` — 引言與家族補子女 `bagel-2024-07-12`（貝果，父 `wo-wo-tou`）；sources 補作者確認
- `wo-wo-tou.md` — 子女表 貝果 另一方親本「不詳」改 `mi-gao-2021-06-05` wikilink；待查證移除「貝果之母」
- `index.md` — 米糕列補「貝果之母」；貝果列改「窩窩頭×米糕之女」、移除「母待查證」

**重建**：`build_db` + `export_json`；audit --strict、check_twins

## [2026-07-12] update | 資料更正回報兩筆：Asunaro 轉園日、飲飲讀音更名 Yum-Yum

**背景**：處理「資料更正」收件匣兩筆未處理回報（另兩筆 Ai、Riku 已於先前處理）。(1) `asunaro-2016-06-22` 釧路來園日，釧路市動物園官方個體頁證實為 2019-06-04（原記 2019-06-05），官方來源直接採用。(2) `in-in-2005-07-07` 名字回報：漢字名「飲飲」園方讀音為ヤムヤム（大森山官方園報），作者確認拼音不採中式 In-In，改為 Yum-Yum 並依規則更名 slug。回報者 `楊桃` 已在致謝名單，不重複列。

**來源**：
- https://www.city.kushiro.lg.jp/zoo/shoukai/1001527/1001528/1001554.html (釧路市動物園 官方個體介紹；アスナロ来園日 2019-06-04)
- https://www.city.akita.lg.jp/_res/projects/default_project/_page_/001/037/648/105p6.pdf (秋田市大森山動物園 官方園報 vol.105；ヤムヤム)

**更新條目**：
- `asunaro-2016-06-22.md` — `zoos:` 大島訖／釧路起 2019-06-05 → **2019-06-04**；`sources:` 補釧路官方頁；居住史表重生
- `in-in-2005-07-07.md` → 更名 **`yum-yum-2005-07-07.md`**：`name` In-In → **Yum-Yum**、`japanese` 補 **ヤムヤム**、舊拼音移入 `english_variants`；標題與引言同步；同步修正 wikilink（`an-an-2005-07-07.md`、`ma-ma-2005-07-07.md`、`index.md`）
- `index.md` — 該行改 `yum-yum-2005-07-07`、顯示名 Yum-Yum 飲飲（ヤムヤム）

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-12] add | 天津動物園：圖圖、小寶、團團（原待查證回報，作者提供資料採用）

**背景**：作者提供——天津動物園三隻：`tu-tu`（圖圖，♂，團團之父）、`xiao-bao`（小寶，♀，生於天津動物園，團團之母）、`tuan-tuan`（團團，♀，2023-06-06 生於天津動物園）。此前 2026-07-11 讀者「圖鑑缺漏」回報同三隻但未附來源、標待查證；本次由作者直接提供資料，據以建檔並解除待查證。天津動物園未登記，先於 `data/zoos.json` 新增（canonical `天津動物園`、天津市南開区、座標據 Wikipedia 39.0811/117.16、無官網）。

**來源**：
- 作者提供（2026-07-12）
- https://zh.wikipedia.org/zh-hans/天津动物园 （動物園座標／位置）

**新增條目**：
- `tu-tu.md` — 圖圖 Tu Tu（♂，styani），生年不詳，現居天津動物園；`tuan-tuan` 之父。查得生年後 slug 應更名 `tu-tu-YYYY`
- `xiao-bao.md` — 小寶 Xiao Bao（♀，styani），生年不詳，生於天津動物園現居；`tuan-tuan` 之母。查得生年後 slug 應更名 `xiao-bao-YYYY`
- `tuan-tuan-2023-06-06.md` — 團團 Tuan Tuan（♀，styani），2023-06-06 生於天津動物園現居；父 `tu-tu`、母 `xiao-bao`

**更新條目**：
- `data/zoos.json` — 新增 `天津動物園`（Tianjin Zoo，天津市南開区）
- `index.md` — 新增「海外個體（中國・天津動物園）」段收三筆；條目總數 591 → **594**

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-12] update | Karma 出生地更正（作者指出動物園有誤）＋補建 Hamilton 一家 4 條目

**背景**：作者指出 `karma-2013` 的動物園弄錯、要求重新驗證。查證結果：Karma 並非生於河川生態園——Hamilton Zoo（紐西蘭）公開命名活動與 Red Panda Network 記載其為 2012 年 Hamilton Zoo 三胞胎（Nima・Karma・Dawa，母 Tayla）之一；Mandai 2018-08-30 官方新聞稿記 Karma 該年 12 月滿 6 歲（→ 2012 年 12 月生）；RPF #970 記 2012-12-20 生於 Hamilton Zoo、2014-11-10 移居 River Wonders。Stars of Mandai 頁「2013 年生、出生起即居 River Wonders」為行銷頁錯誤（官方來源衝突，採出生園方＋新聞稿說）。現居 River Wonders 不變。另依作者：Mandai Wildlife Reserve 官方中文名為「萬態野生動物世界」（舊稱萬禮野生動物保護區），註冊表補別名。

**來源**：
- https://www.mandai.com/en/about-mandai/media-centre/feisty-red-panda-moves-into-river-safaris-giant-panda-forest.html (Mandai 官方新聞稿 2018-08-30)
- https://redpandanetwork.org/post/red-panda-cubs-at-hamilton-zoo-have-new-namesi (Hamilton Zoo 三胞胎命名)
- https://redpandafinder.com/#profile/970 (Karma；RPF 非權威、補精確日期)

**更新條目**：
- `karma-2013.md` → 更名 **`karma-2012-12-20.md`**：生日 2013-12 → **2012-12-20**、補出生園 **Hamilton Zoo**（2014-11-10 移居河川生態園）、`rpf_id` 970、japanese カルマ；家族補母 `tayla`、父 `chito`、三胞胎 `nima`・`dawa`；條目內注記 Mandai 官方頁矛盾、精確日期標 🚧
- `data/zoos.json` — 河川生態園 aliases 補「萬態野生動物世界」「萬禮野生動物保護區」（Hamilton Zoo／Auckland Zoo／National Zoo & Aquarium 原已在註冊表）

**新增條目**：
- `tayla-2007-12-08.md` — Tayla テイラ（♀，fulgens，RPF #964），生於坎培拉 National Zoo & Aquarium，2010 移居 Hamilton Zoo；Karma 三胞胎之母
- `chito-2002-12-18.md` — Chito（♂，fulgens，RPF #967），生於 Auckland Zoo，2006 移居 Hamilton Zoo；三胞胎之父（高齡，現況 🚧 待查證）
- `nima-2012-12-20.md` — Nima ニマ（♂，fulgens，RPF #968），Hamilton 三胞胎，2015-03-13 移居 National Zoo & Aquarium
- `dawa-2012-12-20.md` — Dawa ダワ（♂，fulgens，RPF #969），同上
- 其餘手足（RPF #954・#965・#966・#971・#972）待查證、暫無條目
- `index.md` — Karma 行改寫、新增「海外個體（紐西蘭・澳洲：Karma 一家）」段；條目總數 591 → **595**（加計作者同日新增之天津動物園 3 筆為 **598**）

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

## [2026-07-13] update | 讀者回報批次：大森山官方名單補漢字／讀音更正＋Anko・Roppo 轉園史＋IG 投稿回填 4 筆

**背景**：資料更正收件匣 6 筆（大森山 4 筆同源官方 PDF；Anko、Roppo 轉園 2 筆），作者確認官方來源直接採用。照片投稿收件匣 4 筆全數乾淨回填。

**來源**：
- https://www.city.akita.lg.jp/_res/projects/default_project/_page_/001/037/648/105all.pdf (秋田市大森山動物園官方名單)
- https://mainichi.jp/articles/20161105/k00/00e/040/193000c (毎日新聞：Anko 轉園)
- https://zoo.city.kyoto.lg.jp/zoo/news/20160616-20083.html (京都市動物園官方公告：Roppo 轉園)

**更新條目**：
- `riku-2004-07-13.md` — japanese 補漢字 **陸**（リク）
- `kaze-2004-07-13.md` → 更名 **`fuu-2004-07-13.md`**：官方名單讀音為**フウ**（風），name Kaze → **Fuu**、舊拼音 Kaze 留 english_variants；加與 `fuu-1998-07-04` 互相「注意同名」提示；`riku`、`index.md` 之 wikilink 同步改
- `an-an-2005-07-07.md` / `ma-ma-2005-07-07.md` — 母 Nana 純文字改 `nana-2001-07-13` wikilink；與 `yum-yum-2005-07-07` 標明**同日三胞胎**；父注記官方名單作「健健」待確認；sources 補官方 PDF
- `yum-yum-2005-07-07.md` — 手足標示改「三胞胎」
- `nana-2001-07-13.md` — 補「子女」表（riku・fuu 雙胞胎＋an-an・ma-ma・yum-yum 三胞胎）
- `anko-2013-06-22.md` — 補出生園**東京都立大島公園動物園**（2013-06-22 – 2016-11-02），2016-11-02 移居富山市ファミリーパーク（毎日新聞）；sources 補報導
- `roppo-2015-06-25.md` — 補出生園**京都市動物園**（2015-06-25 – 2016-06-22），2016-06-22 移居富山市ファミリーパーク（京都市動物園官方公告）；sources 補公告
- `index.md` — Riku 補漢字、卒年 2004–2014 更正為 2004–2015；Kaze 行改 Fuu；最後更新 2026-07-13（條目總數 598 不變）

**IG 投稿回填（照片收件匣 4 筆，Sheet I 欄待作者手動標記）**：
- `rei-fa-2019-07-12.md` — +1（DarD4IbD1j2，本人投稿）
- `fuumi-2007-07-11.md` — +1（DapulNTExjc，非本人、已取得原作者同意；原無 instagram 欄位，新增）
- `himawari-2017-07-13.md` — +1（DasR8RGk49u，本人投稿）
- `zun-2018-07-13.md` — +1（Das8PAeEzxA，本人投稿）

**致謝**：楊桃（Anko・Roppo 轉園回報）已在 contributors.json，不重複列；其餘回報者未留名。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-13] add | Pairi Daiza（比利時）Mohan 一家：圖鑑缺漏回報查證後新增

**來源**：
- https://www.pairidaiza.eu/en/news/animals-conservation/two-rare-red-pandas-born-at-pairi-daiza/ （園方新聞稿 2026-07-03，官方一手來源）
- https://redpandafinder.com/#profile/1312 (Mohan) / #1298 (Loha) / #1247 (Hui Hu) / #1058 (Himiko)（血系/生日/移居等空白補齊，非權威）

**背景**：圖鑑缺漏回報（Tally 2EVJlb）回報 Mohan（♂，2021-06-20，Pairi Daiza），附園方官網新聞稿。查證：新聞稿確認 Loha × Mohan 於 2026-06-25 產下雙胞胎幼崽，Mohan 為 Hui Hu × Himiko 之子，三代同堂。官方來源，直接採用。

**新增條目**：
- `mohan-2021-06-20.md` — Mohan（RPF #1312），生於 2021-06-20，現居 Pairi Daiza（生日以園方新聞稿為準；lineage 記 2021-07-22 存查）
- `loha-2020-06-06.md` — Loha（RPF #1298），生於 2020-06-06 柏林、2021 移居 Pairi Daiza（出生園：新聞稿泛稱 Berlin Zoo，lineage 記 Tierpark Berlin，採後者存查）
- `hui-hu-2019-06-22.md` — Hui Hu（RPF #1247），生於 2019-06-22 Chester Zoo、2020 移居 Pairi Daiza，別名 Firefox
- `himiko-2019-06-10.md` — Himiko（RPF #1058），生於 2019-06-10 Pairi Daiza

**修正**：初版誤將 lineage 帶的片假名轉寫填入 `japanese:`（Mohan モハン等），但四隻均為歐洲個體、與日本無關，已全數移除（含 Hui Hu 的 `japanese: 火狐`；火狐/Firefox 保留於內文別名）。

**未建條目（僅 lineage、非官方，暫列內文純文字待補）**：Mohan 雙胞胎 Minju 🌈（#1313）、Hui Hu 之父母 Nima/Koda 與雙胞胎 Tiang Tang、Himiko 之父母 Yin 🌈/Mojo 🌈、Loha × Mohan 之 2026 幼崽（尚未命名）。

**更新**：
- `data/zoos.json` — 補 location_ja 空白：Pairi Daiza 布呂熱萊特、Tierpark Berlin 柏林、Chester Zoo 柴郡
- `tools/gen_residence.py` — CFLAG 新增 Belgium 🇧🇪 / Germany 🇩🇪 / UK 🇬🇧
- `index.md` — 新增「海外個體（比利時・Pairi Daiza）」分類 4 筆；條目總數 598 → 602

**致謝**：回報者（Tally 回報 kdrJPdM）未於暱稱欄留名，不列入 contributors。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-14] update | 資料更正回報（Tally ODr777）：Nara 生日、Fuuka／Kazu／Shou-Shou／Gao-Gao 居住史

**來源**（回報者查證所附，均為官方一手來源，直接採用）：
- https://www.nhdzoo.jp/red-panda/kakeizu/index.html （静岡市立日本平動物園 家系圖）
- https://www.asahi.com/articles/ASV6121PGV61TZNB001M.html （朝日新聞：「徳山動物園には08年6月に来園。」）
- https://www.nhdzoo.jp/sp/news/naka.php?p=98 ・ https://x.com/nhdzoo/status/1744656071640379567 （日本平動物園 令和6年1月9日 Shou-Shou／Gao-Gao 對調公告）

**更新條目**：
- `nara-2000-07-13.md`（原 `nara-2000-07-17`）— 生日依日本平家系圖由 2000-07-17 更正為 **2000-07-13**；slug 隨之更名，安佐入園日與內文引言同步；相關 13 條目與 `index.md` 的 `[[wikilink]]` 一併改指新 slug（log 歷史條目保留原名不改）
- `fuuka-2006-06-02.md` — 徳山動物園入園日由 2006-06-30 更正為 **2008-06-30**（朝日新聞：08年6月来園；千葉市動物公園在園期間延長至 2008-06-30）；補 nhdzoo 家系圖與朝日來源
- `kazu-2019-07-02.md` — 補出生園 **富山市ファミリーパーク**（2019-07-02 – 2020-12-25），2020-12-25 移居日本平；🐣 出生地由日本平改為富山，內文引言同步；補 nhdzoo 家系圖來源
- `shou-shou-2017-07-15.md` — 日本平入園日由 2023-01-09 更正為 **2024-01-09**（令和6年）；內文與備注年份同步；補 nhdzoo 公告與 X 來源
- `gao-gao-2015-06-27.md` — 豊橋（Non Hoi Park）入園日由 2023-01-09 更正為 **2024-01-09**（與 Shou-Shou 同日對調）；內文年份同步；補 nhdzoo 公告與 X 來源
- `buna-2000-07-13.md`（原 `buna-2000-07-17`）— 連動更正：Buna（RPF #336）為 Nara 雙胞胎，生日隨之由 2000-07-17 更正為 **2000-07-13**（作者確認雙胞胎同生日）；slug 更名，安佐入園日與內文引言同步，相關 5 條目與 `index.md` 的 wikilink 改指新 slug；補 nhdzoo 家系圖來源
- `index.md` — 更新最後更新日；Nara／Buna wikilink 改指新 slug

**致謝**：楊桃（本批 5 筆更正回報）已在 `contributors.json`，不重複列。

**重建**：`gen_residence`（重生 602 檔居住史表格）+ `build_db` + `export_json`；audit --strict（🔴 0）、check_twins（0 錯誤）均通過

---

## [2026-07-14] add | Calgary Zoo 2023 窩雙胞胎 Anshu、Aahana（附命名由來）

**來源**（Calgary Zoo 官方 Facebook，官方一手來源）：
- https://www.facebook.com/thecalgaryzoo/posts/726496149521692 （命名公布貼文，2023-11-08）
- https://www.facebook.com/thecalgaryzoo/posts/1433323718838928 （Anshu 三歲生日貼文，2026-06-18）

**新增條目**：
- `anshu-2023-06-18.md` — Anshu ♂，生於 2023-06-18，現居 Calgary Zoo；母 `udaya`、父 `linus`，`ravi`／`sundari` 之弟。命名尼泊爾語「ray of sun」（讀音 UN-shoe）
- `aahana-2023-06-18.md` — Aahana ♀，Anshu 雙胞胎姊妹；命名尼泊爾語「first rays of the sun」（讀音 a-HAW-na）。兩名經公眾票選、延續家族「太陽」主題（母 Udaya=dawn、兄 Ravi=sun）

**更新條目**：
- `udaya-2019-06-20.md`、`linus-2018-06-23.md` — 子女表與引言補 2023 窩
- `ravi-2022-06-14.md`、`sundari-2022-06-14.md` — 家族補同父母弟妹
- `index.md` — 海外個體（加拿大）新增 2 筆；條目總數 602 → 604

**備注**：兩隻尚未收錄於 Red Panda Finder／redpanda-lineage，故無 rpf_id；父 `linus` 依同窩配對與官方稱 Ravi 為其「brother」推定。

**重建**：`gen_residence` + `build_db` + `export_json`；audit --strict、check_twins

---

## [2026-07-14] add | Jen-Jen 健健（大森山 5 子女之父，RPF #475）

**來源**：
- https://redpandafinder.com/#profile/475 (Jen-Jen)
- https://www.city.akita.lg.jp/_res/projects/default_project/_page_/001/037/648/105p6.pdf （秋田市大森山動物園官方名單）

**新增條目**：
- `jen-jen-1995-07-06.md` — Jen-Jen ジェンジェン／健健（RPF #475）♂，生於 1995-07-06 周南市徳山動物園，1997-04-08 移居秋田市大森山動物園ミルヴェ，歿 2005-12-25；`mii-mii-1992-08-07` 之子，與 `nana-2001-07-13` 育有 `riku`／`fuu`（2004 雙胞胎）與 `an-an`／`ma-ma`／`yum-yum`（2005 三胞胎）。生日不確定，暫依 RPF 建立

**更新條目**：
- `riku-2004-07-13.md`、`fuu-2004-07-13.md`、`an-an-2005-07-07.md`、`ma-ma-2005-07-07.md`、`yum-yum-2005-07-07.md` — 父由純文字「Jen-Jen（待確認）」改為 `jen-jen-1995-07-06` wikilink，移除「待作者確認是否為同一隻」提示（作者確認 健健＝ジェンジェン＝RPF #475）
- `mii-mii-1992-08-07.md` — 子女表 Jen-Jen 改 wikilink
- `ken-ken-2006-07-18.md` — 半血緣手足 Jen-Jen 改 wikilink
- `index.md` — 新增 Jen-Jen；條目總數更新為 605

## [2026-07-14] unhide | 恢復 `takeru` 上站（作者裁定，附官方家系圖佐證）

作者提供日本平動物園官方家系圖，確認 `takeru`（タケル，RPF #896）資料無誤，裁定恢復上站——反轉 2026-07-02「未滿一歲夭折暫時隱藏」對此隻的處置（其餘 4 筆維持隱藏）。條目內容本就完整正確（♂🌈、styani、2015-07-29 生於静岡市立日本平動物園、雙胞胎 `yamato`、父 `taku`🌈 母 `sea`🌈、2015-12-17 幼逝，存活 141 天），本次僅移出 `_hidden/`、還原連結、補官方來源。

**來源**：
- https://redpandafinder.com/#profile/896 (Takeru タケル)
- https://www.nhdzoo.jp/red-panda/kakeizu/index.html (日本平動物園 官方家系圖)

**恢復條目（移出 `wiki/_hidden/` → `wiki/`）**：
- `takeru-2015-07-29.md` — Takeru タケル（RPF #896），♂🌈，`sea`🌈 × `taku`🌈 之子，`yamato` 雙胞胎，2015-07-29 生、2015-12-17 幼逝，終居静岡市立日本平動物園

**更新條目**：
- 還原指向 `takeru` 的 `[[wikilink]]`（先前隱藏時改為純文字）：`yamato-2015-07-29.md`、`taku-2010-06-15.md`、`sea-2010-07-19.md`、`miho-2013-07-09.md`、`matsuba-2014-07-17.md`、`maruko-2018-07-11.md`、`maruo-2018-07-11.md`、`nico-2017-06-23.md`
- `takeru-2015-07-29.md` — sources 補官方家系圖連結
- `index.md` — 全血緣兄弟姊妹小節新增 Takeru 列、還原 Yamato 列描述連結；條目總數 605 → 606；`_hidden/` 6 → 5

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-14] rule+unhide | 修訂幼逝收錄原則；恢復 `tsubasa`、`wu-tan` 上站

**規則變更（作者指示）**：夭折（未滿一歲）個體只要**有正式命名**即照常收錄上站；僅「從未取名、以佔位名 `Baby`／`赤ちゃん` 登錄」者才續藏 `wiki/_hidden/`。取代 2026-07-02「未滿一歲一律暫藏」。已寫入 `CLAUDE.md`「注意事項」。回題適用：恢復兩隻已命名幼逝個體上站；未命名的 `baby-kiku`／`baby-luna` 續藏；`sokka`（資料未核實，非本規則範圍）續藏。

**來源**：
- https://redpandafinder.com/#profile/278 (Tsubasa つばさ)
- https://redpandafinder.com/#profile/241 (Wu-Tan ウータン)

**恢復條目（移出 `wiki/_hidden/` → `wiki/`）**：
- `tsubasa-2017-07-08.md` — Tsubasa つばさ（RPF #278），♂🌈，fulgens，`cinnamon`×`olivia`🌈 之長子，與 `kodama`／`kagayaki` 三胞胎，2017-07-08 生、2018-02-01 幼逝，熱川バナナワニ園（⚠️ 同名，另有 `tsubasa-2006-06-20`）
- `wu-tan-2018-06-21.md` — Wu-Tan ウータン（RPF #241），♂🌈，styani，`oolong`×`jasmine`🌈 之子，2018-06-21 生、2018-07-29 幼逝（38 天），京都市動物園

**更新條目**：
- 還原指向兩隻的 `[[wikilink]]`（隱藏時改純文字）：Tsubasa → `cinnamon-2009-07-12`、`olivia-2011-08-10`、`kodama-2017-07-08`、`kagayaki-2017-07-08`、`yotsuba-2016-06-25`、`mitsuba-2016-06-25`、`akatsuki-2018-07-25`、`akebono-2018-07-25`、`asahi-2018-07-25`；Wu-Tan → `oolong-2011-06-05`、`jasmine-2010-07-14`、`mutan-2014-06-19`、`puerh-2015-06-25`、`roppo-2015-06-25`、`mugi-2015-07-13`
- `kodama-2017-07-08.md`／`kagayaki-2017-07-08.md` — 移除「三胞胎第三隻 Tsubasa 幼逝、暫存 `_hidden/`」的過時註記（Tsubasa 已復原，三胞胎齊全）
- `index.md` — Cinnamon 家族新增 Tsubasa 列、Oolong×Jasmine 兄弟新增 Wu-Tan 列；條目總數 606 → 608；`_hidden/` 5 → 3
- `CLAUDE.md` — 「注意事項」新增幼逝收錄原則

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-14] add | 蘋果籽制度首批：熊本 Shin-Fa 第二子＋西山 Kanoko 雙胞胎（3 筆佔位條目）

**說明**：依本日新訂「當季寶寶佔位條目：蘋果籽」制度建檔（父母確認＋生日確認＋在世＋未命名，直接上站）。三筆均為園方官方公告（X 官方帳號），依「官方來源可直接採用」原則逕行建檔；RPF 均尚未建檔，`rpf_id` 待補。

**來源**：
- https://x.com/kumamotocityzoo/status/2062708738474344721 (熊本市動植物園官方：シンファ 5/27 產子，父かぼす)
- https://kumanichi.com/articles/1999252 (熊本日日新聞：6/4 體重 286g、秋季公開預定)
- https://x.com/nishiyama_zoo/status/2076501885012549978 (鯖江市西山動物園官方：かのこ 6/26 產雙胞胎，父ライト，其一人工哺育)

**新增條目**：
- `apple-seed-shin-fa-2026-05-27.md` — 蘋果籽（未命名、性別待確認），`shin-fa-2019-06-19` × `kabosu-2018-06-28` 之第二子（`ako` 全血緣弟妹），生於 2026-05-27，現居熊本市動植物園
- `apple-seed-1-kanoko-2026-06-26.md` — 蘋果籽1號（未命名、性別待確認），`kanoko-2016-06-24` × `light-2013-07-18` 之子，生於 2026-06-26，かのこ親自育兒，現居鯖江市西山動物園
- `apple-seed-2-kanoko-2026-06-26.md` — 蘋果籽2號（未命名、性別待確認），同上之雙胞胎，出生後不久改人工哺育

**更新條目**：
- `shin-fa-2019-06-19.md`／`kabosu-2018-06-28.md` — 家族關係補第二子（蘋果籽）
- `ako-2023-06-01.md` — 補全血緣弟妹（蘋果籽）
- `kanoko-2016-06-24.md` — 子女表 3→5 隻；`kaede`／`kaito` 純文字改 wikilink；補父別註記（Piisuke 父 `taiyo`、其餘父 `light`）
- `light-2013-07-18.md` — 子女表改「母：kanoko」並 wikilink 化 `kaede`／`kaito`，補 2026 雙胞胎
- `index.md` — Taofa 第三代補蘋果籽、Kanoko × Light 家族補蘋果籽1號2號、Kabosu 說明更新；條目總數 608 → 611

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-14] add | Pairi Daiza：Loha × Mohan 雙胞胎蘋果籽（2 筆佔位條目）

**說明**：讀者回報 Pairi Daiza 誕生雙胞胎，附園方官方新聞稿（2026-07-03），依「官方來源可直接採用」原則逕行建檔。回報父名寫作 "Moken"，經核對園方新聞稿為 **Mohan**（生日 2021-06-20 與既有條目 `mohan-2021-06-20` 一致，同一隻）。兩隻寶寶未命名、性別未公布，依蘋果籽制度建佔位條目；序號 1／2 為暫定（園方未區分個體）。RPF 均尚未建檔，`rpf_id` 待補。

**來源**：
- https://www.pairidaiza.eu/en/news/animals-conservation/two-rare-red-pandas-born-at-pairi-daiza/ (Pairi Daiza 官方新聞稿：Loha 6/25 晚間產下雙胞胎)

**新增條目**：
- `apple-seed-1-loha-2026-06-25.md` — 蘋果籽1號（未命名、性別待確認），`loha-2020-06-06` × `mohan-2021-06-20` 之子，生於 2026-06-25，現居 Pairi Daiza
- `apple-seed-2-loha-2026-06-25.md` — 蘋果籽2號（未命名、性別待確認），同上之雙胞胎

**更新條目**：
- `loha-2020-06-06.md`／`mohan-2021-06-20.md` — 子女表「（尚未命名，雙胞胎）」改為兩筆蘋果籽 wikilink
- `index.md` — Pairi Daiza 家族補蘋果籽1號、2號；條目總數 611 → 613

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-14] add | Xia（RPF #430）與 Kayah × Koko 家其他成員（12 筆）

**說明**：依使用者提供的 RPF #430 建立 `xia`，並依「直系親屬自動補齊」建立其三胞胎兒子、兄弟姊妹與外祖父。資料來源僅 RPF（線索性質）：Akito／Pip 的出生園、Kachin 的居住園 RPF 無記錄，依親屬居住史推定並標 🚧；Koko × Lala 為 Edmonton 五女之父母係依 RPF 補空（原 Koko 記「另一母」、Lala 記「父不詳」），標 🚧 待官方佐證。Stellar 的 lineage 漢字名「恒星」依非日本個體規則未入 `japanese`，疑中文名待作者確認。所有新條目均非日本個體，RPF 假名轉寫一律未採用。

**來源**：
- https://redpandafinder.com/#profile/430 (Xia)
- https://redpandafinder.com/#profile/429 (Akito)、#428 (Itsuki)、#427 (Xing)
- https://redpandafinder.com/#profile/442 (Cassie)、#312 (Stellar)、#443 (Pip)、#383 (Tai)、#441 (Sha-Lei)
- https://redpandafinder.com/#profile/418 (Dash)、#444 (Madeline)、#848 (Kachin)

**新增條目**：
- `xia-2013-07-01.md` — Xia（RPF #430），`kayah` × `koko` 三胞胎之一，生於 2013-07-01 Granby，現居 Greater Vancouver Zoo（🚧 2021-10 移居日期 lineage 標不確定）
- `akito-2015-06-22.md` — Akito（RPF #429），`xia` × Rufus 三胞胎之一，2015–2017 🌈（🚧 居住史推定 Assiniboine）
- `itsuki-2015-06-22.md` — Itsuki（RPF #428），同上三胞胎，2017 移居 Memphis Zoo
- `xing-2015-06-22.md` — Xing（RPF #427），同上三胞胎，2015–2020 🌈，歿於 Memphis
- `cassie-2007-06-26.md` — Cassie（RPF #442），`koko` × `lala` 之女、`stellar` 雙胞胎，現居 Safari Niagara
- `stellar-2007-06-26.md` — Stellar（RPF #312），`cassie` 雙胞胎，2007–2017 🌈，終居森林公園動物園
- `pip-2008-05-26.md` — Pip（RPF #443），`tai` 雙胞胎，2008–2020 🌈（🚧 居住史推定 Edmonton）
- `tai-2008-05-26.md` — Tai（RPF #383），`pip` 雙胞胎，2008–2022 🌈，終居 Henry Vilas Zoo
- `sha-lei-2009-06-13.md` — Sha-Lei（RPF #441），2009–2022 🌈，終居 Roger Williams Park Zoo
- `dash-2012-06-06.md` — Dash（RPF #418），`kayah` × Dusk（#447）之子，現居 Milwaukee County Zoo
- `madeline-2015-06-22.md` — Madeline（RPF #444），`kendji` 雙胞胎，現居 Greensboro Science Center
- `kachin-1995-05-31.md` — Kachin（RPF #848），`kayah` 之父，1995–2011 🌈（🚧 居住園不詳）

**更新條目**：
- `kayah-2007-06-11.md` — 父 `kachin` wikilink 化；子女表 Dash／Xia／Madeline 改 wikilink、Dash 父補 Dusk（#447）
- `koko-2000-06-25.md` — 子女表 10 隻全 wikilink 化；Edmonton 五女之母補 `lala`（依 RPF 🚧）
- `lala-2000-07-04.md` — 子女表「父不詳」改父 `koko`（依 RPF 🚧）、五女 wikilink 化
- `zorro-2013-07-01.md`／`sakura-2013-07-01.md` — 三胞胎 Xia、兄弟姊妹 Madeline 等改 wikilink
- `kendji-2015-06-22.md` — 雙胞胎 `madeline` 與 ½ 兄弟姊妹六隻改 wikilink
- `malikha-2004-06-08.md` — 子女表 Kayah row 父 `kachin` wikilink 化
- `index.md` — 新增「海外個體（加拿大・Xia 與 Kayah × Koko 家其他成員）」一節（12 筆）；Zorro row 的 Xia 改 wikilink；條目總數 613 → 625

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-14] fix | 動物園註冊表：合併重複的 Safari Niagara／Safari Niagra

**說明**：`data/zoos.json` 有兩筆同一座園——「Safari Niagra」（lineage 拼法，#68，帶完整資料，`maki` 在用）與「Safari Niagara」（正確拼法，空殼，`malikha`／`cassie` 在用）。經作者確認合併：正確拼法 **Safari Niagara** 為 canonical，承接 lineage_id 68、中文名、座標、官網等全部資料；`map` 更新為作者提供的地址連結（2821 Stevensville Rd, Stevensville, ON；https://goo.gl/maps/tarQmaigJpsyb8iW7）；舊拼法「Safari Niagra」降為 alias 後刪除該筆。註冊表 341 → 340 座。

**更新條目**：
- `data/zoos.json` — 兩筆合併為一筆（Safari Niagara，alias: Safari Niagra）
- `maki-2007-06-14.md` — frontmatter zoos／tag／內文 Safari Niagra → Safari Niagara
- `index.md` — Maki row 園名改拼法
- `malikha-2004-06-08.md`／`cassie-2007-06-26.md` — 居住史表格「地點」由合併後註冊表自動帶入（原空白）

**重建**：`gen_residence` + `build_db` + `export_json`（未匹配園名 0 種；audit --strict、check_twins 均通過）

## [2026-07-14] add | 羽村：梨梨 × アル 2026-06-28 寶寶（蘋果籽佔位）

**來源**：
- https://hamurazoo.jp/news/detail.html?CN=430019（園方 2026-07-08 公告，官方來源）

**新增條目**：
- `apple-seed-rii-rii-2026-06-28.md` — 蘋果籽（佔位，未命名），`rii-rii`（#236）× `aru`（#195）第二子，生於 2026-06-28 羽村市動物公園；性別待確認、展示待續報；RPF 未建檔，rpf_id 待補

**更新條目**：
- `rii-rii-2018-07-11.md` — 引言改育有二子；子女表加蘋果籽
- `aru-2013-08-15.md` — 引言改育有三子；子女表加蘋果籽
- `takenoko-2024-06-14.md` — 補全血緣弟妹連結
- `luka-2016-06-15.md` — 補 ½ 弟妹連結
- `index.md` — Aru 家族子女表加蘋果籽；條目總數 625 → 626

## [2026-07-14] add | 泡泡：甜甜的雙胞胎兄弟（上海動物園）

**來源**：
- http://www.shanghaizoo.cn/ （沿用 `tian-tian` 之來源；官方個體佐證待補）

**新增條目**：
- `pao-pao-2024-06-23.md` — 泡泡 Pao Pao（♂），生於 2024-06-23 上海動物園，`zhuang-zhuang`（壯壯）× `niu-niu`（妞妞）之子，與 `tian-tian`（甜甜）為雙胞胎；甜甜 2026-06 移居台北，泡泡留上海

**更新條目**：
- `tian-tian-2024-06-23.md` — 引言與家族補雙胞胎 `pao-pao`
- `fu-fu-2023-06-24.md`／`mei-mei-2023-06-24.md` — 兄弟姊妹加 `pao-pao`
- `niu-niu.md`／`zhuang-zhuang.md` — 子女表加 `pao-pao`
- `index.md` — 上海動物園區加泡泡；條目總數 626 → 627

**重建**：`gen_residence` + `build_db` + `export_json`

## [2026-07-15] add | Kiki（Edmonton Valley Zoo）— Fred・George 之母

**來源**：
- https://www.instagram.com/edmontonvalleyzoo/p/DAJTP_9PnmN/ （Edmonton Valley Zoo 官方 IG，介紹「Kiki, the mom」；官方來源）
- https://redpandafinder.com/#profile/998 (Kiki)

**新增條目**：
- `kiki-2019-06-07.md` — Kiki（RPF #998，♀），生於 2019-06-07 Milwaukee County Zoo，2021-11-03 依 SSP 移居 Edmonton Valley Zoo 與 `tango` 配對；2024-07-07 產下雙胞胎 `fred`／`george`。父 `dash`（#418，已在 wiki）；母 Dr. Erin Curry（RPF #392，RPF 佔位名，未建條目）

**更新條目**：
- `george-2024-07-07.md`／`fred-2024-07-07.md` — 母 `kiki` 由純文字改 wikilink（引言、同名提示、家族欄）
- `tango-2015-07-30.md` — 引言與子女表的 `kiki` 改 wikilink
- `dash-2012-06-06.md` — 新增子女表，列 `kiki`（wikilink）、Dr. Lily（#419）、Cinder（#1379，後二者未建條目）
- `index.md` — 加拿大 Zorro × Tanvi 一家一節新增 Kiki row；Fred/George row 的 Kiki 改 wikilink；條目總數 627 → 628

**備注**：依作者指示只補 Kiki 本人並接上既有連結；其母系（Dr. Erin Curry #392）、外祖父母（Lin #390🌈、Rover #590🌈）與全血緣手足（Dr. Lily #419、Cinder #1379）皆為 RPF 佔位/玩笑名、無官方佐證，暫不建檔。

## [2026-07-15] update | Sayuri 補假名

**更新條目**：
- `sayuri-2016-07-13.md` — `japanese` 由「小百合」補為「小百合（さゆり）」（漢字＋假名）

---

## [2026-07-15] add | 新增 Mebo 一家（Memphis → 美國各地）

**來源**：
- https://redpandafinder.com/#profile/1419 (Mebo)
- https://redpandafinder.com/#profile/323 (Hazel)
- https://redpandafinder.com/#profile/1418 (Enoki)

**新增條目**：
- `mebo-2023-06-13.md` — Mebo（RPF #1419），♀，生於 2023-06-13，Memphis Zoo 出生、2024 移居 San Francisco Zoo；曾用名 Doza／Marsala
- `hazel-2016-06-14.md` — Hazel（RPF #323），♀，生於 2016-06-14，Cincinnati 生 → 森林公園動物園 → 現居 Memphis Zoo；`itsuki` 之配偶、Mebo／Enoki 之母
- `enoki-2023-06-13.md` — Enoki（RPF #1418），♂，生於 2023-06-13，`mebo` 之雙胞胎，2024 移居森林公園動物園（西雅圖）；曾用名 Debree

**更新條目**：
- `itsuki-2015-06-22.md` — 補配偶 `hazel` 與子女 `mebo`／`enoki`
- `zan-2020-05-25.md` — 補 🚧 待查證註記：RPF 記其母為 `hazel`，若屬實則與 `mebo`／`enoki` 為半血緣手足（父系存疑）
- `index.md` — 海外個體區新增 Hazel／Mebo／Enoki；條目總數更新為 631

**備注**：Mebo 一家為美國個體、無日本居住史，故不採 RPF 的 `ja.name`（メボ等機械轉寫）為 `japanese`。Hazel 較早期產仔（Zeya #325、Ila #324🌈、Tián #1172、`zan` #1171）RPF 記父為 Yukiko #313，惟該 ID 對應 `yukiko-2005-06-23` 記為 ♀、與父系角色矛盾，暫標待查證未建檔。

## [2026-07-15] add | 新增柔柔、栗子（香港海洋公園，皆已歿）

**來源**：
- https://corporate.oceanpark.com.hk/tc/media-partnerships/press-release/ocean-park-s-beloved-red-panda-rou-rou-bids-farewell-to-visitors (柔柔歿訊，園方公告)
- https://redpandafinder.com/#profile/931 (柔柔)
- https://www.facebook.com/photo?fbid=10151628367866390 (栗子，讀者所附)
- https://redpandafinder.com/#profile/933 (栗子)

**新增條目**：
- `rou-rou-2008-07-09.md` — 柔柔 Rou-Rou（RPF #931），♀，生於 2008-07-09，2009-03-22 由成都移居香港海洋公園，歿於 2026-03-17（享年 17，園方公告）
- `li-zi-2008-06-15.md` — 栗子 Li-Zi／Chestnut（RPF #933），♀，生於 2008-06-15 🚧，2009 移居香港海洋公園，歿於 2013-06-15；生日與居住史僅見非官方來源，標待查證

**更新條目**：
- `tai-shan-2008-06-14.md` — 柔柔純文字改 `[[rou-rou-2008-07-09]]` wikilink
- `cong-cong-2008-06-11.md` — 柔柔改 wikilink；歿日依園方公告由 2026-03-16 更正為 2026-03-17
- `index.md` — 香港區新增柔柔、栗子；條目總數更新為 633
- `data/contributors.json` — 新增致謝 Gaia（回報柔柔、栗子）

**備注**：兩者皆為成都出生、無日本居住史，故不採 RPF 的 `ja.name`（ロウロウ／リジ 機械轉寫）為 `japanese`；ja.othernames 的漢字實為中文名，放 `chinese`。柔柔歿日以園方公告 2026-03-17 為準（RPF 記 2026-03-16）。

## [2026-07-15] update | 蘋果籽（rii-rii × aru 之二子）補性別

**更新條目**：
- `apple-seed-rii-rii-2026-06-28.md` — 依作者確認補性別：`sex` 空白→male、tags 加 `male`、引言加 ♂、移除「性別待確認」字樣（仍為未命名佔位條目）
- `index.md` — 該蘋果籽性別欄 ？→♂

**追記（同日）**：性別依園方官方 IG @hamurazoo.official（2026-07-14 貼文 https://www.instagram.com/p/DaywLHLSJcZ/ ，「雌雄を確認…オスでしたぁ」）確認為雄性，屬園方官方公告；已加入 `instagram:` 展示與 `sources:`。

## [2026-07-15] add | 新增燑燑（澳門石排灣郊野公園，已歿）

**來源**：
- https://www.macaotourism.gov.mo/en/sightseeing/gardens/seac-pai-van-park (澳門旅遊局石排灣郊野公園)
- http://www.gcs.gov.mo/news/detail/zh-hant/N16KPhBKiN (澳門政府新聞局)

**新增條目**：
- `tongtong-2013-07-02.md` — 燑燑 Tongtong，♀，2013-07-02 生於成都大熊貓繁育研究基地，2016 贈澳、移居澳門石排灣郊野公園珍稀動物館，與 `loklok` 同為澳門保育大使；2021-09-08 病逝

**更新條目**：
- `loklok-2013-07-02.md` — 配偶燑燑純文字改 `[[tongtong-2013-07-02]]` wikilink（內文與家族欄）
- `index.md` — 澳門區新增燑燑；條目總數更新為 634

**備注**：燑燑為成都出生、無日本居住史，不採 RPF 的 `ja.name` 為 `japanese`；歿日 2021-09-08 沿用既有 `loklok` 條目所載。2016 贈澳年份與 `loklok` 同批，確切異動日期待進一步查證。

---

## [2026-07-15] update | 更正 `fu-fu-2023-06-24`、`mei-mei-2023-06-24` 親本

**說明**：依作者更正，上海動物園的富富、美美（2023-06-24 雙胞胎）之母非妞妞，而是「小白」；父暫列不詳。此小白為上海個體，與柳州市動物園的 `xiao-bai`（白桃之母）為不同個體、尚未建檔，故母欄以純文字列出並標 🚧 待查證，不誤連至柳州小白條目。妞妞、壯壯仍為 2024 胎甜甜、泡泡之父母，不受影響。

**更新條目**：
- `fu-fu-2023-06-24.md` — 父 `zhuang-zhuang`→不詳、母 `niu-niu`→小白（純文字＋待查證）；引言改寫；移除甜甜/泡泡兄弟姊妹（非同父母）
- `mei-mei-2023-06-24.md` — 同上
- `niu-niu.md` — 子女表移除富富、美美（保留甜甜、泡泡）
- `zhuang-zhuang.md` — 子女表移除富富、美美（保留甜甜、泡泡）
- `tian-tian-2024-06-23.md` — 兄弟姊妹移除富富、美美
- `pao-pao-2024-06-23.md` — 兄弟姊妹移除富富、美美
- `index.md` — 富富、美美說明改為「母小白（上海）、父不詳」，移除「壯壯×妞妞」「甜甜之姊」

**追記（同日）**：作者確認母為小白（上海），並指示**僅以名字記錄、不為小白另設頁面**（故母欄維持純文字、不 `[[wikilink]]`，亦不誤連柳州 `xiao-bai`）。父仍不詳、待查。

---

## [2026-07-15] add | 建立上海小白條目、富富／美美母欄改 wikilink

**說明**：接續上一筆，作者改為要求為上海的小白建檔。因生日不詳、`xiao-bai` slug 已被柳州個體占用，依作者稱呼「上海小白」採地點後綴 slug `xiao-bai-shanghai`。查得生日後可再更名為 `xiao-bai-YYYY`。

**新增條目**：
- `xiao-bai-shanghai.md` — 小白 Xiao Bai，♀，生年不詳，現居上海動物園；富富・美美之母，出身／父母待查證

**更新條目**：
- `fu-fu-2023-06-24.md` — 母欄由純文字「小白」改為 `[[xiao-bai-shanghai]]`（引言、待查證註、家族三處）
- `mei-mei-2023-06-24.md` — 同上
- `xiao-bai.md`（柳州）— 注意同名註加入上海 `xiao-bai-shanghai`
- `index.md` — 上海動物園區新增小白；條目總數 634→635

**待辦**：小白（上海）生日、出身、父母及富富／美美之父仍待查。

---

## [2026-07-15] add | 廈門靈玲動物王國 飛飛×豆豆一家（含三胞胎沙沙・茶茶・面面）

**來源**：
- 作者提供（官方來源待補）

**新增條目**：
- `fei-fei-xiamen.md` — 飛飛 Fei Fei，♂🌈，三胞胎之父，歿於 2024-08；生年不詳（撞名廣州 `fei-fei` 霏霏，以園區消歧）
- `dou-dou.md` — 豆豆 Dou Dou，♀，馬蹄酥與三胞胎之母；生年不詳
- `ma-ti-su.md` — 馬蹄酥 Ma Ti Su，♂，豆豆之子、三胞胎同母兄（父不詳）；生年不詳
- `sha-sha.md` — 沙沙 Sha Sha，♂🌈，三胞胎大哥，已故（歿日不詳）；生年不詳
- `cha-cha.md` — 茶茶 Cha Cha，♀，三胞胎二姐；生年不詳（⚠️ 與日本 `cha-cha-1992-07-17`／`cha-cha-1997-06-17` 同名）
- `mian-mian.md` — 面面 Mian Mian，♂，三胞胎小弟；生年不詳
- `te-xiang-bao.md` — 特香包 Te Xiang Bao，性別不明，與豆豆家關係待查證，暫作獨立個體

**更新條目**：
- `index.md` — 新增「海外個體（中國・廈門靈玲動物王國）」分區 7 筆；條目總數 635→642

**待辦**：全家生年、出身、官方來源；馬蹄酥之父（是否即飛飛）、特香包性別與家族關係、沙沙精確歿日均待查。查得生年後各 slug 應更名為 `名字-YYYY`。

---

## [2026-07-15] update | 富富／美美 補回父壯壯（母小白，上海）

**說明**：接續今日更正，作者確認 `fu-fu-2023-06-24`、`mei-mei-2023-06-24` 之父為壯壯（母仍為上海小白 `xiao-bai-shanghai`）。故富富/美美與 2024 胎甜甜/泡泡為**同父異母半血緣（½）兄弟姊妹**；壯壯有兩配偶（妞妞、小白）。

**更新條目**：
- `fu-fu-2023-06-24.md` — 父 不詳→`[[zhuang-zhuang]]`；引言與註改寫；補同父異母 ½ 兄弟姊妹（甜甜、泡泡）
- `mei-mei-2023-06-24.md` — 同上
- `zhuang-zhuang.md` — 配偶加 `[[xiao-bai-shanghai]]`；子女表加富富、美美（另一方親本＝小白）；引言補述
- `xiao-bai-shanghai.md` — 配偶加 `[[zhuang-zhuang]]`；子女表另一方親本 不詳→`[[zhuang-zhuang]]`；引言與待查證更新
- `tian-tian-2024-06-23.md`、`pao-pao-2024-06-23.md` — 補同父異母 ½ 兄弟姊妹（富富、美美）
- `index.md` — 富富、美美、小白說明更新為含壯壯

**待辦**：小白（上海）生年、出身、父母及全家官方來源仍待查。

---

## [2026-07-15] add | 新增好吃鬼（好紅之母，柳州市動物園）

**說明**：作者提供 `hao-hong`（好紅）之母為「好吃鬼」，雌性，其餘資訊不詳。生日不詳，slug 採純名 `hao-chi-gui`（查得生年後更名 `hao-chi-gui-YYYY`）。

**新增條目**：
- `hao-chi-gui.md` — 好吃鬼 Hao Chi Gui，♀，生年不詳，現居柳州市動物園；好紅之母，出身／父母待查證

**更新條目**：
- `hao-hong.md` — 母 不詳→`[[hao-chi-gui]]`（引言、待查證註、家族欄）
- `index.md` — 柳州區新增好吃鬼；好紅說明補「好吃鬼之女」；條目總數 642→643

**待辦**：好吃鬼生年、出身、父母，好紅之父均待查。

---

## [2026-07-15] add | 新增麻薯（窩窩頭×麵包之女，中山市紫馬嶺動物園）＋米糕補回父窩窩頭

**說明**：作者提供兩筆中山市紫馬嶺動物園家族更正。其一，`mi-gao` 之父確認為 `wo-wo-tou`（原記父不詳），故米糕為窩窩頭×麵包所生，與飯糰／鬆餅由「同母半血緣」升為全血緣手足。其二，窩窩頭與麵包另有一女「麻薯」，雌性，2023-06-17 生、2024 年 8 月歿（未滿兩歲）。麻薯有正式名，依 2026-07-14 幼逝收錄原則照常收錄上站；標 `deceased`＋🌈。注意：貝果為窩窩頭與其長女米糕所生（父女配對），已於相關條目與 index 註明。

**新增條目**：
- `ma-shu-2023-06-17.md` — 麻薯 Ma Shu，♀，2023-06-17 生、2024-08 歿，終居中山市紫馬嶺動物園；窩窩頭×麵包之女，deceased

**更新條目**：
- `mi-gao-2021-06-05.md` — 父 不詳→`wo-wo-tou`；補全血緣手足（麻薯🌈、飯糰、鬆餅）；引言與待查證更新；註明貝果為父女配對所生
- `wo-wo-tou.md` — 子女表加米糕（母麵包）、麻薯🌈；引言重寫；註父女配對
- `mian-bao.md` — 子女表米糕另一方 不詳→`wo-wo-tou`、加麻薯🌈；引言更新；待查證移除「米糕之父」
- `fan-tuan-2026-06-05.md`、`song-bing-2026-06-05.md` — 米糕由半血緣改列全血緣手足、加麻薯🌈；貝果仍為 ½ 同父
- `bagel-2024-07-12.md` — 補母方祖父 `wo-wo-tou`（亦為其父）與母方阿姨／舅舅（麻薯、飯糰、鬆餅）
- `index.md` — 中山區新增麻薯列；窩窩頭／麵包／米糕說明更新；園註補「另 1 隻麻薯已歿」；條目總數 643→644

**待辦**：麻薯精確歿日與歿因、出生地細節、官方來源；此家族生年與出身仍多待查。

## [2026-07-16] update | Asahi 轉園日精確化（神戸→横浜・八景島シーパラダイス）

**說明**：讀者回報 `asahi`（朝日／RPF #261）轉入横浜・八景島シーパラダイス的生效日。附官方來源——横浜八景島官方新聞稿（PR TIMES），載明「朝日（アサヒ）… 搬入 ２０１９年４月２０日」，屬園方一手資料，依 2026-07-01 官方來源可直採原則更新。原條目已有此轉園、但僅記年份（2019），今精確化為 2019-04-20。

**來源**：
- https://prtimes.jp/main/html/rd/p/000000321.000011571.html （横浜八景島 官方新聞稿，2019-07-03）

**更新條目**：
- `asahi-2015-06-29.md` — `zoos:` 神戸どうぶつ王国訖、横浜・八景島シーパラダイス起由 2019 精確化為 2019-04-20；引言補精確轉園日；`sources` 增列官方新聞稿

## [2026-07-16] add | 野毛山動物園歷史雄性個體 Chip、Momotaro（讀者回報，園方官方園史佐證）

**說明**：讀者經「圖鑑缺漏」表單回報，希望補齊野毛山動物園（横浜）歷代小熊貓，附野毛山官方園史〈野毛山レッサーパンダヒストリー①〜③〉與 reddishpanda。核對後：海（`umi-2002-06-24`）、きんた（`kinta-2000-06-08`）、かぐや（`kaguya-2000-06-29`）等已在庫；本批先補兩隻資料完整、RPF 可查核的歿雄——Chip 與 Momotaro，皆 styani、已歿（🌈）。生日／居住史／歿日以 RPF 為據，並經野毛山官方園史與 reddishpanda 佐證（三方一致）。

**來源**：
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php （野毛山官方園史②平成前編：モモタロウ 1999 來園）
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1580.php （野毛山官方園史③平成後編：チップ＝デール雙胞胎、2006 來園）
- https://redpandafinder.com/#profile/548 （Chip）、https://redpandafinder.com/#profile/594 （Momotarou）
- https://reddishpanda.com/?page_id=2332 （野毛山個體介紹，非官方，佐證日期）

**新增條目**：
- `chip-2001-06-19.md` — Chip チップ（RPF #548），♂，2001-06-19 生（`dale-2001-06-19` 雙胞胎）、2009-09-10 歿；ズーラシア（2001-06-19–2006-01-30）→野毛山（2006-01-30–2009-09-10）；父母 `pam-1997-06-26`×`mii-mii-1994-06-26`；deceased
- `momotaro-1997-07-17.md` — Momotaro 桃太郎／モモタロウ（RPF #594），♂，1997-07-17 生（`kintarou-1997-07-17` 雙胞胎）、2007-10-14 歿；姫路セントラルパーク（1997-07-17–1999-10-18）→野毛山（1999-10-18–2007-10-14）；父母 Shin-Shin×Kō-Kō（暫純文字）；deceased

**更新條目**：
- `dale-2001-06-19.md` — 雙胞胎 Chip 由純文字改 `[[chip-2001-06-19]]`；備注更新
- `kintarou-1997-07-17.md` — 雙胞胎 Momotarou 由純文字改 `[[momotaro-1997-07-17]]`
- `pam-1997-06-26.md`、`mii-mii-1994-06-26.md` — 子女表 Chip 由純文字改 `[[chip-2001-06-19]]`
- `index.md` — 補漏區新增 Chip（Dale 家族叢）、Momotaro（Kintarou 旁）；條目總數 644→646；最後更新 2026-07-16

**待補（尚未建，待作者定奪／補資料）**：野毛山昭和～平成早期個體，官方園史有記但無生／歿日、且不在 RPF/lineage：ノンノン Non-non・ライライ Rai-rai（1973 首對，短命）／コロ Koro・ミミ Mimi（1976，育有アツコ、~1986 前離園）／アツコ Atsuko（1978 園內出生、~1979 移多摩）／ケイ Kei・ミヤ Miya（1987；ミヤ 1998 移ズーラシア）／ボウボウ Bou-bou・サイサイ Sai-sai（1989-09-01 上海動物園來）／ミーミー・テンテン（1998–99 ズーラシア開園前短期寄養）。另官方園史含大量歷史照片（1970s–，園方版權），是否收錄／如何處理待與作者確認授權方式。

## [2026-07-16] add | 野毛山動物園昭和～平成早期歷史個體 7 隻（讀者回報，官方園史；生歿日不詳）

**說明**：承前一筆讀者回報，補齊野毛山動物園官方園史〈野毛山レッサーパンダヒストリー①昭和編／②平成前編〉所載、Kinta 之前的歷代小熊貓。此 7 隻皆**不在 RPF/lineage**，官方園史亦**無生日、無歿日**，僅有來園年與少數轉園錨點。依專案「確為已歿、歿日不詳」慣例（2026-07-04）設 `died: "?"`（locale 中性、抑制「現在」、is_alive=0）；生年僅 Atsuko 可考（1978 園內出生），餘留空、slug 不帶生日。全部標 `待查證`。亞種暫記 styani（日本館藏主流）待考。

**來源**：
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1575.php （①昭和編）
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php （②平成前編）

**新增條目**：
- `non-non.md` — Non-non ノンノン，♀，野毛山最初一對之一（1973 來園、短命）；生歿不詳
- `rai-rai.md` — Rai-rai ライライ，♂，野毛山最初一對之一（1973 來園、短命）；生歿不詳
- `koro.md` — Koro コロ，♂，1976 來園；`mimi` 配偶、`atsuko-1978` 之父
- `mimi.md` — Mimi ミミ，♀，1976 來園；`koro` 配偶、`atsuko-1978` 之母（⚠️ 與 Dale 之父美美 `mii-mii-1994-06-26` 為不同個體）
- `atsuko-1978.md` — Atsuko アツコ，♀，1978 野毛山園內出生（**野毛山唯一繁殖成功**）、未滿 1 歲移多摩動物公園；`koro`×`mimi` 之女
- `kei.md` — Kei ケイ，♂，1987 來園；`miya` 配偶；1989–96 四頭中最早離世
- `miya.md` — Miya ミヤ，♀，1987 來園；`kei` 配偶；1998 隨ズーラシア開園移入該園

**更新條目**：
- `index.md` — 補漏區 Kaguya 後新增上列 7 隻；條目總數 646→653

**仍待補（本批未建）**：ボウボウ Bou-bou・サイサイ Sai-sai（1989-09-01 上海動物園來、屬平成、非昭和）／ミーミー・テンテン（1998–99 ズーラシア開園前短期寄養）——生歿日同樣不詳，待作者定奪是否收錄。另官方園史含 1970s 起大量歷史照片（横浜市緑の協会版權），本 wiki 一律不轉載／不 rehost，僅以 `sources:` 連回官方頁；若要在站上展示需另洽園方授權。

## [2026-07-16] add | 野毛山動物園：ボウボウ・サイサイ（1989 上海動物園來）＋ 溫馨提醒溫存寄養個體待辨識

**說明**：接續野毛山歷史個體補建。新增平成初期自上海動物園來園的 ボウボウ・サイサイ 一對（1989-09-01「防災の日」來園，故名）。同前 7 隻昭和個體，官方園史無生歿日，依 `died: "?"` 慣例、生年留空、標 `待查證`；因來源明確為上海動物園、亞種取 styani。

**來源**：
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php （②平成前編）

**新增條目**：
- `bou-bou.md` — Bou-bou ボウボウ，♂，上海動物園→野毛山（1989-09-01）；`sai-sai` 同期；園史記為當時最胖
- `sai-sai.md` — Sai-sai サイサイ，♀，上海動物園→野毛山（1989-09-01）；`bou-bou` 同期；園史記為「狐狸臉」

**更新條目**：
- `index.md` — 補漏區新增 Bou-bou、Sai-sai；條目總數 653→655

**暫緩（待作者辨識，避免重複建檔）**：園史②載 1998–99 年ズーラシア開園前，曾有 **ミーミー、テンテン** 兩隻在野毛山短期寄養數月。此二名與 wiki 既有多筆條目撞名（`mii-mii-1992-08-07`／`mii-mii-1994-06-26`／`mii-mii-2017-07-15`；`ten-ten-1989-06-26`／`-1991-06-29`／`-1997-06-18`／`-1998-07-07`），且此二隻本為ズーラシア個體、極可能已在庫。故**不逕建新 stub 以免重複**——正確作法應是辨識出對應既有個體後，於該條目補一段 1998–1999 年野毛山「短期寄養」居住史。待作者指認是哪兩隻（或授權以 RPF 查對）再處理。

## [2026-07-16] add/update | テンテン 辨識為 RPF #591 並建檔；ミーミー 確認為既有美美

**說明**：續辦野毛山 1998–99 ズーラシア開園前短期寄養的 ミーミー・テンテン 二隻。經 RPF（以ズーラシア始祖群交叉比對）確認：
- **ミーミー ＝ 美美 `mii-mii-1994-06-26`（RPF #359），已在庫**，其居住史本就含横浜市立野毛山動物園（1997–1998）＝該寄養段，故**不另建**、僅補官方園史來源與說明，避免重複建檔。
- **テンテン ＝ Ten-Ten（RPF #591）**，生於天王寺動物園、1999-04-03 入野毛山（寄養段）、1999-11-11 遷ズーラシア、2002 遠渡加拿大 Assiniboine Park Zoo、2008-04-22 歿。為全新個體、且有完整生日→依常規 slug（名字-生日）建檔，**無須加園名後綴**。

**來源**：
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/details/post-1577.php （②平成前編，記 ミーミー・テンテン 寄養）
- https://redpandafinder.com/#profile/591 （Ten-Ten）、https://redpandafinder.com/#profile/359 （美美）

**新增條目**：
- `ten-ten-1997-07-03.md` — Ten-Ten 天天／テンテン（RPF #591），♂，1997-07-03 生、2008-04-22 歿；天王寺→野毛山→ズーラシア→Assiniboine Park Zoo；父母 Pan-Pan #592×Jen-Jen #547（暫純文字，父 Jen-Jen #547 ⚠️ 勿與 `jen-jen-1995-07-06` #475 混淆）

**更新條目**：
- `mii-mii-1994-06-26.md` — `sources:` 補野毛山官方園史；引言加註野毛山（1997–1998）即園史「ミーミー」寄養段、並連結 `ten-ten-1997-07-03`
- `index.md` — 補漏區新增 Ten-Ten；條目總數 655→656

**備註（slug 消歧原則，2026-07-16 確認）**：同名個體優先以「名字-生日」自然消歧；生日不詳且與既有條目撞名時，才考慮以**落腳／出生園名**當後綴（前例 `fei-fei-xiamen`、`xiao-bai-shanghai`），**不用「來園年」當後綴**（會被誤讀為生年、且易與既有生日 slug 相撞）。本批 テンテン 因 RPF 有生日，直接用生日 slug、未加後綴。

## [2026-07-16] fix | 更正上海動物園來源歸屬：ノンノン・ライライ（是）↔ ボウボウ・サイサイ（非）

**說明**：作者提供野毛山展場官方年表面板照片（園方版權，僅列 URL 不轉載）並指出前次建檔來源歸屬有誤。核對面板後更正：
- **ノンノン・ライライ（1973）＝上海動物園來**：面板明載「上海動物園からやってきました！しかし、残念ながら短命な2頭でした」。前次誤標為「來源不詳」，今補上海動物園為來源園（🐣）、亞種確立 styani。
- **ボウボウ・サイサイ（1989）：撤下上海動物園**：面板未標其來源；作者校訂為非上海來源。前次依園史〈②平成前編〉內文「1989年、上海動物園から…ボウボウとサイサイ」而標上海，現移除、來源改列待查，並在條目內保留該內文矛盾備忘（園史內文 vs 面板／作者校訂），供日後定奪。
- 另面板佐證：チップ「ズーラシア生まれ、双子の姉デール」、アツコ「野毛山唯一繁殖成功」、コロ×ミミ 亦同——與既有條目一致。

**來源**：野毛山展場官方年表面板照片（作者提供，横浜市緑の協会版權）：
- https://www.hama-midorinokyokai.or.jp/zoo/nogeyama/authorc8504/980d27529f9b96bdfee156016aeede7e8300afa0.jpg

**更新條目**：
- `non-non.md`、`rai-rai.md` — `zoos:` 補 上海動物園 ( – 1973)；引言／備注／居住史更新；來源園不再列待查
- `bou-bou.md`、`sai-sai.md` — `zoos:` 移除 上海動物園；引言去「自上海」；備注改列來源待查＋內文矛盾備忘
- `index.md` — Non-non/Rai-rai 補「上海動物園來」；Bou-bou/Sai-sai 改「來源待查」

**檢討**：前次未讀作者所附之面板圖片（只讀了 blog 內文），導致（1）漏掉面板明載的 Non-non/Rai-rai 上海來源，（2）把 blog 內文的上海歸屬套到面板未支持的 Bou-bou/Sai-sai。往後作者附圖時務必實際讀圖。

## [2026-07-16] fix | Bou-bou・Sai-sai 來源改列「上海動物園（待查證）」

**說明**：作者裁定——Bou-bou・Sai-sai 的上海動物園來源先列上、標「待查證」。理由：blog 內文〈②平成前編〉有實際出處（非憑空推測），只是展場面板未複述、尚待園方確認；此屬「有來源待確認」＝待查證，不同於「無來源之推測」。故 zoos 補回 上海動物園 ( – 1989-09-01)，條目與 index 標「上海動物園（待查證）」，亞種暫記 styani。

**更新條目**：
- `bou-bou.md`、`sai-sai.md` — `zoos:` 補回 上海動物園；引言／備注／居住史標「上海動物園（待查證）」
- `index.md` — Bou-bou/Sai-sai 改「上海動物園來（待查證）」

## [2026-07-16] fix | Bou-bou・Sai-sai 上海動物園來源改為「確定」

作者確認 Bou-bou・Sai-sai 確自上海動物園來（園史〈②平成前編〉內文亦載），撤下「待查證」，`bou-bou.md`／`sai-sai.md`／`index.md` 來源標記改為確定；亞種 styani。

## [2026-07-16] fix | Mii-Mii（#359）日文名更正：美美 → ミーミー

**說明**：作者校訂——此公個體（RPF #359，Gaia 之父）的名字沒有漢字「美美」，只有片假名「ミーミー」。原「美美」為 2026-06 lineage 補漢字批次誤帶入（見該批 log），今全數撤下。（徳山的 ♀ `mii-mii-1992-08-07` #371 名為美美，不受影響。）

**更新條目**：
- `mii-mii-1994-06-26.md` — `japanese:` 美美 → ミーミー；標題補（ミーミー）；備注去「美美」
- `chip-2001-06-19.md`、`ten-ten-1997-07-03.md`、`koai-2004-06-10.md` — 內文對此個體的「美美」改為「ミーミー」
- `index.md` — #359 列補 ミーミー

## [2026-07-16] update | Umi（#368）日文名補「うみ」

**說明**：作者提供——`umi-2002-06-24` 日文名補平假名「うみ」（原有 海、ウミ）。

**更新條目**：
- `umi-2002-06-24.md` — `japanese:` 補 うみ；標題改（海 / ウミ / うみ）

## [2026-07-16] update | Udaya（#1081）移除日文名（非日本個體）

**說明**：作者校訂——Udaya（Calgary Zoo，加拿大）名字沒有日文，移除 `japanese: ウダヤ` 與舊名的アドゥヤ標注（lineage ja.name 機械轉寫，非日本個體不採用）。

**更新條目**：
- `udaya-2019-06-20.md` — 移除 `japanese:`；標題與引言去片假名
- `linus-2018-06-23.md`、`ravi-2022-06-14.md`、`sundari-2022-06-14.md`、`anshu-2023-06-18.md`、`aahana-2023-06-18.md` — 親屬欄去（ウダヤ）
- `index.md` — Udaya 列去 ウダヤ

## [2026-07-16] add | Calgary Zoo 三胞胎蘋果籽（Udaya × Linus，2026-06-08）

**來源**（官方）：
- https://www.calgaryzoo.com/news/welcoming-red-panda-cubs/ （園方新聞稿）
- https://www.instagram.com/calgaryzoo/reel/DaS3WVsAvG5/ （園方官方 IG post，作者提供）

**說明**：作者告知＋園方公告——`udaya`（母）× `linus`（父）於 2026-06-08 產下三胞胎，為此配對第三窩（2022、2023 後）。寶寶未命名、未公布性別，依蘋果籽制度建佔位條目三筆；序號為暫編（園方未公布順序、RPF 未建檔）。官方 IG 一併掛入三筆條目的 `instagram:`。

**新增條目**：
- `apple-seed-1-udaya-2026-06-08.md` — 蘋果籽1號，生於 2026-06-08，現居 Calgary Zoo
- `apple-seed-2-udaya-2026-06-08.md` — 蘋果籽2號，同上
- `apple-seed-3-udaya-2026-06-08.md` — 蘋果籽3號，同上

**更新條目**：
- `udaya-2019-06-20.md`、`linus-2018-06-23.md` — 引言補三胞胎；子女表各加 3 列
- `ravi-2022-06-14.md`、`sundari-2022-06-14.md`、`anshu-2023-06-18.md`、`aahana-2023-06-18.md` — 家族補「弟妹（同父母，三胞胎）」
- `index.md` — Calgary 家族段補三胞胎、新增 3 列；條目總數更新為 659

## [2026-07-16] update | 已歿個體最後居住訖日補死亡日（4 筆）

**說明**：讀者回報（楊桃，資料更正收件匣 OQjaPjR）檢視 `asahi` 時發現：已歿個體的最後一段居住若訖日留空，網站會顯示「?」（僅在世個體才顯示「現在」）。依既有慣例（如 `a-ya`、`airi`），最後一段訖日應為死亡日。順手盤點全 wiki，共 4 筆同型（其餘訖日空白者為 `died: "?"`、歿日不明，維持現狀）。回報本身所述 2019-04-20 轉園資訊條目原已收錄，無需變更。

**更新條目**：
- `asahi-2015-06-29.md` — 横浜・八景島シーパラダイス 訖日補 2019-09-04
- `malikha-2004-06-08.md` — Safari Niagara 訖日補 2016-02-21
- `pip-2008-05-26.md` — Edmonton Valley Zoo 訖日補 2020-01-08
- `zeyar-2007-06-21.md` — Calgary Zoo 訖日補 2013-10-01

## [2026-07-16] update | Linus（#1000）移除日文名（非日本個體）

**說明**：作者確認——Linus（Cincinnati 生、現居 Calgary Zoo）同 Udaya，名字沒有日文，移除 `japanese: ライナス`（lineage ja.name 機械轉寫，非日本個體不採用）。

**更新條目**：
- `linus-2018-06-23.md` — 移除 `japanese:`；標題去片假名
- `udaya-2019-06-20.md`、`ravi-2022-06-14.md`、`sundari-2022-06-14.md`、`anshu-2023-06-18.md`、`aahana-2023-06-18.md` — 親屬欄去（ライナス）
- `index.md` — Linus 列去 ライナス

## [2026-07-16] hide | `tang-yuan` 暫存 _hidden/（作者要求下架）

**說明**：作者要求隱藏 `tang-yuan`（湯圓／汤圆，上海動物園；性別、生年、出身、父母均待查證，僅「作者提供」為來源）。依隱藏慣例移入 `wiki/_hidden/`，不計數、不上站；非刪除。index 該列一併移除。

**更新條目**：
- `tang-yuan.md` — 移入 `wiki/_hidden/`
- `index.md` — 移除該列；條目總數更新為 658（_hidden 暫存 4 筆）

## [2026-07-17] add | 大連森林動物園三隻檔案卡（首批 limited-profile 條目）

**來源**：
- 圖鑑缺漏回報：讀者 2025-04 實地參觀所攝園方展牌（回報附件；官網 https://www.dlzoo.com/home 及新聞動態 73 篇（2023–2026）、微信均查無個體資訊）

**說明**：套用本日新制「資料有限個體：檔案卡」（見 CHANGELOG 2026-07-17）。生日不詳 → slug 用 `名字-園簡稱`；`last_seen: 2025-04`；展牌實拍依作者裁定記入新欄位 `extra_sources`（與官方 sources 分開）。名字與性別依展牌。

**新增條目**：
- `nuo-mi-dalian.md` — 糯米 Nuo Mi ♀，生年不詳，現居 大連森林動物園
- `xi-ning-dalian.md` — 希檸（希柠）Xi Ning ♀，生年不詳，現居 大連森林動物園
- `mi-duo-dalian.md` — 米朵 Mi Duo ♂，生年不詳，現居 大連森林動物園

**更新條目**：
- `index.md` — 新增「海外個體（中國・大連森林動物園）」段落；條目總數更新為 661

## [2026-07-17] update | Matsuba 名字整理：加中文名 松葉、移除暱稱

**來源**：
- 作者提供（名稱以作者為準）

**更新條目**：
- `matsuba-2014-07-17.md` — 新增 `chinese: 松葉`；移除 `nicknames`（Battle Princess / Mochi-slayer / Mochi-sweetie）及內文暱稱句；標題改為 Matsuba（松葉・まつば）
- `index.md` — 該列說明同步更新

## [2026-07-17] update | Matsuba 新增 IG 貼文連結

**來源**：
- https://www.instagram.com/kinusayaffa/p/Da38ZYpjxsp/ (@kinusayaffa，まつば 12 歲生日貼文)

**更新條目**：
- `matsuba-2014-07-17.md` — frontmatter 新增 `instagram:`（含帳號完整形式）

## [2026-07-17] add | 円山動物園蘋果籽出生：`hinagiku` × `puerh` 第一胎（2026-07-16）

**來源**：
- https://www.instagram.com/p/Da4GzmzGaea/ (@maruyamazoo_official，2026-07-16 出産公告，母子平安、已確認授乳)
- https://www.city.sapporo.jp/zoo/03doubutsu/05asiazone/redpanda/r8/redpanda_pregnant.html (札幌市官網：ヒナギク × プーアル 2026-03-25～04-05 配對交尾、6月確認懷孕)

**說明**：讀者回報。官方來源齊備（園方 IG＋市官網），依 2026-07-01 授權直接採用。蘋果籽四資格全符合；胎數官方尚未明示（懷孕公告載「胎子頭數確認中」），暫以單胎建檔、不編號，若後續公告多胞胎再補條目並編號。

**新增條目**：
- `apple-seed-hinagiku-2026-07-16.md` — 蘋果籽 Apple Seed（未命名，性別待確認），生於 2026-07-16，現居 札幌市円山動物園

**更新條目**：
- `hinagiku-2022-07-01.md` — 引言與家族補子女
- `puerh-2015-06-25.md` — 引言補 2026 配對與新子；新增「子女（母 `hinagiku`）」表；**更正**子女之母誤連 `yuu-yuu-2014-07-27`（友友，2018 起居広島）→ `yuu-yuu-2011-05-28`（渝渝，旭山，據子女條目及居住史比對）
- `ren-ren-2020-06-29.md`、`rin-rin-2020-06-29.md`、`jin-jin-2022-07-05.md`、`chen-chen-2022-07-05.md` — 父「Pu'erh（無條目）」改為 wikilink（條目其實已存在）；補父方半血緣妹弟（蘋果籽）
- `index.md` — Pu'erh 家族新增子女（母 `hinagiku`）段落；兩處 `yuu-yuu-2014-07-27` 誤連同步更正為 `yuu-yuu-2011-05-28`；Hinagiku 列說明更新；條目總數更新為 662

## [2026-07-18] add | 緑々之姊 紅紅（作者提供）＋緑々補中文名 綠綠

**來源**：
- 作者提供（名稱以作者為準）；家系參照 https://www.nhdzoo.jp/red-panda/kakeizu/index.html

**新增條目**：
- `hou-hou.md` — 紅紅 Hou-Hou（紅々／ホウホウ）♀，`naka-naka`（中々）× `hana-hana`（華々）之女、`ryu-ryu-1990` 🌈（緑々）之姊；生卒、居住地、RPF 皆不詳，標 unverified（⚠️ 勿與茶臼山 1993 年前後之 Hou-Hou 混淆）

**更新條目**：
- `ryu-ryu-1990.md` — 新增 `chinese: 綠綠`；標題補 綠綠；家族補姊 `hou-hou`
- `naka-naka.md`、`hana-hana.md` — 引言與家族補女 `hou-hou`
- `index.md` — 風々一脈新增「姑母」段落；Ryu-Ryu 列補 綠綠；條目總數更新為 663

## [2026-07-18] rename | 紅紅補生卒 1988–1999，slug 改為 `hou-hou-1988`

**來源**：
- 作者提供（生卒僅知年份；緑々 1990–1999 與既有條目一致，未變動）

**更新條目**：
- `hou-hou.md` → `hou-hou-1988.md` — 補 `born: 1988`、`died: 1999`；tags 改 deceased（移除 unverified）；標題與引言補 🌈 與生卒
- `ryu-ryu-1990.md`、`naka-naka.md`、`hana-hana.md` — wikilink 同步改 `hou-hou-1988` 並補 🌈
- `index.md` — 姑母列補生卒 1988–1999 🌈、wikilink 同步

## [2026-07-18] update | 清除 RPF 遺毒英文別名：`gao-gao-2015-06-27` 移除 Stripes、Shaggy

**來源**：
- 作者裁定（RPF 帶入的翻譯型別名，非正式名稱；清理清單見 docs/english-variants-audit.md）

**更新條目**：
- `gao-gao-2015-06-27.md` — frontmatter 移除 `english_variants: [Stripes, Shaggy]`；引言移除「別名：Stripes、Shaggy」列

## [2026-07-21] update | 円山動物園蘋果籽 `hinagiku` × `puerh` 第一胎夭折（2026-07-20，生後 4 日）

**來源**：
- https://www.city.sapporo.jp/zoo/03doubutsu/05asiazone/redpanda/r8/redpand_child.html （札幌市円山動物園官方訃告：2026-07-20 死亡，子為メス／雌、0 歲；7/19 起活動力轉弱、7/20 產箱確認死亡；同日解剖無明確異常、母獸健康無虞）

**說明**：寶寶出生後未及正式命名即夭折。官方訃告齊備，依 2026-07-01 授權直接採用，並回填性別為雌（原留空）。依 2026-07-21 作者裁定的新做法，**當季（6/1–11/30）仍保留於 wiki／首頁「新鮮的寶寶」（帶歿記）**，不立即移入 `_hidden`；季末（每年 12/1 由排程 `hide-deceased-apple-seeds-yearly` 自動）區塊隱藏後再下架。故此筆僅記死亡、未移 `_hidden`、條目總數不變（仍 663、仍上站）。

**更新條目**：
- `apple-seed-hinagiku-2026-07-16.md` — frontmatter 補 `died: 2026-07-20`、`sex: female`、tags 加 `female`／`deceased`、`sources` 補官方訃告、`zoos:` 訖日 現在 → 2026-07-20；標題與引言補 🪽、♀、歿日與「生後 4 日」，佔位提示改為「未及命名即夭折」，內文改過去式並補死亡經過／解剖結果
- `puerh-2015-06-25.md`、`hinagiku-2022-07-01.md` — 引言與子女表對該子補 🪽 與幼逝註記
- `ren-ren-2020-06-29.md`、`rin-rin-2020-06-29.md`、`jin-jin-2022-07-05.md`、`chen-chen-2022-07-05.md` — 父方半血緣手足列對該妹補 🪽
- `index.md` — 該列補 🪽 與「生後四日夭折」；總數不變

## [2026-07-18] update | 來源勘誤：日本平家系圖頁僅列現役個體，錯引批次更正

作者指出 `hou-hou-1988`（紅紅）、`ryu-ryu-1990`（綠綠）引用的日本平家系圖連結中查無其人。實際核對家系圖圖片（sec01-img01.png，2320×3000）：最上代僅自 シュウシュウ／楢／風々 起、共 27 隻現役相關個體，且頁尾註明「一部の情報は省略しています」——與 2026-07-01 log 已註記的「僅列現役個體」一致，但當時未同步清理各條目 sources。本批將「不在圖中卻引用該頁」的 11 個條目改引真正佐證來源：多摩官方個體名單（4travel 轉載，官方轉載可直採）有載者換該連結；未載者移除、改記實際來源。並依名單補採 中中／華華 之「出自不明・死亡」。

**來源**：
- https://www.nhdzoo.jp/red-panda/kakeizu/imgs/sec01-img01.png （日本平家系圖原圖，核對用）
- https://4travel.jp/travelogue/11691476 （多摩官方個體名單轉載：中中、華華、緑々、光々、ハナ、ナナ、ノア 有載；紅々、希々、蘭々 未載）

**更新條目**：
- `ryu-ryu-1990.md` — sources 家系圖改 4travel 名單；註記名單原文「緑々（♂／1990年生まれ）中中×花花　1999年に死亡」及「花花」應為華華筆誤；父母欄改「官方名單確認」＋🌈
- `naka-naka.md`／`hana-hana.md` — sources 家系圖改 4travel 名單；依名單「出自不明・死亡」補 `deceased`／🌈（歿日不詳）、移除 `unverified`；居住園（多摩）年份不詳故 `zoos:` 暫不登錄；`hana-hana` 原「同母異父半手足 ハナ」註為誤植（兩者無血緣），改為單純勿混淆提示
- `hou-hou-1988.md` — sources 改「作者提供（2026-07-18）」；註記未見於多摩官方名單、日本平家系圖亦無；父母補 🌈
- `ki-ki-1996.md` — sources 改「圖鑑缺漏回報收件匣（submission aOEzG62）」；註記未見於多摩官方名單
- `kou-kou-1997-06-20.md`／`nana-2001-07-13.md`／`noa-2004.md`／`hana-2001-07-13.md` — sources 家系圖改 4travel 名單（四者皆有載）
- `ran-ran-1998-06-29.md`／`buna-2000-07-13.md` — 移除家系圖連結（蘭々未見於名單、ブナ非多摩個體且不在圖中），餘 RPF
- `index.md` — 中々／華々 列補 🌈（生卒不詳）、多摩動物公園（年份不詳）；紅紅列補「作者提供、未見於多摩官方名單」

**保留引用**（確實在家系圖中）：`fu-fu-1997-06-20`、`fuuka-2006-06-02`、`kazu-2019-07-02`、`nara-2000-07-13`、`takeru-2015-07-29`

## [2026-07-18] update | 批次清除 RPF 遺毒英文別名（審核清單 D 類）

**來源**：
- 作者裁定（docs/english-variants-audit.md D 類「翻譯型／無關／可疑」全刪；9 筆有非 RPF 來源或作者先前裁定者保留，詳清單 ⏸ 標記）

**更新條目**（59 檔、移除 95 個 english_variants 字串；內文「別名／英文名」殘句一併清除）：
- `anri-1994-06-19.md` — 移除 Annapulina、Anna Pulina、Annapuluna
- `aru-2013-08-15.md` — 移除 Love、Al
- `buna-2000-07-13.md` — 移除 Beech
- `chuihowa-2010-07-10.md` — 移除 Chuy-Fa、Ju-Hua、Juhua
- `cocoa-2018-06-28.md` — 移除 Kuro、Kufa、Ku-Fa
- `cong-cong-2008-06-11.md` — 移除 Chung Chung
- `fin-fin-2002-06-20.md` — 移除 Tanpopo
- `foa-foa-2004-06-29.md` — 移除 Angdu
- `fuu-1998-07-04.md` — 移除 Huu-Huu
- `fuumi-2007-07-11.md` — 移除 Kazumi、Kazami
- `hana-2005-06-21.md` — 移除 Himawari
- `hui-hu-2019-06-22.md` — 移除 Firefox
- `kaori-1991-06-18.md` — 移除 Kou
- `ken-ken-2006-07-18.md` — 移除 Freckle-kun
- `kiku-2015-06-26.md` — 移除 Chrysantheum
- `kinta-2000-06-08.md` — 移除 Spaceman、Quintana-Roo、Ageless Beauty
- `kou-2011-06-14.md` — 移除 Kisaki
- `kusu-1991-06-24.md` — 移除 Cous
- `kusukusu-2015-07-21.md` — 移除 Couscous、Cous-Cous
- `leanne-2020-07-20.md` — 移除 Rian、Rians
- `lemon-2013-07-07.md` — 移除 Meruki、Miruki、Miruki-
- `lessy-2014-08-18.md` — 移除 Tōya、Toya、Touya
- `li-zi-2008-06-15.md` — 移除 Chestnut
- `light-2013-07-18.md` — 移除 Raito
- `liuxing-1997-06-16.md` — 移除 Ryuusi、Ryuusii、Ryuusin
- `luna-2015-08-23.md` — 移除 Moon
- `maple-2022-06-14.md` — 移除 Moose
- `maruo-2018-07-11.md` — 移除 Mihota
- `maruru-2014-06-06.md` — 移除 Musuko
- `mei-mei-2007-06-28.md` — 移除 May-May、Maymay、MayMay
- `meixiang-2017-06-29.md` — 移除 Meisyan、Mei-Shan、Meishan、Mei Shan
- `mii-2013-06-23.md` — 移除 Mie
- `mitsuba-2016-06-25.md` — 移除 Clover
- `mulan-2019-06-07.md` — 移除 Mokuren
- `nohana-2017-07-31.md` — 移除 Norin
- `piisuke-2020-06-27.md` — 移除 Peaceke、Peace Ke
- `raichi-2005-06-25.md` — 移除 Lychee
- `rei-mei-2019-07-10.md` — 移除 Raymay、Ray-May
- `rei-rei-2016-06-28.md` — 移除 Thunder-Lightning
- `reika-2019-06-02.md` — 移除 Wasabi
- `rimu-2021-07-31.md` — 移除 Rheem
- `rou-rou-2008-07-09.md` — 移除 Rouge、Yauyau
- `rouge-2002-06-20.md` — 移除 Chya-Fa、Chafa
- `sakura-2004-06-17.md` — 移除 Cherry-Blossom
- `shan-tou-2005-05-10.md` — 移除 Li-hua、Ri-fa、Riifa
- `shin-fa-2019-06-19.md` — 移除 Xinghua
- `shin-shin-2000-06-30.md` — 移除 Chenxing
- `tai-shan-2008-06-14.md` — 移除 Taixiang
- `tashan-2002-07-01.md` — 移除 Ta-Xiang、Taxiang、Taixiang、Daoguang
- `tiara-2015-07-06.md` — 移除 Minko
- `xianchi-2007-06-26.md` — 移除 Shanzhi
- `yao-2017-07-14.md` — 移除 Yō、Yo
- `you-you-2002-06-21.md` — 移除 Flying
- `yueshi-1999-07-08.md` — 移除 Yeosy
- `yukiko-2005-06-23.md` — 移除 Take、Také
- `yum-yum-2005-07-07.md` — 移除 Yin-Yin、Inin
- `yun-yun-2016-06-28.md` — 移除 Cloud
- `yuu-yuu-2014-07-27.md` — 移除 Yao-Yao、Yaoyao
- `yuuki-2013-07-04.md` — 移除 Snow
- `ren-2004-06-17.md` — english_variants 的「レン」實為讀音，移至 japanese 欄（恋, レン）

## [2026-07-18] update | 清除英文別名：作者複核後，原保留之 9 筆一併刪除

**來源**：
- 作者裁定（docs/english-variants-audit.md D 類清理之補充；原因保留欄位見清單）

**更新條目**：
- `fuu-2004-07-13.md` — 移除 Kaze（撤銷 2026-07-06「留作檢索別名」；內文改「舊拼音 Kaze 廢止」）
- `yum-yum-2005-07-07.md` — 移除 In-In（同上）
- `leah-2019-05-17.md` — 移除 Rose（內文 RPF 主名敘述保留）
- `enoki-2023-06-13.md` — 移除 Debree；內文曾用名句刪除
- `mebo-2023-06-13.md` — 移除 Doza、Marsala；內文曾用名句刪除
- `rou-rou-2008-07-09.md` — 移除 Yau-Yau；內文粵語讀音句刪除
- `sumire-2004-06-17.md` — 移除 Viola；內文改「到台後取中文名」
- `shan-tou-2005-05-10.md` — 移除 Rifa（同名消歧警告保留）

## [2026-07-19] update | 已故標記全面改用 🪽（原 🌈）

**來源**：
- 作者裁定（配合網站「今日前往小熊星球」區塊改版，全站統一星球意象）

**更新條目**：
- `wiki/*.md` 全部條目（含 `_hidden/`）— 內文已故標記 🌈 → 🪽，共 559 檔
- `index.md` — 同步替換
- 規範文件同步：`SCHEMA.md`、`CLAUDE.md`、`rpf-wiki-SKILL.md`、`ROADMAP.md`；工具 `tools/query.py`（顯示標記）、`tools/zoo_registry.py`（_NOTES 兩者並收向下相容）
- 網站側：五語 i18n（標題 ja/ko/en 改直譯「前往小熊星球」）、各頁已故標記、OG 卡彩虹條改星球漸層條
- 歷史紀錄不改：`log.md`、`log-archive/`、`CHANGELOG.md`、docs/ 內既往文件維持 🌈

## [2026-07-19] hide | `ichiko-2014-07-06` 暫時下架：官方公告該胎僅一隻，Ichiko 存在待查證

**來源**：
- https://www.facebook.com/zounokuni/posts/686909551385606/ （市原ぞうの国官方 FB：2014-07-06 出生公告僅一郎一隻，未提及雙胞胎）
- 作者裁定（Ichiko 僅有 RPF 來源、無 rpf_id，可能為錯誤資料，先隱藏待查證）

**更新條目**：
- `ichiko-2014-07-06.md` — 加註下架原因後移入 `wiki/_hidden/`
- `ichiro-2014-07-06.md` — 移除雙胞胎 Ichiko 之 wikilink 與家族列，改為 🚧 待查證純文字注記
- `kojirou-2010-07-14.md` — 子女表移除 Ichiko 列、備注改「育有 Ichiro（RPF 另記 Ichiko，🚧 待查證）」
- `tomato-2007-07-21.md` — 引言與子女表移除 Ichiko，改 🚧 待查證注記
- `index.md` — 移除 Ichiko 列；條目總數 663 → 662（_hidden 4 → 5 筆）

## [2026-07-20] update | 清除非日本個體誤填的片假名 japanese 名

**來源**：
- 作者裁定（依 CLAUDE.md 資料來源原則：`japanese` 僅限有日本居住史之個體；lineage/RPF 的 ja.name 為機械轉寫，非日本個體不採用）

**更新條目**：
- 36 隻無日本居住史個體：移除 frontmatter `japanese:` 片假名欄（純片假名者整欄移除；`tai-shan`、`hou-hou` 之漢字名已存於 `chinese`，亦整欄移除），並清除各自標題行的（片假名）
  - `arun`、`carson`、`dawa`、`duli`、`ferguson`、`hou-hou`、`karma`、`kayah`、`kelu`、`kendji`、`kiari`、`kovu`、`leah`、`lincoln`、`maja`、`malikha`、`meeko`、`mei-mei`、`mulan`、`nima`、`poppy`、`rakesh`、`ravi`、`rinzen`、`sakura`、`sophia`、`sundari`、`tai-shan`、`tango`、`tanvi`、`tayla`、`willa`、`xi-xi`、`xiao-bai-lian`、`zeyar`、`zorro`
- 其他條目家族欄中指向上列 36 隻的（片假名）交叉引用一併清除（保留性別、RPF 編號、韓文名等其他括號內容；日本居住個體之片假名與動物園名不動）
- 內文引言中提及片假名別名者（如 `leah` ローズ、`sundari` サンサリ）依作者裁定保留原文、不動
- 重建：`gen_residence.py` → `build_db.py` → `export_json.py`；`verify.sh` 通過（🔴 0）

---

## [2026-07-21] add | 王子動物園早期個體 `太郎`（讀者回報，楊桃）

**來源**：
- http://ojizoo.jp/html/oj-07-114.htm （王子動物園官方個體アルバム頁：出生 1989-07-01・オス・1990-12-12 由長野市茶臼山動物園來園）
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki66.pdf （園報〈はばたき No.66〉2010 年 4 月號第 16 頁「別れ」欄：シセンレッサーパンダ「太郎」オス・20 歳・10 月 25 日死亡 → 2009-10-25）

**新增條目**：
- `tarou-1989-07-01.md` — `Tarou` 太郎（タロウ），♂，生於 1989-07-01 長野市茶臼山動物園，1990-12-12 移神戸市立王子動物園，2009-10-25 歿（享年 20 歲）；家系不詳；styani；deceased

**更新條目**：
- `index.md` — 「王子動物園 早期個體（神戸）」新增 `太郎`；條目總數 662 → 663

**備注**：讀者（楊桃）回報，兩筆來源皆官方（園方官網＋園報），依 CLAUDE.md「官方來源可直接採用」建檔。兩座園（長野市茶臼山動物園、神戸市立王子動物園）皆已登記於 `data/zoos.json`。無 RPF profile（缺 rpf_id，audit 列 ⚪ info）。

---

## [2026-07-21] add | 紅山 `夏娃` 家系補入父 `小小白`、兄 `醬醬`（limited-profile，全待查證）

**來源**：
- 作者提供（2026-07-21）；家系與出身暫無官方公告佐證，全數標 🚧 待查證

**新增條目**：
- `xiao-xiao-bai-nanjing.md` — `小小白` Xiao Xiao Bai，♂，生年不詳；現居南京市紅山森林動物園，自 `常州淹城野生動物世界` 轉入（年份不詳）；`夏娃` 之配偶，`醬醬`・`仲夏`・`孟夏` 之父；limited-profile
- `jiang-jiang-nanjing.md` — `醬醬` Jiang Jiang，♂，生年不詳；生於南京市紅山森林動物園，`夏娃`×`小小白` 之子、`仲夏`・`孟夏` 之兄，推測為夏娃第一胎；limited-profile

**更新條目**：
- `zhong-xia-2025-07-17.md`、`meng-xia-2025-07-17.md` — 父由「不詳」改 `小小白`（🚧），家族加兄 `醬醬`
- `xia-wa.md` — 家族加配偶 `小小白`、子 `醬醬`；更新待查證注（配偶／第一胎）
- `data/zoos.json` — 既有 `Yancheng Wild Animal World`（lineage_id 301，即常州淹城）補中文 canonical `常州淹城野生動物世界`、`zh` 與中英別名，供 CN 條目正常解析顯示
- `index.md` — 紅山區新增 `小小白`、`醬醬`，`夏娃` 說明加醬醬；條目總數 663 → 665

**備注**：無生日者依 CN 檔案卡規則以「名字-園簡稱」命名（`-nanjing`），查得生日後 rename。`小小白` 居住史 `淹城 🐣 → 紅山 🏡`，兩園年份不詳（作者裁定淹城標出生地）。皆缺 RPF profile（audit ⚪ info）。

---

## [2026-07-23] update | `aahana-2023-06-18` 轉園 Calgary Zoo → Safari Niagara（讀者回報，官方雙邊確認）

**來源**：
- https://www.instagram.com/p/DCcCw9nIDT2/ （thecalgaryzoo 官方 IG，2024-11-17：依 Red Panda SSP 建議轉出 Aahana，該週末為離園前最後展出）
- https://www.instagram.com/p/DHySw7Wp7u3/ （safariniagara 官方 IG，2025-03-29：Aahana 已加入 Safari Niagara）

**更新條目**：
- `aahana-2023-06-18.md` — `zoos:` 由 `Calgary Zoo (…現在)` 改為 `Calgary Zoo (2023-06-18 – 2024)` ＋ `Safari Niagara (2024 – 現在)`；tags `zoo:Calgary Zoo` → `zoo:Safari Niagara`；sources 與新增 `instagram:` 欄各補兩則官方 IG（帶帳號形式 thecalgaryzoo／safariniagara）；現居、引言改寫（SSP 轉出、父母仍在 Calgary）
- `index.md` — Aahana 現居改 Safari Niagara、備注加「2024 移居」；最後更新 2026-07-23

**備注**：讀者回報（收件匣 `bZN9zl7`，回報效期 2024-12）。兩則佐證皆為園方**官方 IG 帳號**（來源園＋目的園雙邊確認），依 CLAUDE.md「官方來源可直接採用」採納。離園月份採 Calgary 官方公告（2024-11），到園月份採回報效期（2024-12，官方僅確認 2025-03 已在園、未載明確切到園日）。Safari Niagara 已登記於 `data/zoos.json`。無 RPF profile。

## [2026-07-24] update | `kirara-2002-06-29` 補母 `lala-2000-06-27`（讀者回報，官方確認）

**來源**：
- https://www.city.sabae.fukui.jp/nishiyama_zoo/news/2011_news.html （鯖江市西山動物園官網訃告，2011：`ヒサシ`「2002年には、ララとの間に子どもを1頭もうけました」）

**更新條目**：
- `kirara-2002-06-29.md` — 母由「待查證」改 `lala-2000-06-27`（該園同期唯一的 `ララ`，RPF #341）；引言補母、sources 補西山官網、家族注改為官方佐證
- `lala-2000-06-27.md` — 子女表與引言補 `kirara-2002-06-29`（雙向 wikilink）

**備注**：讀者回報（收件匣 `RW8oO5j`，回報者 楊桃）。父 `hisashi-1993-06-30` 一生僅居西山，`lala-2000-06-27` 為西山 2000–2015 唯一同名個體，故母親確認為此隻。依 CLAUDE.md「官方來源可直接採用」採納。

---

## [2026-07-24] rename+update | `栃` 生日更正 2001-07-04 → 2001-07-24，slug 隨改（讀者回報，官方確認）

**來源**：
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/news-blog/osirase/d066363.html （旭川市旭山動物園官網訃告：「『栃』は2001年7月24日広島県安佐動物公園生まれのメス」）

**更新條目**：
- `tochi-2001-07-04.md` → `tochi-2001-07-24.md` — `born` 與 `zoos:` 起始日由 2001-07-04 改 2001-07-24；引言生日改寫；sources 補旭山官網
- `index.md` — `栃` slug 更新；最後更新 2026-07-24
- 同步更換 14 筆條目內 `[[tochi-2001-07-04]]` → `[[tochi-2001-07-24]]`：`banana-1996-08-09`、`daichi-2006-08-01`、`kojirou-2010-07-14`、`koto-2009-07-09`、`kurumi-2011-07-18`、`mikan-2011-07-18`、`nono-2002-07-15`、`ron-ron-1995-06-30`、`ron-ron-2013-07-19`、`shii-2000-07-13`、`sora-2006-08-01`、`yuu-yuu-2011-05-28`、`yuu-yuu-2014-07-27`

**備注**：讀者回報（收件匣 `gbW9d2P`，回報者 楊桃）。原 07-04 疑為 RPF 誤植；旭山官方訃告載明 07-24，另經搜尋獨立核對一致。依 CLAUDE.md「官方來源可直接採用」採納並更正既有 wiki。

---

## [2026-07-24] add | 深圳野生動物園 4 隻檔案卡（維護者提供，無官方佐證）

**來源**：
- 維護者提供（2026-07-24）：太子 ♀、毛毛 ♂、點點 ♂、桃子 ♀（桃子 2025 年 12 月離世）

**新增條目**：
- `tai-zi-shenzhen.md` — 太子 Tai Zi，♀，現居深圳野生動物園；生年・家系不詳
- `mao-mao-shenzhen.md` — 毛毛 Mao Mao，♂，現居深圳野生動物園；生年・家系不詳；⚠️ 與上海野生動物園 `mao-mao` 同名（不同個體）
- `dian-dian-shenzhen.md` — 點點 Dian Dian，♂，現居深圳野生動物園；生年・家系不詳
- `tao-zi-shenzhen.md` — 桃子 Tao Zi，♀，曾居深圳野生動物園，2025 年 12 月離世 🪽；生年・家系不詳

**更新條目**：
- `data/zoos.json` — 新增登記「深圳野生動物園」（Shenzhen Safari Park；広東省深圳市南山区；wechat 深圳野生动物园）
- `index.md` — 新增「海外個體（中國・深圳野生動物園）」分區 4 筆；條目總數 673 → 677

**備注**：依 2026-07-24 放寬後的檔案卡門檻建檔（名字＋性別已知、綁定已登記園為硬門檻、維護者親自確認即可，官方來源非必要）。四隻皆 `limited-profile`、`sources` 記「維護者提供」→ `has_official_source: false`，網站顯示「維護者提供・未經官方佐證」標記。均無官方公告，生日／出身／父母標 🚧 待查證。無 RPF profile。詳見 `docs/中國個體建檔放寬-計劃.md`。

---

## [2026-07-24] add | 廣州動物園 2 隻檔案卡（維護者提供，無官方佐證）

**來源**：
- 維護者提供（2026-07-24）：朗朗 ♂（目前非展出）、維維 ♂（2024–2025 曾展出，目前非展出）

**新增條目**：
- `lang-lang-guangzhou.md` — 朗朗 Lang Lang，♂，現居廣州動物園、目前非展出；生年・出身・家系不詳
- `wei-wei-guangzhou.md` — 維維 Wei Wei，♂，現居廣州動物園；2024–2025 曾展出、目前非展出；生年・出身・家系不詳

**更新條目**：
- `index.md` — 「海外個體（中國・廣州動物園）」分區新增 2 筆；條目總數 677 → 679

**備注**：依 2026-07-24 放寬後的檔案卡門檻建檔（名字＋性別已知、綁定已登記園「廣州動物園」為硬門檻、維護者親自確認即可，官方來源非必要）。兩隻皆 `limited-profile`、`sources` 記「維護者提供」→ `has_official_source: false`，網站顯示「維護者提供・未經官方佐證」標記。兩隻現正在園（維維目前非展出但仍在園），動向明確故不掛 `unverified`。生年・出身・父母標 🚧 待查證。無 RPF profile。查得生日後依命名規則將 slug 由 `-guangzhou` 改為 `-生日`。

---

## [2026-07-24] update | 檔案卡居住史起始年改為留空（「? – 現在」）

**變更**：限定檔案卡（`limited-profile`）個體的 `zoos:` 起始年，凡屬「僅首次確認、非真正入園／出生年」者一律改為**留空**，渲染為「? – 現在」（已故則「? – 死亡日」），比照 `pei-pei`／`kang-kang` 等既有廣州條目慣例。原先填「首次確認年份」會在網站顯示假的入園年、污染統計。

**更新條目**（起始年由實際年份改留空）：
- 廣州：`lang-lang-guangzhou`、`wei-wei-guangzhou`
- 深圳：`dian-dian-shenzhen`、`mao-mao-shenzhen`、`tai-zi-shenzhen`、`tao-zi-shenzhen`（訖留 2025）
- 大連：`nuo-mi-dalian`、`xi-ning-dalian`、`mi-duo-dalian`
- 柳州：`luo-ke-liuzhou`、`xiao-hong-liuzhou`、`xiong-da-liuzhou`、`da-lian-liuzhou`（訖留 2026-02-22）

**政策**：`CLAUDE.md` 檔案卡規則同步更新——起始年預設留空（覆蓋舊「一律填首次確認年份」）；已知副作用為空白起始首站會被標 🐣（可接受，老條目皆然）。

**備注**：`gen_residence` → `build_db` → `export_json` 已重建；`audit --strict`、`check_twins` 皆通過。

---

## [2026-07-24] update | 新增「已宣告手足」機制，補顯示 `luo-xi` × `luo-ke-liuzhou` 兄妹

**背景**：`luo-xi`（洛茜）與 `luo-ke-liuzhou`（洛克）為維護者確認的兄妹，但兩隻共同父母不詳。網站家系原僅由共同父母推導手足，故站上不顯示此關係。

**新增機制**：frontmatter 新增選填欄位 `siblings:`——維護者確認為兄弟姊妹、但父母不詳無法推導時才用；對稱（單邊列出即可），網站顯示為未分血緣度的「兄弟姊妹」列。父母已知者仍走共同父母自動推導、勿用此欄。

**改動**：
- `tools/schema.sql` — 新增 `declared_siblings` 表（對稱，slug_a < slug_b）
- `tools/build_db.py` — 解析 frontmatter `siblings:` → 建對稱邊
- `pipeline/scripts/export_json.py` — 每隻補 `declared_siblings`、`family.json` 加 `declared_siblings` 邊
- `web/src/lib/data.js` — 計算顯示清單（排除已列為全血／半血、直系父母/子女者）
- `web/src/components/Panda.astro` — 家族卡新增一列
- `pipeline/src/i18n/*.json`（五語）— 新增 `rel_siblings_unknown` 字串
- `SCHEMA.md` — 記錄 `siblings:` 欄位用法

**更新條目**：
- `luo-xi.md`、`luo-ke-liuzhou.md` — 各加 `siblings:` 指向對方

**備注**：`build_db` → `export_json` 已重建（`declared_siblings` 邊 1 組已出現於 `family.json` 與兩隻的 `pandas.json`）；`audit --strict`、`check_twins` 皆通過。Astro 站需 CI／本機重建生效。

## [2026-07-24] add | 無錫動物園三隻（暖暖・露露・暖寶寶）＋新登記兩座園

**來源**：
- 讀者 Gaia 回報，附無錫動物園官網 https://www.wxzoo.com.cn/（維護者確認採用）

**新登記動物園**（`data/zoos.json`）：
- `無錫動物園`（Wuxi Zoo，江蘇省無錫市濱湖區・太湖歡樂園）
- `宜興隱龍谷君瀾度假酒店`（Yixing Inlong Narada Resort Hotel，江蘇省無錫市宜興市）
- 座標為近似值、`宜興隱龍谷` 官網待補，🚧 待查證

**新增條目**（維護者確認、`limited-profile`；來源記 `維護者提供（2026-07-24）`、無官方佐證）：
- `nuan-nuan-wuxi.md` — 暖暖 Nuan Nuan（♀），生年不詳，現居 無錫動物園、目前未展出；暖寶寶之母
- `lulu-2022-06-18.md` — 露露 Lulu（♀），生於 2022-06-18，現居 無錫動物園
- `nuan-bao-bao-2023-07-06.md` — 暖寶寶 Nuan Bao Bao（♀），生於 2023-07-06，暖暖之女；2026 曾短暫轉 宜興隱龍谷君瀾度假酒店、同年返回無錫

**暫緩／候補**（`data/cn-candidates.json`）：
- `麻團` — 雄性，月餅之雙胞胎哥哥；資料矛盾（報稱 2026-06-16 生於杭州動物園，卻又 2024 年轉無錫），待維護者釐清生日／轉園年份後轉正
- `月餅` — 麻團之雙胞胎手足，性別未述（未達建檔門檻），現於杭州動物園、未展出

**更新條目**：
- `index.md` — 新增「海外個體（中國・無錫動物園）」分類三筆；條目總數 683 → 686

## [2026-07-25] add | 成都動物園全雌性八隻（檔案卡）＋新登記成都動物園

**來源**：
- 維護者提供（2026-07-25）；成都動物園官網 http://www.cdzoo.com.cn/（園名/地點參考，個體名單無官方公告佐證）

**新登記動物園**（`data/zoos.json`）：
- `成都動物園`（Chengdu Zoo，四川省成都市成華区昭覺寺南路234號；1953 創立、1976 遷現址）——與既有 `Chengdu Research Base of Giant Panda Breeding`（成都大熊貓繁育研究基地，panda.org.cn）為不同機構；座標 30.6989,104.0986 為近似值 🚧

**新增條目**（維護者提供、`limited-profile`、`sex: female`、`species: styani`；來源記 `維護者提供（2026-07-25）`、無官方佐證；生日／入園年／家系均不詳，`zoos:` 起始留空 `( – 現在)`、`last_seen: 2026-07`；未掛 `unverified`，確認現存）：
- `qiu-qiu-chengdu.md` — 球球 Qiu Qiu（♀）
- `jiu-jiu-chengdu.md` — 玖玖 Jiu Jiu（♀）
- `qian-qian-chengdu.md` — 淺淺／浅浅 Qian Qian（♀）
- `mao-mao-chengdu.md` — 毛毛 Mao Mao（♀）
- `wai-wai-chengdu.md` — 歪歪 Wai Wai（♀）
- `yuan-yuan-chengdu.md` — 圓圓／圆圆 Yuan Yuan（♀）
- `han-han-chengdu.md` — 憨憨 Han Han（♀）
- `dou-dou-chengdu.md` — 豆豆 Dou Dou（♀）

**備注**：查得各隻生日後依命名規則將 slug 由 `名字-chengdu` 更名為 `名字-生日` 並同步修正 wikilink。既有 `毛毛`（上海野生動物園 `mao-mao.md`）、`憨憨`（柳州 `han-han-liuzhou.md`，另 `cn-candidates` 亦有柳州憨憨）、`豆豆`（`dou-dou.md`）為不同個體，以園簡稱區隔。

**更新條目**：
- `index.md` — 新增「海外個體（中國・成都動物園）」分類八筆；條目總數 686 → 694

## [2026-07-25] fix | Mutan 西山→茶臼山移動日 2020-01-18 → 2021-01-18（官網更正）

**來源**：
- https://www.city.sabae.fukui.jp/nishiyama_zoo/news/2021_news.html （鯖江市西山動物園 2021年ニュース「ムータンが旅立ちます」：移動日 令和３年１月１２日 ※降雪により１月１８日に移動）

**更新條目**：
- `mutan-2014-06-19.md` — 依西山動物園官網更正 `zoos:` 移動日：鯖江市西山動物園訖與長野市茶臼山動物園起由 `2020-01-18` 改為 `2021-01-18`（原僅有 RPF 來源、年份誤差一年）；居住史表格同步；`sources` 補西山官網。回報者「楊桃」填目的地「京都市動物園」為出生園之誤，未採納。
- `contributors.json` — 更新「楊桃」致謝 note。

## [2026-07-25] add | Kiki 喜喜（RPF #331）與其全血緣手足

**來源**：
- https://redpandafinder.com/#profile/331 (Kiki)
- https://redpandafinder.com/#profile/477 (Aporo)
- https://redpandafinder.com/#profile/714 (Ten-Ten)
- https://redpandafinder.com/#profile/716 (Kei-Kei)
- https://redpandafinder.com/#profile/715 (Ai-Ai)

**新增條目**（`rin-rin-1999-07-09` 怜怜 × `ryuunosuke-1999-07-27` 緑之介 之子女；RPF 為線索）：
- `kiki-2007-07-25.md` — Kiki 喜喜（♀，RPF #331），生於 2007-07-25 愛媛県立とべ動物園，2009-11-25 移居長崎バイオパーク（現居）
- `aporo-2004-06-28.md` — Aporo アポロ（♂，RPF #477），2004-06-28 生、2023-04-03 歿；`luna-2004-06-28` 之雙胞胎；とべ→ソウル大公園動物園
- `ten-ten-2005-07-12.md` — Ten-Ten 天天（♂，RPF #714），2005-07-12 生、2014-10-07 歿；とべ→恩賜上野動物園→天王寺動物園（同名消歧註記）
- `kei-kei-2008.md` — Kei-Kei（♂，RPF #716），僅知生年 2008、RPF 標示已歿；生日／居住史／歿日不詳 🚧（`zoos: []`）
- `ai-ai-2008.md` — Ai-Ai（♀，RPF #715），僅知生年 2008、RPF 標示已歿；生日／居住史／歿日不詳 🚧（`zoos: []`）

**更新條目**（回填雙向 wikilink）：
- `ron-ron-2002-06-28.md` — 兄弟姊妹表六隻改為 wikilink
- `luna-2004-06-28.md` — 雙胞胎／兄弟姊妹改 wikilink；更正雙胞胎 `aporo` 性別 ♀→♂
- `rin-rin-1999-07-09.md`、`ryuunosuke-1999-07-27.md` — 子女敘述補齊七名手足 wikilink
- `index.md` — 新增「Ron-Ron 的兄弟姊妹（父方旁系）」分類五筆；條目總數 694 → 699

## [2026-07-26] add | 南京市紅山森林動物園 三隻（藍羽・兔子・糖芋苗）

**來源**：
- 維護者提供（2026-07-26）；無官方公告佐證，🚧 待查證

**新增條目**（檔案卡 `limited-profile`；生日／年份全部不詳）：
- `lan-yu-nanjing.md` — 藍羽／蓝羽 Lan Yu（♂），現居南京市紅山森林動物園，自常州淹城野生動物世界轉入（年份不詳）；糖芋苗之父
- `tu-zi-nanjing.md` — 兔子 Tu Zi（♀）🪽，曾居南京市紅山森林動物園，已故、歿日不詳（`died: "?"`）；糖芋苗之母
- `tang-yu-miao-nanjing.md` — 糖芋苗 Tang Yu Miao（♂），生於南京市紅山森林動物園、現居同園；`lan-yu-nanjing` × `tu-zi-nanjing` 之子

**備注**：三隻皆無生日資料，slug 依檔案卡規則用園簡稱（`名字-nanjing`）；`zoos:` 起始年留空（不詳抵達年，渲染為「? – 現在」）。既有紅山個體 `xiao-xiao-bai-nanjing`、`xia-wa` 一系與本批無已知親緣關係。查得生日後依命名規則改為 `名字-生日` 並同步修正 wikilink。

**更新條目**：
- `index.md` — 「海外個體（中國・南京市紅山森林動物園）」新增三筆；條目總數 699 → 702

## [2026-07-26] update | 六隻補居住史（Drusillas 三隻・多摩三隻）、`you-you-1997-06-20` 補日文名

**背景**：網站新增「地區」篩選後盤點出 10 隻個體無法歸屬任何地區，原因皆為 frontmatter `zoos:` 空白或缺欄。本批補回六隻，餘四隻（`ai-ai-2008`、`kei-kei-2008`、`kachin-1995-05-31`、`ki-ki-1996`）仍無居住地線索。

**來源**：
- https://www.drusillas.co.uk/news/red-pandas-born-at-drusillas-park-
- https://www.drusillas.co.uk/news/panda-pair-arrive-at-zoo-in-sussex
- https://www.drusillas.co.uk/news/red-pandas-babies-are-named-at-drusillas
- 維護者提供（2026-07-26：`hana-hana`、`naka-naka`、`hou-hou-1988` 居住多摩動物公園）
- 維護者提供（2026-07-26：`you-you-1997-06-20` 日文名補「葉々」）

**更新條目**：
- `anmar-2014-06-16.md`、`mya-2014-06-16.md` — 依園方報導補 `zoos: Drusillas Park (2014-06-16 – 現在)`（出生園，標 🐣）；🚧 註記改寫——「現在」僅表示查無離園紀錄、非園方確認之現居，仍掛 `unverified` 不計入現存統計
- `tibao-2011.md` — 補 `zoos: Drusillas Park (2012 – 現在)`；抵園前的 Zoo d'Asson 期間起始不詳，寫入 frontmatter 會被自動標為 🐣 出生地（等同宣稱生於 Asson），故僅記於內文敘述、不進 `zoos:`
- `hana-hana.md`、`naka-naka.md` — 補 `zoos: 多摩動物公園`（起訖不詳）、`birth_zoo: unknown`（多摩名單明載「出自不明」，不標 🐣）、`died: "?"`（原僅有 `deceased` tag 而無 `died`，會被居住史誤標 🏡 現居）、tag 補 `zoo:多摩動物公園`
- `hou-hou-1988.md` — 補 `zoos: 多摩動物公園 ( – 1999)`、`birth_zoo: unknown`（入園年份與出生園皆不詳）、tag 補 `zoo:多摩動物公園`；`sources` 的「作者提供」改「維護者提供」
- `you-you-1997-06-20.md` — `japanese` 由「葉葉 / ユウユウ」改為「葉葉, 葉々, ユウユウ」（比照雙胞胎 `fu-fu-1997-06-20` 的「風風, 風々, フウフウ, ふうふう」寫法）；標題同步

**備注**：條目總數不變（702）。`birth_zoo: unknown` 為本次新增的選填 frontmatter 欄位，見 SCHEMA.md 與 CHANGELOG.md 同日條目。

## [2026-07-26] update | `ki-ki-1996` 補居住史（多摩 → 墨西哥）、合併 チャプルテペック動物園 重複登記

**來源**：
- 維護者提供（2026-07-26：`ki-ki-1996` 生於多摩動物公園，後移居チャプルテペック動物園；日期不詳）

**更新條目**：
- `ki-ki-1996.md` — 補 `zoos: 多摩動物公園 (1996 – )`（出生園，起始年＝生年故標 🐣）與 `チャプルテペック動物園 ( – 現在)`；tag 補兩座園。**移園日期與離開多摩的年份皆不詳**，🚧 註記改寫說明「現在」僅表示查無後續紀錄；父母仍為〔待查證〕，`unverified` 維持
- `data/zoos.json` — 合併重複登記：刪除 `Chapultepec Zoo`（`lineage_id` 66、無 wiki 條目使用），其 `lineage_id` 與 map 併入實際在用的 `チャプルテペック動物園`（該筆原 `lineage_id` 為 null、走合成 ID）；註冊表 345 → 344 座
- `data/zoos.json` — 補 `location_zh`：チャプルテペック動物園「墨西哥墨西哥城」、Buin Zoo「智利首都大區布因」。兩園的 `location_ja` 為片假名（メキシコ・メキシコシティ／チリレヒオン・メトロポリターナ州ブイン），中文介面缺 `location_zh` 時會退回 `location_ja`、對中文讀者不可讀

**備注**：條目總數不變（702）。配套工具修正見 CHANGELOG.md 同日條目（`export_json.py` 現居判定、`gen_residence.py` 國旗表）。

## [2026-07-26] add | 清遠長隆森林王國 八隻（新園登記）

**來源**：
- 維護者提供（2026-07-26；zoo 友告知）；無官方公告佐證，🚧 待查證
- 園方官網（園區資訊，非個體名單）：https://www.chimelong.com/qy/forestkingdom/

**新增條目**（檔案卡 `limited-profile`；生日／入園年份全部不詳，性別由維護者確認）：
- `da-ge-qingyuan.md` — 大哥 Da Ge（♂）
- `xiao-xiong-bing-gan-qingyuan.md` — 小熊餅乾／小熊饼干 Xiao Xiong Bing Gan（♂）
- `pi-pi-qingyuan.md` — 皮皮 Pi Pi（♀）
- `niu-niu-qingyuan.md` — 妞妞 Niu Niu（♀）；與上海動物園 `niu-niu` 同名、非同一隻
- `qi-qi-qingyuan.md` — 琪琪 Qi Qi（♀）
- `jojo-qingyuan.md` — Jojo（♀）；以英文名登錄，無中文名
- `lady-qingyuan.md` — Lady（♀）；以英文名登錄，無中文名
- `pang-pang-qingyuan.md` — 胖胖 Pang Pang（♀）

**備注**：八隻皆無生日資料，slug 依檔案卡規則用園簡稱（`名字-qingyuan`）；`zoos:` 起始年留空（不詳抵達年，渲染為「? – 現在」）；`last_seen: 2026-07`、皆為現況在世故不掛 `unverified`。`sources` 為「維護者提供」（無 host）故 `has_official_source` 為 false，網站顯示未經官方佐證標記。查得生日後依命名規則改為 `名字-生日` 並同步修正 wikilink。

**更新條目**：
- `data/zoos.json` — 新增登記「清遠長隆森林王國」（Chimelong Forest Kingdom，広東省清遠市清城区；官網 chimelong.com/qy/forestkingdom）；座標暫缺（lat／lng 為 null）。註冊表 344 → 345 座
- `niu-niu.md` — 補 ⚠️ 同名提示，指向 `niu-niu-qingyuan`
- `index.md` — 新增分類「海外個體（中國・清遠長隆森林王國）」八筆；條目總數 702 → 710

## [2026-07-26] add | 南京市紅山森林動物園 四隻（新園登記：南京金牛湖野生動物王國）

**來源**：
- 維護者提供（2026-07-26）；無官方公告佐證，🚧 待查證
- 金牛湖園方官網（園區資訊，非個體名單）：https://www.zoojnh.cn/ ；英文頁 https://www.zoojnh.cn/en/

**新增條目**（檔案卡 `limited-profile`；生日／轉入年份全部不詳，性別由維護者確認）：
- `niu-niu-nanjing.md` — 牛牛 Niu Niu（♂）；自南京金牛湖野生動物王國轉入，年份不詳
- `rou-rou-nanjing.md` — 肉肉 Rou Rou（♀）；自南京金牛湖野生動物王國轉入，年份不詳
- `hei-xuan-feng-nanjing.md` — 黑旋風／黑旋风 Hei Xuan Feng（♂）；自常州淹城野生動物世界轉入，年份不詳；`nuo-mi-nanjing` 之父
- `nuo-mi-nanjing.md` — 糯米 Nuo Mi（♂）；`hei-xuan-feng-nanjing` 之子，母不詳

**更新條目**：
- `data/zoos.json` — 新增登記「南京金牛湖野生動物王國」（Nanjing Jinniu Lake Wildlife Kingdom，江蘇省南京市六合区；官網 zoojnh.cn）；座標暫缺（lat／lng 為 null）。註冊表 345 → 346 座。**維護者原稱「南京金牛湖野生動物世界」，依官網正式名定 canonical 為「王國」，「世界」寫入 aliases**
- `du-du.md` — 補出身：由南京金牛湖野生動物王國轉入（年份不詳），`zoos:` 增列該園、tag 補 `zoo:南京金牛湖野生動物王國`；待查證項目由「出身（園內繁殖或外園轉入）」改為「出身園是否為金牛湖、轉入紅山年份」；`sources` 的「作者提供」改「維護者提供」並註明本次補正
- `niu-niu.md`、`niu-niu-qingyuan.md` — ⚠️ 同名提示增列 `niu-niu-nanjing`（三隻羅馬拼音相同：上海妞妞♀、清遠妞妞♀、南京牛牛♂）
- `nuo-mi-dalian.md` — 補 ⚠️ 同名提示，指向 `nuo-mi-nanjing`（大連糯米♀ vs 南京糯米♂，中文名相同）
- `rou-rou-2008-07-09.md` — 補 ⚠️ 同名提示，指向 `rou-rou-nanjing`（香港柔柔 vs 南京肉肉，僅拼音相同）
- `index.md` — 南京分類新增四筆、`du-du` 說明改為「自南京金牛湖轉入」；條目總數 710 → 714

**備注**：四隻皆無生日資料，slug 依檔案卡規則用園簡稱（`名字-nanjing`）；`zoos:` 起始年留空（不詳抵達年，渲染為「? – 現在」，首站因既有慣例會帶 🐣 符號）；`last_seen: 2026-07`、皆為現況在世故不掛 `unverified`。`sources` 為「維護者提供」（無 host）故 `has_official_source` 為 false，網站顯示未經官方佐證標記。糯米之母、黑旋風與牛牛／肉肉／糯米的生日與轉入年份待查。

## [2026-07-26] add | 常州淹城野生動物世界 二十一隻（新園登記：鄂州靈玲野生動物王國）

**來源**：
- 維護者提供（2026-07-26）；個體名、性別、生卒與轉園年份皆由維護者確認，無官方公告佐證，🚧 待查證
- 淹城園方官網（園區資訊，非個體名單）：https://www.yczoo.com/ ；紅熊貓館 https://www.yclyq.com/11306.html
- 鄂州靈玲園區佐證（政府公告／新聞，非個體名單）：鄂州市國資委 2023-08-25 https://gzw.ezhou.gov.cn/xwzx/gqdt/202308/t20230825_570740.html （靈玲文旅集團落戶鄂州園博園，文中列明旗下含「江苏灵玲淹城野生动物世界」）；荊楚網 2026-03-31 http://news.cnhubei.com/content/2026-03/31/content_19896791.html （2026-03-30 開園、華中最大小熊貓種群繁育基地）

**新增條目**（檔案卡 `limited-profile`；生日／入園年份全部不詳，性別由維護者確認）：

雄性 6 隻：
- `ya-se-yancheng.md` — 亞瑟／亚瑟 Ya Se（♂）；2025 年歿 🪽，精確歿日不詳
- `yi-yi-yancheng.md` — 一一 Yi Yi（♂）；與廣州 `yi-yi-2023-06-28`（逸逸）拼音相同、非同一隻
- `yi-zhi-er-yancheng.md` — 一隻耳／一只耳 Yi Zhi Er（♂）
- `jing-jing-yancheng.md` — 靜靜／静静 Jing Jing（♂）；2026 年轉至鄂州靈玲野生動物王國
- `ti-la-yancheng.md` — 提拉 Ti La（♂）；`mi-su-yancheng`（米蘇）之雙胞胎哥哥
- `tuan-zi-yancheng.md` — 團子／团子 Tuan Zi（♂）；2026 年轉至鄂州靈玲野生動物王國

雌性 15 隻：
- `tao-hua-yancheng.md` — 桃花 Tao Hua（♀）；2025 年歿 🪽；與多摩 `taofa-2015-06-14` 中文名相同、非同一隻
- `mu-lan-yancheng.md` — 木蘭／木兰 Mu Lan（♀）
- `hong-shu-yancheng.md` — 紅薯／红薯 Hong Shu（♀）
- `mi-su-yancheng.md` — 米蘇／米苏 Mi Su（♀）；`ti-la-yancheng`（提拉）之雙胞胎妹妹、`mi-hu-yancheng`（米糊）之母
- `mi-hu-yancheng.md` — 米糊 Mi Hu（♀）；`mi-su-yancheng`（米蘇）之女，父不詳
- `jiao-tang-yancheng.md` — 焦糖 Jiao Tang（♀）；`bu-ding-yancheng`（布丁）之雙胞胎姐姐
- `bu-ding-yancheng.md` — 布丁 Bu Ding（♀）；`jiao-tang-yancheng`（焦糖）之雙胞胎妹妹；2026 年轉至鄂州靈玲野生動物王國
- `hui-xiang-yancheng.md` — 茴香 Hui Xiang（♀）
- `hei-mei-yancheng.md` — 黑妹 Hei Mei（♀）；別名「短短」
- `mu-si-yancheng.md` — 沐絲／沐丝 Mu Si（♀）；別名「角角」
- `chu-wu-yancheng.md` — 初霧／初雾 Chu Wu（♀）
- `zhu-li-yancheng.md` — 朱莉 Zhu Li（♀）
- `sha-qi-ma-yancheng.md` — 沙琪瑪／沙琪玛 Sha Qi Ma（♀）
- `lu-lu-yancheng.md` — 露露 Lu Lu（♀）；與無錫 `lulu-2022-06-18` 中文名相同、非同一隻
- `mei-jing-yancheng.md` — 梅景 Mei Jing（♀）

**更新條目**：
- `data/zoos.json` — 新增登記「鄂州靈玲野生動物王國」（Ezhou Lingling Wild Animal Kingdom，湖北省鄂州市鄂城区；2026-03-30 開園，隸屬靈玲文旅集團，與廈門靈玲動物王國、常州淹城野生動物世界為姊妹園）；座標與官網暫缺（lat／lng／website 為 null）。註冊表 346 → 347 座
- `data/cn-candidates.json` — 刪除已轉正的淹城五筆（桃花、木蘭、黑妹、沐絲、初霧）；候補 8 → 3 筆
- `taofa-2015-06-14.md` — 補 ⚠️ 同名提示，指向 `tao-hua-yancheng`（多摩桃花 vs 淹城桃花，中文名相同）
- `lulu-2022-06-18.md` — 補 ⚠️ 同名提示，指向 `lu-lu-yancheng`（無錫露露 vs 淹城露露，中文名相同）
- `yi-yi-2023-06-28.md` — 補 ⚠️ 同名提示，指向 `yi-yi-yancheng`（廣州逸逸 vs 淹城一一，拼音相同）
- `index.md` — 新增分類「海外個體（中國・常州淹城野生動物世界）」十八筆與「海外個體（中國・鄂州靈玲野生動物王國）」三筆；條目總數 714 → 735

**備注**：二十一隻皆無生日資料，slug 依檔案卡規則用園簡稱、依維護者指定採園名「淹城」而非城市名（`名字-yancheng`）；`zoos:` 起始年一律留空（不詳抵達年，渲染為「? – 現在」，首站因既有慣例會帶 🐣 符號），轉至鄂州的三隻**兩園起訖年份均留空**（僅記先後順序，比照 `hei-xuan-feng-nanjing`）；歿者訖填 2025。`last_seen: 2026-07`（歿者 2025），現況在世故不掛 `unverified`。`sources` 為「維護者提供」（無 host）故 `has_official_source` 為 false，網站顯示未經官方佐證標記。淹城與鄂州同屬靈玲文旅集團，此前已有小小白、藍羽、黑旋風三隻自淹城轉入南京市紅山森林動物園。查得生日後依命名規則改為 `名字-生日` 並同步修正 wikilink。

## [2026-07-27] add | 新增中國個體六筆：無錫麻團與杭州動物園五隻

**來源**：
- 維護者提供（2026-07-27）：麻團（♂，2023-06-16 生，父山竹）、月餅（♀，麻團之雙胞胎妹妹）、山竹（♂，2018 生）、楊桃（♀，2018 生，山竹之雙胞胎妹妹、桃子之母）、文文（♀）、朵朵（♀）
- 讀者回報（圖鑑缺漏收件匣，2026-07-24，回報者：Gaia）：麻團生於杭州動物園、2024 年轉入無錫動物園；月餅現於杭州動物園、目前未展出

**新增條目**：
- `ma-tuan-2023-06-16.md` — 麻團／麻团 Ma Tuan（♂），2023-06-16 生於杭州動物園，2024 年轉入無錫動物園；父 `shan-zhu-2018`，與 `yue-bing-2023-06-16` 雙胞胎
- `yue-bing-2023-06-16.md` — 月餅／月饼 Yue Bing（♀），2023-06-16 生於杭州動物園、現居杭州；`ma-tuan-2023-06-16` 之雙胞胎妹妹
- `shan-zhu-2018.md` — 山竹 Shan Zhu（♂），2018 年生；`yang-tao-2018` 之雙胞胎哥哥、麻團與月餅之父
- `yang-tao-2018.md` — 楊桃／杨桃 Yang Tao（♀），2018 年生；`shan-zhu-2018` 之雙胞胎妹妹，育有一女「桃子」
- `wen-wen-hangzhou.md` — 文文 Wen Wen（♀），生年・家系不詳
- `duo-duo-hangzhou.md` — 朵朵 Duo Duo（♀），生年・家系不詳

**更新條目**：
- `data/zoos.json` — 杭州動物園正式名由英文 `Hangzhou Zoo` 改為中文 `杭州動物園`（比照其他中國園慣例），補 `zh: 杭州动物园`、`location_ja: 浙江省杭州市`，舊名與變體移入 aliases；註冊表座數不變（347）
- `data/cn-candidates.json` — 刪除已轉正的麻團、月餅兩筆（生日經維護者確認為 2023-06-16，先前回報之 2026-06-16 為誤植，轉園年份矛盾隨之解消）；候補 3 → 1 筆
- `lulu-2022-06-18.md`、`nuan-nuan-wuxi.md` — 同園個體清單補入 `ma-tuan-2023-06-16`
- `index.md` — 無錫動物園分類新增麻團一筆；新增分類「海外個體（中國・杭州動物園）」五筆；條目總數 735 → 741

**備注**：六隻皆依「資料有限個體：檔案卡」規則建檔（`limited-profile`、`last_seen: 2026-07`，現況在世故不掛 `unverified`）。麻團與月餅生日明確、slug 用標準「名字-生日」；山竹與楊桃只知生年，slug 為「名字-年份」；文文與朵朵無生日，slug 用園簡稱 `名字-hangzhou`，查得生日後改回標準 slug 並同步修正 wikilink。山竹・楊桃・文文・朵朵的 `zoos:` 起始年留空（不詳抵達年，渲染為「? – 現在」，首站因既有慣例會帶 🐣 符號）；麻團與月餅確知生於杭州故填生日為起始。麻團與月餅之母不詳、山竹與楊桃之父母不詳，一律留「不詳（待查證）」，未從 RPF/lineage 腦補。楊桃之女「桃子」僅知名字，未達建檔門檻，以純文字記於楊桃 `## 家族`，並於楊桃條目加 ⚠️ 同名提示指向深圳已故的 `tao-zi-shenzhen`。`sources` 為「維護者提供」（無 host）故 `has_official_source` 為 false，網站顯示未經官方佐證標記。

## [2026-07-27] update | 麻團 補入無錫日報 2024 報導（轉園時間細化、認養更名線索；喬喬・久久記入候補）

**來源**：
- https://www.wxrb.com/doc/2024/07/09/356287.shtml — 無錫日報報業集團「無錫新傳媒網」2024-07-09〈动物园来了新晋"顶流"——小熊猫"麻团"入赘无锡〉（來源：江南晚報）；文中直接引述無錫動物園保育員高蒙丹

**更新條目**：
- `ma-tuan-2023-06-16.md` — 新增上述報導連結為 `sources` 首項；內文補入園經過（後勤繁育場適應 20 天後於萌寵樂園展出）、「入贅」引入新鮮種源以豐富血統、保育員談性格、與暖寶寶／喬喬／久久相處、愛吃蘋果「蘋果收割機」、2024-07 體重 5.4 公斤、長三角動物園聯盟（2024 成立於上海動物園，無錫與杭州同為成員）背景；加 📝 佐證註記。**待查證項目更新**：移除「轉入無錫之確切日期與事由」（事由已明），改列「母親」「更名田田是否實行」「確切轉入日」
- `index.md` — `ma-tuan-2023-06-16` 說明改為「生於杭州動物園、2024『入贅』轉入；2024 年報導稱將由揚名實驗學校認養更名『田田』🚧」。條目總數不變
- `data/cn-candidates.json` — 新增無錫動物園 `喬喬`、`久久` 兩筆（報導提及之園內同齡個體，性別／生日／家系皆未載，未達檔案卡門檻）。候補 1 → 3 筆

**備注**：
- **更名「田田」未採用**：報導末段稱麻團已由無錫市梁溪區揚名實驗學校認養、「即將更名為田田」，但維護者確認現仍稱麻團，故 `name`／`chinese` 維持 `Ma Tuan`／`麻團`，僅於內文與 index 註記待查證（維護者裁定 2026-07-27）。
- **來源顯示**：wxrb.com 為新聞媒體、非園方官網／政府／官方微信，依 2026-07-07 最嚴政策不列入 `build_db.py` 的 `OFFICIAL_HOSTS`，故此連結**保留在 frontmatter 供校訂與稽核、但不顯示**於個體頁來源區塊，`has_official_source` 仍為 false（與 `meng-xia-2025-07-17`、`xia-wa` 已收之新浪／荔枝新聞連結同一處理）。報導內容改以內文 📝 註記呈現，讀者仍看得到事實與出處。是否放寬「新聞媒體」為可顯示層待維護者裁定。
- **轉園時間僅記至年份**：報導可推得入園約 2024 年 6 月，但 `zoos:` 的日期模型只吃完整 `YYYY-MM-DD` 或純 `YYYY`（`gen_residence.dates_from` 無年月粒度），寫 `2024-06` 會被自動降回 `2024`。故 `zoos:` 維持 `2024`，「2024 年 6 月前後」寫在內文。
- 無錫「久久」與維護者 2026-07-27 提報之「久妹」（♀，2023-06-28 生）名字相近，是否同一隻或手足待釐清；久妹之官方來源連結尚未提供，條目暫未建檔。

## [2026-07-27] add | 新增動物園「杭州少年兒童公園」與該園個體五筆

**來源**：
- 維護者提供（2026-07-27）：奶油（♀）、桃子（♀，2021 年 6 月生，蘋果與楊桃之女）、半半（♂）、蘋果（♂，桃子之父，目前未展出）、楊梅（2025 年 6 月生）
- https://www.hzzoo.com/segyjs.html — 杭州動物園官網〈少儿公园介绍〉（園區基本資料：西湖風景名勝區南線虎跑路 61 號、佔地 180 畝，園內「萌寵樂園」設有小熊貓展區；杭州動物園與杭州少年兒童公園共用同一官網、同屬一家管理單位）

**新增條目**：
- `ping-guo-hangzhou-children.md` — 蘋果／苹果 Ping Guo（♂），生年不詳，現居杭州少年兒童公園、目前未展出；與 `yang-tao-2018` 育有一女 `tao-zi-2021`
- `tao-zi-2021.md` — 桃子 Tao Zi（♀），2021 年 6 月生，現居杭州少年兒童公園；父 `ping-guo-hangzhou-children`、母 `yang-tao-2018`
- `nai-you-hangzhou-children.md` — 奶油 Nai You（♀），生年・家系不詳
- `ban-ban-hangzhou-children.md` — 半半 Ban Ban（♂），生年・家系不詳
- `yang-mei-2025.md` — 楊梅／杨梅 Yang Mei（性別待確認），2025 年 6 月生，家系不詳

**更新條目**：
- `data/zoos.json` — 新增一座「杭州少年兒童公園」（`zh: 杭州少年儿童公园`、`en: Hangzhou Children's Park`、`location_ja: 浙江省杭州市西湖区`、`location_zh: 浙江省杭州市西湖區`、`website` 指官網少兒公園介紹頁）；`lineage_id`、座標留 null（lineage 未收錄、查無可靠座標，比照鄂州靈玲・清遠長隆・金牛湖）。註冊表 347 → 348 座
- `yang-tao-2018.md` — 女兒「桃子」由純文字改為 `[[tao-zi-2021]]`，補配偶 `ping-guo-hangzhou-children`；同名提示改指向新條目；待查證項目更新
- `index.md` — 新增分類「海外個體（中國・杭州少年兒童公園）」五筆；杭州動物園分類的楊桃說明移除「（桃子未建檔）」；條目總數 741 → 746

**備注**：
- 五隻皆依「資料有限個體：檔案卡」規則建檔（`limited-profile`、`last_seen: 2026-07`，現況在世故不掛 `unverified`）。`zoos:` 起始年一律留空（不詳抵達年，渲染為「? – 現在」，首站因既有慣例會帶 🐣 符號）。
- **slug**：無生日的奶油、半半、蘋果用園簡稱後綴 `-hangzhou-children`（`-hangzhou` 已為杭州動物園的 `wen-wen-hangzhou`／`duo-duo-hangzhou` 佔用，故加 `children` 區隔，維護者裁定 2026-07-27）；桃子與楊梅只知年月，依規則降為年份 `tao-zi-2021`、`yang-mei-2025`（月份寫在內文），查得完整生日後改回標準 slug 並同步修正 wikilink。
- **楊梅 `sex:` 留空**：檔案卡門檻本要求性別必填，經維護者裁定破例照建、內文註明「性別待確認」（比照蘋果籽做法），tags 不加性別；公布後回補 `sex` 與性別 tag。
- **居住史只寫少年兒童公園**：桃子之母楊桃現居杭州動物園、兩園同屬一家管理單位，但無公告說明蘋果／桃子是否曾在動物園，故不推測前段居住史，列為待查證（維護者裁定 2026-07-27）。
- **來源顯示**：`sources` 為「維護者提供」（無 host）故 `has_official_source` 為 false，網站顯示未經官方佐證標記；hzzoo.com 官網只佐證該園飼有小熊貓、未載個體資料，故僅登記於 `data/zoos.json` 的 `website`，不列入個體 `sources`（亦未加入 `build_db.py` 的 `OFFICIAL_HOSTS`）。
- 同名提醒：深圳野生動物園已故的 `tao-zi-shenzhen` 🪽 與本批杭州「桃子」為不同個體，兩頁均已加 ⚠️ 提示。

## [2026-07-27] add | 新增中國個體三筆：武漢動物園 糯米雞・歡喜坨・美美（並登記武漢動物園）

**來源**：
- 維護者提供（2026-07-27）：武漢動物園「糯米雞」，♂，生日不詳
- https://www.wuhanzoo.com.cn/main/zxdt/yqgz/detail/3c22beedf2aa40aab9ff9be116c26eac — 武漢動物園官網 2020-09-10〈软萌可爱的小熊猫twins宝宝来啦〉（園方官網＝官方來源）
- http://news.cnhubei.com/content/2020-09/25/content_13357073.html — 荊楚網轉載《武漢晚報》2020-09-25〈它们是武汉动物园首次成功繁育的小熊猫双胞胎"欢喜坨"和"糯米鸡"十月出道〉

**新增條目**：
- `nuo-mi-ji-2020-05-10.md` — 糯米雞／糯米鸡 Nuo Mi Ji（♂），2020-05-10 生於武漢動物園；母 `mei-mei-wuhan`，與 `huan-xi-tuo-2020-05-10` 雙胞胎
- `huan-xi-tuo-2020-05-10.md` — 歡喜坨／欢喜坨 Huan Xi Tuo（性別未公布），2020-05-10 生於武漢動物園；`nuo-mi-ji-2020-05-10` 之雙胞胎手足
- `mei-mei-wuhan.md` — 美美 Mei Mei（♀），生年不詳；歡喜坨・糯米雞之母

**更新條目**：
- `data/zoos.json` — 新增一座：`武漢動物園`（zh 武汉动物园／en Wuhan Zoo／湖北省武漢市漢陽区／官網 wuhanzoo.com.cn）。註冊表 348 → 349 座
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `wuhanzoo.com.cn`（園方官網，來源區塊即顯示）
- `data/cn-candidates.json` — 新增武漢動物園 `糊米酒`、`小小` 兩筆
- `index.md` — 新增分類「海外個體（中國・武漢動物園）」三筆；條目總數更新

**備注**：
- **生日由官方來源改寫維護者提報**：維護者提報時記為「生日不詳」，惟園方官網與《武漢晚報》均載明糯米雞為 2020-05-10（母親節）出生之雙胞胎之一，依「官方來源可直接採用」原則採信，故 slug 走標準「名字-生日」而非檔案卡的園簡稱式。經維護者確認後採用。
- **性別分工**：糯米雞的 ♂ 由維護者提供（官方報導未載明性別）；歡喜坨性別園方從未公布，`sex` 留空、tags 不加性別 tag、內文註明待確認。
- **在世軸**：糯米雞經維護者確認 2026-07 仍在園，故不掛 `unverified`；歡喜坨（最後確認 2020-10）與美美（2020-09）此後六年未見園方個體消息，依規則掛 `unverified` 並記 `last_seen`，不計入現存統計。美美另因無生日、無家系依「資料有限個體」規則加 `limited-profile`，slug 用園簡稱 `mei-mei-wuhan`，查得生日後改回標準 slug 並同步修正 wikilink。
- **父不詳**：園方僅稱 2020-06-21 出生的第三崽（母「小小」，後命名「糊米酒」）與雙胞胎為「同父異母」，可知父為同一隻，但未公布姓名，故一律留「不詳」，未從 RPF/lineage 腦補。
- **未建檔者**：糊米酒（2020-06-21 生，性別未公布）與其母小小（性別可推定為 ♀，但無其他資料）依維護者裁定暫不建條目，記入 `data/cn-candidates.json`。
- 美美與既有 `mei-mei-1989-06-19`／`mei-mei-1999-06-27`／`mei-mei-2007-06-28`／`mei-mei-2022-06-14`／`mei-mei-2023-06-24` 同名無關，條目內已加 ⚠️ 同名提示。

## [2026-07-27] update | 西山動物園 かのこ×Light 2026 年雙胞胎蘋果籽性別確認：1號♀、2號♂

**來源**：
- https://x.com/nishiyama_zoo/status/2081588807456215393 — 鯖江市西山動物園官方 X，公布雌雄鑑定結果（園方官方帳號＝官方來源）

**更新條目**：
- `apple-seed-1-kanoko-2026-06-26.md` — `sex: female`；tags 加 `female`；`sources` 增列官方 X 公布連結；引言加 ♀、佔位提示移除「性別待確認」；內文補雌雄公布說明；家族欄雙胞胎補 ♂
- `apple-seed-2-kanoko-2026-06-26.md` — `sex: male`；tags 加 `male`；`sources` 增列官方 X 公布連結；引言加 ♂、佔位提示移除「性別待確認」；內文補雌雄公布說明；家族欄雙胞胎補 ♀
- `kanoko-2016-06-24.md` — 子女表兩隻蘋果籽性別 ？→ ♀／♂；小節標題「5 隻：1 女 2 男 2 待確認」→「5 隻：2 女 3 男」；RPF 欄「待建檔」→「—」（RPF 為線索非指標，缺就留空不寫待補）
- `light-2013-07-18.md` — 子女表兩隻蘋果籽性別 ？→ ♀／♂
- `index.md` — Kanoko × Light 家族分類兩列性別 ？→ ♀／♂

**備注**：
- 性別由維護者提報並附園方官方 X 貼文，依「官方來源可直接採用」原則直接更新。X 連結工具端無法抓取內容，公布日期依維護者告知記載：**1號（♀）為 2026-07-27 公布**；2號（♂）公布日期未確認，內文僅記「園方於官方 X 公布」。
- 兩隻仍未正式命名，`apple-seed` tag 與佔位提示保留；園方公布正式名後再依轉正流程 rename。
- 配合本次來源，`tools/build_db.py` 新增 `OFFICIAL_X_ACCOUNTS`（見下一筆），兩隻的 `has_official_source` 由 false 轉 true、網站來源區塊開始顯示官方 X 連結。

## [2026-07-27] update | 多摩出生的雙胞胎 `fujimaru`／`ranmaru` 補上漢字名（藤丸・蘭丸）

**來源**：
- 維護者提供（2026-07-27）——漢字名依維護者提報
- https://www.tokyo-zoo.net/topic/topics_detail?kind=news&inst=tama&link_num=27678 — 多摩動物公園 2022-11-09 公開公告（官方僅以片假名「フジマル」「ランマル」表記，未載漢字）
- https://www.hamazoo.net/breeder_log.php?eid=02866 — 浜松市動物園 2025-04-06 飼育員日記（同樣只用「ランマル」）

**更新條目**：
- `fujimaru-2022-07-27.md` — `japanese: フジマル` → `藤丸 / フジマル`；標題同步改為 `Fujimaru（藤丸 / フジマル）`
- `ranmaru-2022-07-27.md` — `japanese: ランマル` → `蘭丸 / ランマル`；標題同步改為 `Ranmaru（蘭丸 / ランマル）`

**備注**：
- **漢字用字校訂**：維護者原提報 `福丸`，經查讀音不合——「福」音讀ふく（Fukumaru），無法讀作フジマル；フジ 對應的是「藤」。且雙胞胎命名為植物對句（藤／蘭），與母親 `himawari`（向日葵）成套，故採 `藤丸`。經維護者確認後採用。
- 漢字字形已確認為日中共用字碼（藤 U+85E4、蘭 U+862D、丸 U+4E38），非簡化字，無需另作日本字形轉寫。
- 兩園官方公告一律只用片假名，漢字無官方佐證；依「命名以維護者提供為準」原則收錄，不另標待查證。今日為兩隻 4 歲生日。

## [2026-07-27] update | X（Twitter）園方官方帳號列為官方來源：`tools/build_db.py` 新增 `OFFICIAL_X_ACCOUNTS`

**更新條目**：
- `tools/build_db.py` — 比照既有 `OFFICIAL_FB_PAGES` 機制，新增 `OFFICIAL_X_ACCOUNTS` 白名單與 `_X_HOSTS`（`x.com`／`twitter.com`／`mobile.*`）；`is_official_source()` 對 X 網域改比對路徑第一段 handle。首批登記四個園方帳號：`nishiyama_zoo`（鯖江市西山動物園）、`nhdzoo`（静岡市立日本平動物園）、`ichikawa_zoo`（市川市動植物園）、`kumamotocityzoo`（熊本市動植物園）

**受影響條目（來源區塊由不顯示轉為顯示官方 X 連結）**：
- `apple-seed-1-kanoko-2026-06-26.md`、`apple-seed-2-kanoko-2026-06-26.md`、`apple-seed-shin-fa-2026-05-27.md` — `has_official_source` false → true（此三筆原本只有 X 來源，網站顯示「未經官方佐證」）
- `gao-gao-2015-06-27.md`、`shou-shou-2017-07-15.md`、`meito-2013-06-20.md`、`rifa-2013-06-20.md` — 原已有官網／自治體來源，本次額外顯示園方 X 連結

**備注**：
- 理由：X 為多數日本園的主要公告管道，出生・命名・雌雄鑑定・訃報常只發在 X、官網不另發稿。整域白名單不可行（粉絲與個人帳號同域），故沿用 Facebook 的「逐帳號登記」做法。
- **未列入**：`0yDeN464cBT145p`（`ichiro-2014-07-06` 的來源）為個人帳號、非園方，維持非官方（已驗證 `is_official_source` 回 false）。
- 日後新增園方 X 帳號：把小寫 handle 補進 `OFFICIAL_X_ACCOUNTS` 即自動生效；請勿加入粉絲／個人拍攝帳號。

## [2026-07-27] add | 南京市紅山森林動物園 10 隻檔案卡（思思・小美・豆豆・招財・花臉・小仙・牙牙・臉臉・球球・胖胖）

**來源**：
- 維護者提供（2026-07-27）：南京市紅山森林動物園個體名單與性別；思思・小美・豆豆・招財 4 隻為 2025 年轉入，其餘 6 隻最後確認 2026-06 在園

**新增條目**：
- `si-si-nanjing.md` — 思思 Si Si（♀），2025 年轉入紅山，原園不詳
- `xiao-mei-nanjing.md` — 小美 Xiao Mei（♀），2025 年轉入紅山，原園不詳
- `dou-dou-nanjing.md` — 豆豆 Dou Dou（♂），2025 年轉入紅山，原園不詳
- `zhao-cai-nanjing.md` — 招財／招财 Zhao Cai（♂），2025 年轉入紅山，原園不詳
- `hua-lian-nanjing.md` — 花臉／花脸 Hua Lian（♂），現居紅山，最後確認 2026-06
- `xiao-xian-nanjing.md` — 小仙 Xiao Xian（♀），現居紅山，最後確認 2026-06
- `ya-ya-nanjing.md` — 牙牙 Ya Ya（♀），現居紅山，最後確認 2026-06
- `lian-lian-nanjing.md` — 臉臉／脸脸 Lian Lian（♀），現居紅山，最後確認 2026-06
- `qiu-qiu-nanjing.md` — 球球 Qiu Qiu（♂），現居紅山，最後確認 2026-06
- `pang-pang-nanjing.md` — 胖胖 Pang Pang（♀），現居紅山，最後確認 2026-06

**更新條目**：
- `index.md` — 「海外個體（中國・南京市紅山森林動物園）」分類新增 10 列（該園條目 13 → 23 隻）；條目總數 749 → 759
- `dou-dou.md`、`dou-dou-chengdu.md` — 補 ⚠️ 同名提示（互指含南京豆豆）
- `qiu-qiu-chengdu.md` — 補 ⚠️ 同名提示（南京球球）
- `pang-pang-qingyuan.md` — 補 ⚠️ 同名提示（南京胖胖、西山 胖胖／パンパン）

**備注**：
- 依「資料有限個體：檔案卡」規則建檔：名字＋性別已知、綁定已登記園（南京市紅山森林動物園）、佐證為維護者親自確認，三項門檻皆符合。全數 `limited-profile`，`sources` 記 `維護者提供（2026-07-27）`；無官方來源，`has_official_source` 自動為 false，網站顯示「維護者提供・未經官方佐證」標記。
- **在世軸**：10 隻皆經維護者確認在世（4 隻 2025 轉入、6 隻 2026-06 確認），距今未滿兩年，**一律不掛 `unverified`**。
- **起始年**：4 隻轉入者**確知抵達年 2025**，故 `zoos:` 填 `(2025 – 現在)`（居住史顯示「2025 – 現在」、不標 🐣）；其餘 6 隻不知入園年，依規則起始留空 `( – 現在)`（顯示「? – 現在」，首站 🐣 為既有可接受副作用）。
- 全數無生日，slug 依規則用園簡稱式 `名字-nanjing`；查得生日後改回 `名字-生日` 並同步修正 wikilink。
- 家系一律留「不詳（園方未公布）」，未從 RPF/lineage 腦補；轉入前所在園不詳，`zoos:` 只登紅山一站。
- 中文名繁簡並列：招財／招财、花臉／花脸、臉臉／脸脸（`chinese` 存繁體單值）；其餘同形不重複。

---

## [2026-07-27] add | `ko-ko-1990-06-26`（興興）與 `shin-shin-1988-07-13`（真真）— 桃太郎／金太郎之父母

維護者追溯 `momotaro-1997-07-17`（桃太郎）・`kintarou-1997-07-17`（金太郎）家系，補建雙親兩條目。父 `興興`（讀音 ココ／Ko-Ko，RPF #849）1990-06-26 生於神戸市立王子動物園、1992-02-19 移居姫路セントラルパーク、2007-10-25 歿；為 `yuyu-1986-07-05`（遊遊）× 王子之子，與泰泰（Tai Tai）雙胞胎。母 `真真`（シンシン，RPF #852）1988-07-13 生於広島市安佐動物公園、1992-11-06 移居姫路、2003-06-15 歿；與雙胞胎姉妹 Mu-Mu 同胎，父母為安佐的 ユウユウ × アイアイ。二者育三子（桃太郎・金太郎・健太 1998），因母真真育児放棄，兄弟由園方人工哺育。生日・居住史・歿日以 RPF 為據；父母家系與育児放棄由維護者提供。`真真` 與既有 `shin-shin-1986`（雄・市川市）等為不同個體，雙向補同名提示；`興興` 讀音 ココ、與 `kou-kou-1997-06-20`（光々・コウコウ）非同一，補混淆提示。

**來源**：
- https://redpandafinder.com/#profile/849 （興興／Ko-Ko）
- https://redpandafinder.com/#profile/852 （真真／Shin-Shin）
- 維護者提供（2026-07-27）：父母家系（祖父母・雙胞胎）、真真育児放棄→人工哺育

**新增條目**：
- `ko-ko-1990-06-26.md` — 興興 Ko-Ko（♂，RPF #849），生於 1990-06-26 神戸市立王子動物園，歿於 2007-10-25，終居 姫路セントラルパーク
- `shin-shin-1988-07-13.md` — 真真 Shin-Shin（♀，RPF #852），生於 1988-07-13 広島市安佐動物公園，歿於 2003-06-15，終居 姫路セントラルパーク

**更新條目**：
- `momotaro-1997-07-17.md`、`kintarou-1997-07-17.md` — 父母純文字改雙向 wikilink（`ko-ko-1990-06-26`／`shin-shin-1988-07-13`）；補人工哺育備注、Kenta 改記為弟
- `yuyu-1986-07-05.md` — 子女「姫路セントラル興興」改連結 `[[ko-ko-1990-06-26]]`
- `shin-shin-1986.md` — 同名提示補列 `shin-shin-1988-07-13`（真真）
- `index.md` — 新增 `ko-ko-1990-06-26`、`shin-shin-1988-07-13` 兩列；條目總數 759 → 761

---

## [2026-07-28] add | `kenta-1998`（健太）— 桃太郎／金太郎之弟

維護者追溯桃太郎家系，補建三兄弟中最小的 `健太`（讀音 ケンタ／Kenta，RPF #851）。為 `ko-ko-1990-06-26`（興興）× `shin-shin-1988-07-13`（真真）之子，比雙胞胎兄 `momotaro-1997-07-17`（桃太郎）・`kintarou-1997-07-17`（金太郎）晚一年出生（1998），生於姫路セントラルパーク，因母真真育児放棄，與兩兄同由園方人工哺育。RPF #851 僅登錄名字與性別（♂），無生日・居住史・家系；生年 1998・家系・居住由維護者提供，與既有四份條目一致。以小熊貓壽命判斷 1998 年生者已歿（`died: "?"`＋`deceased` tag），惟確切生日・歿日・離開姫路的時間均無來源，內文標 `🚧 待查證`。

**來源**：
- https://redpandafinder.com/#profile/851 （健太／Kenta）
- 維護者提供（2026-07-28）：生年 1998、家系（興興 × 真真之子、桃太郎／金太郎之弟）、姫路セントラル居住、人工哺育

**新增條目**：
- `kenta-1998.md` — 健太 Kenta（♂，RPF #851），1998 年生於姫路セントラルパーク，已歿（歿日待查證）

**更新條目**：
- `momotaro-1997-07-17.md`、`kintarou-1997-07-17.md` — 弟 `kenta` 純文字改 `[[kenta-1998]]` 雙向 wikilink
- `ko-ko-1990-06-26.md`、`shin-shin-1988-07-13.md` — 子女表 Kenta 改連結 `[[kenta-1998]]`、備注改為已建條目
- `index.md` — 新增 `kenta-1998` 一列；條目總數 761 → 762

---

## [2026-07-28] add | `pam-1976-08-19`（パム）與 `ayumi-1991`（あゆみ）— 釧路市動物園早期兩代

維護者提供部落格「北のレッサーパンダ日記」一篇追查釧路市動物園小熊貓歷史的文章（起因為查 `cha-1997-07-27` 的父母），該文後半逐條轉載**釧路市發行的開園 40 週年記念誌《あゆみ》年表**。經核對，年表中可與釧路市動物園官網互相驗證的條目（コーアイ 2006-06 來園、シンゲン 2014-11 來園、メイメイ／剛 2012 年互換）全數相符，轉載可信度高，據此建兩條目。

**書誌查證**：《あゆみ：釧路市動物園40周年記念誌》，釧路市動物園編集發行，2016-03，71 頁，書誌注記「年表あり」，NDL 請求記號 RA12-M47（書誌ID 032594801），北海道立圖書館亦有藏（480.76／KU）。**未數位化、線上讀不到**，本次未取得原本核對。同系列另有 10／20／30／50 週年記念誌，其中 50 週年版（2026-03，84 頁，內含「50年のあゆみ」p.6–24）為最新官方年表，日後可用以覆核。

`pam-1976-08-19`（パム）為**純官方來源**條目：釧路市動物園官網〈繁殖賞に輝く動物たち〉載 1976-08-19 誕生♂♀各一、♀翌年 2-14 夭折、♂命名「パム」11 歲歿，此胎為**日本國內首次小熊貓繁殖成功**（獲繁殖賞），並明載為喜馬拉雅系（`fulgens`），與釧路現存個體（styani）非同一血系。官方未載確切歿日（僅「11歳で死亡」），故 `died: "?"`＋`deceased`，內文註明推算約 1987–1988 年。同胎♀從未命名，依幼逝寶寶收錄原則不另立條目，僅記於パム 內文。與既有 `pam-1997-06-26`（ズーラシア、コーアイ 之母）雙向補同名提示。

`ayumi-1991`（あゆみ）依記念誌年表建檔：1991 年生於釧路（該園睽違 15 年的繁殖）、與西山來的 `sabatarou-1992-06-22` 配對、一生產 6 仔、1998-02 歿。年表記生日為「1991 年 6 月」、部落格作者考證為 1991-07-27，兩說相左且無一手佐證，`born` 暫記 `1991`，查實後須 rename 為 `ayumi-1991-07-27`。年表未點名子女，故五名子女對應標 🚧 待查證；佐證有三：RPF #728／#729 皆記 1995-07-04 生於釧路（合年表「1995 年 7 月產 2 仔」）、`marimo` 原記母「無名 #727」與 #728／#729／#731／#732 連號、サバタロウ 1995-02-15 抵釧路至 1995-07-04 為 139 天（合妊娠期 114–145 天）。亞種比照配偶與子女記為 styani，惟釧路建群個體為 fulgens，血系是否混有 fulgens 無法確認，已於備注標明。

**來源**：
- https://www.city.kushiro.lg.jp/zoo/sougou_kodomo/1001634.html （釧路市動物園「繁殖賞に輝く動物たち」，官方；パム 全部資料）
- https://www.city.kushiro.lg.jp/zoo/shoukai/1001527/1001528/1001554.html （釧路市動物園「レッサーパンダ」，官方；用於交叉驗證年表）
- https://ndlsearch.ndl.go.jp/books/R100000002-I032594801 （NDL：40 週年記念誌書誌）
- https://ndlsearch.ndl.go.jp/books/R100000001-I01111100001562866 （NDL：50 週年記念誌書誌）
- https://kosaru323.blog.fc2.com/blog-entry-563.html （北のレッサーパンダ日記；記念誌年表轉載＋作者考證）

**新增條目**：
- `pam-1976-08-19.md` — パム Pam（♂，`fulgens`），1976-08-19 生於釧路市動物園，日本首例繁殖成功，得年 11 歲（歿日待查證）
- `ayumi-1991.md` — あゆみ Ayumi（♀），1991 年生於釧路市動物園，1998-02 歿，一生產 6 仔

**更新條目**：
- `cha-1997-07-27.md` — 母／父由「（未記名）」改 `[[ayumi-1991]]`／`[[sabatarou-1992-06-22]]`（標 🚧）；マリモ 純文字改 wikilink（原誤記未建檔）；補居住史待查證註（部落格記釧路與浜松間另有西山一站，未改 `zoos:`）與配偶金太郎；sources 補部落格
- `ikura-1996-07-09.md` — 同上補父母 wikilink（標 🚧）、マリモ 改 wikilink、sources 補部落格
- `marimo-1995-07-04.md` — 母「無名 #727」改 `[[ayumi-1991]]`（標 🚧）、補雙胞胎與兄弟姊妹列、sources 補部落格
- `tara-1995-07-04.md` — 母／父純文字改雙向 wikilink、マリモ 改 wikilink；刪除重複的 📝 出生註記
- `sabatarou-1992-06-22.md` — 補配偶 `[[ayumi-1991]]` 與五名子女表（標 🚧）、補抵園至產仔 139 天的時序佐證、sources 補部落格
- `index.md` — Ikura × Tan-Tan 一脈新增 `ayumi-1991`、`marimo-1995-07-04` 兩列並補上一代說明；其他（獨立）新增 `pam-1976-08-19`；條目總數 762 → 764

---

## [2026-07-28] add | `kuro-1997-07-27`（クロ）— チャ 的雙胞胎、釧路市動物園

補建 `cha-1997-07-27`（チャ）的雙胞胎姊妹 `クロ`，同時是 `ayumi-1991` × `sabatarou-1992-06-22` 五名可對應子女中最後一隻未建檔者。生日 1997-07-27、歿日 2004-09-28（享年 7 歲）由**維護者確認**，與部落格「北のレッサーパンダ日記」記載一致。クロ 是該胎手足中唯一終生留在出生園者（チャ→浜松、`tara-1995-07-04`→上野→墨西哥、`marimo-1995-07-04`→西山→姫路、`ikura-1996-07-09`→多摩→福岡）。

**兩項獨立交叉驗證**（非取自同一部落格，故有佐證力）：（一）配偶 `gou-2000-06-19`（剛）的既有條目依 RPF #348 記其 **2004-04-08 自アドベンチャーワールド 移入釧路市動物園**，與部落格「2004.4.8 迎剛為婿」完全一致；記念誌年表載 2012-03 剛 移往羽村，亦與剛的條目相符。（二）「クロ 未產仔」與官方紀錄相容——釧路市動物園官網顯示 `kokin-2017-06-28` 為該園近年首例出生，即 1997-07-27 クロ＆チャ 之後 20 年無誕生；若クロ 曾產仔則此空窗不成立。

名字與家系仍無官方佐證（40 週年記念誌年表未提及クロ，只記母獸あゆみ 共產 6 仔、未點名子女），父母欄續標 🚧。RPF 編號未填：同批連號 #727（推定あゆみ）／#728（タラ）／#729（マリモ）／#731（チャ）／#732（サバタロウ）皆已對應，**#730 尚無對應個體、位置上極可能即クロ**，惟未核對故從缺，僅記於備注。死因不明。

**來源**：
- 維護者提供（2026-07-28）：生日 1997-07-27、歿日 2004-09-28
- https://kosaru323.blog.fc2.com/blog-entry-563.html （北のレッサーパンダ日記；名字・居住・配對・未產仔）
- https://redpandafinder.com/#profile/348 （剛；2004-04-08 移入釧路，用於交叉驗證）
- https://www.city.kushiro.lg.jp/zoo/shoukai/1001527/1001528/1001554.html （釧路市動物園官方個體介紹；コキン 2017 年出生，用於交叉驗證）

**新增條目**：
- `kuro-1997-07-27.md` — クロ Kuro（♀），1997-07-27 生於釧路市動物園，2004-09-28 歿，終生留釧路

**更新條目**：
- `cha-1997-07-27.md` — 雙胞胎クロ 由純文字改 `[[kuro-1997-07-27]]`（引言與家族兩處）
- `ayumi-1991.md`、`sabatarou-1992-06-22.md` — 子女表クロ 改 wikilink、移除「未建檔」
- `ikura-1996-07-09.md`、`tara-1995-07-04.md`、`marimo-1995-07-04.md` — 兄弟姊妹列クロ 改 wikilink
- `gou-2000-06-19.md` — 補配對對象 `[[kuro-1997-07-27]]` 與來園緣由註記
- `index.md` — Ikura × Tan-Tan 一脈新增 `kuro-1997-07-27` 一列、`cha` 該列補雙胞胎；條目總數 764 → 765

---

## [2026-07-28] rename | `ayumi-1991` → `ayumi-1991-07-27`（あゆみ）— 生日經維護者確認

維護者確認 `あゆみ` 生日為 **1991-07-27**。原條目建檔時因記念誌年表記「1991 年 6 月」、部落格作者考證記 1991-07-27，兩說相左且皆無一手佐證，`born` 暫記為 `1991`、slug 為 `ayumi-1991`；今依維護者校訂定案，照 rename 流程改為完整生日 slug。**依資料來源原則，wiki 的維護者校訂優先於記念誌，40 週年記念誌年表「1991 年 6 月」該筆視為有誤**（該年表另一處「1991 年 6 月」與部落格作者的獨立考證亦不符，作者早已指出）。生卒推算得年由「1991–1998」精確為 6 歲。

同時修正 `ikura-1996-07-09` 家族區塊中一則 🚧 註記插在「兄弟姊妹」與「配偶」兩列之間、打斷項目清單的排版問題，移至清單末尾。

**來源**：
- 維護者提供（2026-07-28）：生日 1991-07-27

**重命名**：
- `ayumi-1991.md` → `ayumi-1991-07-27.md`；frontmatter `born` 改 1991-07-27、`zoos:` 起訖改 `(1991-07-27 – 1998-02)`、`sources` 增列維護者提供；引言補歿齡；備注「🚧 生日待查證」改為「✅ 生日經維護者確認」並註明與記念誌之出入

**更新條目**（`[[ayumi-1991]]` → `[[ayumi-1991-07-27]]`，共 7 檔）：
- `cha-1997-07-27.md`、`kuro-1997-07-27.md`、`tara-1995-07-04.md`、`marimo-1995-07-04.md`、`ikura-1996-07-09.md`、`sabatarou-1992-06-22.md`、`index.md`
- `index.md` — 另移除誤植重複的 `kuro-1997-07-27` 列（保留 `cha` 之後那一列）；條目總數不變（765）

---

## [2026-07-28] add | `hajime-1991-07-27`（ハジメ）— あゆみ 的雙胞胎兄，官方訃報佐證

維護者提供鹿児島市平川動物公園「飼育員の日記」2011 年訃報全文（原連結 404，經 Internet Archive 2022-07-02 快照取得），據此建檔。**這是本批釧路早期個體中，除パム 之外第二筆有園方一手官方來源的條目。**

訃報明載：ハジメ（♂）**1991 年 7 月 27 日生於北海道釧路市動物園**、**1994 年 1 月來到平川動物公園**、**2011 年 4 月 23 日（六）中午因老衰死亡**，享年「19 才 8 ヶ月と 23 日」。文中稱他是「平川動物公園小熊貓的門面」，性格親人討喜，一生無大病大傷，晚年仍能奔跑，愛吃竹葉・蘋果・香蕉；標題為「大往生でした！」。

**連帶確立三件事**：

1. **記念誌年表「1991 年 6 月」確為誤記**。平川訃報是針對個體本身的園方一手紀錄，且與 40 週年記念誌年表另一筆「1994 年 1 月 釧路出生的雄性出借平川」完全吻合（可確認該筆即指ハジメ）。依「官方來源衝突以園方資料為準」，1991 年那胎的生日採 **1991-07-27**；愛好者部落格「北のレッサーパンダ日記」作者先前對此年表的更正意見，至此獲官方證實。
2. **`ayumi-1991-07-27` 的生日取得官方佐證**。原僅有維護者確認＋部落格考證；ハジメ 與あゆみ 同為記念誌所記 1991 年那胎的「2 頭」，故同日出生，あゆみ 的 1991-07-27 由其雙胞胎兄的官方訃報間接佐證。兩者互記為雙胞胎。
3. **`tools/build_db.py` 的 `OFFICIAL_HOSTS` 新增 `hirakawazoo.jp`**（含園方 staff blog「飼育員の日記」）。`data/zoos.json` 早已將該網域登記為鹿児島市平川動物公園官網，依 build_db 內註記「日後新增園方官網時，把 host 補進 OFFICIAL_HOSTS 即會自動顯示」補登。既有的 `fuumi-2007-07-11`、`shun-pei-2011-07-04`、`melody-2017-07-06` 等平川個體日後補園方連結時亦自動生效。

`sources` 同時保留原始官方網址（正確標示出處）與 Internet Archive 快照網址（供查核；依 2026-07-07 政策，web.archive 不列入個體頁的官方來源顯示）。訃報所記享年「19 才 8 ヶ月と 23 日」以生歿日精算應為 19 年 8 個月 27 日，疑為園方將歿日日數誤植為日齡尾數，年月無誤，條目採「得年 19 歲 8 個月」並於備注說明。父母仍不詳（釧路未公布 1991 年那胎雙親）。

**來源**：
- https://hirakawazoo.jp/zooblog/breeding/1063 （平川動物公園「飼育員の日記」訃報，官方；原連結已 404）
- http://web.archive.org/web/20220702181434/https://hirakawazoo.jp/zooblog/breeding/1063 （同上，Internet Archive 2022-07-02 快照）
- https://kosaru323.blog.fc2.com/blog-entry-563.html （北のレッサーパンダ日記；名字與釧路端脈絡）

**新增條目**：
- `hajime-1991-07-27.md` — ハジメ Hajime（♂），1991-07-27 生於釧路市動物園，1994-01 移入鹿児島市平川動物公園，2011-04-23 老衰而歿

**更新條目**：
- `ayumi-1991-07-27.md` — 「同胎手足はじめ（未建檔）」改為雙胞胎 `[[hajime-1991-07-27]]`；引言補雙胞胎；生日備注由「維護者確認」升級為「已有官方佐證」，並明記記念誌該筆為誤；`sources` 增列平川訃報與快照網址
- `index.md` — 新增 `hajime-1991-07-27` 一列、`ayumi` 該列補雙胞胎；條目總數 765 → 766
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `hirakawazoo.jp`

---

## [2026-07-28] update | `apple-seed-shin-fa-2026-05-27` — 園方公告性別為雌，補官方 IG 照片

熊本市動植物園官方 Instagram（@kumamoto_doushokubutsuen）2026-07-28 貼文公告：5 月 27 日出生的 `shin-fa` 之仔**性別確定為メス（雌）**，並公布滿兩個月體重 1670 克。依「官方來源可直接採用」原則回補 `sex: female` 與 `female` tag，佔位提示移除「性別待確認」（尚未命名，`apple-seed` tag 續留）。該貼文同時公告 8/1–8/16 命名投票，本次未寫入條目，待正式命名後照轉正流程處理。

**工具**：`tools/build_db.py` 比照既有 X／FB 白名單新增 `OFFICIAL_IG_ACCOUNTS`（含 `_IG_HOSTS` 判定），登記 `kumamoto_doushokubutsuen`；**僅認含帳號的完整形式** `/帳號/p/XXXX/`，IG「複製連結」的短形式 `/p/XXXX/` 無從判斷發文者、一律非官方。日後其他園方官方 IG 帳號補進名單即自動於個體頁來源區塊顯示。

**來源**：
- https://www.instagram.com/kumamoto_doushokubutsuen/p/DbUkQpSCR13/ （熊本市動植物園官方 IG，性別公告，官方）

**更新條目**：
- `apple-seed-shin-fa-2026-05-27.md` — `sex: female`、tags 加 `female`；新增 `instagram:` 官方貼文（2026-07-28）；`sources` 增列該貼文；引言補 ♀、性別公告與體重，「第二子／弟妹／外孫」改「次女／妹妹／外孫女」；移除「RPF 尚未建檔、rpf_id 待補」贅述
- `index.md` — 該列性別 ？ → ♀、說明改「次女」；條目總數不變（766）
- `tools/build_db.py` — 新增 `OFFICIAL_IG_ACCOUNTS` 官方 IG 帳號白名單

---

## [2026-07-28] add | 神戸市立王子動物園 早期繁殖群 — 依園報《はばたき》第 23・29 號建 4 條目，`ko-ko-1990-06-26` 改名 `shin-shin-1990-06-26`

維護者提供王子動物園園報《はばたき》PDF（園方官網，官方來源）。第 29 號（平成 3＝1991-03-20 發行）pp.5–6〈動物育児日記：レッサーパンダの人工哺育〉附「表1 レッサーパンダの系図」，第 23 號 pp.5–6〈動物育児日記：レッサーパンダの子育て〉記該園首次繁殖全程。兩篇合起來把王子動物園 1987–1990 的繁殖群補齊，並解決三處既有疑點。

**表1（第 29 號）內容**：洋洋♀ × 王子♂ → 1987-07-03（表）1 頭 ♀「無名」，1988-02-05 轉出京都市動物園；王子♂ × 遊遊♀ → 1989-06-03 1 頭 ♀ 元元、1990-06-03（表）2 頭 ♂ 興興・♂ 泰泰，皆「現在飼育中」。

**三處判定**：

1. **興興讀音 ココ → シンシン**。表1 明載「興興（シンシン）」，與同胎「泰泰（タイタイ）」、母「遊遊（ユウユウ）」、姉「元元（ゲンゲン）」同為中文式讀音，內部一致；RPF #849 與姫路時期流通的 ココ／Ko-Ko 無官方佐證，降為 `english_variants`。依「園方讀音優先」原則改名。
2. **泰泰・興興生日 1990-06-26（非表中的 6 月 3 日）**。第 29 號內文日齡全部以 6/26 起算才成立（7/18＝22 日齡、7/21＝25 日齡、9/18＝84 日齡、12/4＝161 日齡、12/17＝174 日齡），RPF #849／#850 亦記 6/26；表中「6 月 3 日」判為與上一列元元重複之誤植。
3. **洋洋之女並非無名，也不是 7 月 3 日生**。第 23 號記 1987-07-07 早晨產仔並以此起算日數，王子官方追悼頁（洋洋）亦記 07-07，故採 1987-07-07（二比一）；該女 1988-02-05 前往母親出生地京都市動物園，**在京都獲名「優優」**。原 `yan-yan-1985-05-31` 子女欄「名字不詳・未建檔」得以轉正。

**來源**：
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki29.pdf （神戸市立王子動物園《はばたき》第 29 號，1991-03-20，pp.5–6，官方）
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki23.pdf （同上第 23 號，pp.5–6，官方）
- https://redpandafinder.com/#profile/850 （泰泰；釧路移居日與歿日）
- http://ojizoo.jp/html/oj-07-166.htm （王子動物園 洋洋 追悼頁，官方）

**新增條目**：
- `ouji-kobe.md` — 王子 オウジ（♂），園內種雄；生日・出身・歿日皆不詳（`birth_zoo: unknown`、`unverified`、`last_seen: 1990-06`），slug 暫用城市後綴
- `yuu-yuu-1987-07-07.md` — 優優 ユウユウ（♀），1987-07-07 王子動物園生（該園首例繁殖成功），1988-02-05 移京都市動物園並在京都獲名；其後動向不明（`unverified`、`last_seen: 1988-02`）
- `gen-gen-1989-06-03.md` — 元元 ゲンゲン（♀），1989-06-03 王子動物園生；1991-03 記「現在飼育中」，其後動向不明（`unverified`、`last_seen: 1991-03`）
- `tai-tai-1990-06-26.md` — 泰泰 タイタイ（♂，RPF #850），1990-06-26 王子動物園生、1991-05-28 移釧路市動物園、1999-03-27 歿；**王子動物園首例小熊貓人工哺育個體**（皮膚炎，25 日齡離母入院、161 日齡命名、174 日齡回舍與姉元元同居）

**更新條目**：
- `ko-ko-1990-06-26.md` → `shin-shin-1990-06-26.md` — rename；`name` Ko-Ko → Shin-Shin、`japanese` 興興, シンシン、舊拼音移入 `english_variants`；父母／雙胞胎／姉改 wikilink，家系由「維護者提供」升級為官方佐證；`sources` 增列第 29 號
- `yuyu-1986-07-05.md` — 配偶「王子王子（無條目）」改連結 `ouji-kobe`；子女純文字改子女表（元元・興興・泰泰），註明依表1
- `yan-yan-1985-05-31.md` — 子女「名字不詳・未建檔」改連結 `yuu-yuu-1987-07-07`；補配偶連結 `ouji-kobe`、首次繁殖成功段落；`sources` 增列第 23・29 號
- `shin-shin-1988-07-13.md` — 同名提示補「配偶興興羅馬拼音亦為 Shin-Shin」
- `momotaro-1997-07-17.md`・`kintarou-1997-07-17.md`・`kenta-1998.md` — wikilink 隨改名更新
- `index.md` — 王子動物園早期個體區新增 `ouji-kobe`・`yuu-yuu-1987-07-07`・`gen-gen-1989-06-03`；姫路區新增 `tai-tai-1990-06-26`、興興該列改寫；條目總數 766 → 770

---

## [2026-07-28] update | 王子早期三隻改標已歿 — `unverified` 誤用改為 `died`；`yuu-yuu-1987-07-07` 歿年 1988

同日建的 `ouji-kobe`（王子）、`yuu-yuu-1987-07-07`（優優）、`gen-gen-1989-06-03`（元元）原掛 `unverified` tag，網站因此顯示 🚧 存疑徽章、並把三隻排除在現存數與統計外。掛 tag 的動機是壓掉「居住史訖日留空 → 渲染成 現在 🏡」造成的在世假象，但 `unverified` 的語意是「動向不明、可能還在世」，用在 1980 年代個體上是誤用。

改依 repo 既有的「確定已歿、歿日不詳」慣例（同 `koro`／`mimi`／`bou-bou`／`sai-sai`／`kei`／`miya`／`atsuko-1978`／`tara-1995-07-04`）：移除 `unverified`、改掛 `deceased` 並填 `died`。`died` 一存在，`gen_residence` 即自動不標 🏡 現居、網站也不再算入在世統計，效果與原意相同且語意正確。

優優的歿年由維護者提供：**1988 年**——抵京都市動物園（1988-02-05）同年即過世，故未留下繁殖紀錄。依「幼逝寶寶收錄原則」（2026-07-14），幼齡夭折但已有正式命名者照常收錄上站，維持現狀不移 `_hidden`（得年僅知在 1988 年內、未滿 1 歲半）。

**來源**：
- 維護者提供（2026-07-28：優優歿年 1988）
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki23.pdf （神戸市立王子動物園《はばたき》第 23 號，官方；優優 1988-02-05 轉出京都）

**更新條目**：
- `yuu-yuu-1987-07-07.md` — `died: 1988`、移除 `last_seen`、tags `unverified` → `deceased`；`zoos:` 京都段訖填 1988；標題與引言補 🪽、改「終居：京都市動物園」，待查證段改為歿年說明
- `gen-gen-1989-06-03.md` — `died: "?"`、tags `unverified` → `deceased`（`last_seen: 1991-03` 保留為最後確認在世時點）；標題引言補 🪽
- `ouji-kobe.md` — `died: "?"`、tags `unverified` → `deceased`（`last_seen: 1990-06` 保留）；標題引言補 🪽
- 全 wiki 指向此三隻的 wikilink 補 🪽（洋洋・遊遊・興興・泰泰・元元・優優・王子各條目與 `index.md`）
- `index.md` — 三列生卒欄改 `1987–1988 🪽`／`1989–? 🪽`／`?–? 🪽`；條目總數不變（770）

---

## [2026-07-28] add | 安佐動物公園 重慶來源始祖：`yuu-yuu-1983`（友友）・`ai-ai-1984`（愛愛）

`shin-shin-1988-07-13`（真真）長期以純文字記錄的父母 ユウユウ／アイアイ 正式建檔。兩隻於 1987-07-12 由廣島市友好都市・中國重慶市以配對形式贈與広島市安佐動物公園（維護者提供來園日與贈與經緯），是該園小熊貓飼育的起點。

安佐動物公園 2004-02-16 發表（四国新聞同日報導，照片由該園提供）載明：雌「愛愛」於 2004-02-13 以 19 歲老衰過世，為當時**日本最高齡小熊貓**，園方認為亦可能是世界最高齡；1987 年來園時 3 歲；產下並育成的 14 隻子女分佈全國各動物園、孫輩亦已誕生；2 月 12 日中午前後起無法站立，經點滴治療後翌日過午離世。同發表亦提及雄「友友」已於**前一年（2003）年末以 20 歲**過世，其後愛愛才成為最高齡。

生年由園方陳述回推（友友 1983、愛愛 1984，皆標推定；愛愛另有「1987 年時 3 歲」一項可交叉印證），精確生日與友友歿日仍 🚧 待查證；出生地為重慶市贈與、實際設施不明，故 `birth_zoo: unknown`。14 隻子女目前僅確認真真與其雙胞胎手足 Mu-Mu（沐々，無條目）。

安佐動物公園飼育記録集第 17 卷（1990）茶村真一郎〈レッサーパンダの来園から出産までの飼育経過〉（J-STAGE，DOI 10.69229/asazoo.17.0_47）為記載本對來園至首次繁殖的官方一手文獻，惟該 PDF 為 CCITT G4 掃描、**無文字層**，本次未能判讀，故未列入 `sources`；日後取得判讀本可據以補齊生日、家系與 14 子名單。

**來源**：
- https://www.shikoku-np.co.jp/national/life_topic/print.aspx?id=20040216000496 （四国新聞 2004-02-16「最高齢レッサーパンダ死ぬ／昨年末の雄に続き雌も」；報導安佐動物公園官方發表）
- 維護者提供（2026-07-28：1987-07-12 來園、中國重慶市友好都市贈與一對）

**新增條目**：
- `yuu-yuu-1983.md` — 友友 ユウユウ（♂），生年 1983 推定，1987-07-12 來園安佐，2003 年末歿（20 歲）；真真之父
- `ai-ai-1984.md` — 愛愛 アイアイ（♀），生年 1984 推定，1987-07-12 來園安佐，2004-02-13 歿（19 歲・老衰）；歿時日本最高齡、育成 14 子

**更新條目**：
- `shin-shin-1988-07-13.md` — 父母由純文字 ユウユウ／アイアイ 改 wikilink；引言補來園經緯，ℹ️ 註更新（`メイメイ` 一說改標 🚧 待確認）
- `ai-1991-06-20.md` — 補 🚧 註：登錄名「愛愛２」疑承襲 `ai-ai-1984`，若確為安佐生則可能是愛愛×友友之女（僅列線索，出生地本身存疑）
- `index.md` — 新增「安佐動物公園 重慶來源始祖（廣島）」區塊兩列；真真該列補父母連結；條目總數 770 → 772

---

## [2026-07-28] update | 安佐 1987 重慶來園實為 3 隻：新增 `mei-mei-hiroshima`（明明）；依官方年報／記録集更正三隻生日

維護者提供《安佐動物公園飼育記録集》第 17 卷（1990）茶村真一郎〈レッサーパンダの来園から出産までの飼育経過〉（J-STAGE，DOI 10.69229/asazoo.17.0_47；PDF 為無文字層掃描，本次由維護者下載後逐頁判讀）。園方一手記載改寫了三件事：

**1. 1987 年由重慶來園的是 3 隻、不是 1 對。** 「1987年7月12日に中国の重慶市からオス1メス2、計3頭のレッサーパンダが来園した。名前はオスは友友、メスは愛愛、明明と名づけられた。」——除友友・愛愛外還有雌性**明明（メイメイ）**，故新建條目。明明來園時 5.3／5.0／4.3 kg 中最輕（4.3 kg），竹葉採食量三隻中最少，常見體況不佳與眼屎，園方給牠較多水果；月平均體重仍穩定增加，1988-06 達 6 kg。第 17 卷僅涵蓋 1987-07～1988-07，其後動向與歿日不明；因係 1980 年代來園成獸、確定已不在世，依既有慣例填 `died: "?"` + `deceased` 並記 `last_seen: 1988-07`（**不掛** `unverified`）。生日不詳，slug 依 `ouji-kobe` 慣例用城市後綴。

順帶解掉一個懸案：真真條目長年記載的「友友亦與 メイメイ 交配」（維護者提供），所指應即本個體，而非仙台八木山那隻 `mei-mei-1989-06-19`（美美，父母記為「中国友友×中国好好」）；惟第 17 卷未載明明的繁殖，仍標 🚧 待查證。

**2. 真真生日 1988-07-13 → 1988-07-14（rename）。** 第 17 卷於摘要（「翌年の1988年7月14日に愛愛が2頭の子供を出産した」）與「まとめ」第 2 項（「7月14日にメスの子2頭を出産した」）兩處一致記為 **7 月 14 日**，且明載該胎 **2 隻皆為雌性**（即真真與 Mu-Mu／沐々）。原值 07-13 來自 RPF #852；依 CLAUDE.md「官方／園方資料為準」改採官方，slug 同步更名 `shin-shin-1988-07-13` → `shin-shin-1988-07-14`。⚠️ 舊網址 /p/shin-shin-1988-07-13/ 將失效。

同卷另記繁殖細節：1988-02-06 與 02-24 兩度確認交尾、妊娠期間自最後交尾確認日起算 140 天、產前 36 天因陰部腫大與膣口張開而隔離至產室（設 50×40×35 cm 產箱 2 個＋80×60×35 cm 產箱 1 個）；愛愛臨產前體重 6.4 kg，友友穩定於 5.8 kg 前後。

**3. ブナ／ナラ 生日 2000-07-13 → 2000-07-17、移動日各提前一天（rename）。** 広島市安佐動物公園年報 平成 22 年度「ブリーディングローン動物一覧（貸し出している動物）」記 **ブナ 2000/07/17**（貸出 江戸川区自然動物園、動物移動日 **2001/11/08**）、**ナラ 2000/07/17**（貸出 静岡市立日本平動物園、動物移動日 **2001/12/17**）。原值（生日 07-13、移動日 11-09／12-17→12-18）來自 RPF #336／#49，依官方優先改採官方；兩者為同胎雙胞胎，一併更正故 `check_twins` 仍一致。slug 更名 `buna-2000-07-13` → `buna-2000-07-17`、`nara-2000-07-13` → `nara-2000-07-17`。⚠️ 舊網址失效。（同胎名單另有 2000-07-13 的 `kashi-2000-07-13`／`shii-2000-07-13`，母為麻衣、屬**不同一胎**，不受影響。）

**工具**：`tools/build_db.py` 的 `is_official_source` 既有 `.go.jp` 政府網域 pattern 已使 J-STAGE 上的《安佐動物公園飼育記録集》自動判為官方園報（符合 CLAUDE.md「園報視為官方」），故**無需新增判定**；僅補註解說明此事與其副作用（J-STAGE 上非園方編輯的學術論文也會被判官方，日後若要收緊可改為只認 `/article/asazoo/` 等園方刊物路徑）。

**來源**：
- https://www.jstage.jst.go.jp/article/asazoo/17/0/17_47/_article/-char/ja （安佐動物公園飼育記録集 17:47-53, 1990-03，茶村真一郎，官方園報）
- http://www.asazoo.jp/pdf/asazoo/h22_annual_repo04.pdf （広島市安佐動物公園年報 平成22年度，官方）
- https://www.shikoku-np.co.jp/national/life_topic/print.aspx?id=20040216000496 （四国新聞 2004-02-16，報導安佐動物公園發表）

**新增條目**：
- `mei-mei-hiroshima.md` — 明明 メイメイ（♀），1987-07-12 與友友・愛愛同批由重慶來園；生日不詳、`died: "?"`、`last_seen: 1988-07`

**更新條目**：
- `shin-shin-1988-07-13.md` → `shin-shin-1988-07-14.md` — rename；`born` 與 `zoos:` 安佐段起日改 07-14，引言補「該胎 2 隻皆為雌性」，ℹ️ 註記更正緣由，`sources` 增列第 17 卷；`メイメイ` 一說改指向 `mei-mei-hiroshima`
- `buna-2000-07-13.md` → `buna-2000-07-17.md` — rename；`born` 07-17、安佐→江戸川移動日 2001-11-08，補更正註記，`sources` 增列平成22年度年報
- `nara-2000-07-13.md` → `nara-2000-07-17.md` — rename；`born` 07-17、安佐→日本平移動日 2001-12-17（並補記為繁殖借出），補更正註記，`sources` 增列平成22年度年報
- `yuu-yuu-1983.md`・`ai-ai-1984.md` — 改寫為「3 隻來園」，補交尾日・妊娠期間・體重・產室設置等第 17 卷細節，`sources` 增列第 17 卷，親屬連結補 `mei-mei-hiroshima`
- 全 wiki 指向三個舊 slug 的 `[[wikilink]]` 同步更名（含 `index.md`）
- `tools/build_db.py` — `is_official_source` 政府網域 pattern 補註解（無行為變更）
- `index.md` — 安佐始祖區塊改「雄1雌2共3隻」並新增 `mei-mei-hiroshima` 一列；條目總數 772 → 773
- `buna-2000-07-17.md`・`nara-2000-07-17.md` — 順手把 `## 家族` 的純文字父母／雙胞胎改 `[[wikilink]]`（母 `banana-1996-08-09`、父 `ron-ron-1995-06-30`、彼此互為雙胞胎；nara 的「Banana 無條目」為過時說明），nara 子女表 Sea 改連 `sea-2010-07-19`

---

## [2026-07-29] add | 天王寺動物園 1990 年代繁殖對建檔：`pan-pan-1994-06-17`（パンパン）、`jen-jen-1992-08-07`（健健）；補上 `ten-ten-1997-07-03` 的父母

讀者回報（楊桃，圖鑑缺漏表單 2 筆）附天王寺動物園園報《なきごえ》官方頁，兩筆全部欄位皆有官方佐證，依「官方來源可直接採用」建檔。這兩隻正是 `ten-ten-1997-07-03`（天天）條目長年以純文字記錄、標明「暫無條目」的父母 Pan-Pan #592 與 Jen-Jen #547。

**官方佐證原文**：

- 2008 年 11 月號個體介紹「くらべてみようレッサーパンダ」：パンパン「1994年6月17日に長野市茶臼山動物園で生まれ、1996年12月13日に天王寺動物園に来ました」；健健（ジェンジェン）「1992年8月7日に岡山県の池田動物園で生まれ、1994年12月21日に天王寺動物園に来ました」
- 2014 年 4 月號「レッサーパンダあれこれ」：「今年の1月に19歳で雌のパンパンが老衰で亡くなったため」→ パンパン 性別 ♀、歿於 2014-01（僅到月）、死因老衰
- 2009 年 11 月號 ZOO DIARY 10 月 18 日條：「岡山市の池田動物園からお借りしていたレッサーパンダの雄の健健（ジェンジェン）が老衰で死亡しました」→ 健健 性別 ♂、歿日 2009-10-18、且為向池田動物園**繁殖借出（ブリーディングローン）**之個體、漢字名「健健」出自園報原文

**判定與待查證**：`pan-pan-1994-06-17` 的歿日官方僅記「1 月」，日期 31 日依 RPF #592（線索）暫填、標 🚧；其父母（Hoa-Hoa × Yuu-Yuu）與雙胞胎 Ton-Ton 亦僅見於 RPF／lineage，列純文字並標 🚧 待查證——其中「Yuu-Yuu」未必是 `yuu-yuu-1990-06-25`（該隻 1990 年生，無法為 1992 年出生的同胎手足之父），身分待釐清。`jen-jen-1992-08-07` 父母官方與 RPF 皆未載，記「不詳」。RPF #547／#592 兩筆的生日・居住史・歿日與官方完全一致，可互相佐證。

**來源**：
- https://www.tennojizoo.jp/nakigoe/2008/11/graph_zoo.html （天王寺動物園園報《なきごえ》2008-11，官方）
- https://www.tennojizoo.jp/nakigoe/2014/04/keep2.html （同上 2014-04，官方）
- https://www.tennojizoo.jp/nakigoe/2009/11/diary.html （同上 2009-11 ZOO DIARY，官方）
- https://redpandafinder.com/#profile/592 (パンパン)
- https://redpandafinder.com/#profile/547 (健健)

**新增條目**：
- `pan-pan-1994-06-17.md` — パンパン Pan-Pan（RPF #592），♀，1994-06-17 生於長野市茶臼山動物園、1996-12-13 來天王寺動物園、2014-01-31 歿（19 歲・老衰）；`ten-ten-1997-07-03` 之母
- `jen-jen-1992-08-07.md` — 健健 ジェンジェン Jen-Jen（RPF #547），♂，1992-08-07 生於池田動物園、1994-12-21 借出天王寺動物園、2009-10-18 歿（17 歲・老衰）；`mii-mii-1992-08-07` 的雙胞胎、`ten-ten-1997-07-03` 之父

**更新條目**：
- `ten-ten-1997-07-03.md` — 父母由純文字改 wikilink，移除「暫無條目」ℹ️ 註
- `mii-mii-1992-08-07.md` — 雙胞胎 Jen-Jen #547 由純文字改 wikilink（引言與 家族 兩處）
- `jen-jen-1995-07-06.md` — 同名提示改指向新條目 wikilink
- `pan-pan-1983.md` — 新增 ⚠️ 同名提示（1994 天王寺 パンパン、清遠／南京胖胖）
- `koko-2000-06-25.md` — ½ 兄弟姊妹列的 Pan-Pan（1994）與 Rin-Rin（1992）改 wikilink
- `rin-rin-1992-06-21.md` — 新增「全血緣兄弟姊妹」一行（含 `pan-pan-1994-06-17`）
- `index.md` — 新增「天王寺動物園 1990 年代繁殖對（大阪）」區塊兩列；最後更新 2026-07-29；條目總數 773 → 775
- `data/contributors.json` — 致謝名單 楊桃 的 note 追加本批回報
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `tennojizoo.jp`（天王寺動物園官網，含園報《なきごえ》與 ZOO DIARY）；否則兩隻的官方來源會被判為非官方、個體頁不顯示來源區塊且誤掛「未經官方佐證」標記

---

## [2026-07-29] fix | `ouji-kobe`（王子）補歿日 1990-07-15、居住史起訖與前一站天津動物園

讀者回報（楊桃，資料更正表單 2 筆，實為同一件事投兩次、第二次補園報連結）。原條目生日・出身・來園年・歿日全不詳，`died: "?"`＋`last_seen: 1990-06`；本次依王子動物園的**剥製展示解說牌**與**園報《はばたき》**更正。

**已採用（有官方佐證）**：

- **歿日 1990-07-15、王子園飼育期間 1983-02-22 – 1990-07-15** — 依王子動物園動物科學資料館的剥製展示解說牌（讀者 2014-05 實拍，2014 年企画展「おしりから見た動物たち」）：「レッサーパンダ Ailurus fulgens／愛称：王子／オス／飼育期間 1983.2.22 ～ 1990.7.15」。展牌屬園方展示物、性別 オス 與 wiki 現值一致；剥製由王子園製作展示，故飼育期間終日即歿日。連結已核（圖檔親驗）。
- **前一站＝天津動物園（起始年不明，訖 1983-02-22）** — 園報第 13（1983.2）・14（1983.7）號記神戸市友好都市・中國天津市贈與小熊貓一對，由天津市動物護送團（張煥亭團長、天津動物園長陳國斌等）空運、1983-02-22 抵園、2-26 贈呈式，第 14 號封面即該天津小熊貓照片。⚠️ 園報**未點名個體**，係「抵園日 = 展牌飼育期間起日」的推論，條目內已標 🚧 待查證；`birth_zoo` 仍維持 `unknown`（來源園未必是出生園）。同批來園的另一隻（雌）身分尚未查得。
- 天津動物園已在 `data/zoos.json`，無須新增註冊。

**回報出入（以來源為準）**：回報自由填答欄寫「1986-02-22 自天津動物園來到王子動物園」，與其自填的「生效日期 1983-02-22」及展牌矛盾；園報出版於 1983.2 亦排除 1986 → 採 **1983-02-22**。

**未處理的線索（非官方，不採用）**：同一篇 blog 的讀者留言記「ケンタ 1998～2011・姫セン」，`kenta-1998` 現為 `died: "?"`；モモタロウ（1997–2007）・キンタロウ（1997–）與 wiki 現值相符。留言非官方來源，`kenta-1998` 歿年待官方佐證再補。

**來源**：
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki13.pdf （王子動物園園報《はばたき》第 13 號，1983-02，官方）
- https://www.kobe-ojizoo.jp/habataki/pdf/habataki14.pdf （同上第 14 號，1983-07，官方）
- http://shinshin.cocolog-nifty.com/redpanda/2014/05/post-828b.html （剥製展示解說牌實拍，記入 `extra_sources`）

**更新條目**：
- `ouji-kobe.md` — `died: "?"` → `1990-07-15`；移除 `last_seen`；`zoos:` 改為 天津動物園 ( – 1983-02-22)＋神戸市立王子動物園 (1983-02-22 – 1990-07-15)；引言改寫歿日與來園、移除「最後確認」行；⚰️ 段落改寫並新增 🚧 來園經緯段；`sources` 增列第 13・14 號，新增 `extra_sources`（展牌實拍）
- `index.md` — 王子該列備注補來園日與歿日、期間欄 `?–?` → `?–1990`（條目總數不變，775）
- `data/contributors.json` — 致謝名單 楊桃 的 note 追加本批回報

---

## [2026-07-29] update | 維護者確認：`pan-pan-1994-06-17` 之父為 `yuu-yuu-1990-06-25`（勇勇）；勇勇日文名 ユーユー → ゆうゆう

**1. 日文名更正**：`yuu-yuu-1990-06-25`（勇勇）的假名依維護者提供改為 **ゆうゆう**（原記 ユーユー）。`japanese` 與標題兩處已改；`english_variants` 不變（Yuu-Yuu 拼音與 ゆうゆう 一致）。其餘寫作 ユーユー 的條目皆指西山的 `yuu-yuu-1987-05-31`，不受影響、未動。

**2. 父女關係確立**：維護者確認勇勇為 `pan-pan-1994-06-17`（パンパン）之父，改為 wikilink 並雙向補齊（勇勇頁新增「子女（母不詳）」小節）。時序相符：勇勇 1991-10-17 來茶臼山，パンパン 1994-06-17 生於該園。母仍記 Hoa-Hoa（RPF 線索）、🚧 待查證。

**3. 連帶推翻 RPF 的手足判定**：RPF #592 把茶臼山的 Run／Rin-Rin（1992）／Min-Min／Cha-Cha（1993）／Ton-Ton（1994）／Ron-Ron（1995）全列為パンパン的**全血緣**手足，但父既為 1990 年生、1991-10 才來園的勇勇，1992–1993 那幾隻時序不合，研判 RPF 把茶臼山數隻同名「Yuu-Yuu」混為一人。故昨日建檔時暫列的全血緣手足一律撤下、標 🚧 待查證；パンパン 改列父方勇勇一脈的 ½ 手足（母為 `liuxing-1997-06-16` 的 8 隻）。

**來源**：
- 維護者提供（2026-07-29）——日文假名與父女關係

**更新條目**：
- `yuu-yuu-1990-06-25.md` — `japanese` 改 `勇勇, ゆうゆう`、標題同步；引言與「子女（母不詳）」新小節補 `pan-pan-1994-06-17`
- `pan-pan-1994-06-17.md` — 父改 `[[yuu-yuu-1990-06-25]]` wikilink（維護者確認）、引言補父名；½ 手足改列勇勇一脈 8 隻；撤下 RPF 全血緣手足列並改為 🚧 說明
- `rin-rin-1992-06-21.md` — 撤下昨日誤加的「全血緣兄弟姊妹」行，改為 🚧 說明 RPF 同名混同之疑
- `index.md` — パンパン 該列補父名；勇勇 該列補 ゆうゆう 與 `pan-pan-1994-06-17`

---

## [2026-07-29] update | `pei-pei`（霈霈）歿於 2026-07-27 — 讀者實拍廣州動物園園內公告牌

讀者回報並附廣州動物園園內現場公告牌實拍，載霈霈於 **2026-07-27** 過世。展牌屬園方現場公告，依「資料有限個體：檔案卡」慣例記入 `extra_sources`（園方微信公眾號等官方管道尚未查得對應訃告，`sources` 維持無官方來源）。生年不詳故得年不明，死因未公布。

`zoos:` 訖日由現居改為 2026-07-27（起始年仍留空，渲染為「? – 2026-07-27」）；順帶把 `sources` 的「作者提供」改為「維護者提供」以符現行用語。

**來源**：
- 廣州動物園 園內現場公告牌（讀者 2026-07 實拍，回報附件）

**更新條目**：
- `pei-pei.md` — 新增 `died: 2026-07-27`；tags 加 `deceased`；`zoos:` 訖日改 2026-07-27；新增 `birth_zoo: unknown`（野生救護個體，廣州非出生園，居住史不再誤標 🐣）；新增 `extra_sources`（展牌實拍）；標題加 🪽、引言「現居」改「歿」、內文改過去式並新增 ⚰️ 段落；🚧 待查證追加死因與官方訃告
- `lang-lang-guangzhou.md`／`wei-wei-guangzhou.md`／`fei-fei.md`／`pi-pi-qingyuan.md` — 提及霈霈處的 wikilink 補 🪽
- `index.md` — 廣州該列備注補歿日、生年欄補 🪽（條目總數不變，775）

---

## [2026-07-29] update | 維護者確認 `pan-pan-1994-06-17` 之母名為「花花」；wiki 內三處 Hoa-Hoa 判定為同一隻並統一寫法

維護者確認 パンパン 之母名為 **花花**（Hoa-Hoa），但僅知名字——生日・居住史・歿日皆不明。依維護者裁定：**暫不建條目**（維持純文字，同 `yuu-yuu-1987-05-31` 頁對其母的既有做法），且 wiki 內三處記為「Hoa-Hoa」的母親**判定為同一隻花花**、寫法統一為「花花 Hoa-Hoa」。

**三處為**：`pan-pan-1994-06-17`（1994 茶臼山生，父 勇勇）、`rin-rin-1992-06-21`（1992 茶臼山生）、`yuu-yuu-1987-05-31`（1987 茶臼山生，父 I-I）。一隻母獸於 1987–1994 連續繁殖於茶臼山時序合理。

**連帶關係**：三隻因此互為**同母異父的 ½ 手足**，已在三頁互相補上「½ 兄弟姊妹（母方花花一脈）」並雙向 wikilink。也因此修正了前一筆 log 的判讀——RPF 把 1992–1995 那批列為 パンパン 的「全血緣」手足，實際上（若母皆為花花）只能是**同母異父的 ½**，而非全錯；仍不確定的是各自的父方「Yuu-Yuu」是哪隻。

**未採用 `siblings:` frontmatter**：該欄位在網站顯示為「未分血緣度的兄弟姊妹」，而此處明確是 ½，為免誤導僅記於內文；待花花本身建檔後，手足即可由共同母親自動推導。

**來源**：
- 維護者提供（2026-07-29）——母名「花花」、三處為同一隻之裁定

**更新條目**：
- `pan-pan-1994-06-17.md` — 母改「花花 Hoa-Hoa」；新增「½ 兄弟姊妹（母方花花一脈）」；ℹ️ 註改記母名為維護者確認、僅知名字故未建檔
- `rin-rin-1992-06-21.md` — 母改「花花 Hoa-Hoa」並註明同為另兩隻之母；新增母方 ½ 手足行；🚧 註改為「那批應為同母異父 ½ 而非全血緣」；½ 小節標題同步改寫
- `yuu-yuu-1987-05-31.md` — 引言與 母 欄改「花花 Hoa-Hoa」並註明同為另兩隻之母；新增母方 ½ 手足行
- `yuu-yuu-1990-06-25.md` — 子女表 パンパン 該列的母欄改記「花花 Hoa-Hoa（僅知名字、暫無條目）」

---

## [2026-07-29] add | 新增 `hoa-hoa-1982-06-15`（花花 ホアホア）——長野市茶臼山動物園始祖母、13 子女之母

維護者提供完整資料，取代同日前一筆「僅知名字、暫不建檔」的判定：**生日 1982-06-15、歿 2000-10-08、出生於中國河北省石家莊市動物園**（該園已在 `data/zoos.json` 註冊），並附 13 名子女名單。花花是茶臼山動物園小熊貓族群的始祖母，後代散布日本各地。

**RPF 獨立佐證**：RPF #761 的歿日（2000-10-08）與日文假名（ホアホア）與維護者資料**完全一致**；RPF 未載生日，故 1982-06-15 以維護者為準。

**與 RPF 的兩處分歧，一律以 wiki（維護者）為準**：

1. RPF 把花花記為「野生捕獲個體（中國）」，維護者記為石家莊市動物園出生 → 採維護者。
2. RPF 記 14 名子女、維護者名單 13 名（RPF 另有兩筆「(no name)」1987／1988，維護者名單僅一筆無明確對應）→ 差額標 🚧 待釐清。
3. 來園日 1985-03-19 僅見於 RPF（線索），暫填並標 🚧；石家莊 → 茶臼山之間是否經其他園亦未確認。

**子女對應**：13 隻中 3 隻已有條目——`yuu-yuu-1987-05-31`（西山友友，RPF #763）、`rin-rin-1992-06-21`（枚方リンリン，#659）、`pan-pan-1994-06-17`（天王寺パンパン，#592）。其餘 10 隻（日本平美美・佐世保愛愛・茶臼山鈴・浜松元気・みさきマホ・とくしまラン・京都茶々・茶臼山ミンミン・群馬トントン・群馬春）依維護者裁定**先只列在花花頁的子女表**、不逐隻建條目；表中以 🚧 標示依出生年與園別所作的 RPF 對應推測。另確認 **群馬トントン（RPF #593）為 `pan-pan-1994-06-17` 的雙胞胎**，`春`（♂）為トントン之弟。

**來源**：
- 維護者提供（2026-07-29）——生日・歿日・出生園・13 子女名單
- https://redpandafinder.com/#profile/761 (花花)

**新增條目**：
- `hoa-hoa-1982-06-15.md` — 花花 ホアホア Hoa-Hoa（RPF #761），♀，1982-06-15 生於石家莊市動物園、1985-03-19 來長野市茶臼山動物園、2000-10-08 歿（18 歲）；13 子女之母。`sources` 為維護者提供（無官方來源，`has_official_source` 為 false）

**更新條目**：
- `pan-pan-1994-06-17.md`・`rin-rin-1992-06-21.md`・`yuu-yuu-1987-05-31.md` — 母 花花 由純文字改 `[[hoa-hoa-1982-06-15]]` wikilink（三處原記「Hoa-Hoa」者即同一隻，已於同日前一筆判定）
- `pan-pan-1994-06-17.md` — 雙胞胎行補「トントン（群馬サファリパーク，RPF #593）」；½ 手足行標明「已建條目者」；ℹ️ 註改寫
- `yuu-yuu-1990-06-25.md` — 子女表 パンパン 該列的母欄改 wikilink
- `index.md` — 新增「長野市茶臼山動物園 始祖母（中國石家莊來源）」區塊一列；天王寺區塊 パンパン 該列補母名；條目總數 775 → 776

---

## [2026-07-29] update | ⚠️ 自我更正：撤回「RPF 混同茶臼山同名 Yuu-Yuu」之誤判；並依 RPF 逐隻補齊花花 13 子女的生卒與居住史

**1. 更正誤判（重要）**：同日前一筆 log 斷言「勇勇 1990 年生，不可能是 1992–93 那批之父，故 RPF 把茶臼山數隻同名 Yuu-Yuu 混為一人」——**此推論有誤，予以撤回**。勇勇（`yuu-yuu-1990-06-25`）1991-10-17 即由市川市動植物園移入茶臼山，1992 年初交配期時約 19 個月齡，而小熊貓雄性約 18 個月即可繁殖，時序完全可行。RPF 的血緣度劃分反而內部一致：1985–1991 年出生者父為 I-I／You-You（相對パンパン標 ½）、1992 年後出生者父為 Yuu-Yuu（標全血緣）。且 1988 年 `yuu-yuu-1987-05-31` 已移西山，此後茶臼山無其他 Yuu-Yuu，故研判該「Yuu-Yuu」即勇勇（仍待維護者確認、標 🚧）。相關 🚧 註記已於 `pan-pan-1994-06-17`、`rin-rin-1992-06-21` 兩頁改寫。

**2. 依 RPF 逐隻比對 13 名子女**（RPF 為線索級，全部標 🚧 待官方佐證）。維護者名單的園名與 RPF 居住史**逐隻吻合**，確認了 8 隻對應：

| 維護者名 | RPF | 生－歿 | 移入該園日 |
| --- | --- | --- | --- |
| 日本平美美 | #762 Mi-Mi ミミ ♀ | 1985-06-12 – 2003-06-11 | 日本平 1988-10-20 |
| 浜松元気 | #767 Genki 元気／げんき ♂ | 1989-06-30 – 1995-09-13 | 浜松 1990-03-20 |
| みさきマホ | #738 Maho マホ ♀ | 1991-06-06 – 1999-05-09 | みさき公園 1993-03-13 |
| とくしまラン | #660 Run ルン ♀ | 1992-06-21 – 2011-08-22 | 五月山 1994-03-11 → とくしま 2003-04-15 |
| 京都茶々 | #663 Cha-Cha 茶々／チャチャ ♀ | 1993-06-27 – 2016-02-17 | 京都 1995-06-17 |
| 茶臼山ミンミン | #664 Min-Min ♀ | 1993-06-27？ – 不明 | （RPF 該頁細節區塊無法載入）|
| 群馬トントン | #593 Ton-Ton トントン ♂ | 1994-06-17 – 2007-12-16 | 群馬サファリ 1998-01-28 |
| 群馬春 | #665 Ron-Ron ロンロン ♂（🚧 名字不符）| 1995-06-17 – 2004-11-19 | 群馬サファリ 1998-01-28 |

**新確認的雙胞胎關係**：ラン↔`rin-rin-1992-06-21`、茶々↔ミンミン、トントン↔`pan-pan-1994-06-17`。**新確認的父方**：1985–89 三隻父為 I-I、マホ 父為 You-You、1992 年後為勇勇（研判）。**花花的孫女**：マホ 之女 Fumi・Hou-Hou（1993 雙胞胎），即 RPF 列在パンパン ½ 手足中卻不在花花子女名單裡的那兩筆——疑點已解。

**仍未解**：

- **佐世保愛愛** 在 RPF 花花子女名單中無任何對應（RPF 剩餘三筆 #764／#766／#765 皆無佐世保居住史），全部資料待查證。
- **茶臼山鈴** 疑為 #766（Rei，♀，1988），惟「鈴」讀音（リン／スズ）與 Rei 不合。
- **RPF 14 vs 維護者 13**：RPF 多出 #764（♀，1987-05-31 生、2003-05-13 歿，茶臼山→西山 1991-10-30，**`yuu-yuu-1987-05-31` 的無名雙胞胎**，有三子女 Aiko／Taro／Jirou）。該隻正是 `yuu-yuu-1987-05-31` 頁所記「另有一隻無名雙胞胎手足」。
- #764／#765／#766／#664 四筆的 RPF 頁面細節區塊**無法載入**（只渲染名字列），僅能取得姓名與性別。

**來源**：
- https://redpandafinder.com/#profile/761 及其子女各頁（#762・#764・#765・#766・#767・#738・#660・#663・#664・#593・#665）

**更新條目**：
- `hoa-hoa-1982-06-15.md` — 子女表改寫為含生卒・移入日・父・RPF ID 的完整表；新增父欄研判說明 🚧
- `pan-pan-1994-06-17.md` — 撤回誤判註記，改列全血緣手足（花花 × 勇勇：リンリン・ルン・ミンミン・茶々・ロンロン）與 ½ 手足（父不同者）
- `rin-rin-1992-06-21.md` — 🚧 註改寫為「父研判即勇勇」並說明時序依據

---

## [2026-07-29] add | 新增 `apple-seed-1-akebi-2026-07-08`／`apple-seed-2-akebi-2026-07-08`（鯖江市西山動物園，母 アケビ 初次生產之雙胞胎）

鯖江市西山動物園官方 X（2026-07-29 發文）公布：**2026 年 7 月 8 日誕生雙胞胎寶寶 2 頭，母 アケビ、父 かんた，兩隻性別皆為雌性（メス）**。アケビ 為初次生產，幾乎整日待在巢箱內育兒，兩隻寶寶在巢箱中順利成長。尚未命名，依蘋果籽制度建佔位條目直接上站。

**建檔資格四項全符**：父母皆有條目（`akebi-2020-06-29` × `kanta-2018-07-12`）、生日確認（2026-07-08）、公告時在世、尚未命名。性別已由園方公布故直接填 `sex: female` 與 `female` tag（非留空）。園方公告未區分兩隻寶寶的個別特徵，1號／2號僅為建檔序號、非園方編號（已於 2號 頁註明）。RPF 尚無建檔。

同時是 アケビ 與 かんた 雙方的第一胎，故兩隻寶寶無手足（除彼此）、無 ½ 手足。

**來源**：
- https://x.com/nishiyama_zoo/status/2082300119756706179 （鯖江市西山動物園官方 X）

**新增條目**：
- `apple-seed-1-akebi-2026-07-08.md` — 蘋果籽1號 Apple Seed 1，♀，2026-07-08 生於鯖江市西山動物園，現居同園（佔位，`apple-seed` tag）
- `apple-seed-2-akebi-2026-07-08.md` — 蘋果籽2號 Apple Seed 2，♀，同胎

**更新條目**：
- `akebi-2020-06-29.md` — 引言補初次生產；`## 家族` 新增 配偶 `kanta` 與兩名女兒 wikilink；`sources` 加園方 X
- `kanta-2018-07-12.md` — 引言補 2026 年產仔；`## 家族` 新增 配偶 `akebi` 與兩名女兒 wikilink；`sources` 加園方 X
- `index.md` — Sumomo × Yan-Yan 家族區塊新增兩列；條目總數 776 → 778

---

## [2026-07-29] add | 花花 13 子女中 6 隻建檔：`mi-mi-1985-06-12`、`genki-1989-06-30`、`maho-1991-06-06`、`ran-1992-06-21`、`cha-cha-1993-06-27`、`ton-ton-1994-06-17`

承同日 RPF 逐隻比對結果，把資料齊備的 6 隻子女建檔（維護者提供的名單與 RPF 居住史逐隻吻合，園名全部對得上）。生日・歿日・居住史・性別依 RPF（🚧 線索級、無官方佐證），母子關係與所屬園由維護者名單佐證；`sources` 均為「維護者提供（2026-07-29）」＋ RPF，故 `has_official_source` 為 false。

**暫不建檔的 4 隻**：茶臼山ミンミン（RPF #664 頁面細節區塊無法載入、缺歿日）、群馬春（疑為 RPF #665 ロンロン 但名字不符）、佐世保愛愛（RPF 無對應）、茶臼山鈴（疑為 #766 Rei 但讀音不合）。

**新確立的家族結構**（皆記於各頁，🚧 待維護者確認父方）：

- **花花 × I-I**（1985–89）：`mi-mi-1985-06-12`、`yuu-yuu-1987-05-31`、`genki-1989-06-30` 三隻互為**全血緣**手足
- **花花 × You-You**（1991）：`maho-1991-06-06`
- **花花 × 勇勇**（1992–95，研判）：`ran-1992-06-21`＋`rin-rin-1992-06-21`（雙胞胎）、`cha-cha-1993-06-27`＋ミンミン（雙胞胎）、`ton-ton-1994-06-17`＋`pan-pan-1994-06-17`（雙胞胎）、ロンロン
- **花花的孫女**：`maho-1991-06-06` 之女 Fumi・Hou-Hou（1993 雙胞胎）——即 RPF 列在パンパン ½ 手足中卻不在花花子女名單裡的兩筆，疑點已解

**來源**：
- 維護者提供（2026-07-29）——13 子女名單（姓名・所屬園・性別提示）
- https://redpandafinder.com/#profile/762 ／ 767 ／ 738 ／ 660 ／ 663 ／ 593 （各隻生卒・居住史・性別・父）

**新增條目**：
- `mi-mi-1985-06-12.md` — 美美 ミミ（RPF #762），♀，1985-06-12 – 2003-06-11；茶臼山→静岡市立日本平動物園（1988-10-20）；父 I-I
- `genki-1989-06-30.md` — 元気 げんき（RPF #767），♂，1989-06-30 – 1995-09-13；茶臼山→浜松市動物園（1990-03-20）；父 I-I；一女 Yuu（1994）
- `maho-1991-06-06.md` — マホ（RPF #738），♀，1991-06-06 – 1999-05-09；茶臼山→みさき公園（1993-03-13）；父 You-You；二女 Fumi・Hou-Hou
- `ran-1992-06-21.md` — ラン（RPF #660），♀，1992-06-21 – 2011-08-22；茶臼山→五月山動物園（1994-03-11）→とくしま動物園（2003-04-15）；`rin-rin-1992-06-21` 雙胞胎。名字以維護者的「ラン」為準，RPF 的 ルン／Run 收入 `english_variants`
- `cha-cha-1993-06-27.md` — 茶々 チャチャ（RPF #663），♀，1993-06-27 – 2016-02-17；茶臼山→京都市動物園（1995-06-17）；享年 22 歲
- `ton-ton-1994-06-17.md` — トントン（RPF #593），♂，1994-06-17 – 2007-12-16；茶臼山→群馬サファリパーク（1998-01-28）；`pan-pan-1994-06-17` 雙胞胎

**更新條目**：
- `hoa-hoa-1982-06-15.md` — 子女表 6 隻改 wikilink；引言改寫（9/13 已建檔）
- `yuu-yuu-1990-06-25.md` — 原「子女（母不詳）」小節改為「子女（與花花所生）」，列 7 隻（含 ミンミン・ロンロン 純文字）；引言補花花一批
- `rin-rin-1992-06-21.md` — 父改 `[[yuu-yuu-1990-06-25]]` wikilink（🚧 研判）；雙胞胎 Run 改 `[[ran-1992-06-21]]`；補全血緣／½ 手足行
- `pan-pan-1994-06-17.md` — 雙胞胎改 `[[ton-ton-1994-06-17]]`；手足行全面 wikilink 化
- `yuu-yuu-1987-05-31.md` — 補「全血緣兄弟姊妹（花花 × I-I）」與 ½ 手足行
- `index.md` — 花花區塊拆為「始祖母／子女」兩表、新增 6 列；條目總數 778 → 784
- `data/zoos.json` — 五月山動物園 `location_ja` 由「池田市 大阪府」修正為「大阪府池田市」（與其他園一致的都道府県優先寫法）

## [2026-07-29] update | 茶臼山動物園官方年度存檔比對：`seina`／`koko` 生日改 2000-06-23、修 `chao` 誤連、42 隻補官方 sources

**來源**：
- 長野市茶臼山動物園 動物情報バックナンバー（園方官網，官方一手來源）
  - http://www.chausuyama.com/zukan/zukan/2003 ／ 2006 ／ 2008 ／ 2009 ／ 2010 ／ 2011 ／ 2012 ／ 2013 ／ 2014 ／ 2015 ／ 2017 ／ 2021 ／ 2022
  - 逐年小熊貓段落原文摘錄已存 `sources/chausuyama-zukan/2003.md`–`2022.md`（21 檔），比對報告見同資料夾 `gap-analysis.md`
  - 實測 2004／2005／2019／2020 為 404、2007／2016／2018 該年無小熊貓記述、2021 僅涵蓋 1–5 月
  - 抓取注意：帶 `www.` 常回空白，須用 `https://chausuyama.com/zukan/zukan/YYYY`

**重命名（rename）**：
- `seina-2000-06-25.md` → `seina-2000-06-23.md` — 生日依園方改 2000-06-25 → **2000-06-23**。原值僅有 RPF #89 為據；園方 2010 年動物情報（「セイナ(2000年6月23日長野市茶臼山動物園生まれ)」）與 2017 年訃報（「2000年6月23日に当園で生まれました」）兩處獨立記載均為 6/23，依「官方來源可直接採用／衝突以園方為準」改正。旁證：2011-06-24 生產當日園方記「セイナ(11歳)」，6/23 生才剛滿 11 歲
- `koko-2000-06-25.md` → `koko-2000-06-23.md` — 雙胞胎一併改。RPF #440 原即記 2000-06-23，先前為配合 `seina` 的 6/25 而暫從並留 🚧 待裁定；官方採 6/23 後兩者一致，🚧 備注已刪（條目與 `index.md` 皆刪）
- 全 wiki 47 檔內指向 `seina-2000-06-25` 的連結（55 處）與指向 `koko-2000-06-25` 的連結（49 處）已同步更名；`log.md` 與 `log-archive/` 為既往紀錄，不追改

**更新條目（事實修正）**：
- `mei-2003-06-21.md`、`kokoro-2006-06-20.md`、`sara-2009-06-19.md`、`gigi-2009-06-19.md`、`luna-2010-06-26.md`、`momo-2011-06-24.md` — 手足列的 `chao-2006-07-06` 改為 `chao-2004-06-17`。園方 2009 年頁明載 `chao-2006-07-06`（2006-07-06 生）是 2009-01-23 自鯖江市西山動物園來的種雄，與 Seina × Kiki 無血緣；`momo` 該列原本連結指 2006 生、生年欄卻寫 2004，自我矛盾
- `subaru-2010-06-26.md` — 茶臼山訖日 2013-05-14 → **2013-05-13**（園方載 5 月 13 日「旅立ちます」；平川入園日維持 05-14）
- `shingen-2011-06-18.md` — 茶臼山訖日 2014-11-13 → **2014-11-11**（園方載 11/11 出発、11/13 釧路到着；釧路起日維持 11-13）
- `taiyo-2013-06-21.md` — 茶臼山訖日與千葉市起日 2021-05-19 → **2021-05-20**（園方載 5/19 展示終了、5/20 移動）
- `ron-2005-06-23.md` — 母親中文名「劉星」改「流星」並改 wikilink（園方寫「リューシー(流星)」，與 `liuxing-1997-06-16` 自身一致）
- `seina-2000-06-23.md` — 子女表 `tsubasa-2006-06-20` 整列重複兩次，刪去一列

**更新條目（補官方細節）**：
- `seina-2000-06-23.md` — 補死亡時刻與死因（2/17 上午 10 時半、加齢による心不全）、得年 16 歲 7 個月、「7 胎 14 隻」與園方語彙「グランドマザー」；補生日採官方之註記
- `ron-2005-06-23.md` — 補死因（腸閉塞による胃拡張および誤嚥性肺炎による呼吸不全）、得年 15 歲 8 個月、獻花台期間；補散步活動沿革（2006 起、13 年、2014 夏停辦→10/11 再開、2017 起 8–9 月中止、2019-03 引退、2019-09 展示終了轉後場）
- `nene-2012-07-05.md` — 補死因（心不全および肺水腫による循環機能不全）、得年 9 歲 11 個月、歿前食慾衰退、追思留言簿期間
- `hikaru-2015-07-19.md` — 補死因（腸重積と十二指腸閉塞）、得年 6 歲 7 個月、病程、追思留言簿期間、雙胞胎眼周深淺辨識法與 2015-10-17 首次公開
- `ajisai-2006-06-22.md` — 子女表補產次（第 1–4 胎，2010 為初產）
- `non-2009-06-19.md` — 子女表補產次（第 1–3 胎，2012 為初產）
- `subaru-2010-06-26.md` — 引言補配偶 `fuumi-2007-07-11` 與園方記述（幼時膽小、討厭上體重計）；母親與子女改 wikilink、子女表補母欄
- `fuumi-2007-07-11.md` — 補 Subaru 2013 年婿入平川係茶臼山方面點名她為配對對象
- `shingen-2011-06-18.md` — 補命名軼事（茶臼山未辦募集，由《どうぶつのくに》讀者徵名）、母親改 wikilink
- `furin-2007-07-11.md` — 補 2008-06-30 來園為母親故鄉「里帰り」與新獸舍擴充第一步、外觀似親描述、2012 年 `taichi-2005-07-01` 為其配偶候補
- `holly-2016-06-02.md`、`mutan-2014-06-19.md` — 補 2021-02-03 起於「レッサーパンダのおうち」同居展示
- `taiyo-2013-06-21.md` — 補命名經過（2013 秋祭徵名 182 人、選定理由）與移動細節；母親改 wikilink
- `koko-2000-06-23.md` — 補生日改採 6/23 的依據說明
- `anzu-2013-06-21.md`、`kirara-2005-06-23.md`、`seita-2005-06-23.md` — 母親由純文字改 wikilink（`ajisai-2006-06-22`／`liuxing-1997-06-16`）

**補官方 sources（42 隻，原先全庫零引用 chausuyama.com）**：
- 2003：`non-non-2003-06-16`、`chi-chi-2003-06-16`、`chihiro-2003-06-16`、`mei-2003-06-21`
- 2006–2011：`tsubasa-2006-06-20`、`kokoro-2006-06-20`、`airi-2006-06-20`、`sora-seina-2008-06-16`、`lala-2008-06-16`、`seita-2005-06-23`、`furin-2007-07-11`、`kiki-2000-07-04`、`seina-2000-06-23`、`chao-2006-07-06`、`ajisai-2006-06-22`、`sara-2009-06-19`、`non-2009-06-19`、`gigi-2009-06-19`、`subaru-2010-06-26`、`luna-2010-06-26`、`momo-2011-06-24`、`shingen-2011-06-18`
- 2012–2015：`kenshin-2012-06-18`、`sachi-2012-06-18`、`nene-2012-07-05`、`nozomu-2012-07-05`、`taichi-2005-07-01`、`taiyo-2013-06-21`、`anzu-2013-06-21`、`popo-2014-07-01`、`jaja-2014-07-01`、`hikaru-2015-07-19`、`hibiki-2015-07-19`、`fuumi-2007-07-11`、`yuri-2013-06-26`、`futa-2003-07-05`
- 2017／2021：`liuxing-1997-06-16`、`yuu-yuu-1990-06-25`、`koko-2000-06-23`、`ron-2005-06-23`、`mutan-2014-06-19`、`holly-2016-06-02`

**更新條目**：
- `index.md` — `seina`／`koko` 兩處 slug 更名；刪去 Koko 列的 🚧 生日備注。條目總數不變（784）

**待維護者裁定（未改）**：
- `kirara-2005-06-23.md` 引言稱「父親 Kiki 亦是 `seina-2000-06-23` 的父親」，但園方 2017 年訃報載 Seina 之父為 ユーユー(勇勇)、Kiki 是其配偶，該句疑誤
- `chao-2004-06-17.md` frontmatter 第二站為 恩賜上野動物園，`index.md` 該列卻寫多摩動物公園，兩者不一致
- 官方拼法不一：`liuxing-1997-06-16` 的假名 2017 年頁作「リューシー」、2021 年頁作「リュウシー」，是否增列異寫待定
- 2004／2005／2018／2019／2020 年度頁無法取得（404 或空白），該期間官方記述（含 `chi-chi` 2005-03 嫁千葉、`mei` 2005-04 赴首爾、`non-non` 2005-03 赴多摩、`chihiro` 2005-12 赴東武、`ron` 2019 引退）仍缺一手佐證；2021 年 6–12 月段落亦待補

## [2026-07-29] update | `liuxing` 假名並收官方兩種寫法

**來源**：
- http://www.chausuyama.com/zukan/zukan/2017 — 女兒 `seina` 訃報作「リューシー(流星)」
- http://www.chausuyama.com/zukan/zukan/2021 — 兒子 `ron` 訃報作「リュウシー」

**更新條目**：
- `liuxing-1997-06-16.md` — `japanese` 由「流星, リューシー, リューシン」改為「流星, リューシー, リュウシー, リューシン」，標題同步；引言補註園方兩種假名寫法的出處（2017 年頁的「リューシー(流星)」亦是漢字名唯一的官方佐證）

## [2026-07-29] update | 茶臼山舊年度存檔網址已失效之處理：`chausuyama.com` 列入官方白名單、Wayback 改為拆內層判斷

**背景（更正前一筆記錄的前提）**：`http://www.chausuyama.com/zukan/zukan/YYYY` 這批 sources
**在瀏覽器開啟已是 404**。官網已改版為扁平靜態站（`event.html`、`news/YYYY-MM-DD.html`），
舊 CMS 年度存檔整批下架，`/zukan` 系列路徑亦無索引頁，新站無替代頁面。先前抓取到內容是
工具端快取所致；內容為園方原文無誤，但原始位址已死。

**處理方針（維護者裁定）**：`sources:` **保留原始位址作為 canonical 出處**（不改為 Wayback），
另在存檔資料夾標註失效狀態；線上覆核走 Wayback。

**工具變更**：
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `chausuyama.com`（園方官網，現站仍在用），
  並註明舊 `/zukan/zukan/YYYY` 已下架
- `tools/build_db.py` — `is_official_source` 新增 Wayback 處理：**不**整域列入 `web.archive.org`
  （archive.org 上什麼站都有，整域列入會把粉絲站快照誤判官方），改為以 `_unwrap_wayback()`
  拆出被封存的原始 URL、遞迴判斷內層 host。故
  `https://web.archive.org/web/2018/http://www.chausuyama.com/zukan/zukan/2013` 判為官方，
  而同形式包住粉絲部落格或 RPF 則仍為非官方。timestamp 可省略成年份
- 已驗證：8 組測試 URL 判定皆符合預期

**效果**：`sources` 含 chausuyama 的 42 隻個體 `has_official_source` 全數轉 true
（原先為 false，前一筆記錄誤稱已轉），全庫官方旗標 true 由 127 增至 169。

**新增文件**：
- `sources/chausuyama-zukan/README.md` — 記錄原始網址已失效、Wayback 覆核寫法、各年可取得狀態表、
  以及 2004／2005／2019／2020 缺頁導致尚無一手佐證的事件清單

## [2026-07-30] fix | 社群回報查證：`yuu-yuu` 補旭山官方來源（資料值不變）

**來源**：
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/2200/p008756.html （旭山動物園ヒストリー・平成25年）
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/2200/p008801_d/fil/dayori200.pdf （どうぶつえんだより №200，2013-08-30）

**背景**：讀者回報 `yuu-yuu`（2011-05-28，旭山）轉園一事並附上兩份旭山官方資料。查證後
**wiki 現值完全正確、無需更正**——園方年表載「レッサーパンダの渝渝(ユーユー・メス)が中国の
重慶動物園から来園(7月10日)」，園報載「7月上旬。中国の重慶動物園からやってきました」「メス２才」，
與 wiki 的 2013-07-10 入旭山一致。京都停留（2013-03-30 – 2013-07-10）亦不衝突：2013 年重慶
動物園一批 3 隻先抵京都，其中 1 隻後轉旭山。

**更新條目**：
- `yuu-yuu-2011-05-28.md` — `sources` 新增旭山年表與園報 №200 兩筆官方來源（原僅 RPF #227），
  `has_official_source` 轉 true

**待查證（同批回報，暫不動）**：
- `laila` 轉園日期：回報稱 2013-04-15（依 YouTube 影片第 23 秒拍到的園方公告牌），wiki 現值
  2013-02-28（僅 RPF #60 支撐）。円山 2013 年移動公告已下架、查無官方頁；同好紀錄指向 2013 年
  4 月（另有 4/21「送る会」說法），日期未定，待維護者核對影片後再改

## [2026-07-30] add | `anri` 的雙胞胎 `daura` 一線：曾外祖父母與旁系四筆

**來源**：
- https://redpandafinder.com/#profile/454 (Daura)
- https://redpandafinder.com/#profile/668 (Namu)
- https://redpandafinder.com/#profile/786 (Kuro)
- https://redpandafinder.com/#profile/453 (Luli)

**新增條目**：
- `daura-1994-06-19.md` — Daura ダウラ（RPF #454），♀，生於 1994-06-19 群馬サファリパーク、歿於 2012-06-11 東北サファリパーク；`anri` 之雙胞胎
- `namu-1993.md` — Namu ナム（RPF #668），♀，中國野生捕獲、生年不詳（比照雙胞胎兄弟 `kuku` 以抵日年 1993 為近似），1993-10-26 見於群馬サファリパーク、1994-10-15 歿；`anri`／`daura` 之母
- `kuro-1992-07-01.md` — Kuro クロ（RPF #786），♂，生於 1992-07-01 長野市茶臼山動物園、1993-12-26 赴群馬サファリパーク、2009-11-19 歿；`anri`／`daura` 之父、`you-you-1987-07-26` 陽陽之子（⚠️ 勿與 `kuro-1997-07-27` ♀ 混淆）
- `luli-2004-06-29.md` — Luli ルリ／Pi-Pa（RPF #453），♀，生於 2004-06-29 東北サファリパーク、2005-07-08 移居 Buenos Aires Eco-Park 🇦🇷、2019-10-01 歿；`daura` × `kuku` 之女

**更新條目**：
- `anri-1994-06-19.md` — 父母（`namu`／`kuro`）、雙胞胎（`daura`）、配對（`kuku`）由純文字改為 wikilink
- `kuku-1993.md` — **更正子女歸屬**：原表格把 8 隻子女全列為與 `anri` 所生，惟 RPF #478／#453 明載 `shin-shin-2000-06-30`（晨星）與 `luli-2004-06-29` 之母為 `daura`，故拆為「與 `anri` 所生（6 隻）」與「與 `daura` 所生（2 隻）」兩表；雙胞胎 `namu` 補 wikilink，引言補述兩名外甥女皆與其產仔
- `shin-shin-2000-06-30.md` — 父母補 wikilink；手足改分「全血緣妹 `luli`」與「半血緣（母 `anri`）」兩列
- `you-you-1987-07-26.md` — 子女列補上 `kuro-1992-07-01`（原僅列於無條目的假名清單）與 `maho-1991-06-06`
- `liuxing-1997-06-16.md`、`yueshi-1999-07-08.md` — 手足清單中已有條目者補 wikilink（含新建的 `luli`）
- `index.md` — 暢暢家族新增「曾外祖父母與外祖母旁系（群馬 → 東北サファリ）」小節共 4 筆；條目總數更新為 788

**備注**：
- Namu 與 Kuku 為雙胞胎兄妹，其女 `anri`／`daura` 又分別與 Kuku 產仔（舅父 × 外甥女），為真實近親配對紀錄、非資料錯誤
- 四筆皆僅有 RPF（線索級）為據，各條目已註明園方一手佐證 🚧 待查證
- Kuro 之母 Rei（RPF #766）、三胞胎手足 Ken-Ken（#787）／Shiro（#785）暫未建條目

## [2026-07-30] fix | `laila` 離開円山日期由 2013-02-28 更正為 2013-04-15（承上批回報，影片查證完成）

**來源**：
- https://www.youtube.com/watch?v=W6Cu-14Lywc — 円山動物園「ライラを送る会」影像（Mmovies21，2013-04-14 攝）

**查證經過**：影片說明欄載「4月14日(日)は、園内の動物科学館にて『ライラを送る会』が行われ」、
拍攝日註明 2013 年 4 月 14 日；影片 0:57 園方職員於會中說明「明日、動物園を出発いたします」，
故出發日為 **2013-04-15**。回報者所稱 4/15 成立（其指第 23 秒的公告，實際依據為 0:57 的職員說明；
0:17 處的說明為會場改至動物科学館ホール）。原值 2013-02-28 僅有 RPF #60 支撐，予以更正。
円山 2013 年度移動公告已自官網下架，查無官方頁；此影片為園方職員口頭公告之實錄，
歸入 `extra_sources`（非官方 host，不計入 `has_official_source`）。

**更新條目**：
- `laila-2010-07-10.md` — `zoos:` 札幌市円山動物園訖與アドベンチャーワールド起由 2013-02-28 改為
  2013-04-15；居住史表格同步；引言補「送る会」與啟程日；新增 `extra_sources`（影片連結＋出處註）

**備注**：確認的是**離開円山**之日；抵達アドベンチャーワールド之確切日期無來源，
沿用單一交界日慣例暫記同日，日後若查得園方公開日再修。

## [2026-07-30] add | `kuro-1992-07-01` 上溯茶臼山：`rei` 一家四筆；確認花花名單的「鈴」＝ Rei

**來源**：
- https://redpandafinder.com/#profile/766 (Rei)
- https://redpandafinder.com/#profile/739 (Santa)
- https://redpandafinder.com/#profile/785 (Shiro)
- https://redpandafinder.com/#profile/787 (Ken-Ken)

**新增條目**：
- `rei-1988-06-17.md` — Rei レイ／鈴（RPF #766），♀，1988-06-17 – 2008-01-19，終生長野市茶臼山動物園；`hoa-hoa-1982-06-15` 花花 × I-I 之女、`you-you-1987-07-26` 陽陽之配偶
- `santa-1991-06-29.md` — Santa サンタ（RPF #739），♂，1991-06-29 – 2005-07-28；茶臼山 → みさき公園（1993-03-13，與 ½ 姊 `maho-1991-06-06` 同日）→ 姫路セントラルパーク（1999-08-20）
- `shiro-1992-07-01.md` — Shiro シロ／Siro（RPF #785），♂，1992-07-01 – 2006-01-20，終生茶臼山、無子女；`kuro-1992-07-01` 之三胞胎手足
- `ken-ken-1992-07-01.md` — Ken-Ken ケンケン／Kenken（RPF #787），♂，1992-07-01 – 2001-11-25；茶臼山 → 多摩動物公園（1995-02-14），無子女（⚠️ 勿與 `ken-ken-2006-07-18` 混淆）

**更新條目**：
- `hoa-hoa-1982-06-15.md` — **解決名單上「鈴」的 🚧 待確認**：原註記「疑為 RPF #766（Rei），惟『鈴』讀音與 Rei 不合」，經查「鈴」的音讀正是 レイ（如「予鈴」よれい），加上 1988 年生・茶臼山出生並終老全數相符，判定為同一隻，該列改為 `rei-1988-06-17` 條目連結並補齊生卒與子女；引言「9 隻已建條目、餘 4 隻」改為「10 隻、餘 3 隻」
- `hoa-hoa-1982-06-15.md` — 13 vs 14 名子女的差額註記補進度：RPF 兩筆「(no name)」已辨明為 #764（♀，1987-05-31 – 2003-05-13，1991 年移西山；`jirou-1990-07-06`・アイコ・タロ 之母）與 #765（♂，1988-06-17 生、同年 10-18 夭折，`rei` 之同胎手足）；#765 早夭未入名單屬合理，差額主要來自 #764。另註明上表的「You-You」即已建條目的 `you-you-1987-07-26`（陽陽，RPF #775）
- `kuro-1992-07-01.md` — 母（`rei`）、三胞胎手足、全血緣兄（`santa`）由純文字改為 wikilink，補外祖母 `hoa-hoa-1982-06-15`
- `you-you-1987-07-26.md` — 子女列補 `rei` 所生四子；加註牠同時與花花及花花之女配對（母女兩代）
- `index.md` — 花花區塊新增 `rei` 一列與「孫輩」小表 4 筆；區塊說明改為「10 隻已建條目、餘 3 隻」；條目總數更新為 792

**備注**：
- RPF 的 #766（Rei）與 #785（Shiro）**個體頁無法載入**（資料集缺 `location.N` 欄位，SPA 渲染失敗、只留前一頁殘影）。改由 RPF 匯出資料集 `https://redpandafinder.com/export/redpanda.json` 直接取值（vertices／edges；zoo 以 lineage_id 對應 `data/zoos.json`），已在兩條目註明
- `rei` 的居住史因資料集無移動紀錄，以「生日 – 歿日」單段填入，🚧 待官方佐證
- 陽陽（`you-you-1987-07-26`）同時與花花及其女 `rei`、#764 產仔，為茶臼山早期繁殖的真實紀錄，非資料錯誤
- Rei 之父 I-I（RPF #768，ja 良／いい，中國野生捕獲、生年不詳，1985-03-19 與花花同日入園、1990-03-19 歿）暫未建條目——生年不詳且明顯為成獸入園，若比照 `kuku-1993` 以抵日年當近似生年會失真，建檔方式待維護者裁定

## [2026-07-30] add | 茶臼山初代種公 `i-i-nagano`（誼誼）建為檔案卡；`rei` 補漢字名「鈴」

**來源**：
- 維護者提供（2026-07-30）— 中文名「誼誼」、`rei` 的漢字名「鈴」
- https://redpandafinder.com/#profile/768 (I-I) — 經 https://redpandafinder.com/export/redpanda.json 取值

**新增條目**：
- `i-i-nagano.md` — I-I 誼誼／谊谊（RPF #768），♂，**生年不詳**、歿於 1990-03-19；長野市茶臼山動物園（1985-03-19 – 1990-03-19）。花花前六名子女（`mi-mi-1985-06-12`／`yuu-yuu-1987-05-31`／無名♀ #764／無名♂ #765／`rei-1988-06-17`／`genki-1989-06-30`）之父，茶臼山**初代種公**

**建檔方式（維護者裁定）**：採 📇 檔案卡（`limited-profile`）——`born` 留空、`birth_zoo: unknown`、`last_seen: 1990-03-19`；不比照 `kuku-1993` 以抵日年當近似生年（牠明顯是成獸入園，填 1985 會失真）。**不掛 `unverified`**（已確認歿日、非動向不明）。slug 依無生日 fallback 規則取 `名字-園簡稱` ＝ `i-i-nagano`
**命名（維護者提供）**：
- **中文名「誼誼／谊谊」**（誼 yì → 羅馬拼音 I-I）。lineage 的 `ja.name` 記漢字「良」屬機械轉寫之誤（「良」訓讀作 いい 罕見，實為把中文名硬套日文漢字），**不採用**——正是 `CLAUDE.md`「ja.name 含漢字多半實為中文名，應經維護者確認後放 `chinese`」的案例。假名 いい 取自 `ja.othernames`、暫收 `japanese`，園方實際稱呼 🚧 待查證

**更新條目**：
- `rei-1988-06-17.md` — **補漢字名「鈴」**（維護者提供）：`japanese` 由「レイ」改為「鈴, レイ」，標題改 `Rei 🪽（鈴 / レイ）`；父改連 `i-i-nagano`
- `hoa-hoa-1982-06-15.md` — 子女表「父」欄的 4 筆 I-I 改為條目連結；配偶行改列三代種公分期（誼誼 1985–1989／陽陽 1991／勇勇 1992 後）；父欄補充改為「已建條目」並記中文名來由與「野生捕獲」存疑（與花花同日入園，極可能同批自石家莊來園）
- `mi-mi-1985-06-12.md`、`yuu-yuu-1987-05-31.md`、`genki-1989-06-30.md` — 父 I-I 由純文字改為 `[[i-i-nagano]]`，移除「暫無條目」字樣
- `index.md` — 花花區塊「始祖母」小節改名為「始祖母與初代種公」並新增 `i-i-nagano` 一列；條目總數更新為 793

**備注**：
- 承上一筆的待裁定事項，維護者選擇 `born` 留空 + `limited-profile` 檔案卡寫法
- 誼誼與花花的入園日同為 1985-03-19，兩隻應為同批引進；RPF 對兩隻都標「野生捕獲」，但花花經維護者校訂為石家莊市動物園出生，故誼誼的出身同樣存疑、留待官方佐證

## [2026-07-30] update | `i-i-nagano` 補來日前居住史：石家莊市動物園（年份不詳）

**來源**：
- 維護者提供（2026-07-30）

**更新條目**：
- `i-i-nagano.md` — `zoos:` 首站補 `石家莊市動物園 ( – 1985-03-19)`（**起始年份不詳、留空**，居住史渲染為「? – 1985-03-19」）；引言補述自石家莊來日；原「野生捕獲之說待查證」註記改寫為「來日前居於石家莊市動物園」＋「是否出生於該園未確認」兩段
- 維持 `birth_zoo: unknown`：只知來源園、不確定是否為出生園（花花是確定出生於石家莊，誼誼不是），故首站不標 🐣

**備注**：
- 誼誼與花花同批自石家莊市動物園來日、同日（1985-03-19）入茶臼山，可解釋 RPF 把兩隻都誤標為「野生捕獲」

## [2026-07-30] fix | `yuu-yuu`（渝渝）刪除不存在的京都停留：重慶 → 旭山為直接移動

**來源**：
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/2200/p008756.html （旭山動物園ヒストリー・平成25年）
- https://www.city.asahikawa.hokkaido.jp/asahiyamazoo/2200/p008801_d/fil/dayori200.pdf （どうぶつえんだより №200，2013-08-30）
- https://www.city.kyoto.lg.jp/bunshi/page/0000183875.html （京都市廣報資料「レッサーパンダの移動について」，2015-06-05）

**背景（推翻本日前一筆判斷）**：本日先前一筆記錄稱「京都停留（2013-03-30 – 2013-07-10）亦不衝突：
2013 年重慶動物園一批 3 隻先抵京都，其中 1 隻後轉旭山」，該推論有誤，實為誤讀同好紀錄。
重新查證三方官方來源後確認渝渝**從未待過京都**：

1. 旭山年表載「レッサーパンダの渝渝(ユーユー・メス)が**中国の重慶動物園から**来園(7月10日)」；
   園報 №200 載「7月上旬。**中国の重慶動物園から**やってきました」——來源園明載為重慶，
   若自京都轉入，園方寫法會是「京都市動物園から来園」。
2. 京都市廣報資料載 2013-03-30 由**上海動物園**導入者為「ウーロン」與「ジャスミン」**兩隻**
   （`oolong-2011-06-05`、`jasmine-2010-07-14`），名單中無渝渝。
3. 同好紀錄原文為「2013 年重慶動物園有 3 隻來日，其中 1 隻是到旭山的渝渝」——是**分別**
   來日、各往不同園，並非「先集體抵京都再分流」。

原 wiki 的京都區間起日 `2013-03-30` 與烏龍完全相同，研判為早期建檔時由烏龍條目誤植。

**更新條目**：
- `yuu-yuu-2011-05-28.md` — `zoos:` 刪除「京都市動物園 (2013-03-30 – 2013-07-10)」一段，
  重慶動物園訖日由 `2013` 改為 `2013-07-10`（居住史表格隨 `gen_residence.py` 重生）；
  引言改為「2013-07-10 直接由重慶動物園來到旭山」並註明官方來源與「渝」的命名由來

**備注**：
- `oolong-2011-06-05` 的來源園亦待釐清——wiki 記其出生於重慶動物園，但京都廣報資料寫
  「上海動物園（中国）から導入」，可能為經上海出口或京都記載以出口機構為準，🚧 待查證（本次未動）

## [2026-07-31] add | 桐生が岡動物園首次繁殖：`fran` × `kazunoko` 雙胞胎誕生（蘋果籽佔位）

**來源**：
- https://www.city.kiryu.lg.jp/zoo/event/1027433.html （桐生市官方公告「レッサーパンダの赤ちゃんが誕生しました！」，2026-07-31）
- https://www.instagram.com/kiryuzoo/p/DbcdbHIDyjK/ （桐生が岡動物園官方 IG，2026-07-31）
- https://www.city.kiryu.lg.jp/zoo/event/1027366.html （懷孕公告與レッサーパンダ舎觀覽限制，2026-07-08）

**新增條目**：
- `apple-seed-1-fran-2026-07-12.md` — 蘋果籽1號（Apple Seed 1），**第一仔**（上午 5:56 誕生、毛色較淺），生於 2026-07-12，桐生が岡動物園
- `apple-seed-2-fran-2026-07-12.md` — 蘋果籽2號（Apple Seed 2），**第二仔**（上午 6:55 誕生、毛色較深），生於 2026-07-12，桐生が岡動物園

**建檔方式**：蘋果籽佔位（四項資格全符合——父母皆有條目、生日確認、尚在世、尚未命名）。
`sex` 留空、tags 不加性別（園方以巢箱內攝影機觀察，**尚未進行雌雄判別**）；`japanese` 留空（園方稱「赤ちゃん」為泛稱非名字）。
序號 1號／2號**對應園方公告的「第一仔／第二仔」**，非任意暫編——官方公告明載出生時刻與毛色深淺可資區別。
RPF 尚未建檔，故無 `rpf_id`／`rpf_url`。

**要點**：
- **桐生が岡動物園創園以來首次成功繁殖小熊貓**，亦為母 `fran`（6 歲）與父 `kazunoko`（4 歲）雙方的初次產仔
- 自然哺育：園方經巢箱攝影機確認授乳與促進排泄行為，判定成長順利；為免干擾育兒，飼育員與獸醫暫不直接接觸寶寶
- レッサーパンダ舎自 7 月 8 日公布懷孕起臨時休館，出生後繼續閉館
- 巧合：母親 `fran` 的雙胞胎姊妹 `lian`（現居ソウル大公園動物園）於 2026-06-19 亦產下雙胞胎，兩姊妹同年各生一對雙胞胎

**更新條目**：
- `fran-2020-07-20.md` — 引言補 2026 產仔敘述；`## 家族` 加配偶 `kazunoko` 與子女兩筆；`sources` 補園方公告與官方 IG；`instagram` 補官方 IG 貼文
- `kazunoko-2021-08-04.md` — 引言補 2026 產仔敘述；`## 家族` 加配偶 `fran` 與子女兩筆；`sources` 補園方公告與官方 IG；新增 `instagram` 欄
- `index.md` — Franken 其他子女區塊新增兩隻蘋果籽；`fran` 與 `kazunoko` 說明欄補產仔註記；最後更新改 2026-07-31、條目總數更新為 795

**工具變更**：
- `tools/build_db.py` — `OFFICIAL_IG_ACCOUNTS` 新增 `kiryuzoo`。已核實：桐生市官網動物園首頁的 IG banner 連至 `instagram.com/kiryuzoo`，確為園方官方帳號，故其貼文可認列官方來源（僅完整形式 `/kiryuzoo/p/…` 生效）

## [2026-07-31] rename | 繁繁 Fan-Fan → 樂樂 Le-Le（台北市立動物園揭名）

**來源**：
- https://www.zoo.gov.taipei/News_Content.aspx?n=BD065B2FA7782989&sms=72544237BBE4C5F6&s=09AADC73DBB8E0B3 （臺北市立動物園新聞稿〈小貓熊「樂樂」、「甜甜」溫帶動物區可愛亮相 動物訓練無縫接軌〉，2026-07-29 發布）

**更名條目**：
- `fan-fan-2023-05-02.md` → **`le-le-2023-05-02.md`** — 台北市立動物園於 2026-07-29 舉行見面會，由台北市長蔣萬安揭名，上海動物園來的雄性個體「繁繁」正式改名為「**樂樂**」（同批雌性「甜甜」維持原名）。`name` Fan-Fan → **Le-Le**、`chinese` 繁繁 → **樂樂**；舊名保留於 `nicknames: [繁繁]`／`english_variants: [Fan-Fan]` 以利搜尋。內文標題、引言、基本資料表加「原名」列並補亮相經過（月餘檢疫、溫帶動物區企鵝館旁新整修戶外活動場、2024 年臺北上海城市論壇「動物交換」備忘錄背景）。`sources` 補此新聞稿。

**更新條目**：
- `tian-tian-2024-06-23.md` — 指向 `fan-fan-2023-05-02` 的 wikilink 改指 `le-le-2023-05-02` 並註明改名；引言補 2026-07-29 亮相與揭名（甜甜維持原名）；`sources` 補同一新聞稿
- `index.md` — 區塊標題「繁繁（獨立個體）」改為「樂樂（獨立個體）」，連結改指新 slug、說明補原名與揭名日；甜甜列補揭名註記。條目總數不變（795）

**備注**：官方來源（市立動物園新聞稿）可直接採用。園方新聞稿未提及父母資料，`## 家族` 維持「待確認」。羅馬拼音 Le-Le 依既有中國／台灣個體疊字命名慣例（Tian-Tian、Pao-Pao）擬定，園方英文名如日後公布以官方為準。

## [2026-07-31] add | 都江堰小熊貓森林公園 8 隻檔案卡建檔（維護者提供）

**來源**：
- 維護者提供（2026-07-31）—— 名字與性別由維護者確認，暫無官方公告佐證
- 園區基本資料（地址／經營單位）：攜程、大河票務等旅遊資訊彙整

**新增條目**（皆為 `limited-profile` 檔案卡，生日／入園／家系不詳）：
- `tian-tian-dujiangyan.md` — 天天 Tian Tian ♀（⚠️ 與台北 `tian-tian-2024-06-23` 甜甜同拼音）
- `xiao-xiao-dujiangyan.md` — 小小 Xiao Xiao ♀
- `xiao-bai-dujiangyan.md` — 小白 Xiao Bai ♀（⚠️ 與柳州 `xiao-bai`、上海 `xiao-bai-shanghai` 同名）
- `xiao-mi-feng-dujiangyan.md` — 小蜜蜂 Xiao Mi Feng ♀（別名 唐小糖）
- `mai-mai-dujiangyan.md` — 麥麥 Mai Mai ♀
- `qing-tian-dujiangyan.md` — 晴天 Qing Tian ♀
- `xiu-xiu-dujiangyan.md` — 秀秀 Xiu Xiu ♀（⚠️ 與西山 `shuu-shuu-1981` 同名）
- `can-can-dujiangyan.md` — 燦燦 Can Can ♂

**更新條目**：
- `data/zoos.json` — 新登記「都江堰小熊貓森林公園」（四川省成都市都江堰市蒲陽街道華西社區；無官網，座標待補）
- `index.md` — 新增「海外個體（中國・都江堰小熊貓森林公園）」區塊；條目總數更新為 803

## [2026-07-31] add | 讀者回報：Hertfordshire Zoo × Bojnice 一脈 6 筆（含 2026 雙胞胎蘋果籽）

**來源**：
- https://zoobojnice.sk/obrovska-radost-v-nasej-zoo-mame-mladata-pandy-cervenej/ （Bojnice 官方公告，2024-07-24：Bambu 於 6 月 2 日產下兩仔、父為 Mao）
- https://zoobojnice.sk/bambu-nova-obyvatelka-nasej-zoo/ （Bojnice 官方公告，2023-06-09：Bambu 自 ZOO Ljubljana 抵園始末、Mao「快滿 8 歲」）
- https://zoobojnice.sk/uspech-nasho-chovu-ziskal-ocenenie/ （Bojnice 官方公告，2025-06-18：2024 年育幼獲 BÍLÝ SLON 第三名、Mao 10 歲／Bambu 3 歲）
- https://zoobojnice.sk/video-mame-mladata-pandy-cervenej/ （Bojnice 官方公告，2025-07-10：2025-06-03 再產雙胞胎）
- https://www.zoo.si/novice/mladic-macje-pande-prvic-v-zoo-ljubljana （ZOO Ljubljana 官方公告，2022-09-13：Bambu 為該園首隻誕生小熊貓、6 月生、命名由來）
- https://hertfordshirezoo.com/news/meet-nila-hertfordshire-zoos-new-red-panda/ （Hertfordshire Zoo 官方公告，2025-11-12：Nila 抵園、1 歲 5 個月、名字取自 Nila Gurung）
- https://hertfordshirezoo.com/news/ash-the-red-panda/ （Hertfordshire Zoo 官方公告，2024-02-09：Ash 自 Welsh Mountain Zoo 抵園）
- https://hertfordshirezoo.com/news/endangered-red-panda-twins-born/ （Hertfordshire Zoo 官方公告，2026-07-07：Nila × Ash 於 2026-06-03 產下雙胞胎）
- https://www.instagram.com/p/DRHMP_5DEjj/ （回報者提供，Nila 轉園）
- https://www.instagram.com/reel/DakdJ6DtWFw/ ・ https://www.instagram.com/hertfordshirezoo/reel/Dba-5ztpRj_/ （回報者提供，2026 產仔）

**新增條目**：
- `nila-2024-06-02.md` — Nila ♀，生於 2024-06-02（Bojnice，雙胞胎之一），2025-11 移居 Hertfordshire Zoo
- `mao-2015.md` — Mao ♂，Nila 之父，現居 Bojnice；生年 2015 僅依園方三度公布的年齡推定，標 🚧
- `bambu-2022.md` — Bambu（暱稱 Ola）♀，Nila 之母，2022-06 生於 ZOO Ljubljana（該園首隻），2023-04-24 移居 Bojnice
- `ash-hertfordshire.md` — Ash ♂，Nila 之配偶，2024-02 自 Welsh Mountain Zoo 抵 Hertfordshire Zoo；生日不詳故用園簡稱 slug、tags 加 `limited-profile`＋`last_seen`
- `apple-seed-1-nila-2026-06-03.md` — 蘋果籽1號（Apple Seed 1），生於 2026-06-03，Hertfordshire Zoo
- `apple-seed-2-nila-2026-06-03.md` — 蘋果籽2號（Apple Seed 2），生於 2026-06-03，Hertfordshire Zoo

**回報處理**：來自「圖鑑缺漏回報收件匣」的一筆（Nila）。回報所附出生／轉園／生產三組連結逐項核對，
**全部由園方官網證實**（Bojnice、Hertfordshire Zoo 皆為園方一手公告），依「官方來源可直接採用」逕行建檔。
回報內容與官方來源的兩處差異已修正：
1. 回報寫「子女：2026年6月3日出生，未命名」為**單數**，官方公告明載為**雙胞胎兩隻**（園方暱稱 the Little Red twins），故建兩筆蘋果籽
2. 回報未提 Nila 本身是**雙胞胎之一**（Bojnice 2024 年那胎為 `dve mláďatá` 兩隻），已補入家族欄；同胎手足園方未公布名字與性別、去向不明，不建條目

**建檔方式**：兩筆 2026 幼崽走蘋果籽佔位（四項資格全符合——父母皆已建條目、生日確認、尚在世、尚未命名）。
`sex` 留空、tags 不加性別（園方未公布性別）。**⚠️ 1號／2號純為 wiki 暫編**——與桐生那胎不同，
Hertfordshire 官方公告並未區分兩仔（無出生順序、體徵或 RPF ID 可依），命名公布後須依園方對應關係更正。
六筆均無 RPF 收錄，故無 `rpf_id`／`rpf_url`。

**要點**：
- Hertfordshire Zoo **12 年來首次成功繁殖雙胞胎**（上次為 2014），亦為該園 2022 年 Tashi 之後的第一胎；Nila 與 Ash 雙方皆為初次產仔
- Bojnice 一脈連兩年繁殖成功：2024-06-02（Nila 那胎）與 2025-06-03，兩胎皆雙胞胎；2024 那胎為捷克・斯洛伐克動物園「BÍLÝ SLON」2024 年度哺乳類育幼第三名
- 2025-06-03 出生的兩隻園方未公布名字，僅記於 `nila`／`mao`／`bambu` 的家族欄，不建條目
- Bambu 的父母媒體記為 Muka × Magu，園方公告未載 → 標 🚧 待查證、不建祖父母條目（依查證省時原則不另行搜證）
- Hertfordshire 曾與 Ash 同居展區的雌性 Tilly 僅見於園方介紹文，資料不足未建條目

**更新條目**：
- `index.md` — 新增「海外個體（英國・Hertfordshire Zoo ← 斯洛伐克 Bojnice 一脈）」區塊共 6 筆；條目總數更新為 809

**註冊表變更（`data/zoos.json`）**：
- 新增 `Národná zoologická záhrada Bojnice`（斯洛伐克，`en: Bojnice Zoo`）與 `Zoo Ljubljana`（斯洛維尼亞）兩座園
- `Hertfordshire Zoo` 補 `zh`／`location_ja`／`location_zh`，官網由已失效的舊名網域 `pwpark.com` 改為 `hertfordshirezoo.com`，別名補「Paradise Wildlife Park」

**工具變更**：
- `tools/gen_residence.py` — `CFLAG` 與 `_COUNTRY_WORDS` 新增 Slovakia 🇸🇰、Slovenia 🇸🇮（原本無此兩國，居住史表格不會顯示國名與國旗）
- `web/src/lib/data.js` — `COUNTRY_NAMES` 補 `slovenia` 一列（`slovakia` 本已有）
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `hertfordshirezoo.com`、`zoobojnice.sk`、`zoo.si`，並順手補上先前遺漏的 `pairidaiza.eu`（Pairi Daiza 一家的 `sources` 因此本來不顯示於個體頁）；`OFFICIAL_IG_ACCOUNTS` 新增 `hertfordshirezoo`（已核實：園方官網 News & Socials 與頁尾 IG 連結皆指向此帳號）

**備注**：
- 條目總數基準修正——上一批（都江堰 8 筆）的 log 已記為 803，但 `index.md` 頁首當時仍留 795，本次一併校正後為 809（`ls wiki/*.md | wc -l` 減 index／log 驗證相符）

## [2026-08-02] add+fix | 讀者回報：都江堰小熊貓森林公園家系 4 筆更正 ＋ 4 隻新建、5 隻列候補

**來源**：
- 「回報資料更正」收件匣 4 筆（提交 2026-08-01，回報者 `@red.panda.ct`，依據皆為「現場所見」）
- 「圖鑑缺漏回報」收件匣 8 筆（同回報者，同日提交）
- 對照 `Gaia` 於 2026-07-14 提交的都江堰園內名單（該筆列多數個體為性別不明）

**新增條目**：
- `xin-xin-dujiangyan.md` — 心心 Xin Xin ♂，種公；`xiao-mi-feng-dujiangyan`・`xiao-xiao-dujiangyan` 之父
- `yang-yang-dujiangyan.md` — 陽陽 Yang Yang ♂，種公；`mai-mai-dujiangyan` 之父
- `yuan-yuan-dujiangyan.md` — 圓圓 Yuan Yuan ♀，`xiao-mi-feng-dujiangyan` 之母
- `kai-kai-dujiangyan.md` — 開開 Kai Kai ♂，`tian-tian-2022-07-10` 之配偶
- `hei-shuai-dujiangyan.md` — 黑帥 Hei Shuai，**性別不詳**，`xin-xin-dujiangyan` 之子女
- `nian-nian-dujiangyan.md` — 年年 Nian Nian，**性別不詳**，`yang-yang-dujiangyan` 之子女

**重命名**：
- `tian-tian-dujiangyan.md` → `tian-tian-2022-07-10.md` — 補生日 2022-07-10 後依命名規則改 slug；
  `index.md` 之 wikilink 已同步。舊網址 `/p/tian-tian-dujiangyan/` 失效。
  ⚠️ 生日僅有讀者現場確認、無展牌實拍或園方公告，內文標 🚧。

**更新條目**：
- `xiao-mi-feng-dujiangyan.md` — 補父 心心、母 圓圓
- `xiao-xiao-dujiangyan.md` — 補父 心心
- `mai-mai-dujiangyan.md` — 補父 陽陽
- `tian-tian-2022-07-10.md` — 補 `born: 2022-07-10`、配偶 開開、`last_seen` 2026-07 → 2026-08
- `yuan-yuan-chengdu.md` — 補「⚠️ 注意同名」指向新建的都江堰 圓圓
- `xin-xin-dujiangyan.md`・`yang-yang-dujiangyan.md` — 子女表補入 黑帥／年年（見下方裁定）
- `index.md` — 都江堰區塊 8 → 14 隻（♂4／♀8／性別不詳 2）、加註候補 3 隻；條目總數更新為 815
- `data/contributors.json` — `red.panda.ct` 補 note（本批回報內容）

**列入候補名單（`data/cn-candidates.json`，不建條目、不上站）**：
- 多多、歡歡、樂樂 —— 三隻**性別未回報、亦無家系線索**，未達檔案卡建檔門檻
  （CLAUDE.md 2026-07-24「性別必填，不確定就先進 cn-candidates.json」）。

**⚠️ 建檔門檻放寬（維護者 2026-08-02 裁定，已寫進 CLAUDE.md）**：
- 黑帥・年年**性別未回報，仍依維護者指示建檔**，`sex:` 留空、tags 不加性別 tag，
  內文與 index 標「性別不詳」。理由：兩者均有明確父系線索（心心／陽陽），
  比純名字目擊的三隻紮實，留在候補名單反而讓兩位種公的子女表不完整、家系圖斷鏈。
- 據此修訂 `CLAUDE.md`「資料有限個體：檔案卡」的性別門檻：原則仍是性別已知才建檔，
  **例外是「父／母／子女／配偶其中一方已建條目」時性別可留空**；並明訂關係語推定性別的
  規則與界線。家系連結**仍不能**替代「綁定已登記園」硬門檻。詳見 `CHANGELOG.md` 同日條目。
- 網站影響：兩筆會出現在總數與園頁，但不計入任何性別統計（同蘋果籽佔位條目的處理）。

**採用理由與界線**：
- 依 CLAUDE.md 2026-07-24 放寬條款，中國個體**經維護者確認的社群流通資訊即可建檔**，
  不以官方來源為必要條件。本批經維護者核可後逕行採用。四隻新建者性別皆有依據：
  心心・陽陽由「父親」身分、開開由「天天的老公」、圓圓由「母親」身分推定。
- 四隻新建者綁定的 `都江堰小熊貓森林公園` 已登記於 `data/zoos.json`（硬門檻符合）。
- `sources` 一律寫 `讀者回報（@red.panda.ct，現場所見，2026-08-01）`＋`維護者提供（2026-08-02）`，
  無 host 故 `has_official_source` 仍為 false，網站顯示「未經官方佐證」標記——符合兩軸分工。
- **未掛 `unverified`**：本批皆為 2026-08 現場確認在世，屬「在世但無官方佐證」，
  不可為觸發標記而濫掛（CLAUDE.md 兩軸分工）。
- 家系全部標 🚧：園方未公布家系，關係僅有讀者現場觀察，日後官方公告若有出入以官方為準。
- 新建四隻的 `zoos:` 起始年**留空**（`( – 現在)`），未知抵達年不填首次確認年份。

**待辦**：
- 天天生日、四對家系關係俟園方公告或展牌實拍佐證後移除 🚧
- 黑帥・年年查得性別後回補 `sex` 與性別 tag、移除內文「性別待確認」
- 候補 3 隻（多多・歡歡・樂樂）確認性別**或**查得家系連結後即可轉正（門檻已放寬，見上）
- 同批「圖鑑缺漏」尚有 `南通森林野生動物園`（附官網）與早前 `銀基動物王國`・`北京野生動物園`・
  `都江堰熊貓谷` 等動物園缺漏回報未處理，另批辦理

---

## [2026-08-02] add | Kalden（RPF #480）一家：Edmonton Valley Zoo 種公與其父母、四名子女

**來源**：
- https://redpandafinder.com/#profile/480 (Kalden)
- https://redpandafinder.com/#profile/482 (Tae-Bo)
- https://redpandafinder.com/#profile/399 (Leafa)
- https://redpandafinder.com/#profile/434 (Kola)
- https://redpandafinder.com/#profile/481 (Willow)
- https://redpandafinder.com/#profile/485 (Pepper)
- https://redpandafinder.com/#profile/486 (Paprika)

**新增條目**：
- `kalden-2012-06-07.md` — Kalden ♂（RPF #480），生於 2012-06-07 Northeastern Wisconsin Zoo，2013-07-11 移 Edmonton Valley Zoo、2024-11-01 移 Toronto Zoo；既有 `rinzen`（全兄）與 `tango`（子）之連結對象
- `tae-bo-1998-06-27.md` — Tae-Bo ♂🪽（RPF #482，別名 Taebo），1998-06-27 – 2015-09-22，享年 17 歲；Cincinnati 生，歷 Binder Park・Nashville，2003 起定居 Northeastern Wisconsin Zoo；父母 RPF 無記錄
- `leafa-2009-06-11.md` — Leafa ♀（RPF #399，別名 Rifa），生於 2009-06-11 Red River Zoo，現居 Western North Carolina Nature Center；`rinzen`・`kalden` 之母
- `kola-2015-08-24.md` — Kola ♂（RPF #434），Edmonton 生，2019 起居サンディエゴ動物園；`willow` 雙胞胎
- `willow-2015-08-24.md` — Willow ♀（RPF #481），Edmonton 生，經 Prospect Park，2022-12 移 Houston Zoo（日不詳，暫記 12-01 🚧）
- `pepper-2017-07-23.md` — Pepper ♀（RPF #485），Edmonton 生，2019-03-29 移 Red River Zoo
- `paprika-2017-07-23.md` — Paprika ♀（RPF #486），Edmonton 生，經 Toronto，2023-12-17 移 Greater Vancouver Zoo

**更新條目**：
- `rinzen-2011-06-12.md` — 母 Leafa、父 Tae-Bo、全血緣兄弟 Kalden 由純文字改 wikilink
- `tango-2015-07-30.md` — 父 Kalden 改 wikilink；½ 兄弟姊妹 4 隻補 wikilink 並註明母為 Pip
- `pip-2008-05-26.md` — 補配偶 Kalden 與「子女」表（Kola・Willow・Pepper・Paprika）
- `rina-2012-08-02.md` — 引言與子女表補入父 Kalden、補配偶欄
- `yukiko-2005-06-23.md`・`shan-tou-2005-05-10.md` — 子女列中 Leafa 改 wikilink，並加 🚧 親本歸屬註記（見下）
- `index.md` — 新增「海外個體（北美・Kalden 一家）」7 筆；條目總數更新為 822

**🚧 待查證：Leafa 的親本歸屬**：
RPF 同時把 `shan-tou`（#405）與 `yukiko`（#313）列為 Leafa（及 Xiao-Li・Li-Ming・Také・Wei-Da・Taiji・
Mattie 共 7 仔）的親本，但本 wiki 已校訂兩者**皆為 ♀**（RPF 把 Yukiko 標為 ♂，應為誤植）。兩隻母獸
2007–2014 年同居 Red River Zoo，實際父方待官方佐證，暫於兩邊條目與 `leafa` 條目標 🚧。

**未建條目（本批範圍外）**：
- Leafa × Phoenix（#400）在 Lincoln Park Zoo 所生四仔——Clark（#420）、Addison（#421）、
  Waveland（#416）、Sheffield（#417），以純文字記於 `leafa` 與 `kalden` 條目；Phoenix 本身亦未建。
  另需登記 Zoo Boise、Tulsa Zoo 兩座園後才宜補建。

---

## [2026-08-02] add | Poppy（RPF #1438）：多倫多的遺腹女；出生地矛盾由園方新聞稿釐清

**來源**：
- https://www.torontozoo.com/mediaroom/press2024/20240617 （官方：2024-06-13 双子誕生）
- https://www.torontozoo.com/mediaroom/press2024/20240801 （官方：雄仔夭折、Sakura 病況）
- https://www.torontozoo.com/mediaroom/press2024/20241118 （官方：公眾票選命名 Poppy）
- https://redpandafinder.com/#profile/1438 (Poppy／Biggie)

**新增條目**：
- `poppy-2024-06-13.md` — Poppy ♀（RPF #1438，暱稱 Biggie），2024-06-13 生於 Toronto Zoo，現居該園；
  母 `sakura`🪽、父 `arun`；⚠️ 與 `poppy-2019-05-17` 同名（血緣上為表姊妹）

**更新條目**：
- `sakura-2013-07-01.md` — 補 2024 年生產經過與歿因；子女表加 Poppy 與未命名雄仔；移除「未建檔」註記
- `arun-2014-06-28.md` — 同上；子女表加兩筆並註明於 Toronto Zoo 產下
- `poppy-2019-05-17.md` — 加「⚠️ 注意同名」指向新條目
- `kalden-2012-06-07.md` — 補一句：2024-11 抵多倫多後與 Poppy 同居一區
- `index.md` — 「加拿大・Arun × Sakura 一家」補敘述與 Poppy 一列；條目總數更新為 823
- `tools/build_db.py` — `OFFICIAL_HOSTS` 補 `torontozoo.com`、`gvzoo.com`（既有 `sakura`／`arun` 條目
  已引用 gvzoo.com，先前未被認列為官方來源）

**🔎 前案更正（2026-07-08 的「出生地資料矛盾、未建檔」已解決）**：
lineage 記 Sakura 2024-06-13 於多倫多產子，但她 2024-01-26 才自 Greater Vancouver Zoo 抵園、
父方 Arun 仍在溫哥華，故當時判為矛盾而未建檔。多倫多動物園 2024-06-17 官方新聞稿說明：Sakura
是以 AZA SSP「退休」身分入園，離開溫哥華前與舊配偶 Arun 共度繁殖季初期，**抵達多倫多時已懷孕**
（2 月採糞便檢體、3 月測得黃體素升高、6 月 4 日超音波確認胎兒）。故出生地為 Toronto Zoo、
父方確為 Arun，兩者並不矛盾。依 CLAUDE.md「官方來源可直接採用」逕行建檔並更正兩邊條目。

**未建條目**：
- 同胎雄仔（RPF #1437，2024-06-13 – 2024-07-31，未滿六週夭折）園方未命名，依 CLAUDE.md
  「僅以佔位名登錄者暫不上站」不建檔，於 `poppy`・`sakura`・`arun` 三處以純文字記載。

## [2026-08-02] add | アーニャ 建檔（アーヤ 雙胞胎）＋ 導入「其他參考資料」（extra_sources 上站）

**來源**：
- https://www.nhdzoo.jp/diary/index.php?s_keyword=%E3%82%A2%E3%83%BC%E3%83%8B%E3%83%A3&s1_diary_date_y=-1&s1_diary_date_m=-1&s1_diary_date_d=-1&s2_diary_date_y=-1&s2_diary_date_m=-1&s2_diary_date_d=-1
  （日本平動物園 飼育日誌・關鍵字「アーニャ」共 9 筆；2016-06-04「アーニャ(♀)老衰で死亡する」）
- https://www.nhdzoo.jp/diary/index.php?s_keyword=%E3%82%A2%E3%83%BC%E3%83%A4&s1_diary_date_y=-1&s1_diary_date_m=-1&s1_diary_date_d=-1&s2_diary_date_y=-1&s2_diary_date_m=-1&s2_diary_date_d=-1
  （同上・關鍵字「アーヤ」共 8 筆；2016-09-21「午後に倒れ、夕方遅く老衰で死亡…18歳3か月で、国内のレッサーパンダのメスでは最高齢」）
- 維護者提供（2026-08-02）：アーニャ 生日 1998-07-03、歿日 2016-06-04、2012-12-02 轉入日本平

**其他參考資料**（非官方，僅供延伸閱讀）：
- https://mihorinh.exblog.jp/19574101/ — レサパン日和「アーヤ・アーニャ姉妹」（2014-03-16）
- http://shinshin.cocolog-nifty.com/redpanda/2012/11/post-f4a2.html — 徒然レッサーパンダ「秋吉台４姉妹 アーヤ＆アーニャ編」（2012-11-09）
- https://www.youtube.com/watch?v=gL9q-U_pXIE — 日本平動物園 タク・アーヤ・アーニャ（mametube2011）

**新增條目**：
- `a-nya-1998-07-03.md` — A-nya アーニャ ♀，1998-07-03 生於秋吉台自然動物公園サファリランド，
  2012-12-02 移居静岡市立日本平動物園，2016-06-04 老衰歿（享年 17 歲）；母 `kaori-1991-06-18`🪽、
  父 `bau-bau-1994-07-11`🪽、雙胞胎 `a-ya-1998-07-03`🪽。無 RPF profile，rpf_id 留空

**更新條目**：
- `a-ya-1998-07-03.md` — 補日本平飼育日誌為官方來源、歿因老衰與「國內最高齡雌性」記載；
  母 Kaori、雙胞胎 A-nya 由純文字改 wikilink；補 extra_sources 三筆
- `kaori-1991-06-18.md` — 家族補「子女」列（與 `bau-bau-1994-07-11` 所生 6 女），移除「子女待補」註記
- `bau-bau-1994-07-11.md` — 子女表 A-ya／A-nya 改 wikilink
- `miku-1999-07-21.md` — 母 Kaori、姊妹 A-ya／A-nya 改 wikilink
- `index.md` — 「2026-06-25 第三批補漏」表加 A-nya 一列、A-ya 說明補雙胞胎與歿因；條目總數更新為 824

**⚠️ 待查證**：
- 轉入日本平的日期兩邊不一致——`a-nya` 依維護者提供記 2012-12-02、`a-ya` 既有記載為 2012-12-12。
  雙胞胎應為同日轉園。園方飼育日誌無入園紀錄（關鍵字「秋吉台」0 筆），最早於 2012-12-17 記到
  兩姊妹已在園內與シュウシュウ相親。兩條目均已加註，待官方資料釐清後統一

**流程／工具變更（見 CHANGELOG）**：
- 導入「其他參考資料」政策：部落格、YouTube 等非官方連結一律留存於 frontmatter `extra_sources`，
  不進 `sources`（避免污染 `has_official_source` 判定）。`SCHEMA.md` 新增〈sources 與 extra_sources
  的分工〉一節、`CLAUDE.md` 於「官方來源可直接採用」補一則原則
- `web/src/components/Panda.astro` — 新增「其他參考資料」區塊（列於「來源」下方）：值為 URL 者
  顯示網域並連結（`rel="noopener nofollow"`），純文字說明（如讀者實拍展牌）原樣顯示不連結
- `pipeline/src/i18n/*.json` — 五語各補 `sec_extra_sources`、`extra_sources_note` 兩個 key

---

## [2026-08-02] add | 補齊 Kaori（RPF #495）待補的子女：Non 與 Riku

**來源**：
- https://redpandafinder.com/#profile/569 (Non ノン)
- https://redpandafinder.com/#profile/570 (Riku リク)
- https://redpandafinder.com/#profile/495 (Kaori 香・子女關係)

**背景**：`kaori-1991-06-18` 條目原註記「於 lineage 另記有數名子女（待補）」。核對 RPF 資料集，
Kaori 與 `bau-bau` 育有 6 女、無雄仔，其中 4 隻（`a-ya`・`a-nya`・`riku`・`miku`）已有條目，
本批補上缺漏的 2 隻。

**新增條目**：
- `non-1996-07-05.md` — Non ノン ♀🪽（RPF #569），1996-07-05 – 2014-10-21，享年 18 歲；
  Kaori × Bau-Bau 之長女，終生居秋吉台自然動物公園サファリランド，未曾轉園
- `riku-1999-07-20.md` — Riku リク ♀🪽（RPF #570），1999-07-20 – 2015-10-12，享年 16 歲；
  秋吉台生，2012-12-21 移仙台市八木山動物公園（時稱セルコホーム ズーパラダイス八木山）；
  與 `miku` 為雙胞胎（登錄生日相差一天，7/20 與 7/21，依來源原樣保留）

**更新條目**：
- `kaori-1991-06-18.md` — 移除「子女待補」註記，改列完整「### 子女」表（6 女）
- `bau-bau-1994-07-11.md` — 移除「Non・Riku 尚未建檔」註記，子女列全數改 wikilink
- `miku-1999-07-21.md` — 雙胞胎 Riku 改 wikilink，補 2012 年 12 月四姊妹分別轉園之背景
- `a-ya-1998-07-03.md`・`a-nya-1998-07-03.md` — 姊妹列 Non・Riku 改 wikilink
- `non-2003-07-25.md`・`non-2009-06-19.md`・`riku-2004-07-13.md` — 補「⚠️ 注意同名」交叉指向
- `index.md` — 西山家族區補 Non・Riku 兩列；條目總數更新為 826

**未建條目**：
- Kaori 的三女（RPF #571，1997-06-30 – 2005-11-05，♀）於來源中**未載名字**（`(no name)`／`(無名)`），
  依 CLAUDE.md「僅以佔位名登錄者不建檔」不建立條目，於 `kaori`・`bau-bau`・`non` 三處以純文字記載。
  其居住史為：秋吉台生 → 2000-03-09 高知県立のいち動物公園 → 2005-02-26 九十九島動植物園森きらら。

**🚧 待查證**：兩筆新條目的生卒與居住史目前僅有 RPF／redpanda-lineage 為據，尚無園方一手來源。

---

## [2026-08-02] fix | `maple-2022-06-14` 移除 lineage 帶入的漢字名「松楓」

**更新條目**：
- `maple-2022-06-14.md` — 移除 frontmatter `japanese: 松楓`，標題由「Maple（松楓）」改為「Maple」
- `mei-mei-2022-06-14.md` — 雙胞胎欄移除「松楓」
- `index.md` — 該列說明由「Maple 松楓」改為「Maple」

**理由**：Maple（RPF #1405）為加拿大 Greater Vancouver Zoo 出生、現居 Granby Zoo，
**無任何日本居住史**，依 CLAUDE.md 資料來源原則「lineage/RPF 的 `ja.name` 是機械轉寫，
僅有日本居住史的個體才採用為 `japanese`」，此名不該收；其漢字形式亦非園方或維護者給的中文名，
故直接移除、不轉入 `chinese`。網站個體頁（/p/maple-2022-06-14/）先前因此顯示中文名，已一併消除。

**全庫掃描**：以「非日本園居住史 + `japanese` 為純漢字（無假名）」為條件掃過 823 篇，
僅此一筆，其餘無同類殘留。

---

## [2026-08-02] update | `yuu-yuu-1987-05-31` 補漢字名「友友」

**來源**：
- 維護者提供（2026-08-02）

**更新條目**：
- `yuu-yuu-1987-05-31.md` — `japanese` 由「ユーユー」改為「友友, ユーユー」；標題改為「Yuu-Yuu（友友 / ユーユー）🪽」；`sources` 補「維護者提供（2026-08-02）」
- `index.md` — 該列說明由「Yuu-Yuu ユーユー」改為「Yuu-Yuu 友友 ユーユー」

**備注**：本個體生於長野市茶臼山動物園、終老鯖江市西山動物園，有日本居住史，
故漢字名依維護者提供收為 `japanese`（非 `chinese`）。wiki 內文多處早已以「西山友友」稱之，
惟 frontmatter 未收，網站個體頁因此未顯示漢字名，此次補齊。
其餘條目（子女／手足頁）中寫作「（ユーユー）」處暫未動。

---

## [2026-08-02] update | 全庫統一 `yuu-yuu-1987-05-31` 寫法為「友友 ユーユー」

承上一筆補漢字名，將 wiki 內指向該個體、原寫作「（ユーユー）」的 14 處一併改為「（友友 ユーユー）」。

**更新條目**（父／配偶／子女表等提及處）：
- `chao-chao-1991-06-18.md`・`chii-chii-1989-06-30.md`・`chun-chun-1992-06-22.md`・`hana-1990-06-29.md`・
  `hoa-hoa-1982-06-15.md`・`i-i-nagano.md`・`kaori-1991-06-18.md`・`kusu-1991-06-24.md`・`lili-1986-07-05.md`・
  `ran-ran-1987-07-26.md`・`sabatarou-1992-06-22.md`・`sui-sui-1989-06-29.md`・`ten-ten-1989-06-26.md`・
  `yuu-yuu-1987-07-07.md`
- `yuu-yuu-1987-05-31.md` — 「⚠️ 注意同名」擴充，明列 `yuu-yuu-2014-07-27`（漢字同為友友）、`yuu-yuu-2011-05-28`（渝渝）、`yuu-yuu-1990-06-25`（勇勇）、`yuu-yuu-1987-07-07`
- `yuu-yuu-2014-07-27.md` — 「⚠️ 注意同名」補上 `yuu-yuu-1987-05-31`（漢字同為友友）

**發現**：`yuu-yuu-2014-07-27`（RPF #224，♀，安佐）的 `japanese` 早已是「友友, ユーユー」，
故本 wiki 現有兩隻漢字名同為「友友」的個體（1987 西山♂ 與 2014 安佐♀），已於兩頁互相標註。
log 內既有的歷史敘述（含 2026-07 那筆「其餘寫作 ユーユー 的條目皆指西山…」）不追改。

---

## [2026-08-02] update | 日本個體：把「參照了卻在站上看不到」的連結全部救回

盤點日本個體後發現三類「有參照、無連結」的情形，一併處理。網站個體頁的來源區塊只顯示官方來源、
`extra_sources` 才顯示非官方連結，故非官方連結若誤放 `sources` 會被 `build_db` 靜默丟棄、讀者完全看不到。

**A. `extra_sources` 的連結寫在文字說明行末（整行被當純文字、不做連結）**

- `ouji-kobe.md` — 展牌說明與 cocolog 部落格連結拆為兩筆。網站判斷連結的規則是「整行以 http(s):// 開頭」

**B. 非官方連結誤置 `sources` → 移入 `extra_sources`（連結內容不變，行末加 YAML 註解記標題）**

- 北のレッサーパンダ日記（釧路記念誌年表轉載）9 筆：`ayumi-1991-07-27`・`cha-1997-07-27`・`hajime-1991-07-27`・
  `ikura-1996-07-09`・`kuro-1997-07-27`・`marimo-1995-07-04`・`pam-1976-08-19`・`sabatarou-1992-06-22`・`tara-1995-07-04`
- 4travel 旅行記（目擊記錄性質）4 筆：`ron-ron-2002-06-28`・`ten-ten-1997-06-18`・`shin-shin-2003-07-15`（2 筆）・`sora-2002-06-24`
- 新聞報導 7 筆：`ai-ai-1984`・`yuu-yuu-1983`（四国新聞）、`anko-2013-06-22`（毎日）、`fuuka-2006-06-02`・
  `nanako-2025-07-07`（朝日）、`apple-seed-shin-fa-2026-05-27`（熊本日日）、`shun-shun-2007-07-01`（鹿児島経済）
- 同好整理／個人社群 8 筆：`chip-2001-06-19`・`momotaro-1997-07-17`（reddishpanda）、`fu-fu-2014-06-22`・
  `yan-yan-2014-06-22`（redpandapedia）、`rai-rai-2014-07-05`（レサパン日和）、`cha-cha-1992-07-17`（popncall）、
  `kusu-1991-06-24`（日文維基）、`lili-1986-07-05`（code4fukui 開放資料）
- `ichiro-2014-07-06` — X 個人帳號貼文與 IG reel 2 筆（該帳號 2026-07 已確認非園方）
- `tara-1995-07-04` — 另含都議活動報告、sopitas 報導

**C. 內文有參照、frontmatter 未收**

- `franken-2012-06-11` — 備注的 `@otenba_redpanda`（個人拍攝帳號）收入 `extra_sources`
- `mulan-2019-06-07` — 父「Rai-Rai」為純文字，改為指向 `rai-rai-2014-07-05` 的 wikilink

**D. 其實是官方、卻沒被來源分類器認出（改工具，見 CHANGELOG）**

- `apple-seed-rii-rii-2026-06-28`（羽村官網＋官方 IG）、`kirara-2002-06-29`・`mutan-2014-06-19`（鯖江市西山動物園）、
  `asahi-2015-06-29`（横浜八景島 PR TIMES 新聞稿）、`ten-ten-1997-06-18`（東北サファリパーク園內家系圖照片）、
  多摩官方個體名單轉載（`hana-2001-07-13`・`hana-hana`・`kou-kou-1997-06-20`・`naka-naka`・`nana-2001-07-13`・
  `noa-2004`・`ryu-ryu-1990`・`ryuunosuke-1999-07-27`）
- IG 短形式 `/p/XXXX/` 補回官方帳號的完整形式：`apple-seed-hinagiku-2026-07-16`（maruyamazoo_official）、
  `lian-2020-07-20`・`apple-seed-1-lian-2026-06-19`・`apple-seed-2-lian-2026-06-19`・`ravi-2022-06-14`（seoulgrandpark）

**備注**：`hajime-1991-07-27` 的 Internet Archive 快照連結原本就在 `sources`（未遺失）；
本次移出的只有該條目的 fc2 部落格。RPF／lineage 連結留在 `sources` 不動（線索性質，網站另以 RPF 欄呈現）。
非日本個體亦有同類情形（Calgary／Roger Williams 等），本批未處理。

---

## [2026-08-02] update | 次郎的父母查明：母親「愛愛」正名並建條目（RPF #764）

**起點**：維護者提供市川市動植物園開園 30 週年展板／「大人のための動物講座」的參觀紀錄（同好部落格，
2018-03-27），詢問次郎的父母。該文其實未載次郎的父母，只記「次郎自茶臼山來園」；但 wiki 內部
2026-07-30 的 RPF 比對成果（記在 `hoa-hoa-1982-06-15` 與 `i-i-nagano`）早已指出父為陽陽、母為
RPF #764「無名之雌」，只是 `jirou-1990-07-06` 一直沒同步。維護者並確認 **#764 即西山友友的同胎手足
「愛愛」**，據此正名建檔。

**來源**：
- https://redpandafinder.com/#profile/764 （愛愛，RPF 記為 (no name)）
- https://redpandafinder.com/#profile/750 （太郎 タロ）
- https://redpandafinder.com/#profile/751 （アイコ）
- https://redpandafinder.com/#profile/754 （次郎）
- 維護者提供（2026-08-02：#764 名為愛愛；次郎之父為陽陽）
- http://blog.livedoor.jp/maiaitsuki/archives/1070532051.html （非官方，列入各條目 `extra_sources`）

**新增條目**：
- `ai-ai-1987-05-31.md` — 愛愛 アイアイ（RPF #764），生於 1987-05-31、歿 2003-05-13，
  長野市茶臼山動物園 → 鯖江市西山動物園；花花×誼誼之女、西山友友之雙胞胎、次郎／太郎／アイコ之母
- `aiko-1989-07-01.md` — アイコ Aiko（RPF #751），生於 1989-07-01、歿 2001-01-19，茶臼山 → 浜松市動物園；
  太郎之雙胞胎，與舅舅 `genki-1989-06-30` 配對育有一女 Yuu（1994）

**更新條目**：
- `jirou-1990-07-06.md` — 母欄由「（無記錄）」改為 `ai-ai-1987-05-31`、父欄 You-You 改為 `you-you-1987-07-26`
  的 wikilink；補手足、外祖父母、1991 年市川⇄茶臼山交換說明；加 `extra_sources`
- `tarou-1989-07-01.md` — 確認即 RPF #750（生日・出生園・移園日三項與王子動物園官方個體アルバム完全一致），
  補 `rpf_id: 750`、父母（陽陽×愛愛）與雙胞胎 アイコ；歿日仍採官方 2009-10-25（RPF 記 10-15，不採用）
- `you-you-1987-07-26.md` — 子女由條列改為表格（含母欄），タロ・アイコ 由「無條目」改為 wikilink
- `yuu-yuu-1987-05-31.md` — 雙胞胎「無名」改為 `ai-ai-1987-05-31`
- `i-i-nagano.md` — 子女表「無名之雌」改為 `ai-ai-1987-05-31`
- `hoa-hoa-1982-06-15.md` — 愛愛該列補齊資料並連往新條目；13 隻中已建條目數 10 → 11；改寫 13／14 差額備注
  （差額收斂為「名單的佐世保愛愛是否即 #764」一個問題，🚧 待官方釐清）
- `genki-1989-06-30.md` — 補配偶 `aiko-1989-07-01`（外甥女）、全血緣手足補愛愛與鈴；女兒 Yuu 補母欄
- `rin-rin-1989-06-21.md` — 父母改為 wikilink、補配偶次郎與弟妹；加 🚧 備注：30 週年展板記其漢字名為
  「鈴鈴」、與現用「怜怜」不同，非官方故暫不改
- `sei-sei-1986.md`・`shin-shin-1986.md` — 子女表補生日（愛愛／鈴鈴 1989-06-21、美美／勇勇 1990-06-25、
  健健 1991-06-21、奈奈 1992-06-23、雄雄 1993-07-01），加來源備注與 `extra_sources`
- `yuu-yuu-1990-06-25.md` — 手足補生日、補 1991 年與次郎交換的說明與 `extra_sources`
- `index.md` — 新增 `ai-ai-1987-05-31`・`aiko-1989-07-01`；花花家族新增「孫輩（愛愛×陽陽）」小節；
  次郎・太郎列補說明；條目總數 826 → 828

## [2026-08-02] update | アイコ 的漢字名確認為「愛子」

維護者提供（該個體有日本居住史，故收入 `japanese`；RPF #751 的 `ja.name` 僅記片假名）。

**更新條目**：
- `aiko-1989-07-01.md` — `japanese` 由「アイコ」改為「愛子, アイコ」，標題改為「Aiko（愛子 / アイコ）」，備注記來源
- `ai-ai-1987-05-31.md`・`tarou-1989-07-01.md`・`jirou-1990-07-06.md`・`you-you-1987-07-26.md`・
  `yuu-yuu-1987-05-31.md`・`genki-1989-06-30.md`・`index.md` — 名稱顯示改為「愛子 アイコ」

（slug 依「名字-生日」規則由 `name: Aiko` 決定，不受漢字名影響，無需 rename。）

## [2026-08-02] update | 都江堰 天天 之母為 小白（讀者回報）

讀者 `@red.panda.ct` 現場所見回報：`tian-tian-2022-07-10`（天天）之母為都江堰小熊貓森林公園的
`xiao-bai-dujiangyan`（小白），且天天即於該園出生。園方未公布家系，故仍標 🚧 待查證。

**來源**：
- 讀者回報（@red.panda.ct，現場所見，2026-08-02；母親與出生園）
- 維護者提供（2026-08-02）

**更新條目**：
- `tian-tian-2022-07-10.md` — 母欄由「不詳」改為 `xiao-bai-dujiangyan`；確認園內出生，
  `zoos:` 起日由留空改為 2022-07-10（🐣 名實相符）、居住史表同步；引言改寫、待查證項收斂為「父不詳＋官方來源」
- `xiao-bai-dujiangyan.md` — 新增「### 子女」表（天天，另一方親本不詳）；引言補「天天之母、至少 2022 年即在園內」；
  加 `birth_zoo: unknown`（出身不明，居住史不再誤標 🐣 出生地）
- `index.md` — 天天列補「小白之女（園內出生）」、小白列補「天天之母」；都江堰段落家系來源日期補 08-02

## [2026-08-03] update | 安佐 1987 年重慶來源 3 隻：來源園具體化為重慶動物園

讀者 `楊桃` 回報安佐動物公園 `ai-ai-1984`（愛愛）的來歷（四国新聞 2004-02-16 報導安佐 2004-02-16
發表：「愛愛は３歳だった１９８７年、広島市の友好都市の中国・重慶市から贈られた」）。該筆內容與
2026-07-28 建檔時所採用者相同、資料本身已在條目內（生年 1984 推定、1987-07-12 來園、2004-02-13 歿
19 歲・日本最高齡，四国新聞連結已在 `extra_sources`），故無新增事實。

**依維護者裁定，將來源由「重慶市」具體化為「重慶動物園」**：官方來源僅載「重慶市から贈られた」、
未指名設施，此為維護者確認之補充，記為 `維護者提供（2026-08-03）`。作法為**在居住史加一站來源園、
不改出生地**——`zoos:` 前置 `Chongqing Zoo ( – 1987-07-12)`（抵達年不詳故起始留空），
`birth_zoo` 三隻**均維持 `unknown`**（是否生於該園無佐證，居住史亦因此不誤標 🐣）。

**來源**：
- 讀者回報（楊桃，四国新聞 2004-02-16 報導安佐動物公園發表，2026-08-02）
- 維護者提供（2026-08-03：來園前所在地為重慶動物園）

**更新條目**：
- `ai-ai-1984.md`・`yuu-yuu-1983.md`・`mei-mei-hiroshima.md` — `zoos:` 加 Chongqing Zoo 一站、
  `sources` 增列維護者提供、內文與 `## 家族` 的「中國重慶市」改為「重慶動物園」、
  🚧 待查證改寫為「來源園已具體化、出生設施仍不明故 `birth_zoo: unknown`」；居住史表由
  `gen_residence.py` 重生
- `data/zoos.json` — Chongqing Zoo 的 `zh` 由 `null` 補為「重慶動物園」

（回報者 `楊桃` 已在 `data/contributors.json` 致謝名單，不重複列。）

## [2026-08-03] add | Dusk 一家七筆：`udaya` 之父確認，卡加利時期子女與 Dusk 兄弟補齊

讀者回報 `udaya-2019-06-20` 之父為 `dusk`，附 Calgary Zoo 官方訃告〈Farewell to an Old Friend〉。
該訃告明載「his daughter, Udaya」，屬園方官網一手來源，依「官方來源可直接採用」逕行採用。

**回報值與來源的出入（以來源為準）**：回報稱 Dusk 歿於 2023-01-16，惟該日為訃告**發稿日**，
原文寫「last week we said goodbye」；RPF #447 記歿日 2023-01-10，與官方敘述相符，故採 2023-01-10。
回報稱「2004 年出生於 Assiniboine Park Zoo」，官方僅寫「Born in 2004 in Winnipeg」未指名設施，
RPF 居住史則明確記為 Assiniboine Park Zoo（2004-06-02 起），兩者一致故採用。

**連帶釐清**：官方訃告稱 Dusk 一生育有六隻幼獸，與 RPF 所列 Dash・Usha・Khairo・Chiya・Nisha・Udaya
六隻完全吻合，可交叉佐證。`zeyar-2007-06-21` 兄弟表中的 Dusk 亦確認即為 #447（RPF 兄弟名單相同），
先前的同名疑慮解除。

**來源**：
- https://www.calgaryzoo.com/news/farewell-to-an-old-friend/ （Calgary Zoo 官方訃告，2023-01-16）
- https://redpandafinder.com/#profile/447 (Dusk)
- https://redpandafinder.com/#profile/460 (Usha)、#459 (Khairo)、#458 (Chiya)、#462 (Nisha)
- https://redpandafinder.com/#profile/590 (Rover)、#473 (Rusty)
- 讀者回報（未留暱稱，回報資料更正表單，2026-08-03）

**新增條目**：
- `dusk-2004-06-02.md` — Dusk（RPF #447），2004-06-02 生於 Assiniboine Park Zoo，
  經 Granby Zoo（2005–2012）、Assiniboine（2012–2013）於 2013-10-30 入 Calgary Zoo，
  2023-01-10 歿於卡加利、享年 18 歲；`sources` 為園方訃告＋RPF
- `usha-2015-07-15.md` — Usha（RPF #460）♀，`sakura` × `dusk` 之女，Calgary 生，2016 移居 Greensboro Science Center
- `khairo-2016-06-21.md` — Khairo（RPF #459）♂，`chiya` 之雙胞胎，2017 移居 Northeastern Wisconsin Zoo、2021 轉 Red River Zoo
- `chiya-2016-06-21.md` — Chiya（RPF #458）♂，別名 Chiyo，現居 Northeastern Wisconsin Zoo
- `nisha-2017-06-13.md` — Nisha（RPF #462）♀，2018 移居 Zoo New England Franklin Park Zoo
- `rover-2005-05-16.md` — Rover（RPF #590）♂ 🪽，Dusk 之弟、`rusty` 之雙胞胎，2005–2015，`homer-2012-06-11` 之父
- `rusty-2005-05-16.md` — Rusty（RPF #473）♂ 🪽，Dusk 之弟、`rover` 之雙胞胎，2005–2023

**未建檔（資料不足）**：Dusk 另一兄弟 Rufus（RPF #426）**無任何居住史**，
依維護者裁定維持純文字、不建檔案卡（缺「綁定已登記園」硬門檻）。
其 profile 頁因缺 `location` 欄位而渲染失敗，改由 `/export/redpanda.json` 取得生日 **2003-06-18**，
已回填至各條目的純文字提及處。父母（#601／#602）與雙胞胎（#603）皆為 (no name) 佔位名，同樣不建。

**更新條目**：
- `udaya-2019-06-20.md` — 父由「不詳（🚧 待查證）」改為 `dusk-2004-06-02`；補同父母兄姊四隻與
  ½ 兄 `dash`、½ 妹 `poppy`；`sources` 增列 Calgary Zoo 官方訃告
- `sakura-2013-07-01.md` — 子女表補 `usha`／`khairo`／`chiya`／`nisha` 四列（另一方親本均為 `dusk`）、
  `udaya` 的另一方親本由「不詳」改為 `dusk`；配偶欄補 Calgary 時期的 `dusk`；
  移除「卡加利時期其他子女亦未建檔」的待辦註記
- `dash-2012-06-06.md`・`kayah-2007-06-11.md`・`madeline-2015-06-22.md`・`xia-2013-07-01.md`・
  `zorro-2013-07-01.md` — 純文字「Dusk（RPF #447）」改為 wikilink
- `zeyar-2007-06-21.md` — 兄弟表的 Dusk／Rover／Rusty 改 wikilink，並補生卒年與雙胞胎關係
- `homer-2012-06-11.md` — 父由「Rover 🪽（#590，無條目）」改為 wikilink
- `maple-2022-06-14.md`・`mei-mei-2022-06-14.md`・`poppy-2024-06-13.md` — 半血緣兄姊列表補上
  卡加利時期四隻同母異父手足
- `index.md` — 新增「海外個體（加拿大／美國・Dusk 一家）」一節共 7 列；`dash`／`udaya` 說明改 wikilink；
  條目總數更新為 835
- `data/zoos.json` — 補 Greensboro Science Center 與 Zoo New England Franklin Park Zoo 的
  `location_ja`（原為 null，居住史地點欄會空白）；兩園 `zh` 仍留 null，待維護者定名

（回報者未留暱稱，`data/contributors.json` 不列。）

## [2026-08-03] fix | 26 筆條目的非官方連結由 `sources` 移入 `extra_sources`

承同日 `CHANGELOG.md`「來源分類器」條目：`audit.py` 新增的「sources 有非官方 host」檢查跑出 16 個 host。
逐一判定後，**全部屬「本來就非官方、應改放 `extra_sources`」**（非白名單漏掛），故依 `SCHEMA.md`
〈sources 與 extra_sources 的分工〉搬移，並在行末以 YAML 註解補記出處與看點。連結一律留存、未刪除。

搬移的 16 個 host：新聞媒體（`turnto10.com`、`wpri.com`、`cbc.ca`、`ytn.co.kr`、`hkcd.com`、
`timeout.com.hk`、`news.cnhubei.com`、`finance.sina.com.cn`、`m.sohu.com`、`wxrb.com`、
`zsrbapp.zsnews.cn`、`guinnessworldrecords.com`）、保育 NGO（`redpandanetwork.org`）、
園方支援團體（`buildingourzoo.com`）、非園方粉專轉載（`facebook.com/Bangkok.Pattaya`）、
無法辨識發文者的 FB 連結（`facebook.com/photo?fbid=…`）。

**更新條目（26 筆，共搬移 31 條連結）**：
`bagel-2024-07-12`・`bei-bei`・`cong-cong-2008-06-11`・`dawa-2012-12-20`・`fred-2024-07-07`・
`george-2024-07-07`・`hana-2023`・`hashi-2022`・`huan-xi-tuo-2020-05-10`・`karma-2012-12-20`・
`katara-2025-07-04`・`kendji-2015-06-22`・`li-zi-2008-06-15`・`ma-tuan-2023-06-16`・`mei-mei-wuhan`・
`meng-xia-2025-07-17`・`nan-nan-2024-07-02`・`nima-2012-12-20`・`nuo-mi-ji-2020-05-10`・
`ravi-2022-06-14`・`tayla-2007-12-08`・`taylor-1998`・`xia-wa`・`you-you`・`zan-2020-05-25`・
`zhong-xia-2025-07-17`

**待補官方來源（4 筆，搬移後 `sources` 已空，audit 列 ⚪）**：
`hana-2023`・`hashi-2022`・`katara-2025-07-04`・`taylor-1998`。
這幾隻原本就只有新聞／轉載佐證，搬移只是讓「無官方佐證」誠實顯示出來，非資料退步。

**`buildingourzoo.com` 依維護者裁定認列為官方**（同日稍後）：Valley Zoo Development Society 是
Edmonton Valley Zoo 的官方支援團體，園內動物資訊由園方提供、以第一人稱發布，比照 Calgary Zoo 的
Wilder Institute 辦理。已補進 `OFFICIAL_HOSTS`，並把 `fred-2024-07-07`・`george-2024-07-07` 的該連結
由 `extra_sources` 移回 `sources`（兩筆 `has_official_source` 轉 true、來源區塊恢復顯示）；
兩條目的 CBC 報導仍留在 `extra_sources`。

**`li-zi-2008-06-15` 的 FB 連結經維護者確認為官方，已認列**（同日稍後）：該貼文出自
**香港海洋公園 Ocean Park Hong Kong 官方專頁**，2013-06-16 發布的栗子訃告（園方載明栗子於前一日中午
在後勤設施進食竹子時無徵兆倒下，解剖初判為腦梗塞或急性心臟衰竭），與條目所記歿日 2013-06-15 及
RPF #933 一致。作法：
- 網址由 `facebook.com/photo?fbid=10151628367866390` 改存**含 vanity 的正規形式**
  `facebook.com/oceanparkhk/photos/10151628367866390`（實測可解析至同一則貼文），並移回 `sources`
- `OFFICIAL_FB_PAGES` 補 `oceanparkhk`
- 內文備注改寫：歿日由「非官方、🚧 待查證」改為「有官方佐證」並補死亡經過；生日與居住史仍標 🚧

（作法沿用既有慣例：FB 是共用網域、不可整域列白名單，故存 source 時務必用含 vanity 的正規網址，
`?fbid=` 形式不含專頁識別、離線分類器無從比對。）

## [2026-08-03] add | 都江堰小熊貓森林公園：多多、慢慢 2 筆建檔（維護者授權之門檻例外）

**來源**：
- 讀者回報（Gaia，都江堰園內名單，2026-07-14）——該名單列多數個體為性別不明
- 讀者回報（`@red.panda.ct`，現場所見，2026-08-01）——多多的現場確認
- 維護者提供（2026-08-03）

**新增條目**：
- `duo-duo-dujiangyan.md` — 多多 Duo Duo，**性別不詳**，`man-man-dujiangyan` 之親代
- `man-man-dujiangyan.md` — 慢慢 Man Man，**性別不詳**，`duo-duo-dujiangyan` 之子女

**更新條目**：
- `duo-duo-hangzhou.md` — 補「⚠️ 注意同拼音」指向新建的都江堰 多多（杭州為「朵朵」、漢字不同）
- `index.md` — 都江堰區塊 14 → 16 隻（♂4／♀8／性別不詳 4）、候補改記 3 隻；
  `duo-duo-hangzhou` 該列補同拼音警語；條目總數更新為 837
- `data/cn-candidates.json` — 移除「多多」（已轉正）；新增「緩緩」為獨立一筆
  （原僅寫在多多的 note 裡，易遺漏）

**⚠️ 建檔門檻例外（維護者 2026-08-03 裁定）**：
兩隻**性別皆不詳**，且唯一的家系連結是**彼此**——多多靠子女慢慢、慢慢靠親代多多。
CLAUDE.md 2026-08-02 的性別例外原文是「有**已建條目**的家系連結時性別可留空」，
立意在「別讓既有條目的子女表殘缺、家系圖斷鏈」；本案兩隻同時新建、沒有既有條目會斷，
嚴格照文字並不成立（與黑帥・年年不同——那兩隻的父心心／陽陽是既有且性別已知的條目）。
經提示後由維護者授權建檔，屬**個案例外，未修改 CLAUDE.md 規則**。日後若要常態化，
需另行修訂「性別門檻」一節並說明 bootstrap 的界線。

**⚠️ 已知副作用：家系邊不會進 DB**：
`build_db.py` 由「子女表」反推 `parent_child` 時，需靠**親代的性別**決定 `mother`／`father`
（`schema.sql` 的 `parent_type` CHECK 只允許這兩值）。多多性別不詳 → `ptype` 為 None →
該筆關係被丟棄。故多多與慢慢的親子關係目前**只存在於 wiki 內文**，不會出現在 `redpanda.db`、
網站個體頁的家族欄與家系圖。這是本站第一次出現「性別不詳的親代」（黑帥・年年是性別不詳的**子女**，
親代性別已知故不受影響）。要讓這類關係上站，需擴充 `parent_type` 容許 `parent` 一值並同步
`export_json` 與前端——留待維護者裁定，本次未改工具。慢慢的家族欄因此寫「親代：」而非「父：／母：」。

**其他**：
- 樂樂・歡歡・緩緩三隻仍留候補（`data/cn-candidates.json`），性別未確認、家系線索不足
- 緩緩的佐證強度與慢慢相同（同一份名單、同為多多之子女），僅因不在本次授權範圍內而未建檔
- 兩隻均無 RPF 收錄，故無 `rpf_id`／`rpf_url`；生日不詳故 slug 用園簡稱 `-dujiangyan`

## [2026-08-03] update | 黑帥 性別回補 ♂

**來源**：維護者提供（2026-08-03）

**更新條目**：
- `hei-shuai-dujiangyan.md` — `sex: male`、tags 加 `male`；引言「性別不詳」改 ♂；
  內文「心心之子女」改「之子」；🚧 待查證移除「性別」一項，並註明性別由維護者確認、
  非由名字「帥」字推定（原條目明載不可如此推定，避免日後誤讀為推定值）；
  `sources` 補一行「維護者提供（2026-08-03）：性別 ♂」
- `xin-xin-dujiangyan.md` — 子女表下方註記由「黑帥性別待確認」改為已確認
- `index.md` — 都江堰區塊性別分布由（♂4／♀8／性別不詳 3）更正為（♂5／♀8／性別不詳 3）；
  黑帥該列性別欄 不詳 → ♂。條目總數不變（837）

**影響**：黑帥本身無子女，故 `parent_child` 邊不受影響（其父 心心 性別本已知，邊一直都在）。
都江堰尚有 3 隻性別不詳：年年、多多、慢慢。

## [2026-08-03] add | Tenzing 一家七筆：舊金山明星個體 Tenzing（原名 Kodari，RPF #697）建檔

讀者透過「圖鑑缺漏」表單回報 San Francisco Zoo 的 `Tenzing`（回報者 Tenzing；附 2 條 IG 連結），
比對後兩條皆為 **San Francisco Zoo 官方帳號 @sanfranciscozoo** 貼文（10 歲生日 reel 與訃報），
依「官方來源可直接採用」逕行建檔。連帶把 RPF 家系上的父母、半血緣兄與四位祖父母中三位補齊
（祖母 `sophia-2002-06-20` 早已有條目，本次補上其與 He-Ping 所出的 Takeo 一支）。

**生日以園方為準**：Sacramento Zoo 園方部落格（2013-07-18 五週齡更新）明載幼獸 "born on June 8th"，
且載明因母親育幼不穩、出生後兩週半改人工哺育、三個半月大時命名 Kodari（尼泊爾邊境城市名）。
RPF 記為 2013-06-01，**不採**；回報者所填 2013-06-08 與園方一致。slug 用官方生日。

**Pili 死訊（RPF 未更新）**：RPF 仍顯示 Pili 在世，實則已於 2026-01-16（週五）人道安樂死，
享年 14 歲——Sacramento Zoo 官方 IG @sacramentozoo 訃報載明甲狀腺疾病長期治療、末期腸胃症狀。
以官方為準記 `died`。

**來源**：
- https://www.instagram.com/sanfranciscozoo/p/DL8Mjksz9_q/ （SF Zoo 官方訃報：Tenzing 12 歲、肉孢子蟲症）
- https://www.instagram.com/sanfranciscozoo/p/CtQJY-XuOUi/ （SF Zoo 官方：Tenzing 10 歲生日 "Hang Ten party"）
- https://www.saczoo.org/imported-blog/posts/red-panda-cub-5-week-update-video （Sacramento Zoo：born June 8th、人工哺育）
- https://www.instagram.com/sacramentozoo/p/DTv2-aEiVFP/ （Sacramento Zoo 官方訃報：Pili，2026-01-16 安樂死）
- https://www.cbsnews.com/sanfrancisco/news/san-francisco-red-panda-tenzing-dies-endangered-species/ （CBS SF，非官方；記 extra_sources）
- https://www.cbsnews.com/sacramento/news/sacramento-zoos-red-panda-pili-dies-at-14/ （CBS Sacramento，非官方；記 extra_sources）
- https://redpandafinder.com/#profile/697 ／ /843 ／ /531 ／ /625 ／ /874 ／ /1226 ／ /793

**新增條目**：
- `tenzing-2013-06-08.md` — Tenzing（原名 `Kodari`，RPF #697）♂ fulgens，2013-06-08 生於 Sacramento Zoo，
  2014-03-24 移居 San Francisco Zoo，2025-07-10 歿於肉孢子蟲症（享年 12 歲）
- `pili-2011-06-17.md` — Pili（RPF #843）♀，2011-06-17 生於 National Zoological Park，
  2012-03-29 移居 Sacramento Zoo，2026-01-16 安樂死（享年 14 歲）；Tenzing 之母
- `takeo-2008-06-29.md` — Takeo（RPF #531）♂，2008-06-29 生於 Denver，終居 Sacramento Zoo、2023-05-10 歿；
  Tenzing 之父、`sophia-2002-06-20` 之子（故為 `carson-2014-07-01`／`willa-2014-07-01` 的 ½ 兄）
- `razz-2011-06-14.md` — Razz（RPF #625，別名 Raz／Dato／Starr）♂，2011-06-14 生於 Mill Mountain Zoo，
  終居 Blank Park Zoo、2025-08-08 歿；Tenzing 半血緣兄（母 Nova）
- `shama-2007-07-01.md` — Shama（RPF #874）♀，2007–2014，Pili 之母（Tenzing 外祖母）
- `tate-2006-06-28.md` — Tate（RPF #1226）♂，2006–2015，Pili 之父（Tenzing 外祖父）
- `he-ping-1998-06-19.md` — He-Ping（RPF #793）♂，1998–2011，Takeo 之父（Tenzing 祖父）

**更新條目**：
- `sophia-2002-06-20.md` — 補配偶 `he-ping-1998-06-19`、子女增列 `takeo-2008-06-29` 與 Amaya（雙胞胎，2008）
- `carson-2014-07-01.md` — ½ 手足清單中 Takeo 由純文字改 wikilink；註記改為「10 隻中僅 Takeo 已建檔」
- `mebo-2023-06-13.md` — 補述在 San Francisco Zoo 與 Tenzing 同居（園方昵稱 Little Mebo）至 2025-07 為止
- `index.md` — 海外個體（美國）新增「Tenzing 一家（Sacramento Zoo → San Francisco Zoo）」小節七列；
  條目總數 837 → 844
- `data/zoos.json` — 補 13 座美國園的 `location_ja`／`location_zh`（Sacramento／San Francisco／
  National Zoological Park／SCBI／Erie／Cape May／Denver／Detroit／Milwaukee／Mill Mountain／
  Blank Park／Hemker／Zoo Knoxville）
- `tools/build_db.py` — `OFFICIAL_HOSTS` 補 `saczoo.org`・`sfzoo.org`；
  `OFFICIAL_IG_ACCOUNTS` 補 `sanfranciscozoo`・`sacramentozoo`

**其他**：
- Tenzing 的全血緣妹妹（2018 生，RPF #1228，登錄名 `Baby`）未及正式命名即夭折，
  依「幼逝寶寶收錄原則」僅以佔位名登錄者不建條目，僅於父母條目內以文字記錄
- `japanese` 一律留空：本家系無日本居住史，lineage 的 `ja.name`（テンジン／コダリ／和平 等）
  為機械轉寫不採；He-Ping 的「和平」疑為中文名，已在條目標 🚧 待維護者確認後再放 `chinese`
- He-Ping 於 2003-01-20 – 2007-11-28 間 lineage 僅記「Zoo Not Found」，該段居住史缺、`zoos:` 留空缺
- Takeo 歿日 2023-05-10 僅 RPF 有載（官方僅佐證「卒於 2023 年」），已標 🚧 待查證；
  Razz、Shama、Tate、He-Ping 四筆亦僅有 RPF 依據，各自條目均標 🚧
- 致謝名單：`data/contributors.json` 新增回報者 `Tenzing`（留了暱稱、本批已採用）

---

## [2026-08-03] add | 都江堰 `bei-bei-dujiangyan`、上海野生動物園 `mao-dou-shanghai-wild`；`nian-nian-dujiangyan` 補性別

**來源**：
- 讀者回報（@red.panda.ct，現場所見，2026-08-01）＋維護者確認（2026-08-03）：都江堰 `bei-bei`（心心之子女）、`nian-nian` 性別 ♂
- 維護者提供（2026-08-03）：上海野生動物園 `mao-dou`（♂）

**新增條目**：
- `bei-bei-dujiangyan.md` — 貝貝 Bei Bei，性別待確認，生日不詳，現居 都江堰小熊貓森林公園；
  父 `xin-xin-dujiangyan`（心心），母不詳。依「檔案卡・性別門檻例外」（有已建條目的家系連結時性別可留空）建檔
- `mao-dou-shanghai-wild.md` — 毛豆 Mao Dou ♂，生日不詳，現居 上海野生動物園；父母不詳。
  無生日故 slug 用園簡稱後綴；因上海有兩座已登記園（上海動物園／上海野生動物園），後綴取 `shanghai-wild` 以免混淆

**更新條目**：
- `nian-nian-dujiangyan.md` — 補 `sex: male` 與 male tag，引言改 ♂，待查證清單移除「性別」
- `xin-xin-dujiangyan.md` — 子女表增列 `bei-bei-dujiangyan`（第四筆），引言與註記同步
- `yang-yang-dujiangyan.md` — 註記改為「年年性別 ♂ 由維護者於 2026-08-03 確認」
- `bei-bei.md` — 補同名提示（銀基 貝貝 ≠ 都江堰 貝貝）
- `index.md` — 都江堰小節新增 `bei-bei-dujiangyan`、年年性別欄改 ♂、心心說明補列子女；
  上海野生動物園小節新增 `mao-dou-shanghai-wild`；銀基 `bei-bei` 列補同名提示；條目總數 844 → 846

**其他**：
- 兩筆新條目皆為 `limited-profile` 檔案卡，`last_seen: 2026-08`、`zoos:` 起始年留空（不知抵達年）；
  維護者確認、現正在世故**不掛** `unverified`；`sources` 無 host 故 `has_official_source` 仍為 false
- `貝貝` 之園別經維護者確認為都江堰（同一回報來源），故符合「綁園」硬門檻；性別查得後回補 `sex` 與性別 tag

---

## [2026-08-04] add | 都江堰 `huan-huan-dujiangyan`（歡歡）、`huan-huan-duo-duo-dujiangyan`（緩緩）；多多補性別 ♀、開開／慢慢補家系

**來源**：
- 維護者提供（2026-08-04）：都江堰 `huan-huan`（歡歡 ♀）；`kai-kai`（♂）× `duo-duo`（♀）之子女 `huan-huan`（緩緩，性別未知）；
  `man-man`（慢慢）之母為 `duo-duo`、父不詳
- 既有佐證沿用：讀者回報（@red.panda.ct，現場所見，2026-08-01；歡歡目擊）、讀者回報（Gaia，園內名單，2026-07-14；緩緩・慢慢為多多之子女）

**新增條目**：
- `huan-huan-dujiangyan.md` — 歡歡／欢欢 Huan Huan ♀，生日不詳，現居 都江堰小熊貓森林公園；
  父母不詳，維護者明示為獨立個體、與開開／多多無家系關係。性別 ♀ 由維護者確認，故自 `cn-candidates.json` 轉正
- `huan-huan-duo-duo-dujiangyan.md` — 緩緩／缓缓 Huan Huan，性別待確認，生日不詳，現居 都江堰小熊貓森林公園；
  父 `kai-kai-dujiangyan`、母 `duo-duo-dujiangyan`。依「檔案卡・性別門檻例外」（有已建條目的家系連結時性別可留空）建檔，
  自 `cn-candidates.json` 轉正

**更新條目**：
- `duo-duo-dujiangyan.md` — 補 `sex: female` 與 female tag，引言改 ♀；配偶增列 `kai-kai-dujiangyan`；
  子女表 `man-man-dujiangyan`（父不詳）＋新增 `huan-huan-duo-duo-dujiangyan`（父為開開）；
  待查證清單移除「性別」，改列「慢慢之父」
- `kai-kai-dujiangyan.md` — 配偶增列 `duo-duo-dujiangyan`（原僅 `tian-tian-2022-07-10`）；
  子女新增 `huan-huan-duo-duo-dujiangyan`；註明兩段配對時序不詳
- `man-man-dujiangyan.md` — 親代由「多多（性別不詳）」改為 母 `duo-duo-dujiangyan`、父不詳（維護者明示）；
  手足 緩緩 由純文字改 `[[wikilink]]`
- `huanhuan-2007-07-03.md` — 補同名提示（台北 歡歡 ♂ ≠ 都江堰 歡歡 ♀）
- `data/cn-candidates.json` — 刪除 `緩緩`、`歡歡` 兩筆（已轉正建檔）；餘 6 筆
- `index.md` — 都江堰小節新增 `huan-huan-dujiangyan`、`huan-huan-duo-duo-dujiangyan` 兩列；
  多多性別欄改 ♀、說明改「開開之配偶；緩緩・慢慢之母」；開開說明改「天天・多多之配偶；緩緩之父」；
  慢慢說明補「（父不詳）」；小節統計 16 隻（♂5／♀8／不詳 3）→ 18 隻（♂5／♀10／不詳 3）、
  候補註記 3 隻（歡歡・樂樂・緩緩）→ 1 隻（樂樂）；台北 `huanhuan-2007-07-03` 列補同名提示；
  條目總數 846 → 848

**其他**：
- **slug 消歧**：歡歡（huān）與緩緩（huǎn）同園、皆無生日，去聲調後拼音同為 `huan-huan`。
  依維護者裁定，歡歡取乾淨的 `huan-huan-dujiangyan`；緩緩沿用「撞名加媽媽名」慣例作
  `huan-huan-duo-duo-dujiangyan`。兩條目互相標 ⚠️ 同拼音提示並註明漢字與聲調差異
- 兩筆新條目皆為 `limited-profile` 檔案卡，`zoos:` 起始年留空（不知抵達年）；
  維護者確認、現正在世故**不掛** `unverified`；`sources` 無 host 故 `has_official_source` 仍為 false
- 緩緩與慢慢同母，惟慢慢之父不詳，是否同父（全血緣或 ½）、是否同胎均待查證，兩邊條目皆已標 🚧

---

## [2026-08-04] fix | 社群回報查證：`arun`・`mei-mei` 轉入 Assiniboine Park Zoo；新增 `rufus`・`suva`・`kelly`

**來源**（回報者附的來源不足，查證時另尋官方佐證）：
- https://classic107.com/articles/assiniboine-park-zoo-welcomes-back-red-panda-arun-from-vancouver
  （2025-11-18；忠實轉載 Assiniboine Park & Zoo 聲明：Arun 依 AZA SSP 建議移入與 Tanvi 配對，並載明其父母為 Rufus 與 Rouge）
- https://www.assiniboinepark.ca/stories/236/furry-red-and-fun-our-red-panda-update
  （2024-11-05 園方官網；列出當時園內四隻：Tanvi、Kelly〈9 歲、自 Zoo de Granby 移入〉、Mei Mei〈2 歲、GVZoo 生〉、Suva〈Assiniboine 生、曾在 Toronto Zoo〉）
- https://www.assiniboinepark.ca/stories/253/double-the-fun-meet-suva-and-mei-mei
  （2024-12-17 園方官網；Suva × Mei Mei 依 SSP 配對，入住舊雪豹展區）
- 線索（非採信依據）：RPF #426／#437／#391／#432 之生日、性別、居住史

**回報查核結果**：
- 回報 `M1vqg6l`（`arun`，轉園 → Assiniboine，生效日 2025-11-18，來源僅 IG 貼文）：**採用**。IG 為非官方來源，
  但查得園方聲明轉載可佐證移動事實；回報附帶的「父 Rufus 母 Rouge」亦由該聲明證實（原條目父母為「不詳」）。
  回報者填的 2025-11-18 實為報導日，官方未載抵園日 → 依作者裁定以官方報導日入居住史並標 🚧
- 回報 `bZKyGE1`（`mei-mei`，轉園 → Assiniboine，生效日 2024-12-17，來源為園方官網）：**採用，惟日期修正**。
  回報者填的 2024-12-17 是 stories/253 的發布日，但園方 stories/236（2024-11-05）已載她在園 →
  居住史採官方首次提及日 2024-11-05（較回報值早 6 週），並標 🚧 抵園日不明
- 兩筆回報者均未留暱稱，`data/contributors.json` 不新增

**新增條目**：
- `rufus-2003-06-18.md` — Rufus ♂（RPF #426），生於 2003-06-18（🚧 僅 RPF），Assiniboine Park Zoo 種公；
  `rouge` 之配偶、`arun`・`rakesh` 之父，另與 `xia` 生下 2015 三胞胎。**檔案卡**（`limited-profile`）：
  RPF 無其居住史與歿日、2024 起園方公告未再提及 → `zoos:` 起訖留空、`last_seen: 2015-06-22`、加 `unverified`、
  `birth_zoo: unknown`（出生園不詳、不標 🐣）；官方佐證僅「為 Arun 之父、曾在該園」一項
- `suva-2017-06-13.md` — Suva ♂（RPF #437），生於 2017-06-13 Assiniboine Park Zoo，`tanvi` 之雙胞胎兄弟；
  2019-07-01 → Toronto Zoo，2024-01-15 回 Assiniboine（🚧 兩移動日僅 RPF；官方僅可確認 2024-11-05 已回園）；
  2024 年底依 SSP 與 `mei-mei` 配對。子女 Baby #1193・Adira #1194（2020）、Dash #1380（2022）暫未建條目
- `kelly-2015-06-12.md` — Kelly ♂（RPF #391），生於 2015-06-12 Cincinnati Zoo and Botanical Garden，
  2016-05-12 → Granby Zoo，2024-05-08 → Assiniboine Park Zoo（🚧 兩移動日僅 RPF）；2024-11 與 `tanvi` 引介中；
  母 Bailey #381 亦為 `homer` 之母 → 兩者同母半血緣

**更新條目**：
- `arun-2014-06-28.md` — `zoos:` GVZoo 訖改 2025-11-18、新增 Assiniboine（2025-11-18 – 現在）；tag 改 `zoo:Assiniboine Park Zoo`；
  刪去原「🚧 待查證：讀者稱 2025-11-17 移回、僅 IG 來源」段，改寫為官方聲明佐證的移動與配對；
  父母由「不詳」補為 母 `rouge`、父 `rufus`；補同父母手足與 ½ 手足；配偶增列 `tanvi`；sources 加園方聲明轉載
- `mei-mei-2022-06-14.md` — `zoos:` GVZoo 訖改 2024-11-05、新增 Assiniboine（2024-11-05 – 現在）；tag 改園；
  內文補移居與 SSP 配對、標 🚧 抵園日不明；配偶增列 `suva`；sources 加園方兩篇 stories
- `rouge-2002-06-20.md` — 配偶增列 `rufus`；子女行改列 RPF 編號並把 `arun`・`rakesh` 改 wikilink
- `rakesh-2014-06-28.md` — 父母由「不詳」補為 `rouge`／`rufus`
- `xia-2013-07-01.md`、`xing-2015-06-22.md`、`itsuki-2015-06-22.md`、`akito-2015-06-22.md` — 純文字「Rufus（RPF #426）」改 wikilink
- `tanvi-2017-06-13.md` — 雙胞胎 `suva` 改 wikilink；½ 手足 George・Fred 改 wikilink；
  新增配偶行（`zorro` → `kelly` 引介 → `arun`）；內文補 2024-11・2025-11 兩次配對公告
- `sachi-2012-06-18.md`、`tango-2015-07-30.md` — 子女表 Suva 改 wikilink 並補性別♂與現居
- `homer-2012-06-11.md` — 半血緣手足 Kelly 改 wikilink、註明同母 Bailey
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `assiniboinepark.ca`（Assiniboine Park Conservancy，園方 /stories/ 為官方一手）
- `index.md` — Arun 一家小節新增 `rufus`；Zorro × Tanvi 小節新增 `suva`・`kelly`；
  `arun`・`mei-mei` 兩列動物園欄改 Assiniboine Park Zoo 並改寫說明；兩小節前言補 2024–2025 SSP 重組；
  條目總數 848 → 851

**其他**：
- 依 CLAUDE.md「官方來源可直接採用」處理。**來源分軸**：園方官網 `assiniboinepark.ca` 已補進
  `tools/build_db.py` 的 `OFFICIAL_HOSTS`（比照 torontozoo.com／gvzoo.com）；Classic 107 雖忠實轉載園方聲明，
  但屬新聞媒體 → 依 SCHEMA〈sources 與 extra_sources 的分工〉放 `extra_sources`（`arun`・`rufus`），
  故 `rufus` 的 `has_official_source` 為 false
- 尚未處理：Suva 於 Toronto Zoo 的三隻子女（母不詳）、Rufus 未命名的父母（RPF #601／#602）、
  Rouge × Rufus 的 6 隻無條目子女、Bailey #381・Harold #389

---

## [2026-08-04] add | 補齊 `rufus`・`suva`・`kelly` 牽出的親屬：8 隻新條目＋1 隻暫存

承同日「社群回報查證」那筆——維護者裁定把新條目牽出的無條目親屬一併建檔。

**來源**：RPF `/export/redpanda.json`（#424／#401／#895／#393／#381／#389／#1194／#1380／#1193）。
**這批全部只有 RPF 依據、無官方佐證**，故生卒日、居住史、家系一律標 🚧；居住史中「日＝1」者
（如 Beilei 2019-01-01、Ralphie 2019-06-01、Bailey 生 2008-06-01／歿 2019-01-01）在 RPF 常為
月／年精度佔位，條目內已註明。

**新增條目（Rouge × Rufus 之子女，均生於 Assiniboine Park Zoo）**：
- `ralphie-2008-05-25.md` — ♂，這對配偶已知最早的子女；→ Edmonton Valley Zoo（2009-12-09）
  → Toronto Zoo（2012-11-14）→ Wild Zoo of Saint-Félicien（2019-06-01）。🚧 已 18 歲、RPF 未記歿日，是否在世待查證
- `beilei-2010-06-14.md` — ♀，`meris` 雙胞胎；→ Columbus → Prospect Park Zoo（2011-07-25）
  → Cincinnati（2016-05-26）→ Chattanooga Zoo At Warner Park（2019-01-01）。子女 4 隻（#394／#493／#469／#470）未建條目
- `meris-2010-06-14.md` — ♀ 🪽，`beilei` 雙胞胎；1 歲歿於 Columbus Zoo（2011-10-17）
- `kiah-2012-06-30.md` — ♀；→ Columbus（2013-06-28）→ Toledo Zoological Gardens（2017-11-30）。
  2014-06-20 三胞胎（#384／#411／#422）未建條目

**新增條目（Kelly 的父母，辛辛那提一脈）**：
- `bailey-2008-06-01.md` — ♀ 🪽（2008-06-01 – 2019-01-01）；Cincinnati → Lincoln Park Zoo（2009-04-20）
  → Cincinnati（2011-11-07）。與 `rover` 育有 `homer`、與 `harold` 育有 `kelly`；另有 Lin（#390）無條目
- `harold-2004-06-08.md` — ♂ 🪽（2004-06-08 – 2016-05-31）；辛辛那提種公。**RPF 完全沒有他的居住史與父母**，
  園名係由三隻子女的出生園回推的推定值 → `zoos:` 起始日留空、`birth_zoo: unknown`（不標 🐣）。
  `hazel` 與 Harriet（#425）生於他過世兩週後，屬遺腹胎

**新增條目（Suva 的子女，均生於 Toronto Zoo）**：
- `adira-2020-07-14.md` — ♀；母 Ila（#324 🪽）；2022-10-03 移居 サンディエゴ動物園。子女 Pavitra（#1417）未建條目
- `dash-2022-07-13.md` — ♂ 🪽（2022-07-13 – 2022-10-23，3 個月餘）；母 Paprika（#486）。
  RPF 無居住史，Toronto Zoo 由父 Suva 當時所在園回推 🚧。⚠️ 與既有 `dash-2012-06-06` 同名、無血緣
- `_hidden/baby-ila-2020-07-14.md` — 出生 8 天夭折（2020-07-14 – 2020-07-22），`adira` 同胎、母 Ila。
  依「幼逝寶寶收錄原則」**從未取名、僅以佔位名 `Baby` 登錄 → 移入 `wiki/_hidden/`**，不計數、不上站；
  slug 依佔位名規則含媽媽名。性別 RPF 未記錄

**保留未建（維護者裁定 2026-08-04）**：
- **Phoenix #400 與 #448** — 同名、同為 2011-06-13 生、父母同為 Rufus × Rouge，但兩條居住史各自完整且
  完全不同（#400 走 San Diego → Houston → Lincoln Park → Western North Carolina；#448 走 Saskatoon
  → Safari Niagara）。是同胎同名兩隻、或 RPF 重複登錄未明；且 CLAUDE.md「撞名加媽媽名」在此無效
  （同一個媽）→ **暫不建條目**，slug 消歧規則待裁定。`rufus` 條目已記此疑點

**更新條目**：
- `rufus-2003-06-18.md` — 子女表 Ralphie／Beilei／Meris／Kiah 改 wikilink；補「兄弟」行
  （`rover`・`rusty`・`dusk`・`zeyar`＋RPF #603，均與 `rover` 條目所記的 #601／#602 同父母）；新增兩隻 Phoenix 待釐清備注
- `rouge-2002-06-20.md` — 子女行改 wikilink，Phoenix ×2 註明暫未建
- `arun-2014-06-28.md`、`rakesh-2014-06-28.md` — 同父母手足行改 wikilink；`rakesh` 另補 ½ 手足行
- `xing-2015-06-22.md`、`itsuki-2015-06-22.md`、`akito-2015-06-22.md` — 補「½ 兄弟姊妹（父方，母為 Rouge）」行
- `rover-2005-05-16.md` — 純文字 Rufus、Bailey 改 wikilink（子女表另一方親本同步）
- `homer-2012-06-11.md` — 母 Bailey 改 wikilink；½ 手足行區分同母（Lin・Kelly）與同父（Dr. Erin Curry）
- `kelly-2015-06-12.md` — 父母改 wikilink；½ 手足拆成同母／同父兩行（同父新增 `hazel`・Harriet）
- `hazel-2016-06-14.md` — 補 母（不詳 🚧）／父 `harold`／雙胞胎 Harriet／½ 手足 `kelly` 四行
- `suva-2017-06-13.md` — 子女表補母親欄（Ila #324 🪽、Paprika #486）與 wikilink；補配偶行。
  **修正**：先前寫「母不詳」有誤，RPF 其實有記
- `dash-2012-06-06.md` — 補 ⚠️ 同名提示（指向 `dash-2022-07-13`）
- `data/zoos.json` — 補三座園空白的 `location_ja`／`location_zh`：Saskatoon Forestry Farm Park & Zoo
  （薩斯克其萬省薩斯卡通）、Toledo Zoological Gardens（俄亥俄州托萊多）、Wild Zoo of Saint-Félicien（魁北克省聖費利西安）
- `index.md` — Arun 一家小節新增 4 隻（Ralphie・Beilei・Meris・Kiah）；Zorro × Tanvi 小節新增
  `adira`・`dash-2022-07-13`；Dusk 一家小節新增 `bailey`・`harold`；條目總數 851 → 859

**尚未處理（下一批候選）**：Beilei 的 4 隻子女、Kiah 的 3 隻子女、Ralphie 之子 Qiji（#423）、
Adira 之女 Pavitra（#1417）、Ila（#324）與 Paprika（#486）、Lin（#390）、Harriet（#425）、
Dr. Erin Curry（#392）、Bailey 的父母 Lum（#380）・JJ（#382）、Rufus 未命名的父母（#601／#602）

---

## [2026-08-05] update | `suva` 補 Toronto Zoo 官方新聞稿＋2017 命名報導；回報 `8NAybaY` 查核

處理社群回報 `8NAybaY`（2026-08-04 提交，「沒有看到小熊貓」報缺類，主旨為 Assiniboine Park Zoo 的 Suva）。
**條目其實已存在**——同日「社群回報查證」那批處理 `mei-mei` 時，已把牽出的 `suva` 一併建檔，
故該批 log 的「回報查核結果」未列到這筆。本次僅補來源與佐證，不新增條目（總數 859 不變）。

**來源**：
- https://www.torontozoo.com/press/2020/!newsite.asp?pg=20200919
  （2020-09-19 Toronto Zoo 官方新聞稿；載明 Suva 為「a three-year-old male red panda who came from
  Assiniboine Park Zoo」、依 AZA 紅熊貓 SSP 建議與自 Woodland Park Zoo 移入的 Ila 配對，
  2020-07-14 生下雙胞胎、為該園自 1996 年以來首次小熊貓繁殖）
- https://www.cbc.ca/news/canada/manitoba/red-panda-cubs-winnipeg-zoo-1.4292094
  （CBC News 2017-09-15；載生於 6-13、母 Sachi 父 Tango）
- https://winnipeg.ctvnews.ca/assiniboine-park-zoo-announces-names-of-red-panda-cubs-1.3591700
  （CTV News Winnipeg 2017-09-15；公眾票選命名，Suva ♂・Tanvi ♀，尼泊爾語「好運」／「纖細的女孩」）

**回報查核結果**：
- **基本資料全部吻合**：♂、母 `sachi`、父 `tango`、雙胞胎 `tanvi`、生於 2017-06-13 —— 與既有條目一致。
  原本生日與父母僅靠 RPF #437，本次由 CBC／CTV 兩篇 2017-09-15 報導獨立佐證（媒體 host → `extra_sources`）
- **居住史兩個日期均不採用**：
  - 回報「2024-12-17 回 Assiniboine」**排除**：該日為園方 stories/253 的發布日，非抵園日；
    同站 stories/236（2024-11-05）已載他在園 → 回園必早於回報值。與同批 `mei-mei` 那筆同一個坑
  - 回報「2019-09-06 → Toronto Zoo」**查無佐證**：搜 torontozoo.com 無 2019 抵園公告；
    回報所附兩支 IG 貼文（約 2020-11、2023-12）只能證明「當時他在多倫多」、定不了日期，且 IG 被 robots 擋住無法直讀
  - 故 `zoos:` 維持 RPF 值 2019-07-01／2024-01-15 並續標 🚧；**移動「本身」則因本次 Toronto Zoo 新聞稿首次取得官方依據**
- 回報者未留暱稱，`data/contributors.json` 不新增

**更新條目**：
- `suva-2017-06-13.md` — `sources` 加 Toronto Zoo 2020-09-19 新聞稿（`torontozoo.com` 已在
  `OFFICIAL_HOSTS`）；新增 `extra_sources`（CBC・CTV 兩篇 2017-09-15 報導）；
  🚧 段落改寫（區分「移動事實有官方佐證」與「移動日仍無」，並記下兩個回報日期被排除的理由）；
  內文補公眾票選命名與名字語義；子女表後補一行官方佐證註（Ila 那胎為該園 1996 年以來首次繁殖）

---

## [2026-08-05] update | `fin-fin` × `toku-toku` 之子 `shun-shun`（#597）母子連結補上，全站純文字改 wikilink

維護者指出 `fin-fin`（#136）除了 `nokaze` 之外還有一個兒子 `shun-shun`（#597）。**條目其實早已存在**
（`shun-shun-2007-07-01`，2007–2011，池田→平川），只是兩邊各記一半、彼此沒連上：
`fin-fin` 的子女表寫「Shun-Shun（RPF #597）／父：不明」是純文字，
而 `shun-shun` 的家族欄寫「母：不詳（園方未公布）」。本次把兩邊接起來，不新增條目（總數 859 不變）。

**依據**：既有 wiki 內既存的兩筆 RPF 資料互補，非新來源——
- RPF #136（`fin-fin`）的子女列表已載 #597，父方空白 → 母＝`fin-fin` 由此確立
- RPF #596（`toku-toku`）的子女列表已載 #597（`toku-toku` 條目與 `shun-pei` 條目皆以此記父子）→ 父＝`toku-toku`
- 旁證吻合：兩隻同期同園（`toku-toku` 2004-05-20 – 2008-02-04 在池田動物園、`fin-fin` 2003-02-07 起在池田），
  `shun-shun` 2007-07-01 生於池田動物園

**更新條目**：
- `shun-shun-2007-07-01.md` — 母欄「不詳」改 `fin-fin`（#136）；新增 ½ 妹妹 `nokaze`（同母異父，父 `tsubasa`）；引言改為雙親並列
- `fin-fin-2002-06-20.md` — 子女表 `shun-shun` 純文字改 wikilink、父欄「不明」填 `toku-toku`、備注補平川轉園與 `shun-pei` 父子關係；引言「與不明雄性育有」改為與 `toku-toku` 育有
- `toku-toku-2001-07-21.md` — 引言補配偶 `fin-fin`；子女表備注補母
- `nokaze-2009-06-25.md` — ½ 兄 `shun-shun` 純文字改 wikilink，異父補 `toku-toku`
- `shun-pei-2011-07-04.md` — 家族補「祖父母（父方）：`toku-toku` × `fin-fin`」
- `sora-2014-06-12.md`、`kira-2014-06-12.md` — 半血緣兄弟備注的「父：Shun-Shun #597」純文字改 wikilink
- `index.md` — Shin-Shin 家族「Toku-Toku 之子（母不詳）」段落標題改為「母：`fin-fin`，已收錄於 Nohana 家族」、
  該列說明改父母並列；Nohana 家族祖父母表 `fin-fin` 說明補「亦為 `shun-shun` 之母」；頁首最後更新日改 2026-08-05

---

## [2026-08-05] add | 社群回報：`mei-mei-2022-06-14` × `suva` 2026-06-08 產下雄仔（蘋果籽佔位）

讀者回報 Mei-Mei（`mei-mei-2022-06-14`）產仔、他方親代 Suva，附 IG 連結
`https://www.instagram.com/p/DbYZijXjgmX`。查證後**採用**：該貼文為 Assiniboine Park Zoo
官方 IG（@assiniboineparkzoo，官網 assiniboinepark.ca/zoo 頁尾社群連結指向此帳號）2026-07-29
的出産公告，Classic107・CHVN・CTV Winnipeg 同日轉載園方聲明，三方一致：**2026-06-08 生、
單胎一隻、雄性、母 Mei-Mei（初產）、父 Suva**，公告時尚未命名。回報者填的生日 2026-06-08
與來源相符（非文章發布日），無須重算。

依「當季寶寶佔位條目：蘋果籽」制度建檔（父母皆確認＋完整生日＋在世＋未命名，四項符合）；
性別園方已公告，故 `sex: male` 與 `male` tag 一併填入，不留空。

⚠️ 巧合備注：同日 2026-06-08 另有 Calgary Zoo 的 `udaya` 三胞胎（`apple-seed-1/2/3-udaya-2026-06-08`），
兩窩無關；Udaya 為 Mei-Mei 的同母異父姊姊，查證時已確認非同一則消息誤植。

**新增條目**：
- `apple-seed-mei-mei-2026-06-08.md` — ♂，Assiniboine Park Zoo 出生（🐣🏡）；`sources` 為園方官方 IG 貼文，
  三則新聞轉載入 `extra_sources`；`rpf_id` 待補（RPF 尚未建檔）

**更新條目**：
- `mei-mei-2022-06-14.md` — 引言補產仔一段；新增 `### 子女` 表；`sources` 加園方 IG 貼文、新增 `extra_sources`（三則轉載）
- `suva-2017-06-13.md` — 引言補產仔一段；子女表加一列並改標題（原「子女（均生於 Toronto Zoo）」→「子女」，
  前三隻生於多倫多改以表後註記說明）；`sources` 加園方 IG 貼文、`extra_sources` 補三則轉載
- `index.md` — Arun × Sakura 一家補列蘋果籽、段落敘述補產仔；`suva` 說明補一子；條目總數 859 → 860

**工具**：`tools/build_db.py` 的 `OFFICIAL_IG_ACCOUNTS` 新增 `assiniboineparkzoo`（官網頁尾連結佐證），
故該 IG 貼文列為官方來源、於個體頁「來源」區塊顯示。

回報者未留暱稱，`data/contributors.json` 不變。

---

## [2026-08-05] add | 平川動物公園初代・2 代目：`hon-hon-1984-06-15`、`mii-mii-1985-06-28`、`kiki-1992-07-20`

維護者提供園內「平川ZOO レッサーパンダ史」展牌（2014 年遊客實拍）之三隻歷代個體，
並附平川園報與鹿児島市廣報紙查證。三隻皆為**平川動物公園史上最早的小熊貓**，wiki 原本未收。

**來源**：
- https://hirakawazoo.jp/wp/wp-content/uploads/2022/10/%E3%81%B2%E3%82%89%E3%81%8B%E3%82%8FNo27.pdf （園報《ひらかわ》No.27，1988-12。封面即小熊貓；p.1 表紙解說「当園のレッサーパンダは友好都市中国長沙市より、昭和63年7月26日贈られました」；p.3「友好都市中国長沙市より珍獣『レッサーパンダ』が贈られました。園内での歓迎式（昭63.7.26）」＋照片說明「赤崎鹿児島市長と肖常錫団長がクス玉を割ると、紅紅（ホンホン、雄）が、早速顔を出しごあいさつ。咪咪（ミーミー、雌）は、はずかしいのか部屋の中です。」；p.2 市長致詞「今年は友好都市の中国・長沙市から『レッサーパンダ』が初めてお目見えしました」）
- https://hirakawazoo.jp/wp/wp-content/uploads/2022/10/%E3%81%B2%E3%82%89%E3%81%8B%E3%82%8FNo28.pdf （園報《ひらかわ》No.28，1989-12，p.4「ハイ！担当は私です」田淵賀彦技師：「レッサーパンダは友好都市の中国・長沙市から1988年7月25日来園しました」）
- http://kagoshima-hiroba.jp/wp/oldpdf/h24/03/201203-089.PDF （《かごしま市民のひろば》2012 年 3 月號「平川動物公園のあゆみ」年表：「昭和63年7月　中国・長沙市からレッサーパンダ来園」）
- 園內「平川ZOO レッサーパンダ史」展牌（園方製作，僅遊客實拍可查；**展牌原文寫進條目「備注」段落，`extra_sources` 只列可點的部落格連結、不另列純文字項目**）
- https://mihorinh.exblog.jp/20526830/ （レサパン日和 2014-12-16，展牌實拍；非官方 → `extra_sources`）
- https://4travel.jp/travelogue/10876846 （4travel 2014-04-13 訪，同展牌另一組實拍；非官方 → `extra_sources`）
- https://gachon.exblog.jp/3406686/ ・ https://gachon.exblog.jp/11081022/ （がちょん 2006-07-19 生日文／2010-05-09 訃報，貴貴的出生園與家系線索；非官方 → `extra_sources`）

**新增條目**：
- `hon-hon-1984-06-15.md` — 紅紅 ホォンホォン，♀，1984-06-15 生 – 1999-11-17 歿；長沙市動物園 → 平川（1988-07-25 来園）。
  ⚠️ **性別兩官方來源打架**：展牌 ♀／園報 No.27 「雄」，經維護者裁定採**展牌 ♀**，條目內併記園報原文並標 🚧 待查證
- `mii-mii-1985-06-28.md` — 咪咪 ミーミー，♀，1985-06-28 生 – 2005-12-03 歿（享年 20 歲）；長沙市動物園 → 平川（1988-07-25 来園）
- `kiki-1992-07-20.md` — 貴貴 キキ，♀，1992-07-20 生 – 2010-05-02 歿；生於広島市安佐動物公園 → 平川（來園年不詳，居住史起始留空）。
  🚧 父母（`yuu-yuu-1983` 友友 × `ai-ai-1984` 愛愛）與雙胞胎（恋恋，池田動物園）依同好部落格訃報，**非官方、待查證**；
  與安佐官方「愛愛育成 14 子」及「桃太郎的姑母」說法一致。恋恋資料過少，暫不建條目

**更新條目**：
- `ai-ai-1984.md`、`yuu-yuu-1983.md` — 子女表新增 `kiki-1992-07-20`（標 🚧 非官方）；14 子女註記段落補一句說明
- `hajime-1991-07-27.md` — 內文補「平川 2 代目」定位與初代兩隻；家族補同園夥伴 `kiki-1992-07-20`；
  `extra_sources` 加園內展牌（ハジメ 那張與園方訃報完全一致，可互為佐證）與部落格實拍
- `index.md` — 新增「## 平川動物公園 初代・2 代目個體（鹿兒島）」一節（置於安佐重慶始祖之後）；條目總數 860 → 863

**工具**：`tools/build_db.py` 的 `OFFICIAL_HOSTS` 新增 `kagoshima-hiroba.jp`（鹿児島市広報課的廣報數位封存站，
網域非 `.lg.jp` 故需個別列入），詳見 `CHANGELOG.md`。

**未採用／待辦**：
- 平川園報 No.26（1987-12，開園 15 周年寫真集）早於小熊貓來園（1988-07），與本批無關
- 恋恋（レンレン，池田動物園，貴貴雙胞胎）——僅部落格提及，無性別／生卒，未建條目
- 貴貴由安佐移入平川的年月仍缺；紅紅性別待第三方官方來源裁決

---

## [2026-08-05] update | `extra_sources` 只放 URL：6 筆純文字佐證改由內文承載

維護者裁定：個體頁「其他參考資料」區塊**只呈現連結**，純文字說明不顯示。`SCHEMA.md` 原本
允許「無法線上核對的一手佐證寫純文字說明」，本次改為**一律寫進條目內文／`## 備注`**（可引述展牌原文），
`extra_sources` 只列 URL；網站端亦加過濾（詳見 `CHANGELOG.md`、`SCHEMA.md`、`CLAUDE.md`）。

**更新條目**（僅刪 frontmatter 的純文字項目，內容原本就已在內文／備注，無遺失）：
- `hajime-1991-07-27.md` — 移除「平川動物公園『飼育員の日記』2011 年訃報（原連結已失效…）」（備注段已完整說明）
- `ouji-kobe.md` — 移除剥製展示解說牌純文字（備注段已引述「愛称：王子／オス／飼育期間 1983.2.22 ～ 1990.7.15」原文）
- `pei-pei.md` — 移除廣州動物園園內公告牌純文字（備注段已載）；`extra_sources` 已空，整欄刪除
- `mi-duo-dalian.md`、`nuo-mi-dalian.md`、`xi-ning-dalian.md` — 移除「園方展牌（讀者 2025-04 實拍…）」
  （引言「最後確認」與內文均已記）；三筆 `extra_sources` 已空，整欄刪除
- `hon-hon-1984-06-15.md`、`mii-mii-1985-06-28.md`、`kiki-1992-07-20.md`（本日新建）— 展牌原文自 `extra_sources`
  移入「## 備注」的「📋 展牌原文」一行，`extra_sources` 只留 mihorinh／4travel／gachon 等部落格連結

---

## [2026-08-05] update | 註冊表：`鹿児島市平川動物公園` 座標與地點修正

維護者指出園頁地址不對。核對 Google 地圖後確認：

- **座標偏西約 195 公尺**：原 `31.4630427, 130.4997487`（lineage 帶入值）落在園區西側的平川浄水場一帶，
  非園本身。改為 Google 地圖該園 POI 的 `31.4631175, 130.5017959`。園頁「🧭 路線導航」按鈕即用此座標。
- **`location_ja` 補到町層級**：`鹿兒島縣鹿兒島市` → `鹿兒島縣鹿兒島市平川町`（官方地址為
  〒891-0133 鹿児島県鹿児島市平川町5669-1；比照上野「東京都台東區」、王子「兵庫縣神戸市灘區」的粒度）。
  個體頁居住史的「地點」欄由註冊表自動帶入，重建後一併更新。
- `location_en` 同步補 `Hirakawacho`；`map` 由已停用的 goo.gl 短連結改為座標式 Google Maps 連結。

**更新檔案**：`data/zoos.json`（僅平川一筆，5 行）

---

## [2026-08-05] add | 回報查證（`linus-2018-06-23` 家系）：補建母 `lin-2013-06-16` 與雙胞胎妹妹 `kora-2018-06-23`

社群回報（資料更正・親屬關係）指 `linus` 之母為 Lin、父為 Kola、同胞姊妹為 Kora，並附三個來源。
逐一核對後**三項全部成立**，且來源皆為辛辛那提動物園官方（官網文章＋官方 X），依 CLAUDE.md
「官方來源可直接採用」逕行更新。回報寫「同胞姊妹」，實為**同日雙胞胎**（兩隻同為 2018-06-23 生）。

**來源**（回報所附三筆，全部可開、全部官方）：
- https://cincinnatizoo.org/ch-ch-ch-changes-new-faces-and-better-spaces-at-the-cincinnati-zoo/ （官網 2018-08-31：「Cincinnati Zoo leads the world in red panda births for the *fulgen Styani* subspecies, having produced a total of 88 cubs, including the two born in June to experienced mom **Lin** and first-time dad **Kola**」；文首圖檔名含 kora linus）
- https://x.com/CincinnatiZoo/status/1073359449732067331 （官方 X 2018-12-13：「Red panda cubs **Linus & Kora** & their mom **Lin**」— 一句同時綁定三隻）
- https://x.com/CincinnatiZoo/status/1058388615313657856 （官方 X 2018-11-02：「Our baby red panda cubs **Linus & Kora** are getting brave and adventurous!」）

**補充來源**（本次自行查得）：
- https://cincinnatizoo.org/remembering-red-panda-lin/ （官網 2024-02-22 訃告：「Lin was 10 years old」「She was born here at the zoo and then went on to have **10 offspring** of her own」）
- https://cincinnatizoo.org/red-panda-cubs-born-at-cincinnati-zoo/ （官網 2015-08-03：當年兩胎之母為「two-year-old **Lin**」與「seven-year-old Bailey」→ 獨立佐證 Lin 生於 2013 年、且 2015 年即已育有一胎）
- https://www.facebook.com/cincinnatizoo/videos/173989166813910/ （官方 FB：「Red panda cubs Linus & Kora, born on **June 23**」）
- https://www.foxnews.com/us/columbus-zoo-red-panda-kora-found.amp （Fox News 2020-07-23：Kora 在 Columbus Zoo 一度不見蹤影後尋回，全文以 she/her 稱 → 佐證性別 ♀ 與 2020-07 在該園；新聞轉載，列 `extra_sources`）
- https://www.fox19.com/2024/02/24/cincinnati-zoo-announces-death-10-year-old-red-panda/ （Fox19 訃報轉載；列 `extra_sources`）
- https://redpandafinder.com/export/redpanda.json （RPF #390 Lin ♀ 2013-06-16 – 2024-02-15、#999 Kora ♀ 2018-06-23、#1000 Linus ♂ 2018-06-23，family edge 一致；**其子女表恰為 10 筆，與官方訃告的「10 offspring」數量相符，可互為佐證**）

**新增條目**：
- `lin-2013-06-16.md` — Lin，♀，2013-06-16 生 – 2024-02-15 歿（10 歲）；終身居 Cincinnati Zoo and Botanical Garden（RPF #390）。`bailey-2008-06-01` 之女、辛辛那提 2010 年代後期主力母獸，10 隻子女。🚧 歿日採 RPF（官方訃告僅稱「last week」）；父 Toby（#838）僅 RPF、標待查證
- `kora-2018-06-23.md` — Kora，♀，2018-06-23 生；Cincinnati → Columbus Zoo and Aquarium（RPF #999）。`linus-2018-06-23` 雙胞胎妹妹。🚧 移園日 2019-10-21 僅 RPF 為據（官方層面只能確認 2020-07 已在哥倫布）

**更新條目**：
- `linus-2018-06-23.md` — 母 → `lin-2013-06-16`、父 → `kola-2015-08-24`、雙胞胎 → `kora-2018-06-23`；引言刪「父母不詳」；補全／半血緣手足列；`sources` 加三筆官方（原僅 RPF）、`extra_sources` 加官方 FB
- `kola-2015-08-24.md` — 補配偶 `lin-2013-06-16` 與**子女表**（Kora #999・Linus #1000・Audra #1001・Lenore #1002；原本子女欄整段缺）；引言補「first-time dad」一段；`sources` 加官方兩筆
- `bailey-2008-06-01.md` — 子女表 Lin 一列由純文字改為 `lin-2013-06-16` 連結（原註「無條目」已過期）；父欄由「不詳」補為 Toby（#838）🚧；引言補一句
- `hazel-2016-06-14.md` — 母由「不詳」補為 `lin-2013-06-16` 🚧（依 RPF #390 子女表；官方僅稱 10 子女、未逐隻公布）；補同母 ½ 手足列；引言補一句
- `index.md` — Dusk 一家（加拿大／美國）節新增 `lin-2013-06-16`・`kora-2018-06-23` 兩列與節首說明；Ravi 一家節的 Linus 說明補父母與雙胞胎；條目總數 863 → 865

**工具**：`tools/build_db.py` 新增官方來源判定 `cincinnatizoo.org`（`OFFICIAL_HOSTS`）、`cincinnatizoo`
（`OFFICIAL_X_ACCOUNTS` 與 `OFFICIAL_FB_PAGES`）——否則本批三個回報來源全會被判非官方，詳見 `CHANGELOG.md`。

**待辦**：
- Lin 另有 6 隻子女尚無條目：Dr. Erin Curry #392（2015-06-19）・Harriet #425（2016-06-14 – 2020-09-06 🪽，Hazel 雙胞胎）・Micu #614（2017-06-25 🪽）・Lucas #1191（2020-06-23）・Shenmi #1304（2021-07-16），以及 Kola 之女 Audra #1001・Lenore #1002（2019-07-05）。Audra・Lenore 有官方命名報導（WKYT 2019-10-03「Our red panda cubs born on July 5 have names! Meet Audra & Lenore!」）可據以建檔
- Hazel・Harriet 之母是否確為 Lin，仍待園方逐隻資料確認（現標 🚧）
- 回報者未留暱稱，`data/contributors.json` 不動

---

## [2026-08-05] add | Lin 一家收尾：補建其餘 7 隻子女，辛辛那提繁殖群家系接通

承本日前一筆（`lin-2013-06-16`／`kora-2018-06-23` 建檔），把 Lin 剩下的子女全部補齊。
園方訃告稱 Lin 共 10 隻子女，RPF #390 的子女表也恰為 10 筆（可互為佐證），**10 隻現已全數有條目**。
過程中另發現 Lin 的配偶其實有四隻（原本只掌握 Kola），且 `kendji`／`rover`／`harold`／`kelly`／
`homer`／`dash`／`kiki-2019-06-07`／`katara` 等 8 筆既有條目都存在「親屬其實有條目卻寫成純文字」
或「母不詳」的缺口，一併接通。

**來源**：
- https://cincinnatizoo.org/red-panda-cubs-born-at-cincinnati-zoo/ （官網 2015-08-03：該年兩胎之母為「two-year-old Lin」與「seven-year-old Bailey」，並稱是首次以超音波＋糞便荷爾蒙精準預測小熊貓產期的案例）
- https://cincinnatizoo.org/its-a-girl-x2/ （官網 2019-09-20：2019-07-05 出生的兩隻幼獸經性別鑑定**皆為雌性**、母為 Lin）
- https://cincinnatizoo.org/red-panda-cub-born-at-the-cincinnati-zoo/ （官網 2021-07-30：2021-07-16 Lin 產下一女；園方生殖生理學家 Dr. Erin Curry 稱 Lin 是「the first documented case of a red panda losing her pregnancy and then having another embryo come along and implant in the same year」）
- https://www.facebook.com/cincinnatizoo/posts/10155562383845479/ （官方 FB 2017：「Micu our red panda cub is just over 2-months-old and is starting to venture out」）
- https://www.instagram.com/cincinnatizoo/p/DLu2Y5BuKUg/ （官方 IG 2025-07-06：「Happy 6th Birthday to Audra & Lenore the red panda sisters」→ 佐證兩姊妹至 2025 年仍在出生園）
- https://www.wkyt.com/content/news/Cincinnati-Zoo-announces-names-of-red-panda-cubs-562096431.html （WKYT 2019-10-03 轉載園方命名公布：「Meet Audra & Lenore!」；新聞轉載 → `extra_sources`）
- https://www.fox6now.com/news/meet-dr-erin-curry-milwaukee-county-zoo-welcomes-its-new-red-panda （FOX6 Milwaukee 2016-04-19：密爾瓦基迎入辛辛那提出身的九月齡母獸，並說明命名取自追蹤該次懷孕的生殖生理學家；新聞 → `extra_sources`）
- https://redpandafinder.com/export/redpanda.json （#392／#425／#614／#1001／#1002／#1191／#1304 的性別・生卒・居住史・family edge；Harriet 與 Audra・Lenore 在 RPF **完全無居住地記錄**）

**新增條目**（7 筆）：
- `dr-erin-curry-2015-06-19.md` — Dr. Erin Curry，♀，2015-06-19 生；Cincinnati → Milwaukee County Zoo（2016-03-15）。Lin 長女、父 `rover-2005-05-16` 🪽。名字取自園方生殖生理學家。子女 Dr. Lily #419・`kiki-2019-06-07`・Cinder #1379（RPF #392）
- `harriet-2016-06-14.md` — Harriet，♀，2016-06-14 生 – 2020-09-06 歿；`hazel-2016-06-14` 雙胞胎、父 `harold-2004-06-08` 🪽 遺腹胎（RPF #425）。🚧 RPF 無任何居住地記錄，居住史僅依出生園推定（比照 `harold` 條目做法）
- `micu-2017-06-25.md` — Micu，♂，2017-06-25 生 – 2019-01-01 歿；Cincinnati → Red River Zoo（2018-05-10）。父 `kendji-2015-06-22`（RPF #614）。🚧 歿日「日＝1」為 RPF 精度佔位
- `audra-2019-07-05.md` — Audra，♀，2019-07-05 生；父 `kola-2015-08-24`，`lenore` 雙胞胎；**至今仍居出生園**（RPF #1001）
- `lenore-2019-07-05.md` — Lenore，♀，同胎（RPF #1002）
- `lucas-2020-06-23.md` — Lucas，♂，2020-06-23 生；Cincinnati → サンディエゴ動物園（2021-07-01）。父 `kendji-2015-06-22`；2023 育有一女 Pavitra #1417（無條目）（RPF #1191）
- `shenmi-2021-07-16.md` — Shenmi，♀，2021-07-16 生；Cincinnati → Ross Park Zoo（2022-05-03）。父 `kendji-2015-06-22`、Lin 最後一胎（RPF #1304）。🚧 RPF 另記中文名「神迷」・暱稱「咪咪」（日文 シェンミ／ミーミー）——依慣例中文名與暱稱以維護者提供為準，`chinese` 暫留空；無日本居住史故 `japanese` 不採 RPF 機械轉寫。`english_variants` 收 Shen-Mi／Mimi／Mii-Mii／Miimii（⚠️ 與 `mii-mii-1985-06-28`・`mii-mii-1992-08-07` 為不同個體）

**更新條目**（10 筆，多為「親屬已有條目卻仍是純文字」的缺口）：
- `lin-2013-06-16.md` — 子女表 10 列全部上 `[[wikilink]]`、父欄補齊；配偶由 2 隻補為 4 隻（Rover・Harold 🚧・Kendji・Kola）；引言與備注改寫
- `kola-2015-08-24.md` — 子女表 Audra・Lenore 上連結；引言同步
- `kendji-2015-06-22.md` — 子女表 Micu・Lucas・Shenmi **母欄由「不詳」補為 `lin-2013-06-16`**、三列上連結；配偶補 Lin；引言改寫
- `rover-2005-05-16.md` — 子女表 Dr. Erin Curry 上連結、母欄由「不詳 🚧」補為 Lin
- `harold-2004-06-08.md` — 子女表 Hazel・Harriet 母欄由「不詳 🚧」補為 Lin 🚧、Harriet 上連結；配偶欄由「Hazel・Harriet 之母不詳」改為 Lin 🚧
- `hazel-2016-06-14.md` — 雙胞胎 Harriet 上連結（原註「無條目」已過期）；同母 ½ 手足列全部上連結
- `kelly-2015-06-12.md` — ½ 手足 Lin・Harriet 上連結（原註「無條目」已過期）；同父 ½ 的母欄補 Lin 🚧
- `homer-2012-06-11.md` — ½ 手足 Lin・Dr. Erin Curry 上連結（原註「均無條目」已過期）
- `dash-2012-06-06.md` — 子女表標題的 Dr. Erin Curry 上連結
- `kiki-2019-06-07.md` — **母由「Dr. Erin Curry（RPF 佔位名）」改為 `dr-erin-curry-2015-06-19` 連結**；引言補外祖母 Lin
- `katara-2025-07-04.md` — 父方 ½ 兄姊 Micu・Lucas・Shenmi 上連結、補母 Lin
- `index.md` — 新增「## Lin 家族（辛辛那提繁殖群 → 全美各園）」一節（9 列，Hazel 與 Linus 已收錄於他節故不重複）；Dusk 一家節移出 Lin・Kora 兩列並改寫節首；條目總數 865 → 872

**工具**：`tools/build_db.py` 的 `OFFICIAL_IG_ACCOUNTS` 新增 `cincinnatizoo`（本批引用其官方 IG 貼文佐證 Audra・Lenore 現況）。

**待辦**：
- Lin 的孫輩仍缺條目：Dr. Lily #419（2018-06-06，Milwaukee，該園史上第一隻小熊貓幼獸）、Cinder #1379（2022-06-12，Milwaukee）、Pavitra #1417（2023-06-09，Lucas 之女）
- **辛辛那提 2026-06-22 誕生第 100 隻小熊貓**（官網 2026-06-26〈100th Red Panda Born at the Cincinnati Zoo〉：母 Marcy 首胎、父 Zuko 三歲首次當爸，雙胞胎僅一隻存活，尚未公布名字與性別）→ 符合「蘋果籽」佔位資格，惟 Marcy 與 Zuko 皆無條目，需一併建檔
- Shenmi 的中文名（RPF 記「神迷」）待維護者裁定
- Harriet 的轉園與歿地、Micu 精確歿日仍缺官方來源
---

## [2026-08-05] fix+rename | Leah 的原名是 Poppy 不是 Rose：雙胞胎姊妹身分對調，Rose 實居 Prospect Park Zoo

讀者回報（Tally 資料更正／類型「名字」，未留暱稱）指出 `leah-2019-05-17` 的原名／別名應為 **Poppy**，並附三項來源。查證後成立：本 wiki 原把 Everland 的 Leah 掛成 RPF #1252（主名 Rose），實際上是兩姊妹身分對調——官方年報載明雙胞胎在 2022 年分別去了兩個國家，出生園 Assiniboine 已無這對雙胞胎。

**來源**：
- https://www.assiniboinepark.ca/uploads/public/documents/2022_AnnualReport.pdf （Assiniboine Park Zoo 官方年報第 7 頁：6 月 `Rose` 轉往紐約布魯克林 Prospect Park Zoo、11 月 `Poppy` 轉往韓國 Everland，皆依 AZA 小熊貓 SSP 建議）
- https://www.instagram.com/prospectparkzoo/reel/CkvkQA-DODu/ （Prospect Park Zoo 官方 IG，2022-11：影片以 `Rose` 之名介紹園內小熊貓 → 佐證 Rose 在布魯克林）
- https://namu.wiki/w/%EB%A0%88%EC%95%84(%EB%A0%88%EC%84%9C%ED%8C%90%EB%8B%A4) （韓國 namuwiki「레아(레서판다)」引愛寶樂園官方回覆「에버랜드 공식 답변에 따르면 Poppy가 레아」，並註明 `Rose` 是 2022 年移美的雙胞胎姊妹；fan wiki → `extra_sources`）
- https://redpandafinder.com/#profile/1252 ／ https://redpandafinder.com/#profile/1253 （Claude in Chrome 實查：#1252 `Rose` 名下掛著 Everland 居住史與韓文名 레아／로즈、英文名 Leah／Lea，#1253 `Poppy` 是無居住史的空白檔 → **RPF 上游同樣掛錯**，僅記錄、不影響本 wiki 判定）

**更名**（1 筆）：
- `poppy-2019-05-17.md` → **`rose-2019-05-17.md`** — 這隻是 Rose（RPF #1252），原記「雙胞胎中留在出生地 Assiniboine」有誤。`name` Poppy → **Rose**、`rpf_id` 1253 → **1252**、`zoos:` 改為 `Assiniboine Park Zoo (2019-05-17 – 2022-06-01)` ＋ **`Prospect Park Zoo (2022-06-01 – 現在)`**、tag `zoo:` 同步；補年報與官方 IG 來源、`## 備注` 記身分更正與 RPF 上游誤植；引言補「抵園時園內尚有 `willow-2015-08-24`（同年 12 月移 Houston）」。🚧 轉園精確日不明（年報只記「6 月」），暫記 2022-06-01。

**更新條目**（11 筆）：
- `leah-2019-05-17.md` — `rpf_id` 1252 → **1253**、`nicknames` 移除 `로즈`、`english_variants` 補 `Poppy`；抵 Everland 日由 2022-12-01（RPF 值）改為 **2022-11-01 🚧**（年報與 namuwiki 均只記「2022 年 11 月」，日不明）；標題改 `# Leah（레아 / 原名 Poppy）`、引言改寫為「出生園登錄名 Poppy、赴韓後改稱 Leah」；`sources` 補年報、`extra_sources` 補 namuwiki；`## 備注` 新增「身分更正」（三項來源引述＋RPF 上游誤植）與「注意同名」（Toronto 的 `poppy-2024-06-13`）
- `tanvi-2017-06-13.md`、`zorro-2013-07-01.md` — 引言與子女表的 `poppy-2019-05-17` 改指 `rose-2019-05-17`，備注由「居 Assiniboine」改為「2022-06 移居美國 Prospect Park Zoo」；Leah 的「RPF 名 Rose」改為「原名 Poppy」
- `tango-2015-07-30.md`、`sachi-2012-06-18.md`、`kayah-2007-06-11.md`、`koko-2000-06-23.md`、`rina-2012-08-02.md`、`kendji-2015-06-22.md`、`seina-2000-06-23.md` — 同上：全文「（RPF 名 Rose，現居韓國 Everland）」改為「（原名 Poppy，現居韓國 Everland）」，並補上 Rose 的新 slug 與現居園
- `poppy-2024-06-13.md` — 「⚠️ 注意同名」改指 `leah-2019-05-17` 的**原名** Poppy（已非現用名），親屬稱謂改為「本個體的表姑」
- `index.md` — 節標題改「海外個體（加拿大・Zorro × Tanvi 一家 → 韓國 Leah・美國 Rose）」；`poppy-2019-05-17` 一列改為 `rose-2019-05-17`（Prospect Park Zoo 🇺🇸、RPF #1252）；Leah 列改記原名 Poppy／RPF #1253；`poppy-2024-06-13` 的同名註記改指 Leah 原名。**條目總數不變（872）**

**工具**：`tools/build_db.py` 的 `OFFICIAL_IG_ACCOUNTS` 新增 `prospectparkzoo`（佐證＝官網 `prospectparkzoo.com` 頁尾 IG 連結）；見 `CHANGELOG.md`。

**重建**：`gen_residence`（872 檔、無額外 churn）→ `build_db`（872 個體 / 1239 親子邊 / 237 雙胞胎）→ `export_json` → `audit.py` 🔴 0（🟡 48 皆為既有中國檔案卡）、`check_twins` 0 錯誤 0 警告。

**待辦**：
- RPF #1252／#1253 的錯誤屬**外站資料**（非本專案可控）：Everland 居住史與 레아／Leah／Lea 掛在 #1252、#1253 為空白檔。依資料來源原則以 wiki 為準即可；若日後想回報上游，可到 redpanda-lineage 開 issue（目前未做）
- Rose 抵 Prospect Park 後的動向（同居夥伴、是否再轉園）查無園方公告，現居暫記該園
- 回報者未留暱稱 → 未動 `data/contributors.json`

---

## [2026-08-05] fix | Linus・Kora 的官方 FB 來源已失效 → 換成仍在線的官方貼文，原文移入備注

維護者指出 `linus-2018-06-23` 引用的 Cincinnati Zoo 官方 FB 影片雖屬官方來源，但影片已看不到。
實測確認：`https://www.facebook.com/cincinnatizoo/videos/173989166813910/` 與含標題 slug 的長網址
**兩種形式都回「This Video Isn't Available Anymore」**——Facebook 已移除該則 2018 年的 FB Live 影片
（貼文本身連同影片一起消失，非僅播放失敗）。

**處置**（依 SCHEMA 2026-08-05〈`extra_sources` 只列可點的 URL〉與 `ouji-kobe` 展牌原文的先例）：
- `linus-2018-06-23.md`・`kora-2018-06-23.md` — 移除失效的影片連結；新增「## 備注 → 📋 已失效的官方來源」
  一段，**逐字保留原標題**「Red panda cubs Linus & Kora, born on June 23, have started exploring outside! #fblive」
  並註明失效日與實測結果。這是目前**唯一明確寫出「June 23」出生日的官方文字**（官網文章只寫「born in June」、
  官方 X 兩則都沒提日期），故不能只是刪掉了事。
- 兩筆的 `sources` 改列仍在線的官方 FB 貼文
  https://www.facebook.com/cincinnatizoo/posts/10156593028135479/ （2018-10-24：「Our 2 baby red pandas,
  Linus and Kora, are having fun exploring all the elements of their outdoor yard.」）——同一官方帳號、
  同樣證明兩隻同胎且當時同在辛辛那提。原本這條 FB 來源被放在 `extra_sources`，既然 `cincinnatizoo`
  已入 `OFFICIAL_FB_PAGES`，一併移進 `sources`。

**同批複查**：本日新增的其他 Cincinnati 系連結逐一實測皆仍在線——官網 4 篇、官方 X 2 則、
官方 FB `posts/10155562383845479`（Micu，2017-10-02，內文以 his 稱 → 另佐證性別 ♂）、
官方 IG `p/DLu2Y5BuKUg`（Audra・Lenore 6 歲生日）、以及 fox19／fox6now／foxnews／WKYT 四則新聞轉載。

**教訓**：**Facebook 的 `/videos/` 連結（尤其 2018 年前後的 FB Live）會整則消失**，`/posts/` 相對穩定。
日後採用 FB 來源時優先取 `/posts/` 形式，並在寫進 frontmatter 前實際開一次；若只有影片形式，
就把標題原文抄進條目備注再引連結。

---

## [2026-08-05] add | 圖鑑缺漏回報：壽山動物園（高雄）唯一的小貓熊 `球球`，並登記壽山動物園

讀者回報（2026-08-04，未留暱稱）指壽山動物園有一隻名為「球球」的小貓熊未收錄，附三筆連結。
回報所填「性別 女／來園 2001 年／過世 2014 年」逐筆對照來源後**全部成立**，惟三筆來源皆非官方
（新聞報導 ×2、學生專題頁 ×1），故依 2026-08-02 規範一律列入 `extra_sources`，`sources` 記
`讀者回報（…）` ＋ `維護者提供（…）` 兩行（無 host → `has_official_source` 仍為 false）。

**來源**（皆非官方）：
- https://www.epochtimes.com/b5/1/2/2/n42607.htm （大紀元 2001-02-02：走私棄養個體於高雄縣被發現，2001-02-01 由壽山動物園正式接收、檢疫 21 天；未提名字）
- https://news.ltn.com.tw/news/local/paper/915647 （自由時報 2015-09-15：該園「唯一的小貓熊」「因年紀很大、去年過世（約廿五歲）」→ 歿於 2014；未提名字性別）
- https://www.shute.kh.edu.tw/~2010PBL13/narrative02-5.htm （樹德家商 2010 學生專題〈壽山動物園歷屆活動〉：2008-08-24 園方為小貓熊「球球」辦生日會、文中以「她」稱——名字與性別的唯一佐證）

**查證補充**：
- 該校專題頁對沙盒回 403，改用 Claude in Chrome 讀取原文。
- 園方官網（`zoo.kcg.gov.tw`）現行動物名單已無小貓熊，官方公告亦查無此隻；三則來源可互相對應為同一個體（該園史上僅此一隻）。
- 報導稱歿時「約廿五歲」→ 回推生於 1989 年前後，已超小熊貓常見壽命，屬報導推估，故 `born` 留空、不寫入；生日會辦在 8 月 24 日僅供參考。
- 亞種不詳（走私來源）→ **`species` 欄整行省略**、tags 不加亞種 tag（比照 `tiger-2012`、`punchang` 等亞種不詳個體）。
  ⚠️ 一開始寫成 `species: Ailurus fulgens`（比照 `hana-2023`），但 `build_db.py` 的判斷是 `if "fulgens" in species_str: return "fulgens"`
  → 種名層級的寫法會被**誤判成 fulgens 亞種**（`hana-2023`、`hashi-2022` 目前即被記為 fulgens）。亞種不詳時省略該欄才會輸出 `species: null`。
- `birth_zoo: unknown`（非出生園，避免居住史首站被標 🐣）。

**新增條目**：
- `qiu-qiu-kaohsiung.md` — 球球 Qiu Qiu（♀，走私查獲收容），2001-02-01 入壽山動物園、2014 年歿；生日不詳故 slug 用園簡稱（`limited-profile`＋`rescue`＋`deceased`）

**更新條目**：
- `index.md` — 新增區塊「台灣個體（高雄・壽山動物園）」；條目總數 872 → 873
- `qiu-qiu-chengdu.md`、`qiu-qiu-nanjing.md` — 「⚠️ 注意同名」補上第三隻同名個體

**註冊表／工具**：
- `data/zoos.json` — 新增 `壽山動物園`（zh 高雄市壽山動物園／Shou Shan Zoo／Taiwan／高雄市鼓山區／22.6345573, 120.2751711／官網 zoo.kcg.gov.tw；含 `location_zh`）。休園日（每週一）**未編 `closed_ja`／`closed_rule`**：台灣園的國定假日開園規則與現行欄位語意（日本祝日）不合，暫不編碼
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `zoo.kcg.gov.tw`（供日後若有園方公告可用）

**重建**：`gen_residence`（873 檔、無額外 churn）→ `build_db`（873 個體 / 1239 親子邊 / 237 雙胞胎 / 1514 筆居住史）→ `export_json`（172 園、未匹配園名 0）→ `verify.sh` 通過（`audit` 🔴 0 / 🟡 48 皆既有中國檔案卡、`check_twins` 0 錯誤 0 警告）。
⚠️ 本次重建由 Cowork 遠端 session 經 device_bash 執行，掛載資料夾不支援 SQLite → DB 寫在 /tmp，**repo 根目錄的 `redpanda.db` 仍是舊的**；`pipeline/data/*.json` 已更新。要同步 DB 檔請在本機跑一次 `bash rebuild.sh`。

**致謝**：回報者未留暱稱 → 未動 `data/contributors.json`

---

## [2026-08-05] fix | 泰國走私救援個體 `hana-2023`・`hashi-2022` 的亞種誤記為 fulgens → 改為留空

承本日 `qiu-qiu-kaohsiung` 建檔時發現的坑：`tools/build_db.py` 的亞種判斷是純字串比對
（`if "fulgens" in species_str: return "fulgens"`），所以**種名層級**的 `species: Ailurus fulgens`
（原意是「只到種、亞種不詳」）會被判成 **fulgens（喜馬拉雅亞種）**。

兩隻泰國走私查獲救援個體正是這樣寫的，導致 frontmatter 與內文自相矛盾——內文明寫
「出生地、**亞種**與血緣等資料皆不詳」，DB 與網站卻記為 fulgens 亞種。

**處置**：兩筆的 `species:` 整行移除（tags 本來就沒有亞種 tag，無須調整），輸出即為
`species: null`，與 `tiger-2012`、`punchang`、`poddoung` 等亞種不詳個體一致。

**更新條目**：
- `hana-2023.md`、`hashi-2022.md` — 移除 `species: Ailurus fulgens`

**規範**：
- `SCHEMA.md` — `species` 欄位註解補上「亞種不詳→整行省略、勿寫種名層級 `Ailurus fulgens`」，避免再犯

**重建**：`build_db`（873 個體）→ `export_json` → `verify.sh` 通過。亞種分佈由
styani 820 / fulgens 49 / null 4 變為 **styani 820 / fulgens 47 / null 6**（少掉的 2 隻即本次兩筆）。

**慣例（記錄備忘）**：亞種有據才寫 `Ailurus fulgens styani` / `Ailurus fulgens fulgens`；
**亞種不詳一律整行省略 `species:`**，不要寫種名層級的 `Ailurus fulgens`。

⚠️ 同前一筆：本次重建經 device_bash，repo 根目錄的 `redpanda.db` 仍是舊的，本機跑一次
`bash rebuild.sh` 即可同步。

---

## [2026-08-05] add | 安佐 `ron-ron-1995-06-30` × `banana-1996-08-09` 一家補齊：`suika-2002-08-04`、`baron-1999-07-11`、`meron-1999-07-11`

維護者指定建立 RPF #332（`suika`）。查 RPF export 資料集後確認其 11 隻手足中 `baron` #564、
`meron` #565 尚無條目，依「新增成員流程」第 3 步一併補建；至此 Ron-Ron #231 的 12 名子女
**全數已建檔**。

**來源**：
- https://redpandafinder.com/#profile/332 (Suika スイカ)
- https://redpandafinder.com/#profile/564 (Baron バロン)
- https://redpandafinder.com/#profile/565 (Meron メロン)

**新增條目**：
- `suika-2002-08-04.md` — Suika スイカ ♂（RPF #332），2002-08-04 生於広島市安佐動物公園，
  2010-02-25 → 宮崎市フェニックス自然動物園，2012-12-12 → ひらかたパーク，2016-02-03 歿（享年 13 歲）。
  11 隻手足中**唯一的單胎**（RPF 無同胎 litter 邊），無子女紀錄
- `baron-1999-07-11.md` — Baron バロン ♂（RPF #564），1999-07-11 生於安佐，2001-01-18 → 釧路市動物園，
  2004-04-07 → アドベンチャーワールド，2011-09-27 歿（享年 12 歲）；`meron` 之雙胞胎，無子女
- `meron-1999-07-11.md` — Meron メロン ♀（RPF #565），1999-07-11 生於安佐，2001-01-30 → 群馬サファリパーク，
  2008-07-17 → いしかわ動物園，2014-06-26 歿（享年 14 歲）；`baron` 之雙胞胎。在群馬與 Ron-Ron
  RPF #665（≠ #231／#208）育有雙胞胎 `sora-2002-06-24`・`umi-2002-06-24`

**更新條目**（回填雙向 wikilink——原本兩邊各記一半、對方明明已有條目卻寫成純文字）：
- `ron-ron-1995-06-30.md`、`banana-1996-08-09.md`、`shii-2000-07-13.md` — 子女／½ 手足表中的
  `meron`・`baron`・`buna`・`suika`・`matsu`・`ichi`・`sora`・`daichi` 改為 wikilink，並補上各自終居園
- `tochi-2001-07-24.md` — 父／母原為純文字（`Banana`／`Ron-Ron`），改為 wikilink，此前家系圖上其父母顯示不詳
- `buna-2000-07-17.md`、`daichi-2006-08-01.md`、`sora-2006-08-01.md`、`ichi-2004-07-23.md`、
  `matsu-2004-07-23.md`、`nara-2000-07-17.md` — 手足列改 wikilink（`ichi` 的「雙胞胎：Matsu」亦為純文字，已改）
- `sora-2002-06-24.md`、`umi-2002-06-24.md` — 母由「`Meron`（未建檔）」改為 `meron-1999-07-11`
- `index.md` — 「Ron-Ron #231 × Banana 之子女」區塊新增 3 筆；條目總數 873 → 876

**修正（父/母行 wikilink 陷阱）**：`shii-2000-07-13.md`、`kashi-2000-07-13.md`、`tochi-2001-07-24.md`
的父／母行「⚠️ 勿與…混淆」註記裡夾了 `ron-ron-2002-06-28`／`ron-ron-2013-07-19`／`mai-2013-06-23`
的 wikilink，會被 build_db 當成額外父母（徵兆＝那三隻的子女表憑空多出小孩）。註記中的連結改為純文字
（比照 `nara-2000-07-17` 既有寫法），只留真正的父／母連結。

**維護者提供**：
- `ron-ron-1995-06-30.md` — 補漢字名 **龍龍**（`japanese: 龍龍, ロンロン`、標題同步），`sources` 加記
  維護者提供（2026-08-05）；`index.md` 該列說明同步改為「Ron-Ron 龍龍 / ロンロン」

---

## [2026-08-05] add | 宮崎フェニックス首代家族：`rin-rin-1993-06-29`（玲玲）、`ron-ron-1995-06-15`（龍龍 #367）、`franz-2000-06-23`

維護者請求「建立龍龍（`ron-ron-1995-06-30`）的媽媽リンリン（1995 到達宮崎）」。查證發現**兩隻不同的 Ron-Ron**：
維護者提供的宮崎來源（4travel、exblog、月刊パンダ、四國新聞）描述的リンリン＝RPF #781（漢字**玲玲**，
月刊パンダ載），其子為**宮崎的龍龍 RPF #367**（1995-06-15 生於宮崎、2007-12-17 歿、RPF 上游漢字即「龍龍」、
別名 Long-Long），並非 #231（ロンロン，長崎バイオパーク生 → 広島安佐）。#231 之母為另一隻リンリン
（RPF #830，野生出身 → 長崎，未建條目）。經維護者裁定：分建宮崎系條目，**#231 現載的漢字「龍龍」暫不動、
待後續裁定**。

生日裁定：リンリン採 **1993-06-29**（RPF＋月刊パンダ＋4travel 內文一致；四國新聞 2005-05-24 記 11 歳吻合）；
維護者所見園製照片曾讀作 1992 🚧 已記於條目備注待重核。

**來源**：
- https://redpandafinder.com/#profile/781 (Rin-Rin 玲玲)
- https://redpandafinder.com/#profile/367 (Ron-Ron 龍龍)
- https://redpandafinder.com/#profile/362 (Franz フランツ)
- https://www.gekkan-panda.com/zoo/lesserpanda-kyushu/201710/31-470 （漢字 玲玲，維護者提供）
- https://4travel.jp/travelogue/10781265 ／ https://geroppa55.exblog.jp/11851265/ ／ https://www.shikoku-np.co.jp/national/life_topic/20050524000391 （皆已實開核對，記入各條目 extra_sources）

**新增條目**：
- `rin-rin-1993-06-29.md` — Rin-Rin 玲玲 ♀（RPF #781），1993-06-29 生於周南市徳山動物園，1995-03-27 →
  宮崎市フェニックス自然動物園（**初代小熊貓**），2013-11-01 歿（享年 20 歲）。獨子 `ron-ron-1995-06-15`
  推定為徳山時期受孕（父不詳 🚧）；與同期來園的カンカン（#880，無條目）未有子嗣
- `ron-ron-1995-06-15.md` — Ron-Ron 龍龍 ♂（RPF #367），1995-06-15 生於宮崎（**園內首隻出生**），一生未離園，
  2007-12-17 歿。與 `franz-2000-06-23` 育有 `ribbon-2006-05-30`・`ren-2007-06-14`
- `franz-2000-06-23.md` — Franz フランツ ♀（RPF #362），2000-06-23 生於ズーラシア（`pam-1997-06-26` ×
  `mii-mii-1994-06-26` 之女、`kousei-2000-06-23` 雙胞胎），2005-03-10 → 宮崎，2016-03-08 歿（享年 15 歲）

**更新條目**（回填雙向 wikilink）：
- `ribbon-2006-05-30.md`、`ren-2007-06-14.md` — 父／母由純文字改為 `ron-ron-1995-06-15`／`franz-2000-06-23`
  wikilink；`ribbon` 的 Kotarou・Hiko・Ren、`ren` 的 Ribbon 亦補 wikilink（純文字親屬但條目已存在）
- `kousei-2000-06-23.md`、`chip-2001-06-19.md`、`dale-2001-06-19.md`、`porin-2002-06-15.md` — 手足列
  Franz（及 Chip・Porin・Ko-ai 等既有條目）改 wikilink
- `pam-1997-06-26.md`、`mii-mii-1994-06-26.md`、`gaia-2004-06-10.md` — 子女／手足表 Franz 改 wikilink
- `index.md` — 新增「Rin-Rin 玲玲 × Ron-Ron 龍龍 家族」區塊（3 筆）；條目總數 876 → 879

---

## [2026-08-06] add | 都江堰 `le-le-dujiangyan`（樂樂 ♀，維護者裁定性別）；`寶劍` 列候補

維護者請求「調查都江堰小熊貓森林公園的樂樂是否有性別／生日／家系資料」，查證後依維護者裁定
「按女孩子建檔」。**園方無官網、亦查無官方認證微信公眾號**（搜狗微信搜尋確認），公開管道僅有
同好在 bilibili 上傳的園方直播錄屏（UP 主 `云间一纸书` 等），最早可追溯至 2024-08。

**性別 ♀ 之依據（推定，非官方）**：兩筆既有讀者回報（`@red.panda.ct` 2026-08-01 現場所見、
`Gaia` 2026-07-14 園內名單）均未載性別；同好錄屏標題多次以女性稱呼指稱樂樂——
2025-10-31「看欢欢乐乐两大美女要注意碰头」、2025-10-10「乐乐欢欢姐妹同框睡觉」、
2025-08-26「乐乐邻家小女孩超乖睡姿」、2026-03-15「饲养员又要把乐乐说给自己的亲儿子」。
維護者於 2026-08-06 裁定採 ♀（比照 `hong-hong` 性別由維護者裁定之先例），條目內已註明日後應覆核。

**生日與家系仍查無**：無任何來源提及樂樂生日；同好錄屏僅見與 `huan-huan-dujiangyan`（歡歡）、
`yuan-yuan-dujiangyan`（圓圓）、`duo-duo-dujiangyan`（多多）同框，標題「姐妹」在中文同好語境
多指「兩隻雌性」而非手足，不採為血緣。2025-12-08 標題「乐乐崽…」之「崽」為暱稱後綴，
**不據以判定有子女**。故 `born` 留空、家族欄父母皆記不詳。

**來源**：
- 讀者回報（@red.panda.ct，現場所見，2026-08-01）；Gaia 園內名單（2026-07-14）
- 維護者提供（2026-08-06；性別 ♀）
- 同好參考（非官方，記入 `extra_sources`）：https://www.bilibili.com/video/BV12Rw1zFETw/ ／
  https://www.bilibili.com/video/BV1odAuz2Eh1/ ／ https://www.bilibili.com/video/BV1KKCxB4EiX/ ／
  https://www.bilibili.com/video/BV1i21ZBTESe/

**新增條目**：
- `le-le-dujiangyan.md` — 樂樂／乐乐 Le Le ♀，生日不詳，現居 都江堰小熊貓森林公園（檔案卡
  `limited-profile`，`last_seen: 2026-08`，起始年留空）；父母不詳，備注記同框≠血緣與「崽」之判讀

**更新條目**：
- `le-le-2023-05-02.md` — 補同名提示（上海→台北 樂樂 ♂ ≠ 都江堰 樂樂 ♀）
- `data/cn-candidates.json` — 移除已轉正的 `樂樂`；新增 `寶劍`（多次與樂樂同框，名字僅見於同好
  影片標題、無維護者確認，未達門檻）
- `index.md` — 都江堰區塊 18 → 19 隻（♂5／♀11／性別不詳 3）、候補說明改記寶劍；
  條目總數更新為 880

**備注**：本次同時撈到同園尚未建檔的名字 `岁岁`、`得瓜`、`娇瓜`、`七月`（皆僅見同好影片標題），
以及 2025-07-03 錄屏標題「满满&七月过生日啦！」——「满满」疑為已建檔的 `man-man-dujiangyan`
（慢慢）之異寫，若成立則生日約 7/3，**待維護者向園方核對後再處理**，本次不動。

---

## [2026-08-06] add | 石川 `run-run-1995-07-19`（ルンルン ♀，RPF #713）一家 10 隻；太守一脈補齊

依 RPF #713 建檔並一併補齊直系親屬（配偶、子女、同父手足）。**母系有爭議、依維護者裁定暫記「不詳」**（詳下）。

**來源**：
- https://redpandafinder.com/#profile/713 (Run-Run)
- https://redpandafinder.com/#profile/712 (Ten-Ten) ／ /#profile/725 (Yon-Yon) ／ /#profile/589 (Mam) ／
  /#profile/615 (Tan-Tan) ／ /#profile/710 (Mei-Mei) ／ /#profile/711 (Suku-Suku) ／ /#profile/707 (Souhei) ／
  /#profile/706 (Koro-Koro) ／ /#profile/705 (Shota)

**⚠️ 母系爭議（本批最重要的一點）**：RPF 的親子邊記 `run-run-1995-07-19`（#713）之母為 `ten-ten-1992-06-26`
（#712），而天天本身是 `taisyu-1989`（#708）之女——若成立即為**父女近親交配**。旁證是相符的：天天
1995-03-27 由到津の森公園移入宮崎市フェニックス自然動物園，Run-Run 1995-07-19 生於宮崎，受孕期正落在
天天仍在到津、與太守同園之時。但既有條目 `taisyu-1989` 將 Run-Run 列於「太守 × `rin-rin-1989`（#709）
所生 8 隻」子女表中，而 `rin-rin-1989` 條目只列 6 隻（RPF 的 #709 親子邊亦僅 6 隻，不含 Run-Run 與
Koro-Koro）。兩說相左、無官方來源可證，**維護者 2026-08-06 裁定 Run-Run 母欄暫記「不詳」**，`taisyu-1989`
的子女表不改寫，僅於兩隻爭議個體加註 🚧。

**新增條目**：
- `run-run-1995-07-19.md` — Run-Run ルンルン ♀（RPF #713），1995-07-19 生於 宮崎市フェニックス自然動物園，
  1996-03-21 移居 いしかわ動物園，2007-06-18 歿（享年 11）；父 `taisyu-1989`、母不詳 🚧
- `ten-ten-1992-06-26.md` — Ten-Ten 天天 ♀（RPF #712），1992-06-26 生，到津 → 宮崎 → 日立市かみね動物園，
  2003-03-11 歿；父母 `taisyu-1989` × `rin-rin-1989`
- `yon-yon-1994-07-13.md` — Yon-Yon ヨニヨン ♂（RPF #725），1994-07-13 生於 周南市徳山動物園，
  1995-07-08 移居 いしかわ動物園，2007-04-19 歿；母 `ten-ten-1989-06-26`（#769）、父 Tom（#719，無條目）
- `mam-1997-06-26.md` — Mam マム ♀（RPF #589），1997-06-26 生於 いしかわ動物園，1999-01-09 移居
  東武動物公園，2002-05-22 歿；`pam-1997-06-26` 之雙胞胎
- `tan-tan-2001-06-19.md` — Tan-Tan タンタン ♂（RPF #615），2001-06-19 生，終生居 いしかわ動物園，
  2015-07-22 歿；`rin-rin-2001-06-19` 之雙胞胎
- `mei-mei-1990-06-21.md` — Mei-Mei ♀（RPF #710），1990-06-21 生於 到津の森公園，1998-07-23 移居
  とくしま動物園，1999-06-03 歿；**`japanese` 留空**——RPF 的 ja.name 記為「リンリン」，與英文名不符、
  疑為其母之名誤植 🚧
- `suku-suku-1991-07-18.md` — Suku-Suku スクスク ♀（RPF #711），1991-07-18 生，終生居 到津の森公園，
  2009-03-16 歿；RPF ja.name 原記「スくスく」（混用假名）已正規化 🚧
- `souhei-1993-07-11.md` — Souhei 宗平 ♂（RPF #707），1993-07-11 生，居 到津の森公園，1996-01-23 歿
  （享年 2）；`nene-1993-07-11` 之雙胞胎
- `koro-koro-1995-07-02.md` — Koro-Koro コロコロ ♂（RPF #706），1995-07-02 生於 到津の森公園，
  1999-11-04 移居 福岡市動植物園，2009-04-04 歿；父 `taisyu-1989`、**母不詳 🚧**（RPF 親子邊僅連父方）
- `shota-1997-07-12.md` — Shota ショタ ♂（RPF #705），1997-07-12 生於 到津の森公園，2002-02-10 移居
  大牟田市動物園，2014-02-17 歿

**更新條目**：
- `taisyu-1989.md` — 子女表 8 列全部改為 wikilink；`koro-koro-1995-07-02` 與 `run-run-1995-07-19` 兩列
  加註「母系 🚧 待查證」，表下補一段兩說並陳的說明（依維護者裁定，原本的「與 `rin-rin-1989` 所生」
  寫法不改）
- `rin-rin-1989.md` — 子女表 6 列改為 wikilink；補「配偶：`taisyu-1989`」；加註太守條目另列兩隻、母系待查證
- `nene-1993-07-11.md` — 雙胞胎 `souhei-1993-07-11` 純文字改 wikilink；新增「兄弟姊妹」一行
- `rin-rin-2001-06-19.md` — 母/父/雙胞胎/兄弟姊妹四項純文字全部改 wikilink，移除「非本批成員暫以純文字
  記錄」的過期註記
- `pam-1997-06-26.md` — 補母/父/雙胞胎/兄弟姊妹（原條目完全未記父母）
- `ten-ten-1989-06-26.md` — 新增「子女（部分）」表，收 `yon-yon-1994-07-13`（原註「lineage 另記有數名
  子女（待補）」）
- `index.md` — 新增「Run-Run 家族（到津 → 宮崎 → 石川；太守一脈）」區塊（主角／配偶／子女／父與同父
  手足）；條目總數更新為 890

**備注**：`tan-tan-2001-06-19`、`suku-suku-1991-07-18`、`souhei-1993-07-11` 三隻在 RPF 無逐次居住紀錄
（`location.N` 為空），但 birthplace 與 zoo 兩條邊指向同一園，故以「終生在園」記載並於備注標明。
本批 10 隻全部僅有 RPF 一項來源（線索級），尚無園方官方佐證。

---

## [2026-08-06] update | `run-run-1995-07-19` 補 extra_sources（同好部落格）

維護者提供同好部落格連結一則，依「非官方連結一律留存為其他參考資料」原則放入 `extra_sources`
（不進 `sources`、不影響 `has_official_source`）。

**更新條目**：
- `run-run-1995-07-19.md` — 新增 `extra_sources`：http://redpandamaniax.blog59.fc2.com/blog-entry-193.html

**備注**：該站以 http 提供、且會把 https 轉回 http，本環境（WebFetch 強制升級 https／Chrome 擋此網域）
無法開啟核對，故行末註解未能記標題與日期，內容亦未經確認。日後若能開啟，請補上標題／日期，
並判斷是否有可採信的資訊值得寫入條目。

---

## [2026-08-06] update | `run-run-1995-07-19`／`yon-yon-1994-07-13` 登錄漢字名 風風・勇勇；補官方年報來源

**來源**：
- https://www.ishikawazoo.jp/box/ichiran/10aniv/pdf/10anniversary.pdf — いしかわ動物園《開園10周年記念誌》
  （**官方**；維護者指出內載 Run-Run 的出産紀錄）
- https://redpandapedia.livedoor.blog/archives/16350429.html — RedPanda-pedia〈玲玲(リンリン)〉個體頁
  （同好名鑑，**非官方** → `extra_sources`）；原文載「父：勇勇(ヨンヨン)　母：風風(ルンルン)」，
  且生日 2001-06-19・2005-02-23 移動羽村・2023-09-22 歿三項與既有條目完全一致

**更新條目**：
- `run-run-1995-07-19.md` — `japanese` 由 `ルンルン` 改為 `風風, ルンルン`（漢字名依維護者指示登錄）；
  標題改「風風 / ルンルン」；加 ⚠️ 同漢字名提示（`fu-fu-1997-06-20` 風風／フウフウ 為不同個體、讀音亦異）；
  `sources` 加いしかわ動物園 10 周年記念誌；`extra_sources` 加 RedPanda-pedia
- `yon-yon-1994-07-13.md` — `japanese` 由 `ヨニヨン` 改為 `勇勇, ヨンヨン`；**RPF 的「ヨニヨン」判定為誤植**
  （前一批已標疑義，此次由名鑑確認），舊拼法移入 `english_variants`；標題改「勇勇 / ヨンヨン」；
  `extra_sources` 加 RedPanda-pedia
- `rin-rin-2001-06-19.md` — `extra_sources` 加 RedPanda-pedia（該頁即本隻的個體頁）；父母括號讀音同步
- `pam-1997-06-26.md`／`mam-1997-06-26.md`／`tan-tan-2001-06-19.md`／`ten-ten-1989-06-26.md`／`index.md`
  — 父母欄與說明中的括號讀音同步為「風風 / ルンルン」「勇勇 / ヨンヨン」
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `ishikawazoo.jp`，該園官網／PDF 起算官方來源

**🚧 待辦**：10 周年記念誌 PDF **本環境開不了**（WebFetch 的 robots.txt 逾時、瀏覽器擋此網域），
故僅登錄連結、未抄錄內容。內載的出産紀錄（1997 年 パム・マム、2001 年 玲玲・タンタン 兩胎）
待取得檔案後補入 `run-run-1995-07-19` 及四隻子女的條目。

---

## [2026-08-06] update | `run-run-1995-07-19` 補第二件官方來源（石川県広報《ほっと石川》1999 秋期号）

**來源**：
- https://www.pref.ishikawa.lg.jp/kouhou/hot/documents/hot_up_1999syuuki.pdf — 石川県広報《ほっと石川》
  1999 年秋期号（**官方**；`.lg.jp` 由 `is_official_source` 的政府網域 pattern 自動認列，無須加白名單）

**更新條目**：
- `run-run-1995-07-19.md` — `sources` 新增上述県広報 PDF；`## 備注` 改記兩件官方 PDF 及其無法開啟的原因

**🚧 待辦（累計）**：Run-Run 的兩件官方 PDF 本環境都讀不到——記念誌是 WebFetch 的 robots.txt 逾時
（`ROBOTS_DISALLOWED`），県広報是檔案超過 20 MB 抓取上限（HTTP 413）；`ishikawazoo.jp` 與
`pref.ishikawa.lg.jp` 兩個網域在瀏覽器端亦被擋。內容（1997 パム・マム、2001 玲玲・タンタン 兩胎的
出産紀錄，以及 1999 年開園相關報導）待取得檔案後補入本隻及四隻子女的條目。

---

## [2026-08-06] update | `taisyu-1989` 移除漢字名「太守」，全 wiki 統一為「大州」

維護者於網站 `/ja/p/taisyu-1989/` 檢視後指示刪除漢字名「太守」，並提供同好部落格佐證
（該文所用名稱一律作「大州」）。

**來源**：
- https://gachon.exblog.jp/9485066/ — 部落格〈レッサーパンダ三昧〉2009-03-19
  〈育育スクスク　ありがとうね！〉（**非官方** → `extra_sources`）；原文載
  「1991年7月18日 到津の森生まれ 父親：大州＆母親：輪輪」，並列其手足
  「梅梅（徳島）コロコロ（福岡）、天天（かみね）、寧々（多摩）、草平、将太（到津）」

**更新條目**：
- `taisyu-1989.md` — `japanese` 由 `太守, 大州, たいしゅ` 改為 `大州, たいしゅ`（移除「太守」，
  網站漢字名改顯示「大州」）；標題同步；引言下加 ℹ️ 說明「太守」為 RPF 記法、已依維護者指示移除；
  `extra_sources` 加該部落格
- `suku-suku-1991-07-18.md`／`rin-rin-1989.md`／`mei-mei-1990-06-21.md` — `extra_sources` 加該部落格
- 全 wiki 行文將「太守」改為「大州」（`（太守）`→`（大州）`、`太守之女／之配偶`、`太守 ×`、
  `太守一脈`、index 說明欄）：`shota-1997-07-12`／`koro-koro-1995-07-02`／`run-run-1995-07-19`／
  `ten-ten-1992-06-26`／`suku-suku-1991-07-18`／`mei-mei-1990-06-21`／`souhei-1993-07-11`／
  `rin-rin-1989`／`index.md` 共 9 檔。log 為 append-only 歷史，既有記載不改。

**🚧 待維護者裁定（同一篇部落格帶出的其他漢字名，本次未登錄）**：
`育育`（スクスク #711）、`輪輪`（リンリン #709）、`梅梅`（Mei-Mei #710，可解掉該條目
「japanese 待查證」的 🚧）、`草平`（Souhei #707，**與 RPF 的「宗平」相左**）、
`将太`（Shota #705，RPF 僅記「ショタ」）。名稱依 CLAUDE.md 以維護者提供為準，故先列出不逕改。

---

## [2026-08-06] update | `souhei-1993-07-11` 漢字名由「宗平」改採「草平」

維護者裁定：RPF 記「宗平」與同好部落格〈レッサーパンダ三昧〉的「草平」相左時，比照 `taisyu-1989`
（太守 → 大州）之例，以部落格為準。

**來源**：
- https://gachon.exblog.jp/9485066/ — 〈育育スクスク　ありがとうね！〉2009-03-19（**非官方** → `extra_sources`）

**更新條目**：
- `souhei-1993-07-11.md` — `japanese` 由 `宗平` 改為 `草平`；標題同步；`extra_sources` 加該部落格；
  備注記 RPF 原作「宗平」與本次裁定
- `nene-1993-07-11.md`／`index.md` — 行文中的「宗平」同步改為「草平」

**備注**：slug 不變（`souhei-1993-07-11`＝羅馬名 Souhei ＋生日，未受漢字名影響）。
其餘四個由同一篇部落格帶出的漢字名（育育／輪輪／梅梅／将太）仍待維護者確認，未登錄。

---

## [2026-08-06] update | 到津 大州家族補登四個漢字名：育育・輪輪・梅梅・将太

維護者確認採用同一篇部落格帶出的其餘漢字名（承前一筆 `souhei-1993-07-11` 草平之裁定）。

**來源**：
- https://gachon.exblog.jp/9485066/ — 〈レッサーパンダ三昧〉2009-03-19〈育育スクスク　ありがとうね！〉
  （**非官方** → `extra_sources`）

**更新條目**：
- `suku-suku-1991-07-18.md` — `japanese` `スクスク` → `育育, スクスク`；標題同步；備注改寫：
  該文即本隻悼念文，所載「1991年7月18日 到津の森生まれ」與條目一致；原「スくスく 🚧 正式寫法待查證」
  的 🚧 一併解除（確定為 RPF 機械轉寫誤植）
- `rin-rin-1989.md` — `japanese` `リンリン` → `輪輪, リンリン`；標題同步；同名提示補「漢字作輪輪，
  與玲玲・怜怜可區別」；內文與子女表標題的純文字 `Taisyu` 改為 wikilink `[[taisyu-1989]]（大州）`
- `mei-mei-1990-06-21.md` — 新增 `japanese: 梅梅`；標題同步；**解除「日文名 🚧 待查證」**——該文列
  「梅梅（徳島）」與本隻 1998 年移居とくしま動物園吻合，RPF 的 `ja.name`「リンリン」確認為其母之名誤植
- `shota-1997-07-12.md` — `japanese` `ショタ` → `将太, ショタ`；標題同步；新增 `extra_sources` 與 `## 備注`
- `ten-ten-1992-06-26.md`／`souhei-1993-07-11.md`／`suku-suku-1991-07-18.md`／`mei-mei-1990-06-21.md`
  — 母欄括號由「（リンリン）」改為「（輪輪 / リンリン）」
- `index.md` — 大州一脈區塊五列補漢字名（輪輪／梅梅／育育／将太），並把 Mei-Mei 列的「大州 × 玲玲長女」
  更正為「大州 × 輪輪長女」（玲玲為誤植，#709 的漢字是輪輪）

**備注**：至此該篇部落格帶出的五個漢字名（大州・草平・育育・輪輪・梅梅・将太）全數登錄完畢。
slug 一律不變（slug＝羅馬名＋生日，不受漢字名影響）。

---

## [2026-08-06] update | `run-run-1995-07-19` 父欄改「不詳」；`koro-koro-1995-07-02` 母補為輪輪

**⚠️ 覆蓋本日稍早的裁定。** 維護者指出：`父：大州` 的唯一依據就是 RPF 的 `family` 邊 708→713，
與已被否決的 712→713（母：天天）**是同一組邊、證據等級相同**，留一棄一站不住腳。

**證據鏈重查（本次新確認）**：
- `git log --follow wiki/taisyu-1989.md` → 初版 commit `3e5fffd` 的 `sources` 只有
  `redpandafinder.com/#profile/708` 一行。**該條目「太守 × 玲玲所生 8 隻」的子女表就是照 RPF 的
  #708 子女邊抄的，表頭的母系標籤是當時作業自行推論**——並非獨立來源。原本以為的「兩說相左」不存在。
- RPF 本身自洽：#708 子女 8 隻、#709 子女 6 隻，差的兩隻正是 `koro-koro-1995-07-02` 與
  `run-run-1995-07-19`；#713 的母邊明確指向 #712 天天。
- 同好部落格〈レッサーパンダ三昧〉2009-03-19 原文：「『大州』＆『輪輪』も毎年繁殖していて すご～ぉい！！
  梅梅（徳島）コロコロ（福岡）、天天（かみね）、寧々（多摩）、草平、将太（到津）**の両親です**。」
  連同該文主角育育共 7 隻，**未列ルンルン**（全文無「ルンルン」「風風」）。
- 四項線索彼此吻合、皆指向「大州 × 天天」（父女近親），**但全屬 RPF 與同好來源、無園方佐證**。

**維護者 2026-08-06 裁定**：`run-run-1995-07-19` **父母兩欄一律記「不詳」**；
`koro-koro-1995-07-02` 的母則**採部落格補為輪輪**（RPF 缺該邊屬資料不全、非否認）。

**更新條目**：
- `run-run-1995-07-19.md` — 父欄由 `[[taisyu-1989]]` 改為「不詳 🚧」（純文字，避免建成親子邊）；
  引言與 🚧 區塊改寫為「父母皆不詳」並說明證據等級相同之理由；移除「同父手足」一行（父系未確立），
  改於備注列出完整四點證據盤點
- `taisyu-1989.md` — **子女表移除 `run-run-1995-07-19` 一列（8 → 7 隻）**；否則
  `build_db` 的子女表反向邊會重建父子關係、蓋掉條目自身的「不詳」（見 build_db reverse child edges）；
  引言改「育有 7 隻子女」；表下說明改寫為兩則（Koro-Koro 母系已補、Run-Run 已移出）
- `koro-koro-1995-07-02.md` — 母由「不詳 🚧」改為 [[rin-rin-1989]]（輪輪）；「同父手足」改「兄弟姊妹」；
  新增 `extra_sources`（該部落格）與母系依據說明；引言改寫
- `rin-rin-1989.md` — 子女表新增 `koro-koro-1995-07-02`（6 → 7 隻），引言同步；表下註記改寫
- `mei-mei-1990-06-21`／`suku-suku-1991-07-18`／`ten-ten-1992-06-26`／`nene-1993-07-11`／
  `souhei-1993-07-11`／`shota-1997-07-12` — 手足行的「½ Koro-Koro（同父，母不詳）」改為全血緣
- `ten-ten-1992-06-26.md` — 備注改寫，記明裁定結果
- `index.md` — Run-Run 列改「父母 🚧 皆待查證」；子區塊標題改「到津 大州一脈（RPF 記為 Run-Run 的
  父方，🚧 未確立）」；區塊註記改寫；Koro-Koro 列改「母系依同好部落格補入」；大州列補 🚧 註記

---

## [2026-08-06] update | `run-run-1995-07-19` 父母登錄為 大州 × 天天（父女近親，🚧 待官方佐證）

**⚠️ 覆蓋本日稍早「父母皆不詳」之裁定。** 維護者審視證據後決定據四項吻合線索登錄父母。

**採信依據（四項互不矛盾）**：
1. RPF `family` 邊：#713 的父＝#708 大州、母＝#712 天天（天天為大州與輪輪之女）
2. RPF 內部自洽：#708 子女 8 隻、#709（輪輪）子女 6 隻（＋部落格補入的 Koro-Koro＝7），
   差的一隻正是 Run-Run
3. 同好部落格〈レッサーパンダ三昧〉2009-03-19 列舉「大州＆輪輪」子女共 7 隻，**未含 Run-Run**，
   與「其母另有其人」一致（全文無「ルンルン」「風風」）
4. 時序吻合：天天 1995-03-27 由到津の森公園移入宮崎，Run-Run 1995-07-19 生於宮崎；
   以孕期約 135 天回推，受孕期落在天天仍在到津、與大州同園之時（懷孕轉園）

**仍標 🚧**：四項全屬 RPF 與同好來源，**無園方官方佐證**；待石川兩件官方 PDF 抄錄後複核。

**更新條目**：
- `run-run-1995-07-19.md` — 父欄 `[[taisyu-1989]]`、母欄 `[[ten-ten-1992-06-26]]`（皆標 🚧）；
  引言與 🚧 區塊改寫（標明近交係數 F＝0.25）；新增「½ 同父異母手足」6 隻，並註明因近親之故
  該 6 隻同時是其舅姨、母親天天同時是其同父異母姊
- `taisyu-1989.md` — 子女表**拆為兩組**：「與輪輪所生」7 隻、「與己出之女天天所生」1 隻（Run-Run）；
  引言與配偶行同步；表下說明改寫
- `ten-ten-1992-06-26.md` — 新增「子女（與其父大州所生）🚧」表收 Run-Run；引言與備注改寫
- `rin-rin-1989.md` — 註記改為「Run-Run 非本隻所生，是本隻的外孫女兼繼女」
- `index.md` — Run-Run 列改「大州 × 天天（父女近親）🚧」；子區塊標題改「父方 大州一脈（父：大州；
  母：天天）」；區塊註記改寫；大州列與天天列同步

**一致性檢查（重建後）**：`run-run-1995-07-19` mother=`ten-ten-1992-06-26`／father=`taisyu-1989`；
大州子女 8 隻、輪輪子女 7 隻（差 Run-Run，正確）；天天子女 1 隻；無重複子女；`verify.sh` 通過。

---

## [2026-08-06] update | 抄錄いしかわ動物園《開園10周年記念誌》：2001 年一胎與ヨンヨン歿日取得官方佐證

維護者在 Chrome 擴充功能開放 `www.ishikawazoo.jp` 網站權限後，改以瀏覽器端 pdf.js 讀取該 PDF
（34 頁、14.2 MB、**無文字層**，故以 canvas 逐頁繪製後判讀）。

**來源**：
- https://www.ishikawazoo.jp/box/ichiran/10aniv/pdf/10anniversary.pdf
  《いしかわ動物園 開園10周年記念誌》p.10–11「命のあゆみ ― 10年間の誕生と死 ―」（**官方**）

**原文（誕生欄）**：
> 平成13年6月19日にシセンレッサーパンダの「ヨンヨン」（♂）と「ルンルン」（♀）との間に2頭の
> 赤ちゃんが誕生しました。赤ちゃんは「タンタン」（♂）と「リンリン」（♀）と命名されました。

**原文（死亡欄）**：
> 平成19年4月19日シセンレッサーパンダの「ヨンヨン」（♂）が12歳で死亡しました。

**取得官方佐證的項目**：2001-06-19 一胎兩隻的生日・性別（タンタン ♂／リンリン ♀）、父方ヨンヨン・
母方ルンルン、亞種（シセンレッサーパンダ＝styani）、**ヨンヨン之讀音**（RPF 的「ヨニヨン」確為誤植）、
ヨンヨン歿日 2007-04-19 與享年 12。

**更新條目**：
- `run-run-1995-07-19.md` — 備注以原文引述記載官方紀錄；子女表新增「佐證」欄（2001 一胎標
  ✅園方官方、1997 一胎仍為僅 RPF）；「🚧 待抄錄」縮小為僅剩県広報一件
- `yon-yon-1994-07-13.md` — `sources` 加該 PDF；備注改寫：讀音ヨンヨン已有官方佐證、歿日與享年一致；
  漢字「勇勇」仍僅同好名鑑
- `tan-tan-2001-06-19.md`／`rin-rin-2001-06-19.md` — `sources` 加該 PDF；新增／補寫「## 備注」記官方紀錄

**⚠️ 未解**：該書「命のあゆみ」只記園內十年間的**出生與死亡**，**不載個體來歷與血統**，
故 `run-run-1995-07-19` 自身的父母（大州 × 天天，父女近親）**仍無官方佐證、維持 🚧**。
1997 年パム・マム 一胎早於開園（1999-10）故亦不在該書範圍。
下一步：石川県広報《ほっと石川》1999 年秋期号；另可查該書 p.28–30 施設一覧／飼育動物一覧 有無個體級紀錄。

---

## [2026-08-06] add | トラン（RPF #382「JJ」）一脈：ズーラシア → 北米 5 隻

維護者提供同好部落格「がちょん」兩篇，確認 RPF #382「JJ」即よこはま動物園ズーラシア 2002 年生的
`トラン`：ミーミー追悼記事的出生一覧載「2002.6.15　トラン(Philadelphia)＆ポリン（アドベン）双子誕生」，
與 RPF #382 的生日（2002-06-15）、雙胞胎（`porin` #310）、終居（Philadelphia Zoo）三項全合；
另一篇〈北米生まれのホーマーって・・・・！？〉稱 `bailey`（#381）為「ズーラシア生まれのトランの仔」，
與 RPF 記 #382 為 Bailey 之母一致。故以 `Tran`／`トラン` 為正名建檔，RPF 登錄名 `JJ` 與 Other Names
`Tram` 收為 english_variants。RPF #382 的 Nicknames「ポーリン」／Other Names「Porrin」實為雙胞胎
`porin` 之名混入，未採用。

依 CLAUDE.md 新增成員流程一併補齊直系親屬：配偶 `Lum`（#380）與三隻子女 `Qin`（#386）、
`Big George`（#1403）、`Idgie`（#387）。性別由 RPF 手足性別計數推得：Bailey ♀ 已知，
由 Qin／Big George／Idgie／Bailey 四筆頁面的「N sisters and M brothers」聯立得 Qin ♂、Big George ♂、Idgie ♀。

**來源**：
- https://gachon.exblog.jp/21683474/ （同好部落格・ミーミー追悼記事：ズーラシア出生一覧）
- https://gachon.exblog.jp/23027652/ （同好部落格 2016-03-31：ホーマー來日與血統）
- https://redpandafinder.com/#profile/382 (Tran / JJ)
- https://redpandafinder.com/#profile/380 (Lum)
- https://redpandafinder.com/#profile/386 (Qin)
- https://redpandafinder.com/#profile/1403 (Big George)
- https://redpandafinder.com/#profile/387 (Idgie)

**新增條目**：
- `tran-2002-06-15.md` — Tran トラン（RPF #382，登錄名 JJ），♀，2002-06-15 生於よこはま動物園ズーラシア，
  2004-04-27 渡美，2017-02-02 歿於 Philadelphia Zoo
- `lum-2000-06-04.md` — Lum（RPF #380），♂，2000-06-04 生於 Columbus Zoo and Aquarium，
  2019-10-01 歿於 Henry Vilas Zoo；父母不詳
- `qin-2005-06-23.md` — Qin（RPF #386），♂，2005-06-23 生於 Cincinnati，2019-04-15 歿於 Prospect Park Zoo
- `big-george-2006-06-07.md` — Big George（RPF #1403，別名 Nong-Ren），♂，2006-06-07 生於 Cincinnati，
  2014-05-25 歿；Idgie 雙胞胎
- `idgie-2006-06-07.md` — Idgie（RPF #387），♀，2006-06-07 生於 Cincinnati，2020-04-02 歿於 Zoo Atlanta

**更新條目**：
- `bailey-2008-06-01.md` — 母／父純文字改為 `tran-2002-06-15`／`lum-2000-06-04` wikilink；補 ½ 兄弟姊妹三筆
- `tarrei-2002-07-01.md` — 補配偶 `tran-2002-06-15`（兩隻 2004-04-27 同日渡美入住辛辛那提）；
  子女三筆改為 wikilink
- `beilei-2010-06-14.md` — 子女表「父不詳 🚧」改為父 `qin-2005-06-23`（RPF #386 子女表相符）；補配偶
- `pam-1997-06-26.md`／`mii-mii-1994-06-26.md`／`gaia-2004-06-10.md` — 子女表 `JJ` 列改為 `tran-2002-06-15`
  wikilink，並順手把 `kousei`／`dale`／`porin` 三列補上 wikilink
- `franz-2000-06-23.md`／`chip-2001-06-19.md`／`dale-2001-06-19.md`／`kousei-2000-06-23.md`／
  `porin-2002-06-15.md` — 兄弟姊妹／雙胞胎欄的純文字 `JJ` 改為 `tran-2002-06-15` wikilink；
  移除「JJ 暫以純文字記錄」提示；`dale`／`kousei` 的 `chip`・`porin`・`koai` 亦補 wikilink
- `data/zoos.json` — 補 4 座園的 `location_ja`：Philadelphia Zoo「賓夕法尼亞州費城」、
  Zoo Atlanta「喬治亞州亞特蘭大」、Akron Zoological Park「俄亥俄州阿克倫」、
  Cleveland Metroparks Zoo「俄亥俄州克里夫蘭」（原為 null，居住史地點欄會空白）
- `index.md` — 新增「海外個體（ズーラシア → 北米・トラン 一脈）」一節共 5 筆；條目總數更新為 895

**🚧 待查證**：
- 五筆的生卒日與居住史皆僅有 RPF（線索），無官方佐證；`lum` 歿日 2019-10-01 疑為月精度佔位
- RPF #1403 在 Assiniboine 之後另記一筆 Edmonton Valley Zoo「2014-05-25 – 2014-05-25」（起訖同日＝歿日），
  疑為移園當日死亡或資料重複，居住史暫以 Assiniboine 為終站
- 部落格〈北米生まれのホーマーって・・・・！？〉稱 `rover`（#590）為「旭山で名無し」與「ポンタ」之子，
  與 RPF 記 Rover 父母（#601／#602，Assiniboine Park Zoo）不符；非官方來源，暫不採用、未改 `rover` 條目

---

## [2026-08-06] add | 讀者回報兩筆查證後採用：`kora` 2020 年產仔（Columbus Zoo）、`sundari` 轉園 Saint-Félicien

**來源**：
- https://www.columbuszoo.org/news/columbus-zoo-and-aquarium-celebrates-significant-births-represent-species-risk-and-under (Columbus Zoo 官方新聞稿，2020-06-30：6/13 凌晨 1:22／1:53 產下一公一母，母 Kora 2 歲、父 Gen Tso 7 歲，該園自 2015 年以來首次小熊貓繁殖成功，AZA Red Panda SSP 推薦配對，雙親皆首胎)
- https://www.facebook.com/columbuszoo/posts/10157908765757106 (Columbus Zoo 官方 FB，2020-09-19：國際小熊貓日公布命名 Santi ♀／Bandit ♂，載明「born on June 13 to mother, Kora and father, Gen Tso」)
- https://www.instagram.com/columbuszoo/p/CT7OGW1trwh/ (Columbus Zoo 官方 IG，2021-09-17：世界小熊貓日，`santi`・`bandit` 與媽媽 `kora`；擊掌訓練)
- https://www.instagram.com/zoosauvageofficiel/p/C1H2ktUhxMO/ (Zoo sauvage de Saint-Félicien 官方 IG，2023-12-21：「notre toute nouvelle résidente, Sundari… née au The Calgary Zoo et maintenant parmi nous depuis octobre dernier」)
- https://www.instagram.com/zoosauvageofficiel/p/DOldJGYgQUg/ (同上官方 IG，2025-09-14：Sundari ♀、「Née le 11/12 juin 2022」、「Arrivée au zoo en 2023」)
- https://redpandafinder.com/#profile/394 (Gen Tso)
- https://redpandafinder.com/#profile/1185 (Santi)
- https://redpandafinder.com/#profile/1186 (Bandit)

**新增條目**：
- `gen-tso-2013-06-22.md` — Gen Tso（RPF #394，別名 General Tso／General T'so），♂，2013-06-22 生於 Prospect Park Zoo，
  父 `qin`、母 `beilei`；2020 年在 Columbus Zoo 與 `kora` 育有雙胞胎；現居 Northeastern Wisconsin Zoo（RPF，🚧）
- `santi-2020-06-13.md` — Santi（RPF #1185），♀，2020-06-13 生於 Columbus Zoo and Aquarium，`bandit` 雙胞胎，現居出生園
- `bandit-2020-06-13.md` — Bandit（RPF #1186），♂，2020-06-13 生於 Columbus Zoo and Aquarium，`santi` 雙胞胎，
  現居 Henry Vilas Zoo（RPF，移園日 🚧）

**更新條目**：
- `kora-2018-06-23.md` — 補配偶 `gen-tso` 與子女 `santi`・`bandit`；sources 加 Columbus Zoo 官方新聞稿與官方 FB、
  instagram 加官方 IG；「移園日待查證」的官方最早時點由 2020 年 7 月（Fox News）修正為 2020 年 6 月（園方產仔公告）；
  備注段原稱 Fox News 為「最後一次確認在園的紀錄」已不成立，改記 2021-09 官方 IG
- `sundari-2022-06-14.md` — 居住史加 `Wild Zoo of Saint-Félicien (2023-10-01 – 現在)`、tags 改現居園；
  內文改寫（原稱「留在出生地卡加利」）；sources 補兩則園方官方 IG；抵園日僅「octobre 2023」故標 🚧 暫採 10-01；
  備注新增「生日兩說並存」🚧（官方 IG 記 11/12 juin 2022 vs 現採 2022-06-14）
- `ravi-2022-06-14.md` — 生日 🚧 註記補上 Saint-Félicien 官方 IG 的 6/11–12 佐證方向；內文補姊姊 `sundari` 的去向
- `beilei-2010-06-14.md`／`qin-2005-06-23.md` — 子女表 `Gen Tso` 純文字改為 wikilink，並移除標題的「均無條目」
- `linus-2018-06-23.md`／`udaya-2019-06-20.md`／`anshu-2023-06-18.md`／`aahana-2023-06-18.md`／
  `apple-seed-1-udaya-2026-06-08.md`／`apple-seed-2-udaya-2026-06-08.md`／`apple-seed-3-udaya-2026-06-08.md` —
  內文提到 `sundari` 處補現居魁北克
- `tools/build_db.py` — OFFICIAL_HOSTS 加 `columbuszoo.org`・`zoosauvage.org`；OFFICIAL_FB_PAGES 加 `columbuszoo`；
  OFFICIAL_IG_ACCOUNTS 加 `columbuszoo`・`zoosauvageofficiel`
- `index.md` — 新增一節「海外個體（美國・哥倫布 Kora × Gen Tso 一家）」共 3 筆；`kora`・`sundari` 兩列更新；
  條目總數更新為 898

**🚧 待查證**：
- `gen-tso` 的出生園（Prospect Park Zoo）與現居園（Northeastern Wisconsin Zoo）僅有 RPF，兩次移園日期皆不明；
  唯一官方佐證是 2020 年 6 月他在 Columbus Zoo
- `bandit` 離開 Columbus 的日期不明，現居 Henry Vilas Zoo 僅有 RPF；官方只能確認 2021-09 仍在 Columbus
- `sundari` 抵達 Saint-Félicien 的精確日期不明（園方只寫「十月」），暫採 2023-10-01
- `sundari`／`ravi` 生日：Saint-Félicien 官方 IG 記「11/12 juin 2022」，與現採 2022-06-14（RPF）相左，
  且與 `ravi` 那則舊讀者回報（6/11）方向一致。改生日要連動兩隻 slug 與全部 wikilink，暫不動、待維護者裁定
- 兩筆回報者皆未留暱稱，`data/contributors.json` 未動

---

## [2026-08-06] rename | `ravi`・`sundari` 生日由 2022-06-14 改採 2022-06-11（維護者裁定），兩隻 slug 同步更名

同日稍早那筆記為「暫不動、待維護者裁定」，本筆為裁定後的落實。追加查證結果如下。

**官方來源實查**：
- https://grandpark.seoul.go.kr/board/view/ko/S001006002003/B012.do?bbs_no=103812 — 서울대공원 引進新聞稿：
  加拿大來的雄性記「**2022년 6월생**」（僅到月、無日）；另兩隻（多摩・埼玉）同樣只到月
- https://www.instagram.com/zoosauvageofficiel/p/DOldJGYgQUg/ — Zoo sauvage de Saint-Félicien 官方 IG（2025-09-14，
  已用瀏覽器實讀原文）：「💛Femelle／🥳**Née le 11/12 juin 2022**／🐾Arrivée au zoo en 2023」。
  法文此寫法可讀作「6 月 11 或 12 日」，亦可讀作「11 至 12 日之夜」——**園方本身未指定單一天**
- https://www.calgaryzoo.com/news/red-panda-debut/ 及官網 news／小熊貓展區頁 — 出生園 Calgary Zoo
  **查無 2022 年這一胎的任何公告**；2023 年胎的公告也只寫「五個月大」不給日期；展區頁不列個體名

**非官方來源**：
- RPF #1396／#1397 記 2022-06-14（即原採值）——查無任何官方佐證
- https://namu.wiki/w/%EB%9D%BC%EB%B9%84(%EB%A0%88%EC%84%9C%ED%8C%90%EB%8B%A4) — 나무위키 記 2022-06-11，
  註腳「6월 14일로 알려졌으나 6월 11일이 맞다」所引為 YouTube 社群貼文，發文頻道「실물펜자네」為**同好頻道非官方**；
  與 2026-07 那則讀者回報的 6/11 疑為同源

**裁定**：採 2022-06-11——落在官方唯一給出的區間（11/12）內，且與兩個同好來源一致；原值 06-14 無任何來源支持。
官方仍未指定確切日期，日後園方若公布以園方為準。

**更名條目**：
- `ravi-2022-06-14.md` → `ravi-2022-06-11.md`（`born`、frontmatter `zoos:` 起始日、引言生日同步改）
- `sundari-2022-06-14.md` → `sundari-2022-06-11.md`（同上）

**更新條目**（換 wikilink，共 14 檔）：
- `index.md`（含兩列說明改寫）、`linus`、`udaya`、`anshu`、`aahana`、`dusk`、`usha`、`lian`、
  `apple-seed-1-udaya-2026-06-08`、`apple-seed-2-udaya-2026-06-08`、`apple-seed-3-udaya-2026-06-08`、
  `apple-seed-1-lian-2026-06-19`、`apple-seed-2-lian-2026-06-19`
- `docs/english-variants-audit.md` — 待辦清單的 slug 同步更名
- `ravi` sources 補서울대공원引進新聞稿與 Saint-Félicien 官方 IG；兩隻 extra_sources 補 나무위키

**注意**：`maple-2022-06-14`・`mei-mei-2022-06-14`（溫哥華 Sakura × Arun 那胎）與本次無關，生日不動。

---

## [2026-08-06] verify | `anshu`・`aahana` 生日 2023-06-18 覆查：園方官方佐證成立，維持不動

前一筆處理 `ravi`／`sundari` 生日時順帶發現 Daily Hive 寫 2023 年這胎生於 6 月 17 日，與 wiki 現採 06-18 不符，遂覆查。

**結論：06-18 正確，不改。**

**決定性官方來源**（Calgary Zoo 官方 Facebook，貼文日期 **6 月 18 日**，以瀏覽器實讀）：
> Who is black and white and red all over and **turning three today**? Our male red panda, 'Anshu'!

貼文日期與「今天滿三歲」互證 → 出生日 2023-06-18。園方另有官方影片貼文
「today is the first birthday for our red panda cubs 'Anshu' and 'Aahana'」可佐證同一天
（`/videos/…/1285671739466899/`，該則貼文日期未能讀取，僅作補強）。

**不採 6 月 17 日的理由**：
- https://dailyhive.com/calgary/calgary-zoo-red-panda-twins — Daily Hive（2023-07-11）：
  「Red panda parents 'Udaya' and 'Linus' welcomed their second litter of cubs **on June 17**」，
  記者自述、未註出處、未連園方貼文
- 同日 CTV〈Twinning! Red Panda cubs born at the Calgary Zoo〉與 Global News（2023-07-11，均引園方聲明）
  **都沒給出生日**，只寫本年 6 月生
- 出生園官網 news 亦查無 2023 年這胎的公告（2026 年三胞胎那篇只提「previously welcomed cubs in 2022 and 2023」）

**更新條目**：
- `anshu-2023-06-18.md`／`aahana-2023-06-18.md` — 新增「## 備注」記錄本次覆查與 Daily Hive 的不符；
  sources 補官方一歲生日影片貼文；extra_sources 新增 Daily Hive 連結備查

**⚠️ 工具坑（順手修）**：`build_db` 的 `sources:` 解析**不剝行末 YAML 註解**，註解會連進 URL
（`extra_sources:` 則正常剝除）。本次先在 `ravi`・`anshu`・`aahana` 的 `sources:` 誤加了註解，已全部移除；
全庫掃描確認 `sources:` 區塊現無任何行末註解。要寫註解請放 `extra_sources:`。

---

## [2026-08-07] add | 讀者回報兩筆「圖鑑缺漏」→ `Doofah` × `Sisu` 一家 17 筆建檔（Zoo Knoxville・Potawatomi Zoo）

收件匣兩筆（2026-08-06 提交，回報者未留暱稱）分別回報 `Doofah` 與 `Sisu`。查證後發現**兩筆是同一對配偶**：
兩隻 2024 年起在 Zoo Knoxville 配對，已生兩胎，回報者並未提及這層關係。

**逐筆查證結果**：
- `Doofah` — ♂ 2018-06-21、父 `Ketu` 母 `Tabei`、Rosamond Gifford → Potter Park → Zoo Knoxville：**全部成立**。
  唯一錯誤是「同胞兄弟：Doofah」——雙胞胎兄弟實為 **`Loofah`**（園方取名自《歷險小恐龍》的 Loofah & Doofah）。
- `Sisu` — ♀ 2021-06-17、母 `Maiya` 父 `Justin`、同胞 `Raya`、Potawatomi → Zoo Knoxville：**全部成立**。
  Potawatomi 2024-03-22 的公告未指名去處，去處由 Zoo Knoxville 端官方資料反證。

**官方／一手來源**：
- https://potterparkzoo.org/whats-a-doofah-potter-park-zoo-announces-arrival-of-adorable-male-red-panda/ —
  「born at the Rosamond Gifford Zoo in Syracuse, New York, June 21, 2018」（2019-07-23）
- https://www.zooknoxville.org/animals/red-panda-cubs/ — 2026 年第二胎（6/7 生、雙雄、母 Sisu 父 Doofah、「second litter for the pair」）
- https://www.zooknoxville.org/habitats/red-panda-village/ — 現居個體列 Asha, Doofah, Ganzu, Lincoln
- https://potawatomizoo.org/red-panda-cubs-2021/ — 2021 年這胎的官方頁
- https://www.instagram.com/zooknoxville/p/CMA310lHxN3/ — 官方 IG（美東 2021-03-04）：「Meet Doofa, the new match for Gansu」
- https://www.instagram.com/potawatomizoo/p/CtmpjZKgU2K/ — 官方 IG（2023-06-17）：「It's Raya and Sisu's birthday today… two years old」
- https://www.instagram.com/potawatomizoo/p/C40HttRKvfU/ — 官方 IG（2024-03-22）：Sisu 依 SSP 移往「另一座 AZA 認證動物園」（未指名）
- https://www.instagram.com/zooknoxville/p/DOo_zVRDfXd/ — 官方 IG（2025-09-16）：Sisu 已在 Zoo Knoxville

**新增條目（17 筆）**：
- `doofah-2018-06-21` — ♂（RPF #1224），2018-06-21 生於 Rosamond Gifford，現居 Zoo Knoxville
- `sisu-2021-06-17` — ♀（RPF #1303），2021-06-17 生於 Potawatomi，現居 Zoo Knoxville
- `dr-wallace-2025-06-03`・`mr-darcy-2025-06-03` — ♂♂，Sisu × Doofah 初胎雙胞胎（園方近五年首胎）
- `apple-seed-1-sisu-2026-06-07`・`apple-seed-2-sisu-2026-06-07` — ♂♂，2026 第二胎、未命名，蘋果籽佔位（性別園方已公布）
- `loofah-2018-06-21` — ♂（RPF #1225），Doofah 雙胞胎兄弟，現居 Sunset Zoo
- `sunisa-2024-07-14` — ♀，Loofah 之女，2024-07-14 生於 Sunset Zoo、人工哺育（`sources` 暫空，見下）
- `tabei-2013-06-01`（RPF #912）・`ketu-2011-12-09`（RPF #954）— Doofah・Loofah 之母／父
- `rohan-2015-06-25` 🪽（#343）・`pumori-2015-06-25`（#617）・`ravi-2016-06-27`（#854）・`amaya-2016-06-27`（#855）
  — Tabei × Ketu 的 2015、2016 兩胎，皆為 Doofah・Loofah 的兄姊
- `maiya-2014-06-26`（RPF #553）・`justin-2012-07-01`（RPF #820）— Sisu・Raya 之母／父，現居 Potawatomi
- `raya-2021-06-17`（RPF #1302）— Sisu 雙胞胎姊妹，人工哺育、仍在出生園

**更新條目**：
- `index.md` — 海外個體（美國）新增「Doofah × Sisu 一家」小節（17 列），條目總數 898 → 915
- `tayla-2007-12-08`・`chito-2002-12-18` — 子女表新增 `ketu-2011-12-09`；兩檔原本列「另有子女 RPF #954…待查證、暫無條目」
  的 #954 即是 Ketu，已自待查證清單移除
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `potterparkzoo.org`、`potawatomizoo.org`、`rosamondgiffordzoo.org`；
  `OFFICIAL_IG_ACCOUNTS` 新增 `zooknoxville`、`potawatomizoo`
- `data/zoos.json` — 補 `location_ja`／`location_zh`：Charles Paddock、Fort Wayne Children's、Hamilton、Memphis、
  Potawatomi、Potter Park、Rosamond Gifford、Sunset 八園（原為 null），セントラルパーク動物園 補 `location_zh`

**🚧 標記與待裁定**：
- `Doofah` 抵 Potter Park：官方稿只寫「recently welcomed／is coming to」，暫採 RPF 的 2019-07-01
- `Doofah` 抵 Zoo Knoxville：採官方 IG 公告日 2021-03-04（IG 在 UTC+8 顯示 3/5；WATE 寫「週五引介」＝3/5；
  RPF 記 2021-01-01 疑為月精度佔位）。回報者填的 2021-03-04 因此成立
- `Sisu` 抵 Zoo Knoxville：官方未給抵園日，依 SOP 採送出園公告日 2024-03-22
- `Sunisa` 之母「Simone」**身分待確認**：RPF 唯一的 Simone（#812，2015-06-18 生於 Zoo Boise）記為 2018 年起
  居 Rosamond Gifford，與新聞裡「Sunset Zoo 的 Simone」不符，RPF 亦未記本胎 → 暫不建條目、純文字記載
- Sunset Zoo 官網（sunsetzoo.com／manhattanks.gov）在本環境被 robots 規則擋住無法直讀 → `sunisa` 的 `sources` 暫空
- **祖父母層未建**（RPF-only、待維護者示意）：`Scarlett` #1126・`Madan` #1344（Tabei 之父母）、
  `Ruskan`・`Damini`（Maiya 之父母）、`Ryo`・`Hunter`（Justin 之父母）

**致謝**：兩筆回報皆未留暱稱 → `data/contributors.json` 不動。

---

## [2026-08-07] add | 徳山種雄 `tom-tokuyama`（トム #719）與 `yuu-yuu-1995-07-06`（優優 #595）建檔；補上四筆「父：不詳」

起點是維護者提供的一句日文（がちょん部落格 2019-06-29 `kiki-2000-07-04` 追悼文）：
「義父兄弟にはトムとの間にとくしまの優優（お星様）、大森山の健健（お星様）。」
＝キキ 的同母異父兄弟，是母親美美與トム所生的「とくしま的優優」與「大森山的健健」。
據此上 RPF 核對 #719／#595，補齊徳山 1990 年代前半這條線。

**來源**：
- https://redpandafinder.com/#profile/719 (Tom トム)
- https://redpandafinder.com/#profile/595 (優優，RPF 記為 (no name))
- https://gachon.exblog.jp/27664359/ （同好部落格，非官方 → 僅入 extra_sources）

**新增條目**：
- `tom-tokuyama.md` — Tom トム（RPF #719）♂，野生捕獲個體，生日不詳（故 slug 用「名字-園簡稱」，比照 `ouji-kobe`），
  1989-05-04 確認在 愛媛県立とべ動物園 → 1992-01-23 周南市徳山動物園 → 1998-08-02 歿；血統書 8929。
  已加 `birth_zoo: unknown`，避免首站被標 🐣 出生地
- `yuu-yuu-1995-07-06.md` — 優優（RPF #595）♂，1995-07-06 生於周南市徳山動物園 → 1998-03-25 とくしま動物園 → 2012-01-05 歿；
  `jen-jen-1995-07-06`（健健）之雙胞胎，母 `mii-mii-1992-08-07`，未留子女；血統書 95106（與健健 95107 連號）

**更新條目**：
- `jen-jen-1995-07-06.md` — 父 不詳 → `tom-tokuyama` 🚧；雙胞胎 (no name) → `yuu-yuu-1995-07-06`；補 extra_sources 與備注
- `mii-mii-1992-08-07.md` — 子女表 (no name) #595 轉正為 `yuu-yuu-1995-07-06`；該筆與 `jen-jen-1995-07-06` 的父欄補 `tom-tokuyama` 🚧
- `yon-yon-1994-07-13.md`、`ten-ten-1989-06-26.md` — 純文字「Tom（無條目）」改 wikilink
- `ken-ken-2006-07-18.md`、`purin-1997-07-02.md` — 半血緣兄弟姊妹列的 (no name) #595／純文字 Jen-Jen 改 wikilink
- `ron-ron-1995-06-15.md`、`rin-rin-1993-06-29.md` — 龍龍的父由「不詳」改 `tom-tokuyama` 🚧（RPF #367 記父為 #719；
  トム 1992 起在徳山、玲玲 1993–1995 在徳山，與「1995-03-27 移入宮崎、6 月 15 日產子＝徳山時期受孕」的推算吻合）
- `index.md` — 新增 優優、トム 兩列；條目總數由 898 更新為 **917**（頁首數字先前未隨 8/6 那批新條目更新，本次依
  `ls wiki/*.md` 實算校正）；`_hidden` 筆數由 5 改為 **6**（實際檔案數）

**🚧 待查證（皆為非官方來源帶入，未覆蓋任何既有校訂）**：
1. 優優・健健之父為トム — 僅同好部落格；RPF 兩隻的父欄均空白
2. 「優優」這個名字與其漢字／讀音 — 僅同好部落格；RPF 姓名欄為 (no name)。羅馬拼音暫依既有 優優 條目慣例作 Yuu-Yuu
3. 龍龍之父為トム — RPF 線索，無官方佐證
→ 三項待 周南市徳山動物園 官方名單／園報，或 とくしま・大森山 園方資料佐證

**未處理（留待維護者裁定）**：RPF 記トム另有一子 ロンロン #724（1994-06-24 徳山生、2011-09-06 歿，
母 チィチィ #784，1995-07-12 轉出他園），兩隻皆無條目；wiki 現有四隻 Ron-Ron 均非此隻，是否建檔待裁定。

---

## [2026-08-07] rename+update | トム 生日確定為 1986 年（中國出生），`tom-tokuyama` → `tom-1986`

維護者提供：トム **1986 年生於中國**，愛媛県立とべ動物園是來日後的**中繼地**、非出生園。
原條目因 RPF 記 `birthday: unknown` 而採「名字-園簡稱」fallback slug，今依標準規則改回「名字-生日」。

**來源**：
- 維護者提供（2026-08-07）

**更名條目**：
- `tom-tokuyama.md` → `tom-1986.md`（只知年份故 slug 用 `tom-1986`）

**更新條目**：
- `tom-1986.md` — `born: 1986`；`sources` 首行改記 維護者提供；引言、內文與備注改寫（明示とべ為中繼地、
  非出生園；`birth_zoo: unknown` 保留，居住史首站不標 🐣）；移除原本「生日不詳故用園簡稱 slug」的說明
- `index.md` — 該列改寫並更新生卒為 1986–1998
- 全 wiki wikilink 由 `tom-tokuyama` 換為 `tom-1986`（8 檔）：`ten-ten-1989-06-26`、`yon-yon-1994-07-13`、
  `ron-ron-1995-06-15`、`yuu-yuu-1995-07-06`、`jen-jen-1995-07-06`、`mii-mii-1992-08-07`、
  `rin-rin-1993-06-29`、`index.md`

**未變**：血統書編號 8929、居住史日期（とべ 1989-05-04 起、徳山 1992-01-23 起、1998-08-02 歿）與
三項 🚧 待查證（優優・健健之父、優優的名字、龍龍之父）均照舊。

---

## [2026-08-07] update | 玲玲的母親確認為天天；順帶更正「RPF 無父母記錄」的誤記

維護者提供：`ten-ten-1989-06-26`（天天）是 `rin-rin-1993-06-29`（玲玲）的母親。
據此上 RPF 覆核 #781／#769，發現**本 wiki 原本記的「RPF 無父母記錄」有誤**——RPF 兩邊都有記載。

**來源**：
- 維護者提供（2026-08-07：母為天天）
- https://redpandafinder.com/#profile/781 （記父母為 #769 天天 × #886 チョウチョウ）
- https://redpandafinder.com/#profile/769 （子女 #783・#784・#782・#781・#725）

**更新條目**：
- `rin-rin-1993-06-29.md` — 母 不詳 → `ten-ten-1989-06-26`；父 不詳 → チョウチョウ（RPF #886，生日不詳、無條目）🚧；
  新增半血緣兄弟姊妹 `yon-yon-1994-07-13`（½ 同母）；引言與備注改寫，移除「RPF 無父母記錄」誤記；
  sources 補 維護者提供
- `ten-ten-1989-06-26.md` — 子女表新增 `rin-rin-1993-06-29`；引言補玲玲一系；ℹ️ 註記改為列出
  RPF 記載但尚未建檔的三名子女：#783（無名，1991-06-16）、#784 チィチィ（1991-06-16，雙胞胎）、#782 パンパン（1992-06-27）
- `yon-yon-1994-07-13.md` — 新增半血緣兄弟姊妹 `rin-rin-1993-06-29`（½ 同母）

**連帶影響**：`ron-ron-1995-06-15`（龍龍）的外祖母因此接上 `ten-ten-1989-06-26`，勇勇成為龍龍的舅舅（½）。
另可確認**龍龍之父トム與玲玲之間無父女關係**（玲玲之父為 #886 チョウチョウ，非トム），
先前 🚧 的「龍龍之父為トム」不涉近親配對疑慮。

**待辦**：天天尚有三名子女未建檔（見上）；其中 #784 チィチィ 為 RPF #724 ロンロン 之母，
與先前記的「トム另有一子 #724」是同一條線——要建的話兩隻一起處理較省事。

---

## [2026-08-07] add | `chi-chi-1991-06-16`（チィチィ #784）與 `ron-ron-1994-06-24`（ロンロン #724）建檔

補上前一筆點名的兩隻——天天的女兒チィチィ，以及她與トム所生的ロンロン（アドベンチャーワールド繁殖群之父）。

**來源**：
- https://redpandafinder.com/#profile/784 (チィチィ)
- https://redpandafinder.com/#profile/724 (ロンロン)

**新增條目**：
- `chi-chi-1991-06-16.md` — Chi-Chi チィチィ（RPF #784）♀，1991-06-16 生於 周南市徳山動物園 → 1995-02-01 高知県立のいち動物公園
  → 2001-01-13 日立市かみね動物園 → 2009-12-16 歿（享年 18 歲）；母 `ten-ten-1989-06-26`，父 チョウチョウ（#886）🚧；
  雙胞胎為 RPF #783（無名，未取名故不建條目）；血統書 9169
- `ron-ron-1994-06-24.md` — Ron-Ron ロンロン（RPF #724）♂，1994-06-24 生於 周南市徳山動物園 → 1995-07-12 アドベンチャーワールド
  → 2011-09-06 歿（享年 17 歲）；母 `chi-chi-1991-06-16`、父 `tom-1986`；血統書 9449。
  **wiki 內 Ron-Ron 增為五隻**，五個條目的同名警語已全部互相補齊

**更新條目**：
- `tom-1986.md` — 子女表 ロンロン／チィチィ 由純文字改 wikilink；備注改列四位配偶
- `ten-ten-1989-06-26.md` — 子女表新增 `chi-chi-1991-06-16`；引言補一句；ℹ️ 未建檔子女由三名減為兩名（#783 無名、#782 パンパン）
- `fuu-1998-07-04.md` — 父 由純文字「Ron-Ron（RPF #724）」改 `ron-ron-1994-06-24` wikilink（此前為兩邊各記一半的斷鏈）
- `ron-ron-1995-06-15`／`ron-ron-1995-06-30`／`ron-ron-2002-06-28`／`ron-ron-2013-07-19` — 同名警語補上新條目（#208 原本沒有警語，本次補寫）
- `index.md` — 新增兩列；條目總數更新為 919

**未建（RPF 有名字但資料不全）**：ロンロン 的其餘四名子女 Kai #826（1997-06-26）、Rai #612（1998-07-04，Fuu 之雙胞胎）、
Sei #827／Ten #828（1999-07-06 雙胞胎，皆生後數週至數月夭折，但有正式名可收錄）；母系多為 リン #829（無條目）。
另 天天 之子 パンパン #782（1992-06-27）亦未建。

**🚧 提醒**：チョウチョウ #886 的 RPF 居住史記其 1998-12-14 才入徳山，與「1991／1993 年在徳山生下チィチィ・玲玲」矛盾，
應是 RPF 居住史有缺漏；父系記載暫留 🚧，兩隻姊妹目前僅以同母（½）建立關係。

---

## [2026-08-07] add | `pan-pan-1992-06-27`（パンパン #782）建檔——天天最後一名未建檔的具名子女

前兩筆點名待建的 `ten-ten-1989-06-26`（天天）之子 パンパン，本次補齊。天天的具名子女至此全部建檔完成
（僅餘 RPF #783 無名者依慣例不建）。

**來源**：
- https://redpandafinder.com/#profile/782 (パンパン)
- https://www.gekkan-panda.com/zoo/lesserpanda-kyushu/202001/31-462 （月刊パンダ〈福岡市動物園〉個體表，2020-01 調査；非官方，列為其他參考資料）

**新增條目**：
- `pan-pan-1992-06-27.md` — Pan-Pan パンパン（RPF #782）♂，1992-06-27 生於 周南市徳山動物園 → 1997-04-17 福岡市動植物園
  → 2011-01-13 歿（享年 18 歲）；母 `ten-ten-1989-06-26`，父 チョウチョウ（#886）🚧；無子女；血統書 9263。
  **wiki 內 Pan-Pan／Pang-Pang 增為五隻**（`pan-pan-1983`、`pan-pan-1994-06-17`、`pang-pang-qingyuan`、`pang-pang-nanjing`），
  四個既有條目的同名警語已全部補上本隻

**更新條目**：
- `ten-ten-1989-06-26.md` — 子女表新增 `pan-pan-1992-06-27`；ℹ️ 未建檔子女由兩名減為一名（僅餘 #783 無名）
- `chi-chi-1991-06-16.md` — 半血緣手足新增 `pan-pan-1992-06-27`；備注「パンパン 尚未建條目」改為已建檔並註明父系同為 #886
- `rin-rin-1993-06-29.md` — 半血緣手足補齊為四名（原僅列 `yon-yon-1994-07-13`，本次補 `chi-chi-1991-06-16`、RPF #783 無名者、`pan-pan-1992-06-27`），修正原本的單邊不對稱
- `yon-yon-1994-07-13.md` — 半血緣手足新增 `chi-chi-1991-06-16`、`pan-pan-1992-06-27`
- `pan-pan-1983.md`／`pan-pan-1994-06-17.md`／`pang-pang-qingyuan.md`／`pang-pang-nanjing.md` — 同名警語補上本隻
- `koro-koro-1995-07-02.md` — 備注新增「福岡時期的同居個體」（`pan-pan-1992-06-27` 與 幸／サチ）
- `index.md` — 新增一列；條目總數更新為 920

**旁證**：月刊パンダ〈福岡市動物園〉的「過去のレッサーパンダ」欄記「パンパン／オス／2011年1月13日、天国へ行きました。」
與 RPF 的性別・歿日完全一致（該表未載生年月日）。生年月日與居住史目前仍僅有 RPF 為據。

**🚧 待查證／新發現**：
- 父 チョウチョウ #886 的居住史矛盾（RPF 記 1998-12-14 才入徳山）延續前兩筆的 🚧，本隻同樣僅以同母（½）連結手足。
- **福岡市動物園另有一隻本 wiki 未收的個體：幸（サチ），♀，1995-07-14 生於 広島市安佐動物公園，1997 年 4 月來園，
  2014-01-19 因病歿**（月刊パンダ同一表）。**此隻完全未見於 RPF**，故過去的 RPF 掃描抓不到。
  已在 `pan-pan-1992-06-27` 與 `koro-koro-1995-07-02` 兩處備注記下線索，待維護者裁定是否建檔
  （目前僅有月刊パンダ這一個非官方來源，官方佐證待查広島市安佐動物公園年報／福岡市動物園舊公告）。

---

## [2026-08-07] add | `sachi-1995-07-15`（幸／サチ）與 `mu-mu-1988-07-14`（夢夢 #1347）建檔；安佐「愛愛 14 子」名單由 2 名補到 13 名

前一筆點名的福岡 幸（サチ）依維護者提供的資料建檔。維護者同時提供了她的**完整手足名單**，
一舉把安佐動物公園 2004 年發表所稱「愛愛產下並養育的 14 隻子女」由**已知 2 名補到 13 名**，
並解除既有兩處 🚧（貴貴的父母、王子天天的父母不詳）。

**來源**：
- 維護者提供（2026-08-07）：幸 生卒日 1995-07-15／2014-01-19、出生園 広島市安佐動物公園、1997-04-17 移居福岡市動物園、
  父 中国友友・母 中国愛愛，以及手足名單（安佐星星／姫路風風／王子天天／みさき薫薫／のいち暑暑／双子の兄 安佐和／安佐丹丹／
  池田恋恋／平川貴貴／佐世保鈴鈴／姫路セントラル真真／あやめ夢夢）
- https://redpandafinder.com/#profile/1347 （夢夢；記 あやめ池 移動日 1990-03-23、歿 1998-01-03、血統書 8845）
- https://www.jstage.jst.go.jp/article/asazoo/17/0/17_47/_article/-char/ja （安佐飼育記録集第 17 卷：1988-07-14 產下 2 隻雌性幼獸）
- https://www.gekkan-panda.com/zoo/lesserpanda-kyushu/202001/31-462 （月刊パンダ〈福岡市動物園〉個體表；非官方，列其他參考資料）

**新增條目**：
- `sachi-1995-07-15.md` — Sachi 幸／サチ ♀，1995-07-15 生於 広島市安佐動物公園 → 1997-04-17 福岡市動植物園 → 2014-01-19 病歿（享年 18 歲）；
  母 `ai-ai-1984`、父 `yuu-yuu-1983`；雙胞胎為「和」（♂，讀音未確認、無條目）；無子女。**完全未見於 RPF 與 lineage**，故無 rpf_id
- `mu-mu-1988-07-14.md` — Mu-Mu 夢夢（RPF #1347）♀，1988-07-14 生於 広島市安佐動物公園 → 1990-03-23 近鉄あやめ池遊園地 → 1998-01-03 歿（享年 9 歲）；
  母 `ai-ai-1984`、父 `yuu-yuu-1983`；`shin-shin-1988-07-14`（真真）之雙胞胎；血統書 8845

**更正**：**「沐々」實為「夢夢」**。此前 `shin-shin-1988-07-14`／`yuu-yuu-1983`／`ai-ai-1984` 三處把真真的雙胞胎記為
「Mu-Mu（沐々）」，RPF #1347 的日文名欄與維護者名單（「あやめ夢夢」）兩者皆作**夢夢**，據以更正並建檔。

**更新條目**：
- `yuu-yuu-1983.md`／`ai-ai-1984.md` — 子女表由 2 列增為 4 列（新增 `mu-mu-1988-07-14`、`ten-ten-1991-06-29`、`sachi-1995-07-15`）；
  貴貴列的 🚧 解除；ℹ️ 註記改寫為「14 子中已知 13 名、尚差 1 名」並列出 8 名未建條目者
- `ten-ten-1991-06-29.md` — **父母由「不詳」補為 `yuu-yuu-1983` × `ai-ai-1984`**（維護者確認）；補全血緣手足列；sources 補維護者提供
- `kiki-1992-07-20.md` — 父母與雙胞胎 恋恋 的 🚧 解除（此前僅有同好部落格「がちょん」訃報為據，本次維護者名單一致）；補手足列；恋恋 補記 ♀
- `shin-shin-1988-07-14.md` — 雙胞胎由純文字「沐々」改 `mu-mu-1988-07-14` wikilink；補全血緣手足列
- `sachi-2012-06-18.md` — 新增同名警語（wiki 內 Sachi 增為兩隻）
- `pan-pan-1992-06-27.md`／`koro-koro-1995-07-02.md` — 幸 由純文字改 wikilink；補記三園連動
- `hei-1995-07-18.md` — 新增備注：1997-04-17 三園連動移動
- `index.md` — 新增兩列、天天／貴貴兩列改寫；條目總數更新為 922

**發現：1997-04-17 的三園連動移動**。同一天 安佐 `sachi-1995-07-15` → 福岡、安佐 `hei-1995-07-18` → 徳山、
徳山 `pan-pan-1992-06-27` → 福岡。三隻的移動日完全相同，應為一次串連的個體調度。

**🚧 待查證／待維護者補充**：
- **8 名手足缺讀音與生日、無法決定 slug**，暫以純文字記載：和（安佐，♂，幸之雙胞胎故生日同為 1995-07-15）、
  星星（安佐，♂）、風風（姫路，♂）、薫薫（みさき公園，♂）、暑暑（のいち，♂）、丹丹（安佐，♂）、鈴鈴（佐世保，♀）、恋恋（池田，♀，貴貴之雙胞胎）。
  取得日文讀音後即可依「新增成員流程」逐隻建檔。另 佐世保 的園（現 森きらら）尚未確認是否已登記於 `data/zoos.json`。
- **手足名單的長幼標記不採用**：原始名單把 真真・夢夢 標為「妹」，但兩隻 1988 年生、早於幸 1995 年，與生日矛盾，故只採「是否手足」與「所在園」。
- **幸的生日兩說差一日**：維護者 1995-07-15 vs 月刊パンダ 1995-07-14。依資料來源原則採維護者值（月刊パンダ非官方）。
- **第 14 名子女未知**。安佐 1991 年另有 `kusu-1991-06-24`（楠）與登錄名「愛愛２」的 `ai-1991-06-20` 出生，
  兩隻均不在維護者名單內；若其中之一屬本對後代，則 1991 年會有三胎相距 9 日內出生，需另有繁殖雌性，故暫不推定。
- **無官方來源可補**：安佐年報線上僅回溯至平成 26 年度（2014）、1995／1997 年度未上網；《安佐動物公園飼育記録集》第 22・24 卷無レッサーパンダ論文；
  福岡市動物園官網公告 archive 僅回溯至 2021 年度，2014-01 的訃報已不存在。

---

## [2026-08-07] add + rename | 維護者提供讀音，安佐「愛愛 × 友友」一家再建 6 隻；幸的生日改採月刊、slug 更名

維護者裁定幸的生日改採月刊パンダ的 1995-07-14，並補齊手足讀音（和カズ／風風フウフウ／薫薫クンクン／暑暑ショショ／
丹丹タンタン／鈴鈴リンリン／恋恋レンレン，並確認鈴鈴所在的「佐世保」即現在的森きらら）。據此一次建 6 隻，
安佐初代配偶的 13 名已知子女中**已建條目者由 5 名增為 11 名**。

**來源**：
- 維護者提供（2026-08-07）：幸的生日裁定、上列七個讀音、鈴鈴所在園＝現 九十九島動植物園森きらら
- https://redpandafinder.com/#profile/741 （薫薫；RPF 名字欄作「くンくン」）
- https://redpandafinder.com/#profile/742 （鈴鈴；RPF 名字欄作片假名「リンリン」）
- https://www.gekkan-panda.com/zoo/lesserpanda-kyushu/202001/31-462 （月刊パンダ〈福岡市動物園〉個體表：幸 1995年7月14日）

**重要發現：薫薫與鈴鈴原本 RPF 有收，只是名字對不上。** RPF #741 的日文名欄寫「くンくン」（片假名／平假名混寫，疑輸入錯誤）、
#742 只寫片假名「リンリン」，因此**以漢字「薫薫」「鈴鈴」搜尋 RPF 一律落空**；拿到維護者提供的讀音後才對上號。
兩隻因此有 RPF 的生卒日、居住史與血統書編號可用。**幸・和・恋恋・暑暑・丹丹・星星・風風 與 天天・貴貴 則確認完全不在 RPF／lineage 上。**

**更名**：
- `sachi-1995-07-15.md` → `sachi-1995-07-14.md` — 生日由 1995-07-15 改為 **1995-07-14**（維護者裁定改採月刊パンダ）；
  全 wiki 11 處 wikilink 同步更換；備注改寫並引述月刊原文

**新增條目**：
- `kazu-1995-07-14.md` — Kazu 和／カズ ♂，1995-07-14（由雙胞胎關係推得）生於 広島市安佐動物公園，歿日不詳（`died: "?"`）；`sachi-1995-07-14` 之雙胞胎
- `ren-ren-1992-07-20.md` — Ren-Ren 恋恋／レンレン ♀，1992-07-20（由雙胞胎關係推得）安佐生 → 池田動物園（移居年不詳），歿日不詳；`kiki-1992-07-20` 之雙胞胎
- `kun-kun-1993-07-17.md` — Kun-Kun 薫薫／クンクン ♂（RPF #741）1993-07-17 安佐生 → 1994-11-14 九十九島動植物園森きらら → 1999-10-16 みさき公園 → 2001-04-21 歿（享年 7 歲）；血統書 93108
- `rin-rin-1993-07-17.md` — Rin-Rin 鈴鈴／リンリン ♀（RPF #742）1993-07-17 安佐生 → 1994-11-17 九十九島動植物園森きらら → 2012-10-23 歿（享年 19 歲，**本對子女中最長壽**）；血統書 93109。`kun-kun-1993-07-17` 之雙胞胎
- `sho-sho-noichi.md` — Sho-Sho 暑暑／ショショ ♂，安佐生 → 高知県立のいち動物公園；生日與歿日皆不詳，slug 依無生日慣例取園簡稱
- `tan-tan-hiroshima.md` — Tan-Tan 丹丹／タンタン ♂，在籍 広島市安佐動物公園；生日與歿日皆不詳，slug 取所在城市（比照 `mei-mei-hiroshima`）

**更新條目**：
- `yuu-yuu-1983.md`／`ai-ai-1984.md` — 子女表由 4 列增為 10 列；ℹ️ 註記改寫（13 名已知／11 名已建／尚缺星星・風風・第 14 名）
- `kiki-1992-07-20.md` — 雙胞胎 恋恋 由純文字改 `ren-ren-1992-07-20` wikilink
- `shin-shin-1988-07-14`／`mu-mu-1988-07-14`／`ten-ten-1991-06-29`／`kiki-1992-07-20`／`sachi-1995-07-14` — 全血緣手足列統一重生為 11 名 wikilink ＋ 2 名待建
- 同名警語補齊：`kazu-2019-07-02`（Kazu 兩隻）、`ren-ren-2020-06-29`（Ren-Ren 兩隻）、
  `tan-tan-1986-07-05`／`tan-tan-1992-07-17`／`tan-tan-1998-06-29`／`tan-tan-2001-06-19`（Tan-Tan 五隻）、
  `rin-rin-1986-07-05`／`rin-rin-1989-06-21`／`rin-rin-1989`／`rin-rin-1992-06-21`／`rin-rin-1993-06-29`／
  `rin-rin-1999-07-09`／`rin-rin-2001-06-19`／`rin-rin-2007-06-21`／`rin-rin-2020-06-29`（Rin-Rin 十隻）
- `index.md` — 新增 6 列；條目總數更新為 928

**歿日不詳的處理**：`kazu-1995-07-14`／`ren-ren-1992-07-20`／`sho-sho-noichi`／`tan-tan-hiroshima` 四隻維護者只記「(故)」、
無歿日，一律照 `mei-mei-hiroshima`／`kenta-1998` 的既有慣例寫 `died: "?"`（可避免居住史被誤標 🏡 現居），居住史訖日留空。

**🚧 仍待維護者補充（2 名）**：
- **星星**（安佐，♂）——**讀音未提供**，無法決定 slug（セイセイ／シンシン／ホシホシ 皆有可能），故未建。
- **風風**（フウフウ，姫路，♂）——讀音已有，但「姫路」在註冊表中有**兩座**：`姫路セントラルパーク`（真真的去處）與 `姫路市立動物園`，
  綁園是硬門檻、不可猜，故未建。確認是哪一座即可建檔（無生日者 slug 擬為 `fuu-fuu-himeji`）。
- 另 **第 14 名子女**仍未知（詳見 `ai-ai-1984` 的 ℹ️ 註記）。

---

## [2026-08-07] add | `sei-sei-hiroshima`（星星）與 `fuu-fuu-himeji`（風風）建檔——安佐「愛愛 × 友友」13 名已知子女全部建檔完成

維護者補上最後兩項：**星星＝セイセイ**、**風風所屬的「姫路」＝姫路セントラルパーク**（真真去的那座）。
至此安佐初代配偶的 13 名已知子女**全數建立條目**（四對雙胞胎：真真-夢夢／貴貴-恋恋／薫薫-鈴鈴／幸-和）。

**來源**：
- 維護者提供（2026-08-07）：星星的讀音セイセイ、風風所屬園為姫路セントラルパーク

**新增條目**：
- `sei-sei-hiroshima.md` — Sei-Sei 星星／セイセイ ♂，在籍 広島市安佐動物公園；生日與歿日皆不詳（`died: "?"`），slug 取所在城市（比照 `mei-mei-hiroshima`／`tan-tan-hiroshima`）
- `fuu-fuu-himeji.md` — Fuu-Fuu 風風／フウフウ ♂，安佐生 → 姫路セントラルパーク（與姊姊 `shin-shin-1988-07-14` 同一去處）；生日與歿日皆不詳，slug 取所在城市

**更新條目**：
- `yuu-yuu-1983.md`／`ai-ai-1984.md` — 子女表由 10 列增為 12 列（13 名子女中 12 名為本對已建條目者列於表內，另 1 名即幸的雙胞胎和亦在表中）；
  ℹ️ 註記改寫為「13 名已知全部建檔、尚差 1 名未知」，並補記 RPF #566 ララ（安佐 1996-08-09，`banana-1996-08-09` 之同胎手足）尚無條目
- 全 13 隻的「全血緣兄弟姊妹」列統一重生，互相補齊為 12 名 wikilink（不再有待建的純文字項）
- `sei-sei-1986.md` — 新增同讀音警語（誠誠 vs 星星）
- `fuu-1998-07-04.md`／`fuu-2004-07-13.md` — 新增同拼音警語
- `index.md` — 新增兩列；條目總數更新為 930

**RPF 缺漏的確認方式（留給日後）**：兩隻都以**漢字與片假名兩種寫法**掃過 RPF 的 `ja.name`／`ja.othernames`，
再比對其所在園在 RPF 的在籍名單（安佐＝園 ID 40，1999 年前 13 筆；姫路セントラルパーク＝園 ID 14，1999 年前 5 筆），
確認全部已有對應條目後才判定「不在 RPF 上」。**只掃漢字會漏**——薫薫（RPF 寫「くンくン」）與鈴鈴（RPF 只寫「リンリン」）就是這樣被漏掉過。

**🚧 剩餘待查**：
- **愛愛的第 14 名子女**仍未知。候選線索：`kusu-1991-06-24`（楠）、`ai-1991-06-20`（愛愛２）、RPF #566 ララ（1996-08-09）——三隻皆不在維護者名單內，母系未確認。
- 13 名中 6 隻（和・恋恋・星星・風風・暑暑・丹丹）的**歿日不詳**（`died: "?"`），其中 4 隻連**生日**也不詳。
- 官方一手來源已查到盡頭（安佐年報線上僅至平成 26 年度、飼育記録集第 22・24 卷無レッサーパンダ論文、福岡市動物園公告 archive 僅至 2021 年度）。

---

## [2026-08-07] add | Woburn Safari Park（英國）× Zoo du Bassin d'Arcachon（法國）4 隻建檔——wiki 首度收錄這兩座園

維護者提供 Woburn 官方 IG 的到園 reel（2026-08-06）。順線查出主角 `kochi-2025-06-21` 的法國娘家與雙親，
並補上 Woburn 現居母獸 `mali-2016`。**RPF 完全查無 Kochi／Pici／Chima**（RPF 該園只有 Sanka #1264、Mali #1265 兩筆，
且生日皆記 unknown、無任何 edge），四隻均無 `rpf_id`。

**來源**：
- https://www.instagram.com/woburn_safari/reel/Dbscx5ODXy1/ (Woburn 官方 IG，2026-08-06：Kochi 到園公告)
- https://www.woburnsafari.co.uk/news-and-events/news-2023/happy-birthday-mali/ (Woburn 官網，2023-06-29：Mali 七歲)
- https://www.bedfordindependent.co.uk/red-panda-travels-800-miles-to-woburn-safari-park-for-breeding-program/ (Bedford Independent，2026-08-05：生日 2025-06-21、原居園)
- https://tvba.fr/actu-zoo-bassin-arcachon-panda-roux-naissance/ (TVBA，2025-07-15：Pici 首胎、2025-06-21)
- https://natureetzoo.fr/naissances-de-pandas-roux-en-france-ete-2025/ (Nature et Zoo：Arcachon 一胎，母 Pici、父 Chima)

**新增條目**：
- `kochi-2025-06-21.md` — Kochi ♂，生於 2025-06-21 法國 Zoo du Bassin d'Arcachon（Pici 首胎單仔），2026-08 依 EEP 移居 Woburn Safari Park
- `mali-2016.md` — Mali ♀，2017-07 抵 Woburn，Himalayan Heights 首批住民之一；Kochi 的 EEP 配對對象。生年由園方 2023-06-29 賀七歲文推得，確切日期未公布
- `pici-arcachon.md` — Pici ♀（檔案卡 `limited-profile`），Kochi 之母，Zoo du Bassin d'Arcachon；生日不詳故 slug 取園簡稱
- `chima-arcachon.md` — Chima ♂（檔案卡 `limited-profile`），Kochi 之父，同園；生日不詳故 slug 取園簡稱

**更新條目**：
- `index.md` — 新增「海外個體（英國・Woburn Safari Park ← 法國 Zoo du Bassin d'Arcachon）」一節共 4 列；條目總數更新為 934

**註冊表與工具**：
- `data/zoos.json` — Arcachon 的 canonical 由 lineage 英文名 `Zoo Arcachon Basin` 改為官方法文名 `Zoo du Bassin d'Arcachon`
  （舊名與新聞常用的 `Zoo du Bassin Arcachon La Teste` 收入 `aliases`），與註冊表內其他法國園（`Zoo de Lille`／`ZooParc de Beauval`）一致；
  兩座園補 `zh`／`location_ja`／`location_zh`／`location_en`（沃本＝貝德福德郡沃本、阿卡雄＝吉倫特省拉泰斯特德比施）
- `tools/gen_residence.py` — `CFLAG` 補 `France`（法國 🇫🇷）。**此前註冊表已有 14 座法國園但無任何個體**，故從未觸發；
  現在有了才發現缺，居住史表格原本會不顯示國名與國旗
- `tools/build_db.py` — `OFFICIAL_IG_ACCOUNTS` 補 `woburn_safari`（已核對 woburnsafari.co.uk 頁尾 IG 連結指向此帳號）；
  `OFFICIAL_HOSTS` 補 `woburnsafari.co.uk`、`zoodubassindarcachon.com`

**🚧 待查證**：
- **Kochi 的生日與雙親缺園方一手佐證**。維護者裁定照錄不掛 🚧 旗標：英國側（Bedford Independent，2026-08-05）與法國側
  （TVBA，2025-07-15）兩則獨立報導對 2025-06-21 互相印證，且 Arcachon 當季僅此一胎。Arcachon 官網 actualités 已查無該胎公告（僅列至 2022 年）。
- **Kochi 抵園確切日期不明**——官方 IG 與新聞只說「已安全抵達」，`zoos:` 起訖只能寫到年（`2026`）。
- **Mali 的確切生日、出生園與家系**園方未公布；查到生日後須照 rename 流程改 slug（`mali-2016` → `mali-YYYY-MM-DD`）。
- **Pici／Chima 的生日、出生園與家系**皆不詳，`sources` 記 `維護者提供（2026-08-07）`，`has_official_source` 為 false。
- **Woburn 舊有個體 Mambo（♀，2017-08 自 Birmingham Wildlife Conservation Park 抵園）與 Sanka（♂ RPF #1264，2019-05 抵園）**
  去向未見園方公告，暫不建檔。Kochi 以「新任種公」身分引進，暗示 Sanka 已離園或已歿，但無佐證、不臆測。

---

## [2026-08-07] add | 風子（フウコ）建檔——秋吉台 バウバウ × 香 六姊妹的最後一塊拼圖

維護者提供がちょん部落格的バウバウ 追悼文（2018-01-02），文中逐一列出六名女兒的去向
「ミク＠大崎／ノン＠秋吉台／**風子＠佐世保**／アーヤ＆アーニャ＠日本平／リク＠八木山」，
補上了 RPF #571 缺的名字。該筆此前因「僅以佔位名／無名登錄者不建檔」暫緩，名字查得後補建。

**認定依據**：RPF #571（1997-06-30 生於秋吉台、父 #396 バウバウ、母 #495 香、終居園 #-19 九十九島動植物園森きらら）
與部落格所列「六女中排第二、去向佐世保」四項相符；六名女兒中僅此一隻去向佐世保，無其他候選。

**來源**：
- https://redpandafinder.com/#profile/571 （生卒日、性別、居住史、父母）
- https://gachon.exblog.jp/26293205/ （がちょん「宝宝（バウバウ）さん　ありがとう」2018-01-02：名字「風子」之出處，非官方 → 記入 `extra_sources`）

**新增條目**：
- `fuuko-1997-06-30.md` — Fuuko 風子／フウコ ♀（RPF #571），1997-06-30 生於秋吉台自然動物公園サファリランド，
  2000-03-09 移高知県立のいち動物公園，2005-02-26 移九十九島動植物園森きらら（當時仍稱 佐世保市亜熱帯動植物園），
  2005-11-05 歿，享年 8 歲——`kaori-1991-06-18` × `bau-bau-1994-07-11` 六女中最短命的一隻

**更新條目**：
- `bau-bau-1994-07-11.md`／`kaori-1991-06-18.md` — 子女列／子女表的「（未載名字，RPF #571）」改為 `fuuko-1997-06-30` 連結；註記改寫
- `non-1996-07-05.md`／`a-ya-1998-07-03.md`／`a-nya-1998-07-03.md`／`riku-1999-07-20.md`／`miku-1999-07-21.md` — 姊妹列補上風子（此前五隻都漏記這位 1997 年生的姊妹）
- `index.md` — 新增 1 列（Ran-Ran × Yuu-Yuu 一族表內，接在 `riku-1999-07-20` 之後）；條目總數更新為 935

**🚧 待查證**：
- **漢字「風子」與讀音フウコ 無官方佐證**：漢字出自同好部落格、片假名依維護者提供；羅馬拼音暫依 wiki 既有フウ系條目慣例作 `Fuuko`。
  待秋吉台／のいち／森きらら 官方資料（園報・個體名單）確認後再定，若讀音有異須照 rename 流程改 slug。
- 生卒日與居住史仍僅有 RPF（血統書編號 97102）為據，無園方一手來源。
- 於のいち動物公園的 5 年（2000–2005）是否曾配對、有無子女，RPF 無 edge、亦查無園方紀錄。

## [2026-08-08] update | 已故標記全站統一為 🪽

**說明**：
- 依維護者裁定，wiki 正本的已故標記由 🪐 全面改為 🪽（與網站顯示一致）：條目標題／引言、`index.md`、家族段、`_hidden/` 與 `log-archive/` 舊記錄，共 732 檔 7,976 處。
- 純標記替換，條目總數不變（935）。

---

## [2026-08-08] add | Mogwai 一家四隻建檔——讀者回報「Buffalo Zoo 缺 Mogwai」查證後補建

讀者於「圖鑑缺漏」表單回報 Buffalo Zoo 的 `mogwai` 未收錄，並附 Buffalo Zoo 官方 IG 貼文。
查證後確認確為缺漏，連同雙胞胎姊妹、父、母共四隻一併建檔。**回報所填生日「2021 年 8 月」經查證有誤，
更正為 2021-06-18**：Pueblo Zoo 官方 IG（2021-07-19）寫「baby red pandas had their one month check up today」、
KRDO（2021-11-18）寫亮相時「born five months ago」，兩者與 RPF #1381／#1382 的 6/18 一致；
回報者所本的 NPR 訃聞「born in Aug. 2021」與三者皆矛盾，不採。

**來源**：
- https://www.instagram.com/pueblozoo/p/CRhuVIRlSas/ （Pueblo Zoo 官方 IG，2021-07-19：滿月健檢，生日佐證）
- https://www.facebook.com/pueblozoo/videos/oh-joy-our-red-panda-cubs-mogwai-and-momo-are-making-their-public-debut/602529364498699/ （Pueblo Zoo 官方 FB：命名與公開亮相）
- https://www.instagram.com/buffalo_zoo/p/CxLlDd0Lp5c/ （Buffalo Zoo 官方 IG，2023-09-14：`mogwai` 自 Pueblo 移入、與 Scout 對調）
- https://buffalozoo.org/58027-2/ （Buffalo Zoo 官網，2024-06-06：引進 Himalaya 與 `mogwai` 配對）
- https://buffalozoo.org/red-panda-cub-born-at-the-buffalo-zoo/ （Buffalo Zoo 官網，2025-09-03：`himalaya` × `mogwai` 之女 2025-06-15 生）
- https://nationalzoo.si.edu/animals/news/6807 （史密森尼國家動物園：`shama` × `rusty` 於 SCBI 產下 Clinger／Slash／Shredder）
- https://siarchives.si.edu/collections/siris_sic_13865 （史密森尼機構檔案館：2013 年 `rusty` 逃脫事件）
- https://redpandafinder.com/#profile/1381 / #1382 / #523 / #936

**新增條目**：
- `mogwai-2021-06-18.md` — Mogwai ♂（RPF #1381），2021-06-18 生於 Pueblo Zoo，2023-09-14 移居 Buffalo Zoo；別名 Mowgi／Mowgli
- `momo-2021-06-18.md` — Momo ♀（RPF #1382），`mogwai` 之雙胞胎姊妹，留在出生園 Pueblo Zoo
- `rusty-2012-07-11.md` — Rusty ♂（RPF #523），2012-07-11 生於 Lincoln Children's Zoo，2013-06-24 自史密森尼國家動物園逃脫成名，2022-10-14 歿於 Pueblo Zoo，享年 10 歲
- `priya-2018-06-29.md` — Priya ♀（RPF #936），2018-06-29 生於 Zoo New England Franklin Park Zoo，2023-11-28 歿於 Hogle Zoo，享年 5 歲

**更新條目**：
- `sophia-2002-06-20.md` — 補配偶 Disney、子女 `rusty-2012-07-11` 與 Wayne（RPF #497）；內文補一段
- `shama-2007-07-01.md` — 配偶補 `rusty-2012-07-11`；子女表 Clinger／Shredder／Slash 的「另一方親本」由「不詳」改為 `rusty-2012-07-11`（依史密森尼官方紀錄），生年精確化為 2014-06-26
- `rusty-2005-05-16.md` — 補「⚠️ 注意同名」提示（RPF #473 vs #523）；順手把殘留的 🪐 統一為 🪽
- `momo-2011-06-24.md` — 補「⚠️ 注意同名」提示（茶臼山 Momo vs Pueblo Momo）
- `data/zoos.json` — Buffalo Zoo／Pueblo Zoo／Hogle Zoo 補 `location_ja`（紐約州水牛城／科羅拉多州普韋布洛／猶他州鹽湖城）
- `tools/build_db.py` — `OFFICIAL_HOSTS` 補 buffalozoo.org、pueblozoo.org、nationalzoo.si.edu、siarchives.si.edu；
  `OFFICIAL_IG_ACCOUNTS` 補 pueblozoo、buffalo_zoo；`OFFICIAL_FB_PAGES` 補 pueblozoo
- `index.md` — 海外個體（美國）新增「Rusty 一家」小節共 4 列；條目總數更新為 939

**🚧 待查證**：
- **`mogwai` 抵 Buffalo Zoo 的確切日期**：官方 IG 只寫「recently welcomed」，暫採公告日 2023-09-14
  （RPF 記對調的 Scout 於 2023-09-15 抵 Pueblo）。
- **`priya` 歿日三說**：Salt Lake Tribune 作 2023-11-28（採用）、KSL 作「Wednesday」（＝11-29）、RPF 作 2023-12-02（應為公告日）。
- **`rusty` 歿日**：NPR 與 Washingtonian 皆作 2022-10-14（採用），RPF 記 2022-10-19。
- **`momo` 近況**：官方最後一次明確提及她在園為 2022-10；2023-09 Buffalo Zoo 公告只說 Scout 去 Pueblo「與一隻雌性配對」、未點名。
  暫記現居出生園並填 `last_seen: 2022-10`，未掛 `unverified`——是否要掛請維護者裁定。
- **未建檔的直系親屬**：`mogwai` 之配偶 Himalaya（2023 生，Greenville Zoo 出身）與 2025-06-15 出生之女（尚未命名）、
  `rusty` 之父 Disney（#788）與雙胞胎 Wayne（#497）、`priya` 之父母 Hoppy（#513）／Fia（#653）與其 Hogle 之子 Dorji（#1420）、
  `rusty` × `shama` 的三胞胎 Slash／Shredder／Clinger（#871–873）皆尚無條目，本批未建。

---

## [2026-08-08] add | Mogwai 一家第二批——補齊 8 隻直系親屬

承同日第一批（`mogwai` 一家四隻），依維護者指示補建 `rusty-2012-07-11` 與 `priya-2018-06-29` 的直系親屬。

**來源**：
- https://www.beardsleyzoo.org/press/a-memorable-memorial-day-weekend-at-connecticuts-beardsley-zoo-dorji-the-10-month-old-red-panda-making-his-public-debut （Beardsley Zoo 官方新聞稿，2024-05-24：`dorji` 移入與公開亮相）
- https://nationalzoo.si.edu/animals/news/6807 （史密森尼國家動物園：`shama` × `rusty` 之三胞胎 Clinger／Slash／Shredder）
- https://gephardtdaily.com/local/utahs-hogle-zoo-welcomes-newest-resident-with-birth-of-red-panda-cub/ （2023-06-24：`dorji` 生於 2023-06-23 下午）
- https://www.ksl.com/article/51183370/utahs-hogle-zoo-trades-himalayan-red-pandas-for-chinese-red-panda （2024-11-07：`dorji` 移居 Beardsley、Mow-Mow 移居 SCBI）
- https://www.nbcphiladelphia.com/news/local/elmwood-park-zoo-shredder-red-panda-dies/38843/ ・ https://patch.com/pennsylvania/norristown/elmwood-park-zoo-provides-cause-death-beloved-red-panda （`shredder` 死因心衰竭、`clinger` 死於腦炎）
- https://redpandafinder.com/#profile/788 / #497 / #513 / #653 / #1420 / #871 / #872 / #873

**新增條目**：
- `disney-1997-06-25.md` — Disney ♂（RPF #788），1997-06-25 生於 Indianapolis Zoo，2015-02-21 歿於 Lincoln Children's Zoo，享年 17 歲；`rusty-2012-07-11` 之父，共八名子女
- `wayne-2012-07-11.md` — Wayne ♂（RPF #497），`rusty-2012-07-11` 的雙胞胎兄弟，2015 起在 Brights Zoo
- `hoppy-2015-05-31.md` — Hoppy ♂（RPF #513），`priya-2018-06-29` 之父，SCBI 生的三胞胎之一
- `fia-2015-07-02.md` — Fia ♀（RPF #653），`priya-2018-06-29` 之母，別名 Fiametta／Fiammetta
- `dorji-2023-06-23.md` — Dorji ♂（RPF #1420），`priya` 在 Hogle Zoo 所生、該園首胎，2024 移居 Connecticut's Beardsley Zoo
- `slash-2014-06-26.md` — Slash ♂（RPF #871），`rusty` × `shama` 三胞胎中唯一存活者
- `shredder-2014-06-26.md` — Shredder ♂（RPF #872），2017-01-04 歿於心衰竭，享年 2 歲
- `clinger-2014-06-26.md` — Clinger ♂（RPF #873），2015-11-29 歿於腦部寄生蟲引起的腦炎，未滿 1 歲半

**更新條目**：
- `rusty-2012-07-11.md` — 父／雙胞胎／子女表的純文字親屬改為 wikilink
- `priya-2018-06-29.md` — 父母改為 wikilink；子女表 Dorji 改為 wikilink 並補性別與去向
- `mogwai-2021-06-18.md`／`momo-2021-06-18.md` — ½ 手足（三胞胎與 Dorji）改為 wikilink
- `shama-2007-07-01.md`／`sophia-2002-06-20.md` — 子女表與配偶欄的純文字親屬改為 wikilink
- `data/zoos.json` — Indianapolis Zoo／Bronx Zoo／Brights Zoo／Lee Richardson Zoo／Oglebay's Good Children's Zoo／Elmwood Park Zoo／Connecticut's Beardsley Zoo 補 `location_ja`
- `tools/build_db.py` — `OFFICIAL_HOSTS` 補 beardsleyzoo.org
- `index.md` — 「Rusty 一家」小節擴充為 12 列；條目總數更新為 947

**🚧 待查證**：
- **`dorji` 抵 Beardsley Zoo 的日期**：園方新聞稿只提到亮相前已完成 30 天檢疫，`zoos:` 僅能寫到年（2024）。
- **`clinger` 歿日**：RPF 記 2015-11-29，NBC10 引園方說法為「Dec. 2015」；暫採 RPF。
- **`shredder` 歿日**：RPF 與 Patch 標題皆指向 2017-01-04（1 月 3 日夜間發病）。
- **`wayne`（#497）與 `slash`（#871）現況**：RPF 最後紀錄皆為 2015 年，無後續官方消息，居住史末段標 🚧、未掛 `unverified`（比照 `pumori-2015-06-25` 慣例）。
- **`disney` 的子女出生園有矛盾**：RPF 記 Velcro／Firecracker（2006-06-30 生）出生於 Miller Park Zoo，但同一份資料記 Disney 當時仍在 Memphis Zoo；未逕自調整。
- **仍未建檔**：Mow-Mow（#541，`dorji` 之父）、Gimli（#1092）、Winnie（#499）／Will Smith（#169）、Amberfire（#925）／Wendee（#1123）／Mei-Mei（#498）等配偶與旁系，以及 `mogwai` 的配偶 Himalaya 與 2025-06-15 出生之女。

---

## [2026-08-08] add | Mogwai 一家第三批——旁系 7 隻＋Buffalo Zoo 現行三代 4 隻

承同日前兩批，補齊剩餘旁系；查證 Mogwai 現配偶與後代時，發現 **2025 年那隻幼獸早已命名為 Joy**
（維護者原以為未命名／可能夭折），並查到 **2026-06-10 新生的一對雙胞胎尚未命名**，依蘋果籽制度佔位建檔。

**來源**：
- https://buffalozoo.org/pair-of-endangered-red-panda-cubs-born-at-the-buffalo-zoo/ （官網，2026-07-28：2026-06-10 生雙胞胎、母 Himalaya 父 Mogwai、母獸自行哺育、該園第 14・15 隻）
- https://buffalozoo.org/buffalo-zoos-red-panda-cubs-names-revealed/ （官網，2025-09-20：兩隻皆雌，`joy` 6/15 生於本園、`henny` 來自 Binder Park Zoo）
- https://buffalozoo.org/buffalo-zoo-welcomes-second-red-panda-cub-in-partnership-with-michigan-zoo/ （官網，2025-09-12：Binder Park 幼獸 6/11 生、兩隻皆人工哺育）
- https://buffalozoo.org/buffalo-zoo-bidding-farewell-to-red-panda-cubs-african-lion-sisters/ （官網，2026-04-17：兩隻依 SSP 於 2026-05 離園，去向待公布）
- https://lostcoastoutpost.com/2026/jun/9/new-red-panda-alert-sequoia-park-zoo-welcomes-henn/ （2026-06-09：`henny` 已抵 Sequoia Park Zoo；`joy` 去向仍未見公布）
- https://www.ksl.com/article/51183370/utahs-hogle-zoo-trades-himalayan-red-pandas-for-chinese-red-panda （2024-11-07：`mow-mow` 移居 SCBI）
- https://redpandafinder.com/#profile/541 / #1092 / #498 / #499 / #169 / #925 / #1123

**新增條目**：
- `mow-mow-2014-06-11.md` — Mow-Mow ♂（RPF #541），`priya` 在 Hogle Zoo 的配偶、`dorji` 之父；2024 移居 SCBI
- `gimli-2019-07-06.md` — Gimli ♂（RPF #1092），`priya` 之弟
- `mei-mei-2009-06-28.md` — Mei-Mei ♀（RPF #498），`wayne` 在 Bronx Zoo 的配偶，2017-02-20 歿
- `winnie-2014-07-24.md` — Winnie ♀（RPF #499），`wayne` × `mei-mei` 之女，2022 移居 Saint Louis Zoo
- `will-smith-2015-07-04.md` — Will Smith ♂（RPF #169），Winnie 之弟，2025-04-21 歿於 Happy Hollow Park & Zoo
- `amberfire-2003-06-24.md` — Amberfire ♀（RPF #925，別名 Amber），`disney` 的配偶之一、四子女之母，2019-06-09 歿
- `wendee-1999-06-28.md` — Wendee ♀（RPF #1123，別名 Wen-dee），`disney` 的配偶之一，2016-01-19 歿
- `himalaya-2023.md` — Himalaya ♀，`mogwai` 之配偶；Greenville Zoo 出身，2024-06 移入 Buffalo Zoo。**不在 RPF 上**
- `joy-2025-06-15.md` — Joy ♀，`mogwai` × `himalaya` 初胎，2025-06-15 生於 Buffalo Zoo、人工哺育；2026-05 依 SSP 離園
- `apple-seed-1-himalaya-2026-06-10.md`／`apple-seed-2-himalaya-2026-06-10.md` — 2026-06-10 生的雙胞胎佔位條目

**更新條目**：
- `mogwai-2021-06-18.md` — 配偶改為 wikilink，子女表由「未命名 1 隻」擴為 Joy ＋兩隻蘋果籽；內文改寫
- `priya-2018-06-29.md`／`dorji-2023-06-23.md` — Mow-Mow 改為 wikilink
- `hoppy-2015-05-31.md`／`fia-2015-07-02.md` — 子女表 Gimli 改為 wikilink
- `wayne-2012-07-11.md` — 配偶與子女表改為 wikilink
- `disney-1997-06-25.md` — 配偶與子女表的 Amberfire／Wendee 改為 wikilink
- `data/zoos.json` — Trevor Zoo At Millbrook School／Kansas City Zoo／Saint Louis Zoo／Happy Hollow Park & Zoo／
  Greenville Zoo／Miller Park Zoo／Sequoia Park Zoo 補 `location_ja`
- `index.md` — 「Rusty 一家」小節擴為 23 列；條目總數更新為 958

**🚧 待查證**：
- **`himalaya-2023` 只知生年**：園方 2024-06-06 稱「11 個月大」、2026-07-28 稱「3 歲」→ 2023 年年中生，
  但無確切日期，slug 暫用 `himalaya-2023`。父母亦不詳——Greenville Zoo 2023 年那胎（Mushu／Cricket）父母為
  Asha × Neo，但無來源指她屬該胎，**不逕行採用**。她不在 RPF 上（#1045 的同名個體生於 2013，是別隻）。
- **`joy-2025-06-15` 去向未公布**：園方只說「移完再公布」，`zoos:` 訖只能寫到年（2026）。同伴 `henny`
  （Binder Park Zoo 出身，非本家系血親）已確認於 2026-05 抵 Sequoia Park Zoo。
- **2026 雙胞胎的生日**：園方官網與 BTPM、Niagara Gazette 皆作 6/10，WKBW 作 6/13，採園方。
  兩隻性別未公布（`sex` 留空、tags 不加性別 tag）；1號／2號僅為 wiki 暫編序號。
- **`gimli-2019-07-06` 居住史為推定**：RPF 完全無居住地紀錄，出生園依父母當時所在推定。
- **`wendee-1999-06-28` 居住史有空白**：RPF 記 2001-02-13 至 2003-11-04 所在為「unknown」（園 ID 不在註冊表），`zoos:` 跳過該段。
- **`mow-mow` 在 Binder Park Zoo 時期的四隻子女**（Saffron／Bo／Oolong／Binsa）母方未查證，暫不建檔。

## [2026-08-09] fix | 社群回報 5 筆查證後全數採用（含 `joy-2025-06-15`／`momo-2021-06-18` 去向落實）

Tally「回報資料更正」收件匣 2026-08-07～08-08 的 5 筆，逐筆開來源查證後全部採用（4 筆由 `楊桃` 回報、
Mr. Darcy 那筆未留暱稱）。5 筆的來源皆為官方或官方之忠實轉載，依 CLAUDE.md〈官方來源可直接採用〉直接更正。

**來源**：
- https://www.instagram.com/pueblozoo/p/DY4a2kTj0uB/ （Pueblo Zoo 官方 IG，2026-05-28：`momo` 依 SSP 移出、
  `mr-darcy` 與 `joy` 兩隻新成員抵園並在檢疫中，將接手 Momo 原展示場）
- https://www.soumu.metro.tokyo.lg.jp/documents/d/soumu/20260805_kotarousibou （東京都総務局 官方訃告 PDF：
  `kotarou` 来園日 2007年4月18日、死因 多臓器不全、2024-08-07 入院～2026-06-14 退院之經過）
- https://zoo.city.fukuoka.lg.jp/abouts/history （福岡市動物園官網〈福岡市動物園の歴史〉：
  「平成9年 4月17日　徳山動物園よりレッサーパンダ♂「藩藩（パンパン）」5歳入園 安佐動物公園より♀「サチ」２歳借り受け」、
  「平成16年 7月10日　レッサーパンダの赤ちゃん「タラ」（♂，1頭）が誕生。」、
  照片說明「レッサーパンダ「タラ(生後70日)」…左は母「イクラ」」、「平成23年 1月13日　「パンパン」（♂，18歳）が永眠」）
- https://www.hankyu-hanshin.co.jp/legacy_data/ir/data/ER200303181N1.pdf （阪急電鉄 IR 官方公告，2003-03-18：
  宝塚ファミリーランド 2003-04-07 閉園，シセンレッサーパンダ移轉先為恩賜上野動物園・とくしま動物園）
- https://www.museum.or.jp/news/1449 （日本博物館協会，2011-08-25：`ran` 老衰死，「03年4月に兵庫県の動物園から来園」）
- https://redpandatravel.exblog.jp/27985897/ （同好部落格，2019-02-06：「ファミランにいた２匹はチャチャ君とランちゃん」）

**更新條目**：
- `mr-darcy-2025-06-03.md` — 轉園：`zoos` 加 Pueblo Zoo (2026-05-28 – 現在)、Zoo Knoxville 訖 2026-05-28；
  tag 改 `zoo:Pueblo Zoo`；補官方 IG 於 `instagram`／`sources`；引言現居改 Pueblo Zoo，內文補轉園段與 🚧 抵園日註記
- `joy-2025-06-15.md` — 去向落實為 Pueblo Zoo（與 Mr. Darcy 同批）：`zoos` 補第二段、加 `zoo:Pueblo Zoo` tag、
  補官方 IG 來源；原「現居園待公布」🚧 改為「抵園日暫採官方公告日／身分為比對判定」
- `momo-2021-06-18.md` — 同一則官方 IG 明載她已依 SSP 移出：`zoos` 訖改 2026-05-28、`last_seen` 更新、
  移除 `zoo:Pueblo Zoo` tag、引言現居改「待官方公布」，🚧 改為去向未公布
- `kotarou-2005-07-08.md` — 大島公園来園日由「2007」精確為 `2007-04-18`（江戸川区段訖同步）；補官方訃告 PDF 來源；
  內文補死因 多臓器不全與住院經過（原記「園方訃告未載死因」係當時只見 X 短文）
- `pan-pan-1992-06-27.md` — 補漢字名：`japanese: 藩藩, パンパン`、標題改「藩藩／パンパン」；補福岡市動物園官網來源；
  備注記官方年表對移園日・歿日的佐證，並記 🚧 同頁照片說明作「播播」的寫法歧異、⚠️ 該頁西曆括號誤植（以平成年為準）
- `konta-2004-07-10.md` — 出生名「タラ」（福岡官網年表＋照片說明「左は母「イクラ」」三點吻合）：加 `nicknames: [タラ]`、
  補官網來源、內文與新增「備注」段說明改名（改名發生於移居仙台後，仙台端尚無官方佐證 🚧）
- `ran-1992-06-21.md` — 1994–2003 所在園由「五月山動物園」（RPF #660）更正為「宝塚ファミリーランド」：
  兵庫県 vs 大阪府的矛盾＋阪急官方閉園公告的移轉先＋同好部落格的兩隻名單三方一致；起訖日期仍沿用 RPF；
  補三筆 `extra_sources` 與 🚧 更正理由
- `hoa-hoa-1982-06-15.md`／`yuu-yuu-1990-06-25.md` — 子女表內 `ran` 的居住史字樣同步改宝塚ファミリーランド
- `mogwai-2021-06-18.md`／`himalaya-2023.md`／`apple-seed-1-himalaya-2026-06-10.md`／
  `apple-seed-2-himalaya-2026-06-10.md` — 對 `joy` 的「去向未公布」改為「移居 Pueblo Zoo」
- `index.md` — `mr-darcy`／`joy`／`momo` 三列現居欄與說明更新；Rusty 一家引言的 Joy 去向補上；
  `ran` 列居住史字樣改宝塚；`pan-pan-1992-06-27` 列補漢字、`konta` 列補出生名

**致謝**：
- `data/contributors.json` — `楊桃` 的 note 追記本批 4 筆（Mr. Darcy 那筆回報者未留暱稱，依慣例不列入）

---

## [2026-08-09] fix | 福岡市動植物園補地址與座標；日本園地點欄繁中／日文全面統一

**來源**：
- https://zoo.city.fukuoka.lg.jp/ （福岡市動植物園官網，住所欄）
- 維護者提供（2026-08-09：地址與 Google Maps 點位）

**福岡市動植物園（`data/zoos.json`）**：
- 新增 `address_ja` — `〒810-0037 福岡市中央区南公園1番1号`（照官網原文，非來稿的中文寫法）
- `lat`／`lng` 由 33.5812228／130.3829501 更正為 33.5728036／130.3910108。原值落在大濠公園一帶、
  差約 1 公里；園頁「路線指引」按鈕吃的正是這兩欄，原本會把訪客導錯地方
- `map` 換為維護者提供的現行 Google Maps 連結（舊值為已停用世代的 goo.gl 短網址）

**日本園 `location_ja`／`location_zh` 統一（68 座）**：
- 統一前 68 座裡有 44 座的 `location_ja` 其實寫成繁體中文（`神奈川縣橫濱市`、`靜岡縣濱松市`、
  `東京都台東區`、`鹿兒島縣鹿兒島市平川町`…），ja 語系的日本訪客會看到中文地名。
- 依維護者裁定「其他動物園怎麼做就一致」，比照中國／台灣園既有做法（壽山＝ja `高雄市鼓山区`／
  zh `高雄市鼓山區`）：`location_ja` 一律日文新字体，`location_zh` 一律繁體中文，68 座兩欄補齊。
- 另修 4 筆 lineage 帶入的語序顛倒：`佐世保市長崎県`→`長崎県佐世保市`、
  `東区熊本市熊本県`→`熊本県熊本市東区`、`奈良市 奈良県`→`奈良県奈良市`、
  `那須町 栃木県`→`栃木県那須郡那須町`。順帶統一 `姬路`／`姫路` 兩種寫法。

**更新條目**：
- 515 個條目的「## 居住史」地點欄隨註冊表重生（`gen_residence.py` 衍生，未手改內文）；
  條目總數不變（958）。

**驗證**：`verify.sh` 通過（🔴 0、check_twins 0 錯誤）；`check_i18n.py` 通過；
`build_db` 958 個體與 `wiki/*.md` 檔數相符。

---

## [2026-08-09] fix | 動物園地點欄全庫分流：location_ja／zh／en 一欄一語

接續同日「日本園地點欄統一」，把同一套做法套到其餘 285 座非日本園，並把規則寫進 `CLAUDE.md`
與 `rpf-wiki-SKILL.md`，避免下次建園又混填。

**問題**：`location_ja` 是「日文地點」欄，但全庫有 89 座非漢字圈的園（美、加、英、法、澳…）
存的其實是繁體中文（`紐約州水牛城`、`貝德福德郡沃本`），ja 語系的日本訪客會看到中文地名。
另有 12 座漢字圈的園存了英文、簡體或殘缺值（`Bifengxia Scenic Area, …`／`济南市山东省中国`／
`四川成都`）。

**新規則（一欄一語）**：
- `location_ja`＝當地語言。日本園日文新字体；中／港／澳／台／韓／新加坡園寫日文可讀的漢字或
  片假名（`上海市長寧区`／`香港南区黄竹坑`／`シンガポール`）。**非漢字圈的園留空**——
  ja 語系自動退回 `location_en`，顯示英文遠比顯示中文合理。
- `location_zh`＝繁體中文正本。`location_en`＝英文。

**改動**：
- `data/zoos.json` — 89 座非漢字圈園的繁中地點由 `location_ja` 搬至 `location_zh`、`location_ja`
  改為 `null`；12 座漢字圈園校訂 `location_ja`／補 `location_zh`；6 座（Auckland／Chiang Mai／
  Khao Kheow／National Zoo & Aquarium／Sri Ayutthaya／Welsh Mountain）原本只有無空格英文
  （`Wales,UK`），補上中文地名。非日本園有 `location_zh` 者由 76 座增為 135 座。
- `tools/gen_residence.py` — ①「地點」欄改取 `location_zh → location_ja → location_en`
  （wiki 內文是中文）②**收割回填的目標欄由 `location_ja` 改為 `location_zh`**。
  ②是這次的根因：收割來源是中文內文表格，卻回填到日文欄，非日本園的 `location_ja` 就是這樣
  長年混入繁中的。③ 回寫 `zoos.json` 補上 `encoding="utf-8"`。
- `web/src/lib/data.js` — 更新 `zooLocation` 上方的欄位說明（原註記已過時）。
- `CLAUDE.md`／`rpf-wiki-SKILL.md` — 新增「地點三欄一欄一語」規則與繁中⇄日文對應字表。

**更新條目**：
- 398 個條目的「## 居住史」地點欄隨規則重生（衍生，未手改內文）。中文條目的地點現在一律顯示
  繁中（`神奈川縣橫濱市`、`上海市長寧區`），不再中日文混雜；園名仍沿用日文原名。
  條目總數不變（958）。

**尚未處理**：150 座非日本園三欄只有 `location_en`，中文站顯示英文地名。要補是逐座翻譯的工，
另案處理。

**驗證**：`verify.sh` 通過（🔴 0、check_twins 0 錯誤）；`check_i18n.py` 通過；
`build_db` 958 個體與 `wiki/*.md` 檔數相符；五語系地點取用抽驗正常。

## [2026-08-09] add | `chou-chou-1986`（周周／チョウチョウ #886）建檔——徳山野生出身種雄，7 名子女接上父方

維護者提供 `pan-pan-1992-06-27` 之父的漢字名「**周周**」（讀 チョウチョウ）與「生日不詳」，據此建檔。
該個體原本散見於 8 篇條目的純文字「Chou-Chou／チョウチョウ（#886，無條目）」，現已建立正本並改為 wikilink。

**來源**：
- 維護者提供（2026-08-09：漢字名 周周、生日不詳）
- https://redpandafinder.com/#profile/886 （♂、生日 unknown、歿 2001-09-17、血統書 8856、野生出身）

**新增條目**：
- `chou-chou-1986.md` — Chou-Chou 周周／チョウチョウ ♂（RPF #886），生日不詳（野生捕獲）、
  2001-09-17 歿，1980 年代末～2001 年周南市徳山動物園種雄。**生日完全未知，故 slug 依「無生日→名字-園簡稱」規則**。
  `birth_zoo: unknown`（野生出身，首站不標 🐣）；`zoos:` 起始留空（見下）

**更新條目**：
- `pan-pan-1992-06-27.md` — 父改 wikilink，移除「僅為 RPF 線索 🚧 待查證」（維護者已確認），
  改記「同父同母的 chi-chi／rin-rin 尚未逐一確認、仍標 🚧」
- `chi-chi-1991-06-16.md`／`rin-rin-1993-06-29.md` — 父改 wikilink，🚧 保留為「待官方佐證」
- `pin-pin-1989-06-28.md`／`chin-chin-1991-07-14.md`／`shuu-shuu-2001-07-21.md`／`toku-toku-2001-07-21.md` — 父改 wikilink
- `you-you-1994-07-04.md` — 內文改 wikilink；`### 子女（父：…）` 標題只補漢字**刻意不加 wikilink**
- `ten-ten-1989-06-26.md`／`shin-shin-2003-07-15.md`／`yon-yon-1994-07-13.md` — 子女表／手足敘述只補漢字「周周」，
  **同樣刻意不加 wikilink**：子女表格內的 wikilink 會被 `build_db` 反推成「該表主人的子女」（見 CHANGELOG 既有教訓）
- `index.md` — 徳山那批表格於 `tom-1986` 之後新增一列；`½ 血緣兄弟（母：you-you × 父：…）` 標題改 wikilink；
  最後更新 2026-08-09、條目總數 958 → **959**

**發現：RPF 的「1998-12-14 入徳山」是登錄佔位值，不是抵園日**：
RPF 給 `周周` 的居住史只有「野生 → 1998-12-14 周南市徳山動物園」，但他 13 名子女自 1989 年起全部生於徳山；
且**配偶 Nan-Nan（#890，1992-11-01 歿）也掛一模一樣的 1998-12-14 入園紀錄**——兩隻野生出身個體共用同一日期、
其中一隻當時早已過世。故 `zoos:` 起始留空（渲染「? – 2001-09-17」）、不採該日期。
連帶**撤回**先前 `pan-pan`／`chi-chi`／`rin-rin` 備注裡「該日期與出生年矛盾 → 父子關係存疑」的推論。

**🚧 未採用／待確認**：
- RPF 另記 6 名子女未列入其子女表，避免兩邊不一致：Yan-Yan #722、San-San #723、Pao #779、#783（無名）四隻無條目；
  `cha-cha-1992-07-17` 與 `tan-tan-1992-07-17`（雙胞胎，RPF 記母為 Nan-Nan #890）條目現記「父母不詳」，未逕行覆蓋
- Nan-Nan（南南，#890，野生出身，1992-11-01 歿）尚未建檔——其漢字名「南南」出自既有條目記述，未經維護者確認

---

## [2026-08-09] update | `koro-koro` 補漢字名「丸丸」，兩篇同好部落格列入其他參考資料

**來源**：
- 維護者提供（2026-08-09：漢字名 丸丸）
- https://gachon.exblog.jp/9710272/ （〈最高気温31度　あぢぃ～っ！〉2009-05-11；管理人留言「丸丸と書いてコロコロ」，並記腸閉塞歿）
- https://gachon.exblog.jp/8957222/ （〈輪輪　安らかに！〉2008-11-22；讀者留言「輪輪は、福岡市動植物園の『丸丸（コロコロ）』のお母さん」）

**更新條目**：
- `koro-koro-1995-07-02.md` — `japanese: コロコロ` → `丸丸 / コロコロ`；標題改「Koro-Koro 🪽（丸丸 / コロコロ）」；
  `extra_sources` 補上述兩篇；備注新增「漢字名『丸丸』」（記讀音依據）與「死因」（腸閉塞，非官方轉述）
- `rin-rin-1989.md` — `extra_sources` 補 8957222（本隻訃報）；`koro-koro` 母系的 ℹ️ 註記補第二筆同好佐證
- `index.md` — 該列說明 `Koro-Koro コロコロ` → `Koro-Koro 丸丸／コロコロ`（總數不變）

**讀音備注**：「丸」一般讀 まる／がん，コロコロ 非其常規讀音；福岡市動物園〈歴史〉年表只載片假名「コロコロ」、
無官方漢字。經向維護者確認讀音矛盾後裁定採用「丸丸（コロコロ）」，依「命名以維護者提供為準」收錄、不標待查證。

## [2026-08-09] update + rename | `chou-chou-tokuyama` → `chou-chou-1986`：生年 1986、出身為中國青島市動物園

維護者提供《どうぶつと動物園》所載的**徳山動物園小熊貓家系圖**（由 X @hyper_leopard 2024-01-29 轉載）。
貼文正文載明「**周周（1986～2001）中国・青島市動物園出身**」「**南南（1986～1992）中国・青島市動物園出身**」，
補上了同日建檔時缺的生年與出身園，也推翻了 RPF 的「野生捕獲」。

**來源**：
- 維護者提供（2026-08-09）
- https://x.com/hyper_leopard/status/1751871201319010813 （《どうぶつと動物園》徳山家系圖之轉載；非官方 host → 列 `extra_sources`）

**更新條目**：
- `chou-chou-1986.md`（原 `chou-chou-tokuyama.md`）—— **slug 改名**：生日由「完全不詳」變成「僅知年份」，
  依既有慣例（`tom-1986`／`pan-pan-1983`／`kei-kei-1982`）改用年份而非園簡稱。
  `born: 1986`；移除 `birth_zoo: unknown`；`zoos:` 前段補 `青島動物園 (1986 – )`、徳山段起始留空；
  內文改寫、備注記下與 RPF 的出生地分歧
- `pan-pan-1992-06-27.md`／`chi-chi-1991-06-16.md`／`rin-rin-1993-06-29.md`／`pin-pin-1989-06-28.md`／
  `chin-chin-1991-07-14.md`／`shuu-shuu-2001-07-21.md`／`toku-toku-2001-07-21.md`／`you-you-1994-07-04.md`／
  `index.md` —— wikilink 全部改指新 slug；父行的「生日不詳」字樣移除

**與 RPF 的分歧（採家系圖）**：RPF #886 出生地記為 wild、生日 unknown；家系圖記 1986 年生於青島市動物園。
配偶 Nan-Nan #890 情況相同（家系圖：1986–1992、青島市動物園出身）。家系圖有具體園名與生年、RPF 只有籠統的
wild，故採家系圖；歿年 2001 兩邊一致。這也讓同日記下的「RPF 1998-12-14 入園是佔位值」有了第二層佐證。

**🚧 待裁定：`pan-pan-1992-06-27` 的漢字第三種寫法**：同一張家系圖把 パンパン 寫作「**潘潘**」（1992～2011，
標記為福岡），與福岡市動物園官網年表的「藩藩」、同頁照片說明的「播播」皆不同。三者中只有 潘潘（pān）
在中文讀音上對得上 パンパン。**尚未更動條目**，仍維持 藩藩，待維護者裁定。

## [2026-08-09] update | パンパン 漢字兩寫法並列為別名；徳山家系圖補 5 隻漢字名

承前一筆的《どうぶつと動物園》徳山動物園家系圖（維護者提供）。維護者裁定：`pan-pan-1992-06-27` 的
「藩藩」「潘潘」**兩種漢字並列為別名**，不擇一；並指示把家系圖上的漢字名補進對應條目。

**來源**：
- 維護者裁定（2026-08-09）
- https://x.com/hyper_leopard/status/1751871201319010813 （家系圖轉載；各條目列入 `extra_sources`）

**更新條目**：
- `pan-pan-1992-06-27.md` — `japanese` 由「藩藩, パンパン」改回只留假名 `パンパン`，新增
  `nicknames: [藩藩, 潘潘]`；標題改「（パンパン）」；備注改寫成三出處對照
  （藩藩＝福岡官網年表本文／播播＝同頁照片說明、**未採**／潘潘＝家系圖），並記下中文讀音只有 潘 對得上
- **補漢字名（`japanese: 漢字, 假名`＋標題＋📝 依據＋`extra_sources`）**：
  - `chi-chi-1991-06-16.md` → **姫姫**（圖：姫姫 1991～2009／かみね）
  - `shuu-shuu-2001-07-21.md` → **周周**（圖：周周 2001～2015／日本平；與父 `chou-chou-1986` 同漢字、讀音不同）
  - `toku-toku-2001-07-21.md` → **徳徳**（圖：徳徳 2001～2008／池田）
  - `min-min-2002-07-17.md` → **民民**（圖：民民 2002～2022／埼玉）
  - `aiai-2002-07-17.md` → **愛愛**（圖：愛愛 2002～2022／長崎）
- `index.md` — 上列 6 隻的說明欄補漢字（`shuu-shuu`／`aiai` 各有兩列，皆已補）

**核對方式**：每筆都用「圖上生卒年 ＋ 圖上移動先園略號」對照條目的 `born`／`died`／`zoos`，五筆全數吻合
（姫姫→かみね、周周→日本平、徳徳→池田、民民→埼玉こども、愛愛→長崎バイオパーク）。
圖上其餘有漢字者（虎虎・心心・航航・優貴・風花・優花・賢健・美美・平・遊優・優優）**wiki 早已有漢字**，
與圖一致、不需更動——這也反過來佐證了這次的判讀。

**🚧 圖上有、wiki 無條目者**（未建檔）：星星（1991～????，疑為 RPF #783 チィチィ 的雙胞胎、RPF 記為無名）、
陽陽（1995～????）、風風（1999～2014）、光光（1999～2016）、ブービー（2000～）、南南（86～92，周周之配偶）、
チョコチョコ。

## [2026-08-09] update | `sui-sui-1989-06-29` 補漢字名「松松」

維護者提供（2026-08-09）：西山的 スイスイ 漢字名為「**松松**」。

**旁證**：社群整理的「レッサーパンダ家系」Google Sheet「西山まとめ」分頁第 15 列作「松松スイスイ(故)」
（`docs/西山まとめ對帳/西山まとめ_對帳.md`，非官方）；另全血緣弟名為「楠」，兄弟同取樹名。
「松」的一般讀音為 まつ／しょう、與 スイ 不對應，屬園方寫法（比照 `koro-koro-1995-07-02` 的
「丸丸と書いてコロコロ」）；**主名與 slug 不動**，拼音仍依假名作 Sui-Sui。

**更新條目**：
- `sui-sui-1989-06-29.md` — `japanese` 由 `スイスイ` 改為 `松松, スイスイ`；標題改「Sui-Sui 🪽（松松／スイスイ）」；
  引言後加 📝 依據註記
- `kusu-1991-06-24.md` — 家族段「全血緣兄」的名稱標註補漢字
- `index.md` — 說明欄改「Sui-Sui 松松／スイスイ」

## [2026-08-09] add | 到津の森公園「同同（トントン）」建檔（RPF #703，與群馬 #593 同名不同隻）

維護者提供 RPF #703 與到津の森公園開園 20 週年特設頁；本次補上園方部落格與共同通信報導作為官方一手佐證。
**此隻與既有的 `ton-ton-1994-06-17`（RPF #593，茶臼山→群馬）是不同個體**，兩邊都已加「⚠️ 注意同名」提示。

**來源**：
- https://www.itozu-zoo.jp/blogs/animal/2016/05/7141.php （訃報〈よく頑張りました。お疲れ様。そして、ありがとう。〉2016-05-12）
- https://www.itozu-zoo.jp/blogs/animal/2013/05/4815.php （〈❤Happy Birthday❤〉2013-05-31；「5月で19才」「生まれた日が正確に分からない」）
- https://www.itozu-zoo.jp/blogs/animal/2015/06/6409.php （〈HAPPY BIRTHDAY 同同♪〉2015-06-03；「今年で21歳」）
- https://www.itozu-zoo.jp/blogs/animal/2012/04/3974.php （〈おじいちゃんレッサーパンダさん〉2012-04-24；階梯登不上、改室內飼養）
- https://www.itozu-zoo.jp/blogs/animal/2009/05/2428.php （新レッサーパンダ舎開幕 2009-05-25；「楠と同同というオス２頭」）
- https://www.itozu-zoo.jp/20th/members.php （開園 20 週年〈到津の森公園の動物たち〉；2009／2010／2013「19歳の誕生日」照片）
- https://www.shikoku-np.co.jp/national/life_topic/article.aspx?id=20160512000716 （共同通信 2016-05-12；北九州市發表、國內最高齡、山西省生まれ）
- https://redpandafinder.com/#profile/703

**新增條目**：
- `ton-ton-1994.md` — 同同／トントン（RPF #703），♂，中國野生捕獲、生日僅知 1994 年 5 月，
  1997-12-18 大牟田市動物園 → 2002-02-10 到津の森公園，2016-05-11 歿（享年 22 歲，日本國內最高齡）；
  `birth_zoo: unknown`（出生地為野外／非首站園）

**更新條目**：
- `kusu-1991-06-24.md` — 內文「同同（とんとん）」改為 wikilink，家族段新增「同居夥伴（無血緣）」一行
- `ton-ton-1994-06-17.md` — 標題下加「⚠️ 注意同名」提示，指向本次新建的 `ton-ton-1994`
- `index.md` — Kusu 家族新增「同居夥伴（無血緣）」小節列入 `ton-ton-1994`；`ton-ton-1994-06-17` 該列補同名警語；條目總數 959 → 960

**生日為何只記到年份**：園方自承「生まれた日が、正確に分からない」，僅知 5 月；慶生會日期 2013 年取 5/29、
2015 年取 5/25，且部落格明說 5/29 這個日期「なんのつながりもありませ～ん」，不可當生日。
以 2013 年 19 歲、2015 年 21 歲回推得生年 1994，故 `born: 1994`。

**🚧 待查證**：共同通信報導記出生地為「中国の山西省」，惟山西並非小熊貓自然分布地（styani 分布於四川・雲南一帶），
RPF 僅記 `wild.3`＝Captured Wild Animal（China）。是否指山西省的動物園、或報導轉述有誤，暫無佐證，只記在條目備注。

## [2026-08-09] update | `ton-ton-1994` 補生年／出生地的三組分歧（同好紀錄）

同日建檔後續。維護者提供 4travel 2016-03-26 訪園紀錄，內含「野生出身の可能性・1994年5月は来日した日付の可能性」之說；
另比對兩位訪客對同一塊園內解說牌的不同讀法。**皆為同好來源、無官方佐證，故只補進 `extra_sources` 與備注，`born` 不動。**

**來源（皆列入 `extra_sources`，非官方）**：
- https://4travel.jp/travelogue/11115741 （jillluca 2016-03-26；「野生出身の可能性」「1994年5月は来日した日付の可能性」「実際に生まれたのは1993年の可能性」）
- https://4travel.jp/travelogue/10715320 （jillluca 2012-10-08；解說牌讀作「1994年5月に大牟田市動物園で生まれました」，並記「正確な生年月日は…記載がなかった」）
- https://mihorinh.exblog.jp/20211688/ （レサパン日和 2014-09-20；同牌讀作「1994年生まれ…2002年に大牟田市動物園から来園」）

**更新條目**：
- `ton-ton-1994.md` — `extra_sources` 增 3 筆；備注新增兩則 🚧（「1994年5月」可能是來日日、生年或為 1993；解說牌兩種讀法）
  並在山西省那則補記「查遍大牟田官網與大牟田市 .lg.jp 皆無 1997 年前後的來日／入園紀錄」
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `itozu-zoo.jp`（到津の森公園官網／公園だより；原本漏登記，園方部落格會被判成非官方而不顯示於個體頁「來源」）

**維持 `born: 1994` 的理由**：園方自 2011 年至 2016 年訃告一路以 1994 年計歲（17→19→21→22 歲），官方立場一致；
野生出身說目前只有同好轉述。日後若查到官方引進紀錄支持 1993，需連 slug 一併改名並改所有 wikilink。

**旁證（不寫入正文）**：日本國內出生的小熊貓幾乎集中在 6–7 月，5 月生在日本相當罕見——與「野生出身／中國引進」說相容。

## [2026-08-09] update | `ton-ton-1994` 補血統登録番號 94102 的兩種解讀

**來源**：https://redpandafinder.com/#profile/703 （RPF 資料集 `/export/redpanda.json` 的 `studbook.id` 欄位；
該欄不顯示在 RPF 網頁 UI 上，僅存在於資料集，屬線索級）

**更新條目**：
- `ton-ton-1994.md` — 備注新增一則 🚧：全庫 912 筆有 `studbook.id` 者中，生日與番號皆齊全的 206 筆有 204 筆
  「番號前兩碼＝出生年後兩碼」（`kusu` 9177、`ton-ton-1994-06-17`／`pan-pan-1994-06-17` 9441／9442、
  `koro-koro-1995-07-02` 95102、`kusukusu-2015-07-21` 15157），故 94102 指向 1994；**但**同園的野生捕獲個體
  `taisyu-1989`／`rin-rin-1989` 為連號 8935／8936、對應的是 1989-10-11 入園年而非出生年，
  可見野生捕獲個體的番號年份是「登録（來日）年」——若同理適用，94102 反而支持「1994 年已在日本登録」，
  與「1994年5月＝来日日」之說吻合、與 RPF 的 1997-12-18 入大牟田不符。兩種解讀並存，`born` 仍不動。

## [2026-08-09] update | 全庫補 `studbook_id`（545 筆，RPF 資料集欄位）

新增選填 frontmatter 欄位 **`studbook_id`**，值取自 RPF 資料集 `/export/redpanda.json` 的 `studbook.id`
（**該欄不顯示在 RPF 網頁 UI 上**，只存在資料集裡）。**線索級、不是官方血統登録書**，僅供查詢與生年推定；
`build_db` 不讀取、`pipeline/data/*.json` 不輸出、網站不顯示。

**來源**：
- https://redpandafinder.com/#profile/703 等（RPF 全站資料集 `/export/redpanda.json`，912 筆有 `studbook.id`）

**更新條目**：
- `wiki/*.md` × **545** — 於 `rpf_url:` 之後插入 `studbook_id: "XXXX"`（**一律加引號**，番號有前導零如 `"0992"`）
- `SCHEMA.md` — frontmatter 規範新增 `studbook_id` 欄位說明（含下方兩條判讀規則）

**覆蓋率**：960 條目 → 690 有 `rpf_id` → 545 補入。未補的兩塊——
① **145 隻有 rpf_id 但 RPF 沒填 studbook**（多為 2018 年後出生的新個體：日本 83／美國 20／加拿大 10／台灣 9／中國 9…）；
② **270 隻連 rpf_id 都沒有**（中國 `limited-profile` 檔案卡 182 隻為大宗）。
另 `dorji-2023-06-23`（RPF #1420）RPF 該欄值為 `uknown`（上游拼字錯誤）、`#1398` 為 6 位數異常值，兩者皆略過。

**兩條判讀規則（已寫進 SCHEMA.md）**：
1. **番號前兩碼＝出生年後兩碼**——生日與番號皆齊全的 887 筆中 884 筆吻合（日本 365/367、非日本 519/520），
   為全球通則非日本專用。番號有 4 位（含前導零，`nokaze-2009-06-25` = `0992`）與 5 位兩種。
   例外 3 筆，如 `zorro-2013-07-01`（2013 年生卻是 11129）。
2. ⚠️ **野生捕獲／海外引進個體是「登録年」不是出生年**——`taisyu-1989`／`rin-rin-1989` 為連號 `8935`／`8936`，
   對應的是 1989-10-11 入園日（RPF 對這兩隻 birthday 皆 unknown）。用於推定生年時只能當「不晚於該年出生」的下限。

**用途**：生日不詳的個體（`born` 只有年份或空白）可據此推年份；同胎／同批引進個體常為連號，可交叉驗證關係。

## [2026-08-09] update | `studbook_id` 盤點：移除 2 筆上游誤植；2 隻生年待裁定

承前一筆。用新補的 `studbook_id` 對「生日非完整日期」的個體做了一輪推定與交叉驗證。

**新認識**：該番號不只是「前兩碼＝年份」，而是**依登録日排序的流水號**——同一年內嚴格照生日遞增
（例 9254 yan-yan 06-19 → 9280 mii-mii 08-07）。故 ①同胎／同批必為連號，可交叉驗證關係；
②野生捕獲個體沒有生日、被排在「登録當下」的位置，可用前後鄰居的已知生日**夾出登録時點**。

**已更新條目**：
- `sakuya-2015-06-24.md` — 移除 `studbook_id: "13166"`（13＝2013 與本隻 2015-06-24 生不符；該號已屬
  `mel-2013-07-10`、與其生日吻合），文末補 🚧 註記
- `tsubasa-2006-06-20.md` — 移除 `studbook_id: "1792"`（17＝2017；該號已屬同名的 `tsubasa-2017-07-08`、
  與其生日吻合，疑為 RPF 上游同名混淆），文末補 🚧 註記
- 全庫 `studbook_id` 由 545 → **543** 筆

**🚧 待維護者裁定（尚未更動）**：
1. **`namu-1993`／`kuku-1993` 的 `born: 1993` 幾乎確定是錯的**——番號 8976／8977 為連號，落在
   `8936`（大州 1989-10-11 入園）之後、`9054`（1990-06-26 生）之前，即**1989 年底已在日本登録**；
   現行 1993 是以「最早見於群馬」的 1993-10-26 近似而來，那只是最早目擊、非抵日年。
   **第二層佐證**：Namu 於 1994-06-19 產下雙胞胎，若 1993 年生則隔年繁殖不可能（約 18 個月性成熟），
   1989 年生則 1994 年約 5 歲、合理。建議 `born` 改留空或 1989 以前。
2. **`chou-chou-1986`（周周）可補入園年 1988**——番號 8856 落在 8845（1988-07-14 生）與 8915（1989-06-26 生）
   之間，即 1988 年下半年登録；生於青島 1986、1989-06-28 有第一個子女 `pin-pin-1989-06-28`，時序吻合。
   建議 `zoos:` 改 `周南市徳山動物園 (1988 – 2001-09-17)`（標 🚧）。

**互相印證、不需更動**：`i-i-nagano` 8534 ／ `hoa-hoa-1982-06-15` 8535 連號 → 印證兩隻 1985-03-19 同日入園；
`tom-1986` 8929 → 1989 年中登録，與「1989-05-04 確認在とべ動物園」吻合；`taisyu-1989` 8935／`rin-rin-1989` 8936
連號 → 1989-10-11 同日入園。

**其他上游異常**：`akito-2015-06-22`／`itsuki-2015-06-22` 同為 1522（同胎雙胞胎，分不出哪隻錯，兩邊先留）；
`zorro-2013-07-01` 為 11129（→2011）與 2013 年生不符、無重複號，保留但存疑。

## [2026-08-09] rename+update | `namu` 生年 1993→1987、`kuku` 1993→1990（維護者提供）；解除雙胞胎關係

**來源**：
- 維護者提供（2026-08-09：Namu 生年 1987、Kuku 生年 1990；社群友人整理，**無官方佐證**）

**改名**（slug＝名字-生日，生年變更故一併改名；舊檔已移入 `_to_delete/renamed-2026-08-09/`，待維護者以 git 處理）：
- `namu-1993.md` → **`namu-1987.md`**
- `kuku-1993.md` → **`kuku-1990.md`**

**更新條目**：
- `namu-1987.md` — `born: 1987`；補 `birth_zoo: unknown`（野生捕獲，原本首站群馬被誤標 🐣）；
  `sources` 增「維護者提供（2026-08-09）」；引言改「生年：1987 年（野生捕獲・月日不詳）／享年 7 歲」；
  舊的「以抵日年份為近似」註記改寫為生年來源說明＋旁證
- `kuku-1990.md` — `born: 1990`；補 `birth_zoo: unknown`；同上改寫；另補一則 🚧 矛盾註記（見下）
- **解除雙胞胎關係**：兩隻原依 RPF 記為雙胞胎，新生年相差三年、不可能同胎，故 `## 家族` 的
  「雙胞胎：」改為「同批引進：」（血統書番號連號 8976／8977）。同生群由 222 → 221 組。
  ⚠️ 若不解除，`check_twins` 會因「同生群生日差 > ±1 天」報 E 級並擋 push
- **連帶改寫**：`daura-1994-06-19.md` 移除「（母 Namu 的雙胞胎兄弟、即牠的舅父）」字樣；
  `anri-1994-06-19.md`／`liuxing-1997-06-16.md`／`kuro-1992-07-01.md`／`shin-shin-2000-06-30.md`／
  `luli-2004-06-29.md`／`index.md` 的 `[[wikilink]]` 全部改指新 slug；index 兩列說明同步更新

**🚧 `kuku-1990` 與血統書番號的矛盾（已記在條目內）**：RPF 記其番號 `8977`，與 Namu 的 `8976` 連號，
該段落在 `8936`（大州 1989-10-11 入園）與 `9054`（1990-06-26 生）之間，指向 **1989 年底登録**——
若生年為 1990 則「登録早於出生」。可能是番號年份解讀不適用於本隻、RPF 番號有誤，或生年仍待修正。
**生年以維護者提供者為準**，矛盾記於條目待查。Namu 的 1987 則與 8976（1989 登録）完全相容。

## [2026-08-09] update | `chou-chou-1986` 補徳山入園年 1988（血統書番號推定）

**來源**：https://redpandafinder.com/#profile/886 （RPF 資料集 `studbook.id` = `8856`，線索級）

**更新條目**：
- `chou-chou-1986.md` — `zoos:` 的 `周南市徳山動物園 ( – 2001-09-17)` 補為 **`(1988 – 2001-09-17)`**；
  文末補說明：番號 `8856` 落在 `8845`（`mu-mu-1988-07-14`，1988-07-14 生）與 `8915`
  （`ten-ten-1989-06-26`，1989-06-26 生）之間，該套番號為**依登録日排序的流水號**，故 1988 年下半年登録＝1988 年來日。
  與「1986 年生於青島市動物園」及第一個子女 `pin-pin-1989-06-28`（1989-06-28 生）的時序相符，
  也印證 RPF 所記 1998-12-14 入園為佔位值

## [2026-08-09] rename+update | `kuku` 生年再修正 1990→1989；非雙胞胎而是同批引進（維護者確認）

承前一筆。維護者 2026-08-09 確認：Namu 與 Kuku **不是雙胞胎，而是一起引進**；Kuku 生年改為 **1989**。

**來源**：
- 維護者提供／確認（2026-08-09：Kuku 生年 1989；與 Namu 為同批引進、非雙胞胎。社群友人整理，無官方佐證）

**改名**：`kuku-1990.md` → **`kuku-1989.md`**（舊檔移入 `_to_delete/renamed-2026-08-09/`，待以 git 處理）

**更新條目**：
- `kuku-1989.md` — `born: 1989`；引言享年由 22 改 **23** 歲；`sources` 該行補「與 Namu 為同批引進、非雙胞胎」
- **前一筆記下的 🚧「登録早於出生」矛盾已解除**：番號 `8977`（1989 年底登録）與「1989 年生、當年以幼獸身分
  隨 Namu 一同引進」相符，該註記改寫為 ℹ️ 吻合說明。連號 8976／8977 反過來成為「同批引進」的直接佐證
- `namu-1987.md`／`kuku-1989.md` — 「並非雙胞胎」註記由 🚧 改為 **ℹ️（維護者確認）**，並註明 RPF 記為雙胞胎實為誤記
- `anri-1994-06-19.md`／`daura-1994-06-19.md`／`liuxing-1997-06-16.md`／`shin-shin-2000-06-30.md`／
  `luli-2004-06-29.md`／`index.md` — `[[wikilink]]` 改指 `kuku-1989`；index 該列改「1989–2012」並註明同批引進

**與 RPF 的分歧（採維護者）**：RPF #455／#668 記兩隻為雙胞胎、皆無生日。本 wiki 記為同批引進的獨立個體，
生年 1987（Namu）／1989（Kuku）。血統書番號連號且同為 1989 年底登録，與此一致。

## 2026-08-09　依國際血統登録書（ISB 2008 年版）對齊生年／生日

原檔取自 Wayback（rotterdamzoo.nl 已下架），存於 `sources/isb-red-panda/`；逐筆對帳見
`docs/ISB-2008-對帳-2026-08-09.md`。13 筆生日不一致中 **7 筆採 ISB、6 筆維持原值**。

**採 ISB（含 slug rename）**

- `gou-2000-06-19.md` → `gou-2000-06-29.md` — 生日 2000-06-19 → **2000-06-29**（ISB 00109，生於 SHIRAHAMA；原值僅 RPF #348）
- `i-i-nagano.md` → `i-i-1983.md` — `born` 由留空補為 **1983**（ISB 8534 記 `~1983`、1985-03-19 入茶臼山與原記載吻合），檔案卡改用標準 slug
- `shin-shin-1986.md` → `shin-shin-1984.md` — 生年 1986 → **1984**（ISB 8639 `~1984`）
- `sei-sei-1986.md` → `sei-sei-1984.md` — 生年 1986 → **1984**（ISB 8640 `~1984`）
- `tom-1986.md` → `tom-1987.md` — 生年 1986 → **1987**（ISB 8929 `~1987`）⚠️ 與維護者 2026-08-07 提供的「1986 年生於中國」相差一年，已於條目標記待複核
- `taisyu-1989.md` → `taisyu-1987.md` — 生年 1989 → **1987**（ISB 8935 `~1987`；1989-10-11 入到津與原記載吻合）
- `rin-rin-1989.md` → `rin-rin-1987.md` — 生年 1989 → **1987**（ISB 8936 `~1987`，與大州連號同批引進）
- 上述四隻野生捕獲個體（shin-shin／sei-sei／taisyu／rin-rin）一併補 `birth_zoo: unknown`，居住史首站不再誤標 🐣
- 全 wiki `[[wikilink]]`、`index.md` 顯示文字（`~1989–` → `~1987–` 等）同步更新

**維持原值（ISB 與 RPF 同源，不構成獨立佐證；維護者 2026-08-09 裁定）**

- `koko-2000-06-23.md`／`seina-2000-06-23.md` — ISB 0085／0086 記 2000-06-25（＝RPF 舊值），維持茶臼山官方值 2000-06-23
- `shin-shin-1988-07-14.md`／`mu-mu-1988-07-14.md` — ISB 8844／8845 記 1988-07-13（＝RPF 舊值），維持安佐動物公園飼育記録集第 17 卷的官方值 1988-07-14
- `ron-ron-1994-06-24.md` — ISB 9449 只記 `~ Jun 1994`，粒度低於現值
- `kuku-1989.md` — ISB 8977 記名 **NANA**、`~1987`、1989-06-01 入東北サファリ，與本隻身分不符，🚧 待裁定後再處理

**其他**：`tools/build_db.py` 的 `OFFICIAL_HOSTS` 加入 `rotterdamzoo.nl`，ISB 引用（Wayback 形式）得以列為官方來源。
舊檔備份於 `_to_delete/isb-align-2026-08-09/`。


## [2026-08-09] fix | `gou-2000-06-29` 父母行 wikilink 陷阱：2009 年生的 Koto 被誤掛為 2000 年生個體之母

生年合理性掃描（親代生日 → 子女生日間隔）時抓到一筆負值：`koto-2009-07-09` 被記為
`gou-2000-06-19`（今 `gou-2000-06-29`）之母，母親比孩子晚生九年。

**成因**：該條目 `## 家族` 段原寫「- 母：Koto 🪽（早期同名個體，非 `[[koto-2009-07-09]]`）」——
用來**否定**同名混淆的那個 wikilink，被 `build_db` 的父母行解析當成母親本身，
與既有的父/母行陷阱同型（同一段既有紀錄見 2026-06 起多次）。網站上因此讓 Koto 的
子女表多出一隻 2000 年出生的個體。

**更新條目**：
- `gou-2000-06-29.md` — 母行改為「- 母：Koto 🪽（早期同名個體，與 `koto-2009-07-09` 為不同個體）」，
  wikilink 改 backtick；語意不變、僅去除被誤判的連結

**驗證**：重建後 `pipeline/data/pandas.json` 中 `gou-2000-06-29` 的 `mother`／`father` 皆為 `None`、
`koto-2009-07-09` 的 `children` 僅餘 `mugi-2015-07-13`。

**再掃一次的結果（ISB 對齊後）**：全庫 960 隻、親代→子女間隔 < 640 天者僅餘 3 筆，
皆為「生年只有年份、以該年 12/31 當最晚值」造成的假警報，無真矛盾——
`bambu-2022`（實為 2022-06 生，24 個月）、`himalaya-2023`（園方公告推得 2023 年中，24 個月）、
`i-i-1983`（ISB `~1983` 推定；子 `mi-mi-1985-06-12` 受孕於 1985 年初、在石家莊，若生於 1983 上半年即無矛盾）。
原本 `taisyu`／`rin-rin` 那筆 **172 天**的硬矛盾，已隨 ISB 生年 1989→1987 消除。

## [2026-08-09] update | 大州 × 輪輪 全 12 隻子女（ISB 反查）；父女近親 🚧 解除；新發現 9275 一胎

承前一筆 ISB 對齊。以 `sources/isb-red-panda/ISB-2008-register.csv` 全 2,703 筆掃
**sire=`8935`（大州）或 dam=`8936`（輪輪）**，反查出兩隻的完整子女名單。兩隻分別於 2001-11-16／2008-11-21 歿，
**皆早於該版資料截止日 2008-12-31**，故此名單即為完整名單。

**來源**：
- https://web.archive.org/web/20120128200628/http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%20Panda%20Studbook.pdf
  （International Red Panda Studbook 2008 年版；原檔與逐筆解析存 `sources/isb-red-panda/`）

**查詢結果：大州 × 輪輪 ＝ 12 隻，全部生於到津の森公園**

1990–1997 每年一胎（1996 年無）、多為雙胞胎。既有 wiki 收錄的 7 隻**完全對得上、無漏無多**；
另 5 隻未及命名即夭折（ISB 名字欄空白）——`9051`（1990-06-21 生，10 日）、`9187`（1991-07-18 生，78 日）、
`9262`（1992-06-26 生，9 日）、`9485`（1994-06-30 生，3 日）、`95103`（1995-07-02 生，1 日）——
依〈幼逝寶寶收錄原則〉**不另建條目**，只記入親代與同胎手足的條目。
ISB 中 dam=`8936` 者僅此 12 筆、sire 一律 `8935`，即輪輪無其他配偶。

**🆕 新發現：大州 × 梅梅 一胎（RPF 完全未載）**

ISB `9275`：1992-07-22 生於 ITOZU、1992-07-24 夭折（2 日），sire `8935`、dam `9050`（`mei-mei-1990-06-21` 梅梅）。
梅梅是大州己出之女，故**大州與己出之女交配共兩例**（另一例為 `run-run-1995-07-19` 之母天天），非原先認知的孤例。

**✅ 父女近親 🚧 解除**

ISB `95123`（＝`run-run-1995-07-19`）明載 sire `8935`／dam `9261`（`ten-ten-1992-06-26` 天天），
且該筆的生日・兩次移動・歿日與本 wiki 逐項吻合。原本 2026-08-06 僅憑 RPF ＋ 同好部落格 ＋ 孕期回推裁定登錄、
標 🚧 待官方佐證；ISB 屬官方一手，四項線索全數獲證，🚧 解除。
同理 `koro-koro-1995-07-02` 的母系（原僅同好部落格佐證）由 ISB `95102` 的 dam `8936` 直接證實。

**更新條目**（11 筆）：
- `taisyu-1987.md`／`rin-rin-1987.md` — 子女表改為含 ISB 番號的 12 列（含 5 隻未命名夭折者）；
  新增「與己出之女所生」段（`9275` ＋ `95123`）；引言由「育有 7 隻」改為「育有 12 隻（7 隻活過幼齡）」；
  備注補 ISB 出處、「名單完整」的理由與死因欄；順手修正前一筆遺留的 rename 敘述筆誤（「由 `taisyu-1987` 更名為 `taisyu-1987`」）
- `ten-ten-1992-06-26.md` — 父女近親由 🚧 改 ✅；子女表補 ISB 欄；補同胎雙胞胎 `9262`；
  新增 🚧 **ISB 記本隻名為 `YUU-YUU`**（其餘欄位全吻合、個體同一，疑為到津舊名或誤植；勿與 `yuu-yuu-1990-06-25`／ISB `9052` 混）；
  歿日 2003-03-11 vs ISB 2003-11-03 的分歧記入備注、暫維持現值
- `run-run-1995-07-19.md` — 父／母兩行的 🚧 移除、引言 🚧 區塊改 ✅；家系證據盤點補「2026-08-09 獲官方登録佐證」一條並附 `9275` 旁證
- `mei-mei-1990-06-21.md` — 新增「子女」段（`9275`，與其父大州所生）；引言補該胎；補同胎雙胞胎 `9051`
- `koro-koro-1995-07-02.md` — 母系補 ✅ ISB 佐證；補同胎雙胞胎 `95103`
- `suku-suku-1991-07-18.md`／`souhei-1993-07-11.md`／`nene-1993-07-11.md`／`shota-1997-07-12.md` — 兄弟姊妹行補 5 隻未命名夭折手足（suku-suku 另註同胎 `9187`）
- 上列 9 筆條目的 `sources` 補 ISB Wayback URL

**未新增條目**：5 隻夭折者與 `9275` 皆從未命名，依規則不建頁面、不上站，條目總數不變。

## [2026-08-10] add | 日本平動物園初代五隻（讀者回報 ＋ ISB 2008 覆核）

「レッサーパンダの聖地」静岡市立日本平動物園最早期的五隻，全數建檔。讀者回報（楊桃，2026-08-09，
表單批次 `44G71XY`／回報 ID `WJKM8rQ` `EqZJxB4` `YjJM4Xz` `DqxJ7LN` `OQbJGQ7`）附園方一手來源，
逐欄以 ISB 2008 年版與園方刊物覆核後採用；逐筆判定另存 `docs/日本平初代五隻-驗證-2026-08-10.md`。

**來源**：
- https://www.szga.jp/wp-content/uploads/2021/02/d7562e85a88e3d34098b9e1a69e60e75.pdf
  （《ズーしずおか》84 号，公益財団法人静岡市動物園協会；特集〈日本平動物園 飼育の歴史 ～レッサーパンダ編～〉，第 5 頁）
- https://www.nhdzoo.jp/newspaper/naka.php?newspaper_uid=1215&newspaper_num=31 （〈でっきぶらし〉31 号，1983-02）
- https://www.nhdzoo.jp/newspaper/naka.php?newspaper_uid=1214&newspaper_num=31 （同 31 号，安安訃報）
- https://www.nhdzoo.jp/newspaper/naka.php?newspaper_uid=1509&newspaper_num=211 （〈でっきぶらし〉148 号，2002-07，シンシン訃報）
- https://www.nhdzoo.jp/sp/newspaper/naka.php?newspaper_uid=1873 （〈でっきぶらし〉197 号，2010-12，三世代）
- https://web.archive.org/web/20120128200628/http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%20Panda%20Studbook.pdf
  （International Red Panda Studbook 2008 年版；原檔存 `sources/isb-red-panda/`）

**ISB 對號結果**（全 `styani`，JAZGA「C 系列」野生輸入番號）：

| 個體 | ISB | JAZGA | ISB 記載 |
|---|---|---|---|
| 唐唐 タンタン ♂ | 8019 | 008C | `~1978` 生・父母 WILD／入園 1980-09-16／歿 1986-11-07 |
| 安安 アンアン ♀ | **查無** | — | ISB 未收錄 |
| 渝渝 ユイユイ ♀ | 8220 | 013C | `~1980` 生・父母 WILD／入園 1982-10-08／歿 1991-07-30 |
| 幸幸 シンシン ♂ | 8641 | 036C | **1986-06-23 生於 KYOTO**，父 8016・母 8219／入園 1987-03-11／歿 2002-07-24 |
| キョンキョン ♀ | 8927 | 110C | 1989-07-17 生於 NIHONDAIR，父 8641・母 8220／歿 1990-05-02 |

`8927` 的 sire／dam 直接指向 `8641`／`8220`，三隻互相扣合，親子關係無需推定。

**新增條目**（5 筆）：
- `tan-tan-1978.md` — Tan-Tan 唐唐 タンタン（ISB 8019），生年約 1978（野生捕獲・ISB 推定），
  1980-09-16 入静岡市立日本平動物園、**日本平史上第一隻小熊貓**，1986-11-07 歿。子女 3 隻（1983 三胞胎）全數夭折
- `an-an-nihondaira.md` — An-An 安安 アンアン，唐唐同批配偶，1980-09-16 入園、1981-08-02 因敗血症歿、未及繁殖。
  **生年不詳、ISB 未收錄**（理由見下），slug 依無生日 fallback 規則作 `-nihondaira`
- `yui-yui-1980.md` — Yui-Yui 渝渝 ユイユイ（ISB 8220），生年約 1980，1982-10-08 入園、1991-07-30 歿。
  日本平第一隻成功育仔的母獸；子女 4 隻（1983 三胞胎＋キョンキョン），僅 1 隻活過幼齡
- `shin-shin-1986-06-23.md` — Shin-Shin 幸幸 シンシン（ISB 8641），1986-06-23 生於京都市動物園、
  1987-03-17 入日本平、2002-07-24 歿。第二世代種公，子女僅キョンキョン一隻
- `kyon-kyon-1989-07-17.md` — Kyon-Kyon キョンキョン（ISB 8927），1989-07-17 生於日本平、1990-05-02 因急性肺炎歿。
  **日本平首隻成育個體**、日本國內首例人工哺育成育滿 6 個月以上，園方獲日動水繁殖賞（人工繁殖）

**投稿的一處共通錯誤已更正：「出生動物園＝西安動物園」不成立**

三筆投稿把西安填為出生園。園方《ズーしずおか》84 号原文為「中国の西安市との**動物交換**により、
ノガン2羽、キンケイ6羽とともにレッサーパンダ2頭が**寄贈**されたのが始まりです」；〈でっきぶらし〉197 号記
第一世代為「中国の西安市**から来園した**ペア」——兩者都只講贈與來源、未提出生園。ISB 亦記 `8019`／`8220`
父母皆 `WILD`、生年為推定值 `~`，且 `8019` 的事件列**連 Capture 行都沒有**。
故三隻一律標 `birth_zoo: unknown`、居住史不標 🐣，**且不把西安登記為居住園**（2026-08-10 維護者裁定；
`data/zoos.json` 因此不必新增西安動物園）。西安市與静岡市為友好都市，該批動物屬市級交換。

**安安不在 ISB，是血統簿的真缺漏（非漏查）**

ISB 2008 年版 JAZGA `007C`–`019C` 逐號查過——日本平只有 `008C`（唐唐）與 `013C`（渝渝），
`009C`／`010C` 奈良、`011C` 東京上野、`012C` 到津、`014C`–`018C` 京都／神戸；全庫 1981 年死亡紀錄
逐筆檢視亦無任何日本平個體。安安 1981-08-02 即歿，早於 JAZGA 這批回溯登録的時點，故從未入簿。
本筆投稿因此是**對 ISB 的補充、而非抄錄**。其亞種依同批的唐唐（ISB 記 `styani`）推定，條目已標明為推定。

**一處官方 vs ISB 的分歧（採園方值）**

幸幸的來園日：《ズーしずおか》84 号記 **1987年3月17日**、〈でっきぶらし〉148 号只到月、ISB 記 **11 Mar 1987**，
差 6 天。依「官方／園方資料優先」原則採 03-17，條目 🚧 記下 ISB 值。

**更新條目**（5 筆）：
- `mi-mi-1985-06-12.md` — **移動日依園方刊物由 1988-10-20 改為 1988-10-19**（《ズーしずおか》84 号
  「1988年10月19日には茶臼山動物園からメスのミミが来園し」；原值出自 RPF 與維護者名單）；
  補配偶 `shin-shin-1986-06-23`（兩隻未產仔，〈でっきぶらし〉148 号記「相性が合わないのか」）；`sources` 補 szga PDF
- `nara-2000-07-17.md` — 補記日本平方的来園日 **2001-12-18**（《ズーしずおか》84 号照片說明「楢♀（2001.12.18来園）」），
  與安佐年報的移動日 12/17 差一天、應為送出日與抵達日之別。**值不變**（單日期模型無法同時表達，維持安佐官方值）
- `yuu-yuu-2011-05-28.md` — 「注意同名」補入 `yui-yui-1980`（漢字同為渝渝、讀音 ユーユー vs ユイユイ）
- `index.md` — 新增「日本平動物園 初代（1980–1990）」區塊（三個世代）；條目總數 960 → **965**
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `szga.jp`（公益財団法人静岡市動物園協会，日本平動物園營運協會；
  機關誌《ズーしずおか》PDF 掛在此域）

**未新增條目**：1983-06-27 的三胞胎（1983-06-29 全歿）、幸幸的父母與雙胞胎兄弟（ISB `8016`／`8219`／`8642`）
皆未命名／ISB 名字欄空白，依〈幼逝寶寶收錄原則〉與既有慣例不另建頁面，僅記於各親代條目。

**⚠️ szga.jp PDF 的取得方式（備忘）**：該批 PDF 為**掃描件、9 頁全無文字層**（pdf.js `getTextContent()`
只吐 107 字元），且沙盒 proxy 對 `www.szga.jp` 回 403、`WebFetch` 回「PDF is empty」，Chrome 內建 PDF viewer
的主畫面亦截不到圖。可行解：Chrome 導到同源頁 `https://www.szga.jp/` → 動態 import pdf.js → 同源 fetch PDF
→ 渲染到 canvas 並換掉 DOM → 截圖／zoom 判讀。渲染會超過 CDP 45 秒上限而報 timeout，但畫面其實已畫出、直接截圖即可。

## [2026-08-10] update | 西安來源登記為「西安秦嶺野生動物園」（新增園註冊）

承前一筆。維護者裁定（2026-08-10，覆蓋同日先前「只寫進敘述、不登記園」的決定）：
**中國西安的來源一律登記為西安秦嶺野生動物園**，並補進 `data/zoos.json`。

**來源**：
- https://www.xianzoo.com/ （官網；〈西野概況〉記「西安秦岭野生动物园地处秦岭北麓浅山地带，距西安市区28公里，
  由西安旅游集团投资建设的西北地区首家野生动物园……于2004年5月1日开园」，〈聯繫我們〉記辦公地址
  「西安市长安区滦镇街道西安秦岭野生动物园行政办公楼」；園內設有小熊猫馆）
- https://news.sina.com.cn/s/2004-01-03/04031492422s.shtml （三秦都市報〈2月15日西安动物园搬至秦岭〉2004-01-03，
  新浪轉載，非官方 → `extra_sources`）：記原西安動物園「原附设在西安革命公园内」、1976 年市民義務勞動於**金花北路**興建、
  **1977年5月1日**正式開放，2004-02-15 停止對外開放並「**整体迁往**」秦嶺野生動物園

**新增動物園**：
- `data/zoos.json` — **西安秦嶺野生動物園**（`zh` 西安秦岭野生动物园／`en` Xi'an Qinling Wildlife Park；
  陝西省西安市長安區灤鎮街道；WGS84 `34.0488269, 108.8651073`；`address_ja` 取官網辦公地址；
  `aliases` 含舊名 **西安動物園／西安市動物園** 繁簡與 Xi'an Zoo）。**採 append 而非中間插入**，
  避免無 `lineage_id` 的園合成 ID 平移。
- 座標取自 OpenStreetMap（`tourism=zoo`，WGS84 原生、免百度 BD09MC 三段轉換）；
  ⚠️ 百度地圖此次要求 recaptcha，未走該途徑。

**更新條目**（4 筆）：
- `tan-tan-1978.md`／`an-an-nihondaira.md` — `zoos:` 首站補 `西安秦嶺野生動物園 ( – 1980-09-16)`
- `yui-yui-1980.md` — `zoos:` 首站補 `西安秦嶺野生動物園 ( – 1982-10-08)`
- 上列三筆：`sources` 補官網、`extra_sources` 補三秦都市報；「西安」註記全面改寫（見下）；
  `## 家族` 的「出身」行拆為「出身：中國野生捕獲」＋「來日前：西安秦嶺野生動物園（當時的西安動物園）」兩行
- `index.md` — 「第一世代」小節標題與三列的動物園欄改為「西安 → 日本平動物園」；區塊說明補來源園
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `xianzoo.com`

**兩點刻意保留**：
1. **`birth_zoo: unknown` 不動、居住史不標 🐣**——ISB 記三隻父母皆 `WILD`、生年是推定值 `~`；
   小熊貓不分布於陝西，該批應為四川一帶野生捕獲後集中至西安。西安是「來日前所在」，不是出生園。
2. **🚧 兩層推定已寫進條目**：①「該批個體確實養在西安市的動物園」是推定（園方刊物只寫到市級交換、未指名園）；
   ② 1980／1982 年贈與時該園名為**西安動物園**（金花北路），今日的西安秦嶺野生動物園 2004-05-01 才開園——
   兩者是同一批收藏的前後身（2004-02-15 整體遷入），以現存園登記屬「機構延續性」的取捨，並非同一法人主體；
   官網把自己敘述為「由西安旅游集团投资建设」的新園、未自稱承接西安動物園。

## [2026-08-11] add | 陸（リク）RPF #139 建檔＋修正三處性別誤植（讀者回報查證）

讀者回報（楊桃，2026-08-10）：池田動物園的 `陸`（リク）。全數查證落實，另發現既有條目把牠記成 ♀ 的誤植。

**來源**：
- https://web.archive.org/web/20240515190310/https://ikedazoo.jp/news/レッサーパンダの「陸」が亡くなりました/ （池田動物園 2024-04-27 訃報，**官網原頁已下架**、僅存 Wayback）
- https://www.asahi.com/articles/ASR9H76W5R9HPPZB001.html （朝日新聞 2023-09-16：「2006年に東武動物公園（埼玉県）で生まれたオス」「のいちを経て13年に池田動物園にやってきた」）
- https://www.gekkan-panda.com/zoo/lesserpanda-chugoku/201810/23-39 （月刊パンダ 池田分園個體表：2006年6月5日 オス、2013年1月19日のいちより来園）
- https://4travel.jp/travelogue/10667108 （2012-05-03：「お母さんはチヒロちゃん、お父さんは海君」）
- https://4travel.jp/travelogue/10770115 （2013-04-29：「今年の１月１９日にリク君は岡山市の池田動物園に移動」）
- https://4travel.jp/travelogue/11706325 （2021-07-23：陸與大地為東武出生的三歲差兄弟）
- https://redpandafinder.com/#profile/139 （gender Male／studbook 0664／死亡 2024-04-04；のいち来園 2010-03-02 僅此一家）

**新增條目**：
- `riku-2006-06-05.md` — 陸（リク，RPF #139），♂ styani，2006-06-05 生於東武動物公園，2010-03-02 移のいち、2013-01-19 移池田，2024-04-04 歿（高齢に伴う心機能低下および誤嚥性肺炎），得年 17 歲。母 `chihiro-2003-06-16`、父 `umi-2002-06-24`、雙胞胎 `aya-2006-06-05`

**⚠️ 修正既有誤植（♀ → ♂）**：`chihiro-2003-06-16.md`、`umi-2002-06-24.md` 的子女表把 RPF #139 記為 ♀，`aya-2006-06-05.md` 寫「雙胞胎姊妹」。RPF `gender: Male`、朝日新聞「オス」、園方個體表「オス」、4travel 一律「リク君」，四方一致改為 ♂。

**回報值的一處出入**：回報寫「2013-01-20 由のいち移池田」→ 依園方個體表・4travel 2013 遊記・RPF 三方一致更正為 **2013-01-19**。回報所附的 X 貼文（2024-09-02 同好悼念）本身未載死亡日，4/4 之依據為園方公告。

**更新條目**（6 筆）：
- `aya-2006-06-05.md` — 雙胞胎改 `riku-2006-06-05` wikilink＋「姊妹」改「兄弟」；兄弟姊妹的 `kokoro-2007-09-06` 補 wikilink
- `chihiro-2003-06-16.md`／`umi-2002-06-24.md` — 子女表 `Riku` 補 wikilink、性別 ♀→♂；`Kokoro` 補 wikilink
- `daichi-2009-06-20.md`／`kokoro-2007-09-06.md` — 兄弟姊妹的 `Riku`（與 `Kokoro`）補 wikilink
- `index.md` — Taiyo 家族新增「伯父・姑姑（Daichi 的手足）」小節；條目總數 965 → **966**
- `tools/build_db.py` — `OFFICIAL_HOSTS` 新增 `ikedazoo.jp`（池田動物園官網；訃報等公告發於 /news/）；`OFFICIAL_X_ACCOUNTS` 新增 `love_ikedazoo`（官網頁尾 X 連結指向此帳號）；`OFFICIAL_IG_ACCOUNTS` 新增 `love_ikedazoo`

**⚠️ 備忘：池田動物園官網的舊訃報會消失**——`陸` 那篇 2024-04-27 發布，2025-01-11 的 Wayback 快照就已 404，`/news/` 六頁列表也翻不到。站內搜尋 `?s=` 回空 body、`wp-json` 回 403。查該園個體要走「X 搜日期區間找官方公告推文 → 拿 URL 去 Wayback」。

## [2026-08-11] update | 大地（RPF #137）補記假名 `だいち`——`japanese` 改多值，比照手足慣例

維護者提供：`daichi-2009-06-20` 為日本個體，假名寫作 `だいち`；漢字 `大地` **保留**。
處理方式比照他本人的手足與父親——`japanese` 欄為多值、**漢字擺第一**、逗號分隔，標題括號內用斜線分隔：

| 個體 | `japanese` | 標題 |
|------|-----------|------|
| `yume-2009-06-20`（雙胞胎妹） | `夢, ユメ, ゆめ` | `# Yume 🪽（夢 / ユメ / ゆめ）` |
| `umi-2002-06-24`（父） | `海, ウミ, うみ` | `# Umi 🪽（海 / ウミ / うみ）` |
| `riku-2006-06-05`（兄） | `陸, リク` | `# Riku 🪽（陸 / リク）` |

**來源**：
- 維護者提供（2026-08-11）

**更新條目**：
- `daichi-2009-06-20.md` — `japanese` 由 `大地` 改為 `大地, だいち`；標題改為「Daichi 🪽（大地 / だいち）」
- `index.md` — 該列標籤由「Daichi 大地」改為「Daichi 大地／だいち」（照 `Riku 陸／リク`、`Yume 夢／ユメ` 寫法）

**為什麼不用 `## 別名` 表**：`build_db.py` 只讀 frontmatter（`japanese`／`chinese`／`korean`／`nicknames`／`english_variants`），
`## 別名` 表是純文件、不進 DB 也不上站。漢字／假名並存靠 `japanese` 多值欄即可——`export_json.py` 的
`extract_kanji()` 以 `[\s/／（）()、,，｜|・･]+` 切詞取第一個漢字 token，會正確得出 `kanji: 大地`。
`夢`／`海`／`陸` 三隻都沒有 `## 別名` 段，此條目也不需要。

**🚧 待查證**：園方（池田動物園／東武動物公園）官方公告的正式寫法尚未取得佐證——池田官網訃報已下架、`?s=` 與 `wp-json` 皆不可用（見同日池田備忘）。
另有片假名 `ダイチ` 的線索：4travel 池田遊記〈春のレッサーパンダ紀行【６】〉寫「ダイチ君、ひよりちゃん」（同園同期、與 `hiyori-2009-07-08` 並列，可確認即本個體），
惟同好遊記非官方，本輪未收進 `japanese`；若要補成 `大地, ダイチ, だいち`（比照 `夢`／`海` 的三形式）只需加一個 token。

## [2026-08-11] update | ISB 2008 對帳：陸 #139 性別得到官方佐證，並補出 4 隻只見於 ISB 的夭折手足

承前一筆。維護者提醒後補做國際血統登録書（ISB 2008 年版）對帳。

**來源**：
- https://web.archive.org/web/20120128200628/http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%20Panda%20Studbook.pdf （Rotterdam Zoo 編，官方一手；本地原檔 `sources/isb-red-panda/`）

**① 陸（ISB `0664`）完全吻合，性別多一份官方佐證**：
`M / 5 Jun 2006 / sire 0263（海）/ dam 0362（チヒロ）/ styani / TOBU 出生 / JAZGA 597C`。
與 RPF、朝日新聞、園方個體表、4travel 五方一致 → **♂ 已無疑義**。該版資料截止 2008-12-31，
未涵蓋 2010 のいち移動與 2024 死亡，故對那兩項既無佐證也無矛盾。

**② 反查 sire 0263 / dam 0362 補出 4 隻 RPF 完全沒有的夭折子女**（依〈幼逝寶寶收錄原則〉未命名者不建條目，只寫進親代與同胎手足）：
- `0781` ♂ 2007-09-06 生、**當日夭折**——是 `kokoro-2007-09-06` 的雙胞胎兄
- `0875` ♂／`0876` ♀ 2008-07-07 生、**當日夭折**；`0877` ♂ 2008-07-07 生、2008-07-09 夭折（三胞胎）

チヒロ × 海 的子女因此由 5 隻更正為 **9 隻**（成年 5／夭折 4）。

**更新條目**（4 筆）：
- `riku-2006-06-05.md` — `sources` 補 ISB（Wayback，`_unwrap_wayback` 判為官方）；備注新增「ISB 對帳」段
- `chihiro-2003-06-16.md` — 補 `studbook_id: "0362"`（ISB 生日 16 Jun 2003、NAGANO→TOBU 18 Dec 2005 與本條目完全吻合）；
  子女表補 4 隻夭折個體、引言「5 隻子女」改「9 隻子女」
- `umi-2002-06-24.md` — 同上（子女表與引言）。⚠️ ISB `0263` 的 `name` 欄是 `JAZGA`（已知的欄位污染），
  認個體靠生日 24 Jun 2002 ＋ 出生地 TOMIOKA（＝群馬サファリパーク，富岡市）＋ 2004-01-28 移 TOBU
- `kokoro-2007-09-06.md` — 家族段新增「雙胞胎：未命名 ♂（ISB 0781）」

**先前那筆的補充**：`aya-2006-06-05` 的 `studbook_id "0665"`（AYA，同胎連號）也在此次對帳中確認；
其 ISB 移動記錄 `TOMIOKA 11 Dec 2007 Transfer` 與條目的群馬サファリパーク 2007-12-11 吻合。

## [2026-08-11] add | 夢（ユメ，RPF #567）——Daichi 的雙胞胎妹妹補建

維護者提供 東武動物公園 的 `ユメ／夢`（2009-06-20 – 2011-12-03）。此前 `daichi-2009-06-20`、
`chihiro-2003-06-16`、`umi-2002-06-24`、`aya-2006-06-05`、`riku-2006-06-05`、`kokoro-2007-09-06`
六筆條目都以純文字「Yume（RPF #567）」記載，本次建檔並全數改為 wikilink。

**來源**：
- https://redpandafinder.com/#profile/567 （夢／Yume）：♀・2009/6/20 生・2011/12/3 歿・`studbook.id 0979`・
  父母邊指向 #220 チヒロ 與 #368 海——與維護者提供一致。⚠️ 該筆 RPF 記錄**完全沒有 location 欄位**，
  所屬園（東武動物公園）依維護者提供並由下列遊記佐證
- 維護者提供（2026-08-11）
- https://4travel.jp/travelogue/10620554 （同好遊記，非官方，列 `extra_sources`）：2011-11-12 參觀時
  「ユメ ２歳」與母 チヒロ・姊 ココロ 同場於東武；文末追記「１２月３日、ユメちゃんが心臓の病気のために
  天国に旅立ってしまいました、僅か２歳半でした」——歿日與死因的唯一線索

**新增條目**：
- `yume-2009-06-20.md` — 夢 ユメ（RPF #567，ISB `0979`），♀，2009-06-20 生於東武動物公園、
  2011-12-03 歿於同園（享年 2 歲）；`daichi-2009-06-20` 之雙胞胎妹妹

**更新條目**（7 筆）：
- `daichi-2009-06-20.md` — 引言與「雙胞胎」行的 Yume 改 wikilink
- `chihiro-2003-06-16.md`／`umi-2002-06-24.md` — 子女表 Yume 該列改 wikilink
- `aya-2006-06-05.md`／`riku-2006-06-05.md`／`kokoro-2007-09-06.md` — 兄弟姊妹行的 Yume 改 wikilink
- `index.md` — Taiyo 家族「伯父・姑姑（Daichi 的手足）」新增一列；條目總數 966 → **967**

**🚧 待查證**：東武動物公園官網未見 2011 年訃報，死因「心臓の病気」與居住史目前僅有同好遊記佐證；
ISB 2008 年版資料截止 2008-12-31，涵蓋不到 2009 年出生者，故 `0979` 尚無血統登録書原文可對。

## [2026-08-11] add | 春（シュン，旧名 龍龍／ロンロン，RPF #665）與 ミンミン（RPF #664）——花花 13 子女全數建檔

維護者提供一筆資料卡：「春シュン、旧名龍龍(故)／birth 1995年6月17日／出生zoo 長野市茶臼山動物園／
father 市川勇勇(故)／brother 兄京都茶々(故)・群馬トントン(故)／sister 姉枚方リンリン(故)・とくしまラン(故)・
茶臼山ミンミン(故)・天王寺パンパン(故)／kids 野毛山海(故)・大牟田空(故)」。
**「旧名龍龍」正是缺的那一塊**：wiki 原本只能記「維護者名單的『群馬春』疑即 RPF #665（ロンロン），惟名字不符」，
龍龍 即 ロンロン 的漢字，疑點解除。順帶以 ISB 反查補出雙胞胎 ミンミン 的歿日並建檔。

**來源**：
- 維護者提供（2026-08-11）——上述資料卡
- `sources/isb-red-panda/ISB-2008-register.csv`（ISB 2008 年版，官方一手）：
  - `9593 M 17 Jun 1995 sire 9052 dam 8535 RON-RON | NAGANO Birth | TOMIOKA 28 Jan 1998 Transfer | 19 Nov 2004 Death [Infection associated / Digestive]`
  - `9394 F 27 Jun 1993 sire 9052 dam 8535 | NAGANO Birth | 17 Aug 2001 Death [Respiratory]`（無 Transfer＝終生茶臼山）
  - `9393 M 27 Jun 1993 …`（茶々，**sex=M**）／`9052 M 25 Jun 1990 ICHIKAWA Birth | NAGANO 17 Oct 1991`（勇勇）
  - 掃 `sire==9593` 恰為 `0263`（♂ 海）與 `0264`（♀ SORA），母皆 `9994` メロン，2002-06-24 生於 TOMIOKA
- https://www.gekkan-panda.com/zoo/lesserpanda-kinki （月刊パンダ・きんきちほう，非官方 → `extra_sources`）：
  京都市動物園個體表「茶々(チャチャ)｜1993年6月27日｜**オス**｜1995年6月、長野市茶臼山動物園から来園…
  2016年2月17日、天国へ行きました」

**新增條目**（2 筆）：
- `shun-1995-06-17.md` — 春 シュン（旧名 龍龍／ロンロン；RPF #665、ISB `9593`），♂，1995-06-17 生於長野市茶臼山動物園、
  1998-01-28 與兄 `ton-ton-1994-06-17` 同日移群馬サファリパーク、2004-11-19 歿（享年 9 歲）；`meron-1999-07-11` 之配偶
- `min-min-1993-06-27.md` — ミンミン（RPF #664、ISB `9394`），♀，1993-06-27 – 2001-08-17，`cha-cha-1993-06-27` 之雙胞胎，
  終生留茶臼山、無子女

**更新條目**（11 筆）：
- `cha-cha-1993-06-27.md` — **性別 ♀ → ♂**（ISB 9393 `sex=M`＋月刊パンダ「オス」＋維護者資料卡「兄京都茶々」三方一致；
  原 ♀ 出自 RPF #663，屬線索級）；補 `- 雙胞胎：` 行、月刊パンダ 進 `extra_sources`
- `hoa-hoa-1982-06-15.md` — 子女表 ミンミン／春 兩列改 wikilink 並補生卒；「11 隻已建條目、餘 2 隻資料不足」改為 13 隻全建
- `ton-ton-1994-06-17.md`／`ran-1992-06-21.md`／`rin-rin-1992-06-21.md`／`pan-pan-1994-06-17.md`／`ai-ai-1987-05-31.md`
  — 手足行的純文字 ミンミン／ロンロン 改 wikilink
- `yuu-yuu-1990-06-25.md` — 花花那批子女表全數改 wikilink，並補 1996 年夭折的 ISB 9687 一列
- `meron-1999-07-11.md`／`umi-2002-06-24.md`／`sora-2002-06-24.md` — 配偶／父欄的純文字「Ron-Ron（RPF #665）」改 wikilink；
  `sora` 補漢字「空」（維護者提供）與 `studbook_id "0264"`，`umi`／`sora` 新增「## 備注」段
- `index.md` — 茶臼山區塊新增 ミンミン／春 兩列、茶々 性別改 ♂、Sora 補漢字；條目總數 967 → **969**；
  順手修 `jirou-1990-07-06` 該列壞掉的 🪽

**✅ 本輪解除的 🚧**：
- 「群馬春 vs RPF #665 ロンロン 名字不符」（記於 `hoa-hoa`／`ton-ton`／`yuu-yuu-1990`／`meron`）
- **花花 1992 年後子女的「父為勇勇係研判」**：RPF 只給名字「Yuu-Yuu」須研判是哪一隻，ISB 則以**番號**指名 —— 9256／9257／
  9393／9394／9441／9442／9593／9687 的 `sire` 全為 `9052`＝`yuu-yuu-1990-06-25`（1990 生於 ICHIKAWA、1991-10-17 移 NAGANO）。
  `ran`／`rin-rin`／`cha-cha`／`ton-ton` 的「父為研判」註記與 `yuu-yuu-1990` 子女表的 🚧 一併移除
- ミンミン 的歿日不明、生日僅靠雙胞胎推得（ISB 9394 證實生日並補歿日 2001-08-17）

**🚧 仍待查證**：
- **改名的時點與方向無佐證**：研判為「茶臼山出生時名龍龍 → 1998 移群馬後改稱春」（龍龍 合於茶臼山當時的中式疊字命名、
  ISB／RPF 的登録名亦為 RON-RON），但兩園皆查無公開紀錄。月刊パンダ 群馬頁是 2011 年快照（只有 彩／太陽／后）、
  茶臼山〈動物情報〉線上存檔僅回溯至 2003 年度
- **「龍龍」漢字的歸屬**：1995 年 6 月共三隻登録名 RON-RON（ISB 9590＝#367 宮崎、9593＝本次的春、9598＝#231 長崎）。
  漢字「龍龍」目前**只有 9593 有維護者一手佐證**，`ron-ron-1995-06-15`（#367）與 `ron-ron-1995-06-30`（#231）
  頁面上的漢字歸屬待維護者裁定（原記於 miyazaki-two-ronron 待裁定案）
- **`meron-1999-07-11` 的移園日對不上**：wiki 記 2008-07-17 移いしかわ動物園，ISB 9994 記 `ISHIKAWA 15 Jul 2009`
  （差一年又兩日）。wiki 該日期出自 RPF、本次未動，待園方資料釐清
