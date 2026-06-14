# 小熊貓圖鑑網站（site/）

由 `wiki/*.md` 自動生成的靜態網站（PWA）。**正本永遠是 wiki**，本資料夾全部可重建。

## 重建網站（wiki 更新後執行）

在 wiki 根目錄依序執行：

```bash
python tools/build_db.py              # 1. wiki → SQLite
python site/scripts/export_json.py   # 2. SQLite → site/data/*.json
node site/scripts/build.mjs          # 3. JSON → site/dist/（全站 HTML）
```

零 npm 相依，只需要 Python 3 與 Node 18+。

## 本機預覽

```bash
cd site/dist && python3 -m http.server 8000
```

開 http://localhost:8000 即可。搜尋／地圖／家系圖的資料已內嵌進頁面，
直接雙擊 html 檔（file://）也能用，但建議仍以 http 開啟（PWA 功能需要）。

## 多語系

- 繁中：`/`（根目錄）・日文：`/ja/`・英文：`/en/`，頁面右上角可切換
- 介面字串在 `src/i18n/{zh-TW,ja,en}.json`，新增語言＝翻譯一份 JSON
  並在 `build.mjs` 的 `LOCALES` 加一行

## 部署（要公開時）

`site/dist/` 就是完整網站，丟到任何靜態託管即可：

- **GitHub Pages**：repo Settings → Pages → 指向 dist（或用 Actions 跑上面三步）
- **Cloudflare Pages / Netlify**：build command 設為上面三步，output 設 `site/dist`

## 結構

```
site/
├── scripts/
│   ├── export_json.py   # DB → JSON（含動物園名稱匹配與別名表 ZOO_ALIASES）
│   └── build.mjs        # JSON → HTML（版型、個體頁、搜尋、地圖頁）
├── src/
│   ├── i18n/zh-TW.json  # 全部介面字串（之後加日文就是複製一份翻譯）
│   ├── styles.css       # 主題樣式
│   ├── search.js        # 圖鑑搜尋（前端過濾）
│   ├── map.js           # 動物園地圖（Leaflet/OSM，CDN 載入）
│   ├── tree.js          # 互動家系圖（純 SVG，無相依）
│   ├── sw.js            # service worker（離線快取）
│   └── icon.svg
├── data/                # export_json.py 的輸出（中繼資料，可重建）
│   └── zoos-master.json # 動物園主檔快取（來自 redpanda-lineage，請保留）
└── dist/                # 最終網站（可重建）
```

## 注意事項

- `zoos-master.json` 是動物園座標主檔的快取。若 `/tmp/redpanda-lineage` 不存在，
  export 會直接用快取，**不要刪**。要更新主檔：
  `git clone --depth 1 https://github.com/wwoast/redpanda-lineage /tmp/redpanda-lineage`
- wiki 居住史的園名若匹配不到主檔，會在 `site/data/report.json` 的
  `unmatched_zoo_names` 列出；常用別名請加進 `export_json.py` 的 `ZOO_ALIASES`。
- **動物園 logo**：預設用官網 favicon（透過 Google favicon 服務即時載入）。
  想替某園換成正式 logo，編輯 `site/data/zoo-logos.json`，格式 `{"動物園id": "圖片網址"}`，
  例如 `{"17": "https://example.com/logo.png"}`（id 見 `site/data/zoos.json`）。
  覆蓋優先於 favicon。
- 第二期規劃（badge、IG 連結）資料會存瀏覽器 localStorage，與本生成流程無關。
