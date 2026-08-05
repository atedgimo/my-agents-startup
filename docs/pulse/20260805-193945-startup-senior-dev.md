# Pulse 2026-08-05 19:39

**Trigger:** your card #0014 is in-progress  
**Dispatched to:** startup-senior-dev

## Task

Card #0014 is yours: [part] #0004.3 Boundary Enforcement.

Write the actual files with write_repo_file or edit_repo_file (pass card="0014"), then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

Note: 1 question(s) await the co-founder. Do not block on them — proceed with your best judgement and state your assumption.

## Outcome

I have implemented the boundary enforcement logic in src/backend/collision.py as part of card #0014. The CollisionDetector class now treats out-of-bounds as walls and provides methods to check if a move is valid and to detect collisions with walls, pellets, power pellets, and ghosts.

I moved the card #0014 to review with a comment summarizing the work done.

Next steps would be to wire this collision detection into the game movement logic and ensure it is called by the game state updates, so the boundary enforcement is active during gameplay. Let me know if you want me to proceed with that or anything else.
