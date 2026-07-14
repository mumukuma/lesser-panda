#!/usr/bin/env bash
#
# verify.sh — 資料驗證單一關卡（只讀，不改任何檔案）
#
# 2026-07-14 起不再抓取／比對 redpanda-lineage（wiki 可信度已高於 lineage，
# lineage 降為「線索」；要比對請手動跑 `python3 tools/audit.py --lineage`）。
# 收斂為兩件事：
#   1. audit.py --strict     wiki 完整度（自身檢查）
#   2. check_twins.py        多胞胎稽核
#
# 擋關原則（符合 CLAUDE.md 資料來源原則）：
#   - 只有"真正的 wiki 整合性錯誤"會擋：
#       · audit 的 rpf_id 重複（--strict 計入）
#       · check_twins 的 E 級（連錯隻／同生群生日>±1天／群過大）→ 它自己 exit 1
#   - 缺欄位、單邊缺父母等警告不擋。
#
# 用法：
#   bash tools/verify.sh        # 手動跑
#   （已掛 .git/hooks/pre-push → push 前自動跑，未通過即中止 push）
#
set -uo pipefail
cd "$(dirname "$0")/.."   # 切到 repo 根目錄（本檔在 tools/）

echo "==> [1/2] audit（資料完整度；僅 rpf_id 重複等內部錯誤會擋）"
python3 tools/audit.py --strict
audit_rc=$?

echo
echo "==> [2/2] check_twins（多胞胎稽核；E 級錯誤會擋）"
python3 tools/check_twins.py
twins_rc=$?

echo
echo "================================================================"
if [ "$audit_rc" -ne 0 ] || [ "$twins_rc" -ne 0 ]; then
  echo "❌ 驗證未通過（audit=$audit_rc, check_twins=$twins_rc）。"
  echo "   請修正上方 🔴 / E 級問題後再 push。"
  echo "   （各項警告屬提示、不會擋。）"
  exit 1
fi
echo "✅ 驗證通過。"
