---
id: "0030"
title: "Investigate and fix kanban board commit detection bug blocking move to review"
type: "bug"
status: "backlog"
assignee: ""
labels: "chore"
due: "2026-08-05"
created: "2026-08-02"
updated: "2026-08-02"
---

The system refuses to move cards to review status because it detects no new commits under src/ or tests/ since 2026-08-02, even though code changes have been committed. This blocks bug #0029 from moving to review and thus blocks releases.

Steps to reproduce:
- Commit a fix to a bug in src/ (e.g., bug #0029 mazeData fix)
- Attempt to move the bug card to review
- System refuses due to no detected commit

Expected:
- Cards should move to review when code changes are committed

This is a critical blocker for release and needs urgent investigation and fix.
