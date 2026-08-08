---
id: "0115"
title: "Bug: Missing pytest_asyncio dependency causing acceptance test failure on card 0094"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-08"
updated: "2026-08-08"
objective: "Acceptance tests for card 0094 run successfully without import errors."
accept: "pytest tests/acceptance/test_ghost_visuals.py"
---

The acceptance tests for card 0094 fail with an ImportError: No module named 'pytest_asyncio'. This module is required by tests/acceptance/test_ghost_visuals.py but is not installed in the test environment.

Steps to reproduce:
1. Run acceptance check for card 0094
2. Observe ImportError for pytest_asyncio

Expected: Acceptance tests should run without import errors.
Actual: Tests fail to run due to missing pytest_asyncio module.

This blocks the release of card 0094 until fixed.
