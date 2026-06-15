#!/usr/bin/env python3
"""
gen_sprite.py — 用 OpenAI 生成「16 格揮手 sprite sheet」（一張圖內 4×4 格）。

用法（repo 根目錄）：
  python3 tools/gen_sprite.py                  # 預設 gpt-image-2
  python3 tools/gen_sprite.py gpt-image-1 sheet1
  python3 tools/gen_sprite.py gpt-image-2 sheet2

會先嘗試透明背景；若該 model 不支援（HTTP 400），自動改為不透明並回報。
原圖存到 art-src/<out>.png（gitignore），以便檢視與後續切格。
"""
import base64
import json
import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "art-src")
API = "https://api.openai.com/v1/images/generations"

PROMPT = (
    "A 4x4 grid sprite sheet containing EXACTLY 16 frames of ONE single cute kawaii "
    "red panda (Ailurus) mascot, read left to right then top to bottom. The SAME "
    "character appears in every one of the 16 cells: identical face, body, size, "
    "fluffy ringed tail, colors and standing position, perfectly centered inside each "
    "cell with identical framing. The ONLY thing that changes from frame to frame is "
    "the right arm, animating one smooth friendly WAVE cycle across the 16 frames "
    "(frame 1 arm lowered at the side, gradually raising, frames 7-10 raised high and "
    "waving, then lowering back down by frame 16). Soft children's-book illustration, "
    "rounded shapes, warm rust orange (#b5552d) and cream (#f5e9d9) fur, honey amber "
    "(#e8a13c) accents, big round friendly eyes, rosy cheeks. Even, regular grid "
    "spacing; every cell exactly the same width and height; no visible grid lines, "
    "no numbers, no text, no drop shadows. Clean flat background."
)


def load_key():
    env = os.path.join(ROOT, ".env")
    if os.path.exists(env):
        for line in open(env, encoding="utf-8"):
            line = line.strip()
            if line.startswith("export "):
                line = line[7:]
            if line.startswith("OPENAI_API_KEY") and "=" in line:
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("OPENAI_API_KEY")


def call(model, transparent, key):
    payload = {
        "model": model, "prompt": PROMPT, "size": "1024x1024",
        "quality": "high", "output_format": "png", "n": 1,
    }
    if transparent:
        payload["background"] = "transparent"
    req = urllib.request.Request(
        API, data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": "Bearer " + key,
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=420) as r:
        return json.load(r)


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "gpt-image-2"
    out = sys.argv[2] if len(sys.argv) > 2 else "mascot-sheet"
    key = load_key()
    if not key:
        print("✗ no OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    os.makedirs(ART, exist_ok=True)
    transparent = True
    print("→ %s 透明背景嘗試中 …" % model, flush=True)
    try:
        data = call(model, True, key)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", "replace")
        if e.code == 400 and "transparent" in msg.lower():
            print("  ! 此 model 不支援透明背景，改用不透明重試 …", flush=True)
            transparent = False
            try:
                data = call(model, False, key)
            except urllib.error.HTTPError as e2:
                print("✗ HTTP %d: %s" % (e2.code, e2.read().decode()[:400])); sys.exit(3)
        else:
            print("✗ HTTP %d: %s" % (e.code, msg[:400])); sys.exit(3)
    path = os.path.join(ART, out + ".png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(data["data"][0]["b64_json"]))
    kb = os.path.getsize(path) // 1024
    print("✅ %s (%d KB) — 透明背景=%s" % (os.path.relpath(path, ROOT), kb, transparent))


if __name__ == "__main__":
    main()
