"""C3 — score and lives are shown live while playing.

Static proxy: the page or game code must both DISPLAY score and lives and
UPDATE them from game state. Text that never changes is a label, not a HUD."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _sources():
    out = []
    for cand in ("src/index.html", "src/frontend/index.html", "src/game.js"):
        p = ROOT / cand
        if p.is_file():
            out.append(p.read_text(encoding="utf-8", errors="replace").lower())
    assert out, "no page or game code found"
    return "\n".join(out)


def test_score_and_lives_are_displayed_and_updated():
    text = _sources()
    assert "score" in text, "nothing in the page or game code mentions a score"
    assert "lives" in text, "nothing in the page or game code mentions lives"
    assert any(k in text for k in ("textcontent", "innertext", "innerhtml",
                                   "filltext", "drawscore", "updatescore")), (
        "score/lives appear as words but nothing ever renders them — "
        "no textContent/innerText/fillText style update found")
