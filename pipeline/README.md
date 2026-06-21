# pipeline/ — 資料管線與管線輸出

> ⚠️ **這不是網站。** 真正的前端是 `web/`（Astro + Tailwind）。
> 本資料夾現在只負責「把 wiki 轉成網站要吃的 JSON」，以及存放介面字串與動物園主檔快取。
>
> 第一版純 HTML 生成器（`scripts/build.mjs` + `src/*.js` + `dist/`）已於 2026-06 移除，由 `web/` 取代。

正本永遠是 `wiki/*.md`；本資料夾全部可重建。

## 重建資料（wiki 更新後執行）

在 wiki 根目錄依序執行：

```bash
python tools/build_db.py             # 1. wiki → SQLite（redpanda.db）
python pipeline/scripts/export_json.py   # 2. SQLite → pipeline/data/*.json
```

接著由 `web/` 把 JSON 建成網站，見 `web/README.md`。

## 結構

```
pipeline/
├── scripts/
│   └── export_json.py   # DB → JSON（含動物園名稱匹配與別名表 ZOO_ALIASES）
├── src/
│   └── i18n/            # 三語介面字串（web/ 直接讀這三個檔）
│       ├── zh-TW.json
│       ├── ja.json
│       └── en.json
└── data/                # export_json.py 的輸出，web/ 的資料來源
    ├── pandas.json      # 個體（gitignore，可重建）
    ├── zoos.json        # 動物園含座標與現居個體（gitignore，可重建）
    ├── family.json      # 家系邊（gitignore，可重建）
    ├── report.json      # 匹配報告（gitignore，可重建）
    ├── zoos-master.json # 動物園座標主檔快取（來自 redpanda-lineage，請保留）
    ├── zoo-logos.json   # 各園 logo 覆蓋表（人工維護）
    └── zoo-names.json   # 園名對照
```

> 動物園的唯一事實來源是根目錄的 `data/zoos.json`（作者維護）。
> `export_json.py` 讀它，再與 `zoos-master.json` 的座標主檔匹配後輸出 `pipeline/data/zoos.json`。

## 注意事項

- `zoos-master.json` 是動物園座標主檔的快取。若 `/tmp/redpanda-lineage` 不存在，
  export 會直接用快取，**不要刪**。要更新主檔：
  `git clone --depth 1 https://github.com/wwoast/redpanda-lineage /tmp/redpanda-lineage`
- wiki 居住史的園名若匹配不到主檔，會在 `pipeline/data/report.json` 的
  `unmatched_zoo_names` 列出；常用別名請加進 `export_json.py` 的 `ZOO_ALIASES`。
- **動物園 logo**：預設用官網 favicon。想替某園換成正式 logo，
  編輯 `pipeline/data/zoo-logos.json`，格式 `{"動物園id": "圖片網址"}`
  （id 見根目錄 `data/zoos.json`）。覆蓋優先於 favicon。
- 新增語言＝在 `src/i18n/` 複製一份翻譯 JSON，`web/` 端再登記該語言。
