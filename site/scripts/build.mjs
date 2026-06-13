#!/usr/bin/env node
/**
 * build.mjs — 小熊貓圖鑑靜態網站生成器（零相依，Node 18+）
 *
 * 用法（在 wiki 根目錄）：
 *   python tools/build_db.py
 *   python site/scripts/export_json.py
 *   node site/scripts/build.mjs        → 輸出 site/dist/
 *
 * 多語系：根目錄為繁中，/ja/、/en/ 為日文與英文版（共用資料與資產）。
 * 為了讓 file:// 直接開啟也能用，搜尋／地圖／家系圖資料全部內嵌進頁面。
 */
import { readFileSync, writeFileSync, mkdirSync, rmSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const SITE = dirname(dirname(fileURLToPath(import.meta.url))); // site/
const DATA = join(SITE, 'data');
const SRC = join(SITE, 'src');
const VENDOR = join(SITE, 'vendor');
const DIST = join(SITE, 'dist');

/* 用 write 取代 copy：部分掛載檔案系統不允許 unlink/override 複製 */
const copyFile = (src, dest) => writeFileSync(dest, readFileSync(src));

const LOCALES = [
  { code: 'zh-TW', htmlLang: 'zh-Hant', dir: '', label: '繁中' },
  { code: 'ja', htmlLang: 'ja', dir: 'ja/', label: '日本語' },
  { code: 'en', htmlLang: 'en', dir: 'en/', label: 'EN' },
];

const { pandas } = JSON.parse(readFileSync(join(DATA, 'pandas.json'), 'utf8'));
const { zoos } = JSON.parse(readFileSync(join(DATA, 'zoos.json'), 'utf8'));
const family = JSON.parse(readFileSync(join(DATA, 'family.json'), 'utf8'));
const BUILD_DATE = new Date().toISOString().slice(0, 10);

const zooById = Object.fromEntries(zoos.map(z => [z.id, z]));
const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const inlineJson = (o) => JSON.stringify(o).replace(/</g, '\\u003c');
const zooName = (id, raw) => id && zooById[id] ? (zooById[id].ja_name || zooById[id].en_name) : (raw || '');

/* ── 衍生資料 ──────────────────────────────────────────── */

for (const p of Object.values(pandas)) {
  const sibs = new Set();
  [p.mother, p.father].filter(Boolean).forEach(par => {
    (pandas[par]?.children || []).forEach(c => { if (c !== p.slug) sibs.add(c); });
  });
  p.full_siblings = []; p.half_siblings = [];
  for (const s of sibs) {
    const q = pandas[s];
    const shareM = p.mother && q.mother === p.mother;
    const shareF = p.father && q.father === p.father;
    if (shareM && shareF) p.full_siblings.push(s);
    else p.half_siblings.push(s);
  }
  const byBorn = (a, b) => (pandas[a].born || '9999') < (pandas[b].born || '9999') ? -1 : 1;
  p.full_siblings.sort(byBorn); p.half_siblings.sort(byBorn);
}

/* 完整家系 graph 與每隻個體的「封閉子圖」（內嵌進個體頁，離線可用） */
const GRAPH = (() => {
  const nodes = {}, up = {}, down = {};
  for (const p of Object.values(pandas)) {
    nodes[p.slug] = [p.name, p.japanese || '', p.sex === 'female' ? 'f' : p.sex === 'male' ? 'm' : 'u',
      p.born ? p.born.slice(0, 4) : '', p.died ? p.died.slice(0, 4) : null];
    if (p.mother || p.father) up[p.slug] = [p.mother, p.father];
    if (p.children.length) down[p.slug] = p.children;
  }
  return { nodes, up, down, twins: family.twins };
})();

function subGraph(slug) {
  const set = new Set([slug]);
  (function anc(s) {
    (GRAPH.up[s] || []).forEach(x => { if (x && !set.has(x)) { set.add(x); anc(x); } });
  })(slug);
  (function desc(s) {
    (GRAPH.down[s] || []).forEach(x => { if (!set.has(x)) { set.add(x); desc(x); } });
  })(slug);
  GRAPH.twins.forEach(([a, b]) => {  // 中心的雙胞胎也要能畫
    if (a === slug && !set.has(b)) set.add(b);
    if (b === slug && !set.has(a)) set.add(a);
  });
  const nodes = {}, up = {}, down = {};
  for (const s of set) {
    nodes[s] = GRAPH.nodes[s];
    if (GRAPH.up[s]) up[s] = GRAPH.up[s].map(x => set.has(x) ? x : null);
    if (GRAPH.down[s]) down[s] = GRAPH.down[s].filter(x => set.has(x));
  }
  return { nodes, up, down, twins: GRAPH.twins.filter(([a, b]) => set.has(a) && set.has(b)) };
}

/* ── 版型 ──────────────────────────────────────────────── */

function layout(ctx, { title, body, active, extraHead = '', extraBody = '' }) {
  const { T, locale, assetBase, pageBase, relPath } = ctx;
  const NAV = [
    ['index.html', T.nav_home],
    ['search.html', T.nav_search],
    ['zoos.html', T.nav_zoos],
  ];
  const langOptions = LOCALES.map(l =>
    `<option value="${l.code}"${l.code === locale.code ? ' selected' : ''}>${l.label}</option>`).join('');
  const langSelect = `<select id="lang-select" class="lang-select" aria-label="Language / 言語 / 語言">${langOptions}</select>`;
  const localeMeta = LOCALES.map(l => ({ code: l.code, dir: l.dir, label: l.label }));
  return `<!doctype html>
<html lang="${locale.htmlLang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)} | ${T.site_title}</title>
<link rel="stylesheet" href="${assetBase}styles.css">
<link rel="manifest" href="${assetBase}manifest.webmanifest">
<link rel="icon" href="${assetBase}icon.svg" type="image/svg+xml">
<meta name="theme-color" content="#b5552d">
${extraHead}
<script>window.SITE_BASE=${JSON.stringify(assetBase)};window.PAGE_BASE=${JSON.stringify(pageBase)};window.T=${inlineJson(T)};window.LOCALE=${JSON.stringify(locale.code)};window.LOCALES=${inlineJson(localeMeta)};window.REL_PATH=${JSON.stringify(relPath)};</script>
<script src="${assetBase}lang.js"></script>
</head>
<body>
<header class="site"><div class="wrap">
  <a class="logo" href="${pageBase}index.html">🐾 ${T.site_title}</a>
  <nav>${NAV.map(([href, label]) =>
    `<a href="${pageBase}${href}"${active === href ? ' class="active"' : ''}>${label}</a>`).join('')}
  ${langSelect}</nav>
</div></header>
<div class="wrap">
${body}
<footer class="site">${T.footer_note}・${T.data_note} ${BUILD_DATE}</footer>
</div>
${extraBody}
<script>if(location.protocol!=='file:'&&'serviceWorker' in navigator)navigator.serviceWorker.register(window.SITE_BASE+'sw.js').catch(()=>{});</script>
</body></html>`;
}

/* ── 個體頁 ────────────────────────────────────────────── */

const link = (ctx, slug) => {
  const q = pandas[slug];
  return q ? `<a href="${ctx.pageBase}p/${slug}.html">${esc(q.name)}${q.died ? ' 🌈' : ''}</a>` : esc(slug);
};

function pandaPage(ctx, p) {
  const { T, pageBase } = ctx;
  const sexTxt = p.sex === 'female' ? T.sex_f : p.sex === 'male' ? T.sex_m : T.sex_unknown;
  const sexCls = p.sex === 'female' ? 'f' : p.sex === 'male' ? 'm' : '';
  const curZoo = !p.died && (p.current_zoo || p.current_zoo_raw)
    ? (p.current_zoo
        ? `<a href="${pageBase}zoos.html#zoo-${p.current_zoo}">${esc(zooName(p.current_zoo, p.current_zoo_raw))}</a>`
        : esc(p.current_zoo_raw))
    : null;

  const facts = [
    [T.field_sex, `<span class="badge ${sexCls}">${sexTxt}</span>`],
    [T.field_born, p.born ? `${esc(p.born)} <span id="age" data-born="${esc(p.born)}" data-died="${esc(p.died || '')}"></span>` : '—'],
    p.died ? [T.field_died, `${esc(p.died)} ${T.deceased_mark}`] : null,
    [T.field_species, `<i>${esc(p.species ? 'Ailurus fulgens ' + p.species : '—')}</i>`],
    curZoo ? [T.field_zoo, curZoo] : null,
    p.rpf_url ? [T.field_rpf, `<a href="${esc(p.rpf_url)}" target="_blank" rel="noopener">#${esc(p.rpf_id)}</a>`] : null,
  ].filter(Boolean);

  const aka = [...(p.nicknames || []), ...(p.english_variants || [])];

  const residences = p.residences.length ? `
<h2>${T.sec_residences}</h2>
<div class="card"><table>
<tr><th>${T.th_period}</th><th>${T.th_zoo}</th></tr>
${p.residences.map(r => `<tr>
  <td>${esc(r.start || '?')}–${esc(r.end || '')}</td>
  <td>${r.zoo_id ? `<a href="${pageBase}zoos.html#zoo-${r.zoo_id}">${esc(zooName(r.zoo_id, r.zoo_raw))}</a>` : esc(r.zoo_raw)}</td>
</tr>`).join('')}
</table></div>` : '';

  const famRow = (label, slugs) => slugs && slugs.length
    ? `<li><span class="rel">${label}</span>${slugs.map(s => link(ctx, s)).join('、')}</li>` : '';
  const childRows = p.children.map(c => {
    const q = pandas[c];
    const other = [q.mother, q.father].filter(s => s && s !== p.slug)[0];
    return `<tr><td>${link(ctx, c)}</td><td>${esc((q.born || '?').slice(0, 4))}</td><td>${other ? link(ctx, other) : '—'}</td></tr>`;
  }).join('');

  const familySec = `
<h2>${T.sec_family}</h2>
<div class="card">
<ul class="family">
${famRow(T.rel_mother, p.mother ? [p.mother] : null)}
${famRow(T.rel_father, p.father ? [p.father] : null)}
${famRow(T.rel_twin, p.twins)}
${famRow(T.rel_siblings, p.full_siblings)}
${famRow(T.rel_half_siblings, p.half_siblings)}
</ul>
${p.children.length ? `<h2 style="margin-top:18px">${T.sec_children}</h2>
<table><tr><th>${T.th_name}</th><th>${T.th_born_year}</th><th>${T.th_other_parent}</th></tr>${childRows}</table>` : ''}
</div>`;

  const hasTree = p.mother || p.father || p.children.length || (p.twins || []).length;
  const treeSec = hasTree ? `
<h2>${T.sec_tree}</h2>
<div class="card">
  <div class="tree-controls">
    <button class="btn ghost" id="tree-up">${T.tree_more_ancestors}</button>
    <button class="btn ghost" id="tree-down">${T.tree_more_descendants}</button>
    <span class="tree-zoom">
      <button class="btn ghost zbtn" id="tree-zoom-out" aria-label="zoom out">−</button>
      <button class="btn ghost zbtn" id="tree-zoom-in" aria-label="zoom in">＋</button>
      <button class="btn ghost zbtn" id="tree-reset" aria-label="reset">⟳</button>
    </span>
  </div>
  <div id="tree-box" data-slug="${esc(p.slug)}"></div>
  <p class="tree-hint">${T.tree_hint}</p>
</div>` : '';

  const body = `
<p style="margin-top:20px"><a href="${pageBase}search.html">${T.back_to_search}</a></p>
<div class="profile-head">
  <h1 style="margin:6px 0">${esc(p.name)}${p.died ? ' 🌈' : ''}</h1>
  ${p.japanese ? `<span class="ja">${esc(p.japanese)}</span>` : ''}
</div>
${aka.length ? `<p class="sub">${esc(aka.join('、'))}</p>` : ''}
<div class="card"><dl class="facts">
${facts.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('')}
</dl></div>
${residences}
${familySec}
${treeSec}`;

  return layout(ctx, {
    title: p.name, body, active: null,
    extraBody: `<script>
(function(){var e=document.getElementById('age');if(!e||!e.dataset.born)return;
var end=e.dataset.died?new Date(e.dataset.died):new Date();
var a=Math.floor((end-new Date(e.dataset.born))/31557600000);
if(a>=0)e.textContent='（'+${inlineJson(T.age_years)}.replace('{n}',a)+'）';})();
</script>${hasTree ? `<script>window.GRAPH_DATA=${inlineJson(subGraph(p.slug))};</script><script src="${ctx.assetBase}tree.js"></script>` : ''}`,
  });
}

/* ── 首頁 / 搜尋 / 動物園 ─────────────────────────────── */

function indexPage(ctx) {
  const { T } = ctx;
  const alive = Object.values(pandas).filter(p => !p.died).length;
  const stats = [
    [Object.keys(pandas).length, T.stat_pandas],
    [alive, T.stat_alive],
    [zoos.length, T.stat_zoos],
    [family.parent_child.length, T.stat_edges],
  ];
  const featured = ['taofa', 'shiryu', 'franken', 'shin-fa', 'ako']
    .filter(s => pandas[s]).map(s => link(ctx, s)).join('、');
  const body = `
<h1>${T.site_title}</h1>
<p class="sub">${T.site_subtitle}</p>
<div class="stats">${stats.map(([n, l]) =>
  `<div class="card stat"><div class="num">${n}</div><div class="lbl">${l}</div></div>`).join('')}</div>
<div class="card">
  <form action="search.html" method="get" style="display:flex;gap:10px;flex-wrap:wrap">
    <input type="search" name="q" placeholder="${T.search_placeholder}" style="flex:1 1 220px;font:inherit;padding:9px 14px;border:1px solid var(--line);border-radius:10px">
    <button class="btn" type="submit">${T.nav_search}</button>
    <a class="btn ghost" href="zoos.html">${T.nav_zoos}</a>
  </form>
</div>
<h2>${T.home_featured}</h2>
<p>${featured}</p>
<p class="sub">${T.home_intro}</p>`;
  return layout(ctx, { title: T.nav_home, body, active: 'index.html' });
}

function searchIndexData() {
  return {
    pandas: Object.values(pandas).map(p => ({
      slug: p.slug, n: p.name, j: p.japanese,
      en: [...(p.english_variants || []), ...(p.nicknames || [])].join('|') || null,
      sex: p.sex, born: p.born, died: p.died,
      zoo: !p.died ? zooName(p.current_zoo, p.current_zoo_raw) || null : null,
    })),
  };
}

function searchPage(ctx, searchData) {
  const { T } = ctx;
  const body = `
<h1>${T.nav_search}</h1>
<div class="filters">
  <input type="search" id="f-q" placeholder="${T.search_placeholder}">
  <select id="f-zoo"><option value="">${T.filter_zoo}：${T.filter_all}</option></select>
  <select id="f-sex">
    <option value="">${T.filter_sex}：${T.filter_all}</option>
    <option value="female">${T.filter_female}</option>
    <option value="male">${T.filter_male}</option>
  </select>
  <label class="chk"><input type="checkbox" id="f-alive">${T.filter_alive_only}</label>
</div>
<p id="result-count"></p>
<div class="grid" id="results"></div>`;
  return layout(ctx, {
    title: T.nav_search, body, active: 'search.html',
    extraBody: `<script>window.SEARCH_DATA=${inlineJson(searchData)};</script><script src="${ctx.assetBase}search.js"></script>`,
  });
}

function zoosPage(ctx) {
  const { T } = ctx;
  const cards = zoos.map(z => {
    const name = z.ja_name || z.en_name;
    const residents = z.residents.map(s => link(ctx, s)).join('、');
    return `<div class="card zoo-card" id="zoo-${z.id}">
  <h3>${esc(name)}</h3>
  <div class="loc">${esc(z.location_ja || z.location_en || z.country || '')}</div>
  <div class="residents"><strong>${T.zoo_residents}（${z.residents.length}）</strong><br>${residents || T.zoo_no_residents}</div>
  <div class="actions">
    ${z.lat ? `<button class="btn ghost" data-zoo-focus="${z.id}">📍</button>` : ''}
    ${z.lat ? `<a class="btn" target="_blank" rel="noopener" href="https://www.google.com/maps/dir/?api=1&destination=${z.lat},${z.lng}">${T.zoo_directions}</a>` : ''}
    ${z.website ? `<a class="btn ghost" target="_blank" rel="noopener" href="${esc(z.website)}">${T.zoo_website}</a>` : ''}
  </div></div>`;
  }).join('');
  const body = `
<h1>${T.nav_zoos}</h1>
<p class="sub">${T.zoos_intro}</p>
<div id="map"><p style="padding:20px;color:var(--ink-soft)">Loading map…</p></div>
<div class="grid" style="margin-top:18px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))">${cards}</div>`;
  return layout(ctx, {
    title: T.nav_zoos, body, active: 'zoos.html',
    extraHead: `<link rel="stylesheet" href="${ctx.assetBase}vendor/leaflet.css">`,
    extraBody: `<script>window.ZOOS_DATA=${inlineJson({ zoos })};</script>` +
      `<script src="${ctx.assetBase}vendor/leaflet.js"></script><script src="${ctx.assetBase}map.js"></script>`,
  });
}

/* ── PWA ───────────────────────────────────────────────── */

const T0 = JSON.parse(readFileSync(join(SRC, 'i18n', 'zh-TW.json'), 'utf8'));
const MANIFEST = {
  name: T0.site_title, short_name: T0.site_title,
  start_url: './index.html', display: 'standalone',
  background_color: '#fdf8f2', theme_color: '#b5552d',
  icons: [{ src: 'icon.svg', sizes: 'any', type: 'image/svg+xml' }],
};

/* ── 輸出 ──────────────────────────────────────────────── */

try {
  rmSync(DIST, { recursive: true, force: true });
} catch { /* 掛載檔案系統可能不允許 unlink，直接覆寫 */ }

const searchData = searchIndexData();
let pageCount = 0;

for (const locale of LOCALES) {
  const T = JSON.parse(readFileSync(join(SRC, 'i18n', `${locale.code}.json`), 'utf8'));
  const localeRoot = join(DIST, ...(locale.dir ? [locale.dir.slice(0, -1)] : []));
  mkdirSync(join(localeRoot, 'p'), { recursive: true });

  const mkCtx = (depth, relPath) => ({
    T, locale,
    assetBase: '../'.repeat(depth + (locale.dir ? 1 : 0)),
    pageBase: '../'.repeat(depth),
    relPath,
  });

  writeFileSync(join(localeRoot, 'index.html'), indexPage(mkCtx(0, 'index.html')));
  writeFileSync(join(localeRoot, 'search.html'), searchPage(mkCtx(0, 'search.html'), searchData));
  writeFileSync(join(localeRoot, 'zoos.html'), zoosPage(mkCtx(0, 'zoos.html')));
  pageCount += 3;
  for (const p of Object.values(pandas)) {
    writeFileSync(join(localeRoot, 'p', `${p.slug}.html`), pandaPage(mkCtx(1, `p/${p.slug}.html`), p));
    pageCount++;
  }
}

mkdirSync(join(DIST, 'data'), { recursive: true });
mkdirSync(join(DIST, 'vendor', 'images'), { recursive: true });
for (const f of ['styles.css', 'search.js', 'map.js', 'tree.js', 'lang.js', 'sw.js', 'icon.svg']) {
  copyFile(join(SRC, f), join(DIST, f));
}
for (const f of readdirSync(VENDOR)) {
  if (f === 'images') continue;
  copyFile(join(VENDOR, f), join(DIST, 'vendor', f));
}
for (const f of readdirSync(join(VENDOR, 'images'))) {
  copyFile(join(VENDOR, 'images', f), join(DIST, 'vendor', 'images', f));
}
writeFileSync(join(DIST, 'manifest.webmanifest'), JSON.stringify(MANIFEST));
/* 仍輸出 data/*.json 供外部工具或未來功能使用 */
writeFileSync(join(DIST, 'data', 'search-index.json'), JSON.stringify(searchData));
writeFileSync(join(DIST, 'data', 'graph.json'), JSON.stringify(GRAPH));
copyFile(join(DATA, 'zoos.json'), join(DIST, 'data', 'zoos.json'));

console.log(`✅ 生成 ${pageCount} 頁（${LOCALES.length} 語系 × ${Object.keys(pandas).length + 3} 頁）→ site/dist/`);
