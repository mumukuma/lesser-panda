/* 回報表單設定 — Tally
 *
 * 兩組表單，職責分清楚：
 *
 * 1) FEEDBACK_FORMS（資料更正／近況）— 由「個體頁」的「✏️ 回報這頁資料／近況」按鈕使用。
 *    一定針對「某一隻已存在的熊」，靠 hidden fields（panda/slug/url）帶入身分。
 *    批次 1–3：親屬關係／名字／生日／其他／🚚轉園／🌈過世／🍼出生。
 *
 * 2) MISSING_FORMS（/feedback 頁萬用回報入口；不綁定某一隻）。
 *    沒有 hidden field（孤兒個體無頁面可進、缺園也不屬於任何一隻），
 *    所以走「不綁定某一隻」的獨立表單，避免 hidden field 錯標。
 *    第一題為「類型」下拉，其延伸題目走 Tally 條件邏輯（同 ODr777 多頁分支）。
 *    類型選項：缺熊／缺園／其他建議·意見／許願池（在 Tally 表單裡維護，非程式端）。
 *
 * 在 Tally 建好表單後，把表單網址 https://tally.so/r/XXXXXX 的 XXXXXX 填進對應語系。
 * 尚未填的語系會自動 fallback 到 'zh-TW' 那張；三個都空白時，
 * /feedback 頁會顯示「建置中」訊息（feedback_setup），方便先驗收頁面外觀。
 */

// ── 1) 資料更正／近況（個體頁按鈕；針對已存在的熊）─────────────────
// 2026-06-22 起三語合併為單張三語表單（中／日／英並列），舊單語表單已退役刪除。
// 三個語系皆指向同一張 ODr777。
export const FEEDBACK_FORMS = {
  'zh-TW': 'ODr777',   // 「回報資料更正」三語表單（https://tally.so/r/ODr777）
  ja: 'ODr777',        // 同上（合併後共用）
  en: 'ODr777',        // 同上（合併後共用）
};

export const feedbackFormId = (locale) =>
  FEEDBACK_FORMS[locale] || FEEDBACK_FORMS['zh-TW'] || '';

// ── 2) 報缺：圖鑑還沒有的熊或動物園（/feedback 萬用入口；不綁定某一隻）──
// 2026-06-22 起三語合併為單張三語表單，舊單語表單已退役刪除。三語皆指向 2EVJlb。
export const MISSING_FORMS = {
  'zh-TW': '2EVJlb',   // 「回報缺少的熊或動物園」三語表單（https://tally.so/r/2EVJlb）
  ja: '2EVJlb',        // 同上（合併後共用）
  en: '2EVJlb',        // 同上（合併後共用）
};

export const missingFormId = (locale) =>
  MISSING_FORMS[locale] || MISSING_FORMS['zh-TW'] || '';
