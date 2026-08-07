#!/usr/bin/env python3
"""Regenerate public_html/index.html (the studio main page) from data/apps.json.
Preserves the dark studysingalong design language and links each app card to its subdomain."""
import sys
from html import escape as _esc
def esc(s): return _esc(s, quote=False)
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT

CSS = """
  :root {
    --magenta: #FF2E7E;
    --magenta-deep: #D11E63;
    --violet: #7C3AED;
    --mint: #3DF5B0;
    --yellow: #FFE14D;
    --bg: #0A0514;
    --surface: #15091F;
    --surface-2: #1F1230;
    --border: #2A1A3D;
    --text: #F5F0FF;
    --text-2: #B8A8D1;
    --text-3: #6B5A85;
    --grad: linear-gradient(135deg, #FF2E7E 0%, #7C3AED 100%);
    --font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    --font-body: 'Inter', system-ui, -apple-system, sans-serif;
    --r-md: 12px; --r-lg: 20px; --r-xl: 28px; --r-pill: 999px;
    --shadow-glow: 0 0 48px rgba(255,46,126,0.35);
  }
  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.55; -webkit-font-smoothing: antialiased; overflow-x: hidden; }
  img { max-width: 100%; display: block; }
  a { color: inherit; text-decoration: none; }
  ::selection { background: var(--magenta); color: #fff; }
  .wrap { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
  section { padding: 96px 0; position: relative; }
  @media (max-width: 720px) { section { padding: 64px 0; } }
  h1, h2, h3, h4 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin: 0 0 16px; }
  h1 { font-size: clamp(44px, 8vw, 96px); letter-spacing: -0.04em; }
  h2 { font-size: clamp(32px, 5vw, 56px); letter-spacing: -0.03em; }
  p { margin: 0 0 16px; color: var(--text-2); }
  .lead { font-size: clamp(18px, 2vw, 22px); color: var(--text-2); max-width: 56ch; }
  .eyebrow { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--magenta); margin-bottom: 16px; }
  .gradient-text { background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }

  nav.top { position: sticky; top: 0; z-index: 50; background: rgba(10,5,20,0.72); backdrop-filter: saturate(140%) blur(14px); -webkit-backdrop-filter: saturate(140%) blur(14px); border-bottom: 1px solid transparent; transition: border-color 200ms ease; }
  nav.top.scrolled { border-bottom-color: var(--border); }
  nav.top .wrap { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; }
  .brand { display: flex; align-items: center; gap: 14px; }
  .brand img { width: 56px; height: 56px; }
  .brand-name { font-family: var(--font-display); font-weight: 700; font-size: 20px; }
  nav.top ul { display: flex; gap: 28px; list-style: none; padding: 0; margin: 0; }
  nav.top ul a { color: var(--text-2); font-weight: 500; font-size: 14px; transition: color 150ms; }
  nav.top ul a:hover { color: var(--text); }
  @media (max-width: 800px) { nav.top ul { display: none; } }

  .btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 14px 24px; border-radius: var(--r-pill); font-family: var(--font-body); font-weight: 700; font-size: 15px; transition: transform 120ms ease, box-shadow 200ms ease; }
  .btn:active { transform: scale(0.97); }
  .btn-primary { background: var(--grad); color: #fff; box-shadow: var(--shadow-glow); }
  .btn-primary:hover { box-shadow: 0 0 64px rgba(255,46,126,0.5); }
  .btn-ghost { background: transparent; color: var(--text); border: 1.5px solid var(--border); }
  .btn-ghost:hover { border-color: var(--magenta); color: var(--magenta); }

  .hero { padding: 80px 0 64px; overflow: hidden; position: relative; text-align: center; }
  .hero::before { content: ''; position: absolute; top: -300px; left: 50%; width: 900px; height: 900px; background: radial-gradient(circle, rgba(255,46,126,0.25) 0%, rgba(124,58,237,0) 60%); transform: translateX(-50%); z-index: 0; pointer-events: none; }
  .hero .wrap { position: relative; z-index: 1; }
  .hero img.logo { width: 220px; height: auto; margin: 0 auto 24px; filter: drop-shadow(0 12px 36px rgba(255,46,126,0.4)); }
  .hero h1 { max-width: 18ch; margin: 0 auto 24px; }
  .hero p.lead { margin: 0 auto 32px; }
  .hero-meta { display: flex; flex-wrap: wrap; gap: 18px; justify-content: center; color: var(--text-3); font-size: 13px; }
  .hero-meta span { display: inline-flex; align-items: center; gap: 6px; }
  .hero-meta .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--mint); box-shadow: 0 0 8px var(--mint); }

  .about { padding: 64px 0; }
  .about-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
  @media (max-width: 800px) { .about-grid { grid-template-columns: 1fr; } }
  .about-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r-xl); padding: 32px; transition: border-color 200ms ease; }
  .about-card:hover { border-color: var(--magenta); }
  .about-icon { width: 48px; height: 48px; border-radius: 14px; background: rgba(255,46,126,0.12); border: 1px solid rgba(255,46,126,0.3); display: grid; place-items: center; margin-bottom: 16px; font-size: 22px; color: var(--magenta); }
  .about-card h3 { font-family: var(--font-body); font-size: 18px; font-weight: 700; margin-bottom: 8px; letter-spacing: 0; }
  .about-card p { font-size: 14px; margin: 0; }

  .apps-section { background: var(--surface); }
  .apps-section .wrap > .reveal { text-align: center; }
  .apps-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 56px; }
  @media (max-width: 1000px) { .apps-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 600px)  { .apps-grid { grid-template-columns: 1fr; } }
  .app-card { display: flex; gap: 16px; align-items: flex-start; background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-xl); padding: 22px; transition: transform 200ms ease, border-color 200ms ease; color: inherit; text-decoration: none; position: relative; }
  .app-card:hover { transform: translateY(-4px); border-color: var(--magenta); }
  .app-card-art { width: 64px; height: 64px; border-radius: 16px; flex-shrink: 0; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.4); position: relative; display: grid; place-items: center; }
  .app-card-art img { width: 100%; height: 100%; object-fit: cover; }
  .app-card-info { min-width: 0; flex: 1; }
  .app-card-title { font-family: var(--font-display); font-size: 18px; font-weight: 700; margin: 0 0 4px; color: var(--text); }
  .app-card-cat { font-size: 11px; color: var(--text-3); letter-spacing: 0.12em; text-transform: uppercase; margin: 0 0 8px; font-weight: 600; }
  .app-card-tag { font-size: 13px; color: var(--text-2); margin: 0 0 14px; line-height: 1.5; }
  .app-card-cta { font-size: 13px; font-weight: 600; color: var(--magenta); display: inline-flex; align-items: center; gap: 4px; transition: gap 150ms ease; }
  .app-card:hover .app-card-cta { gap: 8px; }

  .cta-banner { background: var(--grad); border-radius: var(--r-xl); padding: 56px 48px; text-align: center; position: relative; overflow: hidden; margin: 0 0 64px; }
  .cta-banner::before, .cta-banner::after { content: ''; position: absolute; border-radius: 50%; background: rgba(255,255,255,0.12); pointer-events: none; }
  .cta-banner::before { width: 280px; height: 280px; top: -140px; right: -100px; }
  .cta-banner::after { width: 200px; height: 200px; bottom: -100px; left: -80px; }
  .cta-banner h2 { color: #fff; margin-bottom: 12px; position: relative; z-index: 1; font-size: clamp(28px, 4vw, 44px); }
  .cta-banner p { color: rgba(255,255,255,0.88); margin: 0 auto 24px; max-width: 50ch; position: relative; z-index: 1; font-size: 17px; }
  .cta-banner .btn { background: rgba(0,0,0,0.4); color: #fff; border: 1px solid rgba(255,255,255,0.4); position: relative; z-index: 1; }
  .cta-banner .btn:hover { background: rgba(0,0,0,0.6); box-shadow: none; }

  footer { border-top: 1px solid var(--border); padding: 48px 0 36px; color: var(--text-3); font-size: 14px; }
  footer .wrap { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 40px; }
  @media (max-width: 800px) { footer .wrap { grid-template-columns: 1fr; gap: 28px; } }
  footer h4 { font-family: var(--font-body); font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-2); margin: 0 0 16px; }
  footer ul { list-style: none; padding: 0; margin: 0; }
  footer li { padding: 4px 0; }
  footer a { color: var(--text-3); transition: color 150ms ease; }
  footer a:hover { color: var(--magenta); }
  .legal { border-top: 1px solid var(--border); margin-top: 36px; padding-top: 24px; color: var(--text-3); font-size: 12px; display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; }

  @media (prefers-reduced-motion: no-preference) {
    .reveal { opacity: 0; transform: translateY(24px); transition: opacity 600ms ease, transform 600ms ease; }
    .reveal.in { opacity: 1; transform: none; }
  }
"""

