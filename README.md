# 🐾 小熊貓圖鑑 Red Panda Encyclopedia

以 Taofa（桃花）家族為起點的小熊貓（red panda）個體資料庫，目前收錄 360+ 隻、多為日本動物園的個體。資料以手工維護的 Obsidian wiki 為正本，自動生成為一個多語系的靜態網站。

**線上瀏覽**：https://mumukuma.github.io/lesser-panda/

---

## 這是什麼

本專案採 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：人類提供資料來源與問題，LLM 負責撰寫與維護所有條目。`wiki/*.md` 是唯一的真相來源，網站與資料庫都由它自動產生、可隨時重建。

資料來源以 [Red Panda Finder](https://redpandafinder.com) 為主，血統資料參考 [Red Panda Lineage Project](https://github.com/wwoast/redpanda-lineage)。

## 功能

- **個體檔案**：每隻一頁，含生日、物種、居住史與家族關係
- **互動家系圖**：以當前個體為中心展開祖先與後代，手機可縮放／拖曳
- **圖鑑搜尋**：依名字（中／日／英）、動物園、性別、在世與否即時篩選
- **動物園地圖**：標出各園位置、現居個體，並提供路線導航連結
- **三語系**：繁體中文／日文／英文，首訪依瀏覽器語言自動切換，可手動選擇
- **PWA**：可加到手機主畫面、離線瀏覽

## 專案結構

```
.
├── wiki/              # 真相來源：個體條目 + index + log
├── tools/             # wiki → SQLite 的解析與家系查詢工具
├── site/              # 資料管線 + i18n 字串
│   ├── scripts/       # build_db / export_json（wiki → JSON）
│   ├── data/          # 產出的 JSON（中繼資料）
│   └── src/i18n/      # 三語介面字串
├── web/               # Astro + Tailwind 前端（見 web/README.md）
├── CLAUDE.md          # wiki 維護操作手冊
└── SCHEMA.md          # 條目格式規範
```

> 註：早期的 `site/scripts/build.mjs` + `site/src/` 是第一版純 HTML 生成器，
> 現已由 `web/`（Astro + Tailwind）取代；資料管線（`tools/`、`site/scripts/export_json.py`）續用。

## 本地建置

需要 Python 3 與 Node 18+：

```bash
python tools/build_db.py            # wiki → SQLite
python site/scripts/export_json.py  # SQLite → JSON
cd web && npm install && npm run dev # Astro 開發伺服器
```

詳細說明見 [`web/README.md`](web/README.md)。

## 部署

推送到 `main` 分支後，GitHub Actions 會自動重跑上述建置流程並部署到 GitHub Pages（設定見 `.github/workflows/deploy.yml`）。

## 資料來源與致謝

個體資料、家系、居住地與別名主要來自 [Red Panda Finder](https://redpandafinder.com)；底層血統與動物園座標參考 [redpanda-lineage](https://github.com/wwoast/redpanda-lineage)。感謝各動物園與愛好者社群的紀錄。

本專案為非營利的同好整理，若資料來源方有任何疑慮，歡迎來信告知調整。
