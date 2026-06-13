/* 互動家系圖：以當前個體為中心的 pedigree（上：祖先二元樹；下：後代樹）
   手機友善：viewBox 平移／縮放（單指拖曳、雙指縮放、滾輪縮放），載入時置中於焦點。 */
(async function () {
  const box = document.getElementById('tree-box');
  if (!box) return;
  const CENTER = box.dataset.slug;
  const G = window.GRAPH_DATA ||
    await fetch(window.SITE_BASE + 'data/graph.json').then(r => r.json());
  const PAGE = window.PAGE_BASE ?? window.SITE_BASE;

  const NODE_W = 118, NODE_H = 40, GAP_X = 14, ROW_H = 86;
  const unitW = NODE_W + GAP_X;
  let upDepth = 2, downDepth = 2;

  // 由 render() 設定，供 fitView 使用
  let worldW = 0, worldH = 0, focalX = 0, focalY = 0;
  let vb = { x: 0, y: 0, w: 1, h: 1 };

  const parentsOf = (s) => G.up[s] || [null, null];
  const childrenOf = (s) => G.down[s] || [];
  const maxUp = (s, d = 0) => {
    const [m, f] = parentsOf(s);
    if (d > 8 || (!m && !f)) return d;
    return Math.max(m ? maxUp(m, d + 1) : d, f ? maxUp(f, d + 1) : d);
  };
  const maxDown = (s, d = 0) => {
    const kids = childrenOf(s);
    if (d > 8 || !kids.length) return d;
    return Math.max(...kids.map(k => maxDown(k, d + 1)));
  };
  const isMobile = () => window.matchMedia('(max-width:560px)').matches;
  const pxSize = (svg) => { const r = svg.getBoundingClientRect(); return [r.width || 1, r.height || 1, r]; };
  const applyVB = (svg) => svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);

  function fitView(svg, focusMobile) {
    const [pw, ph] = pxSize(svg);
    const aspect = pw / ph;
    const pad = NODE_W / 2 + 16;
    let W = worldW + pad * 2, H = worldH + pad * 2, x = -pad, y = -pad;
    if (W / H < aspect) { const nW = H * aspect; x -= (nW - W) / 2; W = nW; }
    else { const nH = W / aspect; y -= (nH - H) / 2; H = nH; }
    vb = { x, y, w: W, h: H };
    if (focusMobile && isMobile()) {
      // 手機：放大到約 2.6 個節點寬，置中於焦點個體
      const vw = Math.min(W, unitW * 2.6);
      const vh = vw / aspect;
      vb = { x: focalX - vw / 2, y: focalY - vh / 2, w: vw, h: vh };
    }
    applyVB(svg);
  }

  function zoomAt(screenX, screenY, f, svg) {
    const [pw, ph, r] = pxSize(svg);
    const sx = screenX - r.left, sy = screenY - r.top;
    const wx = vb.x + sx / pw * vb.w, wy = vb.y + sy / ph * vb.h;
    const minW = unitW * 1.2, maxW = (worldW + 200) * 2.2;
    let nw = Math.max(minW, Math.min(maxW, vb.w * f));
    const ratio = vb.h / vb.w;
    vb.w = nw; vb.h = nw * ratio;
    vb.x = wx - sx / pw * vb.w; vb.y = wy - sy / ph * vb.h;
    applyVB(svg);
  }

  function setupViewport(svg) {
    const pts = new Map();
    let dragLast = null, moved = 0, downTarget = null, pinchDist = 0;
    svg.style.touchAction = 'none';
    svg.style.cursor = 'grab';

    svg.addEventListener('pointerdown', (e) => {
      svg.setPointerCapture(e.pointerId);
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (pts.size === 1) {
        dragLast = { x: e.clientX, y: e.clientY }; moved = 0;
        downTarget = e.target.closest('.tree-node');
        svg.style.cursor = 'grabbing';
      } else if (pts.size === 2) {
        const a = [...pts.values()];
        pinchDist = Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y);
        dragLast = null;
      }
    });

    svg.addEventListener('pointermove', (e) => {
      if (!pts.has(e.pointerId)) return;
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      const [pw, ph] = pxSize(svg);
      if (pts.size >= 2) {
        const a = [...pts.values()];
        const dist = Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y);
        const mid = { x: (a[0].x + a[1].x) / 2, y: (a[0].y + a[1].y) / 2 };
        if (pinchDist) zoomAt(mid.x, mid.y, pinchDist / dist, svg);
        pinchDist = dist; moved = 99;
      } else if (dragLast) {
        const dx = e.clientX - dragLast.x, dy = e.clientY - dragLast.y;
        moved += Math.abs(dx) + Math.abs(dy);
        vb.x -= dx * vb.w / pw; vb.y -= dy * vb.h / ph;
        applyVB(svg); dragLast = { x: e.clientX, y: e.clientY };
      }
    });

    const end = (e) => {
      pts.delete(e.pointerId);
      if (pts.size < 2) pinchDist = 0;
      if (pts.size === 0) {
        if (moved < 6 && downTarget) {
          const s = downTarget.dataset.slug;
          if (s !== CENTER) location.href = PAGE + 'p/' + s + '.html';
        }
        dragLast = null; downTarget = null; svg.style.cursor = 'grab';
      } else {
        const o = [...pts.values()][0]; dragLast = { x: o.x, y: o.y };
      }
    };
    svg.addEventListener('pointerup', end);
    svg.addEventListener('pointercancel', end);
    svg.addEventListener('wheel', (e) => {
      e.preventDefault();
      zoomAt(e.clientX, e.clientY, e.deltaY > 0 ? 1.12 : 0.89, svg);
    }, { passive: false });
  }

  function render() {
    const nodes = [];
    const links = [];
    const seenTwin = new Set();

    function leafCount(s, d) {
      const kids = d < downDepth ? childrenOf(s) : [];
      if (!kids.length) return 1;
      return kids.reduce((a, k) => a + leafCount(k, d + 1), 0);
    }
    const centerTwins = G.twins
      .filter(t => t.includes(CENTER))
      .map(t => (t[0] === CENTER ? t[1] : t[0]));
    const descUnits = leafCount(CENTER, 0);
    const ancUnits = Math.pow(2, Math.min(upDepth, maxUp(CENTER)));
    const width = Math.max(descUnits, ancUnits, 2) * unitW + 40 + centerTwins.length * unitW;
    const upRows = Math.min(upDepth, maxUp(CENTER));
    const downRows = Math.min(downDepth, maxDown(CENTER));
    const height = (upRows + downRows + 1) * ROW_H + 30;
    const centerY = upRows * ROW_H + 15;

    const addNode = (slug, x, y) => { nodes.push({ slug, x, y }); return { x, y }; };

    function placeAnc(slug, level, slot, childPos) {
      if (!slug || level > upRows) return;
      const span = width / Math.pow(2, level);
      const x = span * (slot + 0.5);
      const y = centerY - level * ROW_H;
      const pos = addNode(slug, x, y);
      links.push({ x1: x, y1: y + NODE_H / 2, x2: childPos.x, y2: childPos.y - NODE_H / 2 });
      const [m, f] = parentsOf(slug);
      placeAnc(m, level + 1, slot * 2, pos);
      placeAnc(f, level + 1, slot * 2 + 1, pos);
    }

    const centerX = width / 2 - (centerTwins.length * unitW) / 2;
    const centerPos = addNode(CENTER, centerX, centerY);
    centerTwins.forEach((t, i) => {
      const pos = addNode(t, centerX + (i + 1) * unitW, centerY);
      const key = t < CENTER ? t + '|' + CENTER : CENTER + '|' + t;
      seenTwin.add(key);
      links.push({ x1: centerPos.x, y1: centerY, x2: pos.x, y2: centerY, twin: true });
    });

    const [cm, cf] = parentsOf(CENTER);
    if (upRows > 0) { placeAnc(cm, 1, 0, centerPos); placeAnc(cf, 1, 1, centerPos); }

    function placeDesc(slug, depth, left, unitsAvail, parentPos) {
      const x = left + (unitsAvail * unitW) / 2;
      const y = centerY + depth * ROW_H;
      const pos = depth === 0 ? parentPos : addNode(slug, x, y);
      if (depth > 0) links.push({ x1: parentPos.x, y1: parentPos.y + NODE_H / 2, x2: x, y2: y - NODE_H / 2 });
      if (depth >= downDepth) return;
      let cursor = left;
      childrenOf(slug).forEach(k => {
        const u = leafCount(k, depth + 1);
        placeDesc(k, depth + 1, cursor, u, pos);
        cursor += u * unitW;
      });
    }
    placeDesc(CENTER, 0, centerX - (descUnits * unitW) / 2, descUnits, centerPos);

    const bySlug = {};
    nodes.forEach(n => { bySlug[n.slug] = bySlug[n.slug] || n; });
    G.twins.forEach(([a, b]) => {
      const na = bySlug[a], nb = bySlug[b];
      const key = a < b ? a + '|' + b : b + '|' + a;
      if (na && nb && na.y === nb.y && !seenTwin.has(key)) {
        seenTwin.add(key);
        links.push({ x1: na.x, y1: na.y, x2: nb.x, y2: nb.y, twin: true });
      }
    });

    const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
    const linkPath = (l) => l.twin
      ? `M${l.x1},${l.y1} L${l.x2},${l.y2}`
      : `M${l.x1},${l.y1} C${l.x1},${(l.y1 + l.y2) / 2} ${l.x2},${(l.y1 + l.y2) / 2} ${l.x2},${l.y2}`;
    const nodeSvg = (n) => {
      const d = G.nodes[n.slug];
      const cls = `tree-node ${d[2] === 'f' ? 'f' : d[2] === 'm' ? 'm' : ''} ${n.slug === CENTER ? 'center' : ''}`;
      const label = d[0] + (d[4] ? ' 🌈' : '');
      const sub = (d[1] ? d[1] + ' ' : '') + (d[3] ? d[3] : '');
      return `<g class="${cls}" data-slug="${esc(n.slug)}" transform="translate(${n.x - NODE_W / 2},${n.y - NODE_H / 2})">
        <rect width="${NODE_W}" height="${NODE_H}" rx="9"></rect>
        <text x="${NODE_W / 2}" y="16" text-anchor="middle">${esc(label)}</text>
        <text class="sub" x="${NODE_W / 2}" y="31" text-anchor="middle">${esc(sub)}</text></g>`;
    };

    worldW = width; worldH = height; focalX = centerX; focalY = centerY;
    box.innerHTML =
      `<svg preserveAspectRatio="xMidYMid meet" role="img" aria-label="family tree">` +
      links.map(l => `<path class="tree-link ${l.twin ? 'twin' : ''}" d="${linkPath(l)}"></path>`).join('') +
      nodes.map(nodeSvg).join('') + '</svg>';

    const svg = box.querySelector('svg');
    fitView(svg, true);
    setupViewport(svg);
    box._svg = svg;

    const btnUp = document.getElementById('tree-up');
    const btnDown = document.getElementById('tree-down');
    if (btnUp) btnUp.style.display = maxUp(CENTER) > upDepth ? '' : 'none';
    if (btnDown) btnDown.style.display = maxDown(CENTER) > downDepth ? '' : 'none';
  }

  const on = (id, fn) => { const b = document.getElementById(id); if (b) b.addEventListener('click', fn); };
  on('tree-up', () => { upDepth++; render(); });
  on('tree-down', () => { downDepth++; render(); });
  on('tree-zoom-in', () => { const s = box._svg; const r = pxSize(s)[2]; zoomAt(r.left + r.width / 2, r.top + r.height / 2, 0.8, s); });
  on('tree-zoom-out', () => { const s = box._svg; const r = pxSize(s)[2]; zoomAt(r.left + r.width / 2, r.top + r.height / 2, 1.25, s); });
  on('tree-reset', () => fitView(box._svg, true));

  render();
  window.addEventListener('resize', () => { if (box._svg) fitView(box._svg, true); });
})();
