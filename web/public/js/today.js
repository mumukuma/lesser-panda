/* 首頁「今天的小熊貓」：依使用者當下日期列出今日生日與今日前往小熊星球 */
(function () {
  /* 本機預覽開關：只在 localhost 生效，網址帶 ?today=YYYY-MM-DD 即可假裝是那一天，
     本檔所有依日期的區塊（新寶寶／IRPD 倒數／今日生日／小熊星球）一起吃到。
     正式站（非 localhost）完全忽略此參數。加 T12:00 定在中午避免時區邊界。 */
  var fake = null;
  try {
    if (/^(localhost|127\.|\[?::1)/.test(location.hostname)) {
      var q = new URLSearchParams(location.search).get('today');
      if (q && /^\d{4}-\d{2}-\d{2}$/.test(q)) fake = new Date(q + 'T12:00:00');
      if (fake && isNaN(+fake)) fake = null;
    }
  } catch (e) {}
  var dateNow = function () { return fake ? new Date(+fake) : new Date(); };

  /* 「新鮮的寶寶」展示區間：每年 6/1 – 11/30 揭示（依訪客當下日期，與最後一次建置無關）。
     區間外整段隱藏；區間內是否有寶寶由建置期內容決定（無則顯示佔位字）。 */
  var sec = document.getElementById('newborns-season');
  if (sec) { var mo = dateNow().getMonth() + 1; if (mo >= 6 && mo <= 11) sec.hidden = false; }

  /* 國際小熊貓日倒數：活動日＝每年 9 月第三個週六（client 端逐年計算）。
     每年 8/16 起揭示倒數、活動當天換慶祝文案＋ .is-today 樣式、隔天起收起。
     與 TODAY_DATA 無關（只用 window.T），故放在下方 early return 之前。 */
  var ib = document.getElementById('irpd-banner');
  if (ib && window.T) {
    var d0 = dateNow();
    var y0 = d0.getFullYear();
    var sep1 = new Date(y0, 8, 1).getDay();                      // 9/1 星期（0=日…6=六）
    var irpd = new Date(y0, 8, 1 + ((6 - sep1 + 7) % 7) + 14);   // 第三個週六
    var t0 = new Date(y0, d0.getMonth(), d0.getDate());          // 今日零時（免時分秒誤差）
    var left = Math.round((irpd - t0) / 864e5);
    if (t0 >= +new Date(y0, 7, 16) && left >= 0) {
      var tEl = document.getElementById('irpd-text');
      var sEl = document.getElementById('irpd-sub');
      var dStr = (irpd.getMonth() + 1) + '/' + irpd.getDate();
      /* 倒數天數包 span.irpd-n 放大強調；i18n 字串為自家維護內容（本檔他處亦直插 T.*） */
      if (tEl) tEl.innerHTML = left === 0 ? window.T.home_irpd_today
        : window.T.home_irpd_countdown.replace('{n}', '<span class="irpd-n">' + left + '</span>');
      if (sEl) sEl.textContent = window.T.home_irpd_note.replace('{d}', dStr);
      if (left === 0) ib.classList.add('is-today');
      ib.hidden = false;
    }
  }

  var data = window.TODAY_DATA;
  if (!data) return;
  var T = window.T, loc = window.LOCALE, PAGE = window.PAGE || window.BASE || '';
  var now = dateNow();
  var today = String(now.getMonth() + 1).padStart(2, '0') + '-' + String(now.getDate()).padStart(2, '0');
  var yr = now.getFullYear();
  var md = function (s) { return s && s.length >= 10 ? s.slice(5, 10) : null; };
  /* 中文（繁／簡）都用 p.k：zh-CN 的簡體已在建置時轉好（searchDataFor(locale)） */
  var nameOf = function (p) { return loc === 'ja' ? (p.j || p.n) : loc.indexOf('zh') === 0 ? (p.k || p.n) : p.n; };
  var esc = function (s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  var fill = function (t, n) { return t.replace('{n}', n); };
  var chip = function (p, info) {
    return '<a class="pop inline-flex items-baseline gap-1.5 bg-cream border border-line rounded-full px-3.5 py-1.5 text-[.92rem] no-underline hover:border-amber" href="' + PAGE + 'p/' + (p.u || p.slug) + '/">' +
      '<span class="font-semibold">' + esc(nameOf(p)) + (p.died ? ' ' + T.deceased_mark : '') + '</span>' +
      (info ? '<span class="text-[.82rem] text-ink-soft">' + esc(info) + '</span>' : '') + '</a>';
  };
  var byBorn = function (a, b) { return (a.born || '') < (b.born || '') ? -1 : 1; };
  var bdays = data.pandas.filter(function (p) { return md(p.born) === today; }).sort(byBorn);
  var rainbow = data.pandas.filter(function (p) { return md(p.died) === today; }).sort(byBorn);

  var bHtml = bdays.length ? bdays.map(function (p) {
    // 存疑個體（uv）不寫「滿 n 歲」（那等於宣稱在世），只列出生年
    var info = !p.died && !p.uv ? fill(T.today_turns, yr - (+p.born.slice(0, 4))) : p.born.slice(0, 4);
    return chip(p, info);
  }).join('') : '<p class="text-ink-soft text-[.9rem] m-0">' + T.today_none_birthday + '</p>';

  var rHtml = rainbow.length ? rainbow.map(function (p) {
    return chip(p, fill(T.today_anniversary, yr - (+p.died.slice(0, 4))));
  }).join('') : '<p class="text-ink-soft text-[.9rem] m-0">' + T.today_none_rainbow + '</p>';

  var eb = document.getElementById('today-birthdays'); if (eb) eb.innerHTML = bHtml;
  var er = document.getElementById('today-rainbow'); if (er) er.innerHTML = rHtml;
})();
