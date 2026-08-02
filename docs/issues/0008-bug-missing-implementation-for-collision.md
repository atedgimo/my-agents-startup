---
id: "0008"
title: "Bug: Missing implementation for Collision/Loss detection logic"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
---

The 'Loss' condition logic in `#0006` is currently only a comment in `src/game.js`. No actual collision detection or state transition to `STATE.LOST` is implemented beyond the visual overlay check.

**Expected:** Game should transition to LOST if player hits ghost (without power_up).
**Actual:** State remains PLAYING until all pellets are collected, unless manually set (not possible via current code).
