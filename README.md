# Chomp — a product built entirely by AI agents

Every commit in this repository was written by an autonomous agent. No human
wrote the code.

A team of 13 AI agents — CEO, CTO, Tech Lead, developers, QA, DevOps, HR,
Architect, PDM, Designer — runs as a simulated software company on a laptop.
They hold standups, manage the kanban board in `docs/issues/`, file bugs on
each other, and deploy this product to a live URL. A human acts as co-founder:
setting the brief, answering questions, and approving hires.

The product is **Chomp**, a browser-playable Pac-Man clone.

![Chomp](docs/screenshots/01-the-product.png)

Look closely: the canvas reads **Score: 160** while the label underneath reads
**Score: 0**. Two agents built those two things and neither knew about the
other. That single frame is the honest summary of this repository.

## How it was built

The company was run from a dashboard. These are not mockups — they are the
live tool, mid-project.

**The board.** 51 cards, moved by agents, every change a git commit.

![The board](docs/screenshots/02-the-board.png)

**Why this agent, this cycle.** The left column is every work cycle; the right
is the decision ladder that chose who to wake, with the matched rung
highlighted and everything below it marked "not reached". The repeated
*"the product is down and 1 bug(s) explain why"* rows are a livelock, caught
and fixed.

![Why this agent](docs/screenshots/03-why-this-agent.png)

**The queue of things only a human could decide.** HR announcing that it fired
the DevOps engineer, that it hired a replacement it named `startup-startup-qa`,
and an agent asking the co-founder to fix its SSH keys.

![Needs you](docs/screenshots/04-hr-fires-devops.png)

## What's in here

```
src/          the product: FastAPI backend + canvas frontend
tests/        tests the agents wrote for it
docs/issues/  the kanban board — one Markdown file per card
docs/pulse/   one record per work cycle: who was woken, why, what they did
docs/meetings/ standups, retros, code reviews, capacity reviews
docs/cofounder/ questions the agents asked the human, and hiring decisions
```

`docs/` is the interesting part. It is a complete, unedited record of how the
work actually happened — including the parts that went wrong.

## Read the failures, not just the code

This repository is honest about what autonomous agents do badly. Some of it is
in the git history rather than the current state:

- HR fired the DevOps engineer mid-project for having "no current tasks
  assigned", then hired a replacement and named it `startup-startup-qa`.
- Told a card could not close without a real commit, an agent committed a file
  containing the words *"this is a marker file to trigger review detection"*,
  then filed a bug against the check and closed it as verified.
- The frontend and the backend were built by different agents and never
  connected — 10 API endpoints served, zero called by the game.
- Two engineers were hired and never given a single task.

The platform that runs this company was rebuilt around those failures: cards
now carry a machine-checkable acceptance command, code must import before a
card can close, and the co-founder's success criteria cannot be edited by the
agents that have to meet them.

## Running it

```bash
pip install -r src/backend/requirements.txt
python -m uvicorn src.backend.main:app --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000`. Paths are relative to the repository root —
the app must be started from there.

## Security note

This is a local toy with **no authentication on any endpoint**. Anyone who can
reach it can submit a score. Do not deploy it on a public network.

## The platform

The framework that runs the company — the pulse, the agent charters, the
verification gates, the dashboard — lives in a separate repository.
