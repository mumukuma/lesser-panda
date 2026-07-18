#!/usr/bin/env python3
"""SVG 重繪四季背景（春/夏/冬），風格對齊現有秋圖：
平塗色塊 + 蠟筆顆粒 + 毛邊。輸出 bg-sky-*.webp / bg-trees-*.webp。"""
import io, math, random
import numpy as np
import cairosvg
from PIL import Image, ImageFilter
from scipy.ndimage import map_coordinates, gaussian_filter, zoom

# ───────────────────────── shape helpers ─────────────────────────

def blob(cx, cy, s, rng, n=6, squash=1.0):
    """canopy/bush：一圈圓形聚成雲朵狀，回傳 circle 列表 (cx,cy,r)"""
    cs = [(cx, cy, s)]
    for i in range(n):
        a = math.pi * 2 * i / n - math.pi / 2 + rng.uniform(-.2, .2)
        d = s * rng.uniform(.62, .8)
        r = s * rng.uniform(.5, .68)
        cs.append((cx + math.cos(a) * d, cy + math.sin(a) * d * squash * .8, r))
    # 頂上再加一顆讓輪廓更像樹
    cs.append((cx + rng.uniform(-.2, .2) * s, cy - s * .78, s * rng.uniform(.5, .62)))
    return cs

def circles_svg(cs, fill, op=1.0):
    o = f' opacity="{op}"' if op < 1 else ''
    return f'<g fill="{fill}"{o}>' + ''.join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>' for x, y, r in cs) + '</g>'

# ── 色塊內明暗（精緻感關鍵）：同形狀 clip 後疊「下緣陰影＋頂部高光」漸層 ──
def _hex2rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def _rgb2hex(c): return '#%02x%02x%02x' % tuple(max(0, min(255, round(v))) for v in c)
def shade(h, f):   # f<1 變暗
    r, g, b = _hex2rgb(h); return _rgb2hex((r * f, g * f, b * f + 8))
def tint(h, f):    # f=往白靠比例
    r, g, b = _hex2rgb(h); return _rgb2hex((r + (255 - r) * f, g + (255 - g) * f, b + (255 - b) * f))

_UID = [0]
def blob_shaded(cs, fill, sh_op=.34, hi_op=.4):
    """圓叢＋內部陰影/高光。回傳 (defs, body)"""
    _UID[0] += 1; u = _UID[0]
    xs = [x - r for x, y, r in cs] + [x + r for x, y, r in cs]
    ys = [y - r for x, y, r in cs] + [y + r for x, y, r in cs]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    dark, light = shade(fill, .8), tint(fill, .55)
    defs = (f'<clipPath id="cp{u}">' + ''.join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>' for x, y, r in cs) + '</clipPath>'
        f'<radialGradient id="sh{u}" cx="38%" cy="92%" r="85%">'
        f'<stop offset="0" stop-color="{dark}" stop-opacity="{sh_op}"/>'
        f'<stop offset="1" stop-color="{dark}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="hi{u}" cx="64%" cy="6%" r="70%">'
        f'<stop offset="0" stop-color="{light}" stop-opacity="{hi_op}"/>'
        f'<stop offset="1" stop-color="{light}" stop-opacity="0"/></radialGradient>')
    rect = f'x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}"'
    body = (circles_svg(cs, fill) +
            f'<g clip-path="url(#cp{u})"><rect {rect} fill="url(#sh{u})"/>'
            f'<rect {rect} fill="url(#hi{u})"/></g>')
    return defs, body

def glow(cx, cy, r, color, op):
    _UID[0] += 1; u = _UID[0]
    defs = (f'<radialGradient id="gl{u}"><stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')
    return defs, f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gl{u})"/>'

def trunk_svg(bx, by, top, w, color, branches):
    """主幹（梯形）＋分枝（圓頭粗線）"""
    s = (f'<path d="M{bx - w:.0f} {by} L{bx - w * .55:.0f} {top} '
         f'L{bx + w * .55:.0f} {top} L{bx + w:.0f} {by} Z" fill="{color}"/>')
    for (x1, y1, x2, y2, bw) in branches:
        s += (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
              f'stroke="{color}" stroke-width="{bw:.1f}" stroke-linecap="round"/>')
    return s

