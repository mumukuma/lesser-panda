# International Red Panda Studbook（ISB）2008 年版原檔

Rotterdam Zoo（Diergaarde Blijdorp）Angela Glatston 編的**國際血統登録書**，
`Ailurus fulgens` 全球圈養族群**自 1977 年起的完整登録簿**，
資料截止 **2008-12-31**，2009-10-01 以 Sparks v1.54 印出。

- **2,703 筆個體**（TOTALS 行：1205♂ / 1233♀ / 292 不詳 = 2730 含重覆事件）
- 兩亞種都收：`fulgens` 與 `styani`
- 每筆含：**血統番號、性別、生日（含 `~` 推定）、父番號、母番號、逐次移動園與日期、
  園內 local ID、事件（Capture／Birth／Transfer／Death）、名字、地區血統簿番號（JAZGA／AZA／ESB）、亞種**
- 死亡個體另附**死因分類**（`[Death by: ...]`）

## 檔案

| 檔 | 說明 |
|---|---|
| `ISB-2008.pdf` | 原始 PDF（680,743 bytes） |
| `ISB-2008.txt` | `pdftotext -layout` 抽出的純文字（保留欄位對齊，便於 grep） |
| `ISB-2008-register.csv` | 解析成表：`stud,sex,birth,sire,dam,taxon,name,death,events` |
| `studbook_id-對帳-2026-08-09.csv` | wiki `studbook_id` 逐筆對帳結果（見 `docs/ISB-2008-對帳-2026-08-09.md`） |

## ⚠️ 原始網址已失效（2026-08-09 確認）

canonical 出處：

```
http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%20Panda%20Studbook.pdf
```

該站 2012 年後改版，整個 `assetmanager` PDF 目錄下架（2024 年快照為 301），
園方資料全面轉進 ZIMS，**公開 PDF 從此消失、Google 也已完全去索引**。

線上覆核走 Wayback：

```
https://web.archive.org/web/20120128200628/http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%20Panda%20Studbook.pdf
```

### 重新下載的坑

Wayback 對這個路徑**要把空白二次編碼成 `%2520`**，否則回 `400 Bad request`：

```
https://web.archive.org/web/20120128200628id_/http://www.rotterdamzoo.nl/import/assetmanager/2/6732/Red%2520Panda%2520Studbook.pdf
```

只有一個版本被存檔（5 個快照同 digest），沙盒 proxy 擋 `web.archive.org`，
要用維護者的 Chrome 抓。

## 這批號碼＝RPF 的 `studbook.id`（已證實）

RPF `/export/redpanda.json` 的 `studbook.id` **就是這本國際血統番號**，不是別的流水號。
逐筆驗證見 `docs/ISB-2008-對帳-2026-08-09.md`；三個獨立錨點：

| 番號 | ISB 記載 | 與 wiki 既有資料 |
|---|---|---|
| 8935 / 8936 | 中國野生 `~1987`，1989-10-11 入 ITOZU（到津） | 大州／輪輪「1989-10-11 入園」完全吻合 |
| 9177 | 1991-06-24 生於 SABAE（鯖江），名 KUSU，1998-02-23 轉 ITOZU | 楠 `kusu` 生日吻合 |
| 8976 | 名 NAMU，中國野生 `~1987`，1989-06-01 入 TOMIOKA，1994-10-15 歿 | 佐證 `namu-1987` 的生年修正 |

## 其他版本狀態（2026-08-09 盤點）

| 版本 | 內容 | 取得狀況 |
|---|---|---|
| **2008 年版（本檔）** | 1977–2008 全登録簿，兩亞種 | ✅ 已存檔 |
| 2006 styani（印 2008-02-05） | 該年在園 306 隻 / 81 園 | Yumpu 唯讀，內容已被本檔涵蓋 |
| 2008 增補（印 2009-10-01） | 該年出生／死亡／移動摘要 | Yumpu 唯讀，內容已被本檔涵蓋 |
| 2010-12-31 在園名單（`fulgens`） | 僅在園名單 | Yumpu 唯讀，**2009–2011 缺口在這裡** |
| 2012-01-01 在園名單（`fulgens`） | 僅在園名單 | Yumpu 唯讀，**2009–2011 缺口在這裡** |
| 印度國家血統登録書 | 印度各園 `fulgens`，2008／2013 兩版 | 官方仍公開直連 `cza.nic.in` / `wii.gov.in` |

Yumpu 四份的上傳帳號就是 `rotterdamzoo.nl` 本人（園方當年 PDF 目錄被整批鏡射）。

## 找這類檔案的搜法（備忘）

原站死了之後有效的關鍵字是**印在每頁上的固定字串**，不是標題：

- `"a.glatston@rotterdamzoo.nl"`
- `"using Sparks v1.54"` ＋ `"Ailurus"` ← 最好用，Sparks 是產生這些血統簿的軟體，
  這串同時撈出 Rotterdam 版與印度版
- `"List of all Ailurus fulgens" alive`

鏡射農場：`site:yumpu.com`、docplayer、vdocuments、dokumen.pub、studylib、pdfslide。
原站檔案清單走 Wayback CDX：

```
https://web.archive.org/cdx/search/cdx?url=<domain>&matchType=domain&filter=original:.*[Ss]tudbook.*&collapse=urlkey&fl=original,timestamp,mimetype
```

現任 GSMP convenor 是 Rotterdam 的 **Janno Weerman**（Glatston 已交棒），要正式資料直接寫信。
北美區域血統簿保管者為 **Mary Noel**（見 wbza.in 的 2019 GSMP workshop 報告）。
