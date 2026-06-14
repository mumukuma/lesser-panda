/* 圖鑑搜尋：前端即時過濾（資料由頁面內嵌 window.SEARCH_DATA） */
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var data = window.SEARCH_DATA;
  if (!data) return;
  var pandas = data.pandas, PAGE = window.PAGE || window.BASE || '', loc = window.LOCALE, T = window.T;
  var nameOf = function (p) { return loc === 'ja' ? (p.j || p.n) : loc === 'zh-TW' ? (p.k || p.n) : p.n; };
  var altOf = function (p) { var pr = nameOf(p); return [p.n, p.j].filter(Boolean).filter(function (x) { return x !== pr; }).filter(function (v, i, a) { return a.indexOf(v) === i; }).join(' · '); };

  var zooCount = {};
  pandas.forEach(function (p) { if (p.zoo) zooCount[p.zoo] = (zooCount[p.zoo] || 0) + 1; });
  var zooSel = $('#f-zoo');
  Object.entries(zooCount).sort(function (a, b) { return b[1] - a[1]; }).forEach(function (e) {
    var o = document.createElement('option'); o.value = e[0]; o.textContent = e[0] + '（' + e[1] + '）'; zooSel.appendChild(o);
  });

  var norm = function (s) { return (s || '').toLowerCase().normalize('NFKC').replace(/[\s\-_]/g, ''); };
  pandas.forEach(function (p) { p._hay = norm([p.n, p.j, p.k, p.en, p.slug].filter(Boolean).join('|')); });
  var ageOf = function (p) { if (!p.born) return null; var end = p.died ? new Date(p.died) : new Date(); return Math.floor((end - new Date(p.born)) / 31557600000); };

  function render(list) {
    $('#result-count').textContent = T.result_count.replace('{n}', list.length);
    $('#results').innerHTML = list.map(function (p) {
      var sexCls = p.sex === 'female' ? 'bg-[#f7e3df] text-female' : p.sex === 'male' ? 'bg-[#dfeef2] text-male' : 'bg-cream text-rust-dark';
      var sexTxt = p.sex === 'female' ? '♀' : p.sex === 'male' ? '♂' : '?';
      var age = ageOf(p);
      var life = p.died ? ((p.born || '?').slice(0, 4) + '–' + p.died.slice(0, 4) + ' 🌈')
        : ((p.born || '?').slice(0, 4) + '–' + (age !== null ? '（' + age + '）' : ''));
      var alt = altOf(p);
      return '<a class="block bg-card border border-line rounded-card shadow-card p-[13px_16px] no-underline text-ink hover:border-amber" href="' + PAGE + 'p/' + p.slug + '/">' +
        '<div class="font-bold">' + nameOf(p) + (alt ? '<span class="font-normal text-ink-soft text-[.9em] ml-1.5">' + alt + '</span>' : '') + '</div>' +
        '<div class="text-[.84rem] text-ink-soft mt-0.5"><span class="inline-block text-[.76rem] px-2 py-px rounded-full mr-1.5 ' + sexCls + '">' + sexTxt + '</span>' + life + '</div>' +
        '<div class="text-[.84rem] text-ink-soft">' + (p.zoo || '') + '</div></a>';
    }).join('');
  }

  function apply() {
    var q = norm($('#f-q').value), zoo = zooSel.value, sex = $('#f-sex').value, aliveOnly = $('#f-alive').checked;
    render(pandas.filter(function (p) {
      return (!q || p._hay.indexOf(q) >= 0) && (!zoo || p.zoo === zoo) && (!sex || p.sex === sex) && (!aliveOnly || !p.died);
    }));
  }
  ['#f-q', '#f-zoo', '#f-sex', '#f-alive'].forEach(function (s) { $(s).addEventListener('input', apply); });
  var params = new URLSearchParams(location.search);
  if (params.get('q')) $('#f-q').value = params.get('q');
  if (params.get('zoo')) zooSel.value = params.get('zoo');
  apply();
})();