def std_branches(bx, top, h, w):
    """以主幹頂端為中心的標準分枝組"""
    return [
        (bx, top + h * .3, bx, top - h * .32, w * 1.1),
        (bx, top + h * .12, bx - h * .3, top - h * .18, w * .8),
        (bx, top + h * .05, bx + h * .28, top - h * .25, w * .8),
        (bx - h * .16, top - h * .02, bx - h * .34, top - h * .3, w * .55),
        (bx + h * .15, top - h * .08, bx + h * .3, top - h * .38, w * .55),
    ]

def cloud_svg(cx, cy, s, fill, op=.92):
    parts = [(0, 0, .52), (-.62, .12, .38), (.6, .1, .4), (-.25, -.28, .4), (.28, -.25, .36)]
    g = f'<g fill="{fill}" opacity="{op}">'
    for dx, dy, r in parts:
        g += f'<circle cx="{cx + dx * s:.0f}" cy="{cy + dy * s:.0f}" r="{r * s:.0f}"/>'
    g += (f'<rect x="{cx - .75 * s:.0f}" y="{cy + .05 * s:.0f}" width="{1.5 * s:.0f}" '
          f'height="{.28 * s:.0f}" rx="{.14 * s:.0f}"/></g>')
    return g

def twigs_svg(cx, base_y, h, color, w=7, spread=.5):
    """灌木裡的小樹枝：一豎＋幾撇"""
    top = base_y - h
    s = (f'<g stroke="{color}" stroke-width="{w}" stroke-linecap="round" fill="none">'
         f'<line x1="{cx}" y1="{base_y}" x2="{cx}" y2="{top}"/>' )
    for k, (fy, fx) in enumerate([(.35, -spread), (.5, spread), (.66, -spread * .8), (.8, spread * .75)]):
        y1 = base_y - h * fy
        s += (f'<line x1="{cx}" y1="{y1:.0f}" x2="{cx + fx * h * .42:.0f}" '
              f'y2="{y1 - h * .28:.0f}"/>')
    s += '</g>'
    return s

# ───────────────────────── palettes ─────────────────────────
# 樹序：sky 圖左起 T1 大、T2 中、T3 中小、T4 大右
PAL = {
  'spring': dict(
    sky=('#8fc3d9', '#f7e9dd', '#fbeff0'),
    cloud='#ffffff', cloud_lo='#fbe3ea',
    sun='#fbe7a3', sun_op=.75,
    ground='#c3dc8f', ground_hi='#cfe49e',
    bushA='#9cc27f', bushB='#b4d491',
    trees=[('#f2b6cb', '#a06b52'), ('#b7d379', '#a06b52'),
           ('#f6c6d6', '#a06b52'), ('#a9cf6e', '#a06b52')],
    # trees 圖層
    backA='#a9c98b', backB='#97b979', twig='#7ea363',
    front=[('#f4bed1', '#d98ba8'), ('#b7d379', '#8fae57'),
           ('#f2b0c8', '#a06b52'), ('#cfe08a', '#a4b862')],
  ),
  'summer': dict(
    sky=('#5fa8cf', '#a9d6e6', '#eaf3d8'),
    cloud='#ffffff', cloud_lo='#f2fafd',
    sun='#ffd95c', sun_op=.9,
    ground='#8fbf62', ground_hi='#a3cc74',
    bushA='#5d9a52', bushB='#74ad60',
    trees=[('#4e8f4c', '#6d4f38'), ('#7ab35f', '#6d4f38'),
           ('#5f9e57', '#6d4f38'), ('#8fbf6a', '#6d4f38')],
    backA='#79a865', backB='#679757', twig='#527e45',
    front=[('#a9cf6e', '#82a44e'), ('#6faf5c', '#54904a'),
           ('#3f8a49', '#6d4f38'), ('#8fbf62', '#6da24c')],
  ),
  'winter': dict(
    sky=('#93aec9', '#c4d3e0', '#dcd8d0'),
    cloud='#ffffff', cloud_lo='#e8edf3',
    sun='#f7f0d8', sun_op=.7,
    ground='#eef2f6', ground_hi='#fafcfd',
    bushA='#b9cbda', bushB='#d5e0ea',
    trees=[('#fbfdfe', '#7a6353'), ('#eef3f8', '#7a6353'),
           ('#fbfdfe', '#7a6353'), ('#f2f6fa', '#7a6353')],
    backA='#d4dfe9', backB='#c3d2df', twig='#9fb2c2',
    front=[('#eef2f6', '#c2d0dc'), ('#e2eaf1', '#b6c7d5'),
           ('#f2f5f8', '#7a6353'), ('#e8eef4', '#bfcedb')],
  ),
}

