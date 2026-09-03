#!/usr/bin/env python3
"""Validate front matter and internal links of the docs source without running Jekyll.

Checks, for every Markdown page in the collections and the language/section index pages:
  * front matter present, with title/order/description on collection pages (nothing else)
  * every {{ '/…' | relative_url }} link and every plain "/en/…" or "/de/…" link resolves to a
    page that exists (permalink derived from collection + file name, or an index page)
  * anchors (#…) on internal links exist as a heading in the target page (kramdown ids)
  * every referenced /assets/… file exists
  * every EN page has a DE counterpart with the same slug and vice versa
Exit status 1 on any finding.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "de")
SECTIONS = ("tutorials", "how-to", "reference", "explanation")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"""\{\{\s*'(/[^']*)'\s*\|\s*relative_url\s*\}\}|href="(/(?:en|de)/[^"#]*)(#[^"]*)?"|\]\((/(?:en|de)/[^)#]*)(#[^)]*)?\)""")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.M)

problems: list[str] = []


def kramdown_id(text: str) -> str:
    # kramdown "auto_ids": strip formatting, lowercase, drop punctuation, spaces -> hyphens.
    t = re.sub(r"`([^`]*)`", r"\1", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_]", "", t)
    t = unicodedata.normalize("NFC", t).lower()
    t = re.sub(r"[^\w\s-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"^[-0-9]+", "", t)  # kramdown drops leading digits/hyphens
    return t or "section"


def page_url(path: Path) -> str | None:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    m = re.match(r"_(en|de)-(tutorials|how-to|reference|explanation)$", parts[0])
    if m:
        return f"/{m.group(1)}/{m.group(2)}/{path.stem}/"
    if len(parts) >= 2 and parts[0] in LANGS and parts[-1] == "index.md":
        return "/" + "/".join(parts[:-1]) + "/"
    if rel == Path("index.md"):
        return "/"
    return None


pages: dict[str, Path] = {}
for md in ROOT.rglob("*.md"):
    if any(p.startswith((".", "_site", "vendor", "node_modules")) for p in md.relative_to(ROOT).parts):
        continue
    if md.name == "README.md":
        continue
    url = page_url(md)
    if url:
        pages[url] = md

headings: dict[str, set[str]] = {}
for url, md in pages.items():
    body = md.read_text(encoding="utf-8")
    fm = FM_RE.match(body)
    if not fm:
        problems.append(f"{md}: missing front matter")
        continue
    keys = [ln.split(":", 1)[0].strip() for ln in fm.group(1).splitlines() if ":" in ln]
    if md.relative_to(ROOT).parts[0].startswith("_"):
        missing = {"title", "order", "description"} - set(keys)
        extra = set(keys) - {"title", "order", "description"}
        if missing:
            problems.append(f"{md}: front matter lacks {sorted(missing)}")
        if extra:
            problems.append(f"{md}: front matter has extra keys {sorted(extra)} (layout/section/lang come from _config.yml)")
    content = body[fm.end():]
    headings[url] = {kramdown_id(h) for _, h in HEAD_RE.findall(content)}

for url, md in pages.items():
    body = md.read_text(encoding="utf-8")
    for m in LINK_RE.finditer(body):
        target = m.group(1) or m.group(2) or m.group(4)
        anchor = m.group(3) or m.group(5)
        if target is None:
            continue
        if target.startswith("/assets/"):
            if not (ROOT / target.lstrip("/")).is_file():
                problems.append(f"{md}: missing asset {target}")
            continue
        base, _, frag = target.partition("#")
        if not anchor and frag:
            anchor = "#" + frag
        if base not in pages:
            problems.append(f"{md}: broken link {target}")
            continue
        if anchor:
            aid = anchor[1:]
            if aid not in headings.get(base, set()):
                problems.append(f"{md}: anchor {anchor} not found in {base} (have: {sorted(headings.get(base, set()))[:8]}…)")

# language parity
for url in list(pages):
    for a, b in (("/en/", "/de/"), ("/de/", "/en/")):
        if url.startswith(a) and url.replace(a, b, 1) not in pages:
            problems.append(f"{pages[url]}: no {b.strip('/')} counterpart at {url.replace(a, b, 1)}")

# unused assets
used = set()
for md in pages.values():
    used.update(re.findall(r"/assets/([^'\"\s]+)", md.read_text(encoding="utf-8")))
for asset in sorted((ROOT / "assets").glob("*")):
    if asset.name not in used:
        problems.append(f"assets/{asset.name}: not referenced by any page")

if problems:
    print("\n".join(problems))
    print(f"\n{len(problems)} problem(s)")
    sys.exit(1)
print(f"ok: {len(pages)} pages, {len(used)} assets, all internal links and anchors resolve")
