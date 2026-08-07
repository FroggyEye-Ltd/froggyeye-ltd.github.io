#!/usr/bin/env python3
"""Render per-app promo pages from templates + data.

Inputs (all inside this skill):
  templates/promo_template.html, templates/promo_template.css
  data/themes.json      — colour presets (theme name -> tokens)
  data/apps.json        — app registry (authoritative folder + theme name)
  data/content/<folder>.json — the page copy: headline, chips, steps,
                               features, examples, plans, stats, faq, ...

Usage:
  python3 gen_promo.py                 # render every non-user_authored app
  python3 gen_promo.py --only <folder> # render one app

Apps flagged "user_authored" in apps.json (e.g. studysingalong) are never
touched. A missing content file is reported with the expected schema; copy an
existing data/content/*.json as a starting point for a new app.

After rendering, run postprocess.py to inject screenshots, the feature banner
and real store URLs.
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import SKILL_ROOT, SITE_ROOT, load_apps, load_themes, template, parse_only_arg

CONTENT_DIR = SKILL_ROOT / "data" / "content"

CONTENT_KEYS = [
    "name", "tagline", "meta_desc", "hero_eyebrow", "headline_pre",
    "headline_accent", "lead", "meta_items", "phone_content", "chips",
    "how_head_pre", "how_head_accent", "how_lead", "steps",
    "feat_head_pre", "feat_head_line2", "features",
    "ex_eyebrow", "ex_head", "ex_lead", "examples",
    "pricing_lead", "plans",
    "why_eyebrow", "why_head_pre", "why_head_accent", "why_lead", "why_body",
    "stats", "faq", "final_title", "final_body", "footer_blurb",
]


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgba(h, a):
    r, g, b = hex_to_rgb(h)
    return f"rgba({r},{g},{b},{a})"


def render_css(theme):
    css = template("promo_template.css")
    primary, violet, mint, yellow = theme["primary"], theme["violet"], theme["mint"], theme["yellow"]
    bg, surface2 = theme["bg"], theme["surface2"]
    repl = {
        "__PRIMARY__": primary,
        "__PRIMARY_DEEP__": theme["primary_deep"],
        "__VIOLET__": violet,
        "__MINT__": mint,
        "__YELLOW__": yellow,
        "__BG__": bg,
        "__SURFACE__": theme["surface"],
        "__SURFACE2__": surface2,
        "__BORDER__": theme["border"],
        "__GLOW__": rgba(primary, 0.35),
        "__GLOW_HOVER__": rgba(primary, 0.5),
        "__MINT_GLOW__": rgba(mint, 0.3),
        "__NAV_BG__": rgba(bg, 0.72),
        "__HERO_GLOW__": rgba(primary, 0.25),
        "__PHONE_SHADOW1__": rgba(primary, 0.4),
        "__PHONE_SHADOW2__": rgba(violet, 0.5),
        "__PHONE_GLOW1__": rgba(primary, 0.35),
        "__PHONE_GLOW2__": rgba(violet, 0.4),
        "__ART_GLOW__": rgba(mint, 0.4),
        "__ART_SHADOW__": rgba(primary, 0.4),
        "__ART_SHADOW_HOVER__": rgba(primary, 0.6),
        "__LYRIC_BG__": rgba(surface2, 0.6),
        "__ICON_BG__": rgba(primary, 0.12),
        "__ICON_BORDER__": rgba(primary, 0.3),
    }
    chip_palette = [
        (primary, 0.18, 0.5, "#FFD0E2"),
        (yellow, 0.15, 0.45, "#FFE0A0"),
        (violet, 0.18, 0.5, "#E2C7FF"),
        (mint, 0.15, 0.45, "#B6FAE0"),
        (theme["primary_deep"], 0.25, 0.55, "#F2C0DA"),
    ]
    for i, (col, bg_a, bd_a, txt) in enumerate(chip_palette, 1):
        repl[f"__CHIP{i}_BG__"] = rgba(col, bg_a)
        repl[f"__CHIP{i}_BORDER__"] = rgba(col, bd_a)
        repl[f"__CHIP{i}_TEXT__"] = txt
    for k, v in repl.items():
        css = css.replace(k, v)
    return css


def render_meta(items):
    parts = []
    for i, t in enumerate(items):
        if i == 0:
            parts.append(f'<span><span class="dot"></span> {t}</span>')
        else:
            parts.append(f'<span>{t}</span>')
    return "\n        ".join(parts)


def render_chips(chips):
    return "\n    ".join(f'<span class="chip" data-c="{(i % 5) + 1}">{c}</span>' for i, c in enumerate(chips))


def render_steps(steps):
    out = []
    for i, (title, desc) in enumerate(steps, 1):
        out.append(f'''      <div class="step reveal">
        <div class="step-num">{i:02d}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>''')
    return "\n".join(out)


def render_features(features):
    out = []
    for icon_svg, title, desc in features:
        out.append(f'''      <div class="feature reveal">
        <div class="icon">{icon_svg}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>''')
    return "\n".join(out)


def render_examples(items):
    out = []
    for grad, emoji, title, meta in items:
        out.append(f'''      <div class="track reveal">
        <div class="track-art" style="background: linear-gradient(135deg,{grad});">{emoji}</div>
        <div class="track-info">
          <p class="track-title">{title}</p>
          <p class="track-meta">{meta}</p>
        </div>
      </div>''')
    return "\n".join(out)


def render_plans(plans):
    out = []
    for p in plans:
        featured = ' featured' if p.get("featured") else ''
        tag = f'<span class="plan-tag">{p["tag"]}</span>' if p.get("tag") else ''
        strike = f'<div class="plan-strike">{p["strike"]}</div>' if p.get("strike") else ''
        per = f'<span class="per">{p["per"]}</span>' if p.get("per") else ''
        items = "\n          ".join(f'<li>{x}</li>' for x in p["items"])
        btn_class = "btn-primary" if p.get("featured") else "btn-ghost"
        out.append(f'''      <div class="plan{featured} reveal">
        {tag}
        <h3>{p["name"]}</h3>
        <div class="plan-price"><span class="num">{p["price"]}</span>{per}</div>
        {strike}
        <p class="plan-blurb">{p["blurb"]}</p>
        <ul>
          {items}
        </ul>
        <a href="#get" class="btn {btn_class}">{p["cta"]}</a>
      </div>''')
    return "\n".join(out)


def render_stats(stats):
    out = []
    n = len(stats)
    for i, (num, color, label) in enumerate(stats):
        col_attr = ""
        if color == "grad":
            col_attr = ' class="gradient-text"'
        elif color == "mint":
            col_attr = ' style="color: var(--mint);"'
        elif color == "yellow":
            col_attr = ' style="color: var(--yellow);"'
        full_width = ' style="grid-column: 1 / -1;"' if (n == 3 and i == 2) else ''
        out.append(f'''      <div class="stats-card"{full_width}>
        <div class="num"{col_attr}>{num}</div>
        <p style="margin:8px 0 0;">{label}</p>
      </div>''')
    return "\n".join(out)


def render_faq(faqs):
    out = []
    for q, a in faqs:
        out.append(f'''      <details class="reveal">
        <summary>{q}</summary>
        <div class="answer"><p>{a}</p></div>
      </details>''')
    return "\n".join(out)


def render_app(reg, content, themes):
    theme = themes[reg["theme"]]
    html = template("promo_template.html")
    repl = {
        "__APP_NAME__": content["name"],
        "__TAGLINE__": content["tagline"],
        "__META_DESC__": content["meta_desc"],
        "__THEME_COLOR__": theme["bg"],
        "__CSS__": render_css(theme),
        "__NAV_EXAMPLES__": content.get("nav_examples", "Examples"),
        "__HERO_EYEBROW__": content["hero_eyebrow"],
        "__HEADLINE_PRE__": content["headline_pre"],
        "__HEADLINE_ACCENT__": content["headline_accent"],
        "__LEAD__": content["lead"],
        "__META_ITEMS__": render_meta(content["meta_items"]),
        "__PHONE_CONTENT__": content["phone_content"],
        "__MARQUEE_CHIPS__": render_chips(content["chips"]),
        "__HOW_HEAD_PRE__": content["how_head_pre"],
        "__HOW_HEAD_ACCENT__": content["how_head_accent"],
        "__HOW_LEAD__": content["how_lead"],
        "__STEPS__": render_steps(content["steps"]),
        "__FEAT_HEAD_PRE__": content["feat_head_pre"],
        "__FEAT_HEAD_LINE2__": content["feat_head_line2"],
        "__FEATURES__": render_features(content["features"]),
        "__EX_EYEBROW__": content["ex_eyebrow"],
        "__EX_HEAD__": content["ex_head"],
        "__EX_LEAD__": content["ex_lead"],
        "__EXAMPLES__": render_examples(content["examples"]),
        "__PRICING_LEAD__": content["pricing_lead"],
        "__PLANS__": render_plans(content["plans"]),
        "__WHY_EYEBROW__": content["why_eyebrow"],
        "__WHY_HEAD_PRE__": content["why_head_pre"],
        "__WHY_HEAD_ACCENT__": content["why_head_accent"],
        "__WHY_LEAD__": content["why_lead"],
        "__WHY_BODY__": content["why_body"],
        "__STATS__": render_stats(content["stats"]),
        "__FAQ__": render_faq(content["faq"]),
        "__FINAL_TITLE__": content["final_title"],
        "__FINAL_BODY__": content["final_body"],
        "__FOOTER_BLURB__": content["footer_blurb"],
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    html = html.replace("__SUBDOMAIN__", reg["folder"])
    html = html.replace("__OG_IMAGE_ALT__",
                        content.get("og_image_alt", f'{content["name"]} — {content["tagline"]}'))
    out = SITE_ROOT / reg["folder"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return out, len(html)


def main():
    only = parse_only_arg(sys.argv)
    themes = load_themes()
    missing = []
    for reg in load_apps():
        folder = reg["folder"]
        if only and folder != only:
            continue
        if reg.get("user_authored"):
            print(f"  {folder}: user-authored — never regenerated, skipping")
            continue
        content_path = CONTENT_DIR / f"{folder}.json"
        if not content_path.exists():
            missing.append(folder)
            print(f"  {folder}: NO CONTENT FILE ({content_path})")
            continue
        content = json.loads(content_path.read_text())
        absent = [k for k in CONTENT_KEYS if k not in content]
        if absent:
            missing.append(folder)
            print(f"  {folder}: content file missing keys: {', '.join(absent)}")
            continue
        out, size = render_app(reg, content, themes)
        print(f"  ✓ {folder}: wrote {out} ({size:,} bytes)")
    if missing:
        print(f"\nMissing/incomplete content for: {', '.join(missing)}")
        print("Create data/content/<folder>.json — copy an existing one as a template.")
        print(f"Required keys: {', '.join(CONTENT_KEYS)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
