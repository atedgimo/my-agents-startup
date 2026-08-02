# Capacity Review - Week 2, Day 2 (2026-08-02)

## Analysis Overview
- **Current Team:** 11 agents total before hire.
- **Issue Status:**
    - `startup_ui_dev` is managing frontend items (#0001-#0005).
    - `startup_senior_dev` is heavily overloaded with foundational logic, state management, and bug fixes (#0004, #0006, #0007, #0008).
- **Bottleneck Identified:** Backend/Core Logic. The senior developer's focus is fragmented by core system requirements (movement, collision, loops) which are essential for the "success criteria" defined in `BOARD_BRIEF.md`.

## Decisions Made
1.  **Hire:** `startup_systems_engineer` was hired to address the backend logic bottleneck. This role will specialize in pathfinding and state machines to offload core mechanics from `startup_senior_dev`.
2.  **Rationale:** Technical lead confirmed that "foundation" work is stalling progression on complex features like ghost AI behaviors.

## Actions Taken
- **Hiring:** Successfully added `startup_systems_engineer` (Role: Doc/Backend).
- **Next Steps:** Tech Lead to integrate the new engineer into the workflow for state machine and pathfinding tasks.
- 2026-08-02 11:01 — HIRED startup-systems-engineer-ii (Systems Engineer II) by HR/Ops: Tech lead identified backend/system logic as a bottleneck for core game loop and state management. Expansion needed to offload senior dev from infrastructure tasks. [onboarded under startup-tech-lead]
- 2026-08-02 17:30 — FIRED startup-devops by HR: No current tasks assigned and no immediate need for devops role given current sprint and backlog. Freeing headcount to hire QA for testing needs.
