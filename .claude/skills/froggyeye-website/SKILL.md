---
name: froggyeye-website
description: Manage the Froggy Eye Ltd website at froggyeye.com — the studio main page plus per-app promo subdomains, with fully automated deploy to Hostinger. Use this whenever the user asks to add a new app, update store assets, regenerate a promo page, refresh SEO/sitemap, change shared elements (footer, logo, emails), deploy the site, or add a subdomain. Triggers include: "add an app", "update the website", "deploy the site", "rebuild the promo page for X", "fetch new screenshots", "regenerate the site", "the store URLs are out of date".
---

# Froggy Eye Ltd website skill

This skill manages the Froggy Eye Ltd website (`froggyeye.com`) — a UK indie app studio site with one main page plus 18 per-app promotional subdomains, all hosted on Hostinger.

## Site map at a glance

```
public_html/
├── index.html                  # Main studio site (apps grid, links to subdomains)
├── icons/                      # Shared icons + corporate logo
│   ├── logo.png                # Icon-only crop (used in nav 56px, footer, favicon)
│   ├── logo-full.png           # Full lockup with "FROGGY EYE LTD" wordmark (hero only)
│   └── <app>.png               # Per-app icon used on the main-site card
├── privacy.html                # Privacy policy
├── terms.html                  # Terms of service
├── app-ads.txt                 # Google AdMob verification
├── sitemap.xml                 # Generated; lists main + all subdomains
├── robots.txt                  # Allows GPTBot/ClaudeBot/PerplexityBot etc.
├── llms.txt                    # AI-agent discovery file
└── <app>/                      # One folder per app subdomain (18 of them)
    ├── index.html              # Promo page (studysingalong design language)
    ├── icon.png                # App icon
    ├── feature.png             # Play Store feature graphic, 2048×1365 (3:2)
    └── screenshot1.png         # First Play Store phone screenshot, full-bleed in mockup
```

The 18 subdomains map to subfolders under `public_html/`. They are served by Hostinger as `<folder>.froggyeye.com`. Apple App Store and Google Play URLs are populated via real listings; subdomains for apps that aren't on a particular store hide that download button via `[data-na]` CSS.

## App registry

The single source of truth for per-app metadata is `data/apps.json` in this skill. It contains, for every app:
- `folder` — subdomain folder name (matches Hostinger subdomain)
- `name`, `tagline`, `category` — stored as RAW text (no HTML entities); scripts escape at render time
- `theme` — preset name from `data/themes.json` (controls page colour palette)
- `package_id` — Android applicationId (for fetching Play Store listing)
- `apple_id` — App Store numeric ID (or `null`)
- `apple_url`, `play_url` — full store URLs (or `null` if not yet listed)
- `user_authored` (optional, true) — page was hand-built, NOT template-rendered. Scripts never
  regenerate/patch these pages or overwrite their per-sub llms.txt/sitemap/robots
  (currently: studysingalong, luckynumbers, postpilot)
- `extra_pages` (optional) — extra HTML pages under the subdomain to list in the main sitemap
- `llms_desc` (optional) — richer description for the root llms.txt line

The page COPY for template-rendered apps lives in `data/content/<folder>.json` — headline,
eyebrow, lead, chips, steps, features (with inline SVG icons), examples, plans, stats, faq,
plus optional `og_image_alt`, `seo_title`, `seo_desc` overrides. To author a new app's page,
copy an existing content file as a schema reference and write fresh copy.

Whenever you need per-app data, **read `data/apps.json` first**. Don't hardcode app lists.

## Common workflows

### 1. Add a new app

