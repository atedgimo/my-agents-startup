---
id: "0007"
title: "Bug: Missing scoring increment for pellet collection"
type: "bug"
status: "review"
assignee: "startup_senior_dev"
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T08:53:24"
---

The 'Scoring' component of this task is incomplete. While a `score` variable exists in `src/game.js`, there is no logic implemented to increment it when pellets are collected. 

**Expected:** Score increases upon pellet collection.
**Actual:** Score remains at 0 regardless of game actions.

> 2026-08-02 — Refining for clarity: 
- Title: Bug: Missing scoring increment on pellet collection
- AC: 1. Player collects a pellet. 2. Score counter increments by 1. 3. UI updates immediately.
- Size: S
- Due Date: 2026-08-07

> 2026-08-02 — Title: Bug: Missing scoring increment on pellet collection.
AC: When a player touches a pellet, the score counter increments by 10.
Size: S
Due: 2026-08-10

> 2026-08-02 — [Pulse Check] Verified in-progress by senior_dev. This is being addressed as part of the movement integration package. Stay in in-progress for now.
