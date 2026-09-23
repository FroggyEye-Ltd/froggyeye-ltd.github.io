#!/usr/bin/env python3
"""Render Passport Photo Studio's PRIVACY_POLICY.md into
passportphoto.froggyeye.com/privacy.html. The policy text is kept verbatim;
only markup is added. Styling follows the other per-app legal pages
(foodscore/apexroute privacy.html) using the app's "tile" theme."""
import html, re
from pathlib import Path

SRC = Path("/Users/kevinlam/projects/passport_photo_app/PRIVACY_POLICY.md")
OUT = Path("/Users/kevinlam/froggyeye-ltd.github.io/public_html/passportphoto/privacy.html")
URL = "https://passportphoto.froggyeye.com/privacy.html"
APP = "Passport Photo Studio"

# "tile" theme from data/themes.json
T = dict(primary="#0EA5E9", primary_deep="#0369A1", violet="#1D4ED8",
         mint="#5EEAD4", yellow="#FDE047",
         bg="#040A14", surface="#0A1626", surface2="#102339", border="#1B3957")

CSS = """
  :root {
    --primary: %(primary)s; --primary-deep: %(primary_deep)s; --violet: %(violet)s;
    --mint: %(mint)s; --yellow: %(yellow)s;
    --bg: %(bg)s; --surface: %(surface)s; --surface-2: %(surface2)s; --border: %(border)s;
    --text: #F1F5FB; --text-2: #B4C3D6; --text-3: #6B819C;
    --grad: linear-gradient(135deg, %(primary)s 0%%, %(violet)s 100%%);
    --font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    --font-body: 'Inter', system-ui, -apple-system, sans-serif;
    --r-sm: 8px; --r-md: 12px; --r-lg: 20px; --r-pill: 999px;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%%; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.65; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
  ::selection { background: var(--primary); color: #04101C; }
  a { color: var(--primary); text-decoration: none; overflow-wrap: anywhere; }
  a:hover { text-decoration: underline; }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.2; margin: 0 0 12px; }
  h1 { font-size: clamp(32px, 5vw, 46px); letter-spacing: -0.03em; }
  h2 { font-size: clamp(21px, 3vw, 26px); margin-top: 44px; scroll-margin-top: 80px; }
  p { margin: 0 0 14px; color: var(--text-2); }
  ul, ol { color: var(--text-2); padding-left: 22px; margin: 0 0 16px; }
  li { margin-bottom: 8px; }
  strong { color: var(--text); }
  .wrap { max-width: 820px; margin: 0 auto; padding: 0 24px; }
  .studio-bar { background: linear-gradient(90deg, #FF2E7E 0%%, #7C3AED 100%%); color: #fff; font-size: 13px; font-weight: 600; text-align: center; padding: 8px 16px; }
  .studio-bar a { color: #fff; }
  nav.top { position: sticky; top: 0; z-index: 50; background: rgba(4,10,20,0.82); backdrop-filter: saturate(140%%) blur(14px); -webkit-backdrop-filter: saturate(140%%) blur(14px); border-bottom: 1px solid var(--border); }
  nav.top .wrap { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-top: 14px; padding-bottom: 14px; }
  .brand { display: flex; align-items: center; gap: 12px; }
  .brand img { width: 32px; height: 32px; border-radius: 8px; }
  .brand-name { font-family: var(--font-display); font-weight: 700; font-size: 17px; color: var(--text); }
  .crumbs { font-size: 13px; color: var(--text-3); }
  .crumbs a { color: var(--text-3); }
  .crumbs a:hover { color: var(--primary); }
  header.hero { padding: 60px 0 30px; border-bottom: 1px solid var(--border); }
  header.hero .eyebrow { display: inline-block; font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--primary); margin-bottom: 14px; }
  header.hero p.lead { font-size: 18px; color: var(--text-2); max-width: 62ch; margin-top: 4px; }
  .meta { margin-top: 18px; font-size: 13px; color: var(--text-3); }
  main.content { padding: 30px 0 70px; }
  .toc { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r-md); padding: 16px 20px; margin: 20px 0 34px; }
  .toc-title { font-family: var(--font-display); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-3); margin-bottom: 8px; }
  .toc ol { padding-left: 22px; margin: 0; font-size: 14px; }
  .toc li { margin-bottom: 4px; }
  .toc a { color: var(--text-2); }
  .toc a:hover { color: var(--primary); }
  .back-link { display: inline-block; margin-top: 30px; padding: 10px 18px; color: var(--primary); border: 1px solid var(--border); border-radius: var(--r-pill); font-weight: 600; font-size: 14px; transition: border-color 150ms ease; }
  .back-link:hover { border-color: var(--primary); text-decoration: none; }
  footer { border-top: 1px solid var(--border); padding: 32px 0; color: var(--text-3); font-size: 13px; text-align: center; }
  footer a { color: var(--text-3); }
  footer a:hover { color: var(--primary); }
""" % T

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
         '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700'
         '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />')


def inline(text):
    """HTML-escape, then **bold**, *italic*, bare URLs and emails. Text unchanged."""
    s = html.escape(text, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*\s][^*]*?)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"(https?://[^\s<]+[^\s<.,;:)])",
               lambda m: f'<a href="{m.group(1)}"'
               + ('' if 'froggyeye.com' in m.group(1) else ' target="_blank" rel="noopener"')
               + f'>{m.group(1)}</a>', s)
    s = re.sub(r"\b(info@froggyeye\.com)\b", r'<a href="mailto:\1">\1</a>', s)
    return s


