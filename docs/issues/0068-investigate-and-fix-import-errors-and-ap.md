---
id: "0068"
title: "Investigate and fix import errors and app definition errors blocking acceptance tests for card #0050"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Acceptance tests for card #0050 pass without import or NameError"
accept: "pytest -q tests/test_ghost_visuals.py"
---

Acceptance tests for card #0050 fail due to:
- ModuleNotFoundError: No module named 'src.backend.ghost_visuals'
- NameError: name 'app' is not defined in src/backend/main.py

The src/backend/ghost_visuals.py file exists but is not found by tests.
The src/backend/main.py file has app.include_router(pellet_router) before app = FastAPI(), causing NameError.

Steps to reproduce:
- Run pytest tests/test_ghost_visuals.py
- Run pytest tests/test_pellet_collection.py

Expected:
- Tests run without import errors
- app is defined before usage

Actual:
- ImportError and NameError as above

Investigate import paths, module visibility, and app initialization order. Fix to allow acceptance tests to pass.
