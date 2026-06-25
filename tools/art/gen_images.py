#!/usr/bin/env python3
"""
gen_images.py — 用 OpenAI gpt-image-1 生成網站可愛風素材。

讀取專案根目錄 .env 的 OPENAI_API_KEY，呼叫 images API，存成 PNG 到 web/public/img/。
零第三方相依（只用標準函式庫）。

用法（在 repo 根目錄）：
  python3 tools/art/gen_images.py mascot          # 跑單一 job
  python3 tools/art/gen_images.py mascot bg-sky    # 跑多個
  python3 tools/art/gen_images.py all              # 全部
  python3 tools/art/gen_images.py --list           # 列出 job
"""
import base64
import json
import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "web", "public", "img")
API_URL = "https://api.openai.com/v1/images/generations"

# 共用風格前綴：讓所有素材視覺一致（柔和、圓潤、繪本感、暖色森林）
STYLE = (
    "Soft kawaii children's-book illustration, gentle painterly shading, rounded shapes, "
    "cozy warm palette of rust orange (#b5552d), cream (#f5e9d9) and honey amber (#e8a13c) "
    "with soft forest green and sky-blue accents, clean edges, no text, no watermark, "
    "high quality, charming and friendly."
)

JOBS = {
    # 吉祥物：透明背景，hero + 品牌用
    "mascot": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A single adorable red panda (Ailurus) mascot, full body, "
        "standing and waving one paw, big round friendly eyes, fluffy ringed tail, "
        "centered, isolated on a transparent background, sticker-style with soft outline.",
    ),
    "mascot-peek": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A cute red panda peeking and hanging from a tree branch with "
        "green leaves, only upper body and paws visible, looking down curiously, "
        "isolated on a transparent background.",
    ),
    # 多層視差背景：天空（不透明底）→ 樹冠（透明）→ 前景葉（透明）
    "bg-sky": dict(
        size="1536x1024", quality="high", background="opaque",
        prompt=STYLE + " A wide dreamy forest sky background, soft gradient from warm "
        "cream at the horizon to gentle sky blue, a few fluffy rounded clouds and warm "
        "sun glow, very soft and out of focus, empty space in the middle, no characters.",
    ),
    "bg-trees": dict(
        size="1536x1024", quality="high", background="transparent",
        prompt=STYLE + " A horizontal band of soft rounded forest tree canopy and foliage "
        "silhouettes in muted green and amber, layered depth, occupying only the lower "
        "third, the rest fully transparent, no characters, isolated on transparent background.",
    ),
    "bg-foreground": dict(
        size="1536x1024", quality="high", background="transparent",
        prompt=STYLE + " Decorative foreground foliage framing the bottom-left and "
        "bottom-right corners only: big soft rounded leaves, ferns and a few bamboo shoots, "
        "the entire center and top fully transparent, isolated on transparent background.",
    ),
    "leaves": dict(
        size="1024x1024", quality="medium", background="transparent",
        prompt=STYLE + " A small set of 5 separate cute autumn leaves and one tiny green "
        "sprig, arranged with gaps between them, soft rounded shapes, isolated on a "
        "transparent background, sticker-style.",
    ),
    # 首頁四格統計圖示（簡潔、置中、透明背景，風格一致）
    "stat-individuals": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A simple clean icon of ONE cute red panda face, front view, "
        "big round friendly eyes, fluffy cheeks, centered with generous margin, "
        "isolated on a transparent background, sticker style, simple and iconic.",
    ),
    "stat-alive": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A simple clean icon of a fresh green bamboo shoot with two "
        "rounded sprout leaves, lively and growing, centered with generous margin, "
        "isolated on a transparent background, sticker style, simple and iconic.",
    ),
    "stat-zoo": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A simple clean icon of one small cozy cottage animal-house with "
        "a single rounded green tree beside it, warm and inviting, centered with generous "
        "margin, isolated on a transparent background, sticker style, simple and iconic.",
    ),
    "stat-family": dict(
        size="1024x1024", quality="high", background="transparent",
        prompt=STYLE + " A simple clean icon of two red pandas side by side, one bigger "
        "parent and one small baby, cute and affectionate, centered with generous margin, "
        "isolated on a transparent background, sticker style, simple and iconic.",
    ),
    # 吉祥物揮手 sprite strip：單張內 3 格同一隻熊貓（一次 render 鎖定身分），之後裁切做 CSS 循環
    "mascot-wave-strip": dict(
        size="1536x1024", quality="high", background="transparent",
        prompt="A horizontal sprite strip of EXACTLY 3 equally-spaced frames in a single row, "
        "left to right, all showing the SAME one cute kawaii red panda mascot in an identical "
        "standing pose and identical size and baseline, where ONLY the right arm position changes "
        "to animate a friendly wave: frame 1 the arm is lowered down at the side, frame 2 the arm "
        "is raised to shoulder height, frame 3 the arm is raised high and waving. Keep the face, "
        "body, tail and colors perfectly identical across all 3 frames, change nothing except the "
        "waving arm. Soft kawaii children's-book illustration, rounded shapes, warm rust orange "
        "(#b5552d) and cream fur, big round friendly eyes, fluffy ringed tail, even gaps between "
        "frames, each frame fully isolated on a transparent background, no text, no frame borders.",
    ),
}


def load_key():
    env = os.path.join(ROOT, ".env")
    if os.path.exists(env):
        with open(env, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("export "):
                    line = line[len("export "):]
                if "=" not in line:
                    continue
                k, v = line.split("=", 1)
                if k.strip() == "OPENAI_API_KEY":
                    return v.strip().strip('"').strip("'")
    return os.environ.get("OPENAI_API_KEY")


def generate(name, spec, key):
    body = json.dumps({
        "model": spec.get("model", "gpt-image-1"),
        "prompt": spec["prompt"],
        "size": spec["size"],
        "quality": spec.get("quality", "high"),
        "background": spec.get("background", "auto"),
        "output_format": "png",
        "n": 1,
    }).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=body, method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    print(f"  → 生成 {name} ({spec['size']}, {spec.get('quality','high')}) …", flush=True)
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.load(resp)
    b64 = data["data"][0]["b64_json"]
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name + ".png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
    kb = os.path.getsize(path) // 1024
    print(f"    ✅ {os.path.relpath(path, ROOT)} ({kb} KB)", flush=True)
    return path


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("--list", "-l"):
        print("可用 jobs：")
        for k, v in JOBS.items():
            print(f"  {k:16} {v['size']:10} {v.get('background','auto')}")
        return
    key = load_key()
    if not key:
        print("✗ 找不到 OPENAI_API_KEY（檢查 repo 根目錄 .env）", file=sys.stderr)
        sys.exit(1)
    print(f"金鑰已載入（…{key[-4:]}）", flush=True)
    names = list(JOBS) if args == ["all"] else args
    for n in names:
        if n not in JOBS:
            print(f"✗ 未知 job：{n}", file=sys.stderr)
            sys.exit(2)
    for n in names:
        try:
            generate(n, JOBS[n], key)
        except urllib.error.HTTPError as e:
            print(f"✗ HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}", file=sys.stderr)
            sys.exit(3)


if __name__ == "__main__":
    main()
