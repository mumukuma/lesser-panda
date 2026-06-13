/* 簡易 service worker：殼層 cache-first、資料 network-first */
const VER = 'rpw-v2';
const SHELL = ['styles.css', 'search.js', 'map.js', 'tree.js', 'icon.svg',
  'vendor/leaflet.js', 'vendor/leaflet.css'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VER).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== VER).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.includes('/data/')) {
    // 資料：先網路、失敗才用快取（離線可看舊資料）
    e.respondWith(fetch(e.request).then(r => {
      const copy = r.clone();
      caches.open(VER).then(c => c.put(e.request, copy));
      return r;
    }).catch(() => caches.match(e.request)));
  } else {
    // 頁面與殼層：先快取、沒有才上網路
    e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
      const copy = r.clone();
      caches.open(VER).then(c => c.put(e.request, copy));
      return r;
    })));
  }
});
