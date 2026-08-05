---
id: "0065"
title: "Bug: Missing src.backend.ghosts module causing import errors and test failures"
type: "bug"
status: "done"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-05"
objective: "Implement ghost visual identifiers and state logic including GhostState and GhostIdentity enums, Ghost and GhostManager classes, and API endpoints to get and set ghost states."
accept: "pytest tests/test_ghost_visuals.py"
resolution: "duplicate of #0060"
---

The backend module src/backend/ghosts.py is missing, causing import errors in multiple test files and src/backend/main.py. This blocks verification and release of card #0020 (Feature: Implement Ghost Visual Identifiers & State Logic).

Steps to reproduce:
1. Run pytest on tests/test_ghost_visuals.py or other affected tests.
2. Observe ModuleNotFoundError for src.backend.ghosts.

Expected:
- The module src/backend/ghosts.py exists and is importable.
- Tests run without import errors.

Actual:
- ModuleNotFoundError: No module named 'src.backend.ghosts'

This blocks card #0020 verification and release.

**2026-08-05 18:50** — closed as a duplicate of #0060: same work, filed more than once
