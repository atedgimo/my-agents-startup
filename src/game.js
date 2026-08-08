import { animatePelletCollection } from "./frontend/motionInterpolation.js";

// Motion interpolation feature implemented for smooth rendering

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game Configuration
const TILE_SIZE = 30;
const ROWS = 20;
const COLS = 20;

// Game States
const STATE = {
    PLAYING: 'PLAYING',
    WON: 'WON',
    LOST: 'LOST'
};

let gameState = STATE.PLAYING;
let score = 0;
let lives = 3;
let power_up = false; // Track if player has a power-up for ghost logic

// Overlay control
let overlayActive = false;

// Visual juice state
let visualJuice = {
    pelletCollected: false,
    powerPelletActive: false,
    ghostHit: false,
    ghostEaten: false,
    powerPelletEffect: 0, // 0 = off, 1 = activating, -1 = deactivating
    powerPelletGlow: 0,   // 0..1 for glow animation
};

let ghostVisualStates = {}; // {ghost_id: {visual_state, position}}
let ghostStateLastFetched = 0;
let ghostStateFetchInterval = 100; // ms

// Function to activate overlay and pause game logic
function activateOverlay(state) {
    gameState = state;
    overlayActive = true;
}

// Function to dismiss overlay and reset or advance game
function dismissOverlay() {
    if (gameState === STATE.LOST) {
        // Reset game
        resetGame();
    } else if (gameState === STATE.WON) {
        // Advance to next level or reset
        nextLevel();
    }
    overlayActive = false;
    gameState = STATE.PLAYING;
}

// Reset game state
function resetGame() {
    score = 0;
    lives = 3;
    power_up = false;
    visualJuice = {
        pelletCollected: false,
        powerPelletActive: false,
        ghostHit: false,
        ghostEaten: false,
    };
    playerPos = { x: 5, y: 5 };
    ghosts.forEach(g => g.pos = { x: 10, y: 10 });
    pellets.forEach(p => p.active = true);
}

// Advance to next level (simplified as reset for now)
function nextLevel() {
    // Could add level increment logic here
    resetGame();
}


// Maze Layout - 1=Wall, 0=Path/Pellet, 2=Power Pellet
const mazeData = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];

const pellets = [];
// Populate pellets from mazeData (type 0 means a path with a pellet)
for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
        if (mazeData[r][c] === 0) {
            pellets.push({ x: c, y: r, active: true });
        }
    }
}

let playerPos = { x: 5, y: 5 };
let prevPlayerPos = { ...playerPos };

// Ghosts: now use ghostVisualStates for rendering
const ghosts = [
    { id: "blinky", pos: { x: 10, y: 10 }, prevPos: { x: 10, y: 10 } },
    { id: "pinky", pos: { x: 15, y: 15 }, prevPos: { x: 15, y: 15 } }
];
ghosts.forEach(g => {
    ghostVisualStates[g.id] = { visual_state: "normal", position: { ...g.pos } };
});

// Timing for interpolation
let lastUpdateTime = performance.now();
const LOGIC_UPDATE_INTERVAL = 1000 / 60; // 60 logic updates per second

function lerp(a, b, t) {
    return a + (b - a) * t;
}

function update() {
    if (overlayActive) return; // Pause updates when overlay active
    if (gameState !== STATE.PLAYING) return;

    // Save previous positions for interpolation
    prevPlayerPos = { ...playerPos };
    ghosts.forEach(g => {
        g.prevPos = { ...g.pos };
    });

    // Example logic update: move player right by one tile every second
    // (Replace with actual input handling and movement logic)
    // For demonstration, we just cycle playerPos.x
    playerPos.x += 1;
    if (playerPos.x >= COLS - 1) playerPos.x = 1;

    // Pellets collection logic
    pellets.forEach(p => {
        if (p.active && !p.animating) {
            if (p.x === playerPos.x && p.y === playerPos.y) {
                // Animate pellet collection
                animatePelletCollection(p, 300);
                score += 10;
                visualJuice.pelletCollected = true;
                // If this is a power pellet, trigger effect
                if (mazeData[p.y][p.x] === 2) {
                    triggerPowerPelletEffect();
                }
            }
        }
    });

    // Win Condition Check
    const remainingPellets = pellets.filter(p => p.active).length;
    if (remainingPellets === 0) {
        activateOverlay(STATE.WON);
    }

    // Collision Detection for ghosts
    ghosts.forEach(g => {
        const dist = Math.hypot(playerPos.x - g.pos.x, playerPos.y - g.pos.y);
        if (dist < 1) { // Same tile
            if (!power_up) {
                activateOverlay(STATE.LOST);
                visualJuice.ghostHit = true;
                // Trigger ghost hit animation or effect here
            } else {
                power_up = false;
                visualJuice.ghostEaten = true;
                // Trigger ghost eaten animation or effect here
                triggerPowerPelletDeactivation();
            }
        }
    });

    lastUpdateTime = performance.now();
}

