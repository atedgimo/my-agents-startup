// Motion Interpolation Module

// This module provides frame-independent motion interpolation
// for smooth rendering of game objects moving on a discrete grid.
// Also provides a helper for smooth pellet collection animation.

class MotionInterpolator {
    constructor() {
        this.previousPosition = { x: 0, y: 0 };
        this.currentPosition = { x: 0, y: 0 };
        this.alpha = 0; // interpolation factor between 0 and 1
    }

    updatePosition(newPosition) {
        this.previousPosition = { ...this.currentPosition };
        this.currentPosition = { ...newPosition };
        this.alpha = 0;
    }

    interpolate(alpha) {
        this.alpha = alpha;
        return {
            x: this.previousPosition.x + (this.currentPosition.x - this.previousPosition.x) * this.alpha,
            y: this.previousPosition.y + (this.currentPosition.y - this.previousPosition.y) * this.alpha
        };
    }
}

// Helper for pellet collection animation
export function animatePelletCollection(pellet, duration = 300) {
    // pellet: {x, y, ...}
    pellet.animating = true;
    pellet.animationStart = performance.now();
    pellet.animationDuration = duration;
}

export default MotionInterpolator;
