---
id: "0078"
title: "Refactor main.py to remove duplication and complete ghost manager implementation"
type: "feature"
status: "backlog"
assignee: ""
labels: "refactor"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "backend implementation correctness and clarity"
accept: "pytest tests/test_backend.py"
---

The main.py backend file currently contains duplicated and commented-out code related to ghost manager initialization. The ghost manager is a dummy or partial implementation that needs completion to fully support ghost state logic.

This refactor will improve code clarity, maintainability, and align with the intended architecture of the backend.

Steps to reproduce:
- Observe duplicated GhostManager class definitions.
- Note commented-out imports and dummy implementations.

Expected:
- Single, clear GhostManager implementation.
- Fully functional ghost state management endpoints.

Actual:
- Duplicate and commented code present.
- Ghost manager is a stub.

This is a structural improvement, no functional bugs detected currently.

Labels: refactor
Objective: "backend implementation correctness and clarity"
Accept: pytest tests/test_backend.py
