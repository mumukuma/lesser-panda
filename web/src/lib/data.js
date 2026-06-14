/* 資料層：讀取 Python 管線產出的 site/data/*.json 與 i18n，計算衍生資料。
   （與舊 build.mjs 邏輯一致，資料管線完全沿用） */
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// 路徑相對於 astro build 的 cwd（web/）。CI 與本機皆從 web/ 執行，
// ../site/... 即 repo 的 site 資料夾（Python 管線的輸出）。
const read = (rel) => JSON.parse(readFileSync(resolve(process.cwd(), '..', rel), 'utf8'));

export const pandas = read('site/data/pandas.json').pandas;
export const zoos = read('site/data/zoos.json').zoos;
export const family = read('site/data/family.json');

export const i18n = {
  'zh-TW': read('site/src/i18n/zh-TW.json'),
  ja: read('site/src/i18n/ja.json'),
  en: read('site/src/i18n/en.json'),
};

export const LOCALES = [
  { code: 'zh-TW', htmlLang: 'zh-Hant', dir: '', label: '繁中' },
  { code: 'ja', htmlLang: 'ja', dir: 'ja/', label: '日本語' },
  { code: 'en', htmlLang: 'en', dir: 'en/', label: 'EN' },
];

const zooById = Object.fromEntries(zoos.map((z) => [z.id, z]));
export const zooName = (id, raw) =>
  id && zooById[id] ? zooById[id].ja_name || zooById[id].en_name : raw || '';

export const displayName = (p, locale) =>
  locale === 'ja' ? p.japanese || p.name
    : locale === 'zh-TW' ? p.kanji || p.name
    : p.name;

// ── URL id：slug + 生日（同名也能區分）；slug 仍為資料主鍵 ──────
for (const p of Object.values(pandas)) {
  p.urlId = p.born ? `${p.slug}-${p.born}` : p.slug;
}

// ── 兄弟姊妹（全血／半血）─────────────────────────────
for (const p of Object.values(pandas)) {
  const sibs = new Set();
  [p.mother, p.father].filter(Boolean).forEach((par) => {
    (pandas[par]?.children || []).forEach((c) => { if (c !== p.slug) sibs.add(c); });
  });
  p.full_siblings = []; p.half_siblings = [];
  for (const s of sibs) {
    const q = pandas[s];
    const shareM = p.mother && q.mother === p.mother;
    const shareF = p.father && q.father === p.father;
    (shareM && shareF ? p.full_siblings : p.half_siblings).push(s);
  }
  const byBorn = (a, b) => ((pandas[a].born || '9999') < (pandas[b].born || '9999') ? -1 : 1);
  p.full_siblings.sort(byBorn); p.half_siblings.sort(byBorn);
}

// ── 完整家系 graph + 每隻的封閉子圖 ──────────────────
const GRAPH = (() => {
  const nodes = {}, up = {}, down = {};
  for (const p of Object.values(pandas)) {
    nodes[p.slug] = [p.name, p.japanese || '', p.sex === 'female' ? 'f' : p.sex === 'male' ? 'm' : 'u',
      p.born ? p.born.slice(0, 4) : '', p.died ? p.died.slice(0, 4) : null, p.kanji || '', p.urlId];
    if (p.mother || p.father) up[p.slug] = [p.mother, p.father];
    if (p.children.length) down[p.slug] = p.children;
  }
  return { nodes, up, down, twins: family.twins };
})();

export function subGraph(slug) {
  const set = new Set([slug]);
  (function anc(s) { (GRAPH.up[s] || []).forEach((x) => { if (x && !set.has(x)) { set.add(x); anc(x); } }); })(slug);
  (function desc(s) { (GRAPH.down[s] || []).forEach((x) => { if (!set.has(x)) { set.add(x); desc(x); } }); })(slug);
  GRAPH.twins.forEach(([a, b]) => {
    if (a === slug && !set.has(b)) set.add(b);
    if (b === slug && !set.has(a)) set.add(a);
  });
  const nodes = {}, up = {}, down = {};
  for (const s of set) {
    nodes[s] = GRAPH.nodes[s];
    if (GRAPH.up[s]) up[s] = GRAPH.up[s].map((x) => (set.has(x) ? x : null));
    if (GRAPH.down[s]) down[s] = GRAPH.down[s].filter((x) => set.has(x));
  }
  return { nodes, up, down, twins: GRAPH.twins.filter(([a, b]) => set.has(a) && set.has(b)) };
}

export const searchData = {
  pandas: Object.values(pandas).map((p) => ({
    slug: p.slug, u: p.urlId, n: p.name, j: p.japanese, k: p.kanji,
    en: [...(p.english_variants || []), ...(p.nicknames || [])].join('|') || null,
    sex: p.sex, born: p.born, died: p.died,
    zoo: !p.died ? zooName(p.current_zoo, p.current_zoo_raw) || null : null,
  })),
};
