# Pulse 2026-08-08 08:44

**Trigger:** 3 card(s) awaiting verification  
**Dispatched to:** startup-senior-dev

## Task

Cards #0018, #0019, #0020 are in review. For each: read the code and run its acceptance command. Move genuinely working cards to done with update_issue. If one fails, move it back to in-progress with a comment naming the failure — do NOT open a new bug card for it; the card itself already tracks the work.

Note: 2 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The backend has modules for ghost AI (src/backend/ghost_ai.py) with classes Ghost, GhostIdentity, GhostManager, and GhostState.

There is a GET API route /ghost-states in src/backend/main.py, but nothing calls it currently.

Other routes exist for pellets and power-pellets, but they are also not called by anything.

The ghost visual identifiers and state logic feature likely relates to the ghost_ai.py module and the /ghost-states route.

Given that /ghost-states is not called by anything, this might indicate incomplete integration or missing frontend calls.

Next, I will check the tests/acceptance directory for any tests related to ghost visuals or ghost states to verify if the feature is tested and working.
