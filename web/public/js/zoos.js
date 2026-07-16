/* 動物園清單：文字過濾 + 排序 + 顯示更多（漸進增強：SSR 卡片，JS 重排既有 DOM 節點） */
(function () {
  var grid = document.getElementById('zoo-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.zoo-card'));
  var sortSel = document.getElementById('zoo-sort');
  var moreBtn = document.getElementById('zoo-more');
  var qInput = document.getElementById('zoo-q');
  var countEl = document.getElementById('zoo-count');
  if (!cards.length || !sortSel || !moreBtn) return;
  var loc = window.LOCALE, T = window.T || {};
  var LIMIT = 24, expanded = false;

  var count = function (c) { return +c.dataset.count || 0; };
  var name = function (c) { return c.dataset.name || ''; };
  var region = function (c) { return c.dataset.region || ''; };
  var byName = function (a, b) { return name(a).localeCompare(name(b), loc); };

  // 過濾索引：data-search（各語園名＋地區）正規化後快取在節點上。
  // 漢字字形折疊：資料的 location_ja 為繁中字形且新舊混雜（縣/県、靜/静…），
  // 折成新字體讓日文使用者打「静岡県」也能命中「靜岡縣」（索引與查詢同折疊，只增命中）。
  var KANJI_FOLD = { 縣: '県', 靜: '静', 兒: '児', 繩: '縄', 廣: '広', 德: '徳', 濱: '浜', 橫: '横', 龍: '竜', 鐵: '鉄' };
  var norm = function (s) {
    return (s || '').toLowerCase().normalize('NFKC')
      .replace(/[縣靜兒繩廣德濱橫龍鐵]/g, function (ch) { return KANJI_FOLD[ch]; })
      .replace(/[\s\-_･・]/g, '');
  };
  cards.forEach(function (c) { c._hay = norm(c.dataset.search || c.dataset.name); });

  function render() {
    var q = norm(qInput ? qInput.value : '');
    var mode = sortSel.value, arr = cards.slice();
    if (mode === 'name') arr.sort(byName);
    else if (mode === 'region') arr.sort(function (a, b) { return region(a).localeCompare(region(b), loc) || (count(b) - count(a)); });
    else arr.sort(function (a, b) { return (count(b) - count(a)) || byName(a, b); });
    var shown = 0;
    arr.forEach(function (c) {
      grid.appendChild(c);
      var hit = !q || c._hay.indexOf(q) >= 0;
      c.style.display = (hit && (expanded || shown < LIMIT)) ? '' : 'none';
      if (hit) shown++;
    });
    if (countEl) {
      countEl.hidden = !q;
      if (q) countEl.textContent = (T.result_count || '{n}').replace('{n}', shown);
    }
    if (shown > LIMIT) {
      moreBtn.classList.remove('hidden');
      moreBtn.textContent = expanded ? T.show_less : (T.show_more + '（' + shown + '）');
    } else {
      moreBtn.classList.add('hidden');
    }
  }

  sortSel.addEventListener('change', render);
  if (qInput) qInput.addEventListener('input', function () { expanded = false; render(); });
  moreBtn.addEventListener('click', function () {
    expanded = !expanded; render();
    if (!expanded) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // 地圖標記彈窗的「↓」會跳到 #zoo-{id}；若該卡片被收合隱藏，先展開再捲動。
  function jumpToHash() {
    if (!/^#zoo-/.test(location.hash)) return;
    var card = document.getElementById(location.hash.slice(1));
    if (!card) return;
    // 被收合或被過濾隱藏時：清掉過濾字串並展開，確保捲得到
    if (card.style.display === 'none') { if (qInput) qInput.value = ''; expanded = true; render(); }
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
  window.addEventListener('hashchange', jumpToHash);

  render();
  if (location.hash) setTimeout(jumpToHash, 0);
})();
