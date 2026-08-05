---
id: "0090"
title: "Fix import error in tests/test_ghost_visuals.py preventing import of src.backend.ghost_visuals"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "The test file tests/test_ghost_visuals.py can import src.backend.ghost_visuals without error."
accept: "pytest -q tests/test_ghost_visuals.py"
---

The test file tests/test_ghost_visuals.py fails to import the module src.backend.ghost_visuals due to an import error. This blocks acceptance testing for bug #0050.

Fix the import path or module structure so the test can run successfully.

This is a prerequisite for verifying bug #0050 fix.
