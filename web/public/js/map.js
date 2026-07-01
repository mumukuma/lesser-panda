/* 動物園地圖：Leaflet + OpenStreetMap（資料由頁面內嵌 window.ZOOS_DATA） */
(function () {
  var mapEl = document.getElementById('map');
  if (!mapEl) return;
  var data = window.ZOOS_DATA;
  if (!data) return;
  var zoos = data.zoos.filter(function (z) { return z.lat && z.lng; });
  if (typeof L === 'undefined') { mapEl.innerHTML = '<p style="padding:20px">⚠️ ' + ((window.T && window.T.map_load_failed) || '地圖元件載入失敗') + '</p>'; return; }

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
  // 預設以日本群為主：框住日本境內的園（座標落在日本範圍框），不含台灣/海外
  var jp = zoos.filter(function (z) { return z.lat >= 24 && z.lat <= 46 && z.lng >= 128 && z.lng <= 154; });
  var jpBounds = jp.length ? L.latLngBounds(jp.map(function (z) { return [z.lat, z.lng]; })) : null;
  var FIT = { padding: [24, 24], maxZoom: 7 };
  // 框住日本群後再往內縮一級（畫面更聚焦，日本核心置中）
  function fitJp() { map.fitBounds(jpBounds, FIT); map.setZoom(map.getZoom() + 1); }
  if (jpBounds) fitJp(); else map.setView([36.5, 138], 5);

  var refit = function () { map.invalidateSize(); if (jpBounds) fitJp(); };
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