def render_card(a):
    g0, g1 = a["card_gradient"]
    icon = f'icons/{a["folder"]}.png'
    return f'''      <a class="app-card reveal" href="https://{a["folder"]}.froggyeye.com">
        <div class="app-card-art" style="background: linear-gradient(135deg, {g0}, {g1});">
          <img src="{icon}" alt="{esc(a["name"])}">
        </div>
        <div class="app-card-info">
          <p class="app-card-cat">{esc(a["category"])}</p>
          <h3 class="app-card-title">{esc(a["name"])}</h3>
          <p class="app-card-tag">{esc(a["tagline"])}</p>
          <span class="app-card-cta">Learn more →</span>
        </div>
      </a>'''

def render():
    apps = load_apps()
    cards = "\n".join(render_card(a) for a in apps)
    n_apps = len(apps)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="#0A0514" />
<title>Froggy Eye Ltd — Mobile apps that make life better.</title>
<meta name="description" content="Froggy Eye Ltd is a UK-based indie app studio. {n_apps} well-crafted iOS and Android apps for productivity, games, family, finance, and creativity." />
<meta property="og:title" content="Froggy Eye Ltd — Mobile apps that make life better." />
<meta property="og:description" content="A UK indie studio shipping useful, beautiful, no-nonsense apps for iOS and Android." />
<meta property="og:type" content="website" />
<link rel="icon" type="image/png" href="icons/logo.png" />
<link rel="apple-touch-icon" href="icons/logo.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<style>{CSS}</style>
</head>
<body>

