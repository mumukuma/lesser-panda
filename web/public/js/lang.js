/* 語言優先序：手動選擇（localStorage）> IP 國家（geo API，快取 7 天）> 瀏覽器語言。
   國家對應：JP→ja、TW/HK/MO→zh-TW、KR→ko、其他→en；geo 查詢失敗才 fallback 瀏覽器語言。
   URL 由頁面注入的 LANG_URLS 提供。 */
(function () {
  var cur = window.LOCALE, urls = window.LANG_URLS || {};
  var KEY = 'rpw-lang', GEO_KEY = 'rpw-geo', GEO_TTL = 7 * 24 * 60 * 60 * 1000;

  function localeFromCountry(c) {
    c = String(c || '').toUpperCase();
    if (c === 'JP') return 'ja';
    if (c === 'TW' || c === 'HK' || c === 'MO') return 'zh-TW';
    if (c === 'KR') return 'ko';
    return c ? 'en' : null;
  }
  function fromNavigator() {
    var navs = navigator.languages || [navigator.language || ''];
    for (var i = 0; i < navs.length; i++) {
      var n = String(navs[i]).toLowerCase();
      if (n.indexOf('ja') === 0) return 'ja';
      if (n.indexOf('zh') === 0) return 'zh-TW';
      if (n.indexOf('ko') === 0) return 'ko';
      if (n.indexOf('en') === 0) return 'en';
    }
    return null;
  }
  function go(pref) {
    if (pref && pref !== cur && urls[pref]) { location.replace(urls[pref]); return true; }
    return false;
  }
  function cachedCountry() {
    try {
      var o = JSON.parse(localStorage.getItem(GEO_KEY));
      if (o && o.c && Date.now() - o.t < GEO_TTL) return o.c;
    } catch (e) {}
    return null;
  }
  function saveCountry(c) {
    try { localStorage.setItem(GEO_KEY, JSON.stringify({ c: c, t: Date.now() })); } catch (e) {}
  }
  /* 免費 geo API：主 country.is、備援 geojs.io；2.5 秒沒回應就放棄改用瀏覽器語言 */
  function fetchCountry(cb) {
    var done = false;
    var timer = setTimeout(function () { finish(null); }, 2500);
    function finish(c) {
      if (done) return;
      done = true; clearTimeout(timer); cb(c);
    }
    function pick(d) { return (d && typeof d.country === 'string' && d.country) || null; }
    fetch('https://api.country.is/')
      .then(function (r) { return r.json(); })
      .then(function (d) { finish(pick(d)); })
      .catch(function () {
        fetch('https://get.geojs.io/v1/ip/country.json')
          .then(function (r) { return r.json(); })
          .then(function (d) { finish(pick(d)); })
          .catch(function () { finish(null); });
      });
  }

  try {
    var saved = localStorage.getItem(KEY);
    if (saved) {
      go(saved); /* 手動選過 → 一律以它為準，不再看 IP／瀏覽器 */
    } else {
      var c = cachedCountry();
      if (c) {
        go(localeFromCountry(c));
      } else if (window.fetch) {
        fetchCountry(function (c2) {
          if (c2) { saveCountry(c2); go(localeFromCountry(c2)); }
          else go(fromNavigator());
        });
      } else {
        go(fromNavigator());
      }
    }
  } catch (e) {}

  document.addEventListener('DOMContentLoaded', function () {
    var sel = document.getElementById('lang-select');
    if (!sel) return;
    sel.value = cur;
    sel.addEventListener('change', function () {
      try { localStorage.setItem(KEY, sel.value); } catch (e) {}
      if (urls[sel.value]) location.href = urls[sel.value];
    });
  });
})();
