/* 首頁「🗓️ 今日休園」：client 端以 JST 判斷今天哪些日本園休園（deploy 無 cron，
   比照今日生日／新鮮的寶寶模式）。資料來源 window.CLOSED_DATA（建置期由
   data/zoos.json 的 closed_rule 帶入；人讀正本為 closed_ja，兩欄改制需同步）。
   依通常時間表推算，臨時開閉園以官網公告為準（首頁有小字註記）。

   closed_rule schema（任一規則命中即休園；設計見 add_closed_rules 註解與 CHANGELOG）：
   - weekly:        {type:'weekly', dow:['mon',..], holiday:'none|open|next_day|next_weekday',
                     months?, skip_nth?, suspend?:[{from:'MM-DD',to:'MM-DD'}]}
       holiday 省略=none（祝日でも休園）；open=祝日は開園；next_day=祝日なら翌日
       （連続祝日はスキップ）休園；next_weekday=祝日なら直後の平日休園
   - nth_weekly:    {type:'nth_weekly', dow:'mon', nth:[2,4], ...同上..., shift:'next_day'?}
       shift=指定日開園、翌日休園（熊本第4月曜型）
   - week_of_nth_dow:{type:'week_of_nth_dow', dow:'wed', nth:2, months:[4,11], days:'mon-fri'}
       含第N曜日之週的平日全休（円山型）
   - range:         {type:'range', from:'MM-DD', to:'MM-DD'}  每年重複；from>to 跨年
   - range_abs:     {type:'range_abs', from?:'YYYY-MM-DD', to?:'YYYY-MM-DD'}  長期休園
   - date:          {type:'date', on:'MM-DD'}

   祝日表：內嵌 2026–2030（jpholiday 產生、對照内閣府／天文台抽驗；含振替休日・国民の休日），
   比照 season.js 內嵌節氣表前例。表外年份視為無祝日（規則退化為「照字面曜日休」）。 */
