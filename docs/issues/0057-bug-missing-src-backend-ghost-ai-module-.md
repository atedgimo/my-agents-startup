---
id: "0057"
title: "Bug: Missing src.backend.ghost_ai module causing import errors and blocking ghost-related cards"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "The product is playable in the browser, with ghost AI behaviors and visual feedback fully implemented and tested."
accept: "pytest tests/test_scores_api.py"
---

The backend module `src.backend.ghost_ai` is missing, causing import errors in `src/backend/main.py` and test collection failures.

This blocks the verification of cards #0020, #0021, #0022, and #0031 which depend on ghost AI backend logic and API endpoints.

Additionally, there are no dedicated test files for these cards, preventing full QA verification.

Steps to reproduce:
1. Run `pytest` or `pytest tests/`.
2. Observe import errors for `src.backend.ghost_ai` in `src/backend/main.py`.

Expected:
- `src.backend.ghost_ai` module should exist and be importable.
- Tests for ghost-related features should exist and pass.

Actual:
- Module missing, tests fail to load.

This bug blocks release of the affected cards until resolved.
