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

// Maze Layout - 1=Wall, 0=Path/Pellet, 2=Power Pellet
const mazeData = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],
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

function update() {
    if (gameState !== STATE.PLAYING) return;

    // Logic for pellet collection and score tracking
    pellets.forEach(p => {
        if (p.active && playerPos_x === Math.round(playerX) && playerPos_y === Math.round(playerY)) { 
            // Note: In a full implementation, 'playerX'/'playerY' would be checked against pellet bounds.
            // For now, we simulate the collection logic for these items in the loop or during collision check.
        }
    });

    // Refined Logic: Iterate through pellets to detect "pickup"
    pellets.forEach(p => {
        if (p.active) {
            const dist = Math.hypot(playerX - (p.x * TILE_SIZE), playerY - (p.y * TILE_SIZE));
            if (dist < TILE_SIZE / 1.5) {
                p.active = false;
                score += 10; // Bug #0007: Increment score by 10
                // Update UI would happen automatically if draw() uses the 'score' variable (currently not displayed but logic is fixed).
            }
        }
    });

    let activePellets = pellets.filter(p => p.active !== false);
    if (activePellets.length === 0) {
        gameState = STATE.WON;
    }

    // Collision Detection logic for Loss Condition
    // Bug #0008: Detect ghost collision and state transition to LOST if no power_up
    ghosts.forEach(g => {
        const dist = Math.hypot(playerX - g.x, playerY - g.y);
        if (dist < 20) { // Simplified radius check
            if (!power_up) {
                gameState = STATE.LOST;
            } else {
                // Optional: logic for losing power-up if hit ghost while it's active
                power_up = false;
            }
        }
    });
}

function draw() {
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

    // Draw pellets
    ctx.fillStyle = '#facc15'; // Tailwind yellow-400
    pellets.forEach(p => {
        if (p.active !== false) {
            ctx.beginPath();
            ctx.arc(p.x * TILE_SIZE + TILE_SIZE / 2, p.y * TILE_SIZE + TILE_SIZE / 2, 4, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    // Draw Score (Added for completeness as per #0007 "updates the UI immediately")
    ctx.fillStyle = '#facc15';
    ctx.font = '16px Arial';
    ctx.fillText(`Score: ${score}`, 10, 20);

    // Draw Overlays
    if (gameState === STATE.WON) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#facc15';
        ctx.font = '30px Arial';
        ctx.fillText('LEVEL CLEAR!', canvas.width/2 - 100, canvas.height/2);
    }

    if (gameState === STATE.LOST) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ef4444'; // Tailwind red-500
        ctx.font = '30px Arial';
        ctx.fillText('GAME OVER', canvas.width/2 - 100, canvas.height/2);
    }

    requestAnimationFrame(draw);
}

// Mock data for ghosts and player (since they aren't fully defined in the snippet but needed for collision check)
let playerX = 100;
let playerY = 100;
const ghosts = [{x: 200, y: 200}, {x: 300, y: 400}];

// Logic to handle game loop state updates (ticked every frame or on event)
setInterval(update, 1000 / 60);

// Start the loop
draw();
