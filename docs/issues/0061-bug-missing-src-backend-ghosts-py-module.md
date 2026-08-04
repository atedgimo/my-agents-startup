---
id: "0061"
title: "Bug: Missing src/backend/ghosts.py module for ghost visual identifiers and state logic"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Implement ghost visual identifiers and state logic as required by card #0020"
accept: "pytest tests/test_ghost_visuals.py"
---

The backend main.py imports src.backend.ghosts module which is missing from the repo. This blocks the implementation of ghost visual identifiers and state logic as required by card #0020. The missing module should define GhostManager, GhostIdentity, and GhostState classes/enums to manage ghost states and identities as per the product requirements.
