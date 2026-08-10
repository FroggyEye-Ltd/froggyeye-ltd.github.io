#!/usr/bin/env python3
"""Comprehensive search-engine + AI-agent discovery enhancement.

Adds, on top of seo_enhance.py:
1. Per-subdomain sitemap.xml, robots.txt, llms.txt
2. FAQPage JSON-LD (parses each page's <details>/<summary> FAQ)
3. BreadcrumbList JSON-LD
4. og:image:width / og:image:height / og:image:alt
5. 'More apps' internal cross-link section in subdomain footers
6. humans.txt + .well-known/security.txt at the main site
7. dns-prefetch hints for performance
"""
from html import escape as _esc
def esc(s): return _esc(s, quote=False)
import json, re, sys, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT

# --------------------------------------------------------------------- per subdomain helpers

def per_sub_sitemap(app):
    folder = app["folder"]
    extra = "".join(
        f'\n  <url><loc>https://{folder}.froggyeye.com/{pg}</loc><priority>0.6</priority></url>'
        for pg in app.get("extra_pages", []))
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://{folder}.froggyeye.com/</loc><priority>1.0</priority></url>
  <url><loc>https://{folder}.froggyeye.com/#how</loc><priority>0.7</priority></url>
  <url><loc>https://{folder}.froggyeye.com/#features</loc><priority>0.7</priority></url>
  <url><loc>https://{folder}.froggyeye.com/#pricing</loc><priority>0.8</priority></url>
  <url><loc>https://{folder}.froggyeye.com/#faq</loc><priority>0.6</priority></url>{extra}
</urlset>
'''

def per_sub_robots(folder):
    return f'''User-agent: *
Allow: /

User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://{folder}.froggyeye.com/sitemap.xml
Sitemap: https://froggyeye.com/sitemap.xml
'''

def per_sub_llms(app):
    folder = app["folder"]
    apple = app.get("apple_url") or "Not yet listed."
    play  = app.get("play_url")  or "Not yet listed."
    return f'''# {app["name"]}

> {app["tagline"]}. From Froggy Eye Ltd, a UK indie app studio.

## App information

