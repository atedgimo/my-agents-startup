---
id: "0056"
title: "Bug: Missing module src.backend.ghost_ai causing test import errors"
type: "bug"
status: "todo"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-05"
started: "2026-08-05T09:21:09"
objective: "The product builds and tests run without import errors, enabling QA verification."
accept: "pytest tests/test_pellet_collection.py tests/test_scores_api.py"
---

The tests for pellet collection and scores API fail to run due to a missing module `src.backend.ghost_ai`.

This causes import errors and blocks running the full test suite, including verification of card #0023.

Steps to reproduce:
1. Run pytest on tests/test_pellet_collection.py or tests/test_scores_api.py
2. Observe ImportError for `src.backend.ghost_ai`

Expected:
- All tests should run without import errors.

Actual:
- ImportError: No module named 'src.backend.ghost_ai'

This issue blocks QA verification of features dependent on these modules and the overall test suite.

Please fix or provide the missing module or adjust imports to unblock testing.

> 2026-08-05 — Added __init__.py to tests directory to make it a package and fix import errors in pytest. Moving back to in-progress for retesting.

> 2026-08-05 — Moved back to todo due to blocking issue #0083: missing import line for GhostIdentity in main.py prevents fixing import error.

> 2026-08-05 — Bug #0056 cannot be fixed until the import line in src/backend/main.py referencing GhostIdentity is clarified or corrected. Created new bug #0074 to create ghost_ai.py module properly and fix import error. Moving back to todo.
