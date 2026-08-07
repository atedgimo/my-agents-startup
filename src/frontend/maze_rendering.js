// src/frontend/maze_rendering.js

// This module handles rendering the maze and pellets on the canvas.

export function drawMaze(ctx, mazeData, tileSize) {
  ctx.fillStyle = '#000'; // Black background for maze
  ctx.fillRect(0, 0, mazeData[0].length * tileSize, mazeData.length * tileSize);

  ctx.fillStyle = '#222'; // Maze walls color
  for (let y = 0; y < mazeData.length; y++) {
    for (let x = 0; x < mazeData[y].length; x++) {
      if (mazeData[y][x] === 1) { // wall
        ctx.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
      }
    }
  }
}

export function drawPellets(ctx, pellets, tileSize) {
  ctx.fillStyle = '#fff'; // White pellets
  pellets.forEach(pellet => {
    const px = pellet.x * tileSize + tileSize / 2;
    const py = pellet.y * tileSize + tileSize / 2;
    const radius = pellet.isPowerPellet ? tileSize / 3 : tileSize / 6;
    ctx.beginPath();
    ctx.arc(px, py, radius, 0, 2 * Math.PI);
    ctx.fill();
  });
}
