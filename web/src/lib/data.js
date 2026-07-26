/* 資料層：讀取 Python 管線產出的 pipeline/data/*.json 與 i18n，計算衍生資料。
   （與舊 build.mjs 邏輯一致，資料管線完全沿用） */
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import * as OpenCC from 'opencc-js';

// 繁→簡轉換（zh-CN 語系用）：資料正本一律存繁體，簡體僅為建置時的顯示轉換。
// 繁→簡幾乎一對一，方向安全；名字裡的日文假名／拉丁字母不受影響。
const toHans = OpenCC.Converter({ from: 't', to: 'cn' });

// 路徑相對於 astro build 的 cwd（web/）。CI 與本機皆從 web/ 執行，
// ../pipeline/... 即 repo 的 pipeline 資料夾（Python 管線的輸出）。
const read = (rel) => JSON.parse(readFileSync(resolve(process.cwd(), '..', rel), 'utf8'));

export const pandas = read('pipeline/data/pandas.json').pandas;
export const zoos = read('pipeline/data/zoos.json').zoos;
export const family = read('pipeline/data/family.json');

// 致謝名單：作者維護的 data/contributors.json（非衍生資料，直接讀 repo 根的 data/）
export const contributors = read('data/contributors.json').contributors || [];

export const i18n = {
  'zh-TW': read('pipeline/src/i18n/zh-TW.json'),
  'zh-CN': read('pipeline/src/i18n/zh-CN.json'),
  ja: read('pipeline/src/i18n/ja.json'),
  en: read('pipeline/src/i18n/en.json'),
  ko: read('pipeline/src/i18n/ko.json'),
};

export const LOCALES = [
  { code: 'zh-TW', htmlLang: 'zh-Hant', dir: '', label: '中文' },
  { code: 'zh-CN', htmlLang: 'zh-Hans', dir: 'zh-CN/', label: '简体' },
  { code: 'ja', htmlLang: 'ja', dir: 'ja/', label: '日本語' },
  { code: 'en', htmlLang: 'en', dir: 'en/', label: 'EN' },
  { code: 'ko', htmlLang: 'ko', dir: 'ko/', label: '한국어' },
];

const zooById = Object.fromEntries(zoos.map((z) => [z.id, z]));

