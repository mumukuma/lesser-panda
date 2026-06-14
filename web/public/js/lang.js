/* 語言：首訪依瀏覽器語言自動導向，手動選擇後記住。URL 由頁面注入的 LANG_URLS 提供。 */
(function () {
  var cur = window.LOCALE, urls = window.LANG_URLS || {}, KEY = 'rpw-lang';
  function fromNavigator() {
    var navs = navigator.languages || [navigator.language || ''];
    for (var i = 0; i < navs.length; i++) {
      var n = String(navs[i]).toLowerCase();
      if (n.indexOf('ja') === 0) return 'ja';
      if (n.indexOf('zh') === 0) return 'zh-TW';
      if (n.indexOf('en') === 0) return 'en';
    }
    return null;
  }
  try {
    var saved = localStorage.getItem(KEY);
    var pref = saved || fromNavigator();
    if (pref && pref !== cur && urls[pref]) { location.replace(urls[pref]); return; }
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
