# Pulse 2026-08-04 18:47

**Trigger:** your card #0020 is in-progress  
**Dispatched to:** startup-senior-dev

## Task

Card #0020 is yours: Feature: Implement Ghost Visual Identifiers & State Logic. Write the actual files with write_repo_file or edit_repo_file (pass card="0020"), then move it to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle.

Note: 4 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The tests in tests/test_ghost_visuals.py indicate that there should be a src/backend/ghosts.py module defining:

- GhostManager class with methods:
  - get_all_states() returning a dict of ghost names to their states as strings
  - set_ghost_state(identity, state)
  - get_ghost_state(identity)
- GhostIdentity enum with members BLINKY, PINKY, INKY, CLYDE
- GhostState enum with members CHASE, FLEE, EATEN, PATROL, AMBUSH

The tests expect initial states to be "chase" for all ghosts.

Currently, there is no src/backend/ghosts.py file in the repo. This is likely why the card #0020 is in progress but not implemented yet.

I will implement src/backend/ghosts.py with the GhostIdentity and GhostState enums, and the GhostManager class that manages ghost states with the required methods and initial states.

Then I will move card #0020 to review.

I will write the file now.