// ── 動物園頁 slug：en_name（缺則 ja_name，如 Safari Niagara）slugify；
//    2026-07-04 驗證 112 園全數唯一。改英文名會變網址，屬已知取捨。──
const zooSlugify = (s) => s.normalize('NFKD').replace(/[̀-ͯ]/g, '')
  .toLowerCase().replace(/['().]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
for (const z of zoos) {
  z.slug = zooSlugify(z.en_name || z.ja_name || '') || `zoo-${z.id}`;
}
export const zooBySlug = Object.fromEntries(zoos.map((z) => [z.slug, z]));
export const zooSlugById = Object.fromEntries(zoos.map((z) => [z.id, z.slug]));
// 動物園列表／地圖只露出「目前有現居個體」的園；無現居者（個體已故或轉出）
// 仍保留於 zoos（供個別頁與居住史連結的園名解析），僅不在列表/地圖顯示。
export const zoosListed = zoos.filter((z) => z.residents && z.residents.length > 0);
// 供前端內嵌資料（ZOOS_DATA）使用的簡體園名：建置時預轉，客戶端不用帶 OpenCC
for (const z of zoos) {
  const zh = z.name_zh || z.ja_name || z.en_name || '';
  const hans = toHans(zh);
  if (hans && hans !== zh) z.name_zh_hans = hans;
}

// 動物園名依語系：zh-TW＝中文名→日文漢字→英文；zh-CN＝同 zh-TW 再繁→簡；
// ja＝日文→英文；en＝英文→日文；ko＝（暫無韓文名）英文→日文（多為日本園，日文名對韓語讀者亦易辨識）
export const zooName = (id, raw, locale = 'zh-TW') => {
  const z = id && zooById[id] ? zooById[id] : null;
  if (!z) return raw || '';
  if (locale === 'ja') return z.ja_name || z.en_name || raw || '';
  if (locale === 'en') return z.en_name || z.ja_name || raw || '';
  if (locale === 'ko') return z.ko_name || z.en_name || z.ja_name || raw || '';
  const zh = z.name_zh || z.ja_name || z.en_name || raw || '';
  return locale === 'zh-CN' ? toHans(zh) : zh;
};

// 動物園地點依語系：中文（zh-TW／zh-CN）優先 location_zh（正本繁體），缺則退回 location_ja；
// 註記：location_ja 對多數非日本園實為繁中，僅日本相關園存真日文，故中文站對「日文地址」的中國園
// 需靠 location_zh 覆蓋。zh-CN 一律 toHans。ja／en／ko 維持既有 location_ja／location_en 順序。
export const zooLocation = (z, locale = 'zh-TW') => {
  if (!z) return '';
  if (locale === 'ja') return z.location_ja || z.location_en || z.country || '';
  if (locale === 'en' || locale === 'ko') return z.location_en || z.location_ja || z.country || '';
  const zh = z.location_zh || z.location_ja || z.location_en || z.country || '';
  return locale === 'zh-CN' ? toHans(zh) : zh;
};

// ── 地區名依語系（動物園清單的地區 filter）──────────────────────────────
// UI 標籤刻意用「地區／地域／Region」而非「國家」（i18n filter_region）：台灣、香港、澳門
// 在此與各國並列，用「國家」會讓部分讀者讀成主權主張，用「地區」則不表態（同 Apple／Google
// 的 Country or Region 慣例）。資料欄位名維持 country（data/zoos.json 正本欄名），故本區
// 函式仍叫 countryXxx——命名對齊資料來源，顯示層才換詞。
// country 欄位正本為英文（data/zoos.json），且歷史資料大小寫不一（france／Germany 並存），
// 故一律以小寫 key 查表、也以小寫值當 filter 值；查不到的國家原樣顯示英文，不致漏園。
// zh-CN 不用 toHans 機器轉：國名的大陸慣用譯名常整詞不同（義大利→意大利、紐西蘭→新西兰），
// 逐筆手寫較準。表涵蓋 data/zoos.json 目前全部國家（含尚無現居個體的園），日後新增園請補一筆。
const COUNTRY_NAMES = {
  argentina: { 'zh-TW': '阿根廷', 'zh-CN': '阿根廷', ja: 'アルゼンチン', en: 'Argentina', ko: '아르헨티나' },
  australia: { 'zh-TW': '澳洲', 'zh-CN': '澳大利亚', ja: 'オーストラリア', en: 'Australia', ko: '호주' },
  austria: { 'zh-TW': '奧地利', 'zh-CN': '奥地利', ja: 'オーストリア', en: 'Austria', ko: '오스트리아' },
  belgium: { 'zh-TW': '比利時', 'zh-CN': '比利时', ja: 'ベルギー', en: 'Belgium', ko: '벨기에' },
  canada: { 'zh-TW': '加拿大', 'zh-CN': '加拿大', ja: 'カナダ', en: 'Canada', ko: '캐나다' },
  chile: { 'zh-TW': '智利', 'zh-CN': '智利', ja: 'チリ', en: 'Chile', ko: '칠레' },
  china: { 'zh-TW': '中國', 'zh-CN': '中国', ja: '中国', en: 'China', ko: '중국' },
  croatia: { 'zh-TW': '克羅埃西亞', 'zh-CN': '克罗地亚', ja: 'クロアチア', en: 'Croatia', ko: '크로아티아' },
  czechia: { 'zh-TW': '捷克', 'zh-CN': '捷克', ja: 'チェコ', en: 'Czechia', ko: '체코' },
  denmark: { 'zh-TW': '丹麥', 'zh-CN': '丹麦', ja: 'デンマーク', en: 'Denmark', ko: '덴마크' },
  france: { 'zh-TW': '法國', 'zh-CN': '法国', ja: 'フランス', en: 'France', ko: '프랑스' },
  germany: { 'zh-TW': '德國', 'zh-CN': '德国', ja: 'ドイツ', en: 'Germany', ko: '독일' },
  'hong kong': { 'zh-TW': '香港', 'zh-CN': '香港', ja: '香港', en: 'Hong Kong', ko: '홍콩' },
  hungary: { 'zh-TW': '匈牙利', 'zh-CN': '匈牙利', ja: 'ハンガリー', en: 'Hungary', ko: '헝가리' },
  india: { 'zh-TW': '印度', 'zh-CN': '印度', ja: 'インド', en: 'India', ko: '인도' },
  indonesia: { 'zh-TW': '印尼', 'zh-CN': '印尼', ja: 'インドネシア', en: 'Indonesia', ko: '인도네시아' },
  ireland: { 'zh-TW': '愛爾蘭', 'zh-CN': '爱尔兰', ja: 'アイルランド', en: 'Ireland', ko: '아일랜드' },
  'isle of man': { 'zh-TW': '曼島', 'zh-CN': '马恩岛', ja: 'マン島', en: 'Isle of Man', ko: '맨섬' },
  italy: { 'zh-TW': '義大利', 'zh-CN': '意大利', ja: 'イタリア', en: 'Italy', ko: '이탈리아' },
  japan: { 'zh-TW': '日本', 'zh-CN': '日本', ja: '日本', en: 'Japan', ko: '일본' },
  laos: { 'zh-TW': '寮國', 'zh-CN': '老挝', ja: 'ラオス', en: 'Laos', ko: '라오스' },
  macau: { 'zh-TW': '澳門', 'zh-CN': '澳门', ja: 'マカオ', en: 'Macau', ko: '마카오' },
  mexico: { 'zh-TW': '墨西哥', 'zh-CN': '墨西哥', ja: 'メキシコ', en: 'Mexico', ko: '멕시코' },
  nepal: { 'zh-TW': '尼泊爾', 'zh-CN': '尼泊尔', ja: 'ネパール', en: 'Nepal', ko: '네팔' },
  netherlands: { 'zh-TW': '荷蘭', 'zh-CN': '荷兰', ja: 'オランダ', en: 'Netherlands', ko: '네덜란드' },
  'new zealand': { 'zh-TW': '紐西蘭', 'zh-CN': '新西兰', ja: 'ニュージーランド', en: 'New Zealand', ko: '뉴질랜드' },
  poland: { 'zh-TW': '波蘭', 'zh-CN': '波兰', ja: 'ポーランド', en: 'Poland', ko: '폴란드' },
  portugal: { 'zh-TW': '葡萄牙', 'zh-CN': '葡萄牙', ja: 'ポルトガル', en: 'Portugal', ko: '포르투갈' },
  russia: { 'zh-TW': '俄羅斯', 'zh-CN': '俄罗斯', ja: 'ロシア', en: 'Russia', ko: '러시아' },
  singapore: { 'zh-TW': '新加坡', 'zh-CN': '新加坡', ja: 'シンガポール', en: 'Singapore', ko: '싱가포르' },
  slovakia: { 'zh-TW': '斯洛伐克', 'zh-CN': '斯洛伐克', ja: 'スロバキア', en: 'Slovakia', ko: '슬로바키아' },
  'south korea': { 'zh-TW': '韓國', 'zh-CN': '韩国', ja: '韓国', en: 'South Korea', ko: '대한민국' },
  spain: { 'zh-TW': '西班牙', 'zh-CN': '西班牙', ja: 'スペイン', en: 'Spain', ko: '스페인' },
  sweden: { 'zh-TW': '瑞典', 'zh-CN': '瑞典', ja: 'スウェーデン', en: 'Sweden', ko: '스웨덴' },
  taiwan: { 'zh-TW': '台灣', 'zh-CN': '台湾', ja: '台湾', en: 'Taiwan', ko: '타이완' },
  thailand: { 'zh-TW': '泰國', 'zh-CN': '泰国', ja: 'タイ', en: 'Thailand', ko: '태국' },
  uk: { 'zh-TW': '英國', 'zh-CN': '英国', ja: 'イギリス', en: 'UK', ko: '영국' },
  usa: { 'zh-TW': '美國', 'zh-CN': '美国', ja: 'アメリカ', en: 'USA', ko: '미국' },
};
export const countryKey = (c) => (c || '').trim().toLowerCase();
export const countryName = (c, locale = 'zh-TW') => {
  const row = COUNTRY_NAMES[countryKey(c)];
  return (row && (row[locale] || row.en)) || (c || '');
};
// 地區 filter 的選項：只列「有現居個體的園」實際出現的地區（園數多→少，同數依名稱）。
// 未登記 country 的園不產生選項，選「全部」時仍會顯示。
export const countryOptions = (locale = 'zh-TW') => {
  const n = {};
  for (const z of zoosListed) {
    const k = countryKey(z.country);
    if (k) n[k] = (n[k] || 0) + 1;
  }
  return Object.keys(n)
    .map((k) => ({ value: k, label: countryName(k, locale), count: n[k] }))
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label, locale));
};

