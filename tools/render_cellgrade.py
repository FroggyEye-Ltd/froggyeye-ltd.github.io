#!/usr/bin/env python3
"""Render Cellgrade's Terms and Privacy Markdown into froggyeye.com legal pages,
plus a minimal landing page. Text is kept verbatim; only markup is added."""
import html, re
from pathlib import Path

SRC = Path("/Users/kevinlam/projects/cellgrade/docs/legal")
OUT = Path("/Users/kevinlam/froggyeye-ltd.github.io/public_html/cellgrade")

# "forest" theme from data/themes.json
T = dict(primary="#34D399", primary_deep="#059669", violet="#047857",
         mint="#A7F3D0", yellow="#FDE047",
         bg="#04120D", surface="#0A2218", surface2="#103224", border="#1A4A35")

CSS = """
  :root {
    --primary: %(primary)s; --primary-deep: %(primary_deep)s; --violet: %(violet)s;
    --mint: %(mint)s; --yellow: %(yellow)s;
    --bg: %(bg)s; --surface: %(surface)s; --surface-2: %(surface2)s; --border: %(border)s;
    --text: #F1F7F4; --text-2: #B7CCC2; --text-3: #6E8A7E;
    --grad: linear-gradient(135deg, %(primary)s 0%%, %(violet)s 100%%);
    --font-display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
    --font-body: 'Inter', system-ui, -apple-system, sans-serif;
    --r-sm: 8px; --r-md: 12px; --r-lg: 20px; --r-pill: 999px;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%%; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.65; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
  ::selection { background: var(--primary); color: #04120D; }
  a { color: var(--primary); text-decoration: none; }
  a:hover { text-decoration: underline; }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; line-height: 1.2; margin: 0 0 12px; }
  h1 { font-size: clamp(32px, 5vw, 46px); letter-spacing: -0.03em; }
  h2 { font-size: clamp(21px, 3vw, 26px); margin-top: 44px; }
  p { margin: 0 0 14px; color: var(--text-2); }
  ul, ol { color: var(--text-2); padding-left: 22px; margin: 0 0 16px; }
  li { margin-bottom: 8px; }
  strong { color: var(--text); }
  .wrap { max-width: 820px; margin: 0 auto; padding: 0 24px; }
  .studio-bar { background: linear-gradient(90deg, #FF2E7E 0%%, #7C3AED 100%%); color: #fff; font-size: 13px; font-weight: 600; text-align: center; padding: 8px 16px; }
  .studio-bar a { color: #fff; }
  nav.top { position: sticky; top: 0; z-index: 50; background: rgba(4,18,13,0.82); backdrop-filter: saturate(140%%) blur(14px); -webkit-backdrop-filter: saturate(140%%) blur(14px); border-bottom: 1px solid var(--border); }
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
  .toc { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r-md); padding: 16px 20px; margin: 24px 0 34px; }
  .toc-title { font-family: var(--font-display); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-3); margin-bottom: 8px; }
  .toc ol { padding-left: 22px; margin: 0; font-size: 14px; }
  .toc li { margin-bottom: 4px; }
  .toc a { color: var(--text-2); }
  .toc a:hover { color: var(--primary); }
  .callout { background: rgba(52,211,153,0.07); border: 1px solid rgba(52,211,153,0.35); border-radius: var(--r-lg); padding: 22px 26px; margin: 24px 0; }
  .callout p { margin: 0 0 8px; color: var(--text-2); }
  .callout p:last-child { margin: 0; }
  .callout strong { color: var(--primary); }
  .clause { padding-left: 3.2em; text-indent: -3.2em; }
  .clause .num { display: inline-block; width: 3.2em; text-indent: 0; color: var(--text-3); font-variant-numeric: tabular-nums; }
  .related { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 30px; }
  .back-link { display: inline-block; padding: 10px 18px; color: var(--primary); border: 1px solid var(--border); border-radius: var(--r-pill); font-weight: 600; font-size: 14px; transition: border-color 150ms ease; }
  .back-link:hover { border-color: var(--primary); text-decoration: none; }
  footer { border-top: 1px solid var(--border); padding: 32px 0; color: var(--text-3); font-size: 13px; text-align: center; }
  footer a { color: var(--text-3); }
  footer a:hover { color: var(--primary); }
""" % T

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
         '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700'
         '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />')

