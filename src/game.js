"""
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

// Maze Layout - 1=Wall, 0=Path/Pellet, 2=Power Pellet
const mazeData = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];

const pellets = [];
// Populate pellets from mazeData (type 0 means a path with a pellet)
for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
        if (mazeData[r][c] === 0) {
            pellets.push({ x: c, y: r });
        }
    }
}

function update() {
    if (gameState !== STATE.PLAYING) return;

    // Logic for pellet collection and win condition
    // Note: This is a simplified check as movement logic is being integrated in #0004
    // In a full implementation, this would happen during the move/collision phase.
    let activePellets = pellets.filter(p => p.active !== false);
    if (activePellets.length === 0) {
        gameState = STATE.WON;
    }

    // Collision Detection logic for Loss Condition
    // Logic: If player hits ghost and !power_up, then gameState = STATE.LOST
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

// Logic to handle game loop state updates (ticked every frame or on event)
setInterval(update, 1000 / 60);

// Start the loop
draw();
"""
