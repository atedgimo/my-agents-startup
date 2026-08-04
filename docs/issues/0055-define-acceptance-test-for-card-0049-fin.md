---
id: "0055"
title: "Define acceptance test for card 0049: Finalize Ghost AI Behaviors and Visuals"
type: "chore"
status: "backlog"
assignee: ""
labels: "chore"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "finalize the ghost AI behaviors and visuals to meet the playable core loop and persistent feedback objectives"
accept: "curl -sf \"http://localhost:8000/ghosts?player_x=0&player_y=0\" | jq -e '.ghosts | length == 4'"
---

The card #0049 was implemented to finalize ghost AI behaviors and visuals, but it lacks an acceptance test command.

Please define a shell command that fails until the ghost AI behaviors and visuals are correctly implemented and passes when they work as expected.

This acceptance test should verify that the backend API for ghost states and positions behaves correctly based on player position input.

This is required to move card #0049 to review and completion.
