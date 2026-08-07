#!/usr/bin/env python3
"""Build a fresh zip of public_html ready for Hostinger upload.
Output: ~/Desktop/froggyeye-website.zip"""
import os, subprocess, sys
from pathlib import Path

SITE_ROOT = Path("/Users/kevinlam/froggyeye-ltd.github.io/public_html")
OUT = Path.home() / "Desktop" / "froggyeye-website.zip"

if OUT.exists():
    OUT.unlink()
os.chdir(SITE_ROOT)

# Build the zip with contents-only (no wrapping public_html/ folder), excluding .DS_Store
# Use the system zip — efficient and avoids needing Python zipfile boilerplate.
items = sorted(p for p in Path(".").iterdir() if not p.name.startswith("."))
cmd = ["zip", "-rq", str(OUT)] + [str(p) for p in items] + ["-x", "*.DS_Store"]
subprocess.check_call(cmd)
print(f"Wrote {OUT}  ({OUT.stat().st_size / 1024 / 1024:.1f} MB)")
print(f"Upload to Hostinger File Manager → public_html → Upload → Extract.")
