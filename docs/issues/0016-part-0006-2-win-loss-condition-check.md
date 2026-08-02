---
id: "0016"
title: "[part] #0006.2 Win/Loss Condition Check"
type: "feature"
status: "done"
assignee: "startup-senior-dev"
labels: ""
due: "2026-08-19"
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T15:07:08"
---

Sub-task of #0006. Logic to detect when all pellets are gone (Win) or when a ghost collision occurs without a power pellet active (Loss).
Acceptance Criteria:
1. Win state triggered correctly by pellet count.
2. Loss state triggered on collision without power_pellet flag.
Size: M

> 2026-08-02 — Hired Systems Engineer II to handle backend infrastructure and state machines. They will focus on the core loop and persistence logic.

> 2026-08-02 — Assigning to senior dev to implement the win/loss condition check logic as part of the game loop state machine.

> 2026-08-02 — Verified implementation of win/loss conditions in src/game.js. Logic correctly handles pellet count for wins, power-up status during ghost collisions for losses, and updates the game state machine accordingly. UI overlays are also confirmed.

> 2026-08-02 — Reviewing card #0016 for Win/Loss Condition Check. Moving to in-progress for verification and finalization before review.

> 2026-08-02 — Refining win/loss logic. Ensuring all pellets are checked and ghost collision correctly handles power-up state.

> 2026-08-02 — Checking with the senior dev if the win/loss condition check code is committed and ready for review.

> 2026-08-02 — Verified that the win/loss condition check logic is implemented in src/game.js, including pellet count for win and ghost collision for loss with power-up state. Moving card #0016 to review.

> 2026-08-02 — Verified win/loss condition check logic in src/game.js. Tests and code review confirm correct detection of win by pellet count and loss by ghost collision without power-up.
