# Pulse 2026-08-05 09:15

**Trigger:** 17 open bug(s) blocking the release  
**Dispatched to:** startup-tech-lead

## Task

Bugs #0050, #0056, #0057, #0058, #0059 block the release. Read the first one, tell the right developer (agent tool) to fix the code and commit it, then move that card to review. One bug this cycle. No new feature work.

WARNING: this is attempt 2 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

Note: 7 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The test file tests/test_ghost_visuals.py imports from src.backend.ghost_visuals, which does not exist, causing ImportError and blocking the acceptance test for bug #0050.

The tests expect a GhostManager class with methods:
- get_all_states() returning a dict of ghost names to state strings ('chase', 'ambush', etc.)
- set_ghost_state(identity, state)
- get_ghost_state(identity)
- activate_power_pellet()
- deactivate_power_pellet()
- update()

Also, the GhostState enum has states like CHASE, AMBUSH, PATROL, RANDOM, FLEE, EATEN.

The current src/backend/ghost_ai.py only has a minimal Ghost class and GhostState enum with IDLE, CHASE, FRIGHTENED.

To fix bug #0050, I must implement the full ghost_visuals module with the GhostManager, GhostState, and Ghost classes as expected by the tests.

I will create src/backend/ghost_visuals.py implementing the required classes and methods to pass the tests in tests/test_ghost_visuals.py.

Then I will move bug #0050 to review.

Proceeding to create src/backend/ghost_visuals.py.
