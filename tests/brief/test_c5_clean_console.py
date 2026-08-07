"""C5 — steady play with no console errors.

Headless proxy (no browser here): every shipped JS file parses, and every
script the page references actually exists. Missing files and syntax errors
are the two commonest sources of a red console."""
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]


def test_every_js_file_parses():
    bad = []
    for js in (ROOT / "src").rglob("*.js"):
        r = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
        if r.returncode != 0:
            bad.append(f"{js.relative_to(ROOT)}: {r.stderr.strip().splitlines()[-1][:80]}")
    assert not bad, "JS that cannot parse guarantees console errors:\n" + "\n".join(bad)


def test_every_script_the_page_references_exists():
    missing = []
    for cand in ("src/index.html", "src/frontend/index.html"):
        page = ROOT / cand
        if not page.is_file():
            continue
        html = page.read_text(encoding="utf-8", errors="replace")
        for src in re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html):
            if src.startswith(("http", "//")):
                continue
            rel = (page.parent / src).resolve()
            if not rel.is_file():
                missing.append(f"{cand} → {src}")
    assert not missing, "the page loads scripts that do not exist:\n" + "\n".join(missing)
