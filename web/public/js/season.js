/* 四季主題：預設依日期自動（3–5 春、6–8 夏、9–11 秋、12–2 冬），
   可經 header 按鈕手動切換並記住（auto → 春 → 夏 → 秋 → 冬 → auto）。
   與 theme.js 同款做法：在 <head> 同步執行設定 data-season，避免載入閃爍。
   冬季另在 body 動態生成全站飄雪層（reduced-motion 一律不生成）。 */
(function () {
  var KEY = 'rpw-season', d = document.documentElement;
  var SEASONS = ['spring', 'summer', 'autumn', 'winter'];
  var ICONS = { spring: '🌸', summer: '🌻', autumn: '🍂', winter: '❄️' };
  var reduced = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function byDate() {
    var m = new Date().getMonth() + 1;
    return m >= 3 && m <= 5 ? 'spring' : m >= 6 && m <= 8 ? 'summer' : m >= 9 && m <= 11 ? 'autumn' : 'winter';
  }
  function pref() {
    var s = null;
    try { s = localStorage.getItem(KEY); } catch (e) {}
    return SEASONS.indexOf(s) >= 0 ? s : 'auto';
  }
  function label(p, s) {
    var T = window.T || {};
    var names = {
      spring: T.season_spring || 'Spring', summer: T.season_summer || 'Summer',
      autumn: T.season_autumn || 'Autumn', winter: T.season_winter || 'Winter'
    };
    var head = T.season_toggle || 'Season';
    return p === 'auto'
      ? head + ' · ' + (T.season_auto || 'Auto') + '（' + names[s] + '）'
      : head + ' · ' + names[s];
  }

  function updateSnow(s) {
    var box = document.getElementById('snowfall');
    if (s !== 'winter' || reduced) { if (box) box.remove(); return; }
    if (box || !document.body) return;
    box = document.createElement('div');
    box.id = 'snowfall'; box.className = 'snowfall';
    box.setAttribute('aria-hidden', 'true');
    var n = Math.max(18, Math.min(38, Math.round(innerWidth / 14)));
    for (var i = 0; i < n; i++) {
      var f = document.createElement('span');
      f.className = 'snowflake';
      var dur = 9 + Math.random() * 13;
      f.style.cssText =
        '--x:' + (Math.random() * 100).toFixed(1) + '%;' +
        '--sz:' + (3 + Math.random() * 4.5).toFixed(1) + 'px;' +
        '--dur:' + dur.toFixed(1) + 's;' +
        '--delay:-' + (Math.random() * dur).toFixed(1) + 's;' +   /* 負 delay：一載入天空就已有雪 */
        '--sway:' + (Math.random() * 120 - 60).toFixed(0) + 'px;' +
        '--o:' + (0.5 + Math.random() * 0.45).toFixed(2);
      box.appendChild(f);
    }
    document.body.appendChild(box);
  }

  function apply(p) {
    var s = p === 'auto' ? byDate() : p;
    d.dataset.season = s;
    var b = document.getElementById('season-toggle');
    if (b) {
      var span = b.querySelector('span') || b;
      span.textContent = ICONS[s];
      span.style.opacity = p === 'auto' ? '.72' : '1';   /* 自動模式：圖示稍淡作區別 */
      b.title = label(p, s);
      b.setAttribute('aria-label', label(p, s));
    }
    updateSnow(s);
  }

  apply(pref());   /* head 階段：先定 data-season（此時尚無 body，雪層延後） */
  document.addEventListener('DOMContentLoaded', function () {
    apply(pref());
    var b = document.getElementById('season-toggle');
    if (!b) return;
    b.addEventListener('click', function () {
      var order = ['auto'].concat(SEASONS);
      var next = order[(order.indexOf(pref()) + 1) % order.length];
      try { next === 'auto' ? localStorage.removeItem(KEY) : localStorage.setItem(KEY, next); } catch (e) {}
      apply(next);
    });
  });
})();
