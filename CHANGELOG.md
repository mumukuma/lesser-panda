# 網站更新紀錄 Changelog

> 記錄**網站功能**的演進（新功能、改版、修正）。
> 小熊貓**資料**的異動請見 `wiki/log.md`；願望與規劃見 `ROADMAP.md`。
> 新的在最上面。

---

## v0.5 — 2026-06-14 ・ IG 照片展示

- 個體頁新增**照片區**：讀 wiki frontmatter 的 `instagram:` 連結，用 Instagram 官方 embed 顯示（自動署名、連回原貼文，不複製圖片檔）
- 維護方式：在條目 frontmatter 加 `instagram:` 公開貼文連結 → 重建即顯示
- （後續：開放同好投稿的表單，寄站長審核後收錄）

## v0.4 — 2026-06-14 ・ 改用 Astro + Tailwind

- 網站從第一版純 HTML 生成器，遷移到 **Astro + Tailwind CSS**（`web/`），元件化、好維護
- **深色模式**：以系統設定為優先，導覽列可手動切換並記住
- PWA 改用成熟的 vite-pwa（Workbox），更新與快取更穩定
- 改用 **pnpm**；GitHub Actions 同步調整
- 修正：首頁搜尋／動物園按鈕對齊
- 資料管線（`tools/`、`site/scripts/export_json.py`）與 wiki 完全不變

## v0.3 — 2026-06-13 ・ 內容與體驗

- **今天的小熊貓**：首頁顯示當日生日與當日「前往小熊星球」（🌈）
- **語系名字顯示**：中文＝漢字（無則退英文）、日文＝日文名、英文＝英文
- **動物園 logo**：用官網 favicon，可在 `site/data/zoo-logos.json` 手動覆蓋
- **資料完整度檢查工具**（`tools/audit.py`）：與 redpanda-lineage 本地比對，不重爬 RPF
- 家系圖手機體驗：雙指縮放、拖曳平移、載入置中於焦點
- 全站手機版 RWD 調整

## v0.2 — 2026-06-13 ・ 多語系、上線

- **三語系**：繁體中文／日文／英文；首訪依瀏覽器語言自動切換，可手動選（下拉選單）
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