# 前景（bg-foreground）：竹子＋葉叢＋角落灌木。含秋季（預設水彩圖留作無 JS fallback）
FG_PAL = {
  'autumn': dict(bamboo='#e3a83e', node='#c8892b', stemleaf='#eac153',
                 fern1='#a9bd8a', fern2='#8fae6f', accent='#cd6236',
                 bigleaf='#8faf72', bigleaf2='#a3bd82', vein='#7a9a5e', sprig='#ecc95c'),
  'spring': dict(bamboo='#b9d47c', node='#9dbb5f', stemleaf='#cfe08a',
                 fern1='#b4d491', fern2='#9cc27f', accent='#f2b6cb',
                 bigleaf='#a9cf6e', bigleaf2='#bfdb85', vein='#8fae57', sprig='#f6c6d6'),
  'summer': dict(bamboo='#8fbf62', node='#74a24b', stemleaf='#a9cf6e',
                 fern1='#74ad60', fern2='#5d9a52', accent='#4e8f4c',
                 bigleaf='#5f9e57', bigleaf2='#74ad60', vein='#478041', sprig='#ffd95c'),
  'winter': dict(bamboo='#cfdae4', node='#b3c3d1', stemleaf='#e2eaf1',
                 fern1='#d5e0ea', fern2='#c3d2df', accent='#eef2f6',
                 bigleaf='#dae4ec', bigleaf2='#e8eef4', vein='#aabccb', sprig='#fbfdfe'),
}

def leaf_el(cx, cy, rx, ry, ang, fill, op=1.0):
    o = f' opacity="{op}"' if op < 1 else ''
    return (f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" '
            f'fill="{fill}"{o} transform="rotate({ang:.0f} {cx:.0f} {cy:.0f})"/>')

def bamboo_svg(xb, yb, yt, w, lean, fill, node_fill):
    """竹稈：微傾斜的圓角長條＋節線"""
    s = (f'<g transform="rotate({lean} {xb} {yb})">'
         f'<rect x="{xb - w/2:.0f}" y="{yt}" width="{w}" height="{yb - yt}" rx="{w/2:.0f}" fill="{fill}"/>')
    y = yt + 90
    while y < yb - 60:
        s += (f'<rect x="{xb - w/2 - 2:.0f}" y="{y:.0f}" width="{w + 4}" height="9" '
              f'rx="4" fill="{node_fill}"/>')
        y += 150
    return s + '</g>'

def stem_leaves_svg(x0, y0, x1, y1, n, llen, fill, stem, sw=7):
    """一根莖＋交錯羽狀葉"""
    s = (f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{stem}" '
         f'stroke-width="{sw}" stroke-linecap="round"/>')
    for i in range(1, n + 1):
        t = i / (n + 1)
        px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        side = -1 if i % 2 else 1
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0)) + side * 52
        lx = px + math.cos(math.radians(ang)) * llen * .55
        ly = py + math.sin(math.radians(ang)) * llen * .55
        s += leaf_el(lx, ly, llen * .55, llen * .22, ang, fill)
    return s

