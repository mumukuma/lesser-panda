#!/usr/bin/env python3
"""
build_wave.py — 用「edits-from-master」產生的幾個手臂姿勢，組成平滑揮手動畫。

關鍵：所有 frame 都從同一張 master 編輯而來 → 身體鎖定、只有手臂動 → 不 shimmer。
本支把各姿勢以同一個 union bbox 對齊裁切（保證對齊）→ 匯出 webp，
並產生：
  web/public/img/wave-*.webp      網站/demo 用（透明，高度 300）
  web/public/wave-demo.html       可在瀏覽器打開看動畫
  web/.wave-widget.html           內嵌 data-uri 的小尺寸版（給 show_widget 用）
"""
import base64
import io
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, "art-src")
IMG = os.path.join(ROOT, "web", "public", "img")

POSES = [
    ("down", os.path.join(ART, "mascot-armdown.png")),
    ("mid",  os.path.join(IMG, "mascot-arm-mid.png")),
    ("up",   os.path.join(ART, "mascot.png")),
    ("out",  os.path.join(IMG, "mascot-arm-out.png")),
]
# 8 步循環：舉起 → 揮 → 放下
SEQ = ["down", "mid", "up", "out", "up", "out", "up", "mid"]
DUR = 1.8


def tight_bbox(im, thr=24):
    a = im.split()[3].point(lambda v: 255 if v > thr else 0)
    return a.getbbox()


def webp_bytes(im, q=88):
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=q, method=6)
    return buf.getvalue()


def main():
    ims = {k: Image.open(p).convert("RGBA") for k, p in POSES}
    boxes = [tight_bbox(im) for im in ims.values()]
    ux = min(b[0] for b in boxes); uy = min(b[1] for b in boxes)
    ux2 = max(b[2] for b in boxes); uy2 = max(b[3] for b in boxes)
    pad = 8
    box = (max(0, ux - pad), max(0, uy - pad), ux2 + pad, uy2 + pad)
    crop = {k: im.crop(box) for k, im in ims.items()}
    w, h = crop["down"].size

    def resized(th):
        tw = int(w * th / h)
        return {k: c.resize((tw, th), Image.LANCZOS) for k, c in crop.items()}, tw

    # 1) 網站尺寸 webp
    big, _ = resized(300)
    os.makedirs(IMG, exist_ok=True)
    for k, c in big.items():
        with open(os.path.join(IMG, "wave-%s.webp" % k), "wb") as f:
            f.write(webp_bytes(c))
    # 2) 小尺寸 data-uri（widget，壓到可內嵌）
    small, sw = resized(104)
    datauris = {k: "data:image/webp;base64," + base64.b64encode(webp_bytes(c, 52)).decode()
                for k, c in small.items()}

    # opacity keyframes：每格在它出現的 step 顯示
    steps = len(SEQ)
    css_kf = []
    layers = []
    for k in ["down", "mid", "up", "out"]:
        slots = [i for i, s in enumerate(SEQ) if s == k]
        stops = []
        for i in range(steps):
            v = 1 if i in slots else 0
            p0 = i * 100.0 / steps
            p1 = (i + 1) * 100.0 / steps - 0.01
            stops.append("%.2f%%{opacity:%d}" % (p0, v))
            stops.append("%.2f%%{opacity:%d}" % (p1, v))
        css_kf.append("@keyframes wv_%s{%s}" % (k, "".join(stops)))
        layers.append(
            '<img class="wv wv_%s" src="%s" alt="" width="%d" height="150" '
            'style="animation:wv_%s %ss steps(1,end) infinite">' % (k, datauris[k], sw, k, DUR))

    widget_tmpl = (
        "<style>\n"
        ".wave-stage{display:flex;justify-content:center;padding:1rem 0}\n"
        ".wave-card{position:relative;width:min(100%,420px);height:250px;background:#f5efe2;"
        "border-radius:16px;overflow:hidden;display:flex;align-items:flex-end;justify-content:center;"
        "box-shadow:inset 0 0 0 1px rgba(58,35,23,.07)}\n"
        ".wave-card .frames{position:relative;width:__SW__px;height:150px;margin-bottom:18px}\n"
        ".wv{position:absolute;left:0;bottom:0;image-rendering:auto}\n"
        ".badge{position:absolute;left:6%;top:9%;font-family:ui-monospace,Menlo,monospace;"
        "font-size:11px;letter-spacing:.1em;color:#b5552d;background:rgba(181,85,45,.1);"
        "padding:3px 9px;border-radius:999px}\n"
        "__KF__\n"
        "@media (prefers-reduced-motion:reduce){.wv{animation:none!important}.wv_up{opacity:1}}\n"
        "</style>\n"
        '<div class="wave-stage"><div class="wave-card">'
        '<div class="badge">edits-from-master · 透明</div>'
        '<div class="frames">__LAYERS__</div>'
        "</div></div>"
    )
    widget = (widget_tmpl.replace("__SW__", str(sw))
              .replace("__KF__", "\n".join(css_kf))
              .replace("__LAYERS__", "".join(layers)))

    with open(os.path.join(ROOT, "web", ".wave-widget.html"), "w", encoding="utf-8") as f:
        f.write(widget)

    # 3) URL demo（引用 webp 檔）
    demo_layers = "".join(
        '<img class="wv wv_%s" src="/lesser-panda/img/wave-%s.webp" alt="" '
        'style="animation:wv_%s %ss steps(1,end) infinite">' % (k, k, k, DUR)
        for k in ["down", "mid", "up", "out"])
    demo_tmpl = (
        "<!doctype html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>edits-from-master 揮手</title><style>"
        "body{margin:0;min-height:100%;background:#e9e1d1;display:flex;align-items:center;"
        "justify-content:center;padding:40px;font-family:ui-sans-serif,sans-serif}"
        ".card{position:relative;width:460px;height:330px;background:#f5efe2;border-radius:20px;"
        "display:flex;align-items:flex-end;justify-content:center;"
        "box-shadow:0 18px 50px rgba(58,35,23,.18)}"
        ".frames{position:relative;width:300px;height:300px;margin-bottom:14px}"
        ".wv{position:absolute;left:50%;bottom:0;transform:translateX(-50%);height:300px}"
        "__KF__"
        "@media (prefers-reduced-motion:reduce){.wv{animation:none!important}.wv_up{opacity:1}}"
        "</style></head><body><div class=\"card\"><div class=\"frames\">__LAYERS__</div></div></body></html>"
    )
    demo = demo_tmpl.replace("__KF__", "".join(css_kf)).replace("__LAYERS__", demo_layers)
    with open(os.path.join(ROOT, "web", "public", "wave-demo.html"), "w", encoding="utf-8") as f:
        f.write(demo)

    print("✅ frames:", ", ".join("wave-%s.webp(%dKB)" % (k, len(webp_bytes(c)) // 1024)
                                  for k, c in big.items()))
    print("   widget:", os.path.relpath(os.path.join(ROOT, "web", ".wave-widget.html"), ROOT),
          "(%d KB)" % (os.path.getsize(os.path.join(ROOT, "web", ".wave-widget.html")) // 1024))
    print("   demo: http://localhost:4321/lesser-panda/wave-demo.html")


if __name__ == "__main__":
    main()
