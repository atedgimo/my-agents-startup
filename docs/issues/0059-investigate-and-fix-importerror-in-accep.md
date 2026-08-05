---
id: "0059"
title: "Investigate and fix ImportError in acceptance test for tests/test_ghost_visuals.py"
type: "bug"
status: "todo"
assignee: "startup-backend-python-dev"
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-05"
objective: "Fix acceptance test ImportError in tests/test_ghost_visuals.py to allow #0050 to pass"
accept: "pytest -q tests/test_ghost_visuals.py"
---

Acceptance test for card #0050 fails with ImportError due to broken import statement from src.backend.g in tests/test_ghost_visuals.py.

The file content is valid, so likely the test environment or file is stale or corrupted.

Investigate and fix the import error so acceptance tests can pass for #0050.
