/* 日本家系圖：世代分層（每代一條色帶）+ 平移縮放閱讀。
   點個體＝高亮其血脈（祖先＋後代）；動物園下拉＝反白該園成員。
   資料由建置期 japanTreeData(locale) 內嵌於 window.JPTREE_DATA。 */
(function () {
  const D = window.JPTREE_DATA;
  const svg = document.getElementById('ft-svg');
  if (!D || !svg) return;
  const NS = 'http://www.w3.org/2000/svg';
  const T = window.T || {};
  const BASE = window.BASE || '/';
  const PAGE = window.PAGE || BASE;
  const tt = (s, m) => (s || '').replace(/\{(\w+)\}/g, (_, k) => (k in m ? m[k] : '{' + k + '}'));
  // 節點只顯示第一個讀音（如「愛愛, アイアイ」→「愛愛」），與個體頁家系圖一致
  const shortName = (s) => s ? String(s).split(/[,、，/／（(]/)[0].trim() : s;
  // node: [urlId,name,sex,born,died,gen,x,y,zooIds]
  const N = D.nodes, E = D.edges, ROWH = 170, NW = 80, NH = 48;
  const parents = N.map(() => []), children = N.map(() => []);
  E.forEach(([c, p]) => { parents[c].push(p); children[p].push(c); });

  // world bounds
  let minX = 1e9, maxX = -1e9;
  N.forEach((n) => { minX = Math.min(minX, n[6]); maxX = Math.max(maxX, n[6]); });
  const worldL = minX - NW, worldR = maxX + NW, worldW = worldR - worldL;

  const gBands = document.createElementNS(NS, 'g');
  const gEdges = document.createElementNS(NS, 'g');
  const gNodes = document.createElementNS(NS, 'g');
  svg.appendChild(gBands); svg.appendChild(gEdges); svg.appendChild(gNodes);

  // ── generation bands（單一暖色漸層：鏽紅家族，越晚的世代越深）+ 標籤 ──
  // 用同一色相、只調透明度，貼合網站奶油／鏽紅色調；深淺帶出世代進程。
  for (let g = 0; g <= D.maxg; g++) {
    const a = (0.045 + (D.maxg ? g / D.maxg : 0) * 0.11).toFixed(3);
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', worldL); r.setAttribute('width', worldW);
    r.setAttribute('y', g * ROWH - NH / 2 - 24); r.setAttribute('height', ROWH);
    r.setAttribute('fill', `hsl(22 55% 48% / ${a})`);
    gBands.appendChild(r);
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', worldL + 14); t.setAttribute('y', g * ROWH - 30);
    t.setAttribute('class', 'ft-genlbl');
    t.textContent = tt(T.ft_gen || '第 {n} 代', { n: g });
    gBands.appendChild(t);
  }

  // ── edges ──
  const edgeEls = E.map(([c, p]) => {
    const l = document.createElementNS(NS, 'line');
    l.setAttribute('class', 'ft-edge');
    l.setAttribute('x1', N[p][6]); l.setAttribute('y1', N[p][7] + NH / 2);
    l.setAttribute('x2', N[c][6]); l.setAttribute('y2', N[c][7] - NH / 2);
    gEdges.appendChild(l); return l;
  });
  // ── nodes ──
  const nodeEls = N.map((n, i) => {
    const g = document.createElementNS(NS, 'g');
    g.setAttribute('class', 'ft-node ' + (n[4] ? 'dead' : 'alive'));
    g.setAttribute('transform', `translate(${n[6]} ${n[7]})`);
    g.dataset.i = i;
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', -NW / 2); r.setAttribute('y', -NH / 2);
    r.setAttribute('width', NW); r.setAttribute('height', NH); r.setAttribute('rx', 10);
    const t1 = document.createElementNS(NS, 'text');
    t1.setAttribute('text-anchor', 'middle'); t1.setAttribute('y', -3); t1.setAttribute('class', 'ft-nm');
    t1.textContent = shortName(n[1]) + (n[2] === 'm' ? ' ♂' : n[2] === 'f' ? ' ♀' : '');
    const t2 = document.createElementNS(NS, 'text');
    t2.setAttribute('text-anchor', 'middle'); t2.setAttribute('y', 14); t2.setAttribute('class', 'ft-sub');
    t2.textContent = n[3] + (n[4] ? '–' + n[4] : '');
    g.appendChild(r); g.appendChild(t1); g.appendChild(t2);
    gNodes.appendChild(g); return g;
  });

  // ── viewport (viewBox pan/zoom) ──
  let vb = { x: 0, y: 0, w: 1, h: 1 };
  const applyVB = () => svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
  const pxw = () => { const r = svg.getBoundingClientRect(); return [r.width || 1, r.height || 1, r]; };
  function fit() {
    const pad = 90, top = -NH / 2 - 24, bot = D.maxg * ROWH + NH / 2 + 20;
    const [pw, ph] = pxw(); const asp = pw / ph;
    let W = worldW + pad * 2, H = (bot - top) + pad * 2, x = worldL - pad, y = top - pad;
    if (W / H < asp) { const nw = H * asp; x -= (nw - W) / 2; W = nw; }
    else { const nh = W / asp; y -= (nh - H) / 2; H = nh; }
    vb = { x, y, w: W, h: H }; applyVB();
  }
  function zoomAt(sx, sy, f) {
    const [pw, ph, r] = pxw();
    const wx = vb.x + (sx - r.left) / pw * vb.w, wy = vb.y + (sy - r.top) / ph * vb.h;
    const nw = Math.max(300, Math.min(worldW * 3, vb.w * f)), ratio = vb.h / vb.w;
    vb.w = nw; vb.h = nw * ratio;
    vb.x = wx - (sx - r.left) / pw * vb.w; vb.y = wy - (sy - r.top) / ph * vb.h; applyVB();
  }
  function center(i) {
    const n = N[i], cw = Math.min(vb.w, 1500), ratio = vb.h / vb.w;
    vb = { x: n[6] - cw / 2, y: n[7] - cw * ratio / 2, w: cw, h: cw * ratio }; applyVB();
  }
  svg.addEventListener('wheel', (e) => { e.preventDefault(); zoomAt(e.clientX, e.clientY, e.deltaY > 0 ? 1.12 : 0.89); }, { passive: false });
  const pts = new Map(); let last = null, moved = 0, down = null, pinch = 0;
  svg.addEventListener('pointerdown', (e) => {
    svg.setPointerCapture(e.pointerId); pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pts.size === 1) { last = { x: e.clientX, y: e.clientY }; moved = 0; down = e.target.closest('.ft-node'); svg.classList.add('grab'); }
    else if (pts.size === 2) { const a = [...pts.values()]; pinch = Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y); last = null; }
  });
  svg.addEventListener('pointermove', (e) => {
    if (!pts.has(e.pointerId)) return; pts.set(e.pointerId, { x: e.clientX, y: e.clientY }); const [pw, ph] = pxw();
    if (pts.size >= 2) {
      const a = [...pts.values()]; const d = Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y);
      const m = { x: (a[0].x + a[1].x) / 2, y: (a[0].y + a[1].y) / 2 }; if (pinch) zoomAt(m.x, m.y, pinch / d); pinch = d; moved = 99;
    } else if (last) {
      const dx = e.clientX - last.x, dy = e.clientY - last.y; moved += Math.abs(dx) + Math.abs(dy);
      vb.x -= dx * vb.w / pw; vb.y -= dy * vb.h / ph; applyVB(); last = { x: e.clientX, y: e.clientY };
    }
  });
  const up = (e) => {
    pts.delete(e.pointerId); if (pts.size < 2) pinch = 0;
    if (pts.size === 0) { svg.classList.remove('grab'); if (moved < 6 && down) selectNode(+down.dataset.i); else if (moved < 6 && !down) clearSel(); }
  };
  svg.addEventListener('pointerup', up); svg.addEventListener('pointercancel', up);

  // ── selection / highlight ──
  const info = document.getElementById('ft-info');
  let sel = null;
  const walk = (i, list, set) => { const st = [i]; while (st.length) { const x = st.pop(); list[x].forEach((y) => { if (!set.has(y)) { set.add(y); st.push(y); } }); } };
  function applyHi(keep, focus) {
    nodeEls.forEach((g, j) => { g.classList.toggle('faded', !keep.has(j)); g.classList.toggle('hl', j === focus); });
    edgeEls.forEach((l, k) => { const [c, p] = E[k]; const on = keep.has(c) && keep.has(p); l.classList.toggle('faded', !on); l.classList.toggle('on', on && focus != null); });
  }
  function selectNode(i) {
    sel = i; const keep = new Set([i]); walk(i, parents, keep); walk(i, children, keep);
    applyHi(keep, i); const n = N[i];
    const href = PAGE + 'p/' + encodeURIComponent(n[0]) + '/';
    info.style.display = 'block';
    info.innerHTML =
      `<h2>${n[1]}${n[2] === 'm' ? ' ♂' : n[2] === 'f' ? ' ♀' : ''}</h2>` +
      `<div class="row"><span>${T.ft_born_died || '生 / 歿'}</span><b>${n[3] || '?'}${n[4] ? ' – ' + n[4] : ''}</b></div>` +
      `<div class="row"><span>${T.ft_generation || '世代'}</span><b>${tt(T.ft_gen || '第 {n} 代', { n: n[5] })}</b></div>` +
      `<div class="row"><span>${T.ft_relatives || '父母 / 子女'}</span><b>${parents[i].length} / ${children[i].length}</b></div>` +
      `<div class="row"><span>${T.ft_bloodline || '高亮血脈'}</span><b>${keep.size}</b></div>` +
      `<a class="ft-open" href="${href}">${T.ft_open || '前往個體頁 →'}</a>` +
      `<button id="ft-clr">${T.ft_clear || '清除'}</button>`;
    document.getElementById('ft-clr').onclick = clearSel;
    if (document.getElementById('ft-zoo')) document.getElementById('ft-zoo').value = '';
    center(i);
  }
  function highlightZoo(zid) {
    if (!zid) { clearSel(); return; }
    sel = null; info.style.display = 'none';
    const keep = new Set();
    N.forEach((n, j) => { if ((n[8] || []).indexOf(+zid) >= 0) keep.add(j); });
    applyHi(keep, null);
  }
  function clearSel() {
    sel = null; info.style.display = 'none';
    nodeEls.forEach((g) => g.classList.remove('faded', 'hl'));
    edgeEls.forEach((l) => l.classList.remove('faded', 'on'));
    const z = document.getElementById('ft-zoo'); if (z) z.value = '';
  }

  // ── controls ──
  const reset = document.getElementById('ft-reset');
  if (reset) reset.onclick = () => { clearSel(); fit(); };
  const search = document.getElementById('ft-search'), dl = document.getElementById('ft-names');
  if (dl) N.forEach((n) => { const o = document.createElement('option'); o.value = n[1] + (n[3] ? ' (' + n[3] + ')' : ''); dl.appendChild(o); });
  if (search) search.addEventListener('change', (e) => {
    const v = e.target.value.split(' (')[0].trim().toLowerCase();
    const i = N.findIndex((n) => n[1].toLowerCase() === v); if (i >= 0) selectNode(i);
  });
  const zoo = document.getElementById('ft-zoo');
  if (zoo) {
    D.zoos.forEach(([id, name, cnt]) => { const o = document.createElement('option'); o.value = id; o.textContent = `${name} (${cnt})`; zoo.appendChild(o); });
    zoo.addEventListener('change', (e) => highlightZoo(e.target.value));
  }
  const stat = document.getElementById('ft-stat');
  if (stat) stat.textContent = tt(T.ft_stat || '{n} 隻 · {g} 世代 · 在世 {a}',
    { n: N.length, g: D.maxg + 1, a: N.filter((n) => !n[4]).length });

  requestAnimationFrame(fit);
  window.addEventListener('resize', () => { sel !== null ? center(sel) : fit(); });
})();
