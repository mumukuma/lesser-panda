/* service worker：同源資源一律「網路優先」，離線時才用快取。
   （先前用快取優先，會導致改了 CSS/JS 卻看到舊版——已改正） */
const VER = 'rpw-v3';

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== VER).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;   // 第三方（favicon、地圖圖磚）交給瀏覽器
  e.respondWith(
    fetch(e.request)
      .then(r => {
        const copy = r.clone();
        caches.open(VER).then(c => c.put(e.request, copy));
        return r;
      })
      .catch(() => caches.match(e.request))      // 離線後備
  );
});
