---
id: "0064"
title: "bug: missing src.backend.ghosts module causing import errors and test failures"
type: "bug"
status: "done"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-05"
objective: "Implement ghost visual identifiers and state logic as backend functionality, with tests passing and API endpoints working."
accept: "pytest tests/test_ghost_visuals.py"
resolution: "duplicate of #0060"
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

**2026-08-05 18:50** — closed as a duplicate of #0060: same work, filed more than once
