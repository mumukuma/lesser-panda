#!/usr/bin/env python3
"""
build_mascot.py — 從 ASCII pixel map 生成「穩定的」像素風小熊貓 sprite 動畫頁。

為什麼穩定（對比之前用 OpenAI 生圖逐格做動畫）：
  - 每一格都是確定性的程式（SVG <rect>），不是生成的點陣圖 → 角色不會走樣、不會對不齊。
  - 動畫全部用 CSS @keyframes + steps()，無 JS、無外部圖檔。
  - 所有會動的部位用同一個 --dur + steps(16) → 整體像 16 格逐格 sprite 一起跳動。

來源是這支 Python（ASCII 圖 + 色票）；輸出 web/public/mascot-lab.html 是衍生品。
改圖：編輯下方的 BASE / TAIL / ARM 字串，重跑本檔即可。
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "web", "public", "mascot-lab.html")

# ── 色票（與站台一致：rust / cream / amber / ink）────────────────────
LEGEND = {
    ".": None,         # 透明
    "K": "#3a2317",    # 描邊 / 深色
    "R": "#b5552d",    # rust 身體
    "r": "#8f3f1e",    # rust 陰影
    "A": "#e8a13c",    # amber 高光
    "C": "#f7ecdc",    # cream 臉部斑紋
    "W": "#ffffff",    # 眼睛反光
    "E": "#241712",    # 眼珠
    "P": "#e8959c",    # 腮紅
}

# ── 身體 + 頭 + 臉（24 寬 × 22 高），不含尾巴與揮手臂 ──────────────────
BASE = [
    "........................",  # 0
    "...KKK........KKK.......",  # 1  耳朵尖
    "..KCCK......KCCK........",  # 2  耳內 cream
    "..KRRRKKKKKKRRRK........",  # 3  頭頂 rust + 耳根
    ".KRRRRRRRRRRRRRRK.......",  # 4  額頭 rust
    ".KRCCCCCCCCCCCCRK.......",  # 5  白眉帶
    ".KCCEECCCCCCEECCK.......",  # 6  眼睛
    ".KCCEWCCCCCCEWCCK.......",  # 7  眼睛 + 反光
    ".KCrrCCCKKCCCrrCK.......",  # 8  淚紋 + 鼻
    ".KCCCCCCKKCCCCCCK.......",  # 9  鼻下
    ".KPCCCCCCCCCCCCPK.......",  # 10 腮紅 + 嘴區
    "..KCCCCCCCCCCCCK........",  # 11 下巴
    "...KRRRRRRRRRRK.........",  # 12 肩
    "...RRRRCCCCRRRR.........",  # 13 胸 cream
    "...RRRRCCCCRRRR.........",  # 14
    "...RRRRCCCCRRRR.........",  # 15
    "...RRRRCCCCRRRR.........",  # 16
    "...RRRRRRRRRRRR.........",  # 17
    "...rRRRRRRRRRRr.........",  # 18 下身陰影
    "...rRRRRRRRRRRr.........",  # 19
    "....KKKK..KKKK..........",  # 20 腳（dark）
    "........................",  # 21
]

# ── 大尾巴（環紋），自成一格以便擺動。放在身體右側 ───────────────────
TAIL = [
    ".KKKK....",   # 0
    "KRRRRK...",   # 1
    "KRRRRRK..",   # 2
    "KCCCCCK..",   # 3 cream 環
    "KRRRRRRK.",   # 4
    "KARRRRAK.",   # 5 amber 高光
    "KCCCCCCK.",   # 6 cream 環
    ".KRRRRRK.",   # 7
    ".KRRRRRK.",   # 8
    ".KCCCCK..",   # 9 cream 環
    "..KRRK...",   # 10 尖
    "...KK....",   # 11
]

# ── 揮手的手臂（cream 掌 + rust 臂），自成一格旋轉 ───────────────────
ARM = [
    ".KCCK.",   # 0 掌
    "KCWCCK",   # 1 掌 + 高光
    "KCCCCK",   # 2
    "KCCCCK",   # 3
    ".KRRK.",   # 4 臂
    ".KRRK.",   # 5
    ".KRRK.",   # 6
    ".KRRK.",   # 7
    "..KK..",   # 8 肩
]


def to_rects(grid, x0=0, y0=0):
    """把 ASCII 圖轉成合併過水平連續色塊的 <rect>。"""
    w = len(grid[0])
    out = []
    for r, row in enumerate(grid):
        assert len(row) == w, "row %d width %d != %d -> %r" % (r, len(row), w, row)
        c = 0
        while c < w:
            ch = row[c]
            color = LEGEND.get(ch)
            if color is None:
                c += 1
                continue
            run = 1
            while c + run < w and row[c + run] == ch:
                run += 1
            out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>'
                       % (c + x0, r + y0, run, color))
            c += run
    return "".join(out)


def group(gid, grid, x0=0, y0=0):
    return '<g id="%s">%s</g>' % (gid, to_rects(grid, x0, y0))


# 組裝 sprite：尾巴(後) → 身體 → 手臂 → 眨眼眼皮(前)
TAIL_SVG = group("tail", TAIL, x0=13, y0=8)
BASE_SVG = '<g id="base">%s</g>' % to_rects(BASE)
ARM_SVG = group("arm", ARM, x0=0, y0=4)
# 眨眼眼皮：蓋在兩眼上的 cream 方塊 + 一條深色睫毛線
LIDS_SVG = (
    '<g id="lids">'
    '<rect x="4" y="6" width="2" height="2" fill="#f7ecdc"/>'
    '<rect x="12" y="6" width="2" height="2" fill="#f7ecdc"/>'
    '<rect x="4" y="7" width="2" height="1" fill="#8f3f1e"/>'
    '<rect x="12" y="7" width="2" height="1" fill="#8f3f1e"/>'
    '</g>'
)

SPRITE = (
    '<svg class="panda" viewBox="0 0 24 22" width="216" height="198" '
    'shape-rendering="crispEdges" aria-label="像素風小熊貓吉祥物" role="img">'
    '<g id="panda">' + TAIL_SVG + BASE_SVG + ARM_SVG + LIDS_SVG + '</g></svg>'
)

CSS = """
:root{
  --cream:#f5efe2; --rust:#b5552d; --rust-dark:#8f3f1e; --amber:#e8a13c;
  --ink:#3a2317; --line:#e3d8c4;
  --dur:1.3s;                      /* 16 格 sprite 的主時脈 */
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{
  background:#e9e1d1;
  display:flex;align-items:center;justify-content:center;padding:24px;
  font-family:ui-sans-serif,-apple-system,"Hiragino Maru Gothic ProN","PingFang TC",sans-serif;
  color:var(--ink);
}
/* ── 舞台：16:9 letterbox，奶油底 + 紙紋 ───────────────────── */
.stage{
  position:relative;width:min(100%,940px);aspect-ratio:16/9;overflow:hidden;
  background:var(--cream);border-radius:18px;
  box-shadow:0 18px 50px rgba(58,35,23,.18), inset 0 0 0 1px rgba(58,35,23,.06);
}
.stage::before{                    /* 紙紋 grain */
  content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
  background:
    radial-gradient(rgba(58,35,23,.05) 1px,transparent 1px) 0 0/4px 4px,
    radial-gradient(rgba(58,35,23,.04) 1px,transparent 1px) 2px 2px/4px 4px;
  mix-blend-mode:multiply;
}
.stage::after{                     /* 暈影 */
  content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(120% 90% at 60% 40%,transparent 55%,rgba(58,35,23,.10));
}
/* ── 頂列 mono ─────────────────────────────────────────────── */
.topbar{
  position:absolute;top:0;left:0;right:0;z-index:5;
  display:flex;justify-content:space-between;align-items:center;
  padding:16px 22px;font-family:ui-monospace,Menlo,monospace;
  font-size:11px;letter-spacing:.18em;color:rgba(58,35,23,.62);text-transform:uppercase;
}
.rec{display:inline-flex;align-items:center;gap:6px;color:var(--rust)}
.rec b{width:7px;height:7px;border-radius:50%;background:var(--rust);
  animation:recblink 1.1s steps(2,end) infinite}
@keyframes recblink{50%{opacity:.15}}
/* ── 左下文字堆疊（flow，避免重疊）+ 大數字焦點 ─────────────── */
.headline{position:absolute;left:7%;bottom:9%;z-index:4;
  display:flex;flex-direction:column;max-width:50%}
.kicker{font-weight:800;font-size:clamp(20px,3.4vw,30px);
  color:var(--ink);letter-spacing:.02em;margin-bottom:2px}
.bignum{position:relative;line-height:.8;
  font-family:"Times New Roman",Georgia,serif;font-weight:800;
  font-size:clamp(58px,13vw,128px);color:var(--rust);
  letter-spacing:-.04em;text-shadow:3px 3px 0 rgba(58,35,23,.12);
  animation:glitch var(--dur) steps(16) infinite;}
.bignum span{
  position:absolute;inset:0;color:var(--amber);mix-blend-mode:multiply;
  clip-path:inset(40% 0 30% 0);animation:scan 2.4s steps(8) infinite;}
@keyframes glitch{0%,86%,100%{transform:translateX(0)}90%{transform:translateX(-2px)}94%{transform:translateX(2px)}}
@keyframes scan{0%{clip-path:inset(0 0 92% 0)}100%{clip-path:inset(92% 0 0 0)}}
.unit{font-family:ui-monospace,Menlo,monospace;font-size:11px;letter-spacing:.22em;
  color:rgba(58,35,23,.55);text-transform:uppercase;margin-top:4px}
/* ── sprite ───────────────────────────────────────────────── */
.sprite-wrap{position:absolute;right:11%;bottom:16%;z-index:3;
  filter:drop-shadow(0 10px 0 rgba(58,35,23,.10))}
.panda{display:block;image-rendering:pixelated}
#panda{animation:bob calc(var(--dur)*.6) steps(8) infinite alternate}
#arm{transform-box:fill-box;transform-origin:60% 86%;
  animation:wave var(--dur) steps(16) infinite alternate}
#tail{transform-box:fill-box;transform-origin:10% 76%;
  animation:sway calc(var(--dur)*1.3) steps(16) infinite alternate}
#lids{transform-box:fill-box;transform-origin:50% 0;
  animation:blink 4.2s infinite}
@keyframes bob{from{transform:translateY(0)}to{transform:translateY(-3px)}}
@keyframes wave{from{transform:rotate(-11deg)}to{transform:rotate(17deg)}}
@keyframes sway{from{transform:rotate(-5deg)}to{transform:rotate(6deg)}}
@keyframes blink{0%,93%,100%{transform:scaleY(0)}96%{transform:scaleY(1)}}
/* 飄落葉子（背景氛圍）*/
.leaf{position:absolute;top:-12px;width:9px;height:9px;border-radius:2px 7px 2px 7px;
  background:var(--amber);opacity:.0;z-index:2;animation:fall 7s linear infinite}
.leaf:nth-child(2){left:24%;background:var(--rust);animation-delay:1.4s;animation-duration:8.5s}
.leaf:nth-child(3){left:38%;animation-delay:3.1s;animation-duration:9.2s}
.leaf:nth-child(4){left:70%;background:var(--rust-dark);animation-delay:.6s;animation-duration:7.8s}
.leaf:nth-child(5){left:82%;animation-delay:2.2s}
@keyframes fall{0%{transform:translateY(0) rotate(0);opacity:0}
  8%{opacity:.85}92%{opacity:.85}100%{transform:translateY(360px) rotate(220deg);opacity:0}}
/* 動感假名 */
.kana{position:absolute;right:8%;bottom:60%;z-index:4;writing-mode:vertical-rl;
  font-weight:800;font-size:clamp(22px,3vw,30px);color:var(--rust-dark);letter-spacing:.1em;
  animation:kana var(--dur) steps(16) infinite alternate}
@keyframes kana{from{transform:translateY(0);opacity:.55}to{transform:translateY(-8px);opacity:1}}
/* 說明 caption */
.caption{margin:14px 0 0;max-width:42ch;
  font-family:ui-monospace,Menlo,monospace;font-size:12px;line-height:1.6;
  color:rgba(58,35,23,.66)}
/* 底部跑馬燈 ribbon */
.ribbon{position:absolute;left:0;right:0;bottom:0;z-index:5;overflow:hidden;
  border-top:1px solid var(--line);background:rgba(245,239,226,.82);
  backdrop-filter:blur(2px);padding:7px 0}
.ribbon .track{display:inline-flex;gap:26px;white-space:nowrap;padding-left:100%;
  font-family:ui-monospace,Menlo,monospace;font-size:11px;letter-spacing:.16em;
  color:rgba(58,35,23,.6);text-transform:uppercase;
  animation:roll 22s linear infinite}
.ribbon .track b{color:var(--rust)}
@keyframes roll{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){
  *{animation:none!important}
  #lids{transform:scaleY(0)}
}
"""

RIBBON_ITEMS = ("桃花 · キキ · フランケン · シンファ · あこ · 紫陽 · もみじ · "
                "ハナビ · こはく · ゆうた · ")

HTML = (
    "<!doctype html>\n<html lang=\"zh-Hant\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
    "<title>像素風吉祥物 · 16 格動畫</title>\n"
    "<style>" + CSS + "</style>\n</head>\n<body>\n"
    "<main class=\"stage\" data-od-id=\"stage\">\n"
    "  <div class=\"topbar\">\n"
    "    <span>RED&nbsp;PANDA&nbsp;ずかん</span>\n"
    "    <span class=\"rec\">FRAME 01 / 16 &nbsp; <b></b> REC</span>\n"
    "  </div>\n"
    "  <span class=\"leaf\"></span><span class=\"leaf\"></span>"
    "<span class=\"leaf\"></span><span class=\"leaf\"></span><span class=\"leaf\"></span>\n"
    "  <div class=\"headline\">\n"
    "    <div class=\"kicker\">小熊貓圖鑑</div>\n"
    "    <div class=\"bignum\" data-od-id=\"year\">365<span>365</span></div>\n"
    "    <div class=\"unit\">個體 · INDIVIDUALS</div>\n"
    "    <p class=\"caption\" data-od-id=\"caption\">像素風吉祥物。整段動畫是全 CSS 的 16 格循環，"
    "無 JS、無外部圖檔，所以每一格都穩定一致、不會走樣。</p>\n"
    "  </div>\n"
    "  <div class=\"kana\" data-od-id=\"kana\">もふもふ</div>\n"
    "  <div class=\"sprite-wrap\" data-od-id=\"sprite\">" + SPRITE + "</div>\n"
    "  <div class=\"ribbon\" data-od-id=\"ribbon\"><div class=\"track\">"
    + ("<span>" + RIBBON_ITEMS.replace(" · ", "</span><span>·</span><span>") + "</span>") * 2 +
    "</div></div>\n"
    "</main>\n</body>\n</html>\n"
)


# ── 16 格 contact sheet（把揮手循環的每一格烘成靜態 sprite）─────────
def sprite_static(arm_deg, tail_deg, bob, blink):
    """把某一格的姿勢烘進 transform 屬性（無動畫），用來證明每格穩定一致。"""
    tail = '<g transform="rotate(%g 13.9 17.12)">%s</g>' % (tail_deg, to_rects(TAIL, 13, 8))
    base = to_rects(BASE)
    arm = '<g transform="rotate(%g 3.6 11.74)">%s</g>' % (arm_deg, to_rects(ARM, 0, 4))
    lids = LIDS_SVG if blink else ""
    inner = '<g transform="translate(0 %g)">%s%s%s%s</g>' % (bob, tail, base, arm, lids)
    return ('<svg viewBox="0 0 24 22" width="118" height="108" shape-rendering="crispEdges">'
            + inner + "</svg>")


def build_frames_html():
    cells = []
    for k in range(16):
        t = k / 15.0
        arm = -11 + 28 * t                       # 揮手：-11° → 17°
        tail = -5 + 11 * t                        # 尾巴擺動
        bob = -3 * (1 - abs(2 * t - 1))           # 三角形上下浮動，中間最高
        blink = k in (12, 13)                     # 接近尾端眨一下眼
        cells.append(
            '<figure class="cell"><span class="fnum">%02d</span>%s</figure>'
            % (k + 1, sprite_static(arm, tail, round(bob, 2), blink)))
    css = """
    body{margin:0;background:#e9e1d1;color:#3a2317;
      font-family:ui-monospace,Menlo,monospace;padding:26px}
    h1{font-family:ui-sans-serif,-apple-system,sans-serif;font-size:18px;margin:0 0 4px}
    p{font-size:12px;color:rgba(58,35,23,.6);margin:0 0 18px}
    .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:760px}
    .cell{position:relative;margin:0;background:#f5efe2;border-radius:12px;
      display:flex;align-items:center;justify-content:center;padding:8px 0 4px;
      box-shadow:inset 0 0 0 1px rgba(58,35,23,.06)}
    .cell svg{image-rendering:pixelated}
    .fnum{position:absolute;top:6px;left:8px;font-size:10px;letter-spacing:.12em;
      color:rgba(58,35,23,.45)}
    """
    return ("<!doctype html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>16 格揮手循環</title><style>" + css + "</style></head><body>"
            "<h1>小熊貓吉祥物 · 16 格揮手循環</h1>"
            "<p>每一格都是確定性的 SVG（pixel rect），全 CSS steps(16) 播放。順讀再逆讀即為完整揮手。</p>"
            "<div class=\"grid\">" + "".join(cells) + "</div></body></html>")


def main():
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HTML)
    print("✅ wrote", os.path.relpath(OUT, ROOT), len(HTML), "bytes")
    frames_path = os.path.join(ROOT, "web", "public", "mascot-frames.html")
    with open(frames_path, "w", encoding="utf-8") as f:
        f.write(build_frames_html())
    print("✅ wrote", os.path.relpath(frames_path, ROOT))
    print("   預覽: http://localhost:4321/lesser-panda/mascot-lab.html")
    print("   16格: http://localhost:4321/lesser-panda/mascot-frames.html")


if __name__ == "__main__":
    main()
