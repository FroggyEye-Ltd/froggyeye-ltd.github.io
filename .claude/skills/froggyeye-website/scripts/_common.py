"""Shared paths and helpers for the froggyeye-website skill scripts."""
import json
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SITE_ROOT  = Path("/Users/kevinlam/froggyeye-ltd.github.io/public_html")

def load_apps():
    return json.loads((SKILL_ROOT / "data" / "apps.json").read_text())

def save_apps(apps):
    # ensure_ascii=False: the registry stores card_emoji as literal characters,
    # so escaping them here would rewrite every entry on any save.
    (SKILL_ROOT / "data" / "apps.json").write_text(
        json.dumps(apps, indent=2, ensure_ascii=False) + "\n")

def load_themes():
    return json.loads((SKILL_ROOT / "data" / "themes.json").read_text())

def template(name):
    return (SKILL_ROOT / "templates" / name).read_text()

def parse_only_arg(argv):
    """Returns the value passed as --only <folder>, or None."""
    if "--only" in argv:
        i = argv.index("--only")
        if i + 1 < len(argv):
            return argv[i + 1]
    return None

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
