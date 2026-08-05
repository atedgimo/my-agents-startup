---
id: "0074"
title: "Create ghost_ai.py module to fix import error"
type: "bug"
status: "todo"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "fix import error preventing backend startup"
accept: "test -f src/backend/ghost_ai.py"
---

Create the src/backend/ghost_ai.py module with ghost logic to fix the ModuleNotFoundError in main.py.

This module must define GhostState enum and Ghost class with visual_identifier and state update methods as used in main.py.

This card serves to unblock the import error preventing backend startup.

> 2026-08-05 — Card created to fix ghost_ai.py missing module import error blocking backend startup. Ready to be picked up.