STUDIO_BAR = '<div class="studio-bar"><a href="https://froggyeye.com">← Part of <strong>Froggy Eye Ltd</strong></a></div>'


def inline(text):
    """HTML-escape, then apply **bold**, mailto links, and the two site links."""
    s = html.escape(text, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\b((?:support|info)@froggyeye\.com)\b", r'<a href="mailto:\1">\1</a>', s)
    s = s.replace("froggyeye.com/cellgrade/privacy",
                  '<a href="../privacy/">froggyeye.com/cellgrade/privacy</a>')
    s = re.sub(r"\(ico\.org\.uk\)", '(<a href="https://ico.org.uk" target="_blank" rel="noopener">ico.org.uk</a>)', s)
    return s


def slug(heading):
    return re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")


def convert(md_text):
    """Returns (title, meta_lines, callout_html, body_html, toc)."""
    lines = md_text.splitlines()
    title = None
    meta = []
    pre = []          # content before the first h2, in document order
    callout = []
    body = []
    toc = []
    i = 0
    in_list = False
    in_comment = False   # <!-- drafting notes --> in the Markdown are never published

    def flush_callout():
        if callout:
            pre.append('<div class="callout">\n' + "\n".join(f"<p>{c}</p>" for c in callout) + "\n</div>")
            callout.clear()

    def close_list():
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i]
        if in_comment or line.lstrip().startswith("<!--"):
            in_comment = "-->" not in line
            i += 1
            continue
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("> "):
            callout.append(inline(line[2:].strip()))
        elif line.startswith("## "):
            close_list()
            flush_callout()
            h = line[3:].strip()
            m = re.match(r"^(\d+)\.\s+(.*)$", h)
            anchor = f"s{m.group(1)}" if m else slug(h)
            toc.append((anchor, h))
            body.append(f'<h2 id="{anchor}">{inline(h)}</h2>')
        elif line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline(line[2:].strip())}</li>")
        elif line.strip() == "":
            close_list()
            flush_callout()
        elif title is not None and not toc and not pre and re.match(r"^\*\*[^*]+:\*\*", line):
            meta.append(inline(line.strip()))
        elif not toc:
            flush_callout()
            pre.append(f"<p>{inline(line.strip())}</p>")
        else:
            close_list()
            m = re.match(r"^(\d+\.\d+)\s+(.*)$", line)
            if m:
                body.append(f'<p class="clause"><span class="num">{m.group(1)}</span>{inline(m.group(2))}</p>')
            else:
                body.append(f"<p>{inline(line.strip())}</p>")
        i += 1
    close_list()
    flush_callout()
    return title, meta, "\n\n".join(pre), "\n".join(body), toc


def effective_date(md_text):
    m = re.search(r"\*\*Effective date:\*\*\s*(.+)", md_text)
    return m.group(1).strip()


def page(kind, md_text, lead, description, other_kind, other_label):
    title, meta, pre, body, toc = convert(md_text)
    date = effective_date(md_text)
    short = "Terms of Use" if kind == "terms" else "Privacy Policy"
    url = f"https://froggyeye.com/cellgrade/{kind}/"
    toc_html = "\n".join(f'    <li><a href="#{a}">{inline(h)}</a></li>' for a, h in toc)
    meta_html = "<br />\n".join(meta)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="{T['bg']}" />
