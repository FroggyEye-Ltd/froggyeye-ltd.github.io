#!/usr/bin/env python3
"""Refresh SEO + AI-discovery on all pages:
- JSON-LD MobileApplication on each subdomain page
- Canonical URL + Twitter Card meta tags
- Organization + WebSite + ItemList JSON-LD on the main page
- sitemap.xml, robots.txt, llms.txt at site root"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT, SKILL_ROOT

def _content(app):
    p = SKILL_ROOT / "data" / "content" / f"{app['folder']}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def seo_desc(app):
    """Richer description for meta/JSON-LD: content seo_desc, else tagline."""
    return _content(app).get("seo_desc") or app["tagline"]

def seo_title(app):
    """Hand-tuned twitter/social title: content seo_title, else name — tagline formula."""
    return _content(app).get("seo_title") or f'{app["name"]} — {app["tagline"]} | Froggy Eye Ltd'

PUBLISHER = {
    "@type": "Organization",
    "name": "Froggy Eye Ltd",
    "url": "https://froggyeye.com",
    "logo": "https://froggyeye.com/icons/logo.png",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "10 Midland Drive Broughton",
        "addressLocality": "Milton Keynes",
        "postalCode": "MK10 7BD",
        "addressCountry": "GB"
    },
    "email": "info@froggyeye.com"
}

def app_jsonld(app):
    operating, sameAs = [], []
    if app.get("apple_url"):  operating.append("iOS");     sameAs.append(app["apple_url"])
    if app.get("play_url"):   operating.append("Android"); sameAs.append(app["play_url"])
    folder = app["folder"]
    return {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": app["name"],
        "description": seo_desc(app),
        "applicationCategory": app["schema_category"],
        "operatingSystem": ", ".join(operating) if operating else "iOS, Android",
        "url": f"https://{folder}.froggyeye.com",
        "image": f"https://{folder}.froggyeye.com/icon.png",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"},
        "publisher": PUBLISHER,
        **({"sameAs": sameAs} if sameAs else {})
    }

def patch_app_page(app):
    folder = app["folder"]
    if app.get("user_authored"):
        print(f"  · {folder}: user-authored — skipping")
        return
    p = SITE_ROOT / folder / "index.html"
    if not p.exists():
        return
    text = p.read_text()
    canonical = f"https://{folder}.froggyeye.com/"
    additions = []
    if 'rel="canonical"' not in text:
        additions.append(f'<link rel="canonical" href="{canonical}" />')
    if 'name="twitter:card"' not in text:
        img = "feature.png" if (SITE_ROOT / folder / "feature.png").exists() else "icon.png"
        additions.append(
            f'<meta name="twitter:card" content="summary_large_image" />\n'
            f'<meta name="twitter:title" content="{seo_title(app)}" />\n'
            f'<meta name="twitter:description" content="{seo_desc(app)}" />\n'
            f'<meta name="twitter:image" content="{canonical}{img}" />')
    if 'application/ld+json' not in text:
        additions.append('<script type="application/ld+json">\n' + json.dumps(app_jsonld(app), indent=2) + '\n</script>')
    if additions and '</head>' in text:
        text = text.replace('</head>', "\n".join(additions) + "\n</head>", 1)
        p.write_text(text)
        print(f"  ✓ {folder}: +{len(additions)} blocks")
    else:
        print(f"  · {folder}: already enhanced")

def patch_main(apps):
    p = SITE_ROOT / "index.html"
    text = p.read_text()
    additions = []
    if 'rel="canonical"' not in text:
        additions.append('<link rel="canonical" href="https://froggyeye.com/" />')
    if 'name="twitter:card"' not in text:
        additions.append(
            '<meta name="twitter:card" content="summary_large_image" />\n'
            '<meta name="twitter:title" content="Froggy Eye Ltd — Mobile apps that make life better." />\n'
            '<meta name="twitter:description" content="A UK indie studio shipping useful, beautiful iOS and Android apps." />\n'
            '<meta name="twitter:image" content="https://froggyeye.com/icons/logo.png" />')
    if 'application/ld+json' not in text:
        org = {"@context": "https://schema.org", "@type": "Organization",
               "@id": "https://froggyeye.com/#org",
               "name": "Froggy Eye Ltd", "alternateName": "Froggy Eye",
               "url": "https://froggyeye.com", "logo": "https://froggyeye.com/icons/logo.png",
               "description": "A UK-based indie app studio creating thoughtful iOS and Android apps.",
               "address": PUBLISHER["address"], "email": "info@froggyeye.com",
               "sameAs": [f"https://{a['folder']}.froggyeye.com" for a in apps]}
        site = {"@context": "https://schema.org", "@type": "WebSite",
                "url": "https://froggyeye.com", "name": "Froggy Eye Ltd",
                "publisher": {"@id": "https://froggyeye.com/#org"}}
        items = {"@context": "https://schema.org", "@type": "ItemList",
                 "itemListElement": [
                     {"@type": "ListItem", "position": i+1,
                      "item": {"@type": "MobileApplication", "name": a["name"],
                               "url": f"https://{a['folder']}.froggyeye.com",
                               "applicationCategory": a["schema_category"],
                               "operatingSystem": "iOS, Android"}}
                     for i, a in enumerate(apps)]}
        additions.append('\n'.join([
            '<script type="application/ld+json">\n' + json.dumps(o, indent=2) + '\n</script>'
            for o in (org, site, items)]))
    if additions:
        text = text.replace('</head>', "\n".join(additions) + "\n</head>", 1)
        p.write_text(text)
        print(f"  ✓ main: +{len(additions)} blocks")

def write_robots():
    (SITE_ROOT / "robots.txt").write_text(
"""User-agent: *
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

