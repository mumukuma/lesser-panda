# 🐾 小熊貓圖鑑 Red Panda Encyclopedia

小熊貓（red panda）個體資料庫，目前收錄 **1,000+ 隻**（精確數以 `wiki/index.md` 頁首為準，另有少數條目暫存），多為日本（及部分海外）動物園的個體。資料以手工校訂的 Obsidian wiki 為正本，自動生成為一個五語系的靜態網站。

**線上瀏覽**：https://ressapanda.com

---

## 這是什麼

本專案採 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：人類提供資料來源與問題，LLM 負責撰寫與維護所有條目。`wiki/*.md` 是唯一的真相來源，網站與資料庫都由它自動產生、可隨時重建。

資料正本為作者手工校訂的 `wiki/*.md`。經作者大量校訂後，wiki 的可信度已高於外部資料庫，故自 2026-07 起 [Red Panda Finder](https://redpandafinder.com/) 已降為「線索」——僅在無官方來源時當參考，衝突一律以 wiki 為準。新條目以園方公告等官方一手來源優先。動物園資料另以 `data/zoos.json` 註冊表（350+ 座園）為唯一來源。

## 功能

- **個體檔案**：每隻一頁，含生日、物種、居住史與家族關係（居住史表格由 `zoos:` 自動生成，標出 🐣出生地／🏡現居；來源區塊只顯示官方來源）
- **互動家系圖**：以當前個體為中心展開祖先與後代，手機可縮放／拖曳
- **日本家系全圖**：`/jptree/` 一次呈現最大連通家族（近 700 隻，含繞經海外的祖先），世代分層＋色帶佈局
- **圖鑑搜尋**：依名字（中／日／英）、動物園、性別、在世與否即時篩選
- **動物園地圖與園頁**：地圖標出各園位置與現居個體；每座園另有專頁（`z/<園>/`），含官網與路線導航連結
- **統計頁**：`/stats/` 彙整族群概況（園別、性別、在世比例等）
- **今天的小熊貓**：首頁列出當日生日與當日「前往小熊星球」的個體
- **新鮮的寶寶**：出生季（6/1–11/30）首頁展示當季新生寶寶，含「蘋果籽」佔位條目
- **照片與影片**：以 Instagram 官方 embed 展示同好公開貼文（自動署名並連回原貼文）；另有 YouTube 影片分頁，以縮圖卡片顯示、點擊才載入播放器
- **物種介紹頁**：`/species/` 介紹「什麼是小熊貓」與喜馬拉雅（fulgens）／中國（styani）兩物種的分辨；個體頁「物種」欄直連對應段落
- **五語系**：繁體中文／簡體中文／日文／英文／韓文，首訪依 IP 與瀏覽器語言自動切換，可手動選擇；名字依語系顯示（簡體為建置期繁→簡轉換，正本仍維持繁體）
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
├── pipeline/              # 資料管線 + i18n 字串
│   ├── scripts/       # export_json（SQLite → JSON）
│   ├── data/          # 產出的 JSON（中繼資料）
│   └── src/i18n/      # 五語介面字串（zh-TW／zh-CN／ja／en／ko）
├── web/               # Astro + Tailwind 前端（見 web/README.md）
├── CLAUDE.md          # wiki 維護操作手冊
└── SCHEMA.md          # 條目格式規範
```

> 註：第一版純 HTML 生成器（`build.mjs` + `src/*.js` + `dist/`，當時在舊的 `site/` 目錄）
> 已於 2026-06 移除，由 `web/`（Astro + Tailwind）取代；該目錄並更名為 `pipeline/`，
> 現只剩資料管線（`scripts/export_json.py`）、管線輸出（`data/`）與五語介面字串（`src/i18n/`）。

## 本地建置

需要 Python 3 與 Node 18+：

```bash
python3 tools/gen_residence.py       # 由 zoos: 重生居住史表格
python3 tools/build_db.py            # wiki → SQLite（園名未登記會報錯）
python3 pipeline/scripts/export_json.py  # SQLite → JSON
cd web && pnpm install && pnpm dev   # Astro 開發伺服器
```

詳細說明見 [`web/README.md`](web/README.md)。

## 部署

推送到 `main` 分支後，GitHub Actions 會自動重跑上述建置流程並部署到 GitHub Pages，以自訂網域 [ressapanda.com](https://ressapanda.com) 對外服務（設定見 `.github/workflows/deploy.yml`）。

## 資料來源與致謝

資料正本為作者手工校訂的 wiki，以園方公告等官方一手來源為優先。建立初期參考了 [Red Panda Finder](https://redpandafinder.com/)（家系、居住地、別名、底層血統與動物園座標），現已降為線索、非權威，一律以作者校訂為準。亦感謝各動物園、透過回報表單提供資料的讀者，以及愛好者社群的紀錄。

本專案為非營利的同好整理，若資料來源方有任何疑慮，歡迎來信告知調整。
