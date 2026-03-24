# Guidance, Navigation, and Control (GNC)

Guidance, Navigation, and Control (GNC) is the set of systems that allow a spacecraft to understand its state and influence its motion. It combines three closely related functions:

- **Guidance** – defining what the spacecraft should do (e.g. point an antenna at Earth, align a payload, follow a trajectory)
- **Navigation** – determining where the spacecraft is and how it is moving (position, velocity, and time)
- **Control** – applying forces or torques to achieve and maintain the desired state

Within this broader framework, **Attitude Determination and Control Systems (ADCS)** focus specifically on the spacecraft’s **orientation** – how it is rotated in space and how that orientation is measured and controlled.

In CubeSats and small spacecraft, GNC typically includes:

- Attitude determination using magnetometers, sun sensors, star trackers, and IMUs  
- Attitude control using magnetorquers and reaction wheels  
- Navigation and timing using GNSS or ground-based orbit determination  
- Control algorithms and estimation  

## Overview

- [NASA Small Spacecraft GNC](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/)
- [NASA State of the Art Small Spacecraft Technology](https://www.nasa.gov/wp-content/uploads/2021/10/5.soa_gnc_2021.pdf)
- [KiboCUBE Academy: Introduction to CubeSat Attitude Control System](https://www.unoosa.org/documents/pdf/psa/access2space4all/KiboCUBE/AcademySeason2/On-demand_Pre-recorded_Lectures/KiboCUBE_Academy_2021_OPL14.pdf)
- [KiboCUBE Academy Lecture 14 (Video)](https://www.youtube.com/watch?v=c--Yiz_7_MM&list=PLaOqa4cng0GGoAGKiMbo4noT8vaKUY43h&index=14)
- [CubeSat Mission and Bus Design – ADCS Chapter](https://pressbooks-dev.oer.hawaii.edu/epet302/part/8-attitude-determination-control-navigation/)

## Guidance

Defines the desired spacecraft behavior, such as pointing targets or trajectory objectives.

To be added here:

- Mission objectives and pointing modes
- Target tracking (Earth-pointing, Sun-pointing, inertial pointing)
- Operational modes (safe mode, detumble, nominal ops)
- Guidance profiles and timelines

## Navigation

Determines the spacecraft’s position, velocity, and time within a chosen reference frame.

To be added here:

- Orbit determination basics
- Onboard vs. ground-based navigation
- GNSS in space (LEO vs. high altitude considerations)
- Time synchronization and clocks
- State vectors and reference frames

## Reference Frames and Coordinate Systems

Defines how position and attitude are represented and transformed between coordinate systems. This is fundamental to both navigation and attitude determination.

To be added here:

- ECI, ECEF, body frame, orbital frame (LVLH)
- Transformations between frames
- Attitude representations (Euler angles, quaternions, DCMs)
- Common pitfalls (gimbal lock, frame confusion)

## Orbit Representation / TLEs

Describes how spacecraft orbits are represented and propagated over time.

- [Definition of Two-line Element Set Coordinate System](https://platform-cdn.leolabs.space/static/files/tle_definition.pdf?7ba94f05897b4ae630a3c5b65be7396c642d9c72)
- [TLE Overview (STK)](https://www.youtube.com/watch?v=woft1j_PJvA)
- [Two Line Element Set Explained](https://www.youtube.com/watch?v=_C-GQy0qTY0)
- [Classical Orbital Elements](https://www.youtube.com/watch?v=AReKBoiph6g)
- [Space Science with Python – Orbital Elements](https://youtu.be/7difa8aiUYo)
- [Classical Orbital Elements (COEs)](https://youtu.be/2gAYqtmNJx8)

To be added here:

- State vectors (position and velocity)
- Propagation and limitations

## Passive Stabilization Methods

Uses environmental forces and simple physical principles to stabilize spacecraft attitude without active control.

To be added here:

- Gravity gradient stabilization
- Magnetic hysteresis damping
- Spin stabilization
- Advantages, limitations, and mission fit

## Attitude Sensors

### Inertial Measurement Units (IMUs)

- [IMU Visualiser](https://www.youtube.com/watch?v=6vpdAXEQaoQ)
- [What is an IMU?](https://www.youtube.com/watch?v=qS9GwaekLW4)
- [Measuring Angles and Movement with an IMU](https://www.youtube.com/watch?v=3mgSi0RkANc)

### Magnetometers

Measure the local magnetic field and provide a reference vector for attitude determination. They are simple and reliable but sensitive to onboard interference and require careful placement and calibration.

To be added here:

- Calibration and alignment
- Noise sources and interference
- Use in attitude determination and control

#### Parts
- [RM3100-CB](https://www.pnisensor.com/rm3100-cb/)
    - [Using the RM3100-CB](https://hackaday.io/project/202392-playing-with-ultra-sensitive-magnetometer-rm3100/details)
    - [Investigation of a low-cost magneto-inductive magnetometer for space science application](https://gi.copernicus.org/articles/7/129/2018/gi-7-129-2018.html)
    - [Single-event effect testing of the PNI RM3100 magnetometer for space applications](https://gi.copernicus.org/articles/11/219/2022/)

### Gyroscopes

Measure **angular velocity** (how fast the spacecraft is rotating). They are essential for short-term attitude propagation but tend to **drift over time**, so they are usually combined with absolute sensors (e.g. magnetometers, sun sensors, star trackers).

To be added here:

- MEMS vs. fiber-optic / ring laser gyros (performance vs. cost)
- Bias, noise, and drift characteristics
- Calibration and temperature effects
- Role in sensor fusion (e.g. with magnetometer / star tracker)

#### Parts
- [TDK IAM-20380HT Gyroscope](https://invensense.tdk.com/products/iam-20380ht/)

### Star Trackers

Provide **high-precision absolute attitude** by imaging the star field and matching it against a catalog. They are the most accurate ADCS sensors but require more **compute, power, and careful optical design**.

- [UW Husky Satellite Lab Open-source Star Tracker (LOST)](https://github.com/UWCubeSat/lost)
- [How Star Trackers Work](https://www.youtube.com/watch?v=hA1LsvgV2UY)
- [Dr. Thomas Albin (Astrodynamics channel)](https://www.youtube.com/@DrThomasAlbin)

To be added here:

- Star identification and pattern matching
- Optics, sensor, and exposure considerations
- Sensitivity to stray light and Earth albedo
- Typical accuracy and update rates
- Open-source implementations and datasets

## Actuators

### Reaction Wheels

Active actuators that control attitude by **exchanging angular momentum** with the spacecraft. They enable precise pointing but introduce complexity and require **momentum management**.

- [University of Bristol: Satellite Reaction Wheels](https://www.youtube.com/watch?v=ZPWiIBcHOh4)
- [Liquid Metal Reaction Wheel](https://www.youtube.com/watch?v=wiRMdRi0LrI)
- [OreSat ADCS Hardware](https://github.com/oresat/oresat-adcs-hardware)
- [Rocket Lab Reaction Wheels](https://rocketlabcorp.com/space-systems/satellite-components/reaction-wheels/)
- [How to Turn a Satellite](https://www.youtube.com/watch?v=zkB3eqjh_mk)
- [CubeSat Reaction Wheel Control](https://github.com/yiqiangjizhang/CubeSat-Reaction-Wheel-control)

To be added here:

- Wheel configurations (3-axis vs. 4-wheel pyramid)
- Momentum buildup and desaturation (e.g. with magnetorquers)
- Jitter, vibration, and balancing
- Failure modes (bearing wear, saturation)
- Sizing vs. required torque and agility

### Magnetorquers

Generate torque by interacting with Earth’s magnetic field. They are simple, robust, and power-efficient, but provide **limited control authority** and depend on the local magnetic field.

- [University of Bristol: Satellite Magnetorquers](https://www.youtube.com/watch?v=r2Ep3aZ630U)
- [RGSAT Magnetorquers](https://www.youtube.com/watch?v=HfWni35TOeQ)
- [PCB Magnetorquer Prototype](https://www.youtube.com/watch?v=cGJYCe6mGR0)
- [Magnetorquer Winding Machine](https://www.youtube.com/watch?v=s6DOWAMhrVA)
- [Carl Bugeja](https://www.youtube.com/@CarlBugeja)

To be added here:

- Rod vs. coil (including PCB coil) implementations
- Torque generation (m × B) and axis limitations
- Use for detumbling (e.g. B-dot control)
- Interaction with onboard magnetometers
- Placement and magnetic cleanliness considerations

## Control Algorithms

Defines how sensor data is translated into actuator commands to achieve desired behavior.

To be added here:

- B-dot and detumbling controllers
- PID and state-space control
- Attitude vs. orbit control
- Quaternion vs. Euler representations
- Controller tuning and stability

## Estimation and Sensor Fusion

Combines data from multiple sensors to estimate spacecraft state reliably.

To be added here:

- Attitude estimation problem overview
- Kalman and extended Kalman filters
- Combining IMU, magnetometer, and sun sensor data
- Common failure modes

## Disturbances and Space Environment

External and internal forces that influence spacecraft motion and must be accounted for in control design.

To be added here:

- Gravity gradient torque
- Atmospheric drag (LEO)
- Solar radiation pressure
- Magnetic field interactions
- Internal disturbances (currents, moving parts)

## Modes of Operation

Defines how the spacecraft transitions between different control and mission states.

To be added here:

- Detumble mode
- Safe mode
- Nominal pointing modes
- Transition logic between modes
- Fault detection and recovery

## Navigation / PNT (Position, Navigation, Timing)

Provides **position, velocity, and time**, forming the navigation side of GNC and supporting guidance and control decisions.

- [OreSat GPS Hardware](https://github.com/oresat/oresat-gps-hardware)
- [Skytraq Orion B16 GNSS Module](https://navspark.mybigcommerce.com/12mm-x-16mm-gnss-receiver-module-for-leo-applications/)
- [The Wassenaar Arrangement](https://www.wassenaar.org/)
- [LeoLabs Visualization](https://platform.leolabs.space/visualization)
- [lumi.space](https://www.lumi.space/)

To be added here:

- GNSS in LEO and high-dynamic environments
- COCOM limits and high-altitude receivers
- Time synchronization and onboard clocks
- Ground-based orbit determination vs. onboard solutions
- Integration with guidance and control systems
- Dual use technology regulations and considerations

## ADCS Integration Considerations

Covers practical aspects of integrating sensors and actuators into a spacecraft system.

To be added here:

- Mechanical alignment and tolerances
- Magnetic cleanliness
- Power and thermal coupling
- Interaction with payload and comms

## Testing and Validation

Covers methods for verifying GNC systems before and during flight.

- [UC CubeCats Helmholtz Cage](https://uccubecats.github.io/HelmholtzCage.html)

To be added here:

- Helmholtz cages and magnetic testing
- Flatsat and HIL testing for ADCS
- On-orbit commissioning strategies
- Common pitfalls during bring-up

👉 **Please consider [contributing](../contributing.md)!**