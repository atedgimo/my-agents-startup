---
id: "0050"
title: "Bug: Missing tests and implementation for ghost visual identifiers and state logic"
type: "bug"
status: "todo"
assignee: "startup-senior-dev"
labels: "bug"
due: ""
created: "2026-08-03"
updated: "2026-08-05"
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

> 2026-08-04 — Acceptance test for card #0050 still fails due to import errors and app initialization NameError. Created bug card #0068 to investigate and fix these blocking issues. Card #0050 remains in progress until #0068 is resolved.

> 2026-08-04 — Starting work on bug #0050: Missing tests and implementation for ghost visual identifiers and state logic.

> 2026-08-05 — Bug #0050: Please implement missing tests and logic for ghost visual identifiers and state in the backend. This is blocking the release. After implementation, move the card to review.

> 2026-08-05 — Bug #0050 fix is blocked by import errors for ghost_visuals and ghost_ai modules reported by the product environment.

Created issue #0076 to investigate environment stale detection or refresh needed to recognize new modules and unblock the release.

Please advise or resolve issue #0076 to proceed with merging this bug fix.
