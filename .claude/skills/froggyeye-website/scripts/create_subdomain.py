#!/usr/bin/env python3
"""Create (or list/delete) a <folder>.froggyeye.com subdomain via the Hostinger API.

Usage:
  python3 create_subdomain.py <folder>            # create, pointing at public_html/<folder>
  python3 create_subdomain.py --list
  python3 create_subdomain.py --delete <folder>

Requires HOSTINGER_API_TOKEN in the environment (set in ~/.zshenv).
"""
import json, os, sys, urllib.request

API = "https://developers.hostinger.com/api/hosting/v1"
DOMAIN = "froggyeye.com"

TOKEN = os.environ.get("HOSTINGER_API_TOKEN")
if not TOKEN:
    sys.exit("HOSTINGER_API_TOKEN not set (see ~/.zshenv)")


def api(method, path, body=None):
    req = urllib.request.Request(
        API + path,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json",
                 "User-Agent": "froggyeye-deploy/1.0 (curl-compatible)"},
        method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"Hostinger API {method} {path} failed: {e.code} {e.read().decode()[:300]}")


def username():
    for s in api("GET", "/websites")["data"]:
        if s["domain"] == DOMAIN or s.get("parent_domain") == DOMAIN:
            return s["username"]
    sys.exit(f"No Hostinger website found for {DOMAIN}")


def main():
    u = username()
    base = f"/accounts/{u}/websites/{DOMAIN}/subdomains"
    if "--list" in sys.argv:
        print(json.dumps(api("GET", base), indent=2))
        return
    if "--delete" in sys.argv:
        sub = sys.argv[sys.argv.index("--delete") + 1]
        api("DELETE", f"{base}/{sub}")
        print(f"Deleted {sub}.{DOMAIN}")
        return
    folder = sys.argv[1]
    # NOTE: "directory" is relative to the website's public directory (public_html/) —
    # passing "public_html/<folder>" double-nests it (verified live Aug 2026).
    api("POST", base, {"subdomain": folder, "directory": folder,
                       "is_using_public_directory": False})
    print(f"Created {folder}.{DOMAIN} → public_html/{folder}")
    print("Note: SSL for the new subdomain can take a few minutes to be issued by Hostinger.")


if __name__ == "__main__":
    main()
