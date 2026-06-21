/* 資料層：讀取 Python 管線產出的 pipeline/data/*.json 與 i18n，計算衍生資料。
   （與舊 build.mjs 邏輯一致，資料管線完全沿用） */
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

// 路徑相對於 astro build 的 cwd（web/）。CI 與本機皆從 web/ 執行，
// ../pipeline/... 即 repo 的 pipeline 資料夾（Python 管線的輸出）。
const read = (rel) => JSON.parse(readFileSync(resolve(process.cwd(), '..', rel), 'utf8'));

export const pandas = read('pipeline/data/pandas.json').pandas;
export const zoos = read('pipeline/data/zoos.json').zoos;
export const family = read('pipeline/data/family.json');

export const i18n = {
  'zh-TW': read('pipeline/src/i18n/zh-TW.json'),
  ja: read('pipeline/src/i18n/ja.json'),
  en: read('pipeline/src/i18n/en.json'),
};

export const LOCALES = [
  { code: 'zh-TW', htmlLang: 'zh-Hant', dir: '', label: '中文' },
  { code: 'ja', htmlLang: 'ja', dir: 'ja/', label: '日本語' },
  { code: 'en', htmlLang: 'en', dir: 'en/', label: 'EN' },
];

const zooById = Object.fromEntries(zoos.map((z) => [z.id, z]));
// 動物園名依語系：zh＝中文名→日文漢字→英文；ja＝日文→英文；en＝英文→日文
export const zooName = (id, raw, locale = 'zh-TW') => {
  const z = id && zooById[id] ? zooById[id] : null;
  if (!z) return raw || '';
  if (locale === 'ja') return z.ja_name || z.en_name || raw || '';
  if (locale === 'en') return z.en_name || z.ja_name || raw || '';
  return z.name_zh || z.ja_name || z.en_name || raw || '';
};

export const displayName = (p, locale) =>
  locale === 'ja' ? p.japanese || p.name
    : locale === 'zh-TW' ? p.chinese || p.kanji || p.name
    : p.name;

// ── URL id：自 2026-06-18 起 slug 本身已是「名字-生日」(撞名再加媽媽名)，
//    全域唯一且已含生日，故 urlId 直接等於 slug。
//    （舊版在此再接一次 -born，會產生 /p/<name>-<born>-<born>/ 的重複生日失效連結。）──
for (const p of Object.values(pandas)) {
  p.urlId = p.slug;
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
      p.born ? p.born.slice(0, 4) : '', p.died ? p.died.slice(0, 4) : null, p.chinese || p.kanji || '', p.urlId];
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
  // 手足：父母的其他子女（只加節點，不展開其後代）
  (GRAPH.up[slug] || []).filter(Boolean).forEach((par) => {
    (GRAPH.down[par] || []).forEach((sib) => { if (sib !== slug) set.add(sib); });
  });
  const nodes = {}, up = {}, down = {};
  for (const s of set) {
    nodes[s] = GRAPH.nodes[s];
    if (GRAPH.up[s]) up[s] = GRAPH.up[s].map((x) => (set.has(x) ? x : null));
    if (GRAPH.down[s]) down[s] = GRAPH.down[s].filter((x) => set.has(x));
  }
  return { nodes, up, down, twins: GRAPH.twins.filter(([a, b]) => set.has(a) && set.has(b)) };
}

export const searchDataFor = (locale) => ({
  pandas: Object.values(pandas).map((p) => ({
    slug: p.slug, u: p.urlId, n: p.name, j: p.japanese, k: p.chinese || p.kanji,
    en: [...(p.english_variants || []), ...(p.nicknames || [])].join('|') || null,
    sex: p.sex, born: p.born, died: p.died,
    zoo: !p.died ? zooName(p.current_zoo, p.current_zoo_raw, locale) || null : null,
  })),
});
