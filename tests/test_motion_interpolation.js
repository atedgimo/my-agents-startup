import MotionInterpolator from '../src/frontend/motionInterpolation.js';

describe('MotionInterpolator', () => {
  let interpolator;

  beforeEach(() => {
    interpolator = new MotionInterpolator();
  });

  test('initial positions are zero', () => {
    expect(interpolator.previousPosition).toEqual({ x: 0, y: 0 });
    expect(interpolator.currentPosition).toEqual({ x: 0, y: 0 });
    expect(interpolator.alpha).toBe(0);
  });

  test('updatePosition updates positions correctly', () => {
    interpolator.updatePosition({ x: 5, y: 10 });
    expect(interpolator.previousPosition).toEqual({ x: 0, y: 0 });
    expect(interpolator.currentPosition).toEqual({ x: 5, y: 10 });
    expect(interpolator.alpha).toBe(0);

    interpolator.updatePosition({ x: 10, y: 20 });
    expect(interpolator.previousPosition).toEqual({ x: 5, y: 10 });
    expect(interpolator.currentPosition).toEqual({ x: 10, y: 20 });
    expect(interpolator.alpha).toBe(0);
  });

  test('interpolate returns correct interpolated position', () => {
    interpolator.updatePosition({ x: 0, y: 0 });
    let pos = interpolator.interpolate(0.5);
    expect(pos).toEqual({ x: 0, y: 0 }); // no movement yet

    interpolator.updatePosition({ x: 10, y: 10 });
    pos = interpolator.interpolate(0);
    expect(pos).toEqual({ x: 0, y: 0 });
    pos = interpolator.interpolate(0.5);
    expect(pos).toEqual({ x: 5, y: 5 });
    pos = interpolator.interpolate(1);
    expect(pos).toEqual({ x: 10, y: 10 });
  });

  test('interpolate updates alpha property', () => {
    interpolator.updatePosition({ x: 0, y: 0 });
    interpolator.interpolate(0.7);
    expect(interpolator.alpha).toBe(0.7);
  });
});
