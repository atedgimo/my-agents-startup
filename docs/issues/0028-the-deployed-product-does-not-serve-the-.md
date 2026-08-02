---
id: "0028"
title: "The deployed product does not serve the game — only the API"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,frontend"
due: "2026-08-03"
created: "2026-08-02"
updated: "2026-08-02"
---

http://chomp.company-product.k8s.orb.local returns {"detail":"Not Found"} for /.

The backend is healthy and exposes GET /scores and POST /submit-score, but nothing serves src/index.html or src/game.js, so a visitor cannot play Chomp. The board brief says success means "playable end to end in a browser".

Fix: mount the frontend from the backend, e.g. serve index.html at / and the static assets alongside it (FastAPI StaticFiles), so one URL gives a playable game backed by the scores API. Then ask DevOps to redeploy and confirm / returns the HTML.

Expected: opening the URL shows the maze and the game runs. Actual: 404.
