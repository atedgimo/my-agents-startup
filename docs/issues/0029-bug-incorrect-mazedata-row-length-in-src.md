---
id: "0029"
title: "Bug: Incorrect mazeData row length in src/game.js causes potential rendering/logic errors"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
---

In src/game.js, the mazeData array has an inconsistent row length at row 5 (index 5). It contains 21 elements instead of the expected 20, which is inconsistent with other rows.

This can cause rendering issues or logic errors when accessing maze tiles by row and column indices.

Steps to reproduce:
1. Run the game frontend.
2. Observe potential misalignment or errors related to maze rendering or pellet placement.

Expected:
All rows in mazeData should have exactly 20 elements to match the defined COLS constant and ensure consistent grid logic.

Actual:
Row 5 in mazeData has 21 elements.

Fix:
Correct the mazeData array to ensure all rows have 20 elements.

This bug is critical to fix for correct game behavior and rendering consistency.
