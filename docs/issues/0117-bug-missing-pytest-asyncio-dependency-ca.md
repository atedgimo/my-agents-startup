---
id: "0117"
title: "Bug: Missing pytest_asyncio dependency causing acceptance test failure on card #0094"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-08"
updated: "2026-08-08"
objective: "Acceptance test for card #0094 passes without ImportError"
accept: "pytest tests/acceptance/test_ghost_visuals.py"
---

The acceptance test for card #0094 fails with ImportError: No module named 'pytest_asyncio'. This dependency is required for the acceptance test in tests/acceptance/test_ghost_visuals.py but is not installed in the test environment.

Steps to reproduce:
1. Run acceptance test for card #0094: `curl -sf $URL/ghosts | jq -e '.Blinky and .Pinky and .Inky and .Clyde'`
2. Observe ImportError for pytest_asyncio.

Expected:
- pytest_asyncio is installed and the acceptance test runs successfully.

Actual:
- ImportError: No module named 'pytest_asyncio'

This bug blocks the acceptance and release of card #0094.

Suggested fix:
- Add pytest_asyncio to the test dependencies and ensure it is installed in the test environment before running acceptance tests.
