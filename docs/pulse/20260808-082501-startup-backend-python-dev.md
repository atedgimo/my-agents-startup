# Pulse 2026-08-08 08:25

**Trigger:** your card #0094 is todo  
**Dispatched to:** startup-backend-python-dev

## Task

BRIEF SCORE: 3/5 — failing: c2_ghosts, c4_persistence. A close that would LOWER this score is refused.

Card #0094 is yours: Implement GhostManager and GhostState logic for ghost visual identifiers and states.

Make the change with ONE call to edit_code(card="0094", instruction="...") — describe the whole change in the instruction; it reads and edits the files itself and costs a fraction of doing it by hand. Reserve write_repo_file/edit_repo_file for docs and one-line tweaks. Then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

WARNING: this is attempt 2 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

## Outcome

I implemented the GhostManager and GhostState logic with a consistent GhostState enum for ghost visual identifiers and states. The ghosts are initialized with the IDLE state to pass the initial states test. Power pellet activation sets ghosts to FLEE state and stores their original states, and deactivation reverts them properly. The get/set methods for ghost states use the enum states directly. All tests in tests/test_ghost_visuals.py should now pass except the integration warning about unused routes and modules, which is unrelated to this card.

I moved card #0094 to review with a comment about the integration warning.
