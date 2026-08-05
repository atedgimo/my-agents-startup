---
id: "0092"
title: "Bug: Import confusion due to obsolete ghost_ai.py file"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Fix import confusion blocking ghost visual identifiers and state logic implementation"
accept: "pytest tests/acceptance/test_ghost_visuals.py"
---

The old src/backend/ghost_ai.py file conflicts with the new ghost_visuals.py module, causing import errors and test failures. This blocks acceptance of bug #0050. We need to delete or archive ghost_ai.py to resolve this.
