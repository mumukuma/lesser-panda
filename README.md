# 🐾 小熊貓圖鑑 Red Panda Encyclopedia

小熊貓（red panda）個體資料庫，目前收錄 369 隻、多為日本動物園的個體。資料以手工校訂的 Obsidian wiki 為正本，自動生成為一個多語系的靜態網站。

**線上瀏覽**：https://mumukuma.github.io/lesser-panda/

---

## 這是什麼

本專案採 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：人類提供資料來源與問題，LLM 負責撰寫與維護所有條目。`wiki/*.md` 是唯一的真相來源，網站與資料庫都由它自動產生、可隨時重建。

資料正本為作者手工校訂的 `wiki/*.md`；[Red Panda Finder](https://redpandafinder.com) 與 [Red Panda Lineage Project](https://github.com/wwoast/redpanda-lineage) 僅作初期建立的參考，非權威，衝突一律以 wiki 為準。動物園資料另以 `data/zoos.json` 註冊表為唯一來源。

## 功能

- **個體檔案**：每隻一頁，含生日、物種、居住史與家族關係（居住史表格由 `zoos:` 自動生成，標出 🐣出生地／🏡現居）
- **互動家系圖**：以當前個體為中心展開祖先與後代，手機可縮放／拖曳
- **圖鑑搜尋**：依名字（中／日／英）、動物園、性別、在世與否即時篩選
- **動物園地圖**：標出各園位置、現居個體，並提供官網與路線導航連結
- **今天的小熊貓**：首頁列出當日生日與當日「前往小熊星球」的個體
- **IG 照片內嵌**：以 Instagram 官方 embed 展示同好公開貼文，自動署名並連回原貼文
- **三語系**：中文／日文／英文，首訪依瀏覽器語言自動切換，可手動選擇；名字依語系顯示（中文＝中文名／漢字、日文＝日文名）
- **深色模式**：以系統設定為優先，可在導覽列手動切換
- **PWA**：可加到手機主畫面、離線瀏覽

## 專案結構

```
.
├── wiki/              # 真相來源：個體條目 + index + log
├── data/              # 動物園註冊表 zoos.json（園資料唯一事實來源）
├── tools/             # wiki → SQLite 解析、家系查詢、園名 resolver、居住史生成
│   ├── build_db.py / query.py
│   ├── zoo_registry.py    # 載入 data/zoos.json 並比對園名
│   └── gen_residence.py   # 由 zoos: 自動生成內文居住史表格
├── site/              # 資料管線 + i18n 字串
│   ├── scripts/       # export_json（SQLite → JSON）
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
python3 tools/gen_residence.py       # 由 zoos: 重生居住史表格
python3 tools/build_db.py            # wiki → SQLite（園名未登記會報錯）
python3 site/scripts/export_json.py  # SQLite → JSON
cd web && pnpm install && pnpm dev   # Astro 開發伺服器
```

詳細說明見 [`web/README.md`](web/README.md)。

## 部署

推送到 `main` 分支後，GitHub Actions 會自動重跑上述建置流程並部署到 GitHub Pages（設定見 `.github/workflows/deploy.yml`）。

## 資料來源與致謝

資料正本為作者手工校訂的 wiki。建立初期參考了 [Red Panda Finder](https://redpandafinder.com)（家系、居住地、別名）與 [redpanda-lineage](https://github.com/wwoast/redpanda-lineage)（底層血統、動物園座標），兩者皆非權威，之後以作者校訂為準。感謝各動物園與愛好者社群的紀錄。

本專案為非營利的同好整理，若資料來源方有任何疑慮，歡迎來信告知調整。
