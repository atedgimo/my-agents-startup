---
id: "0083"
title: "Investigate missing import line for GhostIdentity in main.py blocking bug #0056 fix"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Fix import error blocking bug #0056"
accept: "grep -q 'GhostIdentity' src/backend/main.py"
---

The bug #0056 fix requires removing GhostIdentity from the import line in src/backend/main.py and defining it locally.

However, the exact import line importing GhostIdentity from src.backend.ghost_ai is not found in main.py on the current branch, so the edit is refused.

This blocks the fix for bug #0056.

Please clarify the exact import line or provide a fix to allow the import error to be resolved.
