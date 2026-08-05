# Notes for Product Manager

## Priorities for Next Development Cycle

1. Complete UI state overlays for Game Over and Level Up.
   - These overlays are critical for providing clear persistent feedback to the player.
   - Progress can be measured by the presence and correct display of these overlays in the game UI.

2. Finalize ghost AI behaviors and visuals.
   - Ensure all 4 ghost AI behaviors (Chase, Ambush, Patrol, Random) are fully implemented and visually distinct.
   - Progress can be measured by testing ghost AI behavior completeness and visual correctness.

3. Verify integration of backend routes with frontend.
   - Many backend API routes currently exist but are not called by the frontend.
   - The product manager should verify which routes are integrated and plan frontend calls for those that are not.

## Objective Alignment
- These priorities directly support the success criteria in the OKRs, specifically:
  - "Establish a playable core loop in the browser."
  - "Provide persistent feedback for the player."

## Suggested Acceptance Criteria for Next Cycle Deliverables
- UI overlays for Game Over and Level Up appear correctly under the appropriate game states.
- Ghost AI behaviors operate as expected during gameplay.
- Frontend successfully calls at least one previously uncalled backend route, or a plan is documented for integration.

---

This note is to guide focus and ensure measurable progress in the next cycle.