// 個體所屬地區＝其「代表園」的 country：在世＝現居園、已故＝最後居住園。刻意與搜尋頁
// 動物園 filter 用同一套認定（見 searchDataFor 的 zoo 欄），否則兩個 filter 會互相矛盾。
// 只有 raw 園名、解析不到園 id 時回空字串（該個體不出現在任何地區選項下，選「全部」仍看得到）。
const _zooCountryKey = Object.fromEntries(zoos.map((z) => [z.id, countryKey(z.country)]));
export const pandaRegionKey = (p) => {
  if (!p.died) return _zooCountryKey[p.current_zoo] || '';
  const res = p.residences || [];
  const last = res[res.length - 1];
  return (last && _zooCountryKey[last.zoo_id]) || '';
};

// 佔位個體（蘋果籽）的 ja/ko 顯示名：資料正本 japanese 依規則留空（「赤ちゃん」非正式名）、
// ko 無個體名欄位，故於顯示層由 i18n 直譯（りんごのタネ／사과씨）；多胞胎編號用 placeholder_name_n 模板。
export const placeholderName = (p, locale) => {
  const t = i18n[locale] || {};
  const n = ((p.name || '').match(/(\d+)\s*$/) || [])[1];
  return n && t.placeholder_name_n ? t.placeholder_name_n.replace('{n}', n)
    : t.placeholder_name || p.name;
};

