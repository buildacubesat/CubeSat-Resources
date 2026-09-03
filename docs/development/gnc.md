# Guidance, Navigation, and Control (GNC)

Guidance, Navigation, and Control (GNC) is the set of systems that allow a spacecraft to understand its state and influence its motion. It combines three closely related functions:

- **Guidance** – defining what the spacecraft should do (e.g. point an antenna at Earth, align a payload, follow a trajectory)
- **Navigation** – determining where the spacecraft is and how it is moving (position, velocity, and time)
- **Control** – applying forces or torques to achieve and maintain the desired state

Within this broader framework, **Attitude Determination and Control Systems (ADCS)** focus specifically on the spacecraft's **orientation** – how it is rotated in space and how that orientation is measured and controlled. On a CubeSat this is where nearly all the GNC effort goes: few small missions manoeuvre, but many need to point.

## Overview

<!-- CSR-RESOURCES:START dev-gnc-overview -->
- **[NASA Small Spacecraft GNC](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/)** `Link` – NASA's regularly updated state-of-the-art survey of small spacecraft GNC hardware, with performance and mass figures by component class
- **[NASA State of the Art Small Spacecraft Technology (2021 GNC chapter)](https://www.nasa.gov/wp-content/uploads/2021/10/5.soa_gnc_2021.pdf)** `PDF` – Archived PDF edition of the GNC chapter
- **[KiboCUBE Academy: Introduction to CubeSat Attitude Control System](https://www.unoosa.org/documents/pdf/psa/access2space4all/KiboCUBE/AcademySeason2/On-demand_Pre-recorded_Lectures/KiboCUBE_Academy_2021_OPL14.pdf)** `PDF` – UNOOSA lecture notes introducing CubeSat attitude control
- **[KiboCUBE Academy Lecture 14 (Video)](https://www.youtube.com/watch?v=c--Yiz_7_MM&list=PLaOqa4cng0GGoAGKiMbo4noT8vaKUY43h&index=14)** `Link` – Video version of the KiboCUBE ADCS lecture
- **[CubeSat Mission and Bus Design – ADCS Chapter](https://pressbooks-dev.oer.hawaii.edu/epet302/part/8-attitude-determination-control-navigation/)** `Link` – Open-access textbook chapter on attitude determination, control and navigation
<!-- CSR-RESOURCES:END dev-gnc-overview -->

## Guidance

Guidance defines the desired spacecraft behavior – what the spacecraft *should* be doing at any moment. It is the bridge between mission objectives and the control system.

### Pointing modes

Most CubeSat missions need a small set of pointing modes, each driven by a mission need:

- **[Nadir](../references/glossary.md#nadir)-pointing** – a fixed body axis held toward the centre of the Earth. The standard for Earth observation and for fixed downward-facing antennas.
- **Sun-pointing** – maximising solar array output. Frequently the default attitude in [safe mode](../references/glossary.md#safe-mode), because it is the one that keeps the spacecraft alive. See [EPS](eps.md#illumination-eclipse-and-incidence-angle).
- **Inertial pointing** – a fixed orientation relative to the stars, for astronomy payloads or for holding a direction across an orbit.
- **Target tracking** – following a ground station or a ground target through a pass. Needed for directional antennas and for off-nadir imaging.
- **Velocity/ram or anti-ram pointing** – minimising drag, or deliberately maximising it for deorbit.
- **Uncontrolled / tumbling** – not a failure necessarily, but a valid mode for a mission with no pointing requirement, and the state you will be in immediately after deployment.

### Turning objectives into requirements

Guidance is where vague mission goals become numbers the control engineer can work with. Two distinctions matter and are frequently confused:

- **[Pointing knowledge](../references/glossary.md#pointing-accuracy-pointing-knowledge)** – how well you know where you were pointing, which can be determined after the fact from recorded sensor data.
- **Pointing accuracy** (control) – how well you actually pointed at the time.

Knowledge is much cheaper than accuracy. An imaging mission that can georeference its pictures afterwards may need 0.05° of knowledge but only 1° of control. Specifying tight control when you only needed knowledge is one of the most common ways to make an ADCS unnecessarily expensive.

Also specify **pointing stability** (drift over an exposure) and **[slew](../references/glossary.md#slew) rate** (how fast you can reorient, which sets how much of a pass you can use).

### Guidance profiles and timelines

Because contact is intermittent, guidance is usually pre-planned: the ground uplinks a timeline of attitude commands tied to times or orbital positions, and the spacecraft executes it autonomously. This means guidance depends on the spacecraft knowing both the time and its orbital position accurately – see [Navigation](#navigation) – and it means the timeline must fail safely if it runs past its validity. See [Flight Software – Modes](flight-software.md#modes-state-machines-and-autonomy).

## Navigation

Navigation determines the spacecraft's position, velocity, and time within a chosen reference frame.

### Onboard vs. ground-based

- **Ground-based orbit determination** is the default for CubeSats with no pointing requirements. The US Space Surveillance Network tracks objects and publishes [TLEs](../references/glossary.md#tle); you propagate them on the ground and uplink what the spacecraft needs. Cheap, requires no hardware, and adequate for many missions.
- **Onboard GNSS** gives the spacecraft its own position, velocity and time continuously, which is what makes autonomous operation possible. NASA's survey reports around **1.5 m position accuracy** as achievable with flight-proven small spacecraft GPS receivers.[^nasa-soa-gnc]
- **Onboard propagation** – carrying an SGP4 propagator and a periodically uplinked TLE – is the pragmatic middle ground, and is what many missions actually fly. Accuracy degrades with time since the last uplink, typically from around a kilometre at [epoch](../references/glossary.md#epoch) to tens of kilometres after a couple of weeks.

### GNSS in space

A GNSS receiver in [LEO](../references/glossary.md#leo) is not operating in its design environment:

- **High dynamics.** Orbital velocity is roughly 7.5 km/s, producing far larger Doppler shifts than any terrestrial application. A standard receiver may never acquire a lock.
- **Different geometry.** Satellites are *below* you as well as above; the receiving antenna must be pointed toward the GNSS constellation, which for a LEO spacecraft means zenith-facing.
- **[COCOM limits](../references/glossary.md#cocom-limits).** Commercial receivers are required to disable themselves above roughly 18 km altitude and 1,900 km/h. Space-capable receivers have these limits removed or reconfigured – which is precisely what makes them export-controlled.
- **Export control.** GNSS receivers capable of operating at orbital velocity fall under dual-use export regimes such as the Wassenaar Arrangement, and under ITAR/EAR in the US. This affects procurement lead times and who you can buy from. Treat it as a schedule risk, not a formality. See [Qualification and Launch – Regulatory Requirements](launch.md#regulatory-requirements).

### Time

Navigation is inseparable from timing. Attitude determination needs time to evaluate the orbital position and the magnetic field model; payload data is often worthless without an accurate timestamp. GNSS provides time to sub-microsecond accuracy when locked; otherwise an RTC disciplined by ground uplink is the fallback. See [OBC – Timing and Timekeeping](obc.md#timing-and-timekeeping).

### PNT hardware and resources

<!-- CSR-RESOURCES:START dev-gnc-pnt-hardware -->
- **[OreSat GPS Hardware](https://github.com/oresat/oresat-gps-hardware)** `Link` – Open-source GPS receiver hardware for CubeSats
- **[Skytraq Orion B16 GNSS Module](https://navspark.mybigcommerce.com/12mm-x-16mm-gnss-receiver-module-for-leo-applications/)** `Link` – Compact GNSS receiver module marketed for LEO applications
- **[The Wassenaar Arrangement](https://www.wassenaar.org/)** `Link` – Multilateral export control regime covering dual-use technologies including space-capable GNSS receivers
- **[LeoLabs Visualization](https://platform.leolabs.space/visualization)** `Link` – Interactive visualisation of tracked objects in low Earth orbit
- **[lumi.space](https://www.lumi.space/)** `Link` – Satellite laser ranging services for precise orbit determination
<!-- CSR-RESOURCES:END dev-gnc-pnt-hardware -->

## Reference Frames and Coordinate Systems

Almost every hard-to-find ADCS bug is a frame error. Being pedantic here saves weeks later.

### The frames you need

- **[ECI](../references/glossary.md#eci)** (Earth-Centered Inertial) – non-rotating, centred on Earth. Where orbital dynamics are computed. Note that "inertial" requires an epoch: J2000 and TEME are both ECI frames and they are *not* the same. SGP4 outputs TEME, which is a classic source of arcminute-level errors when silently treated as J2000.
- **[ECEF](../references/glossary.md#ecef)** (Earth-Centered, Earth-Fixed) – rotates with the Earth. Used for ground station positions, latitude/longitude, and Earth-referenced targets.
- **[LVLH](../references/glossary.md#lvlh)** (Local Vertical, Local Horizontal) – orbital frame following the spacecraft, one axis to nadir and one along track. The natural frame for expressing nadir-pointing attitudes.
- **Body frame** – fixed to the spacecraft structure. Every sensor and actuator has its own mounting orientation relative to it.
- **Sensor frames** – each sensor's own axes, related to the body frame by a mounting matrix that must be measured, not assumed.

### Attitude representations

- **Direction cosine matrices (DCM)** – 3×3 rotation matrices. Unambiguous and composable, but nine numbers with six constraints, so they drift from orthonormality with repeated multiplication and need periodic re-orthonormalisation.
- **Euler angles** – three angles, intuitive to humans, and afflicted by [gimbal lock](../references/glossary.md#gimbal-lock) at singularities. Fine for displaying attitude to an operator; a poor choice for computing it.
- **[Quaternions](../references/glossary.md#quaternion)** – four numbers, no singularities, numerically well-behaved, cheap to propagate. The standard onboard representation. The costs are that they are not intuitive, that q and −q represent the same rotation (so you must handle sign consistency in filters and interpolation), and that conventions differ.

### Conventions that will bite you

- **Quaternion ordering.** Scalar-first (q₀, q₁, q₂, q₃) versus scalar-last (q₁, q₂, q₃, q₀). Different libraries make different choices and neither always documents it.
- **Rotation direction.** Whether a quaternion rotates a *vector* or transforms between *frames* – the two are inverses of one another.
- **Euler sequence.** 3-2-1 versus 3-1-3 and the rest; twelve possibilities, all called "Euler angles".
- **Units and sign.** Degrees vs radians, and the handedness of each sensor's axes.

**Write the conventions down in one document, state them at the top of every module, and test round-trip conversions.** A unit test that converts a known rotation through every representation and back catches almost all of these before they reach hardware.

## Orbit Representation / TLEs

### Orbital elements

A Keplerian orbit is fully described by six **classical orbital elements**: semi-major axis (size), eccentricity (shape), [inclination](../references/glossary.md#inclination) (tilt relative to the equator), [RAAN](../references/glossary.md#raan) (where the orbit crosses the equator going north), argument of perigee (orientation within the plane) and true anomaly (position along the orbit). Equivalently, the same state is captured by a **state vector** – three components of position and three of velocity at a given epoch – which is what propagators integrate and what most software actually passes around.

For CubeSats, two orbit types dominate: **[sun-synchronous orbits](../references/glossary.md#sso) (SSO)**, whose precession keeps the local solar time of each pass constant (valuable for imaging and, in the dawn–dusk case, for near-continuous illumination), and lower-inclination orbits from ISS deployment, which give shorter lifetimes and different [beta angle](../references/glossary.md#beta-angle) behaviour.

### TLEs and SGP4

A **[TLE](../references/glossary.md#tle)** is a compact, fixed-format encoding of an orbit at an epoch. It is not a state vector in any general sense: **TLEs are only meaningful when propagated with [SGP4](../references/glossary.md#sgp4)**, the specific analytical model whose internal assumptions the element values were fitted to. Feeding TLE elements into a general-purpose Keplerian propagator produces plausible-looking, wrong answers.

Practical limitations worth knowing:

- Accuracy is roughly a kilometre near epoch, degrading to tens of kilometres over one to two weeks. Refresh TLEs regularly.
- SGP4 outputs coordinates in the **TEME** frame, not J2000 – see above.
- After deployment, several CubeSats released together are catalogued as a cluster and take days to weeks to be individually identified. Early operations often mean tracking several candidate TLEs at once and using Doppler signature to work out which one is yours.

<!-- CSR-RESOURCES:START dev-gnc-orbits-and-tles -->
- **[Definition of Two-line Element Set Coordinate System](https://platform-cdn.leolabs.space/static/files/tle_definition.pdf?7ba94f05897b4ae630a3c5b65be7396c642d9c72)** `PDF` – Reference definition of the TLE format and its coordinate system
- **[TLE Overview (STK)](https://www.youtube.com/watch?v=woft1j_PJvA)** `Link` – Video introduction to two-line element sets
- **[Two Line Element Set Explained](https://www.youtube.com/watch?v=_C-GQy0qTY0)** `Link` – Field-by-field walkthrough of the TLE format
- **[Classical Orbital Elements](https://www.youtube.com/watch?v=AReKBoiph6g)** `Link` – Introduction to the six classical orbital elements
- **[Space Science with Python – Orbital Elements](https://youtu.be/7difa8aiUYo)** `Link` – Practical orbital elements tutorial in Python
- **[Classical Orbital Elements (COEs)](https://youtu.be/2gAYqtmNJx8)** `Link` – Further explanation of the classical orbital elements
<!-- CSR-RESOURCES:END dev-gnc-orbits-and-tles -->

See also [Ground Segment – Tracking and Pass Prediction](ground-segment.md#tracking-and-pass-prediction).

## Passive Stabilization Methods

Passive stabilisation uses environmental forces and simple physics instead of active control. It costs no power, has nothing to fail, and for a surprising number of missions it is sufficient. If your requirement is "keep the antenna roughly downward and don't tumble too fast", passive methods deserve serious consideration before you buy an ADCS.

- **[Gravity gradient stabilisation](../references/glossary.md#gravity-gradient-stabilisation)** exploits the fact that a non-spherical body in a gravity field experiences a torque aligning its long axis with the local vertical. Effective for elongated spacecraft – a 3U is already a reasonable shape, and a deployed boom with a tip mass dramatically increases the effect. Typically delivers a few degrees of nadir pointing, is bistable (it will happily settle upside down), and provides no yaw control at all.
- **Magnetic hysteresis damping** uses rods of high-permeability material that dissipate rotational energy as the Earth's magnetic field sweeps through them during each orbit. This is a *damper*, not a controller: it bleeds off tumbling rates. Very common alongside a permanent magnet.
- **Permanent magnets** align a body axis with the local geomagnetic field. Simple and effective, but the resulting attitude follows the field, which means the spacecraft flips twice per orbit – acceptable for an omnidirectional antenna, not for a camera. Almost always paired with hysteresis rods, which damp the resulting oscillation.
- **Spin stabilisation** uses gyroscopic stiffness to hold a spin axis inertially fixed. Requires spinning up, and constrains the spacecraft to one useful pointing direction.
- **Aerodynamic stabilisation** uses drag on deployed surfaces to weathervane the spacecraft into the velocity vector. Only effective at lower altitudes where there is enough atmosphere.

The design consideration common to all of these: **passive methods must be designed in from the start**, because they depend on mass distribution, geometry and magnetic properties that are hard to change late. And they interact – a permanent magnet makes magnetorquer-based control much harder, and magnetic hysteresis material will damp your reaction wheels' authority too.

## Attitude Sensors

Attitude determination needs at least **two non-parallel reference vectors** measured in the body frame and known in an inertial frame. One vector leaves you with an unresolved rotation about it. This is why almost every CubeSat carries both a magnetometer and a sun sensor: two cheap vectors give a full attitude solution – except in eclipse, when the sun sensor stops working, which is why gyros exist.

### Sun sensors

Sun sensors measure the direction to the Sun and are the cheapest useful attitude sensor available. NASA's survey spans the range:[^nasa-soa-gnc]

- **Cosine detectors** – a bare photodiode whose output varies with incidence angle. Simplest possible, **2–5°** accuracy. Often just the current from a solar panel, which means you may already have coarse sun sensing for free.
- **Quadrant detectors** – four cells behind an aperture, comparing outputs, **0.2–0.5°**.
- **Digital sun sensors / sun cameras** – an aperture imaged onto a detector array, reaching **0.1° down to 0.01°**.

Masses run from **3 g to 375 g**.[^nasa-soa-gnc] Practical considerations: you need enough of them for full sky coverage (typically five or six faces), Earth albedo can be mistaken for the Sun by simple detectors, and they are useless in eclipse – up to two-fifths of every orbit at low beta angles.

### Inertial Measurement Units (IMUs)

An [IMU](../references/glossary.md#imu) packages gyroscopes together with accelerometers. On an orbiting spacecraft only half of it earns its place: in free fall the accelerometers read essentially zero, sensing only non-gravitational accelerations such as drag and thruster firings. The gyroscopes are the part that matters for attitude, and they are covered in [Gyroscopes](#gyroscopes) below.

<!-- CSR-RESOURCES:START dev-gnc-imu-resources -->
- **[IMU Visualiser](https://www.youtube.com/watch?v=6vpdAXEQaoQ)** `Link` – Visual explanation of IMU behaviour
- **[What is an IMU?](https://www.youtube.com/watch?v=qS9GwaekLW4)** `Link` – Introduction to inertial measurement units
- **[Measuring Angles and Movement with an IMU](https://www.youtube.com/watch?v=3mgSi0RkANc)** `Link` – Practical guide to angle and motion measurement with an IMU
<!-- CSR-RESOURCES:END dev-gnc-imu-resources -->

### Magnetometers

Measure the local magnetic field and provide a reference vector for attitude determination. They are simple and reliable but sensitive to onboard interference and require careful placement and calibration.

NASA's survey gives magnetometer-based two-axis attitude estimation at roughly **0.25° accuracy**, with resolutions of **1–25 nT** and masses of **6–330 g**.[^nasa-soa-gnc]

**Calibration and interference.** A magnetometer measures the total field, which is the Earth's field plus everything your own spacecraft is doing. The corrections needed:

- **Hard-iron effects** – a constant offset from permanent magnetisation in nearby materials.
- **Soft-iron effects** – a direction-dependent distortion from ferromagnetic material.
- **Current-loop interference** – fields generated by your own harness, solar panel strings and switching converters. This one varies with spacecraft mode, which makes it much harder than a static calibration: the field measured with the transmitter on is not the field measured with it off.
- **Magnetorquer crosstalk** – your own actuator swamps the sensor completely. Standard practice is to **interleave**: pulse the magnetorquers, then measure with them off.

Calibration is done on the ground in a [Helmholtz cage](#testing-and-validation) and refined in orbit. Magnetic cleanliness – twisted-pair harness, minimised current loops, non-ferrous fasteners, sensor placement as far from batteries and torquers as geometry allows, ideally on a short boom – is a whole-spacecraft discipline, not a magnetometer problem. See [Structure](structure.md#fasteners-and-assembly).

Because the geomagnetic field must be *predicted* to be useful as a reference, you also need an onboard field model (IGRF or a reduced-order fit) and therefore accurate time and position.

#### Parts

<!-- CSR-RESOURCES:START dev-gnc-magnetometer-parts -->
- **[RM3100-CB](https://www.pnisensor.com/rm3100-cb/)** `Link` – Magneto-inductive three-axis magnetometer widely used in CubeSats
- **[Using the RM3100-CB](https://hackaday.io/project/202392-playing-with-ultra-sensitive-magnetometer-rm3100/details)** `Link` – Practical project notes on working with the RM3100
- **[Investigation of a low-cost magneto-inductive magnetometer for space science application](https://gi.copernicus.org/articles/7/129/2018/gi-7-129-2018.html)** `Link` – Open-access evaluation of the RM3100 for space science use
- **[Single-event effect testing of the PNI RM3100 magnetometer for space applications](https://gi.copernicus.org/articles/11/219/2022/)** `Link` – Open-access radiation testing results for the RM3100
<!-- CSR-RESOURCES:END dev-gnc-magnetometer-parts -->

### Gyroscopes

Measure **angular velocity** (how fast the spacecraft is rotating). They are essential for short-term attitude propagation but tend to **drift over time**, so they are usually combined with absolute sensors (e.g. magnetometers, sun sensors, star trackers).

- **MEMS gyros** are what CubeSats fly: grams, milliwatts, a few euros. The tradeoff is bias stability. NASA's survey cites gyro bias stability around **0.15°/hour** for good small spacecraft units;[^nasa-soa-gnc] cheap consumer MEMS parts are far worse, drifting degrees per minute.
- **Fibre-optic and ring laser gyros** offer orders of magnitude better stability, at masses and costs that put them out of reach for most CubeSats.

What actually matters in practice:

- **Bias** – a non-zero output at rest. Estimated continuously by the attitude filter and removed; this is one of the main jobs an [EKF](#estimation-and-sensor-fusion) does.
- **Bias instability and random walk** – how fast the estimate degrades between absolute updates. This sets how long you can coast through eclipse on gyros alone.
- **Temperature sensitivity** – MEMS bias varies strongly with temperature. Characterise across your operating range and compensate; a lookup table from thermal-vacuum data is a cheap and large improvement.
- **Scale factor and misalignment** – errors proportional to rate, significant during fast slews.

#### Parts

<!-- CSR-RESOURCES:START dev-gnc-gyroscope-parts -->
- **[TDK IAM-20380HT Gyroscope](https://invensense.tdk.com/products/iam-20380ht/)** `Link` – High-temperature three-axis MEMS gyroscope
<!-- CSR-RESOURCES:END dev-gnc-gyroscope-parts -->

### Star Trackers

Provide **high-precision absolute attitude** by imaging the star field and matching it against a catalog. They are the most accurate ADCS sensors but require more **compute, power, and careful optical design**.

Performance from NASA's survey: cross-axis accuracy of **2–30 arcseconds** depending on unit, with masses from **0.04 to 2.7 kg**. Representative devices include Blue Canyon's NST (6 arcsec, Gen 2), Jena-Optronik's ASTRO APS3 (2.4 arcsec) and Arcsec's Sagitta (6 arcsec).[^nasa-soa-gnc]

How they work, and where they fail:

- **Lost-in-space identification** matches an observed star pattern against a catalogue with no prior attitude estimate – the hard case, and what distinguishes a real star tracker from a camera. **Tracking mode**, updating from a known prior, is far cheaper computationally.
- **Stray light is the dominant practical constraint.** Sun, Earth albedo and Moon in the field of view all blind the sensor. Baffle design is as important as the optics, and exclusion angles (often 30–40° from the Earth limb and much more from the Sun) directly constrain which attitudes give you a valid solution. Plan attitudes so the star tracker keeps a usable view.
- **Slew rate limits.** Long exposures smear stars. Most trackers lose lock above a few degrees per second, which means they cannot help you during detumble.
- **Compute.** Centroiding and pattern matching need real processing – one reason star trackers are usually self-contained units with their own processor.

<!-- CSR-RESOURCES:START dev-gnc-star-tracker-resources -->
- **[UW Husky Satellite Lab Open-source Star Tracker (LOST)](https://github.com/UWCubeSat/lost)** `Link` – Open-source star tracker algorithm implementation and test framework
- **[How Star Trackers Work](https://www.youtube.com/watch?v=hA1LsvgV2UY)** `Link` – Video explanation of star tracker operating principles
- **[Dr. Thomas Albin (Astrodynamics channel)](https://www.youtube.com/@DrThomasAlbin)** `Link` – Astronomy and Python channel covering star identification and astrodynamics
<!-- CSR-RESOURCES:END dev-gnc-star-tracker-resources -->

## Actuators

### Reaction Wheels

Active actuators that control attitude by **exchanging angular momentum** with the spacecraft. They enable precise pointing but introduce complexity and require **momentum management**.

NASA's survey summarises the small spacecraft range as **0.00023 to 0.3 Nm** peak torque and **0.0005 to 8 Nms** momentum storage – though the chapter's own component tables list units beyond that ceiling, so read the summary as describing the bulk of the market rather than its limits. Examples run from CubeSpace's CW0017 (0.0017 Nms, 60 g) at the small end up to Blue Canyon's RW16 at **16 Nms** and 7.5 kg.[^nasa-soa-gnc] Where the summary and the component tables disagree, trust the component tables and the manufacturers' current datasheets.

**Configurations.** Three orthogonal wheels give full three-axis control with no redundancy. A **four-wheel pyramid** tolerates any single wheel failure and spreads torque across units, at the cost of a fourth wheel and a control allocation problem. Given that wheel bearings are among the most common ADCS failure modes, the fourth wheel is often worth its mass.

**[Momentum desaturation](../references/glossary.md#momentum-desaturation)** is the fundamental constraint. Continuous disturbance torques accumulate momentum in the wheels; once a wheel reaches maximum speed it can produce no further torque in that direction, and the spacecraft loses control authority about that axis. Momentum must be dumped to the environment – on a CubeSat, using magnetorquers against the Earth's field. **A reaction wheel system without a momentum dumping mechanism will saturate and stop working.** Sizing the magnetorquers to dump momentum faster than the disturbances accumulate is a real design constraint, not a detail.

**Other practical issues:** wheel imbalance causes jitter that can blur images from the same spacecraft the wheels are pointing; bearing lubricant behaviour is temperature-dependent and bearings wear; and wheels passing through zero speed exhibit friction nonlinearity that makes precise low-rate control difficult (some systems deliberately bias wheels away from zero to avoid it).

<!-- CSR-RESOURCES:START dev-gnc-reaction-wheel-resources -->
- **[University of Bristol: Satellite Reaction Wheels](https://www.youtube.com/watch?v=ZPWiIBcHOh4)** `Link` – Educational video on reaction wheel operation
- **[Liquid Metal Reaction Wheel](https://www.youtube.com/watch?v=wiRMdRi0LrI)** `Link` – Experimental liquid metal reaction wheel concept
- **[OreSat ADCS Hardware](https://github.com/oresat/oresat-adcs-hardware)** `Link` – Open-source CubeSat ADCS hardware designs
- **[Rocket Lab Reaction Wheels](https://rocketlabcorp.com/space-systems/satellite-components/reaction-wheels/)** `Link` – Commercial reaction wheel product range
- **[How to Turn a Satellite](https://www.youtube.com/watch?v=zkB3eqjh_mk)** `Link` – Introduction to spacecraft attitude actuation
- **[CubeSat Reaction Wheel Control](https://github.com/yiqiangjizhang/CubeSat-Reaction-Wheel-control)** `Link` – Open reaction wheel control simulation code
<!-- CSR-RESOURCES:END dev-gnc-reaction-wheel-resources -->

### Magnetorquers

Generate torque by interacting with Earth's magnetic field. They are simple, robust, and power-efficient, but provide **limited control authority** and depend on the local magnetic field.

The governing relation is **τ = m × B**: torque equals the commanded magnetic dipole crossed with the local field. NASA's survey summarises small spacecraft units at **0.15 to 15 A·m²**, with ZARM's MT0.2-1 (0.2 A·m², 12 g) near the bottom of the range; as with reaction wheels, the chapter's component table runs past its own summary, listing Rocket Lab's TQ-40 at **48 A·m²** and 825 g.[^nasa-soa-gnc] As with the wheels, the component table and the manufacturer's datasheet are the figures to design against.

The cross product is the whole story:

- **You cannot generate torque about the field direction.** At any instant, magnetorquers give you control over only two axes. Full three-axis control is recovered only because the field direction changes as the spacecraft moves around its orbit – which means magnetic-only control is **underactuated at any instant but controllable over an orbit**. This is why magnetic-only attitude control is slow.
- **Authority varies with position.** The geomagnetic field runs roughly **20–55 µT across the 400–600 km band** – appreciably weaker than the 25–65 µT at Earth's surface, since the field falls off with the cube of the radius and that band sits at 0.76–0.83 of the surface value. It is strongest near the poles and weakest over the South Atlantic Anomaly, so control authority varies around the orbit.

**Implementations.** Air-core coils are simple and linear. Rod torquers wind the coil around a ferromagnetic core, multiplying the dipole for the same current and mass, at the cost of residual magnetisation (the core stays slightly magnetised after use, which your magnetometer will see). **PCB-embedded coils** – spiral traces in the board copper – cost essentially nothing and take no volume, and are a popular choice for very small satellites where the required dipole is modest.

**Interaction with magnetometers** is the recurring practical problem: your actuator produces a field thousands of times larger than the one you are trying to measure. Interleaving actuation and measurement in time is the standard solution.

<!-- CSR-RESOURCES:START dev-gnc-magnetorquer-resources -->
- **[University of Bristol: Satellite Magnetorquers](https://www.youtube.com/watch?v=r2Ep3aZ630U)** `Link` – Educational video on magnetorquer operation
- **[RGSAT Magnetorquers](https://www.youtube.com/watch?v=HfWni35TOeQ)** `Link` – Practical magnetorquer build from the RGSAT project
- **[PCB Magnetorquer Prototype](https://www.youtube.com/watch?v=cGJYCe6mGR0)** `Link` – PCB-embedded coil magnetorquer prototype
- **[Magnetorquer Winding Machine](https://www.youtube.com/watch?v=s6DOWAMhrVA)** `Link` – DIY coil winding machine for magnetorquer manufacture
- **[Carl Bugeja](https://www.youtube.com/@CarlBugeja)** `Link` – PCB coil and flexible electronics experiments relevant to PCB magnetorquer design
<!-- CSR-RESOURCES:END dev-gnc-magnetorquer-resources -->

### Thrusters

Propulsion gives translational control – orbit raising, phasing, collision avoidance, controlled deorbit – and can provide attitude control, though it is rarely used that way on CubeSats because propellant is finite while magnetorquers are not. Miniaturised electric and cold-gas systems are increasingly available at CubeSat scale – see [Propulsion](propulsion.md) for the options, the delta-v arithmetic and the safety and regulatory requirements that arrive with them.

## Control Algorithms

### Detumbling and B-dot

After deployment the spacecraft is tumbling, typically at a few degrees per second. Nothing else works until that is fixed: solar generation is poor, the star tracker cannot lock, and communications are intermittent. **[Detumbling](../references/glossary.md#detumbling) is the first thing your ADCS must do, and it must work autonomously with no ground help.**

The **[B-dot](../references/glossary.md#b-dot) controller** is the standard answer, and its appeal is that it needs *only* a magnetometer and magnetorquers – no attitude knowledge, no rate gyro, no orbit knowledge. The insight is that if the spacecraft is rotating, the measured field vector changes in the body frame; commanding a dipole opposing that rate of change extracts rotational energy. In its common form the commanded dipole is **m = −k·Ḃ**, and variants exist that command a dipole held orthogonal to the field.

Reported performance is good: one published algorithm using only three-axis magnetometer data reduced rotational kinetic energy by two orders of magnitude **within roughly 4,500 s – less than one orbital period** – for a 3U with a 0.3 A·m² dipole limit, with steady-state angular rate errors within ±0.2°/s.[^carletta]

Practical notes: B-dot is robust and hard to destabilise, which is exactly what you want as the first thing to run in orbit. It is a *rate* controller – it will not give you a pointing attitude. And it needs the magnetometer read with the torquers off.

### Pointing control

- **PID control** on each axis is simple, well understood, and adequate for many missions. Tuning is complicated by cross-axis coupling and by wheel dynamics.
- **Quaternion feedback control** works directly with the attitude error quaternion rather than decomposed angles, avoiding singularities and handling large slews properly. The standard approach for reaction-wheel systems.
- **LQR and state-space methods** allow explicit trade-off between pointing error and control effort, useful when actuator authority is tight.
- **Sliding mode and robust control** handle uncertain inertia and disturbances, which is relevant given that CubeSat inertia tensors are often known poorly.
- **Magnetic-only control laws** must cope with the underactuation described above. Cross-product control and various periodic/LQR formulations exist; all are slow and none give arbitrary pointing quickly.

### Loop rates

Attitude dynamics on a CubeSat are slow – body rates of a few degrees per second, time constants of minutes – so control loops typically run at **1–10 Hz**, not the kilohertz rates familiar from terrestrial motion control. The rate is bounded from below by the dynamics you need to track and from above by three practical limits: sensor sampling rates, the magnetometer/magnetorquer interleaving duty cycle (you cannot measure and actuate at the same time – see [Magnetorquers](#magnetorquers)), and the processor time you are willing to spend against everything else onboard.

Choose it deliberately and hold it fixed. A control loop whose period varies with system load is a control loop you have not actually analysed, and the resulting behaviour is very difficult to reproduce on the ground. Where a loop must run at a different rate from its sensors, decide explicitly whether it holds the last sample, interpolates, or skips the update.

Tuning notes: simulate before you implement, verify stability with realistic sensor noise and actuator saturation, and remember that **actuator saturation is the norm rather than the exception** on a CubeSat – a controller that is stable only when it can command unlimited torque is not stable.

## Estimation and Sensor Fusion

Individual sensors are noisy, intermittent and partially observable. Estimation combines them into a single best attitude and rate estimate.

### Deterministic methods

**TRIAD** takes two vector observations and constructs an attitude directly. Simple, non-iterative, and useful as an initial estimate or a sanity check – but it discards information (it weights one vector fully and the other partially) and cannot use more than two vectors. **Wahba's problem** generalises the question to optimally fitting N vector observations, with **QUEST** and **SVD-based** methods being the standard solutions.

### Recursive filters

- **Extended Kalman Filter (EKF)** is the workhorse. It propagates the attitude estimate using gyro measurements and corrects it when absolute observations (sun, magnetic field, stars) arrive, while simultaneously **estimating and removing gyro bias** – which is why an EKF plus a cheap MEMS gyro can outperform a much better gyro used open-loop. The **[multiplicative EKF (MEKF)](../references/glossary.md#kalman-filter)** is the standard formulation for attitude, working with a small error rotation rather than the quaternion directly, which avoids the constraint problems of filtering a unit quaternion.
- **Unscented Kalman Filter (UKF)** handles nonlinearity better without needing Jacobians, at higher computational cost.
- **Complementary filters** blend high-rate gyro data with low-rate absolute sensors using simple frequency-domain reasoning. Far cheaper than a Kalman filter, much easier to get right, and entirely adequate for missions with modest pointing requirements. Do not skip past this option just because Kalman filters are more prestigious.

### Common failure modes

- **Filter divergence** when the estimate drifts outside the region where linearisation is valid, and the filter confidently reports a wrong answer. Monitor innovation (measurement minus prediction) and reset when it stays large.
- **Over-confident covariance** – a filter that believes its own estimate too much stops accepting corrections. Inflate process noise rather than tuning for best nominal performance.
- **Eclipse transitions**, where the sun sensor drops out and the observability changes abruptly. Handle explicitly rather than letting the filter discover it.
- **Bad measurements** – albedo mistaken for the Sun, magnetorquer crosstalk, a star tracker locking onto the Moon. Gate measurements on innovation size before accepting them.

## Disturbances and Space Environment

The torques your control system spends its life fighting:

- **Gravity gradient** – arises from the inertia distribution in a non-uniform gravity field. Proportional to the difference between principal moments of inertia and falls off with the cube of orbital radius. Can be a stabilising asset (see [Passive Stabilization](#passive-stabilization-methods)) or a disturbance, depending on what you want.
- **Aerodynamic drag** – acts through the centre of pressure; if that is offset from the centre of mass, it produces a torque. Strongly altitude-dependent and varies with solar activity, which changes atmospheric density substantially over the solar cycle. This is a direct argument for keeping the centre of mass central – see [Structure – Mass Properties](structure.md#mass-properties-and-centre-of-mass).
- **Residual magnetic dipole** – your own spacecraft is a magnet, from current loops, permanent magnets in components, and magnetised materials. It interacts with the geomagnetic field to produce a persistent torque. Often the dominant disturbance on a CubeSat, and one you control by design rather than by control effort.
- **Solar radiation pressure** – photon momentum acting through the centre of pressure of illuminated area. In LEO it is small: one published analysis neglects it entirely on the grounds that it "is typically at least one order of magnitude smaller than any of the other torques."[^rawashdeh] It matters at higher altitudes and for spacecraft with large deployed areas.

In the **300–650 km** band typical of CubeSats, aerodynamic and gravity gradient torques are comparable in magnitude.[^rawashdeh] The practical implications: size actuators against the *sum* of disturbances over an orbit, not a single worst case; keep the centre of mass central and the residual dipole small, because both are far cheaper to fix in design than to fight continuously; and remember that disturbances are what saturate your reaction wheels.

<!-- CSR-RESOURCES:START dev-gnc-attitude-analysis -->
- **[Attitude Analysis of Small Satellites Using Model-Based Simulation](https://www.hindawi.com/journals/ijae/2019/3020581/)** `Link` – Open-access paper (Samir A. Rawashdeh, 2019) describing the SNAP simulation tool and modelling of gravity gradient, aerodynamic, magnetic and hysteresis torques
- **[Design and Numerical Validation of an Algorithm for the Detumbling and Angular Rate Determination of a CubeSat Using Only Three-Axis Magnetometer Data](https://onlinelibrary.wiley.com/doi/10.1155/2018/9768475)** `Link` – Open-access paper (Stefano Carletta, Paolo Teofilatto and M. Salim Farissi, 2018) on magnetometer-only detumbling with reported performance figures
<!-- CSR-RESOURCES:END dev-gnc-attitude-analysis -->

## Modes of Operation

ADCS modes are a subset of the spacecraft mode structure described in [Flight Software – Modes](flight-software.md#modes-state-machines-and-autonomy), and should be defined together with it rather than separately.

A typical progression:

1. **Detumble** – B-dot only, entered automatically at first boot and re-entered whenever body rates exceed a threshold. Must work with the minimum possible set of working hardware.
2. **Coarse sun-pointing** – magnetometer and sun sensor, magnetorquers. Gets power positive. This is usually the ADCS side of [safe mode](../references/glossary.md#safe-mode).
3. **Fine pointing** – full sensor suite and reaction wheels, for nominal operations.
4. **Slew** – transitioning between pointing targets, with rate and acceleration limits.
5. **Momentum management** – dumping accumulated wheel momentum, either continuously in the background or as a discrete mode.
6. **ADCS safe** – actuators disabled or reduced to detumble, entered on fault.

Transition rules that repay themselves: enter detumble automatically above a rate threshold; require the estimator to have converged before enabling fine pointing; time-limit every slew; and add hysteresis to every threshold. **The detumble path must be reachable and functional even if most of the ADCS is broken** – it is the mode that recovers everything else.

## Integrated ADCS Units: buy or build

A complete commercial ADCS module is an appealing option and a substantial cost. NASA's survey puts integrated units at **0.002° to 5° pointing capability** at TRL 7–9, with representative systems including Blue Canyon's XACT-15 (0.003°/0.007°, 885 g, integrating star trackers, sun sensors, IMU, magnetometer and GPS), Arcsec's Arcus (0.1°, 715 g) and CubeSpace's CubeADCS (~70 arcsec, 260 g).[^nasa-soa-gnc]

The honest trade:

- **Buy** if pointing is a hard mission requirement, if the team is small, or if schedule matters more than cost. An integrated unit removes the single most common source of CubeSat mission underperformance.
- **Build** if the mission requirement is loose (coarse sun-pointing and detumble are genuinely achievable in-house), if ADCS *is* the point of the mission, or if the budget makes a commercial unit impossible. Magnetorquers and a B-dot controller are a very reasonable in-house scope; a star-tracker-class three-axis system usually is not.
- **Hybrid** – commercial sensors with in-house control software – is common and works well, provided the interfaces are properly documented.

Whichever you choose, the integration considerations below still apply. A bought ADCS still has to be aligned, magnetically clean and correctly powered.

## ADCS Integration Considerations

- **Mechanical alignment.** Every sensor and actuator has a mounting matrix relating its frame to the body frame. Measure these rather than assuming the CAD is right; a 1° mounting error is an unremovable 1° pointing error. Alignment-critical sensors should reference machined features or dowel pins, not clearance-hole fasteners. See [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **Mass properties.** The control system needs the inertia tensor, and the disturbance environment depends on the centre of mass. Both should come from a CAD model that is kept current and, ideally, verified by measurement.
- **Magnetic cleanliness** is a whole-spacecraft requirement: twisted pairs, minimised loop areas, non-ferrous fasteners near the magnetometer, and awareness that batteries, speakers, relays and motors all contain magnets. Characterise the residual dipole before launch if you can – see [AIT – Environmental Testing](ait.md#environmental-testing).
- **Power and thermal coupling.** Detumbling and slewing are power-hungry and happen exactly when generation is worst. Reaction wheel motors and magnetorquer coils dissipate heat locally. See [EPS](eps.md) and [Thermal](thermal.md).
- **Payload and comms coupling.** Wheel jitter blurs images; the ADCS is what points a directional antenna, so a pointing failure is also a comms failure. Deployables change the inertia tensor – make sure the control system knows which configuration it is in.

## Testing and Validation

ADCS is the hardest CubeSat subsystem to test on the ground, because you cannot remove gravity and cannot reproduce the orbital magnetic field over a full orbit. The practical approach is to test the parts you can and simulate the rest.

- **Helmholtz cage.** Three orthogonal coil pairs generating a controlled, uniform magnetic field around the spacecraft. This is the core ADCS test facility: it cancels the Earth's field and replays a simulated orbital field profile, which lets you calibrate magnetometers, verify magnetorquer polarity and dipole, and run detumble algorithms against realistic input. Building one is a well-documented student project.
- **Air bearing tables** float the spacecraft on a thin air film to remove friction about one or three axes, allowing real reaction wheel control tests. Requires careful balancing, and gravity still dominates unless the centre of mass is placed precisely at the pivot.
- **Sun simulators** – a collimated light source for sun sensor calibration.
- **[HIL](../references/glossary.md#hil) simulation** is where most ADCS verification actually happens: real flight software and real processor, driven by simulated sensor data from an orbit and attitude propagator, with actuator commands fed back into the simulation. This is the only practical way to run hundreds of orbits and to test the mode logic, fault responses and edge cases. See [AIT – HIL Testing](ait.md#hardware-in-the-loop-hil-testing).
- **Polarity checks.** The single most common ADCS bug is a sign error – a magnetorquer wired backwards, a sensor axis inverted, a quaternion convention mismatch. Each one turns a controller into an accelerator. Check every axis of every sensor and actuator physically, on the integrated spacecraft, and write down the result.

### On-orbit commissioning

Commission incrementally: confirm sensor data is sane before enabling any actuator; verify detumble works; verify each actuator's polarity individually with short commanded pulses and observe the response; then enable closed-loop control. Keep a manual override and a way back to detumble at every step. Expect calibration to need refinement in orbit – magnetometer bias in particular is rarely right first time.

<!-- CSR-RESOURCES:START dev-gnc-testing-resources -->
- **[UC CubeCats Helmholtz Cage](https://uccubecats.github.io/HelmholtzCage.html)** `Link` – Student-built Helmholtz cage design and documentation
- **[Basilisk](https://avslab.github.io/basilisk/)** `Link` – Open-source astrodynamics simulation framework from the AVS Lab at CU Boulder, with spacecraft dynamics, environment models, sensor and actuator models and flight algorithm modules. A ready-made simulation half for an ADCS HIL rig ([source](https://github.com/AVSLab/basilisk))
<!-- CSR-RESOURCES:END dev-gnc-testing-resources -->

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-gnc]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 5: Guidance, Navigation and Control](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/) (revision dated 7 May 2026). Open access. Source for sensor accuracies (sun sensors 0.01–5°, magnetometers ~0.25°, star trackers 2–30 arcsec), actuator performance, integrated ADCS pointing capability, and representative vendors. Note that the chapter's summary table and its component tables do not agree at the top of the range: the summary gives 0.0005–8 Nms for reaction wheels and 0.15–15 A·m² for magnetorquers, while the component tables list the Blue Canyon RW16 at 16 Nms and the Rocket Lab TQ-40 at 48 A·m². The summary ranges are best read as describing the bulk of the market rather than its limits; where they conflict, the component tables and the manufacturers' current datasheets are the figures to trust.

[^carletta]: Stefano Carletta, Paolo Teofilatto and M. Salim Farissi, ["Design and Numerical Validation of an Algorithm for the Detumbling and Angular Rate Determination of a CubeSat Using Only Three-Axis Magnetometer Data"](https://onlinelibrary.wiley.com/doi/10.1155/2018/9768475), *International Journal of Aerospace Engineering*, 2018, Article ID 9768475. Open access. Reports rotational kinetic energy reduced by two orders of magnitude "in less than 1 orbital period, within roughly 4500 seconds" for a 3U CubeSat limited to a 0.3 A·m² dipole, with angular rate errors within ±0.2°/s.

[^rawashdeh]: Samir A. Rawashdeh, ["Attitude Analysis of Small Satellites Using Model-Based Simulation"](https://www.hindawi.com/journals/ijae/2019/3020581/), *International Journal of Aerospace Engineering*, 2019, Article ID 3020581. Open access. Describes the SNAP simulation tool and its modelling of gravity gradient, aerodynamic, magnetic and hysteresis damping torques; notes that solar radiation pressure is typically at least an order of magnitude smaller than the others in LEO, and that aerodynamic and gravitational torques are comparable in the 300–650 km band.