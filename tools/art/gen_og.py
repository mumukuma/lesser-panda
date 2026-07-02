#!/usr/bin/env python3
"""生成全站 social media OG 圖（1200×630）→ web/public/img/og.png

用網站現有素材（天空漸層配色、森林圖層、吉祥物）＋三語站名。
需要 Pillow 與 Noto Sans CJK（沙盒 /usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc）。
非 rebuild 管線的一部分，改了素材或站名才需要重跑。
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "web/public/img"
OUT = IMG / "og.png"

W, H = 1200, 630

# 網站配色（global.css :root）
SKY_TOP = (207, 227, 238)   # --sky-2
SKY_BOT = (253, 248, 242)   # --bg
INK = (61, 44, 35)          # --ink
INK_SOFT = (122, 106, 95)   # --ink-soft
RUST_DARK = (143, 63, 30)   # --rust-dark

FONT_TTC = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"


def cjk_font(size: int, family: str = "Noto Sans CJK TC") -> ImageFont.FreeTypeFont:
    """從 ttc 找指定 family 的 index。"""
    for i in range(20):
        try:
            f = ImageFont.truetype(FONT_TTC, size, index=i)
        except OSError:
            break
        if f.getname()[0] == family:
            return f
    raise RuntimeError(f"{family} not found in {FONT_TTC}")


def main() -> None:
    im = Image.new("RGB", (W, H), SKY_BOT)
    # 天空垂直漸層（上 sky-2 → 下 bg，52% 處收斂，同 .forest-bg .sky）
    px = im.load()
    for y in range(H):
        t = min(y / (H * 0.52), 1.0)
        c = tuple(round(a + (b - a) * t) for a, b in zip(SKY_TOP, SKY_BOT))
        for x in range(W):
            px[x, y] = c

    # 森林圖層（半透明，襯底）
    for name, alpha, scale in (("bg-trees.webp", 90, 1.0), ("bg-foreground.webp", 140, 1.0)):
        layer = Image.open(IMG / name).convert("RGBA")
        w = round(W * scale)
        h = round(layer.height * w / layer.width)
        layer = layer.resize((w, h), Image.LANCZOS)
        a = layer.getchannel("A").point(lambda v: v * alpha // 255)
        layer.putalpha(a)
        im.paste(layer, ((W - w) // 2, H - h + 120), layer)

    # 吉祥物（右側）
    mascot = Image.open(IMG / "mascot.webp").convert("RGBA")
    mh = 540
    mw = round(mascot.width * mh / mascot.height)
    mascot = mascot.resize((mw, mh), Image.LANCZOS)
    im.paste(mascot, (W - mw - 90, H - mh - 30), mascot)

    # 文字（左側，三語站名 + 網域）
    d = ImageDraw.Draw(im)
    x = 84
    d.text((x, 150), "小熊貓圖鑑", font=cjk_font(96, "Noto Sans CJK TC"), fill=INK)
    d.text((x, 278), "レッサーパンダ図鑑", font=cjk_font(58, "Noto Sans CJK JP"), fill=INK)
    d.text((x, 368), "Red Panda Encyclopedia", font=cjk_font(40, "Noto Sans CJK TC"), fill=RUST_DARK)
    d.text((x, 452), "ressapanda.com", font=cjk_font(30, "Noto Sans CJK TC"), fill=INK_SOFT)

    im.save(OUT, optimize=True)
    print(OUT, im.size, f"{OUT.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
