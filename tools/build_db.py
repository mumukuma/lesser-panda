#!/usr/bin/env python3
"""
build_db.py — Red Panda Wiki → SQLite

從 wiki/*.md 解析 YAML frontmatter + 家族 section，
輸出 redpanda.db（SQLite）。

使用方式：
    cd red-panda-wiki/
    python tools/build_db.py

每次新增 wiki 條目後重跑即可更新 DB。
"""

from __future__ import annotations  # 相容舊版 Python（str | None 等延後解析）

import os
import re
import json
import sqlite3
import sys
from pathlib import Path

# ── 路徑設定 ──────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).parent
WIKI_DIR    = SCRIPT_DIR.parent / "wiki"
SCHEMA_FILE = SCRIPT_DIR / "schema.sql"
# 優先嘗試放在 tools/ 旁；若掛載資料夾不支援 SQLite（如 Cowork sandbox），
# 自動 fallback 到 /tmp/redpanda.db
DB_PATH     = SCRIPT_DIR.parent / "redpanda.db"
DB_FALLBACK = Path("/tmp/redpanda.db")

# ── YAML frontmatter parser：共用實作在 tools/wiki_io.py ────────
# （re-export 供 check_twins.py 等既有 `from build_db import parse_frontmatter` 使用）
sys.path.insert(0, str(SCRIPT_DIR))
from wiki_io import parse_frontmatter  # noqa: E402


# ── 官方來源分類器（個體頁只顯示官方連結）──────────────────────
# 政策（作者裁定 2026-07-07，最嚴）：個體頁的「來源」區塊只顯示園方官網／政府
# （自治體）公告／園報／中國園官方微信公眾號。RPF、redpanda-lineage、個人部落格、
# 新聞媒體、社群貼文、wiki、web.archive 等一律不顯示（仍保留在 frontmatter sources
# 供校訂與稽核，只是不對外呈現）。
#
# 判定＝白名單 host（精確比對，去掉開頭 www.）＋政府網域 pattern。名單外一律非官方。
# 幽靈親代識別碼格式（frontmatter mother_ref / father_ref）：`isb:<番號>` 優先、`rpf:<id>` 備用。
_PARENT_REF_RE = re.compile(r"(?:isb|rpf):[A-Za-z0-9]+")

# 出身地（frontmatter origin_place）白名單。**只到國別／地區**，粒度比照 ISB 的 locality code
# （CHINA／NEPAL／INDIA／SIKKIM＝錫金／GANGTOK＝錫金首府／DARJEELIN＝大吉嶺／BHUTAN／BURMA）。
# 市級來源地（如「成都市贈與」）是輸出地而非出身地，寫內文即可、不進本欄。
# ⚠️ 新增值時要同步：tools/schema.sql 的 CHECK、五份 pipeline/src/i18n/*.json 的 origin_place_* key。
ORIGIN_PLACES = ("cn", "np", "in", "in-sikkim", "in-darjeeling", "bt", "mm")

# 來自（frontmatter origin_from）白名單：市級來源地。用於「官方只寫到市級、指不出是哪一座園」的個體
# （如甲府市統計書〈沿革〉的「友好都市・成都市より寄贈」）。⚠️ 指名得出來源園就記進 zoos: 首站，別重複填。
# 新增值時要同步：tools/schema.sql 的 CHECK、五份 i18n 的 origin_from_<值，連字號換底線> key。
ORIGIN_FROMS = ("cn-chengdu", "cn-xian", "cn-beijing", "cn-chongqing", "cn-shenyang", "cn-harbin", "cn-guangzhou")
ORIGIN_FROM_KINDS = ("gift", "exchange", "transfer")   # 贈與／動物交換／移入

