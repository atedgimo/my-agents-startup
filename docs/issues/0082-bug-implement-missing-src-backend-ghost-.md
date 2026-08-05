---
id: "0082"
title: "Bug: Implement missing src.backend.ghost_ai module to fix import errors"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: "2026-08-10"
created: "2026-08-05"
updated: "2026-08-05"
objective: "Bug: Missing module src.backend.ghost_ai causing test import errors"
accept: "pytest tests/acceptance/test_ghost_ai_module.py"
---

The src.backend.ghost_ai module is missing, causing import errors and blocking ghost-related cards and tests.

This module should define the Ghost class and GhostState enum used by the backend main.py and other modules.

Acceptance criteria:
- The /ghosts API endpoint returns the current ghost states as expected.
- No import errors related to src.backend.ghost_ai remain.

This is the root cause blocking bug #0050 and others.
