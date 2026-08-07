#!/usr/bin/env python3
"""Deploy the site to Hostinger — fully automated, no FTP credentials needed.

How it works:
  1. Stamps public_html/version.txt, commits, pushes to GitHub (public repo).
  2. Via the Hostinger API, creates a temporary every-minute cron job on the
     hosting account that downloads the pinned-commit tarball from GitHub and
     rsyncs public_html/ into the live docroot (--delete, with safety excludes).
  3. Polls the cron output until the DEPLOYED marker appears, then deletes the
     cron job (always, even on failure).
  4. Verifies the deploy by fetching https://froggyeye.com/version.txt.

Requires HOSTINGER_API_TOKEN in the environment (set in ~/.zshenv).
Run from anywhere:  python3 deploy.py   [--skip-push if already pushed]
"""
import json, os, subprocess, sys, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import SITE_ROOT

REPO_ROOT = SITE_ROOT.parent
API = "https://developers.hostinger.com/api/hosting/v1"
DOMAIN = "froggyeye.com"
GH_REPO = "FroggyEye-Ltd/froggyeye-ltd.github.io"
DOCROOT = "domains/froggyeye.com/public_html"
# Server-side files never touched/deleted by the sync:
EXCLUDES = [".well-known", ".htaccess", "error_log", "cgi-bin", "*.log"]

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
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"Hostinger API {method} {path} failed: {e.code} {e.read().decode()[:300]}")


def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout.strip()


def hosting_username():
    sites = api("GET", "/websites")["data"]
    for s in sites:
        if s["domain"] == DOMAIN or s.get("parent_domain") == DOMAIN:
            return s["username"]
    sys.exit(f"No Hostinger website found for {DOMAIN}")


def main():
    skip_push = "--skip-push" in sys.argv

    if not skip_push:
        dirty = git("status", "--porcelain")
        real_changes = [l for l in dirty.splitlines() if "version.txt" not in l]
        if real_changes:
            sys.exit("Working tree has uncommitted changes — commit them first:\n" + "\n".join(real_changes))
        stamp = f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {git('rev-parse', '--short', 'HEAD')}"
        (SITE_ROOT / "version.txt").write_text(stamp + "\n")
        git("add", "public_html/version.txt")
        if git("status", "--porcelain", "public_html/version.txt"):
            git("commit", "-m", f"Deploy {stamp}", "-m", "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>")
        print(f"Pushing to GitHub… ({stamp})")
        git("push", "origin", "main")

    sha = git("rev-parse", "HEAD")
    stamp = (SITE_ROOT / "version.txt").read_text().strip()
    username = hosting_username()
    print(f"Hosting account: {username}, deploying commit {sha[:12]}")

    # Cron commands are capped at 255 chars, so the real work lives in
    # deploy_remote.sh (in this repo); the cron just fetches and runs it.
    script_url = (f"https://raw.githubusercontent.com/{GH_REPO}/main/"
                  ".claude/skills/froggyeye-website/scripts/deploy_remote.sh")
    cmd = f"curl -sL {script_url} -o /tmp/fe_deploy.sh && bash /tmp/fe_deploy.sh"
    assert len(cmd) <= 255 and not any(c in cmd for c in "|<>")

    print("Creating deploy cron job…")
    api("POST", f"/accounts/{username}/cron-jobs", {"time": "* * * * *", "command": cmd})
    uid = None
    for j in api("GET", f"/accounts/{username}/cron-jobs")["data"]:
        if "fe_deploy.sh" in j["command"]:
            uid = j["uid"]
    if not uid:
        sys.exit("Could not find the created cron job")

    try:
        print("Waiting for the cron to run (fires on the next minute boundary)…")
        deadline = time.time() + 240
        output = ""
        while time.time() < deadline:
            time.sleep(15)
            output = api("GET", f"/accounts/{username}/cron-jobs/{uid}/output").get("output", "")
            if output.strip():
                break
        if f"DEPLOYED {stamp}" not in output:
            sys.exit(f"Deploy cron did not report success. Output:\n{output or '(no output — cron may not have run yet)'}")
        print(f"Server reported: {output.strip().splitlines()[-1]}")
    finally:
        api("DELETE", f"/accounts/{username}/cron-jobs/{uid}")
        print("Deploy cron job removed.")

    print("Verifying live site…")
    live = ""
    for _ in range(6):
        try:
            with urllib.request.urlopen(f"https://{DOMAIN}/version.txt?nocache={int(time.time())}", timeout=15) as r:
                live = r.read().decode().strip()
        except Exception:
            pass
        if live == stamp:
            break
        time.sleep(10)
    if live == stamp:
        print(f"✓ Live: https://{DOMAIN} is serving {stamp}")
    else:
        sys.exit(f"Live version.txt mismatch: expected {stamp!r}, got {live!r} (CDN cache may need a few minutes)")


if __name__ == "__main__":
    main()
