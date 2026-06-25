#!/usr/bin/env python3
"""
slice_sheet.py — 把生成的 4x4 sprite sheet 切格 → 去邊 → 對齊 → 重組成「乾淨 sheet」。

生圖 sheet 的硬傷是各格 drift（位置/大小不一）。這支用 PIL 修正：
  每格依 alpha 邊界裁出主體 → 底部對齊（腳不動）、身體水平置中 → 貼回固定 256 格。
重組後是完美對齊的網格，background-position steps() 就不會跳。

用法：python3 tools/art/slice_sheet.py mascot-sheet-1
輸出：art-src/<name>-clean.png（透明，乾淨 sheet）
      art-src/<name>-contact.png（疊奶油底，給人看的對齊檢視圖）
"""
import os
import sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, "art-src")
CELL = 256
MARGIN = 14
CREAM = (245, 233, 217, 255)


def process(name, cols=4, rows=4):
    src = Image.open(os.path.join(ART, name + ".png")).convert("RGBA")
    W, H = src.size
    cw, ch = W // cols, H // rows
    clean = Image.new("RGBA", (cols * CELL, rows * CELL), (0, 0, 0, 0))
    placed = 0
    for i in range(cols * rows):
        r, c = divmod(i, cols)
        # 內縮 3px 切，避開模型畫的格線
        cell = src.crop((c * cw + 3, r * ch + 3, c * cw + cw - 3, r * ch + ch - 3))
        alpha = cell.split()[3]
        # 若整格幾乎不透明（image-2 opaque），改用亮度去背：把接近奶油底的像素視為背景
        if alpha.getextrema()[0] > 200:
            cell = chroma_drop(cell)
            alpha = cell.split()[3]
        bbox = alpha.getbbox()
        if not bbox:
            continue
        fg = cell.crop(bbox)
        fw, fh = fg.size
        fa = fg.split()[3]
        # 身體水平中心：取下半部 (腳/身體) 的 alpha 邊界，避免被舉起的手臂帶偏
        low = fa.crop((0, int(fh * 0.55), fw, fh)).getbbox()
        cx = (low[0] + low[2]) // 2 if low else fw // 2
        # 太大才縮，維持模型原本畫的尺寸一致性
        max_wh = CELL - 2 * MARGIN
        s = min(1.0, max_wh / fh, max_wh / fw)
        if s < 1.0:
            fg = fg.resize((max(1, int(fw * s)), max(1, int(fh * s))), Image.LANCZOS)
            fw, fh = fg.size
            cx = int(cx * s)
        ox = c * CELL + (CELL // 2 - cx)
        oy = r * CELL + (CELL - MARGIN - fh)        # 底部對齊
        clean.alpha_composite(fg, (max(c * CELL, ox), oy))
        placed += 1
    out = os.path.join(ART, name + "-clean.png")
    clean.save(out)
    # 檢視圖：疊奶油底 + 細格線
    contact = Image.new("RGBA", clean.size, CREAM)
    contact.alpha_composite(clean)
    px = contact.load()
    for k in range(1, cols):
        for y in range(contact.size[1]):
            px[k * CELL, y] = (58, 35, 23, 40)
    for k in range(1, rows):
        for x in range(contact.size[0]):
            px[x, k * CELL] = (58, 35, 23, 40)
    contact.convert("RGB").save(os.path.join(ART, name + "-contact.png"))
    print("✅ placed %d/16 → %s" % (placed, os.path.relpath(out, ROOT)))
    print("   檢視：", os.path.relpath(os.path.join(ART, name + "-contact.png"), ROOT))


def chroma_drop(im, tol=26):
    """把接近四角平均色（奶油底）的像素設為透明，給 opaque 的 image-2 用。"""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    corners = [px[1, 1], px[w - 2, 1], px[1, h - 2], px[w - 2, h - 2]]
    br = sum(c[0] for c in corners) // 4
    bg_ = sum(c[1] for c in corners) // 4
    bb = sum(c[2] for c in corners) // 4
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if abs(r - br) <= tol and abs(g - bg_) <= tol and abs(b - bb) <= tol:
                px[x, y] = (r, g, b, 0)
    return im


if __name__ == "__main__":
    process(sys.argv[1] if len(sys.argv) > 1 else "mascot-sheet-1")
