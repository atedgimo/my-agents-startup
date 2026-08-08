# Pulse 2026-08-08 09:32

**Trigger:** your card #0095 is todo  
**Dispatched to:** startup-backend-python-dev

## Task

BRIEF SCORE: 3/5 — failing: c2_ghosts, c4_persistence. A close that would LOWER this score is refused.

Card #0095 is yours: Implement GhostManager and GhostState logic for ghost visual identifiers and state logic.

Make the change with ONE call to edit_code(card="0095", instruction="...") — describe the whole change in the instruction; it reads and edits the files itself and costs a fraction of doing it by hand. Reserve write_repo_file/edit_repo_file for docs and one-line tweaks. Then run make_check_pass(card="0095") until it reports GREEN, then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

Note: 3 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

I implemented the GhostManager and GhostState logic for ghost visual identifiers and state management in src/backend/ghost_ai.py as required by card #0095. However, the implementation currently causes multiple test failures related to ghost state handling. I moved the card back to todo with a comment explaining the test failures. I will now review and fix the implementation to pass the tests.
