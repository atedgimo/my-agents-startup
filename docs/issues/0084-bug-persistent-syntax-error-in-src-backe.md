---
id: "0084"
title: "Bug: Persistent syntax error in src/backend/main.py blocks review and startup"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Fix syntax errors in src/backend/main.py to unblock backend startup and review of ghost state API implementation"
accept: "python -c 'import src.backend.main'"
---

The file src/backend/main.py contains corrupted trailing code causing an unterminated string literal syntax error at line 92.

This prevents the backend from starting and blocks review of card #0050 which implements ghost state logic and API.

A clean alternative implementation was added as src/backend/main_clean.py but the system insists on importing main.py.

Manual intervention is needed to fix or replace src/backend/main.py to unblock the project.

This bug blocks card #0050 and any backend startup.

Steps to reproduce:
- Run `python -c 'import src.backend.main'` from the repo root

Expected:
- No syntax errors

Actual:
- SyntaxError: unterminated string literal at line 92

Please prioritize fixing src/backend/main.py to unblock development.
