#!/usr/bin/env bash
#
# verify.sh — 資料驗證單一關卡（只讀，不改任何檔案）
#
# 把原本要分開記得跑的三件事收斂成一支：
#   1. 取得/更新 redpanda-lineage（比對基準，"非權威"；離線就略過比對）
#   2. audit.py --strict     wiki 完整度 + 與 lineage 比對
#   3. check_twins.py        多胞胎稽核
#
# 擋關原則（符合 CLAUDE.md 資料來源原則）：
#   - 只有"真正的 wiki 整合性錯誤"會擋：
#       · audit 的 rpf_id 重複（--strict 計入）
#       · check_twins 的 E 級（連錯隻／同生群生日>±1天／群過大）→ 它自己 exit 1
#   - 與 lineage 的"不符"只列出提示、"永不擋"（lineage 非權威，僅供作者檢視）。
#   - 缺欄位、單邊缺父母等警告也不擋。
#
# 用法：
#   bash tools/verify.sh        # 手動跑
#   （已掛 .git/hooks/pre-push → push 前自動跑，未通過即中止 push）
#
set -uo pipefail
cd "$(dirname "$0")/.."   # 切到 repo 根目錄（本檔在 tools/）

LINEAGE=/tmp/redpanda-lineage

echo "==> [1/3] 更新 redpanda-lineage（比對基準，非權威）"
if [ -d "$LINEAGE/.git" ]; then
  if git -C "$LINEAGE" pull --ff-only --depth 1 >/dev/null 2>&1; then
    echo "    已更新既有快照"
  else
    echo "    ⚠️ 無法更新（離線？）→ 沿用既有快照"
  fi
else
  if git clone --depth 1 https://github.com/wwoast/redpanda-lineage "$LINEAGE" >/dev/null 2>&1; then
    echo "    已 clone"
  else
    echo "    ⚠️ 無法 clone（離線？）→ 本次略過 lineage 比對（wiki 自身檢查照跑）"
  fi
fi

echo
echo "==> [2/3] audit（資料完整度 + lineage 比對；僅 rpf_id 重複等內部錯誤會擋）"
python3 tools/audit.py --strict
audit_rc=$?

echo
echo "==> [3/3] check_twins（多胞胎稽核；E 級錯誤會擋）"
python3 tools/check_twins.py
twins_rc=$?

echo
echo "================================================================"
if [ "$audit_rc" -ne 0 ] || [ "$twins_rc" -ne 0 ]; then
  echo "❌ 驗證未通過（audit=$audit_rc, check_twins=$twins_rc）。"
  echo "   請修正上方 🔴 / E 級問題後再 push。"
  echo "   （lineage『不符』與各項警告屬提示、不會擋。）"
  exit 1
fi
echo "✅ 驗證通過。"
