# Pulse 2026-08-04 20:21

**Trigger:** BRIEF unmet (in progress): Playable end to end in a browser: arrow keys move Pa  
**Dispatched to:** startup-senior-dev

## Task

THE CO-FOUNDER ASKED FOR THIS, AND IT IS NOT DONE:
  "Playable end to end in a browser: arrow keys move Pac-Man, ghosts chase, eating all pellets wins the level."

Card #0050 — Bug: Missing tests and implementation for ghost visual identifiers and state logic — serves it.

NOTHING can pass until the product imports. Fix this FIRST, by writing the missing file with write_repo_file — not by renaming the import to another module that also does not exist, and not by filing a bug about it:
  src/backend/main.py: imports 'src.backend.ghost_ai', but src/backend/ghost_ai.py does not exist. The product will crash on startup with ModuleNotFoundError. Write that module, or import something that is actually there — project_map(scope='product') lists every module that exists.
  src/backend/main.py: imports 'src.backend.ghost_visuals', but src/backend/ghost_visuals.py does not exist. The product will crash on startup with ModuleNotFoundError. Write that module, or import something that is actually there — project_map(scope='product') lists every module that exists.

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

WARNING: this is attempt 2 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

Note: 5 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

Error code: 429 - {'error': {'message': 'Rate limit reached for gpt-4.1-mini in organization org-fNy7aB1Vt2bem0177dkjnnRp on tokens per min (TPM): Limit 200000, Used 196249, Requested 9438. Please try again in 1.706s. Visit https://platform.openai.com/account/rate-limits to learn more.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}
