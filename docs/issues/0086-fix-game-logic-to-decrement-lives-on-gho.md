---
id: "0086"
title: "Fix game logic to decrement lives on ghost collision and integrate power-up effect"
type: "bug"
status: "done"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "The game logic correctly handles player lives and power-ups"
accept: "pytest tests/test_player_movement_kinematics.py"
---

The current game logic does not decrement player lives on ghost collision correctly and does not fully integrate the power-up state effect on ghost behavior and game state transitions.

This task is to:
- Update the collision detection logic to decrement lives on ghost collision when no power-up is active.
- Implement the power-up effect that allows the player to 'eat' ghosts.
- Ensure game state transitions to LOST only when lives reach zero.

Acceptance criteria:
- Player lives decrement on ghost collision without power-up.
- Power-up state allows ghost capture and prevents life loss.
- Game state transitions correctly based on lives and power-up.

This serves the objective: "The game logic correctly handles player lives and power-ups" from BOARD_BRIEF.md.

> 2026-08-05 — Closed by the co-founder: the product imports again. One of many duplicates of the same failure.