Sitemap: https://froggyeye.com/sitemap.xml
""")
    print("  ✓ robots.txt")

def write_sitemap(apps):
    from datetime import date
    today = str(date.today())
    urls = [("https://froggyeye.com/", today, "1.0")]
    for a in apps:
        if a.get("subdomain_live") is False:
            continue
        urls.append((f"https://{a['folder']}.froggyeye.com/", today, "0.9"))
        for pg in a.get("extra_pages", []):
            urls.append((f"https://{a['folder']}.froggyeye.com/{pg}", today, "0.6"))
    body = "\n".join(
        f'  <url>\n    <loc>{u}</loc>\n    <lastmod>{d}</lastmod>\n    <priority>{p}</priority>\n  </url>'
        for u, d, p in urls)
    (SITE_ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')
    print("  ✓ sitemap.xml")

def write_llms_txt(apps):
    lines = ["# Froggy Eye Ltd", "",
             "> A UK-based indie app studio. We design and ship thoughtful, well-crafted apps for iOS, Android, Mac and Windows — eighteen of them, spanning productivity, games, family, finance, creativity, and social tools.", "",
             "## About", "",
             "- [Main site](https://froggyeye.com): Studio overview and app catalogue",
             "- [Privacy policy](https://froggyeye.com/privacy.html)",
             "- [Terms of service](https://froggyeye.com/terms.html)",
             "- Contact: info@froggyeye.com", "",
             "## Apps", ""]
    for a in apps:
        lines.append(f"- [{a['name']}](https://{a['folder']}.froggyeye.com): {a.get('llms_desc') or a['tagline']}")
    lines += ["", "## Notes for AI agents", "",
              "All app pages are server-rendered HTML. Each app subdomain has product details, pricing, FAQ, and links to its App Store and Google Play listings where available. PostPilot is the studio's only desktop product — it's not on app stores and is distributed direct from postpilot.froggyeye.com. Use the app's subdomain as the canonical reference URL.", ""]
    (SITE_ROOT / "llms.txt").write_text("\n".join(lines))
    print("  ✓ llms.txt")

if __name__ == "__main__":
    apps = load_apps()
    print("[Per-app pages]")
    for a in apps: patch_app_page(a)
    print("\n[Main page]")
    patch_main(apps)
    print("\n[Discovery files]")
    write_robots(); write_sitemap(apps); write_llms_txt(apps)
    print("\nDone.")