def fg_svg(F):
    W, H = 1536, 1024
    rng = random.Random(11)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">']
    # ── 左角 ──
    # 蕨葉（後層）
    s.append(stem_leaves_svg(60, 1010, 25, 620, 6, 62, F['fern1'], F['fern1'], 8))
    s.append(stem_leaves_svg(130, 1010, 100, 700, 5, 58, F['fern2'], F['fern2'], 7))
    s.append(stem_leaves_svg(370, 1010, 350, 760, 5, 54, F['fern1'], F['fern1'], 7))
    s.append(stem_leaves_svg(330, 1010, 390, 640, 6, 66, F['fern2'], F['fern2'], 8))
    s.append(stem_leaves_svg(300, 1010, 245, 520, 7, 60, F['fern1'], F['fern1'], 7))
    # 竹稈
    s.append(bamboo_svg(150, 1010, 130, 26, -3, F['bamboo'], F['node']))
    s.append(bamboo_svg(80, 1010, 380, 20, -6, F['bamboo'], F['node']))
    s.append(bamboo_svg(212, 1010, 540, 17, 3, F['bamboo'], F['node']))
    # 梯狀葉莖（原圖的黃葉梯）
    s.append(stem_leaves_svg(268, 1000, 262, 240, 9, 56, F['stemleaf'], F['stemleaf'], 8))
    # 角落主灌木（季節重點色、含明暗）
    d, b = blob_shaded(blob(185, 870, 125, rng, squash=.95), F['accent'])
    s.append(f'<defs>{d}</defs>' + b)
    # 底部小草叢
    s.append(stem_leaves_svg(430, 1015, 445, 830, 4, 46, F['fern2'], F['fern2'], 6))
    s.append(stem_leaves_svg(510, 1020, 495, 880, 3, 40, F['fern1'], F['fern1'], 6))
    # ── 右角 ──
    # 小竹＋後層小葉
    s.append(bamboo_svg(1128, 1010, 600, 16, -2, F['bamboo'], F['node']))
    s.append(stem_leaves_svg(1085, 1010, 1060, 640, 5, 52, F['stemleaf'], F['stemleaf'], 7))
    s.append(stem_leaves_svg(985, 1015, 1005, 800, 4, 48, F['fern2'], F['fern2'], 6))
    # 大葉植物（扇形展開）
    for i, (ang, ln) in enumerate([(-118, 300), (-95, 340), (-72, 330), (-48, 300), (-25, 260)]):
        a = math.radians(ang)
        cx = 1330 + math.cos(a) * ln * .55
        cy = 1010 + math.sin(a) * ln * .55
        fill = F['bigleaf'] if i % 2 == 0 else F['bigleaf2']
        s.append(leaf_el(cx, cy, ln * .5, ln * .18, ang, fill))
        s.append(f'<line x1="1330" y1="1010" x2="{1330 + math.cos(a) * ln * .88:.0f}" '
                 f'y2="{1010 + math.sin(a) * ln * .88:.0f}" stroke="{F["vein"]}" '
                 f'stroke-width="6" stroke-linecap="round"/>')
    # 高葉莖＋重點色小叢
    s.append(stem_leaves_svg(1452, 1010, 1440, 300, 8, 58, F['fern1'], F['fern1'], 8))
    s.append(stem_leaves_svg(1258, 1015, 1268, 850, 4, 44, F['sprig'], F['sprig'], 6))
    s.append('</svg>')
    return ''.join(s)

# ───────────────────────── scenes ─────────────────────────

def sky_svg(P):
    W, H = 1280, 854
    rng = random.Random(42)
    D, B = [], []   # defs / body
    def add(pair): d, b = pair; D.append(d); B.append(b)
    a, b, c = P['sky']
    D.append(f'''<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{a}"/><stop offset=".42" stop-color="{b}"/>
      <stop offset="1" stop-color="{c}"/></linearGradient>''')
    B.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
    # 地平線暖染＋太陽光暈＋太陽
    add(glow(660, 720, 560, c, .55))
    add(glow(700, 655, 150, P['sun'], .5))
    B.append(f'<circle cx="700" cy="655" r="42" fill="{P["sun"]}" opacity="{P["sun_op"]}"/>')
    # 雲
    for (cx, cy, cs2, f, o) in [(180,120,105,P['cloud'],.94),(885,280,75,P['cloud_lo'],.88),
                                (1055,130,100,P['cloud'],.94)]:
        B.append(cloud_svg(cx, cy, cs2, f, o))
    # 背景灌木帶（兩色兩排、含明暗）
    for (bx, by, bs) in [(60,760,90),(200,730,110),(330,760,95),(470,790,85),
                         (760,780,90),(950,760,100),(1230,750,95)]:
        add(blob_shaded(blob(bx, by, bs, rng, squash=.8), P['bushA'], .3, .3))
    for (bx, by, bs) in [(130,790,80),(290,800,85),(540,815,70),(700,825,60),
                         (860,805,75),(1050,790,85),(1200,800,80)]:
        add(blob_shaded(blob(bx, by, bs, rng, squash=.8), P['bushB'], .3, .3))
    # 地面（中央下凹）＋灌木底接觸陰影＋色帶
    _UID[0] += 1; u = _UID[0]
    D.append(f'<linearGradient id="gsh{u}" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{shade(P["ground"], .78)}" stop-opacity=".5"/>'
             f'<stop offset="1" stop-color="{shade(P["ground"], .78)}" stop-opacity="0"/></linearGradient>')
    B.append(f'''<path d="M0 760 C 220 770, 420 810, 640 828 C 860 810, 1060 768, {W} 756
      L{W} {H} L0 {H} Z" fill="{P['ground']}"/>''')
    B.append(f'''<path d="M0 760 C 220 770, 420 810, 640 828 C 860 810, 1060 768, {W} 756
      L{W} 830 L0 834 Z" fill="url(#gsh{u})"/>''')
    B.append(f'''<path d="M0 800 C 260 806, 480 838, 640 846 C 820 838, 1040 802, {W} 792
      L{W} {H} L0 {H} Z" fill="{P['ground_hi']}"/>''')
    add(glow(680, 856, 300, tint(P['ground_hi'], .5), .5))   # 太陽下方地面亮斑
    # 四棵主樹（樹冠含明暗）
    T = P['trees']
    def tree(bx, base, ch, cs, ti, tw):
        cnp, trk = T[ti]
        top = base - ch
        B.append(trunk_svg(bx, base, top + cs * .3, tw, trk,
                           std_branches(bx, top + cs * .3, cs * 1.5, tw * .62)))
        add(blob_shaded(blob(bx, top, cs, rng), cnp))
    tree(185, 800, 330, 118, 0, 17)   # 左大
    tree(415, 795, 205, 76, 1, 11)    # 左中
    tree(878, 792, 205, 74, 2, 11)    # 右中
    tree(1100, 792, 275, 102, 3, 15)  # 右大
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">'
            f'<defs>{"".join(D)}</defs>{"".join(B)}</svg>')


def trees_svg(P):
    W, H = 1536, 1024
    rng = random.Random(7)
    GY = 948  # 地面線，之後裁掉以下
    D, B = [], []
    def add(pair): d, b = pair; D.append(d); B.append(b)
    # 背景綠叢（兩色、含明暗）＋小枝
    for (bx, by, bs) in [(120,860,120),(300,800,140),(470,860,115),(700,880,105),
                         (860,860,110),(1290,810,135),(1470,860,115)]:
        add(blob_shaded(blob(bx, by, bs, rng, squash=.85), P['backA'], .3, .3))
    B.append(twigs_svg(255, 900, 190, P['twig'], 8))
    B.append(twigs_svg(800, 940, 160, P['twig'], 7))
    B.append(twigs_svg(1310, 900, 180, P['twig'], 8))
    for (bx, by, bs) in [(60,910,95),(400,905,100),(620,920,85),(950,910,95),
                         (1180,905,95),(1420,915,90)]:
        add(blob_shaded(blob(bx, by, bs, rng, squash=.85), P['backB'], .3, .3))
    F = P['front']
    # 前景灌木 1（左）
    add(blob_shaded(blob(195, 890, 105, rng, squash=.9), F[0][0]))
    B.append(twigs_svg(195, 940, 130, F[0][1], 8))
    # 前景灌木 2
    add(blob_shaded(blob(530, 855, 125, rng, squash=.9), F[1][0]))
    B.append(twigs_svg(530, 935, 175, F[1][1], 9))
    # 大樹（有主幹）
    cnp, trk = F[2]
    B.append(trunk_svg(1025, GY + 6, 700, 15, trk, std_branches(1025, 700, 160, 10)))
    add(blob_shaded(blob(1030, 700, 135, rng), cnp))
    # 前景灌木 3（右）
    add(blob_shaded(blob(1310, 905, 95, rng, squash=.9), F[3][0]))
    B.append(twigs_svg(1310, 945, 110, F[3][1], 7))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">'
           f'<defs>{"".join(D)}</defs>{"".join(B)}</svg>')
    return svg, GY

