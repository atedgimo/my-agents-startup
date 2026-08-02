# Capacity Review - Week 2 Day 2

*Convener: startup_hr_ops · 2026-08-02 04:14*

# Capacity Review - Week 2, Day 2 (2026-08-02)

## Agenda
Review company capacity, identify bottlenecks in backend/frontend/testing/design, and perform hiring adjustments.

## Analysis
1. **Staffing Assessment:** Currently, `startup_senior_dev` is handling multiple high-complexity foundation tasks (#0004, #0006, #0007, #0008). 
2. **Bottleneck Identification:** The Tech Lead confirmed that the primary bottleneck is **Backend/Core Logic**. The senior developer is over-leveraged on state management and collision logic, which delays the implementation of advanced features (like ghost AI).
3. **Evaluation of Other Areas:** Frontend (#0005) and design are stable; Testing has a moderate risk due to slow feedback but isn't the primary bottleneck for immediate growth.

## Decisions & Actions
- **Action 1:** Hired `startup_systems_engineer` (Role: Doc).
    - *Reason:* To offload core mechanics, pathfinding, and state machines from the senior developer.
- **Decision Log:** Updated `docs/hr/DECISIONS.md` with the rationale for this hire.

## Conclusion
The team is now positioned to scale backend logic development independently of frontend iterations.