#!/usr/bin/env python3
"""Pull feature.png + screenshot1..N.png for every app from the Play Store listing."""
import re, subprocess, sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from _common import load_apps, SITE_ROOT, UA, parse_only_arg

URL_RE = re.compile(r'https://play-lh\.googleusercontent\.com/[A-Za-z0-9_\-]+(?:=[\w\d\-,]+)?')
FEATURE_SUF = re.compile(r'=w\d+-h\d+-pc[\w]+-pd$')
SCREENSHOT_SUF = re.compile(r'=w526-h296-rw$')

def fetch_html(pkg):
    out = subprocess.run(
        ["curl", "-sSL", "-o", "-", "-w", "%{http_code}",
         "-H", "Accept-Language: en-GB,en;q=0.9", "-A", UA,
         f"https://play.google.com/store/apps/details?id={pkg}&hl=en"],
        capture_output=True, text=True, errors="replace")
    body = out.stdout[:-3]
    code = out.stdout[-3:]
    if code == "200" and "the requested URL was not found" not in body.lower():
        return body
    return None

def extract(html):
    feature, shots, seen = None, [], set()
    for u in URL_RE.findall(html):
        suf = u.split("=", 1)[1] if "=" in u else ""
        base = u.split("=", 1)[0]
        if FEATURE_SUF.search("=" + suf) and feature is None:
            feature = u
        elif SCREENSHOT_SUF.search("=" + suf) and base not in seen:
            seen.add(base)
            shots.append(u)
    return feature, shots

def to_full(url, target_w):
    base = url.split("=", 1)[0]
    if "-pc" in url and "-pd" in url:
        return f"{base}=w{target_w}-h{int(target_w*500/1024)}-pc0xffffff-pd"
    return f"{base}=w{target_w}"

def download(url, dest):
    return subprocess.run(["curl", "-sSL", "-A", UA, "-o", str(dest), url]).returncode == 0

def process(app):
    folder = app["folder"]
    pkg = app.get("package_id")
    if not pkg:
        print(f"  {folder}: no package_id, skipping")
        return
    out_dir = SITE_ROOT / folder
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[{folder}] {pkg}")
    html = fetch_html(pkg)
    if not html:
        print("  ! Play listing not found")
        return
    feature, shots = extract(html)
    print(f"  feature: {'Y' if feature else 'N'}  screenshots: {len(shots)}")
    for old in out_dir.glob("screenshot*.png"): old.unlink()
    if (out_dir / "feature.png").exists(): (out_dir / "feature.png").unlink()
    if feature and download(to_full(feature, 1024), out_dir / "feature.png"):
        print(f"  saved feature")
    for i, s in enumerate(shots[:6], 1):
        if download(to_full(s, 720), out_dir / f"screenshot{i}.png"):
            print(f"  saved screenshot {i}")

if __name__ == "__main__":
    apps = load_apps()
    only = parse_only_arg(sys.argv)
    for app in apps:
        if only and app["folder"] != only: continue
        process(app)
    print("\nDone.")
