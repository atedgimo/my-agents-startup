---
id: "0051"
title: "Define acceptance test for card #0021 listing startups endpoint"
type: "chore"
status: "backlog"
assignee: ""
labels: "chore"
due: ""
created: "2026-08-03"
updated: "2026-08-04"
objective: "Define acceptance test for card #0021 listing startups endpoint"
accept: "pytest tests/ -q -k collision"
---

The card #0021 implemented the /startups GET endpoint to list all startups from the SQLite database in DATA_DIR.

However, the card has no acceptance test defined, so it cannot be moved to done or merged.

Please define an acceptance test command that verifies the endpoint works as expected, e.g. a curl command that returns a valid JSON array or similar.

This is needed to complete the card properly.

**2026-08-04 17:31** — acceptance repaired: `pytest tests/ -q -k collision` — planner omitted the check: collision acceptance for card 0004
