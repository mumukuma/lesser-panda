/* 首頁「今天的小熊貓」：依使用者當下日期列出今日生日與今日前往小熊星球 */
(function () {
  var data = window.TODAY_DATA;
  if (!data) return;
  var T = window.T, loc = window.LOCALE, PAGE = window.PAGE || window.BASE || '';
  var now = new Date();
  var today = String(now.getMonth() + 1).padStart(2, '0') + '-' + String(now.getDate()).padStart(2, '0');
  var yr = now.getFullYear();
  var md = function (s) { return s && s.length >= 10 ? s.slice(5, 10) : null; };
  var nameOf = function (p) { return loc === 'ja' ? (p.j || p.n) : loc === 'zh-TW' ? (p.k || p.n) : p.n; };
  var esc = function (s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  var fill = function (t, n) { return t.replace('{n}', n); };
  var chip = function (p, info) {
    return '<a class="inline-flex items-baseline gap-1.5 bg-cream border border-line rounded-full px-3.5 py-1.5 text-[.92rem] no-underline hover:border-amber" href="' + PAGE + 'p/' + (p.u || p.slug) + '/">' +
      '<span class="font-semibold">' + esc(nameOf(p)) + (p.died ? ' 🌈' : '') + '</span>' +
      (info ? '<span class="text-[.82rem] text-ink-soft">' + esc(info) + '</span>' : '') + '</a>';
  };
  var byBorn = function (a, b) { return (a.born || '') < (b.born || '') ? -1 : 1; };
  var bdays = data.pandas.filter(function (p) { return md(p.born) === today; }).sort(byBorn);
  var rainbow = data.pandas.filter(function (p) { return md(p.died) === today; }).sort(byBorn);

  var bHtml = bdays.length ? bdays.map(function (p) {
    var info = !p.died ? fill(T.today_turns, yr - (+p.born.slice(0, 4))) : p.born.slice(0, 4);
    return chip(p, info);
  }).join('') : '<p class="text-ink-soft text-[.9rem] m-0">' + T.today_none_birthday + '</p>';

  var rHtml = rainbow.length ? rainbow.map(function (p) {
    return chip(p, fill(T.today_anniversary, yr - (+p.died.slice(0, 4))));
  }).join('') : '<p class="text-ink-soft text-[.9rem] m-0">' + T.today_none_rainbow + '</p>';

  var eb = document.getElementById('today-birthdays'); if (eb) eb.innerHTML = bHtml;
  var er = document.getElementById('today-rainbow'); if (er) er.innerHTML = rHtml;
})();
