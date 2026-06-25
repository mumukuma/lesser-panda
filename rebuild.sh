#!/usr/bin/env bash
#
# rebuild.sh — 改完 wiki/*.md 後，一鍵重建所有衍生資料
#
#   1. gen_residence  依 frontmatter zoos: 重生各條目「## 居住史」表格
#   2. build_db       wiki/*.md → redpanda.db（會驗證園名，未登記即報錯）
#   3. export_json    redpanda.db → pipeline/data/*.json（網站資料）
#
# 用法：在 repo 根目錄執行  bash rebuild.sh
# 之後 git commit / push，GitHub Actions 會自動建置部署網站。
#
set -euo pipefail
cd "$(dirname "$0")"   # 切到 repo 根目錄（本檔所在處）

echo "==> [1/3] gen_residence（重生居住史表格）"
# gen_residence 的守門已改成「改寫前後自我比對」，完全在執行內完成、不依賴外部
# 快照檔（若重生後掉了任何園會直接中止），故這裡直接呼叫即可。
python3 tools/gen_residence.py

echo "==> [2/3] build_db（建 SQLite，驗證園名）"
python3 tools/build_db.py

echo "==> [3/3] export_json（匯出網站 JSON）"
python3 pipeline/scripts/export_json.py

echo "==> 完成。記得 git commit / push 讓網站更新。"
