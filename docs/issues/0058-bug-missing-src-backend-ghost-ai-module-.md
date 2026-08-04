---
id: "0058"
title: "Bug: Missing src.backend.ghost_ai module blocks backend tests"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: "2026-08-10"
created: "2026-08-04"
updated: "2026-08-04"
objective: "Regression tests pass without import errors blocking verification."
accept: "pytest tests/ | tee result.log | grep -q '== 0 failed'"
---

The backend tests fail to run due to a missing module src.backend.ghost_ai imported in src/backend/main.py. This blocks verification of card #0023 and other backend features relying on ghost AI.

Steps to reproduce:
1. Run pytest on tests/
2. Observe ModuleNotFoundError for src.backend.ghost_ai

Expected: The module should exist or be stubbed to allow tests to run.

Actual: ImportError blocks test collection.

This blocks the release as regression tests cannot pass.

Card #0023 verification is blocked until this is resolved.
