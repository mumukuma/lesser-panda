/* 「今日休園」規則引擎單元測試（node web/tests/closed.test.mjs，無相依套件）。
   直接載入 web/public/js/closed.js 的計算核心（module.exports 分支），
   規則取自 data/zoos.json 的 closed_rule（與上線資料同源，非另抄一份）。 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = readFileSync(resolve(here, '../public/js/closed.js'), 'utf8');
const mod = { exports: {} };
new Function('module', 'window', src)(mod, undefined);
const { isZooClosed, isHoliday } = mod.exports;

const zoos = JSON.parse(readFileSync(resolve(here, '../../data/zoos.json'), 'utf8'));
const rules = Object.fromEntries(zoos.filter((z) => z.closed_rule).map((z) => [z.canonical, z.closed_rule]));
const noRule = (name) => !zoos.find((z) => z.canonical === name)?.closed_rule;

const D = (s) => { const [y, m, d] = s.split('-').map(Number); return { y, m, d }; };
let pass = 0, fail = 0;
const eq = (got, want, label) => {
  if (got === want) { pass++; return; }
  fail++; console.error(`❌ ${label}: got ${got}, want ${want}`);
};
const closed = (zoo, date, want, label) => eq(isZooClosed(rules[zoo], D(date)), want, `${zoo} ${date} ${label}`);

/* ── 0. 祝日表本身 ── */
eq(isHoliday(D('2026-09-22')), true, '2026-09-22 国民の休日');
eq(isHoliday(D('2026-05-06')), true, '2026-05-06 振替休日');
eq(isHoliday(D('2027-03-22')), true, '2027-03-22 春分振替');
eq(isHoliday(D('2026-05-07')), false, '2026-05-07 平日');

/* ── 1. 祝日月曜「翌日」順延（上野 mon next_day）：2026-01-12 成人の日 ── */
closed('恩賜上野動物園', '2026-01-12', false, '成人の日は開園');
closed('恩賜上野動物園', '2026-01-13', true, '翌火曜に順延休園');
closed('恩賜上野動物園', '2026-01-19', true, '平常月曜は休園');

/* ── 2. 「翌平日」順延跨連續祝日（日本平 mon next_weekday）：
       2026-05-04 みどりの日(月) → 5/5 こどもの日・5/6 振替を跳過 → 5/7(木) ── */
closed('静岡市立日本平動物園', '2026-05-04', false, 'GW月曜祝日は開園');
closed('静岡市立日本平動物園', '2026-05-05', false, '順延先も祝日→開園');
closed('静岡市立日本平動物園', '2026-05-06', false, '振替休日→開園');
closed('静岡市立日本平動物園', '2026-05-07', true, '直後の平日休園');

/* ── 3. 第 N 週型（大牟田 第2・4月曜 next_day）── */
closed('大牟田市動物園', '2026-08-10', true, '第2月曜休園');
closed('大牟田市動物園', '2026-08-03', false, '第1月曜は開園');
closed('大牟田市動物園', '2026-01-12', false, '第2月曜=成人の日→開園');
closed('大牟田市動物園', '2026-01-13', true, '祝日順延で翌日休園');

/* ── 4. 季節限定週休邊界（茶臼山 12–2月の月曜）── */
closed('長野市茶臼山動物園', '2026-11-30', false, '11月最終月曜は対象外');
closed('長野市茶臼山動物園', '2026-12-07', true, '12月の月曜休園');
closed('長野市茶臼山動物園', '2027-03-01', false, '3月の月曜は対象外');

/* ── 5. 年末年始跨年（ズーラシア 12/29–1/1）── */
closed('よこはま動物園ズーラシア', '2026-12-31', true, '年末休園');
closed('よこはま動物園ズーラシア', '2027-01-01', true, '元日休園');
closed('よこはま動物園ズーラシア', '2027-01-02', false, '1/2 開園');
closed('よこはま動物園ズーラシア', '2026-12-28', false, '12/28 開園（火曜でない）');

/* ── 6. 甲府整修休園中（〜2027-03-31）── */
closed('甲府市遊亀公園附属動物園', '2026-08-15', true, '休園中');
closed('甲府市遊亀公園附属動物園', '2027-03-31', true, '最終日まで休園');
closed('甲府市遊亀公園附属動物園', '2027-04-01', false, '予定明けは判定しない');

/* ── 7. 年中無休／不定休園：closed_rule 無し（=永不出現在今日休園）── */
for (const n of ['川崎市夢見ヶ崎動物公園', 'ネオパークオキナワ', '横浜・八景島シーパラダイス'])
  eq(noRule(n), true, `${n} 年中無休→無rule`);
for (const n of ['那須どうぶつ王国', 'アドベンチャーワールド', '神戸どうぶつ王国', '日立市かみね動物園', '桐生が岡動物園', '旭川市旭山動物園', '池田動物園'])
  eq(noRule(n), true, `${n} 不定休/カレンダー制→無rule`);

/* ── 8. 円山：8月は第1・4水曜＋4月・11月の第2水曜を含む週の平日 ── */
closed('札幌市円山動物園', '2026-08-05', true, '8月第1水曜休園');
closed('札幌市円山動物園', '2026-08-12', false, '8月第2水曜は開園');
closed('札幌市円山動物園', '2026-07-08', true, '7月第2水曜休園');
closed('札幌市円山動物園', '2026-04-06', true, '4月第2水曜(4/8)週の月曜');
closed('札幌市円山動物園', '2026-04-10', true, '同週の金曜');
closed('札幌市円山動物園', '2026-04-11', false, '同週の土曜は対象外');
closed('札幌市円山動物園', '2026-04-15', false, '翌週水曜(第3)は開園');

/* ── 9. 熊本：第4月曜は開園し翌日休園、他の月曜は翌平日順延 ── */
closed('熊本市動植物園', '2026-07-27', false, '第4月曜は開園');
closed('熊本市動植物園', '2026-07-28', true, '翌火曜休園');
closed('熊本市動植物園', '2026-07-06', true, '通常月曜休園');

/* ── 10. 祝日は開園・順延なし（王子 wed open）：2026-11-03 文化の日は火曜 → 対象外、
        2026-02-11 建国記念の日(水) → 開園、翌日も休まない ── */
closed('神戸市立王子動物園', '2026-02-11', false, '祝日水曜は開園');
closed('神戸市立王子動物園', '2026-02-12', false, '順延なし');
closed('神戸市立王子動物園', '2026-02-18', true, '平常水曜休園');

/* ── 11. suspend 慣例窗（群馬 wed、夏休み 7/20–8/31 無休）── */
closed('群馬サファリパーク', '2026-08-05', false, '夏休み中の水曜は無休');
closed('群馬サファリパーク', '2026-06-03', true, '通常水曜休園');
closed('群馬サファリパーク', '2027-01-01', true, '元日休園');
closed('群馬サファリパーク', '2026-12-30', false, '年末無休窗');

/* ── 12. 冬季のみ開園制（大森山 1–2月は土日祝のみ開園）── */
closed('秋田市大森山動物園ミルヴェ', '2027-01-20', true, '1月の平日休園');
closed('秋田市大森山動物園ミルヴェ', '2027-01-11', false, '成人の日は開園');
closed('秋田市大森山動物園ミルヴェ', '2027-01-16', false, '土曜は開園');
closed('秋田市大森山動物園ミルヴェ', '2026-12-15', true, '冬季休園期間');
closed('秋田市大森山動物園ミルヴェ', '2027-03-10', true, '3月休園期間');
closed('秋田市大森山動物園ミルヴェ', '2027-03-25', false, '3/20以降開園');

/* ── 13. 季節限定週休（釧路 12–2月の水曜、祝日でも休園）── */
closed('釧路市動物園', '2027-01-06', true, '1月の水曜休園');
closed('釧路市動物園', '2026-10-07', false, '10月の水曜は対象外');
closed('釧路市動物園', '2026-12-30', true, '年末休園（12/29–1/2）');

/* ── 14. 野毛山：5月無休＋2027-01-07からリニューアル長期休園 ── */
closed('横浜市立野毛山動物園', '2026-05-11', false, '5月の月曜は無休');
closed('横浜市立野毛山動物園', '2026-06-01', true, '6月の月曜休園');
closed('横浜市立野毛山動物園', '2027-02-14', true, 'リニューアル休園中(日曜でも)');

/* ── 15. 東武：1–2月の火水・6月の水・7月第1〜3水 ── */
closed('東武動物公園', '2026-01-20', true, '1月の火曜休園');
closed('東武動物公園', '2026-07-01', true, '7月第1水曜休園');
closed('東武動物公園', '2026-07-22', false, '7月第4水曜は開園');
closed('東武動物公園', '2026-03-03', false, '3月の火曜は対象外');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
