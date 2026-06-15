#!/usr/bin/env python3
"""
build_puppet.py — 剪紙 / puppet rig：靜態身體 + 獨立手臂，手臂繞肩膀旋轉揮手。

零抖原理：身體是同一批像素永遠不重繪；手臂是一張剛體圖只做 CSS 旋轉 → 沒有逐格生圖 → 無 boil。

手臂用 AI 切出來後尺寸/位置不可靠，所以這裡把手臂裁到自己的 bbox，再用 CSS 參數
(ARM_W/ARM_L/ARM_T/PIV) 手動擺到肩膀上、設定旋轉樞紐。調這四個值即可對位。

輸出：puppet-body.webp / puppet-arm.webp、puppet-demo.html、.puppet-widget.html
"""
import base64
import io
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "web", "public", "img")

# ── 手動擺位參數（相對 .puppet 寬度）──────────────────────────
ARM_W = 28      # 手臂寬 = 身體寬的 %
ARM_L = 2       # 手臂左邊距 %
ARM_T = 20      # 手臂上邊距 %
PIV = "52% 88%"  # 旋轉樞紐（手臂底部≈肩/腕）
ROT_A, ROT_B = -6, 14   # 揮手擺動角度


def tight(im, thr=24):
    return im.split()[3].point(lambda v: 255 if v > thr else 0).getbbox()


def webp(im, q=88):
    b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6); return b.getvalue()


def main():
    body = Image.open(os.path.join(IMG, "mascot-body.png")).convert("RGBA")
    arm = Image.open(os.path.join(IMG, "mascot-arm-only.png")).convert("RGBA")
    bb, ab = tight(body), tight(arm)

    TH = 320
    bodyc = body.crop((max(0, bb[0] - 8), max(0, bb[1] - 8), bb[2] + 8, bb[3] + 8))
    bw, bh = bodyc.size
    W, H = int(bw * TH / bh), TH
    bodyc = bodyc.resize((W, H), Image.LANCZOS)

    armc = arm.crop((max(0, ab[0] - 4), max(0, ab[1] - 4), ab[2] + 4, ab[3] + 4))
    aw, ah = armc.size
    armc = armc.resize((int(aw * 300 / ah), 300), Image.LANCZOS)

    with open(os.path.join(IMG, "puppet-body.webp"), "wb") as f:
        f.write(webp(bodyc))
    with open(os.path.join(IMG, "puppet-arm.webp"), "wb") as f:
        f.write(webp(armc))

    css = (
        ".puppet{position:relative}.puppet .pb{display:block;width:100%;height:auto}"
        ".puppet .pa{position:absolute;width:__AW__%;height:auto;left:__AL__%;top:__AT__%;"
        "transform-origin:__PIV__;animation:pwave 1.7s ease-in-out infinite}"
        "@keyframes pwave{0%,100%{transform:rotate(__RA__deg)}50%{transform:rotate(__RB__deg)}}"
        "@media(prefers-reduced-motion:reduce){.puppet .pa{animation:none;transform:rotate(5deg)}}"
    ).replace("__AW__", str(ARM_W)).replace("__AL__", str(ARM_L)).replace("__AT__", str(ARM_T)) \
     .replace("__PIV__", PIV).replace("__RA__", str(ROT_A)).replace("__RB__", str(ROT_B))

    base = "/lesser-panda/img/"
    demo = (
        "<!doctype html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>puppet rig 揮手</title><style>"
        "body{margin:0;min-height:100%;background:#e9e1d1;display:flex;align-items:center;"
        "justify-content:center;padding:40px}"
        ".card{position:relative;width:440px;height:340px;background:#f5efe2;border-radius:20px;"
        "display:flex;align-items:flex-end;justify-content:center;box-shadow:0 18px 50px rgba(58,35,23,.18)}"
        ".puppet{position:relative;width:270px;margin-bottom:14px}" + css +
        "</style></head><body><div class=\"card\"><div class=\"puppet\">"
        "<img class=\"pb\" src=\"" + base + "puppet-body.webp\" alt=\"\">"
        "<img class=\"pa\" src=\"" + base + "puppet-arm.webp\" alt=\"\">"
        "</div></div></body></html>"
    )
    with open(os.path.join(ROOT, "web", "public", "puppet-demo.html"), "w", encoding="utf-8") as f:
        f.write(demo)

    sw = int(W * 150 / H)
    bsmall = bodyc.resize((sw, 150), Image.LANCZOS)
    asmall = armc.resize((int(armc.width * 150 / armc.height), 150), Image.LANCZOS)
    bd = "data:image/webp;base64," + base64.b64encode(webp(bsmall, 78)).decode()
    ad = "data:image/webp;base64," + base64.b64encode(webp(asmall, 78)).decode()
    widget = (
        "<style>.wstage{display:flex;justify-content:center;padding:1rem 0}"
        ".wcard{position:relative;width:min(100%,420px);height:250px;background:#f5efe2;"
        "border-radius:16px;overflow:hidden;display:flex;align-items:flex-end;justify-content:center;"
        "box-shadow:inset 0 0 0 1px rgba(58,35,23,.07)}"
        ".badge{position:absolute;left:6%;top:9%;font-family:ui-monospace,Menlo,monospace;font-size:11px;"
        "letter-spacing:.1em;color:#b5552d;background:rgba(181,85,45,.1);padding:3px 9px;border-radius:999px}"
        ".puppet{position:relative;width:" + str(sw) + "px;margin-bottom:16px}" + css +
        "</style><div class=\"wstage\"><div class=\"wcard\"><div class=\"badge\">puppet rig · 零 boil</div>"
        "<div class=\"puppet\"><img class=\"pb\" src=\"" + bd + "\" alt=\"\">"
        "<img class=\"pa\" src=\"" + ad + "\" alt=\"\"></div></div></div>"
    )
    with open(os.path.join(ROOT, "web", ".puppet-widget.html"), "w", encoding="utf-8") as f:
        f.write(widget)

    print("✅ body %dx%d, arm %dx%d" % (W, H, armc.width, armc.height))
    print("   擺位 ARM_W=%d ARM_L=%d ARM_T=%d PIV=%s rot=%d..%d" % (ARM_W, ARM_L, ARM_T, PIV, ROT_A, ROT_B))
    print("   demo: http://localhost:4321/lesser-panda/puppet-demo.html")


if __name__ == "__main__":
    main()
