---
id: "0089"
title: "Fix import error for ghost_visuals module in test_ghost_visuals.py"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Acceptance tests for bug #0050 run without import errors"
accept: "pytest -q tests/test_ghost_visuals.py"
---

The test file tests/test_ghost_visuals.py fails to import the module src.backend.ghost_visuals, causing test collection to error out.

Error details:
ModuleNotFoundError: No module named 'src.backend.ghost_visuals'

This blocks running the acceptance tests for bug #0050 and needs to be fixed to verify the bug resolution.
