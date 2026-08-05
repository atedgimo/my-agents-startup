---
id: "0096"
title: "Bug: Missing module src.backend.ghost_visuals breaks ghost visuals tests"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "The product is stable and passes all tests without import errors or crashes."
accept: "pytest tests/test_ghost_visuals.py"
---

The test suite fails to run tests/test_ghost_visuals.py due to a ModuleNotFoundError: No module named 'src.backend.ghost_visuals'. This prevents running the ghost visuals tests and blocks verification of related functionality.

Reproduction:
1. Run pytest on the tests folder.
2. Observe the error about missing module src.backend.ghost_visuals.

Actual: ImportError and test collection failure.
Expected: Tests run without import errors.

This is a regression blocking the quality gate for release.
