---
id: "0106"
title: "Improve keyboard accessibility and HUD design for better user experience"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-18"
created: "2026-08-05"
updated: "2026-08-05"
objective: "Playability: Full game cycle reachable in browser (move, eat pellets, win level)."
accept: "curl -sf $URL | grep -q 'aria-live' && curl -sf $URL | grep -q 'score' && curl -sf $URL | grep -q 'animation'"
---

Implement keyboard accessibility features including focus management and ARIA roles for game state announcements to support screen reader users.

Redesign the HUD to be clear, minimalist, and visually accessible using Tailwind CSS, showing score, lives, and level with good contrast.

Add subtle visual feedback animations for pellet consumption, ghost states, and power-pellet activation to enhance game clarity and satisfaction.

Value case: Improves usability and accessibility for all desktop players, including those relying on keyboard navigation and screen readers, aligning with the brief's target users and success criteria for a polished, playable arcade experience.