(function (root) {
  var HOLIDAYS = {
    2026: ['01-01', '01-12', '02-11', '02-23', '03-20', '04-29', '05-03', '05-04',
      '05-05', '05-06', '07-20', '08-11', '09-21', '09-22', '09-23', '10-12', '11-03', '11-23'],
    2027: ['01-01', '01-11', '02-11', '02-23', '03-21', '03-22', '04-29', '05-03',
      '05-04', '05-05', '07-19', '08-11', '09-20', '09-23', '10-11', '11-03', '11-23'],
    2028: ['01-01', '01-10', '02-11', '02-23', '03-20', '04-29', '05-03', '05-04',
      '05-05', '07-17', '08-11', '09-18', '09-22', '10-09', '11-03', '11-23'],
    2029: ['01-01', '01-08', '02-11', '02-12', '02-23', '03-20', '04-29', '04-30',
      '05-03', '05-04', '05-05', '07-16', '08-11', '09-17', '09-23', '09-24', '10-08', '11-03', '11-23'],
    2030: ['01-01', '01-14', '02-11', '02-23', '03-20', '04-29', '05-03', '05-04',
      '05-05', '05-06', '07-15', '08-11', '08-12', '09-16', '09-23', '10-14', '11-03', '11-04', '11-23']
  };
  var DOW = { sun: 0, mon: 1, tue: 2, wed: 3, thu: 4, fri: 5, sat: 6 };

  /* 日期一律以 {y,m,d} 表示、用 UTC 運算（避免訪客時區干擾；JST 換算見底部） */
  function toMs(t) { return Date.UTC(t.y, t.m - 1, t.d); }
  function fromMs(ms) { var x = new Date(ms); return { y: x.getUTCFullYear(), m: x.getUTCMonth() + 1, d: x.getUTCDate() }; }
  function addDays(t, n) { return fromMs(toMs(t) + n * 864e5); }
  function dow(t) { return new Date(toMs(t)).getUTCDay(); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function mmdd(t) { return pad(t.m) + '-' + pad(t.d); }
  function iso(t) { return t.y + '-' + mmdd(t); }
  function isHol(t) { var a = HOLIDAYS[t.y]; return !!a && a.indexOf(mmdd(t)) >= 0; }
  function nth(t) { return Math.ceil(t.d / 7); }   /* 該日是當月第幾個該曜日 */
  function inMMDD(t, from, to) {
    var v = mmdd(t);
    return from <= to ? v >= from && v <= to : v >= from || v <= to;   /* from>to 跨年 */
  }
  function suspended(rule, t) {
    var s = rule.suspend;
    if (!s) return false;
    for (var i = 0; i < s.length; i++) if (inMMDD(t, s[i].from, s[i].to)) return true;
    return false;
  }
  /* t 是否為該規則的「指定休園曜日」（不含祝日／順延判斷） */
  function matches(rule, t) {
    if (rule.months && rule.months.indexOf(t.m) < 0) return false;
    var day = dow(t);
    if (rule.type === 'weekly') {
      var hit = false;
      for (var i = 0; i < rule.dow.length; i++) if (DOW[rule.dow[i]] === day) hit = true;
      if (!hit) return false;
      if (rule.skip_nth && rule.skip_nth.indexOf(nth(t)) >= 0) return false;
      return true;
    }
    return DOW[rule.dow] === day && rule.nth.indexOf(nth(t)) >= 0;
  }
  /* 指定日 D 為祝日時的順延休園日：next_day 跳過連續祝日；next_weekday 再跳過週末 */
  function substitute(D, pol) {
    var s = addDays(D, 1);
    for (var i = 0; i < 14; i++) {
      var wd = dow(s);
      if (isHol(s) || (pol === 'next_weekday' && (wd === 0 || wd === 6))) { s = addDays(s, 1); continue; }
      return s;
    }
    return s;
  }
  function ruleClosed(rule, t) {
    switch (rule.type) {
      case 'date': return mmdd(t) === rule.on;
      case 'range': return inMMDD(t, rule.from, rule.to);
      case 'range_abs': {
        var v = iso(t);
        return (!rule.from || v >= rule.from) && (!rule.to || v <= rule.to);
      }
      case 'week_of_nth_dow': {
        if (!rule.months || rule.months.indexOf(t.m) < 0) return false;
        var wd = dow(t);
        if (wd === 0 || wd === 6) return false;               /* days:'mon-fri' 固定平日 */
        /* 當月第 nth 個 rule.dow */
        var first = { y: t.y, m: t.m, d: 1 };
        var off = (DOW[rule.dow] - dow(first) + 7) % 7;
        var D = { y: t.y, m: t.m, d: 1 + off + (rule.nth - 1) * 7 };
        var mon = addDays(D, -((dow(D) + 6) % 7));            /* 該週的週一 */
        var ms = toMs(t);
        return ms >= toMs(mon) && ms <= toMs(addDays(mon, 4));
      }
      case 'weekly':
      case 'nth_weekly': {
        if (rule.shift) {                                      /* 指定日開園、翌日休園 */
          var prev = addDays(t, -1);
          return !suspended(rule, prev) && matches(rule, prev);
        }
        var pol = rule.holiday || 'none';
        if (matches(rule, t) && !suspended(rule, t)) {
          if (pol === 'none') return true;
          if (!isHol(t)) return true;
          if (pol === 'open') return false;
          /* next_day / next_weekday：指定日は開園（順延で休む） */
        }
        if (pol === 'next_day' || pol === 'next_weekday') {   /* t 是否為某祝日指定日的順延日 */
          for (var k = 1; k <= 10; k++) {
            var D = addDays(t, -k);
            if (matches(rule, D) && isHol(D) && !suspended(rule, D)) {
              var s = substitute(D, pol);
              if (s.y === t.y && s.m === t.m && s.d === t.d) return true;
            }
          }
        }
        return false;
      }
    }
    return false;
  }
  function isZooClosed(rules, t) {
    for (var i = 0; i < rules.length; i++) if (ruleClosed(rules[i], t)) return true;
    return false;
  }

  var api = { HOLIDAYS: HOLIDAYS, isZooClosed: isZooClosed, isHoliday: isHol };
  /* node 單元測試入口（web/tests/closed.test.mjs） */
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; return; }
  root.RPW_CLOSED = api;

  /* ── 首頁渲染 ── */
  var data = root.CLOSED_DATA;
  var wrap = document.getElementById('today-closed-wrap');
  var box = document.getElementById('today-closed');
  if (!data || !wrap || !box) return;
  var jst = new Date(Date.now() + 9 * 3600e3);                 /* JST = UTC+9（無夏令時間） */
  var today = { y: jst.getUTCFullYear(), m: jst.getUTCMonth() + 1, d: jst.getUTCDate() };
  var esc = function (s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  var PAGE = root.PAGE || root.BASE || '';
  var closed = data.zoos.filter(function (z) { return isZooClosed(z.r, today); });
  if (!closed.length) return;                                  /* 今日無休園 → 整欄保持隱藏 */
  box.innerHTML = closed.map(function (z) {
    return '<a class="pop inline-flex items-center gap-1.5 bg-cream border border-line rounded-full px-3.5 py-1.5 text-[.92rem] no-underline hover:border-amber" href="' +
      PAGE + 'z/' + z.u + '/"><span class="font-semibold">' + esc(z.n) + '</span></a>';
  }).join('');
  wrap.hidden = false;
})(typeof window !== 'undefined' ? window : this);
