#!/usr/bin/env python3
"""
wiki_io.py — wiki/*.md 共用讀取層（frontmatter 解析、日期正規化）

背景（2026-07-13 重構）：原本 build_db.py、audit.py、ig_audit.py 各自實作
frontmatter 解析，邊角行為（引號、inline list、空值）不一致，稽核工具看到的
資料可能與建檔工具不同。本模組抽出單一實作，各工具一律 import 這裡：

    from wiki_io import parse_frontmatter, read_frontmatter, norm_date

注意：gen_residence.py 與 apply_lineage_fixes.py 因需「保留原文格式的
surgical edit」（regex 定位後最小改寫），其寫入邏輯不經過本模組；
但任何「唯讀解析」新工具都應該用這裡，勿再自造 parser。
"""

from __future__ import annotations  # 相容舊版 Python

from pathlib import Path


# ── YAML frontmatter parser（不依賴 PyYAML）────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """返回 (frontmatter_dict, body)。無 frontmatter 則回傳 ({}, text)。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    return _parse_simple_yaml(yaml_block), body


def _parse_simple_yaml(yaml_text: str) -> dict:
    """最小化 YAML parser，支援：scalar、quoted scalar、inline list、block list。"""
    result: dict = {}
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # 跳過空行與純縮排
        if not line.strip() or line.startswith("  "):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()

        # inline list: [a, b, c]（空清單 [] 要解析為 []，不可變成 [""]）
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            items = [s.strip().strip('"').strip("'") for s in inner.split(",")] if inner else []
            result[key] = items
            i += 1
            continue

        # block list：接下來行以 "  - " 開頭
        if rest == "":
            block_items = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("  - "):
                block_items.append(lines[j][4:].strip())
                j += 1
            if block_items:
                result[key] = block_items
                i = j
                continue

        # scalar
        result[key] = rest.strip('"').strip("'")
        i += 1
    return result


def read_frontmatter(path: Path | str) -> dict:
    """讀檔並解析 frontmatter（唯讀工具常用的便利版；不需要 body 時用這個）。"""
    fm, _ = parse_frontmatter(Path(path).read_text(encoding="utf-8"))
    return fm


# ── 日期正規化 ─────────────────────────────────────────────────
def norm_date(s):
    """YYYY/M/D、YYYY-M-D 等 → YYYY-MM-DD；只有年份原樣回傳；空值回 None。"""
    if not s:
        return None
    s = str(s).replace("/", "-")
    parts = s.split("-")
    if len(parts) == 3:
        return f"{int(parts[0]):04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    return s  # 只有年份