function draw() {
    const now = performance.now();
    const delta = now - lastUpdateTime;
    const t = Math.min(delta / LOGIC_UPDATE_INTERVAL, 1);

    // Power pellet glow effect (background overlay)
    if (visualJuice.powerPelletGlow > 0) {
        ctx.save();
        ctx.globalAlpha = 0.25 * visualJuice.powerPelletGlow;
        ctx.fillStyle = '#60a5fa'; // Tailwind blue-400
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.restore();
    }

    // Clear canvas
    ctx.fillStyle = '#111';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw maze
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (mazeData[r][c] === 1) {
                ctx.fillStyle = '#2d3748'; // Tailwind gray-800
                ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }
        }
    }

    // Draw pellets (with animation)
    pellets.forEach(p => {
        if (p.active || p.animating) {
            let pelletAlpha = 1;
            let pelletRadius = 4;
            if (p.animating) {
                const elapsed = now - p.animationStart;
                const progress = Math.min(elapsed / p.animationDuration, 1);
                pelletAlpha = 1 - progress;
                pelletRadius = 4 * (1 - progress);
                if (progress >= 1) {
                    p.active = false;
                    p.animating = false;
                }
            }
            ctx.save();
            ctx.globalAlpha = pelletAlpha;
            ctx.fillStyle = (mazeData[p.y][p.x] === 2) ? '#38bdf8' : '#facc15'; // Power pellet blue, normal yellow
            ctx.beginPath();
            ctx.arc(p.x * TILE_SIZE + TILE_SIZE / 2, p.y * TILE_SIZE + TILE_SIZE / 2, pelletRadius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }
    });

    // Interpolated player position
    const interpPlayerX = lerp(prevPlayerPos.x, playerPos.x, t) * TILE_SIZE;
    const interpPlayerY = lerp(prevPlayerPos.y, playerPos.y, t) * TILE_SIZE;

    // Draw player (with power pellet effect)
    ctx.save();
    if (visualJuice.powerPelletGlow > 0) {
        ctx.shadowColor = '#38bdf8';
        ctx.shadowBlur = 20 * visualJuice.powerPelletGlow;
    }
    ctx.fillStyle = '#f59e0b'; // Tailwind amber-500
    ctx.beginPath();
    ctx.arc(interpPlayerX + TILE_SIZE / 2, interpPlayerY + TILE_SIZE / 2, TILE_SIZE / 2 - 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // Draw ghosts with interpolation and visual state
    ghosts.forEach(g => {
        // Use backend ghost visual state if available
        let ghostState = ghostVisualStates[g.id]?.visual_state || "normal";
        let ghostColor = "#ef4444"; // Tailwind red-500
        let ghostAlpha = 1;
        let ghostStroke = false;
        switch (ghostState) {
            case "frightened":
                ghostColor = "#38bdf8"; // Tailwind blue-400
                break;
            case "eaten":
                ghostColor = "#f3f4f6"; // Tailwind gray-100
                ghostAlpha = 0.5;
                break;
            case "returning":
                ghostColor = "#a1a1aa"; // Tailwind gray-400
                ghostAlpha = 0.7;
                ghostStroke = true;
                break;
            default:
                ghostColor = "#ef4444";
        }
        // Interpolated position
        let ghostPos = ghostVisualStates[g.id]?.position || g.pos;
        const interpGhostX = lerp(g.prevPos.x, ghostPos.x, t) * TILE_SIZE;
        const interpGhostY = lerp(g.prevPos.y, ghostPos.y, t) * TILE_SIZE;
        ctx.save();
        ctx.globalAlpha = ghostAlpha;
        ctx.fillStyle = ghostColor;
        ctx.beginPath();
        ctx.arc(interpGhostX + TILE_SIZE / 2, interpGhostY + TILE_SIZE / 2, TILE_SIZE / 2 - 2, 0, Math.PI * 2);
        ctx.fill();
        if (ghostStroke) {
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#fff";
            ctx.stroke();
        }
        ctx.restore();
    });

    // Draw Score
    ctx.fillStyle = '#facc15';
    ctx.font = '16px Arial';
    ctx.fillText(`Score: ${score}`, 10, 20);

    // Visual juice effects
    if (visualJuice.pelletCollected) {
        // Example: briefly flash the score text
        ctx.fillStyle = '#34d399'; // Tailwind green-400
        ctx.font = 'bold 18px Arial';
        ctx.fillText(`+10!`, 60, 20);
        // Reset after drawing
        visualJuice.pelletCollected = false;
    }

    if (visualJuice.ghostHit) {
        // Example: flash screen red briefly
        ctx.fillStyle = 'rgba(220, 38, 38, 0.3)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        // Reset after drawing
        visualJuice.ghostHit = false;
    }

    if (visualJuice.ghostEaten) {
        // Example: flash screen blue briefly
        ctx.fillStyle = 'rgba(59, 130, 246, 0.3)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        // Reset after drawing
        visualJuice.ghostEaten = false;
    }

    // Power pellet activation/deactivation animation
    if (visualJuice.powerPelletEffect !== 0) {
        // Animate glow in/out
        if (visualJuice.powerPelletEffect === 1) {
            visualJuice.powerPelletGlow += 0.05;
            if (visualJuice.powerPelletGlow >= 1) {
                visualJuice.powerPelletGlow = 1;
                visualJuice.powerPelletEffect = 0;
            }
        } else if (visualJuice.powerPelletEffect === -1) {
            visualJuice.powerPelletGlow -= 0.05;
            if (visualJuice.powerPelletGlow <= 0) {
                visualJuice.powerPelletGlow = 0;
                visualJuice.powerPelletEffect = 0;
            }
        }
    }

    // Draw Overlays
    if (gameState === STATE.WON) {
        // Draw Level Up overlay
        ctx.fillStyle = 'rgba(16, 185, 129, 0.85)'; // Tailwind green-500 with opacity
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#d1fae5'; // Tailwind green-100
        ctx.font = 'bold 36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('LEVEL UP!', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '20px Arial';
        ctx.fillText('Great job! Get ready for the next level.', canvas.width / 2, canvas.height / 2 + 20);
    }

    if (gameState === STATE.LOST) {
        // Draw Game Over overlay
        ctx.fillStyle = 'rgba(220, 38, 38, 0.85)'; // Tailwind red-600 with opacity
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fee2e2'; // Tailwind red-200
        ctx.font = 'bold 36px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '20px Arial';
        ctx.fillText('Try again! Click to restart.', canvas.width / 2, canvas.height / 2 + 20);
    }

    // Fetch ghost states from backend periodically
    if (now - ghostStateLastFetched > ghostStateFetchInterval) {
        fetch("/ghost-states")
            .then(r => r.json())
            .then(states => {
                ghostVisualStates = states;
                ghostStateLastFetched = now;
            });
    }

    requestAnimationFrame(draw);
}

// Add event listener for dismissing overlays
canvas.addEventListener('click', () => {
    if (overlayActive) {
        dismissOverlay();
    }
});

// Power pellet effect triggers
function triggerPowerPelletEffect() {
    visualJuice.powerPelletEffect = 1;
    // Optionally, call backend to activate power pellet
    fetch("/activate-power-pellet", { method: "POST" });
}
function triggerPowerPelletDeactivation() {
    visualJuice.powerPelletEffect = -1;
    fetch("/deactivate-power-pellet", { method: "POST" });
}

// Game loop
setInterval(update, LOGIC_UPDATE_INTERVAL);
draw();
