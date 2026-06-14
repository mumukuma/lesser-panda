/* 動物園地圖：Leaflet + OpenStreetMap（資料由頁面內嵌 window.ZOOS_DATA） */
(function () {
  var mapEl = document.getElementById('map');
  if (!mapEl) return;
  var data = window.ZOOS_DATA;
  if (!data) return;
  var zoos = data.zoos.filter(function (z) { return z.lat && z.lng; });
  if (typeof L === 'undefined') { mapEl.innerHTML = '<p style="padding:20px">⚠️ 地圖元件載入失敗</p>'; return; }

  mapEl.innerHTML = '';
  var map = L.map('map', { scrollWheelZoom: false });
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>', maxZoom: 18,
  }).addTo(map);

  var byId = {};
  var loc = window.LOCALE;
  var zname = function (z) {
    if (loc === 'ja') return z.ja_name || z.en_name;
    if (loc === 'en') return z.en_name || z.ja_name;
    return z.name_zh || z.ja_name || z.en_name;
  };
  zoos.forEach(function (z) {
    var name = zname(z);
    var m = L.marker([z.lat, z.lng]).addTo(map);
    m.bindPopup(
      (z.logo ? '<img src="' + z.logo + '" alt="" style="height:18px;vertical-align:-4px;margin-right:5px" onerror="this.style.display=\'none\'">' : '') +
      '<strong>' + name + '</strong><br>' + window.T.zoo_residents + '：' + z.residents.length + '<br>' +
      '<a href="#zoo-' + z.id + '">↓</a> ・ <a href="https://www.google.com/maps/dir/?api=1&destination=' + z.lat + ',' + z.lng + '" target="_blank" rel="noopener">' + window.T.zoo_directions + '</a>'
    );
    byId[z.id] = { marker: m, zoo: z };
  });
  var all = Object.values(byId).map(function (x) { return x.marker; });
  if (all.length) map.fitBounds(L.featureGroup(all).getBounds().pad(0.1)); else map.setView([36.2, 138.2], 5);

  var refit = function () { map.invalidateSize(); if (all.length) map.fitBounds(L.featureGroup(all).getBounds().pad(0.1)); };
  setTimeout(refit, 200);
  window.addEventListener('load', refit);

  document.querySelectorAll('[data-zoo-focus]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var hit = byId[+btn.dataset.zooFocus]; if (!hit) return;
      map.setView([hit.zoo.lat, hit.zoo.lng], 11); hit.marker.openPopup();
      mapEl.scrollIntoView({ behavior: 'smooth' });
    });
  });
})();
