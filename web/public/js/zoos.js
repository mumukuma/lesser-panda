/* 動物園清單：排序 + 顯示更多（漸進增強：SSR 卡片，JS 重排既有 DOM 節點） */
(function () {
  var grid = document.getElementById('zoo-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.zoo-card'));
  var sortSel = document.getElementById('zoo-sort');
  var moreBtn = document.getElementById('zoo-more');
  if (!cards.length || !sortSel || !moreBtn) return;
  var loc = window.LOCALE, T = window.T || {};
  var LIMIT = 24, expanded = false;

  var count = function (c) { return +c.dataset.count || 0; };
  var name = function (c) { return c.dataset.name || ''; };
  var region = function (c) { return c.dataset.region || ''; };
  var byName = function (a, b) { return name(a).localeCompare(name(b), loc); };

  function render() {
    var mode = sortSel.value, arr = cards.slice();
    if (mode === 'name') arr.sort(byName);
    else if (mode === 'region') arr.sort(function (a, b) { return region(a).localeCompare(region(b), loc) || (count(b) - count(a)); });
    else arr.sort(function (a, b) { return (count(b) - count(a)) || byName(a, b); });
    arr.forEach(function (c, i) { grid.appendChild(c); c.style.display = (expanded || i < LIMIT) ? '' : 'none'; });
    if (cards.length > LIMIT) {
      moreBtn.classList.remove('hidden');
      moreBtn.textContent = expanded ? T.show_less : (T.show_more + '（' + cards.length + '）');
    } else {
      moreBtn.classList.add('hidden');
    }
  }

  sortSel.addEventListener('change', render);
  moreBtn.addEventListener('click', function () {
    expanded = !expanded; render();
    if (!expanded) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // 地圖標記彈窗的「↓」會跳到 #zoo-{id}；若該卡片被收合隱藏，先展開再捲動。
  function jumpToHash() {
    if (!/^#zoo-/.test(location.hash)) return;
    var card = document.getElementById(location.hash.slice(1));
    if (!card) return;
    if (card.style.display === 'none') { expanded = true; render(); }
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
  window.addEventListener('hashchange', jumpToHash);

  render();
  if (location.hash) setTimeout(jumpToHash, 0);
})();
