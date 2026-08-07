# Pulse 2026-08-07 18:54

**Trigger:** your card #0020 is in-progress  
**Dispatched to:** startup-senior-dev

## Task

Card #0020 is yours: Feature: Implement Ghost Visual Identifiers & State Logic.

Make the change with ONE call to edit_code(card="0020", instruction="...") — describe the whole change in the instruction; it reads and edits the files itself and costs a fraction of doing it by hand. Reserve write_repo_file/edit_repo_file for docs and one-line tweaks. Then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

Note: 4 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

I have implemented the Ghost Visual Identifiers and State Logic in the backend, including the ghost_ai.py module with GhostState, GhostIdentity, Ghost, and GhostManager classes. I also added the /ghost-states API route in main.py to expose ghost states for the frontend.

I added an acceptance test command to run the existing acceptance test for ghost visuals to verify the implementation.

The card #0020 is now ready for review.
