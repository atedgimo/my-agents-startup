# Pulse 2026-08-08 09:35

**Trigger:** your card #0050 is in-progress  
**Dispatched to:** startup-senior-dev

## Task

BRIEF SCORE: 3/5 — failing: c2_ghosts, c4_persistence. A close that would LOWER this score is refused.

Card #0050 is yours: Bug: Missing tests and implementation for ghost visual identifiers and state logic.

It serves what the co-founder asked for:
  "Playable end to end in a browser: arrow keys move Pac-Man, ghosts chase, eating all pellets wins the level."

The command that decides it:
  $ pytest -q tests/test_ghost_visuals.py
Right now it prints:
..........                                                               [100%]
10 passed in 20.25s

YOUR TURN SUCCEEDS ONLY IF THAT OUTPUT CHANGES.

Make the change with ONE call to edit_code(card="0050", instruction="...") — describe the whole change in the instruction; it reads and edits the files itself and costs a fraction of doing it by hand. Reserve write_repo_file/edit_repo_file for docs and one-line tweaks. Then run make_check_pass(card="0050") until it reports GREEN, then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

Note: 3 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

I have implemented the missing ghost visual identifiers and state logic in the backend, added the necessary API endpoints, and created comprehensive tests for ghost visuals and state transitions. All tests pass successfully.

The card #0050 is now moved to review. However, note that several routes have no client calls, which is an integration advisory warning and does not block the review. These routes and unused modules should be either wired up or removed to avoid shipping unreachable code.
