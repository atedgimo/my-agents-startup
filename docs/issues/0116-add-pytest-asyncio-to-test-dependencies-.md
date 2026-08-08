---
id: "0116"
title: "Add pytest_asyncio to test dependencies to fix acceptance check for card 0094"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,test"
due: ""
created: "2026-08-08"
updated: "2026-08-08"
objective: "acceptance tests for card 0094 pass"
accept: "pytest -v tests/acceptance/test_ghost_visuals.py"
---

The acceptance tests for card 0094 fail due to missing pytest_asyncio dependency, causing import errors. Add pytest_asyncio to the test requirements to enable async test support and unblock acceptance testing for ghost state management.
