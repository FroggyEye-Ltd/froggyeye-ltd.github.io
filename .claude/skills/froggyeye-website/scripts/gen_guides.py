#!/usr/bin/env python3
"""Render the ApexRoute road guides — a listing page plus one page per article.

Articles live in data/guides/<slug>.json as structured content (headings,
paragraphs, lists, road cards), never as raw HTML, so every page gets the same
markup and the same design tokens. Output goes to
public_html/apexroute/guides/.

Pages are self-contained: the CSS is inlined rather than linked, which is the
house pattern for every other page on this site and costs these pages nothing —
they are search landing pages, and a render-blocking stylesheet request is the
one thing they cannot afford.

Run:  python3 scripts/gen_guides.py [--only <slug>]
"""
import html as htmllib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import SKILL_ROOT, SITE_ROOT, load_apps

GUIDES_DIR = SKILL_ROOT / "data" / "guides"
OUT_DIR = SITE_ROOT / "apexroute" / "guides"
BASE = "https://apexroute.froggyeye.com"
GUIDES_URL = f"{BASE}/guides/"

APPLE_URL = "https://apps.apple.com/gb/app/apexroute/id6760571266"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.froggyeye.apexroute"

APPLE_BADGE = (
    '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 12.04c-.03-2.94 2.4-4.36 '
    '2.51-4.43-1.37-2-3.5-2.27-4.26-2.3-1.81-.18-3.54 1.07-4.46 1.07-.94 0-2.35-1.05-3.86-1.02-1.99.03-3.82 '
    '1.16-4.85 2.93-2.07 3.59-.53 8.9 1.49 11.81.99 1.43 2.16 3.03 3.7 2.97 1.49-.06 2.05-.96 3.85-.96 1.79 '
    '0 2.31.96 3.88.93 1.6-.03 2.62-1.45 3.6-2.89 1.13-1.66 1.6-3.27 1.62-3.36-.04-.02-3.11-1.2-3.14-4.74zM14.55 '
    '4.07c.82-1 1.37-2.39 1.22-3.77-1.18.05-2.62.79-3.46 1.78-.76.88-1.42 2.29-1.24 3.65 1.32.1 2.66-.67 '
    '3.48-1.66z"/></svg>'
    '<div><div class="small">Download on the</div><div class="big">App Store</div></div>')

PLAY_BADGE = (
    '<svg viewBox="0 0 24 24"><defs>'
    '<linearGradient id="gp1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00D8FF"/><stop offset="1" stop-color="#0085FF"/></linearGradient>'
    '<linearGradient id="gp2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFD200"/><stop offset="1" stop-color="#FF8A00"/></linearGradient>'
    '<linearGradient id="gp3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF3A44"/><stop offset="1" stop-color="#C31162"/></linearGradient>'
    '<linearGradient id="gp4" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00F076"/><stop offset="1" stop-color="#00A852"/></linearGradient>'
    '</defs>'
    '<path fill="url(#gp1)" d="M3.5 2.2v19.6c0 .5.6.8 1 .4l9.7-9.8L4.5 1.7c-.4-.3-1 0-1 .5z"/>'
    '<path fill="url(#gp2)" d="M17.6 9.7l-3.4-2-2.4 2.5 2.4 2.5 3.4-2c.7-.4.7-1.4 0-1.8z"/>'
    '<path fill="url(#gp3)" d="M14.2 14.7l-9.7 5.7c-.4.3-.9 0-1-.4l9.3-9.3 1.4 4z"/>'
    '<path fill="url(#gp4)" d="M14.2 9.3l-9.7-5.7c-.4-.3-.9 0-1 .4L4 5l8.8 6.8 1.4-2.5z"/></svg>'
    '<div><div class="small">GET IT ON</div><div class="big">Google Play</div></div>')

