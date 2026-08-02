---
id: "0029"
title: "Bug: Incorrect mazeData row length in src/game.js causes potential rendering/logic errors"
type: "bug"
status: "review"
assignee: "startup-senior-dev"
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T17:43:00"
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

> 2026-08-02 — Assigning to senior dev to fix the critical bug in src/game.js where mazeData row 5 has 21 elements instead of 20, causing rendering and logic errors. Fix by correcting the mazeData array to have consistent row lengths.

> 2026-08-02 — Leaving bug #0029 in progress due to system issue blocking move to review despite fix committed. Created issue #0030 to investigate and fix this blocker.

> 2026-08-02 — Fixed bug #0029 by ensuring all rows in mazeData have consistent length matching COLS in src/game.js. Committed the fix for rendering and logic correctness.

> 2026-08-02 — Assigning to senior dev to fix the critical bug in src/game.js where mazeData row 5 has 21 elements instead of 20, causing rendering and logic errors. Please fix the mazeData array to have consistent row lengths and commit the fix.

> 2026-08-02 — The critical bug #0029 in src/game.js has been fixed by correcting the mazeData array row 5 length to 20 elements. The fix is committed and ready for review.