<title>{short} — Cellgrade</title>
<meta name="description" content="{html.escape(description)}" />
<meta name="robots" content="index, follow" />
<link rel="icon" type="image/png" href="../icon.png" />
<link rel="apple-touch-icon" href="../icon.png" />
{FONTS}
<link rel="canonical" href="{url}" />
<meta property="og:title" content="{short} — Cellgrade" />
<meta property="og:description" content="{html.escape(description)}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<style>{CSS}</style>
</head>
<body>
{STUDIO_BAR}

<nav class="top">
  <div class="wrap">
    <a class="brand" href="../">
      <img src="../icon.png" alt="" />
      <span class="brand-name">Cellgrade</span>
    </a>
    <div class="crumbs"><a href="../">Cellgrade</a> &nbsp;›&nbsp; {short.split()[0]}</div>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <span class="eyebrow">Legal</span>
    <h1>{inline(title)}</h1>
    <p class="lead">{lead}</p>
    <p class="meta">{meta_html}</p>
    <p class="meta">Last updated: {html.escape(date)}</p>
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

<div class="related">
  <a class="back-link" href="../">← Back to Cellgrade</a>
  <a class="back-link" href="../{other_kind}/">{other_label} →</a>
  <a class="back-link" href="../verify/">Check a report →</a>
</div>

</div>
</main>

<footer>
  <div class="wrap">
    Cellgrade is made by <a href="https://froggyeye.com">Froggy Eye Ltd</a>. &nbsp;·&nbsp;
    <a href="../terms/">Terms of Use</a> &nbsp;·&nbsp;
    <a href="../privacy/">Privacy Policy</a> &nbsp;·&nbsp;
    <a href="../verify/">Check a report</a>
  </div>
</footer>