<nav class="top" id="topnav">
  <div class="wrap">
    <a class="brand" href="#">
      <img src="icons/logo.png" alt="Froggy Eye Ltd" />
      <span class="brand-name">Froggy Eye Ltd</span>
    </a>
    <ul>
      <li><a href="#about">About</a></li>
      <li><a href="#apps">Apps</a></li>
      <li><a href="mailto:info@froggyeye.com">Contact</a></li>
    </ul>
    <a href="#apps" class="btn btn-primary" style="padding: 10px 18px; font-size: 14px;">Browse apps</a>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <img src="icons/logo-full.png" alt="Froggy Eye Ltd" class="logo">
    <h1>Mobile apps that <span class="gradient-text">make life better.</span></h1>
    <p class="lead" style="margin: 0 auto 32px;">A UK indie studio shipping useful, beautifully made iOS and Android apps. {n_apps} of them so far. Each one solves a real problem — without ads, dark patterns, or shipping garbage.</p>
    <div class="hero-meta">
      <span><span class="dot"></span> Made in the United Kingdom</span>
      <span>{n_apps} live apps</span>
      <span>iOS &amp; Android</span>
    </div>
  </div>
</header>

<section id="about" class="about">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-card reveal">
        <div class="about-icon">🎯</div>
        <h3>User-focused</h3>
        <p>Every app starts with a real user need. We prioritise simplicity and usefulness above 'engagement'.</p>
      </div>
      <div class="about-card reveal">
        <div class="about-icon">✨</div>
        <h3>Quality crafted</h3>
        <p>We obsess over the details. Animations, haptics, performance, copy — all the bits most apps skip.</p>
      </div>
      <div class="about-card reveal">
        <div class="about-icon">🚀</div>
        <h3>Always improving</h3>
        <p>We listen. We ship updates. We don't disappear after launch. Your experience matters to us.</p>
      </div>
    </div>
  </div>
</section>

<section id="apps" class="apps-section">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Our apps</span>
      <h2>{n_apps} apps.<br><span class="gradient-text">All built with the same care.</span></h2>
      <p class="lead" style="margin: 0 auto;">Tap any card to dive into the full story — features, pricing, FAQs, and how to get it.</p>
    </div>
    <div class="apps-grid">
{cards}
    </div>
  </div>
</section>

<section style="padding-top: 0;">
  <div class="wrap">
    <div class="cta-banner reveal">
      <h2>Got a problem we should solve next?</h2>
      <p>We listen to ideas. Send us a note — the best ones become apps.</p>
      <a href="mailto:info@froggyeye.com" class="btn">Email the studio →</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div>
      <a class="brand" href="#" style="margin-bottom: 16px;">
        <img src="icons/logo.png" alt="Froggy Eye Ltd" />
        <span class="brand-name">Froggy Eye Ltd</span>
      </a>
      <p style="font-size: 14px; max-width: 36ch; margin: 0;">A UK indie app studio building thoughtful mobile apps. iOS &amp; Android, ad-free where we can manage it.</p>
    </div>
    <div>
      <h4>Studio</h4>
      <ul>
        <li><a href="#apps">All apps</a></li>
        <li><a href="mailto:info@froggyeye.com">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Legal</h4>
      <ul>
        <li><a href="privacy.html">Privacy policy</a></li>
        <li><a href="terms.html">Terms of service</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap">
    <div class="legal">
      <span>&copy; 2026 Froggy Eye Ltd. All rights reserved.</span>
      <span>App Store and the Apple logo are trademarks of Apple Inc. Google Play and the Google Play logo are trademarks of Google LLC.</span>
    </div>
  </div>
</footer>

<script>
  const nav = document.getElementById('topnav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, {{ passive: true }});
  onScroll();
  if ('IntersectionObserver' in window) {{
    const io = new IntersectionObserver((entries) => {{
      entries.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
    }}, {{ threshold: 0.12 }});
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  }} else {{
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
  }}
</script>
</body>
</html>
"""
    (SITE_ROOT / "index.html").write_text(html)
    print(f"Wrote {SITE_ROOT/'index.html'}  ({len(html):,} bytes)")
    print("After regen, run scripts/seo_enhance.py to inject canonical/twitter/JSON-LD.")

if __name__ == "__main__":
    render()
