---
id: "0062"
title: "Bug: Missing module 'src.backend.ghosts' causing test import errors"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Acceptance tests for bug #0050 run without import errors and verify the fix for ghost visual identifiers and state logic."
accept: "pytest tests/test_ghost_visuals.py"
---

The acceptance tests for bug #0050 failed due to missing module errors. The module 'src.backend.ghosts' is not found, causing import errors in the test files:
- tests/test_ghost_visuals.py
- tests/test_pellet_collection.py
- tests/test_scores_api.py

This blocks running the acceptance tests and verifying the fix for ghost visual identifiers and state logic.

Steps to reproduce:
1. Run pytest on the tests/ folder
2. Observe ImportError for 'src.backend.ghosts'

Expected:
- Tests should import all necessary modules and run without import errors.

Actual:
- ImportError: No module named 'src.backend.ghosts'

Please investigate and fix the missing module or adjust imports accordingly.