# ⚠️ 日後新增園方官網時，把 host 補進 OFFICIAL_HOSTS 即會自動顯示。
# ⚠️ 另有「是官方、但不對外呈現連結」的第三類：NON_PUBLIC_HOSTS（ISB）＋一切 Wayback 快照
#    （2026-08-20 起，見 is_public_source）——兩者皆只在 dev mode 的來源區塊顯示。
OFFICIAL_HOSTS = {
    # 日本園方官網／營運協會
    "tokyo-zoo.net", "nhdzoo.jp", "tohoku-safaripark.co.jp", "tobezoo.com",
    # 公益財団法人静岡市動物園協会（日本平動物園的營運協會；機關誌《ズーしずおか》PDF 掛在此域）。
    # ⚠️ 該批 PDF 為掃描件、無文字層，沙盒 proxy 亦回 403；線上核對要用維護者的 Chrome
    #    在同源頁跑 pdf.js 渲染成 canvas 再讀（見 sources/isb-red-panda 以外的作業備忘）。
    "szga.jp",
    "asazoo.jp", "omutacityzoo.org", "hama-midorinokyokai.or.jp",
    # 名古屋市東山動植物園（/news/ 公告與 /blog/ 官方部落格皆為官方一手）
    "higashiyama.city.nagoya.jp",
    "kobe-ojizoo.jp", "ojizoo.jp",  # 神戸市立王子動物園（現行官網＋舊官方網域）
    "tennojizoo.jp",  # 天王寺動物園（含園報《なきごえ》/nakigoe/ 與 ZOO DIARY，官方一手）
    # 到津の森公園（北九州市；含公園だより「動物たちのおはなし」staff blog 與開園周年特設頁）
    "itozu-zoo.jp",
    # 長野市茶臼山動物園。⚠️ 官網已改版為扁平靜態站，舊 CMS 的年度存檔
    # /zukan/zukan/YYYY（2003–2022「動物情報バックナンバー」）整批下架、現為 404。
    # 既有 sources 仍保留該原始位址作為 canonical 出處，原文摘錄存於
    # sources/chausuyama-zukan/；要驗證請走 Wayback（見下方 _WAYBACK_HOSTS）。
    "chausuyama.com",
    "hirakawazoo.jp",  # 鹿児島市平川動物公園（含園方「飼育員の日記」等 staff blog）
    # 長崎バイオパーク（長崎県西海市／株式会社長崎バイオパーク）。公式ブログ
    # “Como esta! BIO PARK” /staff/YYYY/MM/post_N.html 為官方一手（訃報等發於此）。
    "biopark.co.jp",
    # アドベンチャーワールド（和歌山県白浜町／株式会社アワーズ）。園方公告發於
    # /topics/detail?id=… ，新聞稿 PDF 在 /pressrelease/pdf/YYMMDD.pdf。
    # ⚠️ PDF 為全形數字排版，沙盒的文字擷取會把「２８」讀成「１８」之類，日期一律以
    #    HTML topics 頁核對（維護者 Chrome 實讀），勿只信 PDF 抽取結果。
    "aws-s.com",
    "hamurazoo.jp",  # 羽村市動物公園（園方 /news/ 公告）
    # 高知県立のいち動物公園（公益財団法人高知県のいち動物公園協会）。「動物ニュース」
    # /information/zoo-news/entry-N.html 與「飼育日誌」/blog/breeding-diary/ 為官方一手，
    # 個體訃報發於前者（如 2023-02-03 レッサーパンダ「カイ」）。
    "noichizoo.or.jp",
    # 江戸川区自然動物園（公益財団法人えどがわ環境財団が運営）。/zoo/blog_detail/N/ 的
    # 飼育員ブログ（訃報含在內）與 /zoo/introduction/ 動物紹介皆為官方一手。
    "edogawa-kankyozaidan.jp",
    # 福知山市動物園（京都府福知山市立；個體訃報等公告發於 /lesserpanda-<name>/ 等單頁）
    "fukuchiyamazoo.jp",
    # 池田動物園（岡山市；訃報等公告發於 /news/）。⚠️ 舊訃報會自站上下架（如 2024-04-27
    #    「レッサーパンダの「陸」が亡くなりました」2025 年初已 404），既有 sources 走 Wayback 快照。
    "ikedazoo.jp",
    "ishikawazoo.jp",  # いしかわ動物園（含《開園10周年記念誌》等園方 PDF）
    # 鹿児島市広報課「鹿児島市広報デジタルアーカイブ」（廣報紙《かごしま市民のひろば》
    # 等的官方 PDF 封存站；非 .lg.jp 網域故需個別列入）
    "kagoshima-hiroba.jp",
    # 日本自治體（園區隸屬市府）
    "city.ichikawa.lg.jp", "city.asahikawa.hokkaido.jp", "city.kawasaki.jp",
    # 甲府市（遊亀公園附属動物園為市營）。園方公告在 /zoo/news/；另有兩份市府刊物載小熊貓沿革：
    #   ・甲府市統計書〈沿革〉 /somu-somu/shise/toke/documents/r6toukeisyo.pdf
    #   ・広報こうふ 2024-09-28 号「成都×甲府 友好都市締結40周年」 /shise/koho/kohoshi/r6/documents/20240928.pdf
    # ⚠️ 兩份 PDF 皆為直排，文字層抽取會把同一行的區段順序前後顛倒（如「（トト、ヨーヨー）」
    #    被抽成「）ヨーヨー、トト（」），引用列名順序前務必回頭核對版面。
    "city.kofu.yamanashi.jp",
    "soumu.metro.tokyo.lg.jp", "city.sapporo.jp",  # 札幌市円山動物園
    "city.sabae.fukui.jp",  # 鯖江市西山動物園（園頁掛在市府站 /nishiyama_zoo/）
    # 台灣／港澳
    "zoo.gov.taipei", "gov.taipei", "zoo.kcg.gov.tw",  # 高雄市壽山動物園（高雄市府網域）
    "macaotourism.gov.mo", "gcs.gov.mo",
    # 中國園方官網／官方微信公眾號（無官網者以微信文章為官方，見 CLAUDE.md）
    "shanghaizoo.cn", "nbzoo.com", "shwzoo.com", "enjoyland.cn",
    "swap-shendi.com", "lyhylj.liuzhou.gov.cn", "mp.weixin.qq.com",
    "wuhanzoo.com.cn",
    "xianzoo.com",  # 西安秦嶺野生動物園（西安旅遊集團營運；2004-05-01 開園，承接原西安動物園整體遷入的動物）
    # 小紅書：園方官方帳號亦於此發布（如柳州動物園）。與微信同為共用平台、整域列入，
    # ⚠️ sources 只放官方帳號貼文；粉絲轉載請勿放 sources（會被誤判官方）。xhslink 為短連結轉址域。
    "xiaohongshu.com", "xhslink.com",
    # 其他國家園方官網
    "drusillas.co.uk", "witheverland.com", "chiangmai.zoothailand.org", "sriayuthayalionpark.com",
    "hertfordshirezoo.com",  # Hertfordshire Zoo（英國；舊名 Paradise Wildlife Park）
    "woburnsafari.co.uk",  # Woburn Safari Park（英國貝德福德郡；含 /news-and-events/ 園方報導）
    # Naturschutz-Tierpark Görlitz-Zgorzelec（德國薩克森邦；園方新聞 /de/news/detail/NNN-Titel，
    # 舊連結不含 /de/ 亦可用。註冊表 canonical 為 Görlitz Zoo）
    "tierpark-goerlitz.de", "www.tierpark-goerlitz.de",
    "zoobudapest.com",  # Fővárosi Állat- és Növénykert 布達佩斯動物園（匈牙利；Görlitz 出身的 Dhaya 移居於此）
    # Diergaarde Blijdorp／Rotterdam Zoo（荷蘭）：國際小熊貓血統登録書（ISB）的編纂・保管園。
    # ⚠️ 原站 /import/assetmanager/ PDF 目錄 2012 年後整批下架，sources 一律走 Wayback 快照
    # （內層 host 為 rotterdamzoo.nl，`_unwrap_wayback` 會遞迴判為官方）；原檔存 sources/isb-red-panda/。
    # ⚠️ 官方歸官方，但**不對外呈現連結**（維護者裁定 2026-08-11）：同時列於 NON_PUBLIC_HOSTS。
    "rotterdamzoo.nl", "diergaardeblijdorp.nl",
    "zoodubassindarcachon.com",  # Zoo du Bassin d'Arcachon（法國吉倫特省）
    # ZooParc de Beauval（法國盧瓦-謝爾省聖艾尼昂）。園方新聞站 actus.zoobeauval.com 為官方一手
    # （出生・命名・移動公告發於此，逐隻載生日與去向），主站 /zooparc/animals/ 為現有成員名單。
    "zoobeauval.com", "actus.zoobeauval.com",
    # Zoo d'Amiens Métropole（法國索姆省亞眠市營）。/actualites/detail-actualite/… 為園方公告
    "zoo-amiens.fr",
    # Tiergarten Kleve（德國北萊茵-西發利亞邦；抵園・出生公告發於官網單頁 /標題-slug/）
    "tiergarten-kleve.de",
    # ZOOM Erlebniswelt（德國蓋爾森基興；新聞稿在 /presse-YYYY/…）
    "zoom-erlebniswelt.de",
    "zoo.saarbruecken.de", "saarbruecken.de",  # Zoo Saarbrücken（德國薩爾邦；薩爾布呂肯市營，公告發於市府網域）
    # ZOO Ústí nad Labem（捷克烏斯提州；含年度報告 PDF /data/clanky/…/vyrocni-zprava-YYYY.pdf，
    # 園方自行編纂、記載各物種收支與繁殖，視同園報）
    "zoousti.cz", "www.zoousti.cz",
    "zoobojnice.sk",  # Národná zoologická záhrada Bojnice（斯洛伐克國立動物園，環境部所屬）
    # Miejski Ogród Zoologiczny w Warszawie／Warsaw Zoo（波蘭華沙市立）。個體介紹頁
    # /en/visit-the-zoo/more-about-our-animals/… 載有各隻的性別・生日・出生園，視同園方一手。
    "zoo.waw.pl",
    "zoo.si",  # ZOO Ljubljana（斯洛維尼亞；盧布爾雅那市立）
    "pairidaiza.eu",  # Pairi Daiza（比利時）
    "torontozoo.com",  # Toronto Zoo（加拿大；含 /mediaroom/ 新聞稿）
    # 美國
    # Millbrook School（紐約州；校內附設 Trevor-Lovejoy Zoo，舊名 Trevor Zoo）。
    # 小熊貓出生・命名等公告發於 /zoo-news-detail?pk=… 與 /news-detail?pk=…，為園方一手。
    "millbrook.org",
    "sbzoo.org",  # Santa Barbara Zoo（加州；/zoo-animals/species/… 個體介紹頁載生日與來源園）
    "buffalozoo.org",  # Buffalo Zoo（紐約州；抵園・出産公告發於官網 news）
    "pueblozoo.org",  # Pueblo Zoo（科羅拉多州）
    "beardsleyzoo.org",  # Connecticut's Beardsley Zoo（康乃狄克州；/press/ 為園方新聞稿）
    # 史密森尼（National Zoological Park／SCBI 同屬；siarchives 為機構檔案館）
    "nationalzoo.si.edu", "siarchives.si.edu",
    # Assiniboine Park Conservancy（加拿大；Assiniboine Park Zoo 營運方，園方 /stories/ 為官方一手）
    "assiniboinepark.ca",
    "gvzoo.com",  # Greater Vancouver Zoo（加拿大；含 /news/ 新聞稿）
    "calgaryzoo.com",  # Wilder Institute's Calgary Zoo（加拿大；含 /news/ 新聞稿與訃告）
    # Valley Zoo Development Society：Edmonton Valley Zoo 的官方支援團體，園內動物資訊
    # （出生日、父母、飼育員談話）由園方提供、以第一人稱發布，比照 Calgary 的 Wilder Institute 認列官方。
    "buildingourzoo.com",
    "zooknoxville.org",  # Zoo Knoxville（美國田納西州）
    # Potter Park Zoological Gardens（美國密西根州；抵園・出生公告發於官網新聞稿）
    "potterparkzoo.org",
    # Potawatomi Zoo（美國印第安納州；出生公告發於官網與官方 IG @potawatomizoo）
    "potawatomizoo.org",
    # Rosamond Gifford Zoo at Burnet Park（美國紐約州雪城）
    "rosamondgiffordzoo.org", "www.rosamondgiffordzoo.org",
    # Cincinnati Zoo & Botanical Garden（美國俄亥俄州；全球 styani 亞種繁殖數第一，
    # 出生・命名・訃報公告多發於官網文章與官方 X／FB）
    "cincinnatizoo.org",
    "saczoo.org",  # Sacramento Zoo（美國加州；含 /imported-blog/ 舊園方部落格，出生・命名紀錄）
    # Birmingham Zoo（美國阿拉巴馬州；出生公告發於官網 /YYYY/MM/DD/ 文章與官方 FB）
    "birminghamzoo.com",
    "sfzoo.org",  # San Francisco Zoo & Gardens（美國加州）
    # Columbus Zoo and Aquarium（美國俄亥俄州；出生・命名公告發於官網 /news/ 與官方 FB／IG）
    "columbuszoo.org",
    # Zoo sauvage de Saint-Félicien（加拿大魁北克；到園・個體介紹公告發於官方 IG @zoosauvageofficiel）
    "zoosauvage.org",
    "mandai.com",  # Mandai Wildlife Group（新加坡；Singapore Zoo／River Wonders 營運方）
    "grandpark.seoul.go.kr",  # 서울대공원 首爾大公園（韓國；首爾市所屬，同 IG @seoulgrandpark）
    # ⚠️ host 是「完全比對」，子網域要各自列一筆（corporate. 是新聞稿所在）
    "oceanpark.com.hk", "corporate.oceanpark.com.hk",  # 香港海洋公園
}

