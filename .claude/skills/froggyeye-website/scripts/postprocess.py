#!/usr/bin/env python3
"""Post-process generated promo pages:
1. Replace generic phone-screen contents with full-bleed screenshot (where one exists).
2. Insert feature-banner section under hero.
3. Replace href="#" placeholders with real Apple/Play URLs from data/apps.json.
4. Hide buttons whose URL is null."""
import re, sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT, parse_only_arg

BANNER = (
    '\n<section class="feature-banner-section" style="padding: 0 0 64px 0;">\n'
    '  <div class="wrap">\n'
    '    <div class="feature-banner reveal" style="max-width: 720px; margin: 0 auto; border-radius: var(--r-xl); overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,0.4); border: 1px solid var(--border);">\n'
    '      <img src="feature.png" alt="" style="width:100%; height:auto; display:block;">\n'
    '    </div>\n'
    '  </div>\n'
    '</section>\n'
)

def patch(app):
    folder = app["folder"]
    if app.get("user_authored"):
        print(f"  {folder}: user-authored — skipping postprocess")
        return
    p = SITE_ROOT / folder / "index.html"
    if not p.exists():
        print(f"  {folder}: no index.html, skipping")
        return
    text = p.read_text()

    # 1. Full-bleed screenshot in phone mockup
    if (SITE_ROOT / folder / "screenshot1.png").exists():
        new_screen = (
            '<div class="phone-screen" style="padding:0; background:#000;">'
            '<img src="screenshot1.png" alt="App screenshot" style="width:100%; height:100%; object-fit:cover; display:block;">'
            '</div>'
        )
        text = re.sub(
            r'<div class="phone-screen">[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*</header>',
            new_screen + '\n    </div>\n  </div>\n</header>',
            text, count=1)

    # 2. Feature banner
    if (SITE_ROOT / folder / "feature.png").exists() and 'feature-banner' not in text:
        text = text.replace('<div class="marquee"', BANNER + '<div class="marquee"', 1)

    # 3. Store URLs
    apple = app.get("apple_url")
    play  = app.get("play_url")

    def patch_apple_btn(match):
        block = match.group(0)
        if apple:
            return block.replace('href="#"', f'href="{apple}" target="_blank" rel="noopener"', 1)
        return block.replace('href="#"', 'href="#" data-na="appstore" onclick="return false;"', 1)

    def patch_play_btn(match):
        block = match.group(0)
        if play:
            return block.replace('href="#"', f'href="{play}" target="_blank" rel="noopener"', 1)
        return block.replace('href="#"', 'href="#" data-na="playstore" onclick="return false;"', 1)

    text = re.sub(
        r'<a class="store"[^>]*href="#"[^>]*>\s*<svg[^>]*viewBox="0 0 24 24"[^>]*>\s*<path[^/]*M17\.05[^>]*/>\s*</svg>\s*<div><div class="small">Download on the</div><div class="big">App Store</div></div>\s*</a>',
        patch_apple_btn, text, flags=re.DOTALL)
    text = re.sub(
        r'<a class="store"[^>]*href="#"[^>]*>\s*<svg[^>]*viewBox="0 0 24 24"[^>]*>\s*<defs>.*?</defs>\s*<path[^/]*/>\s*<path[^/]*/>\s*<path[^/]*/>\s*<path[^/]*/>\s*</svg>\s*<div><div class="small">GET IT ON</div><div class="big">Google Play</div></div>\s*</a>',
        patch_play_btn, text, flags=re.DOTALL)

    # 4. Hide-rule for missing-store buttons
    if 'a.store[data-na]' not in text:
        text = text.replace('</style>', 'a.store[data-na]{display:none !important;}</style>', 1)

    p.write_text(text)
    print(f"  ✓ {folder}: shot={'Y' if (SITE_ROOT/folder/'screenshot1.png').exists() else '-'}, feat={'Y' if (SITE_ROOT/folder/'feature.png').exists() else '-'}, apple={'Y' if apple else '-'}, play={'Y' if play else '-'}")

if __name__ == "__main__":
    only = parse_only_arg(sys.argv)
    for app in load_apps():
        if only and app["folder"] != only: continue
        patch(app)
