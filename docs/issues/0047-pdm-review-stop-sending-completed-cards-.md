---
id: "0047"
title: "PDM review: stop sending completed cards in every agent prompt"
type: "chore"
status: "backlog"
assignee: ""
labels: "chore"
due: ""
created: "2026-08-02"
updated: "2026-08-04"
objective: "keep the company affordable to run"
---

The co-founder asks PDM to review and approve (or reject) this change before it is made.

**Proposal.** list_issues currently returns every card, including done ones. Measured today: the payload is 5,009 characters and 76% of it is finished work — roughly 960 tokens of completed cards in every planning prompt, on every cycle. It grows as the company succeeds, which is the wrong direction.

**Change.** Default list_issues to the open board (backlog, todo, in-progress, review). Anyone who genuinely needs history can still ask for it explicitly with status=done, which already works.

**Why it needs PDM.** This changes what every agent sees when it plans. The risk is that an agent loses useful context — for example, filing a duplicate of something already delivered, since the refinement ceremony leans on seeing done cards to spot repeats.

**Please decide and record your reasoning:** approve as proposed, approve with a cap (e.g. the 10 most recently completed), or reject and say what the done cards are load-bearing for.

> 2026-08-04 — Notified UI and Senior Dev teams about updated OKRs prioritizing UI overlays for Game Over and Level Up, and ghost AI behaviors and visuals. Emphasized importance for playable core loop, persistent feedback, and internal demo preparation. Asked to focus next cycle work accordingly.