# Facebook 是共用網域，不能整域列白名單（旅遊/粉絲轉載粉專也在同域）。
# 僅認「園方/機構官方專頁」——比對 URL 路徑第一段（vanity 或數字 page id）。
# 新增官方園方 FB 專頁時，把其 vanity（小寫）補進這裡即會自動顯示。
OFFICIAL_FB_PAGES = {
    "thecalgaryzoo",   # The Calgary Zoo 官方專頁（page id 100064839398464）
    "zounokuni",       # ぞうの国 官方專頁
    "oceanparkhk",     # 香港海洋公園 Ocean Park Hong Kong 官方專頁
    "cincinnatizoo",   # Cincinnati Zoo & Botanical Garden 官方專頁（同 cincinnatizoo.org）
    "columbuszoo",     # Columbus Zoo and Aquarium 官方專頁（官網頁尾 Facebook 連結指向此專頁）
    "pueblozoo",       # Pueblo Zoo 官方專頁（同 pueblozoo.org；出生・命名公告發於此）
    "saitamazoo",      # 埼玉県こども動物自然公園 官方專頁（parks.or.jp/sczoo 頁尾 SNS 連結指向此）
    "zoobojnice",      # ZOO BOJNICE 官方專頁（page id 100064523241079；出生日等細節只發於此，官網 /tag/panda-cervena/ 未收）
    "birminghamzoo",   # The Birmingham Zoo 官方專頁（官網頁尾 Facebook 連結指向此專頁；Gizmo 抵園日只發於此）
    "zooamiens",       # Zoo d'Amiens Métropole 官方專頁（同 zoo-amiens.fr；Wilmer 的生日與出生園只發於此）
}
_FB_HOSTS = {"facebook.com", "m.facebook.com", "web.facebook.com", "fb.com"}

# X（舊 Twitter）同為共用網域，比照 Facebook 只認「園方官方帳號」——比對 URL 路徑
# 第一段的 handle（小寫、不含 @）。多數日本園以 X 為主要公告管道（出生・命名・雌雄
# 鑑定・訃報常只發在這裡），故列為官方來源。
# ⚠️ 只放園方自己的帳號；粉絲／個人拍攝帳號請勿加入（會被誤判官方）。
OFFICIAL_X_ACCOUNTS = {
    "nishiyama_zoo",    # 鯖江市西山動物園
    "nhdzoo",           # 静岡市立日本平動物園（同 nhdzoo.jp）
    "ichikawa_zoo",     # 市川市動植物園（同 city.ichikawa.lg.jp）
    "kumamotocityzoo",  # 熊本市動植物園（ezooko.jp）
    "cincinnatizoo",    # Cincinnati Zoo & Botanical Garden（同 cincinnatizoo.org）
    "ooshimashicho",    # 東京都大島支庁（大島公園動物園）
    "love_ikedazoo",    # 池田動物園（官網頁尾 X 連結指向此帳號；訃報公告發於此）
}
_X_HOSTS = {"x.com", "twitter.com", "mobile.twitter.com", "mobile.x.com"}


def _strip_yaml_comment(value):
    """去掉 `extra_sources` 連結行末的 YAML 註解（`  # 標題（日期）`）。

    ⚠️ 只對「以 http(s):// 開頭」的值動手，且以第一個空白為界切斷——URL 本身不含空白，
    這樣既能清掉註解，又不會誤傷純文字說明（如「…lineage 記為無名 #732）」這種內容裡
    本來就有 ` #` 的一手佐證描述）。也不會誤切 URL 內的 fragment（`…/#profile/397` 前無空白）。
    """
    if not isinstance(value, str):
        return value
    s = value.strip()
    if s.lower().startswith(("http://", "https://")):
        return s.split(None, 1)[0]
    return s

# Instagram 同為共用網域，比照 X／FB 只認「園方官方帳號」——比對 URL 路徑第一段的
# 帳號（小寫、不含 @）。⚠️ 僅認含帳號的完整形式 /帳號/p/XXXX/；IG「複製連結」給的
# 短形式 /p/XXXX/ 無從判斷發文者，一律視為非官方（sources 請存完整形式）。
# ⚠️ 只放園方自己的帳號；同好／個人拍攝帳號請勿加入（會被誤判官方）。
OFFICIAL_IG_ACCOUNTS = {
    "cincinnatizoo",   # Cincinnati Zoo & Botanical Garden 官方 IG（同 cincinnatizoo.org）
    "kumamoto_doushokubutsuen",  # 熊本市動植物園（ezooko.jp）
    "kiryuzoo",  # 桐生が岡動物園（官網 city.kiryu.lg.jp/zoo 首頁 IG banner 連此帳號）
    "hertfordshirezoo",  # Hertfordshire Zoo（官網 News & Socials 與頁尾 IG 連結皆指向此帳號）
    "hamurazoo.official",  # 羽村市動物公園（同 hamurazoo.jp；雌雄鑑定等公告發於此）
    "maruyamazoo_official",  # 札幌市円山動物園（同 city.sapporo.jp；出産公告發於此）
    "seoulgrandpark",  # 서울대공원 首爾大公園（韓國；官方帳號）
    "calgaryzoo", "thecalgaryzoo",  # Wilder Institute's Calgary Zoo（兩個帳號皆官方；FB 白名單已收 thecalgaryzoo）
    "edmontonvalleyzoo",  # Edmonton Valley Zoo（加拿大亞伯達省；市府所屬）
    "safariniagara",  # Safari Niagara（加拿大安大略省）
    "sanfranciscozoo",  # San Francisco Zoo & Gardens（同 sfzoo.org；訃報等公告發於此）
    "sacramentozoo",  # Sacramento Zoo（同 saczoo.org；訃報等公告發於此）
    "assiniboineparkzoo",  # Assiniboine Park Zoo（官網 assiniboinepark.ca/zoo 頁尾 Instagram 連結指向此帳號；出産公告發於此）
    "prospectparkzoo",  # Prospect Park Zoo（WCS；官網 prospectparkzoo.com 頁尾 Instagram 連結指向此帳號）
    "columbuszoo",  # Columbus Zoo and Aquarium（官網 columbuszoo.org 頁尾 Instagram 連結指向此帳號）
    "zoosauvageofficiel",  # Zoo sauvage de Saint-Félicien（加拿大魁北克；貼文內文連回 zoosauvage.org，到園公告發於此）
    "zooknoxville",  # Zoo Knoxville（同 zooknoxville.org；抵園・出産公告發於此）
    "potawatomizoo",  # Potawatomi Zoo（同 potawatomizoo.org；生日・送別公告發於此）
    "woburn_safari",  # Woburn Safari Park（英國；官網 woburnsafari.co.uk 頁尾 Instagram 連結指向此帳號；到園公告發於此）
    "tiergartenkleve",  # Tiergarten Kleve（德國；同 tiergarten-kleve.de，幼獸近況只發於此）
    "pueblozoo",  # Pueblo Zoo（同 pueblozoo.org；幼獸健檢等公告發於此）
    "buffalo_zoo",  # Buffalo Zoo（同 buffalozoo.org；抵園公告發於此）
    "love_ikedazoo",  # 池田動物園（官網頁尾 Instagram 連結指向此帳號）
    "zoogoerlitz",  # Naturschutz-Tierpark Görlitz-Zgorzelec（官網 tierpark-goerlitz.de 頁尾 Instagram 連結指向此帳號；出生・健檢公告發於此）
    "zoopoznan",  # Ogród Zoologiczny w Poznaniu（官網 zoo.poznan.pl 的 Instagram 連結指向此帳號；出生・脫逃・搬園公告發於此）
    "zoo_warszawa",  # Miejski Ogród Zoologiczny w Warszawie（同 zoo.waw.pl；IG bio 自稱「Oficjalny profil Warszawskiego ZOO」並連回官網）
    "capemaycountyzoo",  # Cape May County Park & Zoo（美國紐澤西州郡立；郡府官網 /1008/Park-Zoo 的 Instagram 連結指向此帳號；到園公告發於此）
    "zoobeauval",  # ZooParc de Beauval（法國；同 zoobeauval.com／actus.zoobeauval.com，出生公告同步發於此）
    "trevorzoomillbrook",  # Trevor-Lovejoy Zoo at Millbrook School（美國紐約州；millbrook.org 的 Trevor Zoo 首頁 Instagram 連結指向此帳號）
}
_IG_HOSTS = {"instagram.com", "m.instagram.com"}
_IG_NON_ACCOUNT_SEGS = {"p", "reel", "reels", "tv", "stories", "explore"}

# 「官方內容之忠實轉載」與「共用平台上的園方發布」——整域不可列白名單（同域大多是
# 個人遊記／新聞稿代發），故逐條 URL 認列。依 CLAUDE.md〈官方來源可直接採用〉：
# 園方名單／家系圖／新聞稿之忠實轉載視同官方資料。新增前請先確認轉載內容確為園方一手。
OFFICIAL_URLS = {
    # 多摩動物公園官方個體名單（含全家系生卒與轉園），由 4travel 旅行記整段轉載
    "https://4travel.jp/travelogue/11691476",
    # 横浜八景島 官方新聞稿（2019-07-03），發布於 PR TIMES
    "https://prtimes.jp/main/html/rd/p/000000321.000011571.html",
    # 東北サファリパーク 園內製作家系圖之照片（作者確認為官方資訊忠實轉載）
    "https://mamepandaworld.blog.fc2.com/blog-entry-1311.html",
    # 仙台市八木山動物公園 学芸員 阿部敏計〈仙台市八木山動物公園の愛すべき長寿動物について〉
    # （2010-02-03）。載於「仙台・宮城ミュージアムアライアンス（SMMA）」，園方學藝員署名執筆、
    # 視同園方一手（維護者裁定 2026-08-15）。⚠️ 只認這一篇 URL，不整域列 smma.jp——該站另收
    # 多家館所的隨筆，整域列入會把非園方內容一併誤判為官方。
    "https://www.smma.jp/essay/%E4%BB%99%E5%8F%B0%E5%B8%82%E5%85%AB%E6%9C%A8%E5%B1%B1%E5%8B%95%E7%89%A9%E5%85%AC%E5%9C%92%E3%81%AE%E6%84%9B%E3%81%99%E3%81%B9%E3%81%8D%E9%95%B7%E5%AF%BF%E5%8B%95%E7%89%A9%E3%81%AB%E3%81%A4%E3%81%84-2/",

    # 姫路市立動物園 公式ブログ「姫Ｚｏｏぶろぐ」的舊址（exblog 版，投稿者 `dobutuen`，
    # 副標「姫路市立動物園での『あんなこと』『こんなこと』を紹介します」）。該部落格後來搬到市府網域
    # https://www.city.himeji.lg.jp/hcityzoo/（同名同路徑名 hcityzoo，站上仍留「ブログのお引越しのお知らせ。」一文），
    # 故 exblog 版視同園方一手（2026-08-16 認列，待維護者複核）。⚠️ 只認個別 URL，不整域列 exblog.jp——
    # 該平台同好部落格極多（如 mihorinh.exblog.jp「レサパン日和」），整域列入會把粉絲文誤判官方。
    "https://hcityzoo.exblog.jp/14894060/",
    # 同上（姫Ｚｏｏぶろぐ exblog 版）：2009-06-30〈梅雨本番〉——レッサーパンダ フウフウ 的誕生日
    # （6/29）與「１８才のおじいちゃん」，園方一手佐證 fuu-fuu-1991-06-29 的生日與在籍姫路市立動物園。
    "https://hcityzoo.exblog.jp/8528084/",
}

_WAYBACK_HOSTS = {"web.archive.org", "archive.org"}
_WAYBACK_RE = re.compile(r"/web/[^/]+/(?P<inner>https?://.+)$", re.I)

def _unwrap_wayback(url: str) -> str:
    """從 Wayback 快照 URL 取出被封存的原始 URL；取不到回空字串。

    形如 https://web.archive.org/web/20180101000000/http://example.com/a
    或省略 timestamp 的 https://web.archive.org/web/2018/http://example.com/a。
    """
    m = _WAYBACK_RE.search(url)
    return m.group("inner") if m else ""

def _host(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).netloc.lower().split("@")[-1].split(":")[0].removeprefix("www.") \
        if "//" in url else ""

def is_official_source(url: str) -> bool:
    """僅園方官網／政府公告／園報／官方微信視為官方。名單外＋非 gov pattern＝False。"""
    if not isinstance(url, str) or not url.startswith("http"):
        return False
    if url.split("#")[0].rstrip("/") in {u.rstrip("/") for u in OFFICIAL_URLS}:
        return True
    host = _host(url)
    if not host:
        return False
    if host in OFFICIAL_HOSTS:
        return True
    # Wayback Machine：不整域列白名單（archive.org 上什麼站都有，整域列入會把粉絲站、
    # 部落格的快照也誤判官方）。改為「拆出被封存的原始 URL，遞迴判斷內層 host」——
    # 只有原本就是官方來源的快照才算官方。用於引用已下架的園方頁面（如茶臼山舊年度存檔）。
    if host in _WAYBACK_HOSTS:
        inner = _unwrap_wayback(url)
        return is_official_source(inner) if inner else False
    # Facebook：僅特定園方/機構官方專頁（比對路徑第一段 vanity / page id）
    if host in _FB_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower()
        return seg in OFFICIAL_FB_PAGES
    # X（Twitter）：僅特定園方官方帳號（比對路徑第一段 handle）
    if host in _X_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower().lstrip("@")
        return seg in OFFICIAL_X_ACCOUNTS
    # Instagram：僅特定園方官方帳號（比對路徑第一段帳號；短形式 /p/… 不算官方）
    if host in _IG_HOSTS:
        from urllib.parse import urlparse
        seg = urlparse(url).path.strip("/").split("/")[0].lower().lstrip("@")
        if seg in _IG_NON_ACCOUNT_SEGS:
            return False
        return seg in OFFICIAL_IG_ACCOUNTS
    # 政府網域 pattern（未來新自治體/政府站自動涵蓋）
    # ⚠️ 這條也涵蓋 J-STAGE（jstage.jst.go.jp）。園方自行編輯登載的《安佐動物公園飼育記録集》
    # （https://www.jstage.jst.go.jp/article/asazoo/…，Online ISSN 2759-6567）即靠這條被認列為
    # 官方園報，符合 CLAUDE.md「園報視為官方」。副作用：J-STAGE 上**其他**期刊（非園方編輯的
    # 學術論文）也會被判為官方；日後若要收緊，改成只認 /article/asazoo/ 等園方刊物路徑。
    if host.endswith((".lg.jp", ".go.jp", ".gov", ".gov.tw", ".gov.cn",
                      ".gov.mo", ".gov.taipei")):
        return True
    if ".gov." in host:
        return True
    return False

def official_sources(sources_raw) -> list[str]:
    if not sources_raw:
        return []
    if isinstance(sources_raw, str):
        sources_raw = [sources_raw]
    seen, out = set(), []
    for u in sources_raw:
        u = (u or "").strip()
        if u and is_official_source(u) and u not in seen:
            seen.add(u); out.append(u)
    return out


# ── 官方但不對外呈現的來源 ───────────────────────────────────
# 維護者裁定 2026-08-11：ISB（國際小熊貓血統登録書，Rotterdam Zoo／Diergaarde Blijdorp 編）
# **仍是官方一手來源、佐證權重照舊**（`has_official_source` 不受影響、🚧 判定照舊），
# 但**不在網站個體頁列出連結**——原檔 2012 年已由園方下架，公開可指的只剩 Wayback 快照，
# 不宜對外呈現。連結原封不動留在 frontmatter `sources:` 供校訂稽核，原檔存 sources/isb-red-panda/。
# ⚠️ 這裡放的是「官方但不公開展示」，與「非官方」是兩回事，勿從 OFFICIAL_HOSTS 移除。
NON_PUBLIC_HOSTS = {"rotterdamzoo.nl", "diergaardeblijdorp.nl"}

def is_public_source(url: str) -> bool:
    """官方來源是否可在個體頁公開列出。

    維護者裁定 2026-08-20：凡 Wayback 快照（web.archive.org 等）一律不公開列出，
    改為只在 dev mode 顯示（見 Panda.astro 的 dev-only 來源區塊；資料經
    export_json 的 sources_private 送達，pandas.json 僅建置期讀取、不進 dist）。
    在此之前 Wayback 會拆內層 host、園方舊頁快照照樣公開；現在外層 host 是
    Wayback 就直接判非公開。官方認定（is_official_source）仍拆內層判斷，
    佐證權重與 has_official_source 不受影響。"""
    host = _host(url)
    if host in _WAYBACK_HOSTS:
        return False
    return host not in NON_PUBLIC_HOSTS


def split_sources(sources_raw) -> tuple[list[str], list[str]]:
    """回傳 (公開展示的官方來源, 官方但不公開展示的來源)；兩者皆計入官方佐證。"""
    off = official_sources(sources_raw)
    return [u for u in off if is_public_source(u)], [u for u in off if not is_public_source(u)]


# ── Wikilink 抽取 ─────────────────────────────────────────────
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")

def extract_wikilinks(text: str) -> list[str]:
    """取出所有 [[slug]] 中的 slug，並正規化為 kebab-lowercase。"""
    return [m.group(1).strip().lower() for m in WIKILINK_RE.finditer(text)]

def first_wikilink(text: str) -> str | None:
    m = WIKILINK_RE.search(text)
    return m.group(1).strip().lower() if m else None

# 消歧警語標記：父/母 行常見「（⚠️ 勿與 [[另一隻]] 混淆）」。這些警語裡的
# wikilink 不是父母本身，必須在抽取父母前切掉，否則 first_wikilink 會誤抓警語連結。
WARNING_RE = re.compile(r"⚠|勿與|請勿與|不要與|混淆|注意同名|不同個體")

def parent_link(text: str) -> str | None:
    """從 父/母 行取真正的父母 slug：先切掉消歧警語子句再取第一個 wikilink。
    若真正父母以純文字書寫（無條目），切掉警語後即無連結 → 回 None（不建錯邊）。"""
    head = WARNING_RE.split(text, maxsplit=1)[0]
    return first_wikilink(head)


