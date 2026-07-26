/* 動物園清單：文字過濾 + 地區過濾 + 排序 + 顯示更多（漸進增強：SSR 卡片，JS 重排既有 DOM 節點） */
/* 註：地區 filter 讀卡片的 data-country（資料正本欄名為 country，UI 標籤刻意寫「地區」，見 data.js） */
(function () {
  var grid = document.getElementById('zoo-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.zoo-card'));
  var sortSel = document.getElementById('zoo-sort');
  var countrySel = document.getElementById('zoo-country');
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
    var cty = countrySel ? countrySel.value : '';   // 小寫英文地區名，空＝全部
    var mode = sortSel.value, arr = cards.slice();
    if (mode === 'name') arr.sort(byName);
    else if (mode === 'region') arr.sort(function (a, b) { return region(a).localeCompare(region(b), loc) || (count(b) - count(a)); });
    else arr.sort(function (a, b) { return (count(b) - count(a)) || byName(a, b); });
    var active = !!q || !!cty;
    var shown = 0, hitIds = [];
    arr.forEach(function (c) {
      grid.appendChild(c);
      var hit = (!q || c._hay.indexOf(q) >= 0) && (!cty || (c.dataset.country || '') === cty);
      c.style.display = (hit && (expanded || shown < LIMIT)) ? '' : 'none';
      if (hit) { shown++; hitIds.push(c.id.replace('zoo-', '')); }
    });
    // 通知地圖跟著 focus（map.js 監聽；也存全域，防 map 較晚初始化時漏接）
    // detail.q＝「是否有任何過濾生效」（文字或國家），map.js 據此決定調暗＋縮放或回日本預設視野
    var detail = { q: active, ids: hitIds };
    window.__ZOO_FILTER = detail;
    document.dispatchEvent(new CustomEvent('zoo-filter', { detail: detail }));
    if (countEl) {
      countEl.hidden = !active;
      if (active) countEl.textContent = (T.result_count || '{n}').replace('{n}', shown);
    }
    if (shown > LIMIT) {
      moreBtn.classList.remove('hidden');
      moreBtn.textContent = expanded ? T.show_less : (T.show_more + '（' + shown + '）');
    } else {
      moreBtn.classList.add('hidden');
    }
  }

  sortSel.addEventListener('change', render);
  if (countrySel) countrySel.addEventListener('change', function () { expanded = false; render(); });
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
    // 被收合或被過濾隱藏時：清掉所有過濾條件並展開，確保捲得到
    if (card.style.display === 'none') {
      if (qInput) qInput.value = '';
      if (countrySel) countrySel.value = '';
      expanded = true; render();
    }
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
  window.addEventListener('hashchange', jumpToHash);

  render();
  if (location.hash) setTimeout(jumpToHash, 0);
})();
