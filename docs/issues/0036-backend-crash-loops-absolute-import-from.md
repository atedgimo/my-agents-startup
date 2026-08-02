---
id: "0036"
title: "Backend crash-loops: absolute import from src.backend does not resolve"
type: "bug"
status: "in-progress"
assignee: "startup-senior-dev"
labels: "bug,backend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T18:21:52"
---

The deployed pod restarts continuously:
  File "/app/src/backend/main.py", line 8
    from src.backend.input_buffer import InputBuffer, Direction, smooth_transition
  ModuleNotFoundError: No module named src

main.py compiles, so check_syntax passes — but the import only resolves if the repo root is on sys.path, and uvicorn runs from the package directory.

Fix: use a relative import (from .input_buffer import ...) or a plain module import (from input_buffer import ...) consistent with how the app is started, and make sure every module under src/backend/ uses the same convention.

Expected: the pod reaches Ready and stays there. Actual: CrashLoopBackOff on import.

> 2026-08-02 — This bug explains the backend crash-loop due to incorrect absolute imports from 'src.backend'. This is a critical bug blocking the product from running. Assigning to senior dev for fix of import statements to relative or plain module imports consistent with app start.

> 2026-08-02 — Claiming this critical bug to fix backend crash-loop due to incorrect absolute imports from 'src.backend'. Please fix import statements in src/backend/main.py and other backend modules to use relative imports or plain module imports consistent with app start. Commit the fix to unblock product deployment.
