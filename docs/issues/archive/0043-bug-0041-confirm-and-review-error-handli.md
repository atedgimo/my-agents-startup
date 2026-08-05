---
id: "0043"
title: "Bug #0041: Confirm and review error handling and logging for environment variables and scores file access in src/backend/main.py"
type: "bug"
status: "done"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-02"
updated: "2026-08-02"
---

The current implementation in src/backend/main.py includes error handling and logging for reading the DATA_DIR environment variable and accessing the scores file to prevent CrashLoopBackOff issues.

However, bug #0041 is not marked done and no explicit fix commit is found for it.

Please review the existing error handling and logging code for robustness and completeness, and confirm if this resolves bug #0041 or if further improvements are needed.

> 2026-08-02 — Closed as a duplicate of #0041 by the co-founder. The root cause was a single defect: the frontend static mount resolved relative to the working directory (the app starts with `cd src/backend`), so it pointed at a path that does not exist and StaticFiles raised at import. Fixed by resolving from __file__. The product is live and serving the game, game.js and the scores API.
