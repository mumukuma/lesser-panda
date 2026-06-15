/* 捲動淡入：用 IntersectionObserver（非 scroll 監聽），尊重 prefers-reduced-motion。
   附安全網：即使 IO 因環境未觸發，最遲 2.5s 也會顯示全部，內容絕不卡在隱藏。 */
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  function showAll() { for (var i = 0; i < els.length; i++) els[i].classList.add('in'); }
  if (!('IntersectionObserver' in window) ||
      (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    showAll();
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
  setTimeout(showAll, 2500);
})();