```
1. Read data/apps.json; append a new entry (folder, name, tagline, category,
   schema_category, theme, package_id, card_emoji, card_gradient)
2. Write data/content/<folder>.json — the page copy (copy an existing file as schema)
3. Run scripts/gen_promo.py --only <folder>   # renders the subdomain page
4. Run scripts/fetch_store_assets.py --only <folder>   # pulls screenshots + feature graphic
   (needs a LIVE Play listing — if not live yet, drop icon.png/feature.png/screenshot1.png
   into public_html/<folder>/ from the app repo's store_assets/ instead)
5. Run scripts/postprocess.py --only <folder>          # screenshots, store URLs, studio bar
6. Run scripts/regen_main_index.py                     # rebuilds the main site grid
7. Run scripts/seo_enhance.py && scripts/discovery_enhance.py  # sitemap, llms.txt, JSON-LD
8. Run scripts/create_subdomain.py <folder>            # creates <folder>.froggyeye.com via API
9. Run scripts/deploy.py                               # commit-stamp, push, deploy, verify live
```

### 2. Refresh store assets (screenshots + feature graphics)

When apps are updated on the Play Store, re-pull:
```
python3 scripts/fetch_store_assets.py
python3 scripts/postprocess.py
```

### 3. Refresh real App Store / Play Store URLs

If the user has just published a new app or you suspect URLs are stale:
```
python3 scripts/refresh_store_urls.py
```
This uses the iTunes Search API (filtered by artistName "Froggy Eye Ltd") plus a Play Store HTTP check, and updates `data/apps.json` in-place.

### 4. Regenerate one promo page (e.g. after content edits)

```
python3 scripts/gen_promo.py --only <folder>
python3 scripts/postprocess.py --only <folder>
```

### 5. Regenerate the main index

```
python3 scripts/regen_main_index.py
```

### 6. Update logos site-wide

Place new logo files at `public_html/icons/logo.png` (icon-only crop, 512×512) and `public_html/icons/logo-full.png` (full wordmark, 1024×1024). The main site auto-references these — no HTML edits needed.

### 7. Deploy to Hostinger (automated — no zip, no FTP)

```
python3 scripts/deploy.py
```

This stamps `public_html/version.txt`, commits + pushes to GitHub, then uses the
Hostinger API (`HOSTINGER_API_TOKEN` in `~/.zshenv`) to run a temporary cron job on
the hosting account that pulls the repo tarball and rsyncs `public_html/` into the
live docroot, then verifies `https://froggyeye.com/version.txt` matches. Takes ~2 min
(cron fires on minute boundaries). Requires a clean git tree — commit content changes
first so the deploy commit is just the version stamp.

Legacy fallback (manual): `python3 scripts/build_zip.py` → `~/Desktop/froggyeye-website.zip`
→ Hostinger File Manager → public_html → Upload → Extract.

### 8. Sanity check

```
python3 scripts/sanity.py
```
Reports per app: presence of feature.png + screenshot1.png + icon.png, whether the page has Apple/Google store URLs, whether it has the studio bar, whether it has JSON-LD, etc.

## Design language