</body>
</html>
"""


LANDING = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="{T['bg']}" />
<title>Cellgrade — Every car has a battery. Cellgrade grades it.</title>
<meta name="description" content="Cellgrade reads what your car's own computers report about its battery and turns it into a letter grade and a battery report. By Froggy Eye Ltd." />
<meta name="robots" content="index, follow" />
<link rel="icon" type="image/png" href="icon.png" />
<link rel="apple-touch-icon" href="icon.png" />
{FONTS}
<link rel="canonical" href="https://froggyeye.com/cellgrade/" />
<meta property="og:title" content="Cellgrade — Every car has a battery. Cellgrade grades it." />
<meta property="og:description" content="Cellgrade reads what your car's own computers report about its battery and turns it into a letter grade and a battery report." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://froggyeye.com/cellgrade/" />
<meta property="og:image" content="https://froggyeye.com/cellgrade/icon.png" />
<style>{CSS}
  header.hero.landing {{ padding: 80px 0 60px; text-align: center; border-bottom: 1px solid var(--border); }}
  header.hero.landing .app-icon {{ width: 112px; height: 112px; border-radius: 26px; box-shadow: 0 20px 60px rgba(0,0,0,0.45); border: 1px solid var(--border); margin-bottom: 26px; }}
  header.hero.landing h1 {{ font-size: clamp(38px, 6vw, 60px); }}
  header.hero.landing h1 span {{ background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }}
  header.hero.landing p.lead {{ margin: 12px auto 0; font-size: clamp(18px, 2.4vw, 22px); }}
  .stores {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 34px; }}
  .store-btn {{ display: inline-flex; align-items: center; gap: 10px; padding: 12px 20px; border-radius: var(--r-md); border: 1px solid var(--border); background: var(--surface); color: var(--text-3); font-weight: 600; font-size: 15px; cursor: default; }}
  .store-btn small {{ display: block; font-size: 11px; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-3); }}
  .store-btn .label {{ line-height: 1.15; text-align: left; }}
  .stores-note {{ margin-top: 12px; font-size: 13px; color: var(--text-3); }}
  .links {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 44px 0 10px; }}
  .link-card {{ display: block; background: var(--surface); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 20px 22px; color: var(--text); transition: border-color 150ms ease, transform 150ms ease; }}
  .link-card:hover {{ border-color: var(--primary); text-decoration: none; transform: translateY(-2px); }}
  .link-card h2 {{ font-size: 18px; margin: 0 0 6px; }}
  .link-card p {{ margin: 0; font-size: 14px; }}
</style>
</head>
<body>
{STUDIO_BAR}

<nav class="top">
  <div class="wrap">
    <a class="brand" href="./">
      <img src="icon.png" alt="" />
      <span class="brand-name">Cellgrade</span>
    </a>
    <div class="crumbs"><a href="https://froggyeye.com">Froggy Eye Ltd</a> &nbsp;›&nbsp; Cellgrade</div>
  </div>
</nav>

<header class="hero landing">
  <div class="wrap">
    <img class="app-icon" src="icon.png" alt="Cellgrade app icon" />
    <h1><span>Cellgrade</span></h1>
    <p class="lead">Every car has a battery. Cellgrade grades it.</p>
    <div class="stores" aria-label="Store listings">
      <span class="store-btn" aria-disabled="true"><span class="label"><small>Coming soon on the</small>App Store</span></span>
      <span class="store-btn" aria-disabled="true"><span class="label"><small>Coming soon on</small>Google Play</span></span>
    </div>
    <p class="stores-note">Store listings are not live yet. Download links will appear here when they are.</p>
  </div>
</header>

<main class="content">
<div class="wrap">
  <div class="links">
    <a class="link-card" href="verify/">
      <h2>Check a report</h2>
      <p>Scanned a Cellgrade Battery Report? Confirm it has not been altered since it was issued. The check runs in your browser and nothing is uploaded.</p>
    </a>
    <a class="link-card" href="terms/">
      <h2>Terms of Use</h2>
      <p>What Cellgrade is, what it is not, and what you agree to when you use it.</p>
    </a>
    <a class="link-card" href="privacy/">
      <h2>Privacy Policy</h2>
      <p>No account, no advertising, no analytics. What stays on your phone and what leaves it, and when.</p>
    </a>
  </div>
</div>
</main>

<footer>
  <div class="wrap">
    Cellgrade is made by <a href="https://froggyeye.com">Froggy Eye Ltd</a>. &nbsp;·&nbsp;
    <a href="terms/">Terms of Use</a> &nbsp;·&nbsp;
    <a href="privacy/">Privacy Policy</a> &nbsp;·&nbsp;
    <a href="verify/">Check a report</a> &nbsp;·&nbsp;
    <a href="mailto:info@froggyeye.com">Contact</a>
  </div>
</footer>

</body>
</html>
"""


def main():
    terms_md = (SRC / "TERMS.md").read_text()
    privacy_md = (SRC / "PRIVACY.md").read_text()

    (OUT / "terms").mkdir(parents=True, exist_ok=True)
    (OUT / "privacy").mkdir(parents=True, exist_ok=True)

    (OUT / "terms" / "index.html").write_text(page(
        "terms", terms_md,
        "The agreement between you and Froggy Eye Ltd for the Cellgrade mobile app. Installing or using the app, or relying on anything it produces, means you accept them.",
        "The terms you agree to when using Cellgrade: grades and certificates are information from the vehicle's own data, not an inspection, warranty, guarantee or valuation.",
        "privacy", "Privacy Policy"))
    (OUT / "privacy" / "index.html").write_text(page(
        "privacy", privacy_md,
        "How Cellgrade handles data. There is no account, no advertising and no analytics, and what the app reads from your car stays on your phone unless you choose to send it.",
        "Cellgrade's privacy policy: no account, no advertising, no analytics. What the app stores on your phone, what leaves it and when, permissions, retention and your rights.",
        "terms", "Terms of Use"))
    (OUT / "index.html").write_text(LANDING)
    print("rendered", OUT / "index.html", OUT / "terms/index.html", OUT / "privacy/index.html")


if __name__ == "__main__":
    main()
