# 小熊貓家族 Wiki — Schema

> 本文件依照 [llm-wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)設計。  
> LLM 負責撰寫與維護所有 wiki 頁面；你負責提供資料來源與問問題。

---

## 目錄結構

```
red-panda-wiki/
├── SCHEMA.md          ← 本文件（架構說明）
└── wiki/
    ├── index.md       ← 所有條目的目錄（依類別列出）
    ├── log.md         ← 新增記錄的 append-only 日誌
    └── [name]-[born].md ← 各個小熊貓的個人條目（slug = 名字-生日）
```

> **命名規則（2026-06-18 起）**：slug 一律為 `slugify(name)-生日`（生日用 `YYYY-MM-DD`，只知年份用 `YYYY`）。撞名（同名同生日）才加第三層消歧 = **媽媽的名字**（不用父名）。詳見 `CLAUDE.md`「檔名與消歧」。

---

## 頁面格式（YAML frontmatter + Markdown）

每個個人條目的開頭必須有 YAML frontmatter：

```yaml
---
name: 英文名稱
chinese: 中文名稱        # 台灣／中國出生個體的正式中文名；中文介面優先顯示（如 可忻、丫丫）
japanese: 日文名稱（漢字 / 假名）
nicknames: [暱稱1, 暱稱2]
english_variants: [變體拼法1, 變體拼法2]
sex: female | male
born: YYYY-MM-DD
died: YYYY-MM-DD   # 若健在則省略
species: Ailurus fulgens styani | Ailurus fulgens fulgens
zoos:                      # 居住史唯一來源（frontmatter 為準）；內文「## 居住史」表格純衍生，由 tools/gen_residence.py 自動生成、勿手改
  - 動物園名稱 (起 – 訖)     # 園名須為 data/zoos.json 註冊表 canonical（未登記 build 報錯）；起訖可用 YYYY-MM-DD / YYYY / 現居留空。更正居住地只改這裡再重建；地點欄由 data/zoos.json 的 location_ja 自動帶入
rpf_id: RedPandaFinder 的 profile ID
rpf_url: https://redpandafinder.com/#profile/XXX
tags: [標籤]
instagram:                # 選填：同好的公開 IG 貼文連結，網站以官方 embed 展示（自動署名、連回原貼文）
  - https://www.instagram.com/帳號/p/XXXXXXXXX/ 2025-06-01   # 建議用含「帳號」的完整形式；可在連結後加貼文日期，網站依日期新到舊排序；超過 6 篇自動「顯示更多」
sources:
  - https://redpandafinder.com/#profile/XXX
---
```

> `instagram` 為選填。只放**公開**貼文連結；網站用 Instagram 官方 embed 顯示，會自動標註原作者並連回原貼文（不複製圖片檔）。新增後重跑 `build_db.py` → `export_json.py` 即生效。
>
> **連結請盡量用含帳號的完整形式** `https://www.instagram.com/帳號/p/XXXXXXXXX/`（而非僅 `/p/XXXXXXXXX/`）。網站會從 URL 解析出發文帳號，在照片卡片上額外顯示「📷 @帳號」並連回該 IG profile（embed 兩種形式都吃，含帳號不影響顯示）。沒帶帳號的連結仍可正常 embed，只是不會多顯示這行攝影者署名。IG 的「複製連結」常給不含帳號的短形式，curate 時請改存完整形式。

---

## 家族連結慣例

- 使用 `[[wiki-link]]` 格式互相連結（Obsidian 相容）
- 已故成員在名稱後加 🌈 標記
- ½ 代表同父異母或同母異父的半血緣兄弟姊妹

---

## 資料來源

| 來源 | 說明 |
|------|------|
| [RedPandaFinder](https://redpandafinder.com) | 家系、居住地、別名 |
| [Red Panda Lineage Project](https://github.com/wwoast/redpanda-lineage) | 底層血統資料庫 |

---

## 操作流程

### 新增成員
1. 在 `wiki/` 下建立 `[name]-[born].md`（slug = 名字-生日）
2. 填入 YAML frontmatter
3. 撰寫條目內容（基本資料 → 別名 → 居住史 → 家族 → 備注）
4. 更新 `wiki/index.md`
5. 在 `wiki/log.md` 新增一筆記錄

### 更新現有條目
1. 直接編輯對應的 `[name].md`
2. 在 `wiki/log.md` 新增 update 記錄

### 查詢
- 先讀 `wiki/index.md` 找到相關條目
- 再讀取個別頁面取得詳細資料

---

## 標籤體系

| 標籤 | 說明 |
|------|------|
| `styani` | 中華小熊貓亞種 |
| `fulgens` | 喜馬拉雅小熊貓亞種 |
| `female` / `male` | 性別 |
| `deceased` | 已過世 |
| `zoo:多摩動物公園` | 所在動物園 |
| `taofa-family` | Taofa 直系家族成員 |

---

*本 wiki 收錄小熊貓個體檔案，涵蓋相關家族成員與動物園個體。*
