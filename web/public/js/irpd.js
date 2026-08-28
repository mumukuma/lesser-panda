/* /irpd/ 季節段揭示：本站「今年的寶寶陸續亮相」那段只在每年 6/1–11/30 成立，
   其餘時間讀起來是錯的。比照首頁 #newborns-season 由 client 端依訪客當下日期判斷
   （deploy 無 cron，建置期判斷會過期）；預設 hidden，no-JS 保持隱藏。
   蘋果籽歸零時（10 月盤點轉正後）整段也不顯示——data-seeds 由建置期帶入。 */
(function () {
  var el = document.getElementById('irpd-season');
  if (!el) return;
  var fake = null;
  try {
    if (/^(localhost|127\.|\[?::1)/.test(location.hostname)) {
      var q = new URLSearchParams(location.search).get('today');
      if (q && /^\d{4}-\d{2}-\d{2}$/.test(q)) fake = new Date(q + 'T12:00:00');
      if (fake && isNaN(+fake)) fake = null;
    }
  } catch (e) {}
  var mo = (fake || new Date()).getMonth() + 1;
  if (mo >= 6 && mo <= 11 && +(el.dataset.seeds || 0) > 0) el.hidden = false;
})();
