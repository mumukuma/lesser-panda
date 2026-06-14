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
  function apply(t) {
    d.dataset.theme = t;
    var b = document.getElementById('theme-toggle');
    if (b) b.textContent = t === 'dark' ? '☀️' : '🌙';
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
