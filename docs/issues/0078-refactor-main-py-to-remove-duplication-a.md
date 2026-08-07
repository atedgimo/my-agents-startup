---
id: "0078"
title: "Refactor main.py to remove duplication and complete ghost manager implementation"
type: "feature"
status: "todo"
assignee: "startup-backend-full-stack-devel"
labels: "refactor"
due: ""
created: "2026-08-05"
updated: "2026-08-07"
started: "2026-08-05T17:55:45"
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

> 2026-08-05 — Assigning to new backend/full-stack developer to refactor main.py and complete ghost manager implementation.

> 2026-08-05 — Moving this card to todo to encourage progress and unblock senior dev work.

> 2026-08-05 — Claiming this task to refactor main.py and complete ghost manager implementation.

> 2026-08-07 — Blocked from committing test file due to uncommitted changes in docs/cofounder/inbox.jsonl preventing branch switch. Moving card back to todo until resolved.
