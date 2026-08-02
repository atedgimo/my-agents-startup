# ADR 0038: Investigate and Fix Commit Detection Blocking System

## Context

The system blocks moving kanban cards to review status if no commits are detected under `src/` or `tests/` since a specific cutoff date (2026-08-02). Despite a recent commit with trivial edits to a test file (`tests/test_input_buffer.py`), the system claims no such commit exists, blocking progress on issue #0034.

This commit detection is critical for automating workflow transitions and ensuring QA and review processes are unblocked.

## Decision

Investigate the CI/CD or GitHub Actions automation responsible for detecting commits and updating kanban card statuses. The investigation should focus on:

- Confirming the automation is triggered on push events.
- Verifying commit filtering logic by path (`src/` or `tests/`) and commit date.
- Ensuring commit timestamps and paths are correctly parsed and compared.
- Checking permissions for reading commit history and updating issues.
- Reviewing CI/CD logs for errors or failed runs affecting detection.
- Adding logging/debugging to the automation for visibility.

Fix any misconfiguration or bugs found in the workflow triggers, filters, or permissions.

After fixing, validate by committing a trivial change under `src/` or `tests/` and confirming the kanban card can move to review.

## Consequences

- The commit detection automation will reliably detect relevant commits and unblock kanban card transitions.
- QA and review processes will proceed without manual intervention or blocking.
- Future similar issues will be easier to diagnose with added logging.

## Explanation

Commit detection automation is essential for continuous integration workflows to automate status updates and enforce quality gates. Failures in this automation cause unnecessary blocking and reduce developer productivity. Ensuring the automation correctly filters commits by path and date and has adequate permissions is key to reliable operation.

Adding logging and error handling improves maintainability and troubleshooting.

---

*This ADR documents the investigation and guidance for fixing the commit detection blocking system issue reported in #0037 and #0038.*
