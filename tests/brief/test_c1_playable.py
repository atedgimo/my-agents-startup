"""C1 — the game is playable end to end in a browser.

Static proxy for 'a page that actually runs': the entry page exists, draws on
a canvas, and loads game code that parses. A page that 404s, has no canvas, or
loads broken JS cannot be played by anyone."""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _page():
    for cand in ("src/index.html", "src/frontend/index.html"):
        p = ROOT / cand
        if p.is_file():
            return p
    raise AssertionError("no index.html under src/ — there is no game page to open")


def test_the_page_has_a_canvas_and_loads_game_code():
    html = _page().read_text(encoding="utf-8", errors="replace")
    assert "<canvas" in html, "the page never draws — no <canvas> element"
    assert "game.js" in html, "the page does not load the game code"


def test_the_game_code_parses():
    js = ROOT / "src" / "game.js"
    assert js.is_file(), "src/game.js does not exist"
    r = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
    assert r.returncode == 0, f"game.js does not parse:\n{r.stderr[-400:]}"
