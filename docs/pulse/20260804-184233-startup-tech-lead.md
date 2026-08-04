# Pulse 2026-08-04 18:42

**Trigger:** 7 open bug(s) blocking the release  
**Dispatched to:** startup-tech-lead

## Task

Bugs #0050, #0056, #0057, #0058, #0059 block the release. Read the first one, tell the right developer (agent tool) to fix the code and commit it, then move that card to review. One bug this cycle. No new feature work.

Note: 4 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The test file tests/test_ghost_visuals.py imports from src.backend.ghosts, but the bug card #0050 and acceptance test expect src/backend/ghost_visuals.py to exist and be the source module.

The senior dev committed code on the card branch, but the file src/backend/ghost_visuals.py is missing. Also, the test file imports from a different module name (ghosts vs ghost_visuals).

I will instruct the senior dev to fix the import and file naming to match the acceptance criteria: create src/backend/ghost_visuals.py and update tests/test_ghost_visuals.py to import from src.backend.ghost_visuals.

This fix is required to pass the acceptance test pytest -q tests/test_ghost_visuals.py.
