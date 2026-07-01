/* 圖鑑搜尋：前端即時過濾 + 排序 + 分頁（資料由頁面內嵌 window.SEARCH_DATA） */
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var data = window.SEARCH_DATA;
  if (!data) return;
  var pandas = data.pandas, PAGE = window.PAGE || window.BASE || '', loc = window.LOCALE, T = window.T;
  var nameOf = function (p) { return loc === 'ja' ? (p.j || p.n) : loc === 'zh-TW' ? (p.k || p.n) : p.n; };
  // 顯示一個乾淨的副名：主名非英文時顯示英文，否則顯示日文名
  var altOf = function (p) { var pr = nameOf(p); return pr !== p.n ? p.n : (p.j || ''); };

  var zooCount = {};
  pandas.forEach(function (p) { if (p.zoo) zooCount[p.zoo] = (zooCount[p.zoo] || 0) + 1; });
  var zooSel = $('#f-zoo');
  Object.entries(zooCount).sort(function (a, b) { return b[1] - a[1]; }).forEach(function (e) {
    var o = document.createElement('option'); o.value = e[0]; o.textContent = e[0] + '（' + e[1] + '）'; zooSel.appendChild(o);
  });

  var norm = function (s) { return (s || '').toLowerCase().normalize('NFKC').replace(/[\s\-_]/g, ''); };
  pandas.forEach(function (p) { p._hay = norm([p.n, p.j, p.k, p.en, p.slug].filter(Boolean).join('|')); });
  var ageOf = function (p) { if (!p.born) return null; var end = p.died ? new Date(p.died) : new Date(); return Math.floor((end - new Date(p.born)) / 31557600000); };

  // 隨機排序：以「種子 + slug」算出穩定亂序鍵，過濾子集合時順序不變；按洗牌鈕換種子。
  var PER = 60, page = 1, seed = (Math.random() * 1e9) | 0;
  function randKey(s, str) { var h = s >>> 0; for (var i = 0; i < str.length; i++) { h = Math.imul(h ^ str.charCodeAt(i), 0x01000193) >>> 0; } return h; }

  function sortList(list) {
    var mode = $('#f-sort').value, arr = list.slice();
    if (mode === 'name') arr.sort(function (a, b) { return nameOf(a).localeCompare(nameOf(b), loc); });
    else if (mode === 'born_new') arr.sort(function (a, b) { return (b.born || '').localeCompare(a.born || ''); });
    else if (mode === 'born_old') arr.sort(function (a, b) { return (a.born || '').localeCompare(b.born || ''); });
    else if (mode === 'photos') arr.sort(function (a, b) { return (b.ph || 0) - (a.ph || 0) || randKey(seed, a.slug) - randKey(seed, b.slug); });
    else arr.sort(function (a, b) { return randKey(seed, a.slug) - randKey(seed, b.slug); });
    return arr;
  }

  function cardHtml(p) {
    var sexCls = p.sex === 'female' ? 'bg-[#f7e3df] text-female' : p.sex === 'male' ? 'bg-[#dfeef2] text-male' : 'bg-cream text-rust-dark';
    var sexTxt = p.sex === 'female' ? '♀' : p.sex === 'male' ? '♂' : '?';
    var age = ageOf(p);
    var life = p.died ? ((p.born || '?').slice(0, 4) + '-' + p.died.slice(0, 4) + ' 🌈')
      : ((p.born || '?').slice(0, 4) + '-' + (age !== null ? '（' + age + '）' : ''));
    var alt = altOf(p);
    var photoBadge = p.ph ? '<span class="absolute top-2 right-2 inline-flex items-center gap-0.5 bg-cream text-rust rounded-full px-1.5 py-0.5 text-[.7rem] font-medium leading-none" aria-label="' + p.ph + ' ' + (T.sec_photos || '') + '">' +
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3.2"/></svg>' + p.ph + '</span>' : '';
    return '<a class="relative block pop bg-card border border-line rounded-card shadow-card p-[13px_16px] no-underline text-ink hover:border-amber" href="' + PAGE + 'p/' + (p.u || p.slug) + '/">' + photoBadge +
      '<div class="font-bold pr-9">' + nameOf(p) + (alt ? '<span class="font-normal text-ink-soft text-[.9em] ml-1.5">' + alt + '</span>' : '') + '</div>' +
      '<div class="text-[.84rem] text-ink-soft mt-0.5"><span class="inline-block text-[.76rem] px-2 py-px rounded-full mr-1.5 ' + sexCls + '">' + sexTxt + '</span>' + life + '</div>' +
      '<div class="text-[.84rem] text-ink-soft">' + (p.zoo || '') + '</div></a>';
  }

  function renderPager(pages) {
    var el = $('#pager');
    if (pages <= 1) { el.innerHTML = ''; return; }
    var btn = function (label, disabled, p) {
      return '<button type="button" data-page="' + p + '"' + (disabled ? ' disabled' : '') +
        ' class="pop bg-card border border-line rounded-full px-3.5 py-1.5 text-[.85rem] ' +
        (disabled ? 'opacity-40 cursor-not-allowed' : 'cursor-pointer hover:border-amber') + '">' + label + '</button>';
    };
    el.innerHTML = btn(T.page_prev, page <= 1, page - 1) +
      '<span class="text-ink-soft text-[.85rem] px-1">' + T.page_info.replace('{c}', page).replace('{t}', pages) + '</span>' +
      btn(T.page_next, page >= pages, page + 1);
    el.querySelectorAll('[data-page]').forEach(function (b) {
      b.addEventListener('click', function () {
        var p = +b.dataset.page; if (p < 1 || p > pages) return;
        page = p; draw(); $('#results').scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  var _sorted = [];
  function draw() {
    var total = _sorted.length, pages = Math.max(1, Math.ceil(total / PER));
    if (page > pages) page = pages;
    $('#results').innerHTML = _sorted.slice((page - 1) * PER, page * PER).map(cardHtml).join('');
    renderPager(pages);
  }

  function apply(resetPage) {
    if (resetPage !== false) page = 1;
    var q = norm($('#f-q').value), zoo = zooSel.value, sex = $('#f-sex').value, aliveOnly = $('#f-alive').checked, photosOnly = $('#f-photos').checked;
    var filtered = pandas.filter(function (p) {
      return (!q || p._hay.indexOf(q) >= 0) && (!zoo || p.zoo === zoo) && (!sex || p.sex === sex) && (!aliveOnly || !p.died) && (!photosOnly || p.ph > 0);
    });
    _sorted = sortList(filtered);
    $('#result-count').textContent = T.result_count.replace('{n}', _sorted.length);
    draw();
  }

  ['#f-q', '#f-zoo', '#f-sex', '#f-alive', '#f-photos', '#f-sort'].forEach(function (s) { $(s).addEventListener('input', function () { apply(true); }); });
  $('#f-shuffle').addEventListener('click', function () {
    seed = (Math.random() * 1e9) | 0; $('#f-sort').value = 'random'; apply(true);
  });

  var params = new URLSearchParams(location.search);
  if (params.get('q')) $('#f-q').value = params.get('q');
  if (params.get('zoo')) zooSel.value = params.get('zoo');
  if (params.get('alive')) $('#f-alive').checked = true;
  if (params.get('photos')) $('#f-photos').checked = true;
  apply(true);
})();
