#!/usr/bin/env python3
"""
edit_image.py — 用 OpenAI images/edits 以現有圖為底改一個動作（保持角色一致 + 透明）。
用法：python3 tools/edit_image.py <來源png> <輸出名> "<edit prompt>"
"""
import json
import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "web", "public", "img")
API_URL = "https://api.openai.com/v1/images/edits"


def load_key():
    env = os.path.join(ROOT, ".env")
    for line in open(env, encoding="utf-8"):
        line = line.strip()
        if line.startswith("OPENAI_API_KEY"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("OPENAI_API_KEY")


def multipart(fields, file_field, file_path):
    boundary = "----pandaboundary7studio"
    parts = []
    for k, v in fields.items():
        parts.append(("--" + boundary + "\r\n"
                      'Content-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (k, v)).encode())
    with open(file_path, "rb") as f:
        data = f.read()
    head = ("--" + boundary + "\r\n"
            'Content-Disposition: form-data; name="%s"; filename="%s"\r\n'
            "Content-Type: image/png\r\n\r\n" % (file_field, os.path.basename(file_path)))
    parts.append(head.encode() + data + b"\r\n")
    parts.append(("--" + boundary + "--\r\n").encode())
    return b"".join(parts), boundary


def main():
    src, out, prompt = sys.argv[1], sys.argv[2], sys.argv[3]
    key = load_key()
    body, boundary = multipart(
        {"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024",
         "quality": "high", "background": "transparent", "n": "1"},
        "image", src)
    req = urllib.request.Request(API_URL, data=body, method="POST", headers={
        "Authorization": "Bearer " + key,
        "Content-Type": "multipart/form-data; boundary=" + boundary,
    })
    print("  → editing %s -> %s ..." % (os.path.basename(src), out), flush=True)
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.load(resp)
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode()[:400]); sys.exit(3)
    import base64
    path = os.path.join(OUT_DIR, out + ".png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(d["data"][0]["b64_json"]))
    print("    OK", os.path.relpath(path, ROOT), os.path.getsize(path) // 1024, "KB")


if __name__ == "__main__":
    main()
