---
id: "0076"
title: "Investigate import errors and environment stale detection blocking ghost_visuals module usage"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,blocking"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "The product environment no longer reports ModuleNotFoundError for ghost_visuals or ghost_ai imports, unblocking the release."
accept: "pytest tests/acceptance/test_ghost_api.py"
---

The current bug fix for #0050 implemented the ghost_visuals.py module and updated main.py to import and use it correctly. However, the product environment still reports import errors for src.backend.ghost_visuals and src.backend.ghost_ai (which does not exist).

This causes the product to crash on startup with ModuleNotFoundError and blocks the release.

The ghost_visuals.py file exists in the repo and is committed on the bug branch, but the environment does not detect it.

We need guidance on how to refresh or fix the environment to recognize new modules and allow the ghost_visuals integration to work.

Acceptance:
- The product environment no longer reports ModuleNotFoundError for ghost_visuals or ghost_ai imports.
- The /ghosts API endpoint returns the ghost states successfully.
- The bug #0050 fix can be merged and the release unblocked.

This issue is blocking the release and the completion of bug #0050.
