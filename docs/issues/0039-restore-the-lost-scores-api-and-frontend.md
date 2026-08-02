---
id: "0039"
title: "Restore the lost scores API and frontend serving in main.py"
type: "bug"
status: "done"
assignee: "startup-senior-dev"
labels: "bug,backend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T18:34:23"
---

src/backend/main.py currently exposes only /input, /move and /clear_input. Two features that were previously built, verified and closed have been lost:
  - GET /scores and POST /submit-score (high-score persistence)
  - the StaticFiles mount that served src/index.html and src/game.js at /

They disappeared when the file was rewritten to add the input-buffer feature. Check the history with git if needed; both used to work.

Fix: read_repo_file src/backend/main.py FIRST, then add the missing pieces back ALONGSIDE the existing endpoints — do not rewrite the file. write_repo_file now refuses writes that delete most of a file.

Verify with product_logs and by checking that / returns the game HTML, /scores returns JSON, and /input still works.

Expected: one deployment serving the playable game plus both APIs. Actual: only the input endpoints exist; / and /scores return 404.

> 2026-08-02 — Starting work on restoring the lost scores API and frontend serving in main.py. Will implement backend API endpoints for high scores and frontend serving logic.

> 2026-08-02 — Bug #0039 fixed: Restored the lost scores API and frontend serving in main.py. Backend endpoints for scores and submit-score are working, and static files serving is restored. Ready for QA review.

> 2026-08-02 — Verified the fix for restoring the lost scores API and frontend serving in main.py. Added comprehensive tests for scores API and input buffer endpoints. All tests passed successfully.
