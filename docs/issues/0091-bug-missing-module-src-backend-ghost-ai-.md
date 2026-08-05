---
id: "0091"
title: "Bug: Missing module src.backend.ghost_ai causing test import errors"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Fix import errors in ghost visual tests by renaming ghost_ai.py to ghost_visuals.py"
accept: "pytest -q tests/test_ghost_visuals.py"
---

The tests in tests/test_ghost_visuals.py import from src.backend.ghost_visuals but the implementation was in src/backend/ghost_ai.py, causing import errors.

This bug tracks renaming ghost_ai.py to ghost_visuals.py to fix import errors and ensure tests run correctly.

This is related to bug #0050 but separate to track the import issue specifically.