// 已故標記：把 🪽 包成 role="img" + aria-label（螢幕閱讀器念「已故」而非「翅膀」）。
// 前面留一個半形空格保持與名字的間距（與舊 ' ' + deceased_mark 一致）。
export const deceasedHtml = (locale) => {
  const t = i18n[locale] || {};
  return ` <span role="img" aria-label="${t.deceased || 'deceased'}">${t.deceased_mark || '🪽'}</span>`;
};

export const displayName = (p, locale) =>
  p.placeholder && (locale === 'ja' || locale === 'ko') ? placeholderName(p, locale)
    : locale === 'ja' ? p.japanese || p.name
    : locale === 'ko' ? p.korean || p.name
    : locale === 'zh-TW' ? p.chinese || p.kanji || p.name
    : locale === 'zh-CN' ? toHans(p.chinese || p.kanji || p.name)
    : p.name;

// 蘋果籽佔位的「{媽媽}的蘋果籽」顯示名（多胞胎保留號碼）；非佔位＝displayName、
// 無母資料時退回原佔位名。首頁新生 chip 與蘋果籽個體頁標題共用。
export const placeholderMotherName = (p, locale) => {
  if (!p.placeholder) return displayName(p, locale);
  const t = i18n[locale] || {};
  const m = p.mother && pandas[p.mother] ? displayName(pandas[p.mother], locale) : null;
  if (!m) return displayName(p, locale);
  const n = ((p.name || '').match(/(\d+)\s*$/) || [])[1];
  return n && t.placeholder_of_mother_n
    ? t.placeholder_of_mother_n.replace('{m}', m).replace('{n}', n)
    : (t.placeholder_of_mother || '{m}').replace('{m}', m);
};

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
  // 近親迴圈防呆：自己的直系子女／父母永不列為手足（父女配對時，子女會與親代共用一位親本而被誤判）
  (p.children || []).forEach((c) => sibs.delete(c));
  [p.mother, p.father].filter(Boolean).forEach((par) => sibs.delete(par));
  p.full_siblings = []; p.half_siblings = [];
  for (const s of sibs) {
    const q = pandas[s];
    const shareM = p.mother && q.mother === p.mother;
    const shareF = p.father && q.father === p.father;
    (shareM && shareF ? p.full_siblings : p.half_siblings).push(s);
  }
  const byBorn = (a, b) => ((pandas[a].born || '9999') < (pandas[b].born || '9999') ? -1 : 1);
  p.full_siblings.sort(byBorn); p.half_siblings.sort(byBorn);
  // 已宣告手足（frontmatter siblings:，父母不詳無法推導血緣度）：只顯示尚未被
  // 全血／半血涵蓋、且非自己直系父母/子女者，避免重複列出。
  const shown = new Set([...p.full_siblings, ...p.half_siblings, p.slug,
    p.mother, p.father, ...(p.children || [])]);
  p.declared_siblings = (p.declared_siblings || [])
    .filter((s) => pandas[s] && !shown.has(s));
  p.declared_siblings.sort(byBorn);
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

