# Attitude Determination and Control Systems (ADCS)

Attitude Determination and Control Systems (ADCS) manage a CubeSat's orientation in space — whether it needs to point an antenna, aim a camera, or passively stabilize. This section covers passive methods (like gravity gradient booms and magnetic hysteresis), active control components (magnetorquers, reaction wheels), and sensors for determining orientation (sun sensors, magnetometers, star trackers, and gyros).

## Magnetometers


## Attitude Regimes and Requirements

To be added here:

- Mission-driven pointing requirements
- Detumbling vs. fine pointing
- Passive vs. active stabilization tradeoffs
- Typical ADCS performance metrics

## Passive Stabilization Methods

To be added here:

- Gravity gradient stabilization
- Magnetic hysteresis damping
- Spin stabilization
- Advantages, limitations, and mission fit

## Attitude Sensors

To be added here:

- Magnetometers
- Sun sensors (coarse and fine)
- Gyroscopes and IMUs
- Star trackers
- Sensor fusion considerations

### Magnetometers

To be added here:

- Calibration and alignment
- Noise sources and interference
- Use in attitude determination and control

#### Parts
- [RM3100-CB](https://www.pnisensor.com/rm3100-cb/) ([Using the RM3100-CB](https://hackaday.io/project/202392-playing-with-ultra-sensitive-magnetometer-rm3100/details))

## Actuators

To be added here:

- Magnetorquers (rods and coils)
- Reaction wheels
- Momentum dumping strategies
- Actuator sizing and placement

## Control Algorithms

To be added here:

- B-dot and detumbling controllers
- PID and state-space control
- Quaternion vs. Euler representations
- Controller tuning and stability

## Estimation and Sensor Fusion

To be added here:

- Attitude estimation problem overview
- Kalman and extended Kalman filters
- Combining IMU, magnetometer, and sun sensor data
- Common failure modes

## ADCS Integration Considerations

To be added here:

- Mechanical alignment and tolerances
- Magnetic cleanliness
- Power and thermal coupling
- Interaction with payload and comms

## Testing and Validation

To be added here:

- Helmholtz cages and magnetic testing
- Flatsat and HIL testing for ADCS
- On-orbit commissioning strategies
- Common pitfalls during bring-up

---

👉 **Please consider [contributing](../contributing.md)!**