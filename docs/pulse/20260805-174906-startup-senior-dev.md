# Pulse 2026-08-05 17:49

**Trigger:** BRIEF unmet (in progress): Playable end to end in a browser: arrow keys move Pa  
**Dispatched to:** startup-senior-dev

## Task

THE CO-FOUNDER ASKED FOR THIS, AND IT IS NOT DONE:
  "Playable end to end in a browser: arrow keys move Pac-Man, ghosts chase, eating all pellets wins the level."

Card #0050 — Bug: Missing tests and implementation for ghost visual identifiers and state logic — serves it.

The command that decides this card is:
  $ pytest -q tests/test_ghost_visuals.py
Right now it prints:
odules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_ghost_visuals.py:2: in <module>
    from src.backend.ghost_ai import GhostVisual
E   ModuleNotFoundError: No module named 'src'
=========================== short test summary info ============================
ERROR tests/test_ghost_visuals.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.06s

YOUR TURN SUCCEEDS ONLY IF THAT OUTPUT CHANGES. Write or edit the source files that make it pass, with write_repo_file / edit_repo_file and card="0050". Then move the card to review.

Do NOT create a card, file a bug, or write a document this cycle. Those do not make the command pass. If you genuinely cannot proceed, say precisely which file you would need and why — in your reply, not as a new card.

WARNING: this is attempt 2 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

## Outcome

The test_power_pellet_deactivation_and_revert_state failure suggests that ghosts are not reverting to their original states after power pellet ends.

The current GhostManager.update method only reverts states if power_pellet_active is True and the timer expired, but the test calls deactivate_power_pellet before update, which sets power_pellet_active to False.

Thus, the revert code in update is not running after deactivate_power_pellet.

I will fix this by moving the revert logic into deactivate_power_pellet itself, so that when the power pellet is deactivated, ghosts immediately revert to their original states.

I will now update src/backend/ghost_ai.py accordingly.
