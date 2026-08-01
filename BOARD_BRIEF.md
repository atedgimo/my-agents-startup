# Board Brief — the co-founder's founding input

## Product idea

A browser-playable Pac-Man clone called **Chomp** — a single-page arcade game
with a maze, pellets, four ghosts, power-pellets, lives and scoring, plus a
local high-score board so players can chase their own records.

## Target users

Casual players on a desktop browser who want a 3-minute nostalgia break — no
install, no account, no ads. Secondary: retro-gaming fans who care that the
ghosts behave like the original (each with its own chase personality).

## The problem

Every free Pac-Man on the web is buried in ads, needs Flash-era plugins, or
phones home with trackers. There is no clean, instantly-playable, fully local
version you can host yourself and trust.

## Success criteria

- Playable end to end in a browser: arrow keys move Pac-Man, ghosts chase, eating all pellets wins the level.
- Four ghosts with distinct behaviours (chase, ambush, patrol, random), and power-pellets that make them flee and edible for a limited time.
- Score, lives and level shown live; game over and level-up states work.
- High scores persist across page reloads via the backend API.
- Runs at a steady 60 fps on a laptop with no console errors.

## Constraints & non-goals

- Zero cost: free and open-source technology only.
- No mobile/touch controls, no multiplayer, no sound assets that require a licence in v1.
- No user accounts — high scores are stored per local player name only.
- Keep it to one level's maze layout in v1; more levels come later.

## Co-founder expectations

- Ship small and often: I want something playable early, then improve it — a moving Pac-Man in an empty maze beats a perfect design doc.
- The QA gate is real: no release while a critical bug is open, and I expect actual tests for the scoring and collision logic.
- Ask me through the inbox before widening scope (extra levels, sound, mobile) — I would rather you polish what exists.
- Every release should be demoable at a live URL, and I want the demo requested only after you have run it internally yourselves.
