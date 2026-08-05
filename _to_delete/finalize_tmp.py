# -*- coding: utf-8 -*-
import io, os
os.chdir('/sessions/rcw-01jjjpchrx1museujxfcmswa/mnt/red-panda-wiki/wiki')

def sub(fn, pairs):
    s = io.open(fn, encoding='utf-8').read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            print('FAIL %s: %d matches %r' % (fn, n, old[:50]))
            return
        s = s.replace(old, new)
    io.open(fn, 'w', encoding='utf-8').write(s)
    print('updated', fn)

# 1) Ron-Ron #231 漢字名 龍龍（維護者提供 2026-08-05）
sub('ron-ron-1995-06-30.md', [
  ("japanese: ロンロン", "japanese: 龍龍, ロンロン"),
  ("# Ron-Ron（ロンロン）🪐", "# Ron-Ron（龍龍 / ロンロン）🪐"),
  ("sources:\n  - https://redpandafinder.com/#profile/231",
   "sources:\n  - https://redpandafinder.com/#profile/231\n  - 維護者提供（2026-08-05：漢字名 龍龍）"),
])

# 2) index.md
IDX_OLD = "| [[banana-1996-08-09]] | Banana バナナ — Ron-Ron #231 配偶、Sora/Daichi 之母 | ♀ | 1996–2013 \U0001FA90 | 広島市安佐動物公園 \U0001F1EF\U0001F1F5 |"
IDX_NEW = IDX_OLD + "\n" + "\n".join([
 "| [[baron-1999-07-11]] | Baron バロン — Meron 雙胞胎；廣島 → 釧路 → 白濱 | ♂ | 1999–2011 \U0001FA90 | アドベンチャーワールド \U0001F1EF\U0001F1F5 |",
 "| [[meron-1999-07-11]] | Meron メロン — Baron 雙胞胎；[[sora-2002-06-24]]・[[umi-2002-06-24]] 之母 | ♀ | 1999–2014 \U0001FA90 | いしかわ動物園 \U0001F1EF\U0001F1F5 |",
 "| [[suika-2002-08-04]] | Suika スイカ — 11 隻手足中唯一的單胎；廣島 → 宮崎 → 枚方 | ♂ | 2002–2016 \U0001FA90 | ひらかたパーク \U0001F1EF\U0001F1F5 |",
])
sub('index.md', [
  ("> 最後更新：2026-08-05 | 條目總數：873（另有 5 筆條目暫存 wiki/_hidden/，不計入、不上站）",
   "> 最後更新：2026-08-05 | 條目總數：876（另有 5 筆條目暫存 wiki/_hidden/，不計入、不上站）"),
  (IDX_OLD, IDX_NEW),
  ("| [[ron-ron-1995-06-30]] | Ron-Ron ロンロン — Shii 之父",
   "| [[ron-ron-1995-06-30]] | Ron-Ron 龍龍 / ロンロン — Shii 之父"),
])

# 3) log.md（禁 wikilink）
LOG = u"""
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
"""
s = io.open('log.md', encoding='utf-8').read()
if u'suika-2002-08-04' not in s:
    io.open('log.md', 'a', encoding='utf-8').write(LOG)
    print('appended log.md')
else:
    print('log.md already has entry, skipped')
