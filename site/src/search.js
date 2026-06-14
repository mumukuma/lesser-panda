/* 圖鑑搜尋：載入 search-index.json 做純前端過濾 */
(async function () {
  const $ = (s) => document.querySelector(s);
  const data = window.SEARCH_DATA ||
    await fetch(window.SITE_BASE + 'data/search-index.json').then(r => r.json());
  const pandas = data.pandas;
  const PAGE = window.PAGE_BASE ?? window.SITE_BASE;
  const loc = window.LOCALE;
  const nameOf = (p) => loc === 'ja' ? (p.j || p.n) : loc === 'zh-TW' ? (p.k || p.n) : p.n;
  const altOf = (p) => {
    const primary = nameOf(p);
    return [...new Set([p.n, p.j].filter(Boolean).filter(x => x !== primary))].join(' · ');
  };

  // 動物園下拉選單（依現居數排序）
  const zooCount = {};
  pandas.forEach(p => { if (p.zoo) zooCount[p.zoo] = (zooCount[p.zoo] || 0) + 1; });
  const zooSel = $('#f-zoo');
  Object.entries(zooCount).sort((a, b) => b[1] - a[1]).forEach(([z, n]) => {
    const o = document.createElement('option');
    o.value = z; o.textContent = `${z}（${n}）`;
    zooSel.appendChild(o);
  });

  const normalize = (s) => (s || '').toLowerCase().normalize('NFKC').replace(/[\s\-_]/g, '');
  pandas.forEach(p => { p._hay = normalize([p.n, p.j, p.en, p.slug].filter(Boolean).join('|')); });

  const ageOf = (p) => {
    if (!p.born) return null;
    const end = p.died ? new Date(p.died) : new Date();
    return Math.floor((end - new Date(p.born)) / 31557600000);
  };

  function render(list) {
    $('#result-count').textContent = window.T.result_count.replace('{n}', list.length);
    $('#results').innerHTML = list.map(p => {
      const sexCls = p.sex === 'female' ? 'f' : p.sex === 'male' ? 'm' : '';
      const sexTxt = p.sex === 'female' ? '♀' : p.sex === 'male' ? '♂' : '?';
      const age = ageOf(p);
      const life = p.died
        ? `${(p.born || '?').slice(0, 4)}–${p.died.slice(0, 4)} ${window.T.deceased_mark}`
        : `${(p.born || '?').slice(0, 4)}–${age !== null ? `（${age} 歲）` : ''}`;
      const alt = altOf(p);
      return `<a class="card panda-card" href="${PAGE}p/${p.slug}.html">
        <div class="nm">${nameOf(p)}${alt ? `<span class="ja">${alt}</span>` : ''}</div>
        <div class="meta"><span class="badge ${sexCls}">${sexTxt}</span>${life}</div>
        <div class="meta">${p.zoo || ''}</div></a>`;
    }).join('');
  }

  function apply() {
    const q = normalize($('#f-q').value);
    const zoo = zooSel.value;
    const sex = $('#f-sex').value;
    const aliveOnly = $('#f-alive').checked;
    render(pandas.filter(p =>
      (!q || p._hay.includes(q)) &&
      (!zoo || p.zoo === zoo) &&
      (!sex || p.sex === sex) &&
      (!aliveOnly || !p.died)
    ));
  }

  ['#f-q', '#f-zoo', '#f-sex', '#f-alive'].forEach(s =>
    $(s).addEventListener('input', apply));

  // 支援 ?q= 與 ?zoo= 進入
  const params = new URLSearchParams(location.search);
  if (params.get('q')) $('#f-q').value = params.get('q');
  if (params.get('zoo')) zooSel.value = params.get('zoo');
  apply();
})();
