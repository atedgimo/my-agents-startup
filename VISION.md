# Vision: Chomp

## The Product
**Chomp** is a browser-playable arcade game inspired by Pac-Man. It is a single-page experience that offers players a 3-minute nostalgia break without ads, trackers, or the need for accounts or plugins.

## Target Audience
1. **Casual Players:** Users on desktop browsers looking for an instant, high-quality retro gaming experience.
2. **Retro-Gaming Fans:** Enthusiasts who appreciate authentic mechanics, such as distinct ghost personalities and power-pellets.

## Problem Statement
Most web-based Pac-Man clones are cluttered with ads, require outdated technology (like Flash), or track user data. There is a lack of clean, self-hostable, and privacy-respecting local arcade games.

## Core Goals & Success Metrics
1. **Core Gameplay:** Movement via arrow keys, pellets to collect, 4 ghosts with distinct behaviors (chase, ambush, patrol, random), and power-pellets that reverse ghost behavior.
2. **State Management:** Real-time display of scores, lives, and levels; functioning game over and level-up states.
3. **Persistence:** High scores saved via a backend API and persisted across reloads for local players.
4. **Performance:** Stable 60 FPS on standard hardware with no console errors.

## Roadmap & Scope (v1)
- Single maze layout.
- No mobile/touch controls or sound assets in initial launch.
- Focus on polished core mechanics before expanding to multiple levels or features like social integration.