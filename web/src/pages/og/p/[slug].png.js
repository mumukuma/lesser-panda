/* 個體 OG 卡片（#22）：build 時為每隻生成 1200×630 PNG（satori → resvg）。
   全站語系共用一張（名字以日文名／羅馬拼音為主）；無 emoji（satori 需另掛 emoji 字型，
   已逝改以生卒年間呈現＋彩虹漸層條）。字型：Noto Sans JP Bold（web/assets/og/，SIL OFL）。 */
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { pandas, zooName } from '../../../lib/data.js';

// build cwd 是 web/（同 data.js 的約定）
const font = readFileSync(resolve(process.cwd(), 'assets/og/NotoSansJP-Bold.ttf'));
const mascot = 'data:image/png;base64,' +
  readFileSync(resolve(process.cwd(), 'assets/og/mascot.png')).toString('base64');

// 淺色主題色票（global.css :root）
const C = {
  bg: '#fdf8f2', card: '#fffdfb', ink: '#3d2c23', soft: '#7a6a5f',
  rust: '#b5552d', rustDark: '#8f3f1e', amber: '#e8a13c', cream: '#f5e9d9',
  line: '#ece0cf', female: '#c2563f', male: '#3f7a8c',
};
const RAINBOW = 'linear-gradient(90deg,#e57373,#e8a13c,#f2d06b,#8bb672,#6aa7c4,#9b7fb8)';

const h = (type, style, ...children) =>
  ({ type, props: { style, children: children.length === 1 ? children[0] : children } });

export function getStaticPaths() {
  return Object.values(pandas).map((p) => ({ params: { slug: p.urlId }, props: { slug: p.slug } }));
}

export async function GET({ props }) {
  const p = pandas[props.slug];
  const name = p.japanese || p.name;
  const sub = [p.name !== name ? p.name : null, p.chinese && p.chinese !== name ? p.chinese : null]
    .filter(Boolean).join(' · ');
  const sexMark = p.sex === 'female' ? '♀' : p.sex === 'male' ? '♂' : '';
  const sexColor = p.sex === 'female' ? C.female : p.sex === 'male' ? C.male : C.soft;
  const nameSize = name.length <= 6 ? 92 : name.length <= 10 ? 72 : name.length <= 16 ? 54 : 42;

  const zoo = !p.died && p.current_zoo ? zooName(p.current_zoo, p.current_zoo_raw, 'ja') : (!p.died ? p.current_zoo_raw : null);
  const dates = p.died
    ? `${p.born || '?'} – ${p.died}`
    : (p.born ? `Born ${p.born}` : null);

  const infoLine = (txt, color) => txt
    ? h('div', { display: 'flex', fontSize: 30, color: color || C.soft, marginTop: 10 }, txt)
    : null;

  const tree = h('div', {
    width: 1200, height: 630, display: 'flex', flexDirection: 'column',
    backgroundColor: C.bg, fontFamily: 'Noto Sans JP', padding: '44px 56px 0',
  },
    h('div', { display: 'flex', flex: 1, alignItems: 'center' },
      // 左：文字
      h('div', { display: 'flex', flexDirection: 'column', flex: 1, paddingRight: 30 },
        h('div', { display: 'flex', alignItems: 'baseline' },
          h('div', { display: 'flex', fontSize: nameSize, color: C.rustDark, lineHeight: 1.15 }, name),
          sexMark ? h('div', { display: 'flex', fontSize: Math.round(nameSize * 0.55), color: sexColor, marginLeft: 18 }, sexMark) : null,
        ),
        sub ? h('div', { display: 'flex', fontSize: 34, color: C.soft, marginTop: 8 }, sub) : null,
        // 已逝：彩虹條（代替 🌈）
        p.died ? h('div', { display: 'flex', width: 320, height: 12, borderRadius: 6, marginTop: 22, backgroundImage: RAINBOW }) : null,
        h('div', { display: 'flex', flexDirection: 'column', marginTop: p.died ? 14 : 26 },
          infoLine(dates, p.died ? C.rust : C.soft),
          infoLine(zoo),
        ),
      ),
      // 右：吉祥物
      h('div', { display: 'flex', alignItems: 'center' },
        { type: 'img', props: { src: mascot, width: 238, height: 280, style: { opacity: 0.95 } } },
      ),
    ),
    // 底部品牌條
    h('div', {
      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      borderTop: `3px solid ${C.line}`, margin: '0 -56px', padding: '20px 56px 26px',
      backgroundColor: C.cream,
    },
      h('div', { display: 'flex', fontSize: 30, color: C.rustDark }, '小熊貓圖鑑 · レッサーパンダ図鑑'),
      h('div', { display: 'flex', fontSize: 28, color: C.soft }, 'ressapanda.com'),
    ),
  );

  const svg = await satori(tree, {
    width: 1200, height: 630,
    fonts: [{ name: 'Noto Sans JP', data: font, weight: 700, style: 'normal' }],
  });
  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(png, { headers: { 'Content-Type': 'image/png' } });
}