def slug(h):
    return re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")


def blocks(md):
    """Yield ('h1'|'h2'|'p'|'ul', payload) from paragraph-wrapped Markdown."""
    paras = re.split(r"\n\s*\n", md.strip())
    items = None
    for para in paras:
        lines = para.splitlines()
        if lines[0].startswith("# "):
            yield "h1", lines[0][2:].strip(); continue
        if lines[0].startswith("## "):
            if items: yield "ul", items; items = None
            yield "h2", lines[0][3:].strip(); continue
        if lines[0].startswith("- "):
            # list item (possibly wrapped); consecutive items separated by blank
            # lines form one list
            cur = []
            for ln in lines:
                if ln.startswith("- "):
                    if cur: (items := items or []).append(" ".join(cur))
                    cur = [ln[2:].strip()]
                else:
                    cur.append(ln.strip())
            (items := items or []).append(" ".join(cur))
            continue
        if items: yield "ul", items; items = None
        yield "p", lines
    if items: yield "ul", items


def render(md):
    title, updated = None, None
    pre, body, toc = [], [], []
    for kind, val in blocks(md):
        if kind == "h1":
            title = val
        elif kind == "h2":
            a = slug(val); toc.append((a, val))
            body.append(f'<h2 id="{a}">{inline(val)}</h2>')
        elif kind == "ul":
            (body if toc else pre).append(
                "<ul>\n" + "\n".join(f"  <li>{inline(i)}</li>" for i in val) + "\n</ul>")
        else:
            joined = " ".join(l.strip() for l in val)
            m = re.fullmatch(r"\*\*Last updated: (.+)\*\*", joined)
            if m and not toc:
                updated = m.group(1); continue
            if len(val) > 1 and all(not l.rstrip().endswith((".", ",", ":", ";")) for l in val[:-1]) \
                    and val[0].startswith("Froggy Eye Ltd"):
                # the address block at the end keeps its line breaks
                html_p = "<br />\n".join(inline(l.strip()) for l in val)
            else:
                html_p = inline(joined)
            (body if toc else pre).append(f"<p>{html_p}</p>")
    return title, updated, "\n".join(pre), "\n".join(body), toc


def main():
    md = SRC.read_text()
    assert "mksoft" not in md.lower(), "source mentions mksoft"
    title, updated, pre, body, toc = render(md)
    desc = ("Passport Photo Studio privacy policy, published by Froggy Eye Ltd: your photo never "
            "leaves your device, face detection runs on-device, and no face data is collected, "
            "stored or shared.")
    toc_html = "\n".join(f'    <li><a href="#{a}">{inline(h)}</a></li>' for a, h in toc)
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="{T['bg']}" />
<title>Privacy Policy — {APP}</title>
<meta name="description" content="{html.escape(desc)}" />
<meta name="robots" content="index, follow" />
<meta name="author" content="Froggy Eye Ltd" />
<link rel="icon" type="image/png" href="icon.png" />
<link rel="apple-touch-icon" href="icon.png" />
{FONTS}
<link rel="canonical" href="{URL}" />
<meta property="og:title" content="Privacy Policy — {APP}" />
<meta property="og:description" content="{html.escape(desc)}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{URL}" />
<meta property="og:site_name" content="Froggy Eye Ltd" />
<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy Policy — {APP}",
 "url": "{URL}", "dateModified": "{html.escape(updated or '')}",
 "about": {{"@type": "MobileApplication", "name": "{APP}", "url": "https://passportphoto.froggyeye.com/"}},
 "publisher": {{"@type": "Organization", "name": "Froggy Eye Ltd", "url": "https://froggyeye.com",
   "email": "info@froggyeye.com", "address": {{"@type": "PostalAddress", "addressCountry": "GB"}}}}}}
</script>
<style>{CSS}</style>
</head>
<body>
<div class="studio-bar"><a href="https://froggyeye.com">← Part of <strong>Froggy Eye Ltd</strong></a></div>

<nav class="top">
  <div class="wrap">
    <a class="brand" href="/">
      <img src="icon.png" alt="" />
      <span class="brand-name">{APP}</span>
    </a>
    <div class="crumbs"><a href="/">{APP}</a> &nbsp;›&nbsp; Privacy</div>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <span class="eyebrow">Legal</span>
    <h1>{inline(title)}</h1>
    <p class="meta">Last updated: {html.escape(updated or '')} &nbsp;·&nbsp; Published by Froggy Eye Ltd, United Kingdom</p>
  </div>
</header>

<main class="content">
<div class="wrap">

{pre}

<div class="toc">
  <div class="toc-title">On this page</div>
  <ol>
{toc_html}
  </ol>
</div>

{body}

<a class="back-link" href="/">← Back to {APP}</a>

</div>
</main>

<footer>
  <div class="wrap">
    {APP} is made by <a href="https://froggyeye.com">Froggy Eye Ltd</a>. &nbsp;·&nbsp;
    <a href="https://froggyeye.com/terms.html">Terms of Use</a> &nbsp;·&nbsp;
    <a href="mailto:info@froggyeye.com">Contact</a>
  </div>
</footer>

</body>
</html>
"""
    OUT.write_text(out)
    print("rendered", OUT, f"({len(out)} bytes, {len(toc)} sections)")


if __name__ == "__main__":
    main()
