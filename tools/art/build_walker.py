#!/usr/bin/env python3
"""
build_walker.py — 產生「2 格側面走路」小熊貓 sprite，並輸出乾淨對齊的 2 格 sheet。

走路動畫的主運動是「水平位移」(CSS translateX，完全不抖)；只有兩條腿在 2 格間交替，
小尺寸 + 眼睛在追橫向移動，所以不會有之前逐格重繪的 boil 問題。

流程：gpt-image-1 生一張「左右並排 2 格側面走路」(透明) → 依透明空隙切兩格 →
各自去邊、底部對齊(腳踩同一基線)、上半身水平對齊(身體不位移、只擺腿) → 併成緊密 2 格 sheet。

用法：
  python3 tools/art/build_walker.py            # 生圖 + 切格
  python3 tools/art/build_walker.py --skip-gen # 用 art-src/walk-raw.png 重切
輸出：web/public/img/walk-sheet.webp（2 格）、art-src/walk-raw.png（原圖）、
      art-src/walk-contact.png（對齊檢視）
"""
import base64
import io
import json
import os
import sys
import urllib.request
import urllib.error
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, "art-src")
IMG = os.path.join(ROOT, "web", "public", "img")
GEN_API = "https://api.openai.com/v1/images/generations"

PROMPT = (
    "A simple 2-frame side-view walk-cycle sprite of ONE cute kawaii red panda "
    "(Ailurus) mascot. The two frames are placed side by side with a clear empty gap "
    "between them. BOTH frames show the EXACT SAME character in profile facing RIGHT: "
    "identical head, rounded body, fluffy ringed tail, size, and colors. The ONLY "
    "difference between the two frames is the legs mid-stride: in the LEFT frame the "
    "front leg reaches forward while the back leg pushes behind; in the RIGHT frame the "
    "stride is reversed (the other leg forward). Natural walking posture, body roughly "
    "horizontal, looking ahead to the right, the visible legs clearly drawn. Soft "
    "children's-book illustration, smooth rounded shapes, warm rust-orange (#b5552d) and "
    "cream (#f5e9d9) fur, darker rings on the fluffy tail, honey-amber (#e8a13c) accents, "
    "one big round friendly eye, rosy cheek. The character sits on the SAME ground "
    "baseline in both frames (feet aligned), same width and height per frame. No grid "
    "lines, no numbers, no text, no drop shadow, no ground line. Transparent background."
)


def load_key():
    env = os.path.join(ROOT, ".env")
    if os.path.exists(env):
        for line in open(env, encoding="utf-8"):
            s = line.strip()
            if s.startswith("export "):
                s = s[7:]
            if s.startswith("OPENAI_API_KEY") and "=" in s:
                return s.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("OPENAI_API_KEY")


def generate():
    key = load_key()
    if not key:
        print("✗ no OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    payload = {
        "model": "gpt-image-1", "prompt": PROMPT, "size": "1536x1024",
        "quality": "high", "output_format": "png", "background": "transparent", "n": 1,
    }
    req = urllib.request.Request(
        GEN_API, data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    print("→ gpt-image-1 生 2 格走路 (透明) …", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=420) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print("✗ HTTP %d: %s" % (e.code, e.read().decode()[:400])); sys.exit(3)
    os.makedirs(ART, exist_ok=True)
    raw = os.path.join(ART, "walk-raw.png")
    with open(raw, "wb") as f:
        f.write(base64.b64decode(data["data"][0]["b64_json"]))
    print("✅ %s (%d KB)" % (os.path.relpath(raw, ROOT), os.path.getsize(raw) // 1024))
    return raw


def alpha_bbox(im, thr=24):
    return im.split()[3].point(lambda v: 255 if v > thr else 0).getbbox()


def find_split(im, thr=24):
    """central band 找最空的整欄當切點，容忍角色未置中。"""
    a = im.split()[3]
    w, h = im.size
    px = a.load()
    col = []
    for x in range(w):
        s = 0
        for y in range(0, h, 4):
            if px[x, y] > thr:
                s += 1
        col.append(s)
    lo, hi = int(w * 0.38), int(w * 0.62)
    best, bx = 1 << 30, w // 2
    for x in range(lo, hi):
        if col[x] < best:
            best, bx = col[x], x
    return bx


def webp(im, q=90):
    b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6); return b.getvalue()


def slice_align(raw):
    src = Image.open(raw).convert("RGBA")
    W, H = src.size
    sx = find_split(src)
    halves = [src.crop((0, 0, sx, H)), src.crop((sx, 0, W, H))]
    frames = []
    for half in halves:
        bb = alpha_bbox(half)
        if not bb:
            print("✗ 某格是空的，看 art-src/walk-raw.png", file=sys.stderr); sys.exit(2)
        frames.append(half.crop(bb))
    pad = 12
    cw = max(f.width for f in frames)
    chh = max(f.height for f in frames)
    CELLW, CELLH = cw + 2 * pad, chh + 2 * pad
    sheet = Image.new("RGBA", (CELLW * 2, CELLH), (0, 0, 0, 0))
    contact = Image.new("RGBA", (CELLW * 2, CELLH), (245, 233, 217, 255))
    for i, f in enumerate(frames):
        fa = f.split()[3]
        fw, fh = f.size
        top = fa.crop((0, 0, fw, max(1, int(fh * 0.5)))).getbbox()  # 上半身水平中心
        cx = (top[0] + top[2]) // 2 if top else fw // 2
        ox = i * CELLW + (CELLW // 2 - cx)
        oy = CELLH - pad - fh                                       # 底部對齊：腳踩同基線
        sheet.alpha_composite(f, (ox, oy))
        contact.alpha_composite(f, (ox, oy))
    cpx = contact.load()
    for y in range(CELLH):
        cpx[CELLW, y] = (181, 85, 45, 90)
    # 螢幕上僅約 54px 寬，把 sheet 降到「單格 ~170px」(留 ~3× retina 餘裕)，避免幾百 KB
    TARGET_CELL = 170
    if CELLW > TARGET_CELL:
        sh = max(1, round(CELLH * TARGET_CELL / CELLW))
        sheet = sheet.resize((TARGET_CELL * 2, sh), Image.LANCZOS)
    os.makedirs(IMG, exist_ok=True)
    with open(os.path.join(IMG, "walk-sheet.webp"), "wb") as f:
        f.write(webp(sheet, 86))
    contact.convert("RGB").save(os.path.join(ART, "walk-contact.png"))
    print("✅ walk-sheet.webp  cell %dx%d → 出圖 %dx%d  sheet %dx%d" % (
        CELLW, CELLH, sheet.width // 2, sheet.height, sheet.width, sheet.height))
    print("   檢視 art-src/walk-contact.png（中線=切點，兩格腳應同基線、身體同位置）")
    print("   per-cell aspect = %.3f (宽:高)" % (CELLW / CELLH))


def main():
    raw = os.path.join(ART, "walk-raw.png") if "--skip-gen" in sys.argv else generate()
    slice_align(raw)


if __name__ == "__main__":
    main()
