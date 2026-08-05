---
id: "0101"
title: "Audit and clean up unused backend routes and modules"
type: "chore"
status: "backlog"
assignee: ""
labels: "chore"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Reduce technical debt by removing unused backend code and routes."
accept: "pytest tests/acceptance/test_cleanup_unused_code.py"
---

There are several backend routes and modules not called or imported by anything, indicating dead or orphaned code. This chore is to audit these routes and modules, identify what can be safely removed or refactored, and clean up the codebase to reduce technical debt and improve maintainability.

Modules and routes to review include:
- src/backend/collision.py
- src/backend/ghost_ai.py
- src/backend/input_buffer.py
- src/frontend/motionInterpolation.js
- POST /input
- GET /move
- POST /clear_input
- GET /startups
- GET /pellets
- POST /collect_pellet

Objective: "Reduce technical debt by removing unused backend code and routes."

Acceptance: "pytest tests/acceptance/test_cleanup_unused_code.py" (test to be implemented to verify removal or safe refactor)
