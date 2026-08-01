# Technology Strategy

## Core Principles
- **Zero-Cost Mandate:** We only use free and open-source (FOSS) software, libraries, and tools. No paid licenses or "freemium" tiers are permitted for core infrastructure.
- **Scalability through Simplicity:** Preference is given to tools that provide high performance with minimal overhead.
- **Open Standards:** Favor technologies that follow widely accepted web standards.

## Tech Radar
| Status | Technology | Note |
|-------|-------------|------|
| Adopt | TypeScript | Primary language for type safety and clarity. |
| Adopt | React / Next.js | Framework of choice for internal tools/dashboards (where applicable). |
| Adopt | SQLite | Standard for local data persistence in FOSS projects. |
| Trial | Phaser | Potential engine for game-related components (e.g., 'Chomp'). |
| Hold | Firebase | Due to high cost risk and proprietary nature. |

## Coding Guidelines
- **Documentation:** All functions must have JSDoc or similar comments.
- **Type Safety:** Strict mode is enabled for all TypeScript projects.
- **Linting:** ESLint/Prettier integration is mandatory in CI.

## Project Specifics: Chomp (Pac-Man Clone)
**Requirements:** 60fps, FOSS only, local high scores.
**Recommended Stack:**
- **Frontend:** HTML5 Canvas with TypeScript.
- **Game Engine:** `Phaser` or `Kaboom.js` (Both are FOSS and excellent for arcade mechanics).
- **Local Database:** `SQLite` or `IndexedDB` for local score storage.
- **Deployment:** Standard static hosting (e.g., GitHub Pages/Vercel) with no paid tier usage.
