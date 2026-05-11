# Glossary

Key terms, acronyms, and concepts used throughout this site. Terms are linked inline wherever they first appear on a page. If you encounter an unexplained term that isn't listed here, please consider [contributing](../contributing.md).

---

## A

### ADCS
**Attitude Determination and Control System.** The subsystem responsible for measuring the spacecraft's orientation in space and applying torques to change or maintain it. Sensors (magnetometers, sun sensors, star trackers, IMUs) feed into an estimation algorithm; actuators (reaction wheels, magnetorquers) execute the resulting commands. See [GNC](../development/gnc.md).

### AIT
**Assembly, Integration and Testing.** The phase of spacecraft development in which hardware is physically assembled, subsystems are integrated together, and the combined system is tested. AIT comes after individual subsystem verification and before delivery for launch. See [AIT](../development/ait.md).

### AX.25
A data link layer protocol derived from the amateur X.25 standard, widely used in CubeSat UHF/VHF communications and compatible with amateur ground station networks such as [SatNOGS](#satnogs).

---

## B

### Beta angle
The angle between the orbital plane and the vector from the Earth to the Sun. It determines what fraction of each orbit the spacecraft spends in eclipse. At high beta angles (close to ±90°) the spacecraft can be in continuous sunlight; near 0° it experiences the longest eclipses. Beta angle changes seasonally and is a key input to both power and thermal analysis.

### BMS
**Battery Management System.** Electronics that monitor and protect a battery pack, including cell voltage balancing, temperature monitoring, and over-voltage / over-current / under-voltage cutoffs. Often integrated with or closely coupled to the EPS.

### BPSK
**Binary Phase Shift Keying.** A digital modulation scheme that encodes data by shifting the phase of a carrier signal between two values (0° and 180°). Common in CubeSat UHF downlinks for its simplicity and robustness at low SNR.

---

## C

### CDS
**CubeSat Design Specification.** The original standard document defining the physical, electrical, and operational requirements for CubeSats and their deployers. Published by California Polytechnic State University (Cal Poly) and originally co-authored with Stanford. Sets the baseline 1U dimensions (100 × 100 × 113.5 mm) and mass limit (2 kg/U) that most CubeSat hardware and deployers conform to. Latest revision: [CDS 14.1, February 2022](https://www.cubesat.org/s/CDS-REV14_1-2022-02-09.pdf).

### CDR
**Critical Design Review.** A formal milestone in the spacecraft development lifecycle, typically held after PDR, at which the design is considered mature enough to begin fabrication. At CDR the design should be fully defined, analysis complete, and risk understood. Margins are expected to have tightened from PDR levels (e.g. 20% mass margin at CDR vs. 30% at PDR).

### CONOPS
**Concept of Operations.** A document or narrative describing how a mission is intended to work end-to-end, across all phases from launch to end-of-life. Covers nominal and off-nominal scenarios, how the ground segment interacts with the spacecraft, and what the operators will do and when.

### COTS
**Commercial Off-The-Shelf.** Hardware or software purchased as a standard product rather than custom-designed for the mission. COTS components are the norm in CubeSat development — using tested, available parts reduces cost, schedule, and risk compared to building from scratch. Tradeoffs include radiation tolerance, size/power fit, and availability over the mission lifetime.

---

## D

### DoD (battery)
**Depth of Discharge.** The fraction of a battery's total capacity that has been discharged relative to its fully charged state. Cycling a lithium battery to high DoD (e.g. >80%) significantly reduces its cycle life. CubeSat designs typically target a maximum DoD of 20–30% to keep the battery healthy across thousands of orbits.

---

## E

### ECI
**Earth-Centered Inertial frame.** A coordinate frame centered at Earth's center of mass with axes that do not rotate with the Earth. The X-axis points toward the vernal equinox, Z toward the North Pole. Used to describe spacecraft position and velocity in a non-rotating frame. See [GNC](../development/gnc.md).

### ECEF
**Earth-Centered, Earth-Fixed frame.** A coordinate frame centered at Earth's center of mass that rotates with the Earth. Convenient for describing ground station locations but not inertial — spacecraft state vectors are usually expressed in ECI, not ECEF.

### Eclipse fraction
The proportion of an orbit spent in Earth's shadow and therefore receiving no solar power. Typically 30–35% for low-beta-angle LEO orbits. A key input to power budget sizing. See [EPS — Power Requirements and Budgets](../development/eps.md#power-requirements-and-budgets) and [beta angle](#beta-angle).

### EPS
**Electrical Power System.** The subsystem responsible for generating (solar panels), storing (batteries), conditioning, and distributing electrical power to all other subsystems. See [EPS](../development/eps.md).

---

## G

### GMSK
**Gaussian Minimum Shift Keying.** A continuous-phase frequency modulation scheme with a Gaussian filter applied to reduce spectral bandwidth. Used in CubeSat communications for its spectral efficiency and compatibility with amateur radio infrastructure.

### GNC
**Guidance, Navigation, and Control.** See [GNC](../development/gnc.md). Sometimes used interchangeably with [ADCS](#adcs) in the CubeSat context, though strictly GNC is broader (includes navigation and trajectory) while ADCS focuses on attitude.

### GNSS
**Global Navigation Satellite System.** Umbrella term for satellite navigation systems including GPS (US), GLONASS (Russia), Galileo (EU), and BeiDou (China). CubeSats in LEO can use GNSS receivers for onboard position and time determination, though high-altitude or fast-maneuvering spacecraft may require special receiver modes.

### Gimbal lock
A loss of one rotational degree of freedom that occurs when two of three rotation axes align, a known singularity in Euler angle representations. Avoided in flight software by using [quaternions](#quaternion) for attitude representation.

---

## H

### HDRM
**Hold-Down and Release Mechanism.** A mechanical device that keeps deployable structures (antennas, solar panels, booms) stowed during launch and releases them on command in orbit. See [Inhibits and HDRM](../development/inhibits-hdrm.md).

---

## I

### ICD
**Interface Control Document.** A document that defines the interface between two subsystems or between the spacecraft and an external system (e.g. the launch vehicle). Specifies mechanical, electrical, and data connections, pin-outs, signal levels, protocols, and environmental boundaries. ICDs are the contracts between subsystem teams.

### IMU
**Inertial Measurement Unit.** A sensor package combining accelerometers and gyroscopes to measure linear acceleration and angular velocity. Used in ADCS for short-term attitude propagation. IMUs drift over time and are typically fused with absolute sensors (magnetometers, sun sensors, star trackers) for long-term accuracy.

### ITU
**International Telecommunication Union.** The UN specialized agency that coordinates spectrum use globally. Frequency assignments for space missions require ITU notification and coordination, typically handled at the national level through regulators such as the FCC (US) or Ofcom (UK).

---

## L

### LEO
**Low Earth Orbit.** Roughly defined as orbits with altitudes between ~200 km and ~2000 km. The vast majority of CubeSats fly in LEO. Orbital periods are typically 90–120 minutes, eclipse fractions 30–35% at low beta angles, and radiation environments are relatively benign compared to higher orbits (though the South Atlantic Anomaly can be significant for some missions).

### Link budget
An accounting of all gains and losses along a communications path, from transmitter to receiver. The result is a **link margin** — how many dB of headroom exist above the minimum required SNR. Positive link margin means the link should close; the required margin depends on how much uncertainty is in the system. See [Comms — Link Budget](../development/comms.md#link-budget).

### Link margin
The difference (in dB) between the received signal level and the minimum signal level required to achieve the target bit error rate. A link margin of 0 dB means the link is exactly at threshold; margins of 3–6 dB are typical for well-designed CubeSat links.

### LVLH
**Local Vertical, Local Horizontal frame.** An orbital reference frame centered on the spacecraft, with one axis pointing toward Earth's center (local vertical) and another along the velocity vector (local horizontal). Commonly used to define attitude modes such as nadir-pointing or velocity-pointing.

---

## M

### MLI
**Multi-Layer Insulation.** Thin layers of reflective foil (typically aluminized Mylar or Kapton) separated by spacer netting, used to reduce radiative heat transfer between a spacecraft and its environment. Common in thermal control but requires careful design around conductive pathways and grounding.

### MPPT
**Maximum Power Point Tracking.** A power electronics technique that continuously adjusts the electrical operating point of a solar panel array to extract maximum available power. The maximum power point shifts with illumination intensity and temperature. MPPT is standard on most modern CubeSat EPS boards.

---

## O

### OAP
**Orbit Average Power.** The time-weighted average power consumed (or generated) over a complete orbit, accounting for different operational modes, duty cycles, and eclipse/sunlight fractions. The headline figure a power budget must balance: average generation ≥ average consumption. See [EPS — Power Requirements and Budgets](../development/eps.md#power-requirements-and-budgets).

### OBC
**On-Board Computer.** The central processing unit of the spacecraft, responsible for executing flight software, managing mode transitions, handling telecommands, collecting telemetry, and coordinating subsystem activity. See [OBC](../development/obc.md).

### Orbit

A closed (or near-closed) path followed by a spacecraft around a celestial body under the influence of gravity. For CubeSats, this almost always means an orbit around Earth. Key parameters that define an orbit include its **altitude** (how far above Earth's surface), **inclination** (the angle between the orbital plane and the equator), **eccentricity** (how circular vs. elliptical the path is), and **period** (the time to complete one revolution — typically 90–120 minutes in LEO).

The orbital parameters determine almost everything else about the mission environment: how long each pass lasts over a ground station, what fraction of each orbit is spent in eclipse, how intense the radiation environment is, how quickly the orbit decays from atmospheric drag, and what beta angle the spacecraft sees at different times of year. See [LEO](#leo), [beta angle](#beta-angle), [eclipse fraction](#eclipse-fraction), and [TLE](#tle).

---

## P

### PDR
**Preliminary Design Review.** A formal milestone in the spacecraft development lifecycle, typically held after concept design when the architecture is established and preliminary analysis exists but detailed design is not yet complete. At PDR the design should be feasible and requirements-compliant, with conservative margins (e.g. 30% on mass, power). CDR follows once the design matures.

---

## Q

### Quaternion
A four-element mathematical representation of orientation in 3D space, widely used in spacecraft ADCS for its numerical stability and freedom from the [gimbal lock](#gimbal-lock) singularities that affect Euler angles. A unit quaternion q = [q₀, q₁, q₂, q₃] encodes a rotation axis and angle in a form convenient for onboard computation.

---

## R

### Reaction wheel
A spinning flywheel used as an attitude actuator. By accelerating or decelerating the wheel, angular momentum is exchanged with the spacecraft body, producing a controlled torque without expelling propellant. Reaction wheels can become saturated (spin at their maximum rate) and must be periodically desaturated using magnetorquers or thrusters.

---

## S

### SatNOGS
**Satellite Networked Open Ground Station.** An open-source, community-driven global network of ground stations that receive and share satellite signals, including CubeSat beacons. Operated by the Libre Space Foundation. A de facto standard for beacon reception in academic and open-source missions. [satnogs.org](https://satnogs.org/).

### SNR
**Signal-to-Noise Ratio.** The ratio of signal power to noise power at a receiver input, usually expressed in dB. A key figure in link budget analysis — the received SNR must exceed the minimum required for the chosen modulation and coding scheme.

---

## T

### TLE
**Two-Line Element set.** A standardized format for encoding a satellite's orbital parameters at a given epoch, used as input to propagators such as SGP4. TLEs are published by the US Space Surveillance Network (via Space-Track) and used widely for tracking and pass prediction. See [GNC — Orbit Representation / TLEs](../development/gnc.md#orbit-representation--tles).

### TRL
**Technology Readiness Level.** A scale from 1 to 9 used to assess the maturity of a technology, from basic principles (TRL 1) through lab demonstration (TRL 4–5), relevant environment testing (TRL 6–7), to flight-proven (TRL 9). Originally developed by NASA. Commonly used in CubeSat procurement and mission risk assessment.

### TT&C
**Telemetry, Tracking, and Command.** The fundamental communication function between a spacecraft and its ground segment. Telemetry is housekeeping data downlinked from the spacecraft; tracking determines its position and velocity; command is the uplink of instructions. See [Comms](../development/comms.md).

---

## U

### U (CubeSat unit)
The standard size increment in the CubeSat form factor system. 1U is defined as 100 × 100 × 113.5 mm with a mass limit of 2 kg. Larger form factors (1.5U, 2U, 3U, 6U, 12U, 16U…) scale linearly in one or more dimensions. Defined in the [CDS](#cds).

### UHF / VHF
**Ultra-High Frequency / Very High Frequency.** Radio frequency bands commonly used in CubeSat communications. VHF covers 30–300 MHz (uplinks often around 145–146 MHz); UHF covers 300 MHz–3 GHz (downlinks often around 437 MHz). Both bands are popular with amateur missions due to favorable propagation, lower required transmit power, and the availability of the [SatNOGS](#satnogs) network.

---

## V

### V&V
**Verification and Validation.** Two complementary processes. *Verification* confirms that the system was built correctly (meets requirements, as demonstrated by test, analysis, inspection, or similarity). *Validation* confirms that the right system was built (meets the mission need). See [Systems Engineering](../development/systems-engineering.md).

---

*This glossary is community-maintained. To add or correct an entry, see the [contributing guide](../contributing.md).*
