/* 回報表單設定 — Tally
 *
 * 在 Tally 建好表單後，把表單網址 https://tally.so/r/XXXXXX 的 XXXXXX
 * 填進下面對應語系。建議三語各建一張（用 Tally 的「Duplicate」複製後翻譯題目），
 * 網站會依目前介面語言內嵌對應那一張。
 *
 * 尚未填的語系會自動 fallback 到 'zh-TW' 那張；三個都空白時，
 * /feedback 頁會顯示「建置中」訊息（feedback_setup），方便先驗收頁面外觀。
 */
export const FEEDBACK_FORMS = {
  'zh-TW': 'ODr777',   // 「回報資料更正」中文表單（https://tally.so/r/ODr777）
  ja: 'MePRGE',        // 「データ修正のご報告」日文表單（https://tally.so/r/MePRGE）
  en: 'RG2PlK',        // 「Report a correction」英文表單（https://tally.so/r/RG2PlK）
};

export const feedbackFormId = (locale) =>
  FEEDBACK_FORMS[locale] || FEEDBACK_FORMS['zh-TW'] || '';
