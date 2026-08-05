---
id: "0102"
title: "Refactor InputBuffer and Direction enum to unify implementation and avoid duplication"
type: "feature"
status: "backlog"
assignee: ""
labels: "refactor"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Maintainable and consistent backend code with unified InputBuffer and Direction enum"
accept: "pytest tests/test_input_buffer.py"
---

There are two different implementations of InputBuffer and Direction enum in src/backend/main.py and src/backend/input_buffer.py. This duplication causes confusion and risks bugs due to inconsistent behavior.

Proposed fix:
- Consolidate InputBuffer and Direction enum into a single module.
- Import and use the unified implementation in main.py and elsewhere.
- Ensure consistent behavior and type usage.

This change will improve code clarity, maintainability, and reduce bugs.

Steps to reproduce:
- Review src/backend/main.py and src/backend/input_buffer.py for InputBuffer and Direction enum definitions.
- Observe differences and duplication.

Expected:
- Single source of truth for InputBuffer and Direction enum.

Actual:
- Two different implementations coexist.

Labels: refactor
Objective: "Maintainable and consistent backend code with unified InputBuffer and Direction enum"
Accept: pytest tests/test_input_buffer.py
