# Pulse 2026-08-05 19:33

**Trigger:** your card #0020 is in-progress  
**Dispatched to:** startup-backend-full-stack-devel

## Task

Card #0020 is yours: Feature: Implement Ghost Visual Identifiers & State Logic.

Write the actual files with write_repo_file or edit_repo_file (pass card="0020"), then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

## Outcome

I have implemented the core ghost visual identifiers and state logic classes in src/backend/ghost_ai.py as required by card #0020. The card is now moved to review.

Summary:
- Defined GhostState enum with all relevant states.
- Defined GhostIdentity constants.
- Implemented Ghost class with state management.
- Implemented GhostManager class to manage all ghosts, their states, power pellet activation, and state transitions.

Next steps would be to integrate these with API routes and frontend calls to make the ghost states usable in the game. But that is outside the scope of this card.
