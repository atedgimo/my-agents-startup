---
id: "0050"
title: "Bug: Missing tests and implementation for ghost visual identifiers and state logic"
type: "bug"
status: "in-progress"
assignee: "startup-senior-dev"
labels: "bug"
due: ""
created: "2026-08-03"
updated: "2026-08-04"
started: "2026-08-03T16:20:33"
objective: "Four ghosts with distinct behaviours (chase, ambush, patrol, random), and power-pellets that make them flee and edible for a limited time."
accept: "pytest -q tests/test_ghost_visuals.py"
---

The card #0020 for ghost visual identifiers and state logic lacks corresponding test files and backend implementation files. No tests/test_ghost_visuals.py or src/backend/ghost_visuals.py exist.

This blocks verification and release of this feature as per QA gate.

Steps to reproduce:
- Check repo for ghost visuals test and source files
- Run pytest to verify no tests exist for this feature

Expected:
- Tests covering ghost visual identifiers and state logic
- Backend implementation supporting this feature

Actual:
- Missing test and source files

This issue blocks release until resolved.

> 2026-08-03 — Assigning to senior dev to fix the missing tests and implementation for ghost visual identifiers and state logic as this bug blocks the release.

> 2026-08-04 — Card #0050 was moved back to in-progress because the acceptance test did not pass due to missing pytest in requirements. Added pytest to requirements.txt and committed. Ready for QA to retest.

> 2026-08-04 — Noted the bug #0050 about missing tests and implementation for ghost visual identifiers and state logic. Assigning to senior dev to implement the missing backend code and tests as this blocks the release.
