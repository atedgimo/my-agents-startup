---
id: "0007"
title: "Bug: Missing scoring increment for pellet collection"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
---

The 'Scoring' component of this task is incomplete. While a `score` variable exists in `src/game.js`, there is no logic implemented to increment it when pellets are collected. 

**Expected:** Score increases upon pellet collection.
**Actual:** Score remains at 0 regardless of game actions.
