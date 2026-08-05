# Pulse 2026-08-05 17:45

**Trigger:** BRIEF unmet (in progress): Playable end to end in a browser: arrow keys move Pa  
**Dispatched to:** startup-senior-dev

## Task

THE CO-FOUNDER ASKED FOR THIS, AND IT IS NOT DONE:
  "Playable end to end in a browser: arrow keys move Pac-Man, ghosts chase, eating all pellets wins the level."

Card #0050 — Bug: Missing tests and implementation for ghost visual identifiers and state logic — serves it.

The command that decides this card is:
  $ pytest -q tests/test_ghost_visuals.py
Right now it prints:
ve valid Python names.
Traceback:
/usr/local/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_ghost_visuals.py:2: in <module>
    from src.backend.ghost_visuals import GhostManager, GhostState
E   ModuleNotFoundError: No module named 'src'
=========================== short test summary info ============================
ERROR tests/test_ghost_visuals.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.06s

YOUR TURN SUCCEEDS ONLY IF THAT OUTPUT CHANGES. Write or edit the source files that make it pass, with write_repo_file / edit_repo_file and card="0050". Then move the card to review.

Do NOT create a card, file a bug, or write a document this cycle. Those do not make the command pass. If you genuinely cannot proceed, say precisely which file you would need and why — in your reply, not as a new card.

## Outcome

The acceptance test command explicitly shows the import line it tries to run is "from src.backend.ghost_visuals import ...".

This means the test runner environment expects the import path to be "src.backend.ghost_visuals".

Therefore, the correct fix is to keep the import line in tests/test_ghost_visuals.py as:

from src.backend.ghost_visuals import GhostManager, GhostState

and ensure that the src/ and src/backend/ directories are Python packages by having __init__.py files.

I have already added empty __init__.py files to src/ and src/backend/.

The remaining issue is that the test runner environment must have the root directory (the one containing src/) in its PYTHONPATH or sys.path so that "src" is recognized as a top-level package.

Since I cannot change the test runner environment, I will try to fix this by adding a conftest.py file in tests/ that adds the root directory to sys.path at test runtime.

I will create tests/conftest.py with code to add the repo root to sys.path.

This should allow the import "from src.backend.ghost_visuals import ..." to work.

I will do this now.
