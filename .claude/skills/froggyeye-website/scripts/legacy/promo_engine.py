#!/usr/bin/env python3
"""Engine to render a per-app promo page from the templates and per-app data."""
from pathlib import Path

ROOT = Path("/Users/kevinlam/froggyeye-ltd.github.io/public_html")
CSS_TPL  = Path("/tmp/promo_template.css").read_text()
HTML_TPL = Path("/tmp/promo_template.html").read_text()

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgba(h, a):
    r, g, b = hex_to_rgb(h)
    return f"rgba({r},{g},{b},{a})"

def render_css(theme):
    primary = theme["primary"]            # vivid hue
    primary_deep = theme["primary_deep"]  # darker version
    violet = theme["violet"]              # second gradient stop
    mint = theme["mint"]                  # accent (used for play btn / status dots)
    yellow = theme["yellow"]              # secondary accent
    bg = theme["bg"]                      # page background
    surface = theme["surface"]            # card bg
    surface2 = theme["surface2"]          # raised card bg
    border = theme["border"]              # border color
    css = CSS_TPL
    repl = {
        "__PRIMARY__": primary,
        "__PRIMARY_DEEP__": primary_deep,
        "__VIOLET__": violet,
        "__MINT__": mint,
        "__YELLOW__": yellow,
        "__BG__": bg,
        "__SURFACE__": surface,
        "__SURFACE2__": surface2,
        "__BORDER__": border,
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
    # 5 chip color sets (alternating around the marquee)
    chip_palette = [
        (primary, 0.18, 0.5, "#FFD0E2"),
        (yellow,  0.15, 0.45, "#FFE0A0"),
        (violet,  0.18, 0.5, "#E2C7FF"),
        (mint,    0.15, 0.45, "#B6FAE0"),
        (primary_deep, 0.25, 0.55, "#F2C0DA"),
    ]
    for i, (col, bg_a, bd_a, txt) in enumerate(chip_palette, 1):
        repl[f"__CHIP{i}_BG__"] = rgba(col, bg_a)
        repl[f"__CHIP{i}_BORDER__"] = rgba(col, bd_a)
        repl[f"__CHIP{i}_TEXT__"] = txt
    for k, v in repl.items():
        css = css.replace(k, v)
    return css

def render_meta(items):
    # First item gets the green pulsing dot
    parts = []
    for i, t in enumerate(items):
        if i == 0:
            parts.append(f'<span><span class="dot"></span> {t}</span>')
        else:
            parts.append(f'<span>{t}</span>')
    return "\n        ".join(parts)

def render_chips(chips):
    return "\n    ".join(f'<span class="chip" data-c="{(i%5)+1}">{c}</span>' for i, c in enumerate(chips))

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

def render_app(app):
    css = render_css(app["theme"])
    html = HTML_TPL
    repl = {
        "__APP_NAME__": app["name"],
        "__TAGLINE__": app["tagline"],
        "__META_DESC__": app["meta_desc"],
        "__THEME_COLOR__": app["theme"]["bg"],
        "__CSS__": css,
        "__NAV_EXAMPLES__": app.get("nav_examples", "Examples"),
        "__HERO_EYEBROW__": app["hero_eyebrow"],
        "__HEADLINE_PRE__": app["headline_pre"],
        "__HEADLINE_ACCENT__": app["headline_accent"],
        "__LEAD__": app["lead"],
        "__META_ITEMS__": render_meta(app["meta_items"]),
        "__PHONE_CONTENT__": app["phone_content"],
        "__MARQUEE_CHIPS__": render_chips(app["chips"]),
        "__HOW_HEAD_PRE__": app["how_head_pre"],
        "__HOW_HEAD_ACCENT__": app["how_head_accent"],
        "__HOW_LEAD__": app["how_lead"],
        "__STEPS__": render_steps(app["steps"]),
        "__FEAT_HEAD_PRE__": app["feat_head_pre"],
        "__FEAT_HEAD_LINE2__": app["feat_head_line2"],
        "__FEATURES__": render_features(app["features"]),
        "__EX_EYEBROW__": app["ex_eyebrow"],
        "__EX_HEAD__": app["ex_head"],
        "__EX_LEAD__": app["ex_lead"],
        "__EXAMPLES__": render_examples(app["examples"]),
        "__PRICING_LEAD__": app["pricing_lead"],
        "__PLANS__": render_plans(app["plans"]),
        "__WHY_EYEBROW__": app["why_eyebrow"],
        "__WHY_HEAD_PRE__": app["why_head_pre"],
        "__WHY_HEAD_ACCENT__": app["why_head_accent"],
        "__WHY_LEAD__": app["why_lead"],
        "__WHY_BODY__": app["why_body"],
        "__STATS__": render_stats(app["stats"]),
        "__FAQ__": render_faq(app["faq"]),
        "__FINAL_TITLE__": app["final_title"],
        "__FINAL_BODY__": app["final_body"],
        "__FOOTER_BLURB__": app["footer_blurb"],
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    out = ROOT / app["folder"] / "index.html"
    out.write_text(html)
    return out, len(html)

# Reusable theme presets
THEMES = {
    "magenta_violet": {  # Used by lovescore, lovemenot etc.
        "primary": "#FF2E7E", "primary_deep": "#D11E63", "violet": "#7C3AED",
        "mint": "#3DF5B0", "yellow": "#FFE14D",
        "bg": "#0A0514", "surface": "#15091F", "surface2": "#1F1230", "border": "#2A1A3D",
    },
    "ember": {  # ApexRoute, PokePriceChecker — fiery
        "primary": "#FF4D2E", "primary_deep": "#B81D00", "violet": "#7C2D12",
        "mint": "#FBBF24", "yellow": "#FDE047",
        "bg": "#0F0805", "surface": "#1C0E08", "surface2": "#2A150E", "border": "#3D2418",
    },
    "ocean": {  # BlipBlobb — cool blue
        "primary": "#00D4FF", "primary_deep": "#0087B3", "violet": "#3B82F6",
        "mint": "#5EEAD4", "yellow": "#FACC15",
        "bg": "#040B14", "surface": "#0A1726", "surface2": "#0F2336", "border": "#1B3450",
    },
    "purple_dawn": {  # DoorDigest, NovalWeaver — moody purple
        "primary": "#A855F7", "primary_deep": "#7E22CE", "violet": "#5B21B6",
        "mint": "#67E8F9", "yellow": "#FDE047",
        "bg": "#0B0518", "surface": "#160A2A", "surface2": "#23123F", "border": "#321B58",
    },
    "mystic": {  # Eight Ball Wisdom — deep cosmic
        "primary": "#A78BFA", "primary_deep": "#7C3AED", "violet": "#4C1D95",
        "mint": "#67E8F9", "yellow": "#FDE68A",
        "bg": "#06030F", "surface": "#100823", "surface2": "#1B0F36", "border": "#2D1B52",
    },
    "cyan_safe": {  # Eyesight Angel — clinical/cool
        "primary": "#22D3EE", "primary_deep": "#0891B2", "violet": "#0E7490",
        "mint": "#5EEAD4", "yellow": "#FDE047",
        "bg": "#04101A", "surface": "#0A1F2C", "surface2": "#102D3F", "border": "#1B435C",
    },
    "forest": {  # Focus Timer — calm green
        "primary": "#34D399", "primary_deep": "#059669", "violet": "#047857",
        "mint": "#A7F3D0", "yellow": "#FDE047",
        "bg": "#04120D", "surface": "#0A2218", "surface2": "#103224", "border": "#1A4A35",
    },
    "citrus": {  # Food Score — appetising
        "primary": "#FACC15", "primary_deep": "#D97706", "violet": "#84CC16",
        "mint": "#86EFAC", "yellow": "#FEF08A",
        "bg": "#0F0A02", "surface": "#1F1604", "surface2": "#2E2008", "border": "#46300F",
    },
    "rose": {  # Love Score — romantic
        "primary": "#FB7185", "primary_deep": "#BE123C", "violet": "#9F1239",
        "mint": "#FDA4AF", "yellow": "#FED7AA",
        "bg": "#100408", "surface": "#1F0810", "surface2": "#2E0F1A", "border": "#451A2B",
    },
    "teal_pro": {  # MyLTDTax, ByeByeJob — professional
        "primary": "#14B8A6", "primary_deep": "#0F766E", "violet": "#0D9488",
        "mint": "#5EEAD4", "yellow": "#FDE047",
        "bg": "#03100E", "surface": "#072020", "surface2": "#0E2E2E", "border": "#175555",
    },
    "solar": {  # SolarWise — sun-warm
        "primary": "#FBBF24", "primary_deep": "#D97706", "violet": "#B45309",
        "mint": "#FCD34D", "yellow": "#FEF3C7",
        "bg": "#0F0A02", "surface": "#1F1606", "surface2": "#30220C", "border": "#4A3413",
    },
    "tile": {  # Tileverse — sky/map
        "primary": "#0EA5E9", "primary_deep": "#0369A1", "violet": "#1D4ED8",
        "mint": "#5EEAD4", "yellow": "#FDE047",
        "bg": "#040A14", "surface": "#0A1626", "surface2": "#102339", "border": "#1B3957",
    },
    "treasure": {  # Treasure Hunter Live — gold/adventure
        "primary": "#F59E0B", "primary_deep": "#A16207", "violet": "#854D0E",
        "mint": "#FCD34D", "yellow": "#FEF08A",
        "bg": "#0E0902", "surface": "#1B1306", "surface2": "#291E0B", "border": "#3F2C11",
    },
}
