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
    └── [name].md      ← 各個小熊貓的個人條目
```

---

## 頁面格式（YAML frontmatter + Markdown）

每個個人條目的開頭必須有 YAML frontmatter：

```yaml
---
name: 英文名稱
japanese: 日文名稱（漢字 / 假名）
nicknames: [暱稱1, 暱稱2]
english_variants: [變體拼法1, 變體拼法2]
sex: female | male
born: YYYY-MM-DD
died: YYYY-MM-DD   # 若健在則省略
species: Ailurus fulgens styani | Ailurus fulgens fulgens
zoos:
  - 動物園名稱 (起訖年份)
rpf_id: RedPandaFinder 的 profile ID
rpf_url: https://redpandafinder.com/#profile/XXX
tags: [標籤]
sources:
  - https://redpandafinder.com/#profile/XXX
---
```

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
1. 在 `wiki/` 下建立 `[name].md`
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

*本 wiki 以 Taofa（桃花）為核心起點，未來可擴展至所有相關家族成員。*
