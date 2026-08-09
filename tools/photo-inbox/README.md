# photo-inbox 腳本（讀者照片投稿對帳／回填）

`photo-inbox-audit` skill 隨附腳本的本機副本，放這裡是為了省掉每次執行前
把腳本從雲端容器搬進本機的來回。**與 skill 內的版本應保持一致**。

## 用法

1. 由 Claude 用 Google Drive 連接器讀投稿 Sheet
   （fileId `1sj1YD-Wjrb88-7JnWfXHWXZyZlGATrl37TMPVMYSGw0`），
   整理成 `submissions.json`（欄位見 `audit.py` docstring）。
2. 比對（唯讀，不動 wiki）：

   ```bash
   python3 tools/photo-inbox/audit.py \
     --submissions /path/to/submissions.json \
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

- 只寫 `instagram:` 清單，需複查者（疑投錯隻／一圖兩隻）一律只列出、不自動補。
- **不** git commit、**不**改 Google Sheet（I 欄「已補進 wiki」由作者手動標記）。
- `wiki/*.md` 為唯一正本。

## 已知行為

- 重複檢查會掃全部 `wiki/*.md`，與投稿筆數無關，故 b)「同碼跨不同隻」清單恆長；
  其中絕大多數命中 `log.md`（該檔本就收錄所有連結），屬正常噪音。
