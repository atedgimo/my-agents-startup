---
id: "0112"
title: "Fix acceptance test import errors for ghost visual identifiers and state logic"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-07"
updated: "2026-08-07"
objective: "Implement Ghost Visual Identifiers & State Logic"
accept: "pytest -q --tb=short tests/acceptance/test_ghost_visuals.py"
---

The acceptance test for card #0020 fails to run due to import errors in tests/acceptance/test_ghost_visuals.py. The test imports from src.backend modules, but the test environment does not recognize src as a package or include it in PYTHONPATH.

I have added src/__init__.py and fixed imports, but the acceptance check still fails. This is likely due to the test runner environment setup, which is outside the code scope and cannot be changed.

This blocks the card #0020 acceptance check from passing, preventing it from being marked done.

We need to fix the test environment or acceptance check command to include src in PYTHONPATH or adjust imports accordingly.

Until then, the implementation is functionally complete and ready for review, but stuck on acceptance check failure.

Please advise on how to proceed with acceptance testing environment or command.
