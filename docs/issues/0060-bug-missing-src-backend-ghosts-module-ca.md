---
id: "0060"
title: "bug: missing src.backend.ghosts module causing import errors and test failures"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Implement ghost visual identifiers and state logic as backend functionality, with tests passing and API endpoints working."
accept: "pytest tests/test_ghost_visuals.py"
---

The backend module src.backend.ghosts is missing, causing import errors in main.py and test failures in multiple test files including test_ghost_visuals.py, test_pellet_collection.py, and test_scores_api.py. This blocks verification of cards #0020 and #0021 which depend on this module for ghost visual identifiers and state logic.

Reproduction:
- Run pytest
- Observe ImportError: No module named 'src.backend.ghosts'

Expected:
- The src.backend.ghosts module should exist and be importable.
- Tests should run and pass for ghost visual identifiers and state logic.

Actual:
- ImportError prevents tests from running.

This bug blocks release of the ghost visual identifiers and state logic features.