export function subGraph(slug, locale = 'zh-TW') {
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
    // zh-CN：中文名（index 5）建置時轉簡體；佔位個體 ja（index 1）／ko（index 0）換直譯佔位名；
    // 其餘語系直接共用 GRAPH 節點
    let node = GRAPH.nodes[s];
    if (locale === 'zh-CN' && node[5]) node = node.map((v, i) => (i === 5 ? toHans(v) : v));
    if (pandas[s]?.placeholder) {
      if (locale === 'ja') node = node.map((v, i) => (i === 1 ? placeholderName(pandas[s], 'ja') : v));
      else if (locale === 'ko') node = node.map((v, i) => (i === 0 ? placeholderName(pandas[s], 'ko') : v));
    }
    nodes[s] = node;
    if (GRAPH.up[s]) up[s] = GRAPH.up[s].map((x) => (set.has(x) ? x : null));
    if (GRAPH.down[s]) down[s] = GRAPH.down[s].filter((x) => set.has(x));
  }
  return { nodes, up, down, twins: GRAPH.twins.filter(([a, b]) => set.has(a) && set.has(b)) };
}

export const searchDataFor = (locale) => ({
  // 地區下拉的選項：v＝小寫英文 key（對上每隻的 r）、l＝該語系顯示名、c＝個體數。
  // 建置期算好，client 端不必帶地區譯名表。排序同動物園頁：數量多→少，同數依名稱。
  regions: (() => {
    const n = {};
    for (const p of Object.values(pandas)) {
      const k = pandaRegionKey(p);
      if (k) n[k] = (n[k] || 0) + 1;
    }
    return Object.keys(n).map((k) => ({ v: k, l: countryName(k, locale), c: n[k] }))
      .sort((a, b) => b.c - a.c || a.l.localeCompare(b.l, locale));
  })(),
  pandas: Object.values(pandas).map((p) => ({
    slug: p.slug, u: p.urlId,
    // 佔位個體：ko 主名（n）、ja 日文名（j）用直譯佔位名；原英文名移入 en 保持可搜尋
    n: p.placeholder && locale === 'ko' ? placeholderName(p, 'ko') : p.name,
    j: p.placeholder && locale === 'ja' ? placeholderName(p, 'ja') : p.japanese,
    en: [...(p.english_variants || []), ...(p.nicknames || []),
      ...(p.korean ? [p.korean] : []),
      ...(p.placeholder && locale === 'ko' ? [p.name] : [])].join('|') || null,
    k: locale === 'zh-CN' ? toHans(p.chinese || p.kanji || '') || null : p.chinese || p.kanji,
    sex: p.sex, born: p.born, died: p.died,
    uv: p.unverified ? 1 : null,
    ap: p.placeholder ? 1 : null, // 蘋果籽佔位（尚未命名的寶寶）

    ph: (p.instagram || []).length || null,
    kids: (p.children || []).length || null,
    r: pandaRegionKey(p) || null,   // 地區 key（與下方 zoo 同一座園）
    // 在世＝現居園；已故＝最後居住園（否則 zoo 篩選永遠濾不出已故個體，「現存」checkbox 形同虛設）
    zoo: (() => {
      if (!p.died) return zooName(p.current_zoo, p.current_zoo_raw, locale) || null;
      const last = (p.residences || [])[p.residences.length - 1];
      return last ? zooName(last.zoo_id, last.zoo_raw, locale) || null : null;
    })(),
  })),
});

// ── 首頁「今日休園」：有 closed_rule 的園（名稱依語系解析）；今天是否休園由
//    client 端 js/closed.js 以 JST 計算（deploy 無 cron）。──
export const closedDataFor = (locale) => ({
  zoos: zoos.filter((z) => z.closed_rule)
    .map((z) => ({ n: zooName(z.id, null, locale), u: z.slug, r: z.closed_rule })),
});

// ── 日本家系圖（整合頁 #jptree）：建置期算「日本主網」+ 世代分層佈局 ──────
// 「日本個體」＝一生曾住過 country==='Japan' 的園。整個日本其實是一張互相通婚的
// 大家族網，故取最大連通元件呈現（父子＋雙胞胎為邊）。佈局：世代為橫列（y），
// 列內用 barycenter 掃描排序以降低交叉；座標與間距在此固定，前端純平移縮放閱讀。
const _zooCountry = Object.fromEntries(zoos.map((z) => [z.id, z.country]));
const _jpZooIds = (p) => {
  const ids = [];
  for (const r of p.residences || []) {
    if (r.zoo_id != null && _zooCountry[r.zoo_id] === 'Japan' && !ids.includes(r.zoo_id)) ids.push(r.zoo_id);
  }
  return ids;
};

