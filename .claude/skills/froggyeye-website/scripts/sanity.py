#!/usr/bin/env python3
"""Audit current site state — print one row per app showing presence of key assets and meta."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT

def y(b): return "✓" if b else "·"

apps = load_apps()
print(f"{'FOLDER':22s} {'PAGE':5s} {'ICON':5s} {'FEAT':5s} {'SHOT':5s} {'APPL':5s} {'PLAY':5s} {'LDJS':5s} {'STBR':5s}")
print("-" * 80)
for a in apps:
    f = a["folder"]
    d = SITE_ROOT / f
    page = (d / "index.html").exists()
    icon = (d / "icon.png").exists()
    feat = (d / "feature.png").exists()
    shot = (d / "screenshot1.png").exists()
    apple = bool(a.get("apple_url"))
    play = bool(a.get("play_url"))
    ldjs = stbr = False
    if page:
        text = (d / "index.html").read_text()
        ldjs = "application/ld+json" in text
        stbr = "studio-bar" in text
    print(f"{f:22s} {y(page):5s} {y(icon):5s} {y(feat):5s} {y(shot):5s} {y(apple):5s} {y(play):5s} {y(ldjs):5s} {y(stbr):5s}")

print("\nMain site files:")
for name in ["index.html", "sitemap.xml", "robots.txt", "llms.txt", "icons/logo.png", "icons/logo-full.png"]:
    p = SITE_ROOT / name
    print(f"  {y(p.exists())} {name}")
