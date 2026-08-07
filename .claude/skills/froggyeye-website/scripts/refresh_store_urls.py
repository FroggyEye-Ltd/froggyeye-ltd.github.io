#!/usr/bin/env python3
"""Refresh apple_id, apple_url, play_url in apps.json by querying iTunes Search API + checking Play Store reachability."""
import json, subprocess, sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from _common import load_apps, save_apps, UA

def lookup_itunes(name):
    """Search iTunes for the app by name, filtering to Froggy Eye Ltd as artist."""
    q = name.replace(" ", "+")
    out = subprocess.run(
        ["curl", "-s", f"https://itunes.apple.com/search?term={q}&entity=software&country=gb&limit=15"],
        capture_output=True, text=True)
    try:
        for r in json.loads(out.stdout).get("results", []):
            if "froggy" in r.get("artistName", "").lower():
                return {
                    "apple_id": str(r["trackId"]),
                    "apple_url": r["trackViewUrl"].split("?")[0],
                    "name_on_store": r["trackName"],
                }
    except Exception:
        pass
    return None

def play_exists(pkg):
    """Quick HEAD-style check: fetch the listing and verify it returned 200 with expected content."""
    out = subprocess.run(
        ["curl", "-sSL", "-o", "-", "-w", "%{http_code}", "-A", UA,
         f"https://play.google.com/store/apps/details?id={pkg}"],
        capture_output=True, text=True, errors="replace")
    code = out.stdout[-3:]
    body = out.stdout[:-3]
    return code == "200" and "We're sorry" not in body and "the requested URL was not found" not in body.lower()

if __name__ == "__main__":
    apps = load_apps()
    for app in apps:
        # iTunes
        before_apple = app.get("apple_url")
        hit = lookup_itunes(app["name"])
        if hit:
            app["apple_id"]  = hit["apple_id"]
            app["apple_url"] = hit["apple_url"]
        # else leave as-is (don't null out a working URL on a single failed search)
        # Play
        pkg = app.get("package_id")
        if pkg:
            if play_exists(pkg):
                app["play_url"] = f"https://play.google.com/store/apps/details?id={pkg}"
            else:
                # Don't auto-null an existing URL on a transient failure.
                pass
        change = "·"
        if hit and before_apple != hit["apple_url"]:
            change = "+apple"
        print(f"  {app['folder']:22s} apple={'Y' if app.get('apple_url') else '-'}  play={'Y' if app.get('play_url') else '-'}  {change}")
    save_apps(apps)
    print("\nUpdated data/apps.json.")
