/* 首頁「今天的小熊貓」：依使用者當下日期列出今日生日與今日前往小熊星球的個體 */
(function () {
  const data = window.TODAY_DATA;
  if (!data) return;
  const T = window.T, loc = window.LOCALE, PAGE = window.PAGE_BASE ?? '';
  const now = new Date();
  const today = `${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
  const yr = now.getFullYear();
  const md = (s) => (s && s.length >= 10) ? s.slice(5, 10) : null;
  const nameOf = (p) => loc === 'ja' ? (p.j || p.n) : loc === 'zh-TW' ? (p.k || p.n) : p.n;
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const fill = (tpl, n) => tpl.replace('{n}', n);

  const chip = (p, info) =>
    `<a class="today-chip" href="${PAGE}p/${p.slug}.html">` +
    `<span class="nm">${esc(nameOf(p))}${p.died ? ' 🌈' : ''}</span>` +
    (info ? `<span class="info">${esc(info)}</span>` : '') + `</a>`;

  const byBorn = (a, b) => (a.born || '') < (b.born || '') ? -1 : 1;

  const birthdays = data.pandas.filter(p => md(p.born) === today).sort(byBorn);
  const rainbow = data.pandas.filter(p => md(p.died) === today).sort(byBorn);

  const bHtml = birthdays.length
    ? birthdays.map(p => {
        const bornYr = +p.born.slice(0, 4);
        const info = !p.died ? fill(T.today_turns, yr - bornYr) : p.born.slice(0, 4);
        return chip(p, info);
      }).join('')
    : `<p class="today-empty">${T.today_none_birthday}</p>`;

  const rHtml = rainbow.length
    ? rainbow.map(p => chip(p, fill(T.today_anniversary, yr - (+p.died.slice(0, 4))))).join('')
    : `<p class="today-empty">${T.today_none_rainbow}</p>`;

  const elB = document.getElementById('today-birthdays');
  const elR = document.getElementById('today-rainbow');
  if (elB) elB.innerHTML = bHtml;
  if (elR) elR.innerHTML = rHtml;
})();