- Category: {app["category"]}
- Studio: Froggy Eye Ltd ([https://froggyeye.com](https://froggyeye.com))
- App Store: {apple}
- Google Play: {play}

## About this app

{app["tagline"]}. Built by Froggy Eye Ltd in the United Kingdom.

## Other apps from the same studio

See [https://froggyeye.com](https://froggyeye.com) for the full catalogue (18 apps spanning productivity, games, family, finance, and creativity).

## Notes for AI agents

- All content on this page is server-rendered HTML (no JS gating)
- The canonical URL for this app is `https://{folder}.froggyeye.com/`
- Use the [App Store / Google Play links](#app-information) above for download
- For studio-level questions go to https://froggyeye.com/llms.txt
'''

# --------------------------------------------------------------------- FAQ extraction

FAQ_BLOCK = re.compile(
    r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<div class="answer"><p>(.*?)</p></div>\s*</details>',
    re.DOTALL,
)

def extract_faq(html):
    """Returns list of (question, answer) tuples found in <details>/<summary> blocks."""
    out = []
    for m in FAQ_BLOCK.finditer(html):
        q = re.sub(r'\s+', ' ', m.group(1)).strip()
        a = re.sub(r'\s+', ' ', m.group(2)).strip()
        # Strip HTML tags from a
        a = re.sub(r'<[^>]+>', '', a)
        if q and a:
            out.append((q, a))
    return out

def faqpage_jsonld(faqs):
    if not faqs:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

def breadcrumb_jsonld(app):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Froggy Eye Ltd", "item": "https://froggyeye.com/"},
            {"@type": "ListItem", "position": 2, "name": app["name"], "item": f"https://{app['folder']}.froggyeye.com/"},
        ],
    }

# --------------------------------------------------------------------- per-page patcher

def add_image_dims(text, folder):
    """Ensure og:image points to absolute feature.png URL with correct dimensions/alt."""
    # Fix relative og:image src first (legacy pages point at icon.png)
    text = text.replace(
        '<meta property="og:image" content="icon.png" />',
        f'<meta property="og:image" content="https://{folder}.froggyeye.com/feature.png" />',
        1,
    )
    if 'og:image:width' in text:
        return text
    block = (
        '<meta property="og:image:width" content="2048" />\n'
        '<meta property="og:image:height" content="1365" />\n'
        '<meta property="og:image:alt" content="Promotional banner for the app" />\n'
    )
    return text.replace('<meta property="og:image"', block + '<meta property="og:image"', 1)

def add_og_meta(text, folder):
    """Add og:url, og:site_name, og:locale if missing."""
    inject = []
    if 'og:url' not in text:
        inject.append(f'<meta property="og:url" content="https://{folder}.froggyeye.com/" />')
    if 'og:site_name' not in text:
        inject.append('<meta property="og:site_name" content="Froggy Eye Ltd" />')
    if 'og:locale' not in text:
        inject.append('<meta property="og:locale" content="en_GB" />')
    if not inject:
        return text
    block = '\n'.join(inject) + '\n'
    return text.replace('<meta property="og:type"', block + '<meta property="og:type"', 1)

def add_dns_prefetch(text):
    """Inject dns-prefetch hints to speed up first-paint of fonts & store assets."""
    if 'dns-prefetch' in text:
        return text
    block = (
        '<link rel="dns-prefetch" href="https://fonts.gstatic.com" />\n'
        '<link rel="dns-prefetch" href="https://fonts.googleapis.com" />\n'
        '<link rel="dns-prefetch" href="https://play-lh.googleusercontent.com" />\n'
        '<link rel="dns-prefetch" href="https://is1-ssl.mzstatic.com" />\n'
    )
    return text.replace('<link rel="preconnect"', block + '<link rel="preconnect"', 1)

def render_more_apps(this_app, all_apps):
    """Pick 3 sibling apps deterministically (avoids non-deterministic builds)."""
    siblings = [a for a in all_apps if a["folder"] != this_app["folder"]]
    # Pick 3 deterministic by hashing the folder name so each app always shows the same 3
    seed = sum(ord(c) for c in this_app["folder"])
    rng = random.Random(seed)
    chosen = rng.sample(siblings, 3)
    cards = []
    for a in chosen:
        g0, g1 = a["card_gradient"]
        cards.append(f'''      <a href="https://{a["folder"]}.froggyeye.com" class="more-card">
        <div class="more-card-art" style="background: linear-gradient(135deg, {g0}, {g1});">{a["card_emoji"]}</div>
        <div>
          <div class="more-card-title">{esc(a["name"])}</div>
          <div class="more-card-tag">{esc(a["tagline"])}</div>
        </div>
      </a>''')
    css = """
.more-apps { padding: 64px 0; background: var(--surface); }
.more-apps .wrap { text-align: center; }
.more-apps h3 { font-family: var(--font-display); font-size: clamp(22px, 3vw, 32px); margin-bottom: 32px; }
.more-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; max-width: 880px; margin: 0 auto; text-align: left; }
@media (max-width: 720px) { .more-grid { grid-template-columns: 1fr; } }
.more-card { display: flex; gap: 14px; align-items: center; background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 16px; transition: transform 200ms ease, border-color 200ms ease; color: inherit; text-decoration: none; }
.more-card:hover { transform: translateY(-2px); border-color: var(--magenta); }
.more-card-art { width: 48px; height: 48px; border-radius: 12px; display: grid; place-items: center; font-size: 22px; flex-shrink: 0; }
.more-card-title { font-family: var(--font-display); font-weight: 700; font-size: 15px; color: var(--text); }
.more-card-tag { font-size: 12px; color: var(--text-3); }
"""
    section = f'''
<section class="more-apps">
  <div class="wrap">
    <h3>More from <span class="gradient-text">Froggy Eye Ltd</span></h3>
    <div class="more-grid">
{chr(10).join(cards)}
    </div>
  </div>
</section>
'''
    return css, section

def patch_app(app, all_apps):
    folder = app["folder"]
    if app.get("user_authored"):
        print(f"  · {folder}: user-authored — leaving page and discovery files alone")
        return False
    p = SITE_ROOT / folder / "index.html"
    if not p.exists():
        return False
    text = p.read_text()

    # 1. og:image dimensions + og meta + dns-prefetch
    text = add_image_dims(text, folder)
    text = add_og_meta(text, folder)
    text = add_dns_prefetch(text)

    # 2. FAQPage + BreadcrumbList JSON-LD (only if not already present)
    additions = []
    if '@type": "FAQPage' not in text:
        faqs = extract_faq(text)
        ld = faqpage_jsonld(faqs)
        if ld:
            additions.append('<script type="application/ld+json">\n' + json.dumps(ld, indent=2) + '\n</script>')
    if '@type": "BreadcrumbList' not in text:
        additions.append('<script type="application/ld+json">\n' + json.dumps(breadcrumb_jsonld(app), indent=2) + '\n</script>')
    if additions:
        text = text.replace('</head>', "\n".join(additions) + "\n</head>", 1)

    # 3. More apps section + CSS
    if 'class="more-apps"' not in text:
        css, section = render_more_apps(app, all_apps)
        text = text.replace('</style>', css + '</style>', 1)
        # Insert before <footer
        text = re.sub(r'(<footer\b)', section + r'\1', text, count=1)

    p.write_text(text)

    # 4. Per-subdomain discovery files
    (SITE_ROOT / folder / "sitemap.xml").write_text(per_sub_sitemap(app))
    (SITE_ROOT / folder / "robots.txt").write_text(per_sub_robots(folder))
    (SITE_ROOT / folder / "llms.txt").write_text(per_sub_llms(app))
    return True

# --------------------------------------------------------------------- root-level files

def write_humans_txt():
    (SITE_ROOT / "humans.txt").write_text("""/* TEAM */
Studio: Froggy Eye Ltd
Site: https://froggyeye.com
Email: info@froggyeye.com
Location: Milton Keynes, United Kingdom

/* THANKS */
Thanks for visiting our site. Built with care.
""")

def write_security_txt():
    well_known = SITE_ROOT / ".well-known"
    well_known.mkdir(exist_ok=True)
    (well_known / "security.txt").write_text("""Contact: mailto:info@froggyeye.com
Expires: 2027-12-31T23:59:59Z
Preferred-Languages: en
Canonical: https://froggyeye.com/.well-known/security.txt
""")

def patch_main_image_dims():
    p = SITE_ROOT / "index.html"
    text = p.read_text()
    if 'og:image:width' not in text:
        block = (
            '<meta property="og:image" content="https://froggyeye.com/icons/logo-full.png" />\n'
            '<meta property="og:image:width" content="1024" />\n'
            '<meta property="og:image:height" content="1024" />\n'
            '<meta property="og:image:alt" content="Froggy Eye Ltd logo" />\n'
        )
        text = text.replace('<meta property="og:type"', block + '<meta property="og:type"', 1)
    text = add_dns_prefetch(text)
    p.write_text(text)

# --------------------------------------------------------------------- main

if __name__ == "__main__":
    apps = load_apps()
    print("[Per-subdomain enhancement]")
    for app in apps:
        ok = patch_app(app, apps)
        print(f"  {'✓' if ok else '·'} {app['folder']}")
    print("\n[Root-level files]")
    write_humans_txt();      print("  ✓ humans.txt")
    write_security_txt();    print("  ✓ .well-known/security.txt")
    patch_main_image_dims(); print("  ✓ main page og:image:width/height + dns-prefetch")
    print("\nDone.")
