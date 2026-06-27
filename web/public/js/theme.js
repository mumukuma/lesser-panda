/* 深色模式：預設跟隨 OS（prefers-color-scheme），使用者可手動切換並記住。
   在 <head> 同步執行，避免載入閃爍。 */
(function () {
  var KEY = 'rpw-theme', d = document.documentElement;
  function osDark() { return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches; }
  function resolve() {
    var s = null;
    try { s = localStorage.getItem(KEY); } catch (e) {}
    return s || (osDark() ? 'dark' : 'light');   // 無手動偏好 → 跟隨 OS
  }
  var MOON = '<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var SUN = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor" stroke="none"/><path d="M12 2.5v2.2M12 19.3v2.2M21.5 12h-2.2M4.7 12H2.5M18.7 18.7l-1.6-1.6M6.9 6.9 5.3 5.3M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>';
  function apply(t) {
    d.dataset.theme = t;
    var b = document.getElementById('theme-toggle');
    if (b) b.innerHTML = t === 'dark' ? SUN : MOON;
  }
  apply(resolve());
  document.addEventListener('DOMContentLoaded', function () {
    var b = document.getElementById('theme-toggle');
    if (!b) return;
    apply(d.dataset.theme || resolve());
    b.addEventListener('click', function () {
      var next = d.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(KEY, next); } catch (e) {}
      apply(next);
    });
  });
})();
