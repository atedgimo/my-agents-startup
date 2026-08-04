# Pulse 2026-08-04 19:50

**Trigger:** 11 open bug(s) blocking the release  
**Dispatched to:** startup-tech-lead

## Task

Bugs #0050, #0056, #0057, #0058, #0059 block the release. Read the first one, tell the right developer (agent tool) to fix the code and commit it, then move that card to review. One bug this cycle. No new feature work.

WARNING: this is attempt 2 at the SAME task — the previous attempt did not change the repository. Do the concrete tool call that fixes it, and do not repeat work already done.

Note: 5 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

The error message says that src/backend/main.py imports 'src.backend.ghost_ai', but that module does not exist. However, the current content of main.py on the card's branch does not show any import of 'src.backend.ghost_ai'. It only has a commented-out import of 'src.backend.ghosts' which is also not present.

This suggests that the error message might be from a different branch or an older state.

I will check the full content of main.py for any import of 'src.backend.ghost_ai' or 'ghost_ai' to confirm and then fix it.

If found, I will replace it with the correct import from 'src.backend.ghost_visuals' as the module we created is ghost_visuals.py.

I will read the full main.py file now.
