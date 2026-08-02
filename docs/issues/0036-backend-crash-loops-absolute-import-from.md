---
id: "0036"
title: "Backend crash-loops: absolute import from src.backend does not resolve"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,backend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
---

The deployed pod restarts continuously:
  File "/app/src/backend/main.py", line 8
    from src.backend.input_buffer import InputBuffer, Direction, smooth_transition
  ModuleNotFoundError: No module named src

main.py compiles, so check_syntax passes — but the import only resolves if the repo root is on sys.path, and uvicorn runs from the package directory.

Fix: use a relative import (from .input_buffer import ...) or a plain module import (from input_buffer import ...) consistent with how the app is started, and make sure every module under src/backend/ uses the same convention.

Expected: the pod reaches Ready and stays there. Actual: CrashLoopBackOff on import.
