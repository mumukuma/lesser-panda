/* 動物園地圖：Leaflet + OpenStreetMap（資料內嵌於頁面，離線/file:// 也能列出卡片） */
(async function () {
  const mapEl = document.getElementById('map');
  if (!mapEl) return;
  const data = window.ZOOS_DATA ||
    await fetch(window.SITE_BASE + 'data/zoos.json').then(r => r.json());
  const zoos = data.zoos.filter(z => z.lat && z.lng);

  if (typeof L === 'undefined') {
    mapEl.innerHTML = '<p style="padding:20px">⚠️ 地圖元件載入失敗（Leaflet 未載入）</p>';
    return;
  }

  mapEl.innerHTML = '';
  const map = L.map('map', { scrollWheelZoom: false });
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,
  }).addTo(map);

  const markerById = {};
  zoos.forEach(z => {
    const name = z.ja_name || z.en_name;
    const m = L.marker([z.lat, z.lng]).addTo(map);
    m.bindPopup(
      `<strong>${name}</strong><br>` +
      `${window.T.zoo_residents}：${z.residents.length}<br>` +
      `<a href="#zoo-${z.id}">↓</a> ・ ` +
      `<a href="https://www.google.com/maps/dir/?api=1&destination=${z.lat},${z.lng}" target="_blank" rel="noopener">${window.T.zoo_directions}</a>`
    );
    markerById[z.id] = { marker: m, zoo: z };
  });
  const all = Object.values(markerById).map(x => x.marker);
  if (all.length) {
    map.fitBounds(L.featureGroup(all).getBounds().pad(0.1));
  } else {
    map.setView([36.2, 138.2], 5);
  }

  // 卡片上的「📍」按鈕：定位到該園並開啟 popup
  document.querySelectorAll('[data-zoo-focus]').forEach(btn => {
    btn.addEventListener('click', () => {
      const hit = markerById[+btn.dataset.zooFocus];
      if (!hit) return;
      map.setView([hit.zoo.lat, hit.zoo.lng], 11);
      hit.marker.openPopup();
      mapEl.scrollIntoView({ behavior: 'smooth' });
    });
  });
})();