# ── 家族 section 解析 ─────────────────────────────────────────
def parse_family(body: str) -> dict:
    """
    回傳:
        mother: str | None
        father: str | None
        twins:  list[str]
        children: list[str]   ← 從子女 table 抽取
    """
    result = {"mother": None, "father": None, "twins": [], "children": []}

    # 找 ## 家族 或 ## 家族關係 section
    section_re = re.compile(r"^##\s+家族", re.MULTILINE)
    m = section_re.search(body)
    if not m:
        return result
    section_text = body[m.start():]

    # section 結束於下一個 ## （非 ###）
    next_section = re.search(r"\n##\s+(?!#)", section_text[3:])
    if next_section:
        section_text = section_text[: next_section.start() + 3]

    # --- 解析每一行 ---
    in_children_table = False
    for line in section_text.splitlines():
        stripped = line.strip()

        # 進入子女表格
        if re.match(r"^#{2,3}\s+子女", stripped):
            in_children_table = True
            continue

        # 離開子女表格（碰到另一個 header 或非表格行後不再是 table）
        if stripped.startswith("#") and not re.match(r"^#{2,3}\s+子女", stripped):
            in_children_table = False

        # 子女 table row（以 | [[ 開頭的行）
        if in_children_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            if cells:
                child = first_wikilink(cells[0])
                if child:
                    result["children"].append(child)
            continue

        # 母
        if re.match(r"^-\s*母[：:]", stripped):
            result["mother"] = parent_link(stripped)
            continue

        # 父
        if re.match(r"^-\s*父[：:]", stripped):
            result["father"] = parent_link(stripped)
            continue

        # 多胞胎（雙胞胎／三胞胎／四胞胎…，可能有多人，取所有 wikilinks）
        # 也匹配「雙胞胎姊妹：」「三胞胎兄弟：」「三胞胎妹妹：」等變體
        # 同一資料模型存為兩兩配對；網站再依同生群人數決定顯示「雙胞胎／三胞胎…」
        # 數字開頭者（如「2013 雙胞胎：」）屬「子女」區描述其子女的同生群，不算本人的，故排除
        if re.match(r"^-\s*[二兩雙三四五六]胞胎[^：:]{0,4}[：:]", stripped):
            # 先去除消歧義／警語註記裡的 wikilink（如「⚠️ 非 [[X]] 亦非 [[Y]]」），
            # 那是在說明「不是這幾隻」，不可當成同生群成員
            cleaned = re.sub(r"[（(][^（）()]*[非⚠][^（）()]*[）)]", "", stripped)
            cleaned = re.sub(r"(?:亦)?非\s*\[\[[^\]]+\]\]", "", cleaned)
            result["twins"].extend(extract_wikilinks(cleaned))

    return result


# ── 居住史解析（從 YAML zoos 欄位，唯一事實來源）──────────────
# 格式：「<園名> (<起> – <訖>)」；起訖可為 YYYY-MM-DD / YYYY / 現在(訖留空)
ZOO_RANGE_RE = re.compile(
    r"^(.+?)\s*[（(]\s*"
    r"((?:\d{4}-\d{2}-\d{2})|(?:\d{4}))?\s*[–—~〜-]\s*"
    r"((?:\d{4}-\d{2}-\d{2})|(?:\d{4})|現在|今)?\s*[）)]\s*$")

def _ymd(s):
    if not s:
        return (None, None)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return (s, int(s[:4]))
    if re.fullmatch(r"\d{4}", s):
        return (None, int(s))
    return (None, None)

def parse_zoos(zoos_raw) -> list[dict]:
    """YAML zoos 欄位（字串列表）→ [{zoo_name, start_year, end_year, start_date, end_date}, ...]"""
    if not zoos_raw:
        return []
    if isinstance(zoos_raw, str):
        zoos_raw = [zoos_raw]
    results = []
    for entry in zoos_raw:
        entry = entry.strip()
        m = ZOO_RANGE_RE.match(entry)
        if m:
            zoo_name = m.group(1).strip()
            sd, sy = _ymd(m.group(2))
            end_raw = m.group(3)
            ed, ey = (None, None) if (not end_raw or end_raw in ("現在", "今")) else _ymd(end_raw)
            results.append({"zoo_name": zoo_name, "start_year": sy, "end_year": ey,
                            "start_date": sd, "end_date": ed})
        else:
            # 無括號日期，至少記下動物園名
            results.append({"zoo_name": entry, "start_year": None, "end_year": None,
                            "start_date": None, "end_date": None})
    return results


# ── 主流程 ────────────────────────────────────────────────────
def species_short(species_str: str | None) -> str | None:
    if not species_str:
        return None
    if "styani" in species_str:
        return "styani"
    if "fulgens" in species_str:
        return "fulgens"
    return species_str


