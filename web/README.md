# web/ — Astro + Tailwind 前端

小熊貓圖鑑的網站，用 [Astro](https://astro.build) + Tailwind CSS 建置。
資料來自 Python 管線產出的 `../site/data/*.json`（正本仍是 `wiki/*.md`）。

## 開發 / 建置

需 Node 18+。**先確保資料已產生**（在 repo 根目錄）：

```bash
python tools/build_db.py
python site/scripts/export_json.py
```

然後在 `web/`（使用 pnpm）：

```bash
pnpm install
pnpm dev       # 本機開發伺服器
pnpm build     # 輸出 web/dist/
pnpm preview   # 預覽 build 結果
```

> 沒裝 pnpm 的話：`corepack enable`（Node 內建）即可使用，或 `npm i -g pnpm`。

> 資料路徑是相對於 `web/` 的 `../site/data`，所以 build 必須在 `web/` 目錄執行。

## 結構

```
web/
├── astro.config.mjs       # base=/lesser-panda、Tailwind、PWA(vite-pwa)
├── tailwind.config.cjs    # 顏色對應 CSS 變數；深色模式由變數切換
├── src/
│   ├── lib/data.js        # 讀 ../site/data + i18n，算衍生資料（家系、搜尋、漢字名）
│   ├── lib/links.js       # 連結 helper
│   ├── layouts/Layout.astro    # header/nav/語言下拉/深色切換/全域變數
│   ├── components/        # Home / Search / Zoos / Panda
│   ├── pages/[...path].astro    # 單一 catch-all 生成全部 1083 頁（3 語系）
│   └── styles/global.css  # Tailwind + 主題變數（淺/深）+ 家系圖/地圖樣式
└── public/
    ├── js/                # 互動腳本（search/map/tree/today/lang/theme）
    ├── vendor/            # Leaflet（本地化）
    └── icon.svg
```

## 深色模式

以 OS 設定（`prefers-color-scheme`）為預設，使用者可用導覽列 🌙/☀️ 手動切換並記住
（`public/js/theme.js` 寫入 `html[data-theme]`）。顏色全走 CSS 變數，深色時整組翻轉。

## 部署

GitHub Actions（`.github/workflows/deploy.yml`）會跑 Python 管線 → `cd web && pnpm install --frozen-lockfile && pnpm build`
→ 部署 `web/dist` 到 GitHub Pages（base path `/lesser-panda/`）。