Every promo page mirrors the **Study Singalong** design (the user's gold standard):
- Dark theme with brand magenta→violet gradient on the hero
- Two-column hero: text+CTAs on left, phone mockup on right (full-bleed app screenshot inside the phone frame)
- Sticky scroll-aware nav
- Genre/use-case **marquee** strip (auto-scrolling chips)
- 3-step "How it works" section
- 6-feature grid with custom SVG icons
- 8-card examples grid
- 3-tier pricing with featured plan glowing
- Stats section (3 numbers)
- FAQ accordion
- Gradient final-CTA banner
- 4-column footer

The CSS template is `templates/promo_template.css` — it uses placeholders (`__PRIMARY__`, `__VIOLET__`, etc.) that the renderer replaces from the app's theme tokens in `data/themes.json`.

**Do not invent new themes ad-hoc**; pick one from `data/themes.json` and assign it to the app. If a brand-new colour identity is genuinely needed, add the new theme to `data/themes.json` first.

## Constraints to respect

1. **Studysingalong page is sacred** — the user authored that page directly and treats it as the design canon. Don't overwrite `studysingalong/index.html` without explicit consent. Scripts in this skill explicitly skip it during regeneration.
2. **Real Apple/Play URLs only** — never make up store URLs. Use `scripts/refresh_store_urls.py` to look them up, and if a listing genuinely doesn't exist set the field to `null`. Buttons for missing listings are hidden via `[data-na]` CSS.
3. **No fake metrics** — pricing, ratings, user counts, testimonials must reflect reality. The skill does not include a "make up testimonials" path.
4. **Email standard** — only `info@froggyeye.com` appears on the site. `support@`, `press@`, etc. should never be reintroduced.
5. **Feature graphics must be 3:2 aspect** — sourced at 2048×1365 minimum to render sharply on retina at the 720px max-width display cap.
6. **All emails go to `info@froggyeye.com`** — ensure newly added pages don't introduce alternate addresses.
7. **The studio bar** (the `← Part of Froggy Eye Ltd` strip at top of every subdomain page) must be present on every promo page.

## Hostinger

- Hosting is Hostinger shared hosting, account `u384964577`, docroot
  `/home/u384964577/domains/froggyeye.com/public_html`. Subdomains are folders inside it.
- The Hostinger API token is `HOSTINGER_API_TOKEN` in `~/.zshenv`. It can list/create/delete
  subdomains (`scripts/create_subdomain.py`) and run account cron jobs (how `scripts/deploy.py`
  deploys). There is no file-upload API and no FTP/SSH endpoint — the cron trick is the deploy path.
- Subdomains: create with `python3 scripts/create_subdomain.py <folder>` (no hPanel needed).
  After creation, DNS is an ALIAS to `<sub>.froggyeye.com.cdn.hstgr.net`, and that CDN endpoint
  can take 5–15 minutes to provision — the subdomain won't resolve until it does. This is normal;
  poll patiently, do NOT delete/recreate (that restarts the provisioning clock).
  Eyesight Angel has content JSON but no registry entry, site folder or subdomain yet — when it
  ships, add the registry entry then run workflow 1.
- The GitHub repo (FroggyEye-Ltd/froggyeye-ltd.github.io, public) is the source of truth;
  the deploy pulls from it, so anything not committed+pushed does NOT deploy.

## Files in this skill

- `SKILL.md` — this file
- `data/apps.json` — app registry (canonical source of truth)
- `data/content/<folder>.json` — per-app page copy for template-rendered apps
- `data/themes.json` — colour theme presets
- `templates/promo_template.html` — full per-app page HTML structure
- `templates/promo_template.css` — themed CSS for promo pages
- `scripts/gen_promo.py` — render one or all promo pages from templates + registry + content JSONs
- `scripts/fetch_store_assets.py` — pull feature.png + screenshot1.png from Play Store listings
- `scripts/refresh_store_urls.py` — refresh App Store + Play Store URLs in apps.json
- `scripts/postprocess.py` — inject screenshots / feature banner / store URLs / studio bar into rendered pages
- `scripts/regen_main_index.py` — render the main `public_html/index.html`
- `scripts/seo_enhance.py` — refresh main-domain JSON-LD, canonical, sitemap.xml, robots.txt, llms.txt
- `scripts/discovery_enhance.py` — comprehensive search/AI discovery: FAQPage + BreadcrumbList JSON-LD, per-subdomain sitemap/robots/llms files, og:image dimensions, dns-prefetch hints, internal cross-link "More apps" section, humans.txt + security.txt
- `scripts/sanity.py` — audit current site state
- `scripts/deploy.py` — automated deploy to Hostinger (push + API cron + live verify)
- `scripts/deploy_remote.sh` — the server-side half of deploy.py (fetched by the cron)
- `scripts/create_subdomain.py` — create/list/delete `<app>.froggyeye.com` subdomains via the Hostinger API
- `scripts/build_zip.py` — legacy manual fallback: package public_html for hand upload
- `scripts/legacy/` — historical one-off generators (content now extracted to data/content/)

## When invoked

If the user invokes this skill without specifying what to do, ask them which workflow they want — the list under "Common workflows" above. Don't run anything destructive (regen, postprocess) without an explicit ask.

If they ask something this skill clearly handles ("update the store URLs", "rebuild ApexRoute's page", etc.), pick the right workflow and run it.
