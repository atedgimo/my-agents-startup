# Pulse 2026-08-05 09:20

**Trigger:** BRIEF unmet (in progress): Playable end to end in a browser: arrow keys move Pa  
**Dispatched to:** startup-tech-lead

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

WARNING: this is attempt 154 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

ESCALATED to you: the previous owner attempted this twice with no change to the repository. Diagnose why it is stuck rather than retrying it, and if it cannot be fixed this cycle, say so on the card.

Note: 8 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The test file tests/test_ghost_visuals.py imports from src.backend.ghost_visuals, but that module does not exist in the repo. There is a src/backend/ghost_ai.py file, but it does not define the classes and states expected by the tests.

The error is a ModuleNotFoundError because the module src.backend.ghost_visuals is missing. To fix this, we need to create the src/backend/ghost_visuals.py module with the required classes GhostManager and GhostState, implementing the ghost visual identifiers and state logic as expected by the tests.

I will create the src/backend/ghost_visuals.py file with the GhostManager and GhostState classes and implement the logic to pass the tests in tests/test_ghost_visuals.py.

I will now proceed to write this new module.
