/* 語言選擇：首訪依瀏覽器語言自動導向，使用者手動選擇後記住偏好。
   在 <head> 同步執行，盡早完成導向以減少閃爍。 */
(function () {
  var L = window.LOCALES || [];
  var cur = window.LOCALE;
  var rel = window.REL_PATH || '';
  var base = window.SITE_BASE || '';
  var KEY = 'rpw-lang';

  function has(code) { return L.some(function (x) { return x.code === code; }); }
  function urlFor(code) {
    var l = L.filter(function (x) { return x.code === code; })[0];
    return base + (l ? l.dir : '') + rel;
  }
  function fromNavigator() {
    var navs = navigator.languages || [navigator.language || ''];
    for (var i = 0; i < navs.length; i++) {
      var n = String(navs[i]).toLowerCase();
      if (n.indexOf('ja') === 0) return 'ja';
      if (n.indexOf('zh') === 0) return 'zh-TW';   // 含 zh-CN/zh-HK，皆導向繁中版
      if (n.indexOf('en') === 0) return 'en';
    }
    return null;
  }

  // ── 首訪自動導向 ──
  try {
    var saved = localStorage.getItem(KEY);
    var pref = saved || fromNavigator();
    if (pref && pref !== cur && has(pref)) {
      // 目標頁的 LOCALE 會等於 pref，不會再次觸發，無迴圈風險
      location.replace(urlFor(pref));
      return;
    }
  } catch (e) { /* localStorage 不可用時略過自動導向 */ }

  // ── 下拉選單：手動切換並記住 ──
  document.addEventListener('DOMContentLoaded', function () {
    var sel = document.getElementById('lang-select');
    if (!sel) return;
    sel.value = cur;
    sel.addEventListener('change', function () {
      try { localStorage.setItem(KEY, sel.value); } catch (e) {}
      location.href = urlFor(sel.value);
    });
  });
})();
