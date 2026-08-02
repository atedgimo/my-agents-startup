---
id: "0025"
title: "Deployment crash-loops: backend/main.py exists but backend/requirements.txt does not"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,deployment"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
---

The first release attempt deployed but the pod crash-looped 6 times.

Reproduction: DevOps ran the FastAPI start command 'pip install -r backend/requirements.txt && cd backend && python -m uvicorn main:app'. The pod logs show:
  ERROR: Could not open requirements file: No such file or directory: backend/requirements.txt

src/ currently contains: index.html, game.js, backend/main.py — a half-built backend with no dependency manifest.

Decide and fix ONE of these:
(a) Chomp is a static browser game: delete src/backend/ and serve with python -m http.server, or
(b) the backend is real (high scores API): write src/backend/requirements.txt listing fastapi and uvicorn, and make sure main.py runs.

Expected: the deployed pod reaches Ready and serves the game. Actual: CrashLoopBackOff.
