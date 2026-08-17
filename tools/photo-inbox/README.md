# photo-inbox 腳本（讀者照片投稿對帳／回填）

`photo-inbox-audit` skill 使用的腳本，**這裡（repo `tools/photo-inbox/`）是唯一正本**——
skill 本身不再隨附腳本副本，雲端 session 也不需要再把腳本搬進本機，
直接在 repo 根目錄執行即可（腳本純標準庫、只讀寫 `wiki/*.md` 純文字，
在掛載資料夾上跑是安全的，不像 build_db 需要 SQLite shim）。

## 用法

1. 由 Claude 用 Google Drive 連接器讀投稿 Sheet
   （fileId `1sj1YD-Wjrb88-7JnWfXHWXZyZlGATrl37TMPVMYSGw0`），
   把回傳的**原始 CSV 文字原封不動**存成 `submissions.csv`
   （不用改寫成 JSON；表頭、G 欄多行儲存格、測試列由腳本自行處理。
   舊 JSON 列格式仍相容，欄位見 `audit.py` docstring）。
2. 比對（唯讀，不動 wiki）：

   ```bash
   python3 tools/photo-inbox/audit.py \
     --submissions /path/to/submissions.csv \
     --wiki-dir wiki \
     --json-out /path/to/findings.json
   ```

3. 回填乾淨的待補連結（只碰 `instagram:` frontmatter；加 `--dry-run` 可預覽）：

   ```bash
   python3 tools/photo-inbox/backfill.py \
     --findings /path/to/findings.json \
     --wiki-dir wiki
   ```

## 邊界

- 只寫 `instagram:` 清單，需複查者（疑投錯隻）一律只列出、不自動補。
- **不** git commit、**不**改 Google Sheet（I 欄「已補進 wiki」由維護者手動標記）。
- `wiki/*.md` 為唯一正本。

## 自動放行（2026-08-07/08 維護者裁定，2026-08-17 起腳本內建）

- 重複檢查 b)/d) 的**同生群**（同母＋父不衝突＋生日差 ≤1 天，從 frontmatter `born:`
  與內文 父／母 行的 wikilink 判定）與 **log** 相關組直接過濾、照常回填，
  報告尾行回報放行組數；仍列出的 b)/d) 才是真正要人工複查的。
- a)「同頁同碼」只掃 `instagram:` 區塊本身（與 `sources:` 並列不算重複）。
