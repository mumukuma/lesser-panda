/* 手機版導覽：漢堡鈕開合下拉選單（桌機維持橫向 pill，不受影響）。
   沿用站上玻璃 header 與 nav-link 樣式，僅切換 #site-nav 的 hidden 狀態。 */
(function () {
  var BARS = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  var CLOSE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('nav-toggle');
    var nav = document.getElementById('site-nav');
    if (!btn || !nav) return;
    function setOpen(open) {
      nav.classList.toggle('hidden', !open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.innerHTML = open ? CLOSE : BARS;
    }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(nav.classList.contains('hidden'));
    });
    // 點選單外或按 Esc 收合
    document.addEventListener('click', function (e) {
      if (!nav.classList.contains('hidden') && !nav.contains(e.target) && !btn.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
    // 放大到桌機尺寸時重置（桌機本就 sm:flex 顯示）
    var mq = matchMedia('(min-width: 640px)');
    (mq.addEventListener ? mq.addEventListener.bind(mq, 'change') : mq.addListener.bind(mq))(function () { setOpen(false); });
  });
})();