def build_db():
    md_files = sorted(WIKI_DIR.glob("*.md"))
    skip = {"index.md", "log.md"}
    md_files = [f for f in md_files if f.name not in skip]

    print(f"找到 {len(md_files)} 個 wiki 條目")

    # ── 初始化 DB ──────────────────────────────────────────────
    # 嘗試主路徑，失敗時 fallback 到 /tmp
    actual_db = DB_PATH
    try:
        if actual_db.exists():
            actual_db.unlink()
        conn = sqlite3.connect(actual_db)
        conn.execute("CREATE TABLE _test (x)")
        conn.execute("DROP TABLE _test")
    except Exception:
        actual_db = DB_FALLBACK
        if actual_db.exists():
            actual_db.unlink()
        conn = sqlite3.connect(actual_db)
        print(f"  ℹ️  掛載資料夾不支援 SQLite，改用: {actual_db}")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    with open(SCHEMA_FILE, encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()

    # ── Pass 1：插入 pandas 基本資料 ──────────────────────────
    all_slugs: set[str] = set()
    panda_rows: list[dict] = []
    declared_sib_raw: dict[str, list[str]] = {}  # slug -> frontmatter siblings 列出的 slug

    for md_path in md_files:
        slug = md_path.stem.lower()
        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        if not fm.get("name"):
            print(f"  ⚠️  跳過（無 name）: {md_path.name}")
            continue

        sex_raw = fm.get("sex", "")
        if sex_raw in ("female", "male"):
            sex = sex_raw
        else:
            sex = "unknown"

        tags_raw = fm.get("tags", [])
        if isinstance(tags_raw, str):
            tags_raw = [tags_raw]

        nicknames = fm.get("nicknames", [])
        if isinstance(nicknames, str):
            nicknames = [nicknames]

        english_variants = fm.get("english_variants", [])
        if isinstance(english_variants, str):
            english_variants = [english_variants]

        instagram = fm.get("instagram", [])
        if isinstance(instagram, str):
            instagram = [instagram]

        # YouTube 展示用影片（照片與影片區的影片分頁）；佐證用的 YT 連結仍走 extra_sources。
        # 行末 YAML 註解（`  # 標題／頻道`）自製 parser 不會剝掉，這裡去掉、保留「URL 日期」。
        youtube = fm.get("youtube", [])
        if isinstance(youtube, str):
            youtube = [youtube]
        youtube = [re.sub(r"\s+#.*$", "", str(s)).strip() for s in youtube]
        youtube = [s for s in youtube if s]

        extra_sources = fm.get("extra_sources", [])
        if isinstance(extra_sources, str):
            extra_sources = [extra_sources]
        extra_sources = [_strip_yaml_comment(s) for s in extra_sources]

        # 官方來源拆兩份：公開展示的進 sources、官方但不公開展示的（ISB）進 sources_private。
        # 兩者任一非空即代表有官方佐證（export_json 的 has_official_source 取兩者聯集）。
        src_public, src_private = split_sources(fm.get("sources"))

        # 韓文名可為單值或多值（list）；正規化為以逗號分隔的字串（比照 japanese 多值寫法）
        korean = fm.get("korean")
        if isinstance(korean, list):
            korean = ", ".join(str(x) for x in korean) if korean else None

        # 出身（選填）：wild=野生出身（含野捕／救護）｜confiscated=走私查獲。園內出生者留空。
        # 白名單外的值一律視同留空——schema.sql 對此欄有 CHECK 約束，直接寫入會讓整次建置中止。
        origin = (fm.get("origin") or "").strip().lower() or None
        if origin not in ("wild", "confiscated"):
            if origin:
                print(f"  ⚠️  {slug}: origin 值 `{origin}` 不在白名單（wild／confiscated），已忽略")
            origin = None

        # 出身地（選填，2026-08-17 起）：受控詞彙、只到國別／地區（粒度比照 ISB locality code）。
        # 市級來源地（如「1985 年成都市贈與」）是輸出地而非出身地，寫內文、不進本欄。
        # 沒有 origin 就沒有「出身」列可掛，單獨填 origin_place 一律忽略（避免資料看得見卻永不顯示）。
        origin_place = (str(fm.get("origin_place") or "").strip().lower() or None)
        if origin_place and origin_place not in ORIGIN_PLACES:
            print(f"  ⚠️  {slug}: origin_place 值 `{origin_place}` 不在白名單（{'／'.join(ORIGIN_PLACES)}），已忽略")
            origin_place = None
        if origin_place and not origin:
            print(f"  ⚠️  {slug}: 有 origin_place 但無 origin，已忽略（出身列不會出現）")
            origin_place = None

        # 來自（選填三欄一組，2026-08-17 起）：市級來源地＋年＋方式。獨立於 origin——
        # 園內出生但由某市贈與的個體也適用。年與方式都依附 origin_from，沒有地點就一併忽略。
        origin_from = (str(fm.get("origin_from") or "").strip().lower() or None)
        if origin_from and origin_from not in ORIGIN_FROMS:
            print(f"  ⚠️  {slug}: origin_from 值 `{origin_from}` 不在白名單，已忽略")
            origin_from = None
        origin_from_kind = (str(fm.get("origin_from_kind") or "").strip().lower() or None)
        if origin_from_kind and origin_from_kind not in ORIGIN_FROM_KINDS:
            print(f"  ⚠️  {slug}: origin_from_kind 值 `{origin_from_kind}` 不在白名單（gift／exchange／transfer），已忽略")
            origin_from_kind = None
        origin_from_year = fm.get("origin_from_year")
        try:
            origin_from_year = int(str(origin_from_year).strip()) if origin_from_year not in (None, "") else None
        except ValueError:
            print(f"  ⚠️  {slug}: origin_from_year 值 `{origin_from_year}` 非年份，已忽略")
            origin_from_year = None
        if not origin_from and (origin_from_year or origin_from_kind):
            print(f"  ⚠️  {slug}: 有 origin_from_year／kind 但無 origin_from，已忽略（來自列不會出現）")
            origin_from_year = origin_from_kind = None

        # 幽靈親代（選填）：親代已確認身分但無條目（終生未命名等）。格式 `isb:<番號>` 或 `rpf:<id>`。
        # 只影響網站的全血／半血判定，不建個體、不進 parent_child、不上家系圖。
        def _parent_ref(key: str) -> str | None:
            v = fm.get(key)
            if v is None:
                return None
            v = str(v).strip()
            if not v:
                return None
            if not _PARENT_REF_RE.fullmatch(v):
                print(f"  ⚠️  {slug}: {key} 值 `{v}` 格式不合（需 isb:<番號> 或 rpf:<id>），已忽略")
                return None
            return v

        mother_ref = _parent_ref("mother_ref")
        father_ref = _parent_ref("father_ref")

        # 出生園旗標（選填）：唯一有意義的值是 `unknown`，意為「居住史首站不是出生園」。
        # gen_residence.py 用它決定內文要不要標 🐣；本欄匯出後，網站的園頁「該園出生」、
        # 時間軸 bornHere 與 /stats/ 出生園排行也共用同一判定（web/src/lib/data.js 的 bornAtFirstZoo）。
        birth_zoo = (str(fm.get("birth_zoo") or "").strip().lower() or None)
        if birth_zoo not in (None, "unknown"):
            print(f"  ⚠️  {slug}: birth_zoo 值 `{birth_zoo}` 非 unknown，已忽略")
            birth_zoo = None

        row = {
            "slug":             slug,
            "name":             fm.get("name", ""),
            "japanese":         fm.get("japanese"),
            "korean":           korean,
            "chinese":          fm.get("chinese"),
            "nicknames":        json.dumps(nicknames, ensure_ascii=False) if nicknames else None,
            "english_variants": json.dumps(english_variants, ensure_ascii=False) if english_variants else None,
            "sex":              sex,
            "born":             fm.get("born"),
            "died":             fm.get("died"),
            "last_seen":        fm.get("last_seen"),
            "species":          species_short(fm.get("species")),
            # 出身（選填）：wild=野生出身（含野捕／救護）｜confiscated=走私查獲。
            # 園內出生者一律留空；未知值視同留空（不寫入，避免 CHECK 約束擋掉整次建置）。
            "origin":           origin,
            "origin_place":     origin_place,
            "origin_from":      origin_from,
            "origin_from_year": origin_from_year,
            "origin_from_kind": origin_from_kind,
            "birth_zoo":        birth_zoo,
            "mother_ref":       mother_ref,
            "father_ref":       father_ref,
            "rpf_id":           int(fm["rpf_id"]) if fm.get("rpf_id") else None,
            "rpf_url":          fm.get("rpf_url"),
            # ISB 番號：frontmatter 一律加引號存字串（前導零），這裡原樣帶過不轉型
            "studbook_id":      str(fm["studbook_id"]).strip() if fm.get("studbook_id") else None,
            # ISB 對帳日：已與 ISB 原檔逐欄對過帳的日期（ISB 查無者也可填，見 SCHEMA.md）
            "isb_checked":      str(fm["isb_checked"]).strip() if fm.get("isb_checked") else None,
            "tags":             json.dumps(tags_raw, ensure_ascii=False),
            "instagram":        json.dumps(instagram, ensure_ascii=False) if instagram else None,
            "youtube":          json.dumps(youtube, ensure_ascii=False) if youtube else None,
            "is_alive":         0 if fm.get("died") else 1,
            "sources":          json.dumps(src_public, ensure_ascii=False),
            "sources_private":  json.dumps(src_private, ensure_ascii=False) if src_private else None,
            "extra_sources":    json.dumps(extra_sources, ensure_ascii=False) if extra_sources else None,
        }
        panda_rows.append((slug, body, row))
        all_slugs.add(slug)

        # 已宣告手足（父母不詳、無法由共同父母推導時使用）；正規化為 kebab-lowercase
        siblings_raw = fm.get("siblings", [])
        if isinstance(siblings_raw, str):
            siblings_raw = [siblings_raw]
        if siblings_raw:
            declared_sib_raw[slug] = [str(s).strip().lower() for s in siblings_raw if str(s).strip()]

    cur.executemany("""
        INSERT OR REPLACE INTO pandas
          (slug, name, japanese, korean, chinese, nicknames, english_variants,
           sex, born, died, last_seen, species, origin, origin_place, origin_from, origin_from_year, origin_from_kind, birth_zoo, mother_ref, father_ref, rpf_id, rpf_url, studbook_id, isb_checked, tags, instagram, youtube, is_alive, sources, sources_private, extra_sources)
        VALUES
          (:slug,:name,:japanese,:korean,:chinese,:nicknames,:english_variants,
           :sex,:born,:died,:last_seen,:species,:origin,:origin_place,:origin_from,:origin_from_year,:origin_from_kind,:birth_zoo,:mother_ref,:father_ref,:rpf_id,:rpf_url,:studbook_id,:isb_checked,:tags,:instagram,:youtube,:is_alive,:sources,:sources_private,:extra_sources)
    """, [r for _, _, r in panda_rows])
    conn.commit()
    print(f"  ✅ 插入 {len(panda_rows)} 筆個體資料")

    # ── Pass 2：解析家族關係 ───────────────────────────────────
    parent_child_rows: list[tuple] = []   # (child, parent, type)
    twin_pairs: set[frozenset] = set()
    child_rows: list[tuple] = []          # (parent_slug, child_slug) from 子女 table

    for slug, body, _ in panda_rows:
        fam = parse_family(body)

        # 母
        if fam["mother"] and fam["mother"] in all_slugs:
            parent_child_rows.append((slug, fam["mother"], "mother", "confirmed"))

        # 父
        if fam["father"] and fam["father"] in all_slugs:
            parent_child_rows.append((slug, fam["father"], "father", "confirmed"))

        # 雙胞胎
        for twin in fam["twins"]:
            if twin in all_slugs and twin != slug:
                pair = frozenset([slug, twin])
                twin_pairs.add(pair)

        # 子女（從 table 抽取）→ 反向變成 parent_child
        for child_slug in fam["children"]:
            if child_slug in all_slugs and child_slug != slug:
                child_rows.append((slug, child_slug))

    # 子女 table 的關係：知道的是 parent_slug 是誰，child_slug 是誰，
    # 但不知道是 mother 還是 father → 看 parent 的 sex
    slug_to_sex = {slug: row["sex"] for slug, _, row in panda_rows}
    for parent_slug, child_slug in child_rows:
        ptype = "mother" if slug_to_sex.get(parent_slug) == "female" else \
                "father"  if slug_to_sex.get(parent_slug) == "male"   else None
        if ptype:
            rec = (child_slug, parent_slug, ptype, "confirmed")
            if rec not in parent_child_rows:
                parent_child_rows.append(rec)

    # 去重
    parent_child_unique = list({(c,p,t): (c,p,t,conf)
                                 for c,p,t,conf in parent_child_rows}.values())

    cur.executemany("""
        INSERT OR IGNORE INTO parent_child (child_slug, parent_slug, parent_type, confidence)
        VALUES (?,?,?,?)
    """, parent_child_unique)
    conn.commit()
    print(f"  ✅ 插入 {len(parent_child_unique)} 筆親子關係")

    # 多胞胎為「群」屬性：取連通分量的傳遞閉包，補上群內所有兩兩配對。
    # （即使各條目未互相完整列出，例如三胞胎中 Chao 列了 Ren、Nana，
    #   但 Ren／Nana 只列 Chao，仍能讓三隻彼此互為同生群。）
    adj: dict[str, set[str]] = {}
    for pair in twin_pairs:
        a, b = tuple(pair)
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen: set[str] = set()
    for node in list(adj):
        if node in seen:
            continue
        comp, stack = [], [node]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x); comp.append(x)
            stack.extend(adj[x] - seen)
        for i in range(len(comp)):
            for j in range(i + 1, len(comp)):
                twin_pairs.add(frozenset([comp[i], comp[j]]))

    # 雙胞胎
    twin_rows = []
    for pair in twin_pairs:
        a, b = sorted(pair)
        twin_rows.append((a, b))
    twin_rows.sort()  # set 迭代順序不定；排序讓 DB 內容可重現、利於 dump 比對
    cur.executemany("INSERT OR IGNORE INTO twins (slug_a, slug_b) VALUES (?,?)", twin_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(twin_rows)} 組雙胞胎關係")

    # ── 已宣告手足（frontmatter siblings:）───────────────────────
    # 只在共同父母不詳、無法由 parent_child 推導時使用。對稱（單邊列出即可），
    # 兩隻都須有條目才建邊。
    declared_pairs: set[frozenset] = set()
    for slug, sibs in declared_sib_raw.items():
        for sib in sibs:
            if sib in all_slugs and sib != slug:
                declared_pairs.add(frozenset([slug, sib]))
    declared_rows = sorted((tuple(sorted(pair)) for pair in declared_pairs))
    cur.executemany(
        "INSERT OR IGNORE INTO declared_siblings (slug_a, slug_b) VALUES (?,?)",
        declared_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(declared_rows)} 組已宣告手足關係")

    # ── Pass 3：居住史 ─────────────────────────────────────────
    # 居住史唯一來源 = frontmatter zoos（含精確日期）；內文 ## 居住史 表格由
    # tools/gen_residence.py 自動生成，僅供顯示，不再被解析。
    zoo_rows: list[dict] = []
    for slug, body, row in panda_rows:
        fm_text = (WIKI_DIR / (slug + ".md")).read_text(encoding="utf-8")
        fm2, _ = parse_frontmatter(fm_text)
        for z in parse_zoos(fm2.get("zoos", [])):
            zoo_rows.append({"slug": slug, **z})

    # 園名解析為註冊表 canonical（唯一事實來源）；未登記 → 報錯中止
    from zoo_registry import ZooRegistry
    reg = ZooRegistry.load()
    errors = []
    for zr in zoo_rows:
        rec = reg.resolve(zr["zoo_name"])
        if rec is None:
            errors.append((zr["slug"], zr["zoo_name"]))
        else:
            zr["zoo_name"] = rec["canonical"]
    if errors:
        print(f"\n  ❌ {len(errors)} 筆居住史園名不在註冊表 data/zoos.json：")
        for slug, nm in errors:
            print(f"     {slug}: 「{nm}」")
        print("  → 請先在 data/zoos.json 登記該園（或修正拼法），再重建。")
        sys.exit(1)

    cur.executemany("""
        INSERT INTO residences (slug, zoo_name, start_year, end_year, start_date, end_date)
        VALUES (:slug, :zoo_name, :start_year, :end_year, :start_date, :end_date)
    """, zoo_rows)
    conn.commit()
    print(f"  ✅ 插入 {len(zoo_rows)} 筆居住史")

    conn.close()
    print(f"\n✅ 完成！資料庫儲存於: {actual_db}")


if __name__ == "__main__":
    build_db()