# ───────────────────────── raster post fx ─────────────────────────

def smooth_field(h, w, cells, seed, amp):
    rng = np.random.default_rng(seed)
    small = rng.uniform(-1, 1, (max(2, h // cells), max(2, w // cells)))
    f = zoom(small, (h / small.shape[0], w / small.shape[1]), order=3)
    return f[:h, :w] * amp

def crayon(img, seed=0, amp=4.2, grain=.1, blur=.7, cut_y=None):
    """毛邊位移（粗＋細兩頻）+ 顆粒 + 微模糊。img: PIL RGBA/RGB → 同模式"""
    arr = np.asarray(img).astype(np.float32)
    h, w = arr.shape[:2]
    if cut_y is not None and arr.shape[2] == 4:
        arr[cut_y:, :, 3] = 0
    dx = smooth_field(h, w, 26, seed + 1, amp) + smooth_field(h, w, 7, seed + 5, amp * .38)
    dy = smooth_field(h, w, 26, seed + 2, amp) + smooth_field(h, w, 7, seed + 6, amp * .38)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    coords = [yy + dy, xx + dx]
    out = np.stack([map_coordinates(arr[..., i], coords, order=1, mode='nearest')
                    for i in range(arr.shape[2])], axis=-1)
    for i in range(out.shape[2]):
        out[..., i] = gaussian_filter(out[..., i], blur)
    # 顆粒（細＋中兩層），RGB 乘法、alpha 不動
    rng = np.random.default_rng(seed + 9)
    fine = gaussian_filter(rng.uniform(-1, 1, (h, w)), .55)
    fine /= max(1e-6, np.abs(fine).max())
    mid = smooth_field(h, w, 5, seed + 3, 1.0)
    mid /= max(1e-6, np.abs(mid).max())
    g = 1 + grain * (0.8 * fine + 0.45 * mid)
    out[..., :3] *= g[..., None]
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out, 'RGBA' if out.shape[2] == 4 else 'RGB')


def render(svg, w, h, rgba):
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=w, output_height=h,
                           background_color=None if rgba else 'white')
    im = Image.open(io.BytesIO(png))
    return im.convert('RGBA' if rgba else 'RGB')

# ───────────────────────── main ─────────────────────────
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(OUT, exist_ok=True)
for season, P in PAL.items():
    sky = render(sky_svg(P), 1280, 854, rgba=False)
    sky = crayon(sky.convert('RGBA'), seed=hash(season) % 999, grain=.085).convert('RGB')
    sky.save(f'{OUT}/bg-sky-{season}.png')
    svg2, gy = trees_svg(P)
    tr = render(svg2, 1536, 1024, rgba=True)
    tr = crayon(tr, seed=hash(season) % 999 + 5, grain=.09, cut_y=gy)
    tr.save(f'{OUT}/bg-trees-{season}.png')
    print(season, 'done')
for season, F in FG_PAL.items():
    fg = render(fg_svg(F), 1536, 1024, rgba=True)
    fg = crayon(fg, seed=hash(season) % 999 + 11, grain=.09)
    fg.save(f'{OUT}/bg-foreground-{season}.png')
    print('fg', season, 'done')
