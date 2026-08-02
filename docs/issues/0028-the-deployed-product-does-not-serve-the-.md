---
id: "0028"
title: "The deployed product does not serve the game — only the API"
type: "bug"
status: "review"
assignee: "startup-senior-dev"
labels: "bug,frontend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
started: "2026-08-02T17:39:14"
---

http://chomp.company-product.k8s.orb.local returns {"detail":"Not Found"} for /.

The backend is healthy and exposes GET /scores and POST /submit-score, but nothing serves src/index.html or src/game.js, so a visitor cannot play Chomp. The board brief says success means "playable end to end in a browser".

Fix: mount the frontend from the backend, e.g. serve index.html at / and the static assets alongside it (FastAPI StaticFiles), so one URL gives a playable game backed by the scores API. Then ask DevOps to redeploy and confirm / returns the HTML.

Expected: opening the URL shows the maze and the game runs. Actual: 404.

> 2026-08-02 — Assigning to senior dev to fix the deployment issue where the product serves only the API, not the game frontend.

> 2026-08-02 — Starting work on fixing the deployment to serve the frontend game files along with the API as per bug #0028.

> 2026-08-02 — Fix committed: backend now serves src/index.html at / and mounts src/ as static files under /static for full frontend delivery. Ready for redeployment and QA verification.
