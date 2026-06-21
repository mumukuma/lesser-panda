/* 回報表單設定 — Tally
 *
 * 兩組表單，職責分清楚：
 *
 * 1) FEEDBACK_FORMS（資料更正／近況）— 由「個體頁」的「✏️ 回報這頁資料／近況」按鈕使用。
 *    一定針對「某一隻已存在的熊」，靠 hidden fields（panda/slug/url）帶入身分。
 *    批次 1–3：親屬關係／名字／生日／其他／🚚轉園／🌈過世／🍼出生。
 *
 * 2) MISSING_FORMS（報缺：圖鑑還沒有的熊或動物園）— 由 /feedback 頁使用（萬用入口）。
 *    沒有 hidden field（孤兒個體無頁面可進、缺園也不屬於任何一隻），
 *    所以一定要走「不綁定某一隻」的獨立表單，避免 hidden field 錯標。
 *    欄位：類型（缺熊／缺園）／名稱／RPF 或官網連結／補充／暱稱。
 *
 * 在 Tally 建好表單後，把表單網址 https://tally.so/r/XXXXXX 的 XXXXXX 填進對應語系。
 * 尚未填的語系會自動 fallback 到 'zh-TW' 那張；三個都空白時，
 * /feedback 頁會顯示「建置中」訊息（feedback_setup），方便先驗收頁面外觀。
 */

// ── 1) 資料更正／近況（個體頁按鈕；針對已存在的熊）─────────────────
export const FEEDBACK_FORMS = {
  'zh-TW': 'ODr777',   // 「回報資料更正」中文表單（https://tally.so/r/ODr777）
  ja: 'MePRGE',        // 「データ修正のご報告」日文表單（https://tally.so/r/MePRGE）
  en: 'RG2PlK',        // 「Report a correction」英文表單（https://tally.so/r/RG2PlK）
};

export const feedbackFormId = (locale) =>
  FEEDBACK_FORMS[locale] || FEEDBACK_FORMS['zh-TW'] || '';

// ── 2) 報缺：圖鑑還沒有的熊或動物園（/feedback 萬用入口；不綁定某一隻）──
export const MISSING_FORMS = {
  'zh-TW': '2EVJlb',   // 「回報圖鑑沒有的熊或動物園」中文表單（https://tally.so/r/2EVJlb）
  ja: 'ODrJok',        // 「図鑑にいない子・動物園の報告」日文表單（https://tally.so/r/ODrJok）
  en: 'RG2JVv',        // 「Report a missing panda or zoo」英文表單（https://tally.so/r/RG2JVv）
};

export const missingFormId = (locale) =>
  MISSING_FORMS[locale] || MISSING_FORMS['zh-TW'] || '';