CSS = """
  :root {
    --primary: #FF4D2E; --primary-deep: #B81D00; --violet: #7C2D12;
    --mint: #FBBF24; --yellow: #FDE047;
    --bg: #0F0805; --surface: #1C0E08; --surface-2: #2A150E; --border: #3D2418;
    --text: #FFF5F0; --text-2: #D6B8A8; --text-3: #8A6B5A;
    --grad: linear-gradient(135deg, #FF4D2E 0%, #7C2D12 100%);
    --font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    --font-body: 'Inter', system-ui, -apple-system, sans-serif;
    --r-sm: 8px; --r-md: 12px; --r-lg: 20px; --r-xl: 28px; --r-pill: 999px;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: var(--font-body);
    font-size: 17px; line-height: 1.65; -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale; overflow-x: hidden;
    display: flex; flex-direction: column; min-height: 100vh; }
  img { max-width: 100%; display: block; }
  a { color: inherit; }
  ::selection { background: var(--primary); color: #fff; }
  .wrap { max-width: 780px; margin: 0 auto; padding: 0 24px; width: 100%; }
  .wrap-wide { max-width: 1080px; margin: 0 auto; padding: 0 24px; width: 100%; }

  .studio-bar { background: linear-gradient(90deg, #FF2E7E 0%, #7C3AED 100%); color: #fff;
    font-size: 13px; font-weight: 600; letter-spacing: 0.04em; text-align: center; padding: 8px 16px; }
  .studio-bar a { color: #fff; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; }
  .studio-bar a:hover { text-decoration: underline; }
  .studio-bar .arrow { display: inline-block; transition: transform 150ms ease; }
  .studio-bar a:hover .arrow { transform: translateX(-4px); }

  nav.top { border-bottom: 1px solid var(--border); background: rgba(15,8,5,0.85);
    backdrop-filter: saturate(140%) blur(14px); -webkit-backdrop-filter: saturate(140%) blur(14px);
    position: sticky; top: 0; z-index: 50; }
  nav.top .wrap-wide { display: flex; align-items: center; justify-content: space-between;
    padding-top: 14px; padding-bottom: 14px; }
  .brand { display: flex; align-items: center; gap: 12px; text-decoration: none; }
  .brand img { width: 34px; height: 34px; border-radius: 10px; }
  .brand-name { font-family: var(--font-display); font-weight: 700; font-size: 17px; letter-spacing: -0.01em; }
  .nav-links { display: flex; gap: 22px; align-items: center; }
  .nav-links a { color: var(--text-2); font-weight: 500; font-size: 14px; text-decoration: none; }
  .nav-links a:hover { color: var(--text); }
  @media (max-width: 620px) { .nav-links a.hide-sm { display: none; } }

  main { flex: 1 0 auto; padding: 56px 0 80px; }
  @media (max-width: 720px) { main { padding: 36px 0 56px; } }

  .eyebrow { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: 0.18em;
    text-transform: uppercase; color: var(--primary); margin-bottom: 14px; }
  h1 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.03em; line-height: 1.1;
    margin: 0 0 18px; font-size: clamp(30px, 5vw, 46px); }
  h2 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.2;
    margin: 52px 0 16px; font-size: clamp(23px, 3.2vw, 30px); }
  h3 { font-family: var(--font-display); font-weight: 600; letter-spacing: -0.01em;
    margin: 34px 0 10px; font-size: clamp(18px, 2.4vw, 21px); color: var(--text); }
  p { margin: 0 0 18px; color: var(--text-2); }
  a.inline, main p a, main li a { color: var(--mint); text-decoration: underline;
    text-underline-offset: 3px; text-decoration-thickness: 1px; }
  main p a:hover, main li a:hover { color: var(--primary); }
  .lead { font-size: clamp(18px, 2.1vw, 21px); color: var(--text); }
  .byline { color: var(--text-3); font-size: 14px; margin: 0 0 40px;
    padding-bottom: 24px; border-bottom: 1px solid var(--border); }
  ul, ol { color: var(--text-2); padding-left: 22px; margin: 0 0 20px; }
  li { margin-bottom: 9px; }
  strong { color: var(--text); font-weight: 600; }

  .road { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--primary);
    border-radius: var(--r-md); padding: 18px 20px; margin: 0 0 18px; }
  .road .road-name { font-family: var(--font-display); font-weight: 700; font-size: 18px;
    letter-spacing: -0.01em; margin-bottom: 3px; }
  .road .road-meta { font-size: 13px; color: var(--text-3); margin-bottom: 10px;
    letter-spacing: 0.02em; }
  .road p:last-child { margin-bottom: 0; }

  .note { background: var(--surface-2); border: 1px solid var(--border); border-radius: var(--r-md);
    padding: 16px 20px; margin: 0 0 22px; font-size: 15px; }
  .note p:last-child { margin-bottom: 0; }
  .note strong { color: var(--yellow); }

  .cta-box { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r-xl);
    padding: 30px 30px 34px; margin: 56px 0 0; }
  .cta-box h2 { margin-top: 0; font-size: clamp(21px, 2.8vw, 26px); }
  .stores { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; margin-top: 22px; }
  .store { display: inline-flex; align-items: center; gap: 12px; padding: 11px 18px; background: #000;
    border: 1px solid var(--border); border-radius: 14px; color: #fff; text-decoration: none;
    transition: transform 150ms ease, border-color 200ms ease; min-width: 176px; }
  .store:hover { transform: translateY(-2px); border-color: var(--primary); }
  .store svg { width: 26px; height: 26px; flex-shrink: 0; }
  .store .small { font-size: 11px; color: #c4c4cc; line-height: 1; margin-bottom: 4px; letter-spacing: 0.04em; }
  .store .big { font-family: var(--font-display); font-size: 18px; font-weight: 700; line-height: 1; }

  .more { margin: 56px 0 0; padding-top: 34px; border-top: 1px solid var(--border); }
  .more h2 { margin-top: 0; font-size: 20px; }
  .more-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
  @media (max-width: 660px) { .more-grid { grid-template-columns: 1fr; } }
  .more-card { display: block; background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--r-md); padding: 16px 18px; text-decoration: none; color: inherit;
    transition: transform 180ms ease, border-color 180ms ease; }
  .more-card:hover { transform: translateY(-2px); border-color: var(--primary); }
  .more-card .t { font-family: var(--font-display); font-weight: 700; font-size: 15px;
    line-height: 1.35; margin-bottom: 5px; }
  .more-card .d { font-size: 13px; color: var(--text-3); line-height: 1.5; }

  .list-hero { margin-bottom: 44px; }
  .card-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
  @media (max-width: 760px) { .card-grid { grid-template-columns: 1fr; } }
  .card { display: flex; flex-direction: column; background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--r-lg); padding: 24px; text-decoration: none; color: inherit;
    transition: transform 200ms ease, border-color 200ms ease; }
  .card:hover { transform: translateY(-3px); border-color: var(--primary); }
  .card .eyebrow { margin-bottom: 10px; }
  .card h2 { font-size: 20px; margin: 0 0 10px; line-height: 1.3; }
  .card p { font-size: 15px; margin: 0 0 14px; }
  .card .meta { margin-top: auto; font-size: 13px; color: var(--text-3); }

  footer { flex-shrink: 0; border-top: 1px solid var(--border); background: var(--surface); padding: 30px 0; }
  footer .wrap-wide { display: flex; flex-wrap: wrap; gap: 10px 24px; justify-content: space-between;
    align-items: center; color: var(--text-3); font-size: 13px; }
  footer a { color: var(--text-3); text-decoration: none; }
  footer a:hover { color: var(--text-2); }
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
         '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700'
         '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />')

STUDIO_BAR = ('<div class="studio-bar"><a href="https://froggyeye.com"><span class="arrow">←</span>'
              '<span>Part of <strong>Froggy Eye Ltd</strong> · See all our apps</span></a></div>')


def nav(depth_to_root="/"):
    return f'''<nav class="top">
  <div class="wrap-wide">
    <a class="brand" href="{depth_to_root}">
      <img src="/icon.png" alt="ApexRoute" width="34" height="34" />
      <span class="brand-name">ApexRoute</span>
    </a>
    <div class="nav-links">
      <a href="/guides/">Road guides</a>
      <a class="hide-sm" href="/#features">Features</a>
      <a href="/#get">Get the app</a>
    </div>
  </div>
</nav>'''


FOOTER = f'''<footer>
  <div class="wrap-wide">
    <span>© 2026 Froggy Eye Ltd · Registered in England &amp; Wales</span>
    <span><a href="/guides/">Road guides</a> · <a href="/privacy.html">Privacy</a> ·
      <a href="/terms.html">Terms</a> · <a href="mailto:info@froggyeye.com">info@froggyeye.com</a></span>
  </div>
</footer>'''


def inline(text):
    """Escape, then allow a deliberately tiny subset: [text](url) and **bold**."""
    t = htmllib.escape(text, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t


def render_block(b):
    if "p" in b:
        return f'      <p>{inline(b["p"])}</p>'
    if "lead" in b:
        return f'      <p class="lead">{inline(b["lead"])}</p>'
    if "h3" in b:
        return f'      <h3>{inline(b["h3"])}</h3>'
    if "ul" in b:
        items = "\n".join(f'        <li>{inline(x)}</li>' for x in b["ul"])
        return f'      <ul>\n{items}\n      </ul>'
    if "ol" in b:
        items = "\n".join(f'        <li>{inline(x)}</li>' for x in b["ol"])
        return f'      <ol>\n{items}\n      </ol>'
    if "note" in b:
        return f'      <div class="note"><p>{inline(b["note"])}</p></div>'
    if "road" in b:
        r = b["road"]
        meta = f'\n        <div class="road-meta">{inline(r["meta"])}</div>' if r.get("meta") else ""
        paras = "\n".join(f'        <p>{inline(x)}</p>' for x in r["text"])
        return (f'      <div class="road">\n        <div class="road-name">{inline(r["name"])}</div>'
                f'{meta}\n{paras}\n      </div>')
    raise ValueError(f"unknown block: {list(b)}")


def render_sections(sections):
    out = []
    for s in sections:
        if s.get("h2"):
            out.append(f'      <h2>{inline(s["h2"])}</h2>')
        for b in s["blocks"]:
            out.append(render_block(b))
    return "\n".join(out)


def cta(article):
    return f'''      <div class="cta-box">
        <h2>Drive these in ApexRoute</h2>
        <p>{inline(article["cta_note"])}</p>
        <p>ApexRoute is free to start, needs no account, and carries no ads or trackers —
          <a href="{BASE}">apexroute.froggyeye.com</a>.</p>
        <div class="stores">
          <a class="store" href="{APPLE_URL}" rel="noopener" aria-label="Download ApexRoute on the App Store">{APPLE_BADGE}</a>
          <a class="store" href="{PLAY_URL}" rel="noopener" aria-label="Get ApexRoute on Google Play">{PLAY_BADGE}</a>
        </div>
      </div>'''


def more_reading(article, all_articles):
    others = [a for a in all_articles if a["slug"] != article["slug"]]
    cards = "\n".join(
        f'''          <a class="more-card" href="/guides/{o["slug"]}.html">
            <div class="t">{inline(o["title"])}</div>
            <div class="d">{inline(o["card_blurb"])}</div>
          </a>''' for o in others)
    return f'''      <div class="more">
        <h2>More road guides</h2>
        <div class="more-grid">
{cards}
        </div>
      </div>'''


def article_jsonld(a):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["description"],
        "datePublished": a["published"],
        "dateModified": a["published"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f'{BASE}/guides/{a["slug"]}.html'},
        "author": {"@type": "Organization", "name": "Froggy Eye Ltd", "url": "https://froggyeye.com"},
        "publisher": {
            "@type": "Organization", "name": "Froggy Eye Ltd",
            "logo": {"@type": "ImageObject", "url": "https://froggyeye.com/icons/logo.png"},
        },
        "image": f"{BASE}/feature.png",
        "isPartOf": {"@type": "Blog", "name": "ApexRoute road guides", "url": GUIDES_URL},
    }, indent=2, ensure_ascii=False)


def head(title, desc, url, extra=""):
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="#0F0805" />
<title>{htmllib.escape(title)}</title>
<meta name="description" content="{htmllib.escape(desc, quote=True)}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{url}" />
<meta property="og:title" content="{htmllib.escape(title, quote=True)}" />
<meta property="og:description" content="{htmllib.escape(desc, quote=True)}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{url}" />
<meta property="og:site_name" content="ApexRoute" />
<meta property="og:locale" content="en_GB" />
<meta property="og:image" content="{BASE}/feature.png" />
<meta property="og:image:width" content="2048" />
<meta property="og:image:height" content="1365" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{htmllib.escape(title, quote=True)}" />
<meta name="twitter:description" content="{htmllib.escape(desc, quote=True)}" />
<meta name="twitter:image" content="{BASE}/feature.png" />
<link rel="icon" type="image/png" href="/icon.png" />
<link rel="apple-touch-icon" href="/icon.png" />
{FONTS}
{extra}<style>{CSS}</style>
</head>
<body>
{STUDIO_BAR}
{nav()}'''


def render_article(a, all_articles):
    url = f'{BASE}/guides/{a["slug"]}.html'
    jsonld = f'<script type="application/ld+json">\n{article_jsonld(a)}\n</script>\n'
    return f'''{head(a["seo_title"], a["description"], url, jsonld)}
<main>
  <div class="wrap">
    <article>
      <span class="eyebrow">{inline(a["eyebrow"])}</span>
      <h1>{inline(a["title"])}</h1>
      <p class="lead">{inline(a["summary"])}</p>
      <p class="byline">Froggy Eye Ltd · {a["published_label"]} · about {a["reading_minutes"]} minutes</p>
{render_sections(a["sections"])}
{cta(a)}
{more_reading(a, all_articles)}
    </article>
  </div>
</main>
{FOOTER}
</body>
</html>
'''


def render_listing(articles):
    cards = "\n".join(
        f'''      <a class="card" href="/guides/{a["slug"]}.html">
        <span class="eyebrow">{inline(a["eyebrow"])}</span>
        <h2>{inline(a["title"])}</h2>
        <p>{inline(a["card_blurb"])}</p>
        <span class="meta">{a["published_label"]} · about {a["reading_minutes"]} min</span>
      </a>''' for a in articles)
    desc = ("Guides to Britain's best driving roads — Wales, the Peak District and the Evo "
            "Triangle — plus how to plan a twisty route that ends where it started.")
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "ApexRoute road guides",
        "description": desc,
        "url": GUIDES_URL,
        "hasPart": [{"@type": "Article", "headline": a["title"],
                     "url": f'{BASE}/guides/{a["slug"]}.html'} for a in articles],
    }, indent=2, ensure_ascii=False)
    extra = f'<script type="application/ld+json">\n{jsonld}\n</script>\n'
    return f'''{head("Road guides — ApexRoute", desc, GUIDES_URL, extra)}
<main>
  <div class="wrap-wide">
    <div class="list-hero">
      <span class="eyebrow">Road guides</span>
      <h1>Roads worth the detour.</h1>
      <p class="lead">Honest write-ups of the roads we'd actually drive, and how to string them
        together into something that ends back where you parked. No sponsored detours, no
        invented pit stops — just the roads, what they're like, and what to watch for.</p>
    </div>
    <div class="card-grid">
{cards}
    </div>
  </div>
</main>
{FOOTER}
</body>
</html>
'''


def load_articles():
    articles = []
    for p in sorted(GUIDES_DIR.glob("*.json")):
        articles.append(json.loads(p.read_text()))
    articles.sort(key=lambda a: a.get("order", 99))
    return articles


def main():
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    articles = load_articles()
    if not articles:
        sys.exit(f"No articles found in {GUIDES_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for a in articles:
        if only and a["slug"] != only:
            continue
        out = OUT_DIR / f'{a["slug"]}.html'
        out.write_text(render_article(a, articles))
        words = sum(len(b.get("p", b.get("lead", ""))) for s in a["sections"] for b in s["blocks"])
        print(f'  ✓ {a["slug"]}.html ({out.stat().st_size:,} bytes)')

    if not only:
        (OUT_DIR / "index.html").write_text(render_listing(articles))
        print(f'  ✓ index.html (listing, {len(articles)} articles)')

    # The registry is what puts these in both sitemaps; warn rather than fix it
    # silently, so the two never drift without someone noticing.
    reg = next((x for x in load_apps() if x["folder"] == "apexroute"), None)
    if reg is not None:
        listed = set(reg.get("extra_pages", []))
        want = {"guides/"} | {f'guides/{a["slug"]}.html' for a in articles}
        missing = want - listed
        if missing:
            print("\n  ! Not in apps.json extra_pages (won't reach the sitemaps):")
            for m in sorted(missing):
                print(f"      {m}")


if __name__ == "__main__":
    main()
