/* 圖鑑搜尋：前端即時過濾 + 排序 + 分頁（資料由頁面內嵌 window.SEARCH_DATA） */
(function () {
  var $ = function (s) { return document.querySelector(s); };
  var data = window.SEARCH_DATA;
  if (!data) return;
  var pandas = data.pandas, PAGE = window.PAGE || window.BASE || '', loc = window.LOCALE, T = window.T;
  // 已故標記：role=img + aria-label，SR 念「已故」而非「翅膀」（含前導空格）
  var deadMark = ' <span role="img" aria-label="' + (T.deceased || 'deceased') + '">' + (T.deceased_mark || '🪽') + '</span>';
  /* 中文（繁／簡）都用 p.k：zh-CN 的簡體已在建置時轉好（searchDataFor(locale)） */
  var nameOf = function (p) { return loc === 'ja' ? (p.j || p.n) : loc.indexOf('zh') === 0 ? (p.k || p.n) : p.n; };
  // 顯示一個乾淨的副名：主名非英文時顯示英文，否則顯示日文名
  var altOf = function (p) { var pr = nameOf(p); return pr !== p.n ? p.n : (p.j || ''); };
  // 副名若是日文名，於非日文頁需標 lang="ja"，否則漢字會套到中文字形（見 global.css :lang()）
  var altLangAttr = function (p, alt) { return (alt && alt === p.j && loc !== 'ja') ? ' lang="ja"' : ''; };

  // 動物園下拉的選項來源：園名（各語系已解析）依全庫個體數排序。實際要列出哪些園、
  // 各顯示幾隻，改由下方 faceted 計數每次重算（見 refreshFacets）。
  var zooSel = $('#f-zoo');
  var zooCount = {};
  pandas.forEach(function (p) { if (p.zoo) zooCount[p.zoo] = (zooCount[p.zoo] || 0) + 1; });
  var zooNames = Object.keys(zooCount).sort(function (a, b) { return zooCount[b] - zooCount[a]; });

  // 地區下拉：選項與該語系顯示名在建置期算好（searchDataFor 的 regions）；數量同樣改由 faceted 重算
  var regionSel = $('#f-region');
  (data.regions || []).forEach(function (r) {
    var o = document.createElement('option');
    o.value = r.v; o.textContent = r.l;
    regionSel.appendChild(o);
  });

  var sexSel = $('#f-sex'), ageSel = $('#f-age'), dataSel = $('#f-data');
  // 「現存」定義與 #f-alive 一致：未歿且非待查證（動向不明者不宣稱在世）
  var isAlive = function (p) { return !p.died && !p.uv; };
  // 年齡層邊界（含兩端）。選了任一層即隱含現存——已故個體的年齡是享壽、不是現齡，
  // 混在一起會讓「12 歲以上」同時撈出在世高齡與早逝已故者，語意不成立。
  var AGE_BANDS = { baby: [0, 0], '1_3': [1, 3], '4_7': [4, 7], '8_11': [8, 11], senior: [12, 999] };
  function bandOf(p) {
    if (!isAlive(p)) return null;
    var a = ageOf(p);
    if (a === null) return null;              // 無生日者落不進任何層（僅「全部」看得到）
    for (var k in AGE_BANDS) {
      if (a >= AGE_BANDS[k][0] && a <= AGE_BANDS[k][1]) return k;
    }
    return null;
  }
  function inAgeBand(p, band) { return !!band && bandOf(p) === band; }
  var DATA_TESTS = {
    unverified: function (p) { return !!p.uv; },
    no_birthday: function (p) { return !p.born || p.born.length < 10; },
    no_residence: function (p) { return !p.zoo; },
  };

  // ── 狀態與 faceted 計數 ───────────────────────────────────────────────
  // 單一狀態來源：所有條件一次讀齊，結果清單與各下拉的數量都由它衍生。
  // 每顆下拉的數量＝套用「其他所有條件、但不含自己」後的數量，所以數字永遠等於
  // 「點下去會得到幾筆」。少了 except 自己這一步，選了某項後該顆下拉會塌成只剩該項。
  function readState() {
    return {
      q: norm($('#f-q').value), region: regionSel.value, zoo: zooSel.value,
      sex: sexSel.value, age: ageSel.value, data: dataSel.value,
      alive: $('#f-alive').checked, photos: $('#f-photos').checked,
    };
  }
  var TESTS = {
    q: function (p, s) { return !s.q || p._hay.indexOf(s.q) >= 0; },
    region: function (p, s) { return !s.region || p.r === s.region; },
    zoo: function (p, s) { return !s.zoo || p.zoo === s.zoo; },
    sex: function (p, s) { return !s.sex || p.sex === s.sex; },
    age: function (p, s) { return !s.age || inAgeBand(p, s.age); },
    data: function (p, s) { return !s.data || !DATA_TESTS[s.data] || DATA_TESTS[s.data](p); },
    alive: function (p, s) { return !s.alive || isAlive(p); },
    photos: function (p, s) { return !s.photos || p.ph > 0; },
  };
  function matches(p, s, except) {
    for (var k in TESTS) {
      if (k !== except && !TESTS[k](p, s)) return false;
    }
    return true;
  }
  // 每個 facet 的「一隻個體屬於哪些選項」。資料狀態會回傳多個（一隻可能同時缺生日又待查證），
  // 故各選項數量本就會重疊、不該加總；其餘 facet 每隻最多屬於一項。
  var FACET_KEYS = {
    sex: function (p) { return [p.sex]; },
    age: function (p) { var b = bandOf(p); return b ? [b] : []; },
    data: function (p) { var o = []; for (var k in DATA_TESTS) { if (DATA_TESTS[k](p)) o.push(k); } return o; },
    region: function (p) { return p.r ? [p.r] : []; },
    zoo: function (p) { return p.zoo ? [p.zoo] : []; },
  };
  function tally(facet, s) {
    var keys = FACET_KEYS[facet], out = {};
    pandas.forEach(function (p) {
      if (!matches(p, s, facet)) return;
      keys(p).forEach(function (k) { if (k) out[k] = (out[k] || 0) + 1; });
    });
    return out;
  }
  // 短清單（性別／年齡／資料／地區）：選項固定不動，0 就顯示（0）並變灰——「這個條件存在
  // 但現在沒有」本身是資訊。原始標籤存在 _label，避免每次重算把數量疊加上去。
  function paintShort(sel, facet, s) {
    var t = tally(facet, s);
    Array.prototype.forEach.call(sel.options, function (o) {
      if (!o.value) return;
      if (o._label === undefined) o._label = o.textContent.replace(/（\d+）$/, '');
      var c = t[o.value] || 0;
      o.textContent = o._label + '（' + c + '）';
      o.disabled = c === 0 && sel.value !== o.value;
    });
  }
  // 動物園清單有 121 項，太長，故 0 的直接不列（等於把原本的「地區連動篩減」一併涵蓋：
  // 不屬於所選地區的園自然算出 0）。原選的園若歸零就退回「全部」，並回報有無重設。
  function paintZoo(s) {
    var t = tally('zoo', s), keep = zooSel.value, stillThere = false;
    zooSel.length = 1;                     // 留第一個「動物園：全部」
    zooNames.forEach(function (nm) {
      if (!t[nm]) return;
      var o = document.createElement('option');
      o.value = nm; o.textContent = nm + '（' + t[nm] + '）';
      zooSel.appendChild(o);
      if (nm === keep) stillThere = true;
    });
    zooSel.value = stillThere ? keep : '';
    return !stillThere && !!keep;          // true＝剛才那座園被重設了
  }
  function refreshFacets(s) {
    var reset = paintZoo(s);
    if (reset) s = readState();            // 園被重設會改變狀態，其餘 facet 要用新狀態算
    paintShort(sexSel, 'sex', s);
    paintShort(ageSel, 'age', s);
    paintShort(dataSel, 'data', s);
    paintShort(regionSel, 'region', s);
    return s;
  }

  // 羅馬拼音折疊：把 Hepburn↔訓令式的常見差異、以及 L/R 混用折成同一骨架，
  // 讓「Shin-Fa」用 shinfa／sinfa／sin-fa 都搜得到（查詢與索引都套同一折疊，只增命中不漏）。
  var romajiFold = function (s) {
    return s
      .replace(/ー/g, '')          // 日文長音符
      .replace(/sh/g, 's').replace(/sy/g, 's')   // shi/sha ↔ si/sya
      .replace(/ch/g, 't').replace(/ty/g, 't')   // chi/cha ↔ ti/tya
      .replace(/ts/g, 't')                        // tsu ↔ tu
      .replace(/j/g, 'z').replace(/dy/g, 'z')     // ji/ja ↔ zi/zya
      .replace(/f/g, 'h')                          // fu/fa ↔ hu/ha
      .replace(/l/g, 'r').replace(/v/g, 'b')       // L/R、V/B 混用
      .replace(/([aeiou])\1+/g, '$1');            // 疊母音（長音）壓縮 shii→si
  };
  var norm = function (s) { return romajiFold((s || '').toLowerCase().normalize('NFKC').replace(/[\s\-_]/g, '')); };
  pandas.forEach(function (p) { p._hay = norm([p.n, p.j, p.k, p.en, p.slug].filter(Boolean).join('|')); });
  // 曆法歲數（比對月/日，生日當天即滿歲）：不用固定天數除法，避免閏年與時區造成生日當天差 1 歲（同 Panda.astro 作法）
  var ageOf = function (p) {
    if (!p.born) return null;
    var b = p.born.split('-').map(Number);
    var now = new Date();
    var e = p.died ? p.died.split('-').map(Number) : [now.getFullYear(), now.getMonth() + 1, now.getDate()];
    var a = e[0] - b[0];
    if ((e[1] || 1) < (b[1] || 1) || ((e[1] || 1) === (b[1] || 1) && (e[2] || 1) < (b[2] || 1))) a--;
    return a >= 0 ? a : null;
  };
  // 隨機排序：以「種子 + slug」算出穩定亂序鍵，過濾子集合時順序不變；按洗牌鈕換種子。
  var PER = 60, page = 1, seed = (Math.random() * 1e9) | 0;
  function randKey(s, str) { var h = s >>> 0; for (var i = 0; i < str.length; i++) { h = Math.imul(h ^ str.charCodeAt(i), 0x01000193) >>> 0; } return h; }

  function sortList(list) {
    var mode = $('#f-sort').value, arr = list.slice();
    if (mode === 'name') arr.sort(function (a, b) { return nameOf(a).localeCompare(nameOf(b), loc); });
    else if (mode === 'born_new') arr.sort(function (a, b) { return (b.born || '').localeCompare(a.born || ''); });
    else if (mode === 'born_old') arr.sort(function (a, b) { return (a.born || '').localeCompare(b.born || ''); });
    else if (mode === 'photos') arr.sort(function (a, b) { return (b.ph || 0) - (a.ph || 0) || randKey(seed, a.slug) - randKey(seed, b.slug); });
    else if (mode === 'kids') arr.sort(function (a, b) { return (b.kids || 0) - (a.kids || 0) || randKey(seed, a.slug) - randKey(seed, b.slug); });
    else arr.sort(function (a, b) { return randKey(seed, a.slug) - randKey(seed, b.slug); });
    return arr;
  }

  function cardHtml(p) {
    var sexCls = p.sex === 'female' ? 'bg-[#f7e3df] text-female' : p.sex === 'male' ? 'bg-[#dfeef2] text-male' : 'bg-cream text-rust-dark';
    var sexTxt = p.sex === 'female' ? '♀' : p.sex === 'male' ? '♂' : '?';
    var age = ageOf(p);
    // 存疑個體不顯示推算年齡（等同宣稱在世），改標 🚧
    var life = p.died ? ((p.born || '?').slice(0, 4) + '-' + p.died.slice(0, 4) + deadMark)
      : p.uv ? ((p.born || '?').slice(0, 4) + '- 🚧')
      : ((p.born || '?').slice(0, 4) + '-' + (age !== null ? '（' + age + '）' : ''));
    var alt = altOf(p);
    // 蘋果籽佔位（尚未命名的寶寶）：名字旁加 🍎
    var seed = p.ap ? ' <span role="img" title="' + (T.placeholder_badge || '') + '" aria-label="' + (T.placeholder_badge || '') + '">🍎</span>' : '';
    var photoBadge = p.ph ? '<span class="absolute top-2 right-2 inline-flex items-center gap-0.5 bg-cream text-rust rounded-full px-1.5 py-0.5 text-[.7rem] font-medium leading-none" aria-label="' + p.ph + ' ' + (T.sec_photos || '') + '">' +
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3.2"/></svg>' + p.ph + '</span>' : '';
    return '<a class="relative block pop bg-card border border-line rounded-card shadow-card p-[13px_16px] no-underline text-ink hover:border-amber" href="' + PAGE + 'p/' + (p.u || p.slug) + '/">' + photoBadge +
      '<div class="font-bold pr-9">' + nameOf(p) + seed + (alt ? '<span' + altLangAttr(p, alt) + ' class="font-normal text-ink-soft text-[.9em] ml-1.5">' + alt + '</span>' : '') + '</div>' +
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

  // 單一流程：讀狀態 → 重算所有下拉的數量 → 算結果 → 畫。任何條件變動都走同一條路，
  // 不再有「只有某顆下拉會連動」的分歧（舊版只手動接了動物園那顆）。
  function apply(resetPage) {
    if (resetPage !== false) page = 1;
    var s = refreshFacets(readState());
    _sorted = sortList(pandas.filter(function (p) { return matches(p, s, null); }));
    $('#result-count').textContent = T.result_count.replace('{n}', _sorted.length);
    draw();
  }

  ['#f-q', '#f-region', '#f-zoo', '#f-sex', '#f-age', '#f-data', '#f-alive', '#f-photos', '#f-sort']
    .forEach(function (s) { $(s).addEventListener('input', function () { apply(true); }); });
  $('#f-shuffle').addEventListener('click', function () {
    seed = (Math.random() * 1e9) | 0; $('#f-sort').value = 'random'; apply(true);
  });

  var params = new URLSearchParams(location.search);
  if (params.get('q')) $('#f-q').value = params.get('q');
  if (params.get('region')) regionSel.value = params.get('region');
  if (params.get('alive')) $('#f-alive').checked = true;
  if (params.get('photos')) $('#f-photos').checked = true;
  // 動物園選項由 faceted 計數動態產生，第一輪 apply 之後才存在，故 ?zoo= 要在那之後才設得進去
  apply(true);
  if (params.get('zoo')) { zooSel.value = params.get('zoo'); apply(true); }
})();
