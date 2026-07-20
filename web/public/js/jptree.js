/* 日本家系圖：世代分層（每代一條色帶）+ 平移縮放閱讀。
   點個體＝高亮其血脈（祖先＋後代）；動物園下拉＝反白該園成員。
   資料由建置期 japanTreeData(locale) 內嵌於 window.JPTREE_DATA。 */
(function () {
  const D = window.JPTREE_DATA;
  const svg = document.getElementById('ft-svg');
  if (!D || !svg) return;
  const NS = 'http://www.w3.org/2000/svg';
  const T = window.T || {};
  // 整張圖給群組角色與標籤，供螢幕閱讀器辨識
  svg.setAttribute('role', 'group');
  svg.setAttribute('aria-label', T.nav_family || T.tree_aria || 'family tree');
  const BASE = window.BASE || '/';
  const PAGE = window.PAGE || BASE;
  const tt = (s, m) => (s || '').replace(/\{(\w+)\}/g, (_, k) => (k in m ? m[k] : '{' + k + '}'));
  // 節點只顯示第一個讀音（如「愛愛, アイアイ」→「愛愛」），與個體頁家系圖一致
  const shortName = (s) => s ? String(s).split(/[,、，/／（(]/)[0].trim() : s;
  // node: [urlId,name,sex,born,died,gen,x,y,zooIds,placeholder]（placeholder=1：蘋果籽佔位，尚未命名的寶寶）
  const N = D.nodes, E = D.edges, ROWH = 170, NW = 80, NH = 48;
  const parents = N.map(() => []), children = N.map(() => []);
  E.forEach(([c, p]) => { parents[c].push(p); children[p].push(c); });

  // world bounds
  let minX = 1e9, maxX = -1e9;
  N.forEach((n) => { minX = Math.min(minX, n[6]); maxX = Math.max(maxX, n[6]); });
  const worldL = minX - NW, worldR = maxX + NW, worldW = worldR - worldL;

  const gBands = document.createElementNS(NS, 'g');
  gBands.setAttribute('class', 'ft-bands');
  const gEdges = document.createElementNS(NS, 'g');
  const gNodes = document.createElementNS(NS, 'g');
  svg.appendChild(gBands); svg.appendChild(gEdges); svg.appendChild(gNodes);

  // ── generation bands（單一色相漸層：吃當前節氣點綴色 --jq-ac，越晚的世代越深）+ 標籤 ──
  // 同色相只調透明度；色相隨 data-jieqi 變（無 JS 設定時退回預設暖褐，見 global.css :root）。
  for (let g = 0; g <= D.maxg; g++) {
    const a = (0.045 + (D.maxg ? g / D.maxg : 0) * 0.11).toFixed(3);
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', worldL); r.setAttribute('width', worldW);
    r.setAttribute('y', g * ROWH - NH / 2 - 24); r.setAttribute('height', ROWH);
    r.setAttribute('fill', 'var(--jq-ac)');
    r.setAttribute('fill-opacity', a);
    gBands.appendChild(r);
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', worldL + 14); t.setAttribute('y', g * ROWH - 30);
    t.setAttribute('class', 'ft-genlbl');
    t.textContent = tt(T.ft_gen || '第 {n} 代', { n: g });
    gBands.appendChild(t);
  }

  // ── edges（曲線 path，中性色；性別以節點邊框表達，比照個體頁家系圖）──
  const edgeEls = E.map(([c, p]) => {
    const x1 = N[p][6], y1 = N[p][7] + NH / 2, x2 = N[c][6], y2 = N[c][7] - NH / 2, my = (y1 + y2) / 2;
    const el = document.createElementNS(NS, 'path');
    el.setAttribute('class', 'ft-edge');
    el.setAttribute('d', `M${x1} ${y1} C ${x1} ${my} ${x2} ${my} ${x2} ${y2}`);
    gEdges.appendChild(el); return el;
  });
  // ── nodes ──
  const nodeEls = N.map((n, i) => {
    const g = document.createElementNS(NS, 'g');
    g.setAttribute('class', 'ft-node ' + (n[4] ? 'dead' : 'alive') + (n[2] === 'f' ? ' f' : n[2] === 'm' ? ' m' : ''));
    g.setAttribute('transform', `translate(${n[6]} ${n[7]})`);
    g.dataset.i = i;
    // 全圖近 450 個節點：不逐一納入 Tab 序（否則鍵盤使用者要按數百次才能離開圖），
    // 鍵盤操作走上方 #ft-search（可選任一隻並聚焦其血脈）。此處給節點 role+aria-label，
    // 讓螢幕閱讀器瀏覽模式仍能逐一朗讀名字／生卒／已故。
    g.setAttribute('role', 'img');
    g.setAttribute('aria-label', shortName(n[1])
      + (n[3] ? ' ' + n[3] + (n[4] ? '–' + n[4] : '') : '')
      + (n[4] ? '，' + (T.deceased || 'deceased') : ''));
    // 遠景 LOD：畫成小圓點（縮到很小時只顯示點、隱藏方塊與文字）
    const dot = document.createElementNS(NS, 'circle');
    dot.setAttribute('class', 'ft-dot'); dot.setAttribute('r', 17);
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', -NW / 2); r.setAttribute('y', -NH / 2);
    r.setAttribute('width', NW); r.setAttribute('height', NH); r.setAttribute('rx', 10);
    const t1 = document.createElementNS(NS, 'text');
    t1.setAttribute('text-anchor', 'middle'); t1.setAttribute('y', -3); t1.setAttribute('class', 'ft-nm');
    t1.textContent = shortName(n[1]) + (n[2] === 'm' ? ' ♂' : n[2] === 'f' ? ' ♀' : '');
    const t2 = document.createElementNS(NS, 'text');
    t2.setAttribute('text-anchor', 'middle'); t2.setAttribute('y', 14); t2.setAttribute('class', 'ft-sub');
    t2.textContent = n[3] + (n[4] ? '–' + n[4] : '');
    g.appendChild(dot); g.appendChild(r); g.appendChild(t1); g.appendChild(t2);
    // 蘋果籽佔位：節點右上角掛 🍎（尚未命名的寶寶）
    if (n[9]) {
      const seed = document.createElementNS(NS, 'text');
      seed.setAttribute('x', NW / 2 - 2); seed.setAttribute('y', -NH / 2 + 5);
      seed.setAttribute('text-anchor', 'middle');
      seed.setAttribute('font-size', '13');
      seed.textContent = '🍎';
      const tip = document.createElementNS(NS, 'title');
      tip.textContent = T.placeholder_badge || '';
      seed.appendChild(tip);
      g.appendChild(seed);
    }
    gNodes.appendChild(g); return g;
  });

  // ── viewport (viewBox pan/zoom) ──
  let vb = { x: 0, y: 0, w: 1, h: 1 };
  const applyVB = () => { svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`); lod(); };
  const pxw = () => { const r = svg.getBoundingClientRect(); return [r.width || 1, r.height || 1, r]; };
  // 依縮放程度切換細節層級：遠→只圓點、中→只名字、近→名字＋生卒
  function lod() {
    const [pw] = pxw(); const npx = NW * pw / vb.w;
    const cls = npx < 24 ? 'lod-far' : npx < 52 ? 'lod-mid' : 'lod-near';
    if (svg._lod !== cls) { svg.classList.remove('lod-far', 'lod-mid', 'lod-near'); svg.classList.add(cls); svg._lod = cls; }
  }
  function fit() {
    // 全圖很寬（世代少、每代多）：與其塞下全寬留一大片上下空白，
    // 改成「以高度填滿、水平置中」，其餘用平移瀏覽。
    const pad = 40, top = -NH / 2 - 24, bot = D.maxg * ROWH + NH / 2 + 20;
    const [pw, ph] = pxw(); const asp = pw / ph;
    const H = (bot - top) + pad * 2, W = H * asp;
    const cx = (worldL + worldR) / 2;
    vb = { x: cx - W / 2, y: top - pad, w: W, h: H }; applyVB();
  }
  function zoomAt(sx, sy, f) {
    const [pw, ph, r] = pxw();
    const wx = vb.x + (sx - r.left) / pw * vb.w, wy = vb.y + (sy - r.top) / ph * vb.h;
    const nw = Math.max(300, Math.min(worldW * 3, vb.w * f)), ratio = vb.h / vb.w;
    vb.w = nw; vb.h = nw * ratio;
    vb.x = wx - (sx - r.left) / pw * vb.w; vb.y = wy - (sy - r.top) / ph * vb.h; applyVB();
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
    if (pts.size === 0) { svg.classList.remove('grab'); if (moved < 6 && down) { const j = +down.dataset.i; if (picking) { if (j !== cmpA) showCompare(cmpA, j); } else enterFocus(j); } else if (moved < 6 && !down) { const z = document.getElementById('ft-zoo'); if (mode === 'all' && !picking && z && z.value) showAll(); } }
  };
  svg.addEventListener('pointerup', up); svg.addEventListener('pointercancel', up);

  // ── selection / focus（血脈聚焦：抽出祖先＋後代，就地重排成乾淨小樹）──
  const info = document.getElementById('ft-info');
  const stage = svg.closest('.ft-stage');
  // 顯示／隱藏資訊卡（stage 掛 has-info，手機版 CSS 據此隱藏圖例）
  const infoShow = (on) => { info.style.display = on ? 'block' : 'none'; if (stage) stage.classList.toggle('has-info', on); };
  // 手機版資訊卡是底部卡片：回傳其佔用高度(px)，讓 fitBox 把樹排在卡片上方
  const infoInset = () => (window.matchMedia('(max-width: 560px)').matches && info.style.display === 'block')
    ? Math.min(info.offsetHeight + 8, pxw()[1] * 0.5) : 0;
  const coach = document.getElementById('ft-coach');
  const COLW = 150;
  let mode = 'all', focusI = null, picking = false, cmpA = null, cmpPair = null;
  const walk = (i, list, set) => { const st = [i]; while (st.length) { const x = st.pop(); list[x].forEach((y) => { if (!set.has(y)) { set.add(y); st.push(y); } }); } };
  const bloodSet = (i) => { const s = new Set([i]); walk(i, parents, s); walk(i, children, s); return s; };
  const edgePath = (c, p, X, Y) => { const x1 = X(p), y1 = Y(p) + NH / 2, x2 = X(c), y2 = Y(c) - NH / 2, my = (y1 + y2) / 2; return `M${x1} ${y1} C ${x1} ${my} ${x2} ${my} ${x2} ${y2}`; };
  const hideCoach = () => { if (coach) coach.style.display = 'none'; };

  // 只對血脈子集做世代分層 + barycenter 掃描排序，回傳 {i:[x,y]}
  function layoutFocus(set) {
    const rows = {};
    set.forEach((i) => { (rows[N[i][5]] = rows[N[i][5]] || []).push(i); });
    const gs = Object.keys(rows).map(Number).sort((a, b) => a - b), ming = gs[0], order = {};
    gs.forEach((g) => { rows[g].sort((a, b) => N[a][6] - N[b][6]); rows[g].forEach((i, k) => (order[i] = k)); });
    const pin = (i) => parents[i].filter((x) => set.has(x)), cin = (i) => children[i].filter((x) => set.has(x));
    for (let s = 0; s < 6; s++) {
      gs.forEach((g) => { if (g === ming) return; const key = (i) => { const ps = pin(i); return ps.length ? ps.reduce((a, x) => a + order[x], 0) / ps.length : order[i]; }; rows[g].sort((a, b) => key(a) - key(b)); rows[g].forEach((i, k) => (order[i] = k)); });
      [...gs].reverse().forEach((g) => { const key = (i) => { const ks = cin(i); return ks.length ? ks.reduce((a, x) => a + order[x], 0) / ks.length : order[i]; }; rows[g].sort((a, b) => key(a) - key(b)); rows[g].forEach((i, k) => (order[i] = k)); });
    }
    const pos = {};
    gs.forEach((g) => { const w = rows[g].length; rows[g].forEach((i, k) => (pos[i] = [(k - (w - 1) / 2) * COLW, (g - ming) * ROWH])); });
    return pos;
  }
  function fitBox(minx, maxx, miny, maxy, insetB = 0) {
    // insetB：底部被資訊卡遮住的像素高度——內容先塞進可見區（ph-insetB），
    // 再把 viewBox 往下擴到整個 stage，多出的部分藏在卡片後面。
    const pad = 80; const [pw, ph] = pxw();
    const vph = Math.max(120, ph - insetB); const asp = pw / vph;
    let W = (maxx - minx) + pad * 2, H = (maxy - miny) + pad * 2, x = minx - pad, y = miny - pad;
    if (W / H < asp) { const nw = H * asp; x -= (nw - W) / 2; W = nw; }
    else { const nh = W / asp; y -= (nh - H) / 2; H = nh; }
    vb = { x, y, w: W, h: H * ph / vph }; applyVB();
  }
  function enterFocus(i) {
    mode = 'focus'; focusI = i; picking = false; cmpPair = null; hideCoach();
    const set = bloodSet(i), pos = layoutFocus(set);
    const X = (j) => (pos[j] ? pos[j][0] : 0), Y = (j) => (pos[j] ? pos[j][1] : 0);
    let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
    nodeEls.forEach((g, j) => {
      if (set.has(j)) {
        g.classList.remove('ft-hidden', 'faded'); g.classList.toggle('hl', j === i);
        g.setAttribute('transform', `translate(${X(j)} ${Y(j)})`);
        minx = Math.min(minx, X(j)); maxx = Math.max(maxx, X(j)); miny = Math.min(miny, Y(j)); maxy = Math.max(maxy, Y(j));
      } else g.classList.add('ft-hidden');
    });
    edgeEls.forEach((l, k) => { const [c, p] = E[k]; if (set.has(c) && set.has(p)) { l.classList.remove('ft-hidden', 'faded', 'on'); l.setAttribute('d', edgePath(c, p, X, Y)); } else l.classList.add('ft-hidden'); });
    svg.classList.add('focus');
    showCard(i, set.size); // 先渲染卡片才量得到高度（手機版 fitBox 要避開）
    fitBox(minx - NW / 2, maxx + NW / 2, miny - NH / 2, maxy + NH / 2, infoInset());
    const z = document.getElementById('ft-zoo'); if (z) z.value = '';
  }
  function showCard(i, blood) {
    const n = N[i], href = PAGE + 'p/' + encodeURIComponent(n[0]) + '/';
    infoShow(true);
    info.innerHTML =
      `<h2>${n[1]}${n[2] === 'm' ? ' ♂' : n[2] === 'f' ? ' ♀' : ''}</h2>` +
      (n[9] ? `<div class="row"><span>🍎 ${T.placeholder_badge || ''}</span></div>` : '') +
      `<div class="row"><span>${T.ft_born_died || '生 / 歿'}</span><b>${n[3] || '?'}${n[4] ? ' – ' + n[4] : ''}</b></div>` +
      `<div class="row"><span>${T.ft_generation || '世代'}</span><b>${tt(T.ft_gen || '第 {n} 代', { n: n[5] })}</b></div>` +
      `<div class="row"><span>${T.ft_relatives || '父母 / 子女'}</span><b>${parents[i].length} / ${children[i].length}</b></div>` +
      `<div class="row"><span>${T.ft_bloodline || '血脈'}</span><b>${blood}</b></div>` +
      `<a class="ft-open" href="${href}">${T.ft_open || '前往個體頁 →'}</a>` +
      `<button id="ft-all">${T.ft_showall || '看全圖'}</button>` +
      `<button id="ft-cmp">${T.ft_rel_btn || '查兩隻關係'}</button>`;
    document.getElementById('ft-all').onclick = showAll;
    document.getElementById('ft-cmp').onclick = () => startPick(i);
  }

  // ── 兩隻比較（親等計算）：往上 BFS 找最近共同祖先，路徑高亮 ──────────
  // upMap(i)：i 的所有祖先（含自身，深度 0）→ { d: 最短代數, prev: 回溯用（值為靠 i 側的子節點）}
  function upMap(i) {
    const d = { [i]: 0 }, prev = {}, q = [i];
    for (let h = 0; h < q.length; h++) {
      const x = q[h];
      parents[x].forEach((p) => { if (!(p in d)) { d[p] = d[x] + 1; prev[p] = x; q.push(p); } });
    }
    return { d, prev };
  }
  function relLabel(da, db, nFullCA) {
    if (da === 0 || db === 0) {
      const k = da || db;
      return k === 1 ? (T.ft_rel_parent || '親子') : k === 2 ? (T.ft_rel_grand || '祖孫') : (T.ft_rel_line || '直系血親');
    }
    if (da === 1 && db === 1) return nFullCA >= 2 ? (T.ft_rel_sib || '同胞手足') : (T.ft_rel_half || '半手足（½）');
    if ((da === 1 && db === 2) || (da === 2 && db === 1)) return T.ft_rel_auntuncle || '叔伯姑姨／姪甥';
    if (da === 2 && db === 2) return T.ft_rel_cousin || '堂表親';
    return T.ft_rel_far || '遠親';
  }
  function startPick(i) {
    picking = true; cmpA = i; cmpPair = null; mode = 'all';
    restoreAll(); infoShow(false);
    nodeEls[i].classList.add('hl');
    if (coach) {
      coach.querySelector('span').textContent =
        tt(T.ft_rel_pick || '已選 {name}——再點另一隻小熊貓，看牠們的血緣關係', { name: shortName(N[i][1]) });
      coach.style.display = 'flex';
    }
    fit();
  }
  function showCompare(a, b) {
    mode = 'cmp'; cmpPair = [a, b]; picking = false; focusI = null; hideCoach();
    const A = upMap(a), B = upMap(b);
    let best = Infinity, cas = [];
    for (const k in A.d) {
      if (k in B.d) {
        const t = A.d[k] + B.d[k];
        if (t < best) { best = t; cas = [+k]; } else if (t === best) cas.push(+k);
      }
    }
    // 路徑集合＋路徑邊（child,parent 鍵）
    const set = new Set([a, b]), pe = new Set();
    const chain = (m, ca) => { let x = ca; set.add(x); while (m.prev[x] !== undefined) { const c = m.prev[x]; pe.add(c + ',' + x); set.add(c); x = c; } };
    cas.slice(0, 4).forEach((ca) => { chain(A, ca); chain(B, ca); });
    const pos = layoutFocus(set);
    const X = (j) => (pos[j] ? pos[j][0] : 0), Y = (j) => (pos[j] ? pos[j][1] : 0);
    let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
    const caSet = new Set(cas.slice(0, 4));
    nodeEls.forEach((g, j) => {
      if (set.has(j)) {
        g.classList.remove('ft-hidden', 'faded');
        g.classList.toggle('hl', j === a || j === b);
        g.classList.toggle('ca', caSet.has(j) && j !== a && j !== b);
        g.setAttribute('transform', `translate(${X(j)} ${Y(j)})`);
        minx = Math.min(minx, X(j)); maxx = Math.max(maxx, X(j)); miny = Math.min(miny, Y(j)); maxy = Math.max(maxy, Y(j));
      } else { g.classList.add('ft-hidden'); g.classList.remove('ca'); }
    });
    edgeEls.forEach((l, k) => {
      const [c, p] = E[k];
      if (set.has(c) && set.has(p)) {
        l.classList.remove('ft-hidden', 'faded');
        l.classList.toggle('on', pe.has(c + ',' + p));
        l.setAttribute('d', edgePath(c, p, X, Y));
      } else l.classList.add('ft-hidden');
    });
    svg.classList.add('focus');
    showCmpCard(a, b, best, cas, A, B); // 先渲染卡片才量得到高度（手機版 fitBox 要避開）
    fitBox(minx - NW / 2, maxx + NW / 2, miny - NH / 2, maxy + NH / 2, infoInset());
    const z = document.getElementById('ft-zoo'); if (z) z.value = '';
  }
  function showCmpCard(a, b, deg, cas, A, B) {
    const sexMark = (n) => (n[2] === 'm' ? ' ♂' : n[2] === 'f' ? ' ♀' : '');
    let rel, rows = '';
    if (!cas.length) {
      rel = T.ft_rel_none || '無已知血緣（資料範圍內）';
    } else {
      const rep = [...cas].sort((x, y) => Math.max(A.d[x], B.d[x]) - Math.max(A.d[y], B.d[y]))[0];
      const nFull = cas.filter((c) => A.d[c] === 1 && B.d[c] === 1).length;
      rel = relLabel(A.d[rep], B.d[rep], nFull);
      rows = `<div class="row"><span>${T.ft_rel_degree || '親等'}</span><b>${tt(T.ft_rel_deg_n || '第 {n} 親等', { n: deg })}</b></div>`;
      if (!(cas.length === 1 && (cas[0] === a || cas[0] === b))) {
        rows += `<div class="row" style="display:block"><span>${T.ft_rel_ca || '最近共同祖先'}</span><br>` +
          cas.slice(0, 4).map((c) => `<b>${shortName(N[c][1])}</b> <span style="opacity:.7">(${A.d[c]}↔${B.d[c]})</span>`).join('、') +
          (cas.length > 4 ? ` <span style="opacity:.7">+${cas.length - 4}</span>` : '') + `</div>`;
      }
    }
    infoShow(true);
    info.innerHTML =
      `<h2>${shortName(N[a][1])}${sexMark(N[a])} × ${shortName(N[b][1])}${sexMark(N[b])}</h2>` +
      `<div class="row"><span>${T.ft_rel || '關係'}</span><b>${rel}</b></div>` + rows +
      `<button id="ft-all">${T.ft_showall || '看全圖'}</button>` +
      `<button id="ft-repick">${T.ft_rel_again || '換一隻'}</button>`;
    document.getElementById('ft-all').onclick = showAll;
    document.getElementById('ft-repick').onclick = () => startPick(a);
  }
  // 把節點／連線還原到全圖世界座標並顯示全部（不動視角）
  function restoreAll() {
    mode = 'all'; focusI = null; svg.classList.remove('focus');
    nodeEls.forEach((g, j) => { g.classList.remove('ft-hidden', 'hl', 'faded', 'ca'); g.setAttribute('transform', `translate(${N[j][6]} ${N[j][7]})`); });
    edgeEls.forEach((l, k) => { const [c, p] = E[k]; l.classList.remove('ft-hidden', 'on', 'faded'); l.setAttribute('d', edgePath(c, p, (i) => N[i][6], (i) => N[i][7])); });
  }
  function showAll() { picking = false; cmpPair = null; restoreAll(); infoShow(false); const z = document.getElementById('ft-zoo'); if (z) z.value = ''; fit(); }
  function applyFade(keep) {
    nodeEls.forEach((g, j) => g.classList.toggle('faded', !keep.has(j)));
    edgeEls.forEach((l, k) => { const [c, p] = E[k]; l.classList.toggle('faded', !(keep.has(c) && keep.has(p))); });
  }
  function highlightZoo(zid) {
    if (!zid) { showAll(); return; }
    picking = false; cmpPair = null; restoreAll(); infoShow(false); hideCoach();
    const keep = new Set(); N.forEach((n, j) => { if ((n[8] || []).indexOf(+zid) >= 0) keep.add(j); });
    applyFade(keep); fit();
  }

  // ── controls ──
  const reset = document.getElementById('ft-reset');
  if (reset) reset.onclick = showAll;
  const search = document.getElementById('ft-search'), dl = document.getElementById('ft-names');
  if (dl) N.forEach((n) => { const o = document.createElement('option'); o.value = n[1] + (n[3] ? ' (' + n[3] + ')' : ''); dl.appendChild(o); });
  if (search) search.addEventListener('change', (e) => {
    const v = e.target.value.split(' (')[0].trim().toLowerCase();
    const i = N.findIndex((n) => n[1].toLowerCase() === v);
    if (i >= 0) { if (picking && i !== cmpA) showCompare(cmpA, i); else enterFocus(i); }
  });
  const zoo = document.getElementById('ft-zoo');
  if (zoo) {
    D.zoos.forEach(([id, name, cnt]) => { const o = document.createElement('option'); o.value = id; o.textContent = `${name} (${cnt})`; zoo.appendChild(o); });
    zoo.addEventListener('change', (e) => highlightZoo(e.target.value));
  }
  const coachX = document.getElementById('ft-coach-x');
  if (coachX) coachX.onclick = () => { hideCoach(); picking = false; };
  const stat = document.getElementById('ft-stat');
  if (stat) stat.textContent = tt(T.ft_stat || '{n} 隻 · {g} 世代 · 在世 {a}',
    { n: N.length, g: D.maxg + 1, a: N.filter((n) => !n[4]).length });

  requestAnimationFrame(fit);
  window.addEventListener('resize', () => {
    if (mode === 'cmp' && cmpPair) showCompare(cmpPair[0], cmpPair[1]);
    else if (mode === 'focus' && focusI != null) enterFocus(focusI);
    else fit();
  });
})();