export function japanTreeData(locale = 'zh-TW') {
  const isJP = {};
  for (const p of Object.values(pandas)) isJP[p.slug] = _jpZooIds(p).length > 0;
  const adj = {}, parents = {}, children = {};
  const link = (a, b) => { (adj[a] = adj[a] || new Set()).add(b); (adj[b] = adj[b] || new Set()).add(a); };
  for (const p of Object.values(pandas)) {
    if (!isJP[p.slug]) continue;
    for (const m of [p.mother, p.father]) {
      if (m && isJP[m] && pandas[m]) {
        link(p.slug, m);
        (parents[p.slug] = parents[p.slug] || []).push(m);
        (children[m] = children[m] || []).push(p.slug);
      }
    }
  }
  for (const [a, b] of family.twins) if (isJP[a] && isJP[b]) link(a, b);
  // 最大連通元件
  const seen = new Set(); let best = [];
  for (const s of Object.keys(isJP)) {
    if (!isJP[s] || seen.has(s)) continue;
    const stack = [s], comp = [];
    while (stack.length) {
      const x = stack.pop(); if (seen.has(x)) continue; seen.add(x); comp.push(x);
      if (adj[x]) for (const y of adj[x]) if (!seen.has(y)) stack.push(y);
    }
    if (comp.length > best.length) best = comp;
  }
  const inSet = new Set(best);
  // 世代（元件內最長祖先路徑）
  const memo = {};
  const gen = (s) => {
    if (s in memo) return memo[s];
    memo[s] = 0;
    const ps = (parents[s] || []).filter((x) => inSet.has(x));
    memo[s] = ps.length ? 1 + Math.max(...ps.map(gen)) : 0;
    return memo[s];
  };
  const G = {}; for (const s of best) G[s] = gen(s);
  const maxg = Math.max(...best.map((s) => G[s]));
  const rows = {}; for (const s of best) (rows[G[s]] = rows[G[s]] || []).push(s);
  const gnums = Object.keys(rows).map(Number).sort((a, b) => a - b);
  const order = {};
  const born = (s) => pandas[s].born || '';
  for (const g of gnums) {
    rows[g].sort((a, b) => (born(a) < born(b) ? -1 : born(a) > born(b) ? 1 : 0));
    rows[g].forEach((s, i) => (order[s] = i));
  }
  for (let sweep = 0; sweep < 8; sweep++) {
    for (const g of gnums) {
      if (g === 0) continue;
      const k = (s) => { const ps = (parents[s] || []).filter((x) => inSet.has(x)); return ps.length ? ps.reduce((a, x) => a + order[x], 0) / ps.length : order[s]; };
      rows[g].sort((a, b) => k(a) - k(b)); rows[g].forEach((s, i) => (order[s] = i));
    }
    for (const g of [...gnums].reverse()) {
      const k = (s) => { const ks = (children[s] || []).filter((x) => inSet.has(x)); return ks.length ? ks.reduce((a, x) => a + order[x], 0) / ks.length : order[s]; };
      rows[g].sort((a, b) => k(a) - k(b)); rows[g].forEach((s, i) => (order[s] = i));
    }
  }
  const COLW = 150, ROWH = 170;
  const idx = {}; best.forEach((s, i) => (idx[s] = i));
  const nodes = best.map((s) => {
    const p = pandas[s];
    const rowW = rows[G[s]].length * COLW;
    const x = Math.round((order[s] * COLW - rowW / 2) * 10) / 10;
    return [p.urlId, displayName(p, locale),
      p.sex === 'female' ? 'f' : p.sex === 'male' ? 'm' : 'u',
      p.born ? p.born.slice(0, 4) : '', p.died ? p.died.slice(0, 4) : '',
      G[s], x, G[s] * ROWH, _jpZooIds(p), p.placeholder ? 1 : 0];
  });
  const edges = [];
  for (const s of best) for (const m of parents[s] || []) if (inSet.has(m)) edges.push([idx[s], idx[m]]);
  const twins = [];
  for (const [a, b] of family.twins) if (inSet.has(a) && inSet.has(b)) twins.push([idx[a], idx[b]]);
  const zc = {};
  for (const s of best) for (const z of _jpZooIds(pandas[s])) zc[z] = (zc[z] || 0) + 1;
  const zooList = Object.keys(zc).map(Number).sort((a, b) => zc[b] - zc[a])
    .map((z) => [z, zooName(z, null, locale), zc[z]]);
  return { nodes, edges, twins, maxg, zoos: zooList };
}
