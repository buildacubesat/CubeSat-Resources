# Glossary

Key terms, acronyms, and concepts used throughout this site. Terms are linked inline wherever they first appear on a page. If you encounter an unexplained term that isn't listed here, please consider [contributing](../contributing.md).

---

## A

### Absorptivity (α)
The fraction of incident solar radiation a surface absorbs rather than reflects. Together with [emissivity](#emissivity) it determines a surface's equilibrium temperature in sunlight: the ratio **α/ε** is the single most useful number in passive thermal design. Low α/ε surfaces (white paint, silver FEP tape) run cold and make good radiators; high α/ε surfaces (bare or polished metal) run hot. Solar absorptivity generally increases over a mission as coatings are degraded by UV and atomic oxygen. See [Thermal](../development/thermal.md#surface-finishes-and-coatings).

### Acceptance testing
Environmental testing performed on each flight article to demonstrate that it is free of workmanship defects, conducted at the levels expected in service rather than above them – typically maximum expected random vibration spectrum with no added margin, for one minute per axis. Contrast [qualification testing](#qualification-testing), which proves the *design* has margin, and [protoflight](#protoflight) testing, which combines both on a single article.

### ADCS
**Attitude Determination and Control System.** The subsystem responsible for measuring the spacecraft's orientation in space and applying torques to change or maintain it. Sensors (magnetometers, sun sensors, star trackers, IMUs) feed into an estimation algorithm; actuators (reaction wheels, magnetorquers) execute the resulting commands. See [GNC](../development/gnc.md).

### AIT
**Assembly, Integration and Testing.** The phase of spacecraft development in which hardware is physically assembled, subsystems are integrated together, and the combined system is tested. AIT comes after individual subsystem verification and before delivery for launch. See [AIT](../development/ait.md).

### AFSK
**Audio Frequency Shift Keying.** A simple modulation scheme in which digital data is encoded as audio tones that then modulate an FM carrier. Its virtue is that it works through any ordinary FM radio, which is why it is common on low-rate CubeSat beacons intended to be receivable by as many amateur stations as possible. Spectrally inefficient compared with [BPSK](#bpsk) or [GMSK](#gmsk).

### Apogee / Perigee
The highest and lowest points of an orbit relative to the body being orbited – apogee farthest from Earth, perigee closest. In a circular orbit the two coincide. For CubeSats the relevant consequence is usually orbital lifetime: perigee altitude governs how much atmospheric drag the spacecraft experiences and therefore how quickly the orbit decays.

### Albedo
Sunlight reflected from a planet's surface and atmosphere back into space, and one of the three environmental heat inputs to a spacecraft in orbit. Modelled as a fraction of the [solar constant](#solar-constant); spacecraft thermal analysis conventionally uses an albedo factor of 0.30 nominal, 0.25 cold case and 0.35 hot case, though instantaneous values range from roughly 0.06 over ocean to 0.50 over cloud and ice. See [Thermal](../development/thermal.md#thermal-environment-in-orbit).

### AX.25
A data link layer protocol derived from the amateur X.25 standard, widely used in CubeSat UHF/VHF communications and compatible with amateur ground station networks such as [SatNOGS](#satnogs).

---

## B

### B-dot
The standard magnetic detumbling control law. It commands a magnetic dipole opposing the measured rate of change of the geomagnetic field in the body frame (in its common form **m = −k·Ḃ**), extracting rotational energy from the spacecraft. Its great virtue is that it needs only a magnetometer and magnetorquers – no attitude knowledge, no rate gyro, no orbit knowledge – which makes it the first thing that can run after deployment. See [GNC – Control Algorithms](../development/gnc.md#detumbling-and-b-dot).

### Baseline
A formally agreed, frozen snapshot of a design – requirements, drawings, interfaces, software versions – captured at a project milestone such as [PDR](#pdr) or [CDR](#cdr). Subsequent changes are made against the baseline and recorded, which is what makes it possible to say later what the spacecraft actually was at any point. Without baselines, test results cannot be reliably interpreted because nothing pins down what was tested.

### Beta angle
The angle between the orbital plane and the vector from the Earth to the Sun. It determines what fraction of each orbit the spacecraft spends in eclipse. At high beta angles (close to ±90°) the spacecraft can be in continuous sunlight; near 0° it experiences the longest eclipses. Beta angle changes seasonally and is a key input to both power and thermal analysis.

### BOL / EOL
**Beginning of Life / End of Life.** The two bounding conditions a spacecraft subsystem is sized against. Solar arrays are the classic case: cell efficiency falls over the mission from radiation damage and coverglass darkening, so an array sized to close the [power budget](../development/eps.md#power-requirements-and-budgets) at BOL will not close it at EOL. Always size generation for EOL and check that BOL does not overcharge anything.

### Beacon
A short, low-rate, periodic transmission carrying basic health data – battery voltage, temperature, mode, an identifier. Deliberately designed to be receivable with minimal equipment, so that the spacecraft can be confirmed alive without a full pass. Publishing your beacon format and a decoder turns every [SatNOGS](#satnogs) station on Earth into a receiving station for your mission; many CubeSats have been first detected, and some diagnosed, entirely from beacons received by strangers.

### BMS
**Battery Management System.** Electronics that monitor and protect a battery pack, including cell voltage balancing, temperature monitoring, and over-voltage / over-current / under-voltage cutoffs. Often integrated with or closely coupled to the EPS.

### BPSK
**Binary Phase Shift Keying.** A digital modulation scheme that encodes data by shifting the phase of a carrier signal between two values (0° and 180°). Common in CubeSat UHF downlinks for its simplicity and robustness at low SNR.

---

## C

### Burn wire
The most common CubeSat release mechanism: a synthetic line (Dyneema, Vectran or similar) under tension restrains a stowed deployable, and a resistive heater pressed against it melts or severs the line on command, letting springs deploy the structure. Cheap, light and easy to test many times. The critical caveat is that with no convection in vacuum the heater runs far hotter for the same power, so burn times measured in air are not valid – always characterise in vacuum. NASA's CubeSat 101 recommends two separate burn wires for redundancy.

### Bus (spacecraft)
Everything on a spacecraft that is not the [payload](../development/payload.md) – structure, power, avionics, communications, attitude control, thermal. The bus exists to keep the payload alive, powered, pointed and connected. Note the collision with the other engineering sense of "bus" (a shared electrical or data connection, as in an I²C bus); context normally disambiguates.

### C-rate
A normalised measure of battery charge or discharge current, expressed relative to capacity. 1C discharges the full nominal capacity in one hour; 0.5C takes two hours; 2C takes thirty minutes. Cell datasheets specify maximum charge and discharge C-rates, and cycle life degrades as they are approached. Most CubeSat batteries operate well below 1C, which is one reason they last.

### CDS
**CubeSat Design Specification.** The original standard document defining the physical, electrical, and operational requirements for CubeSats and their deployers. Published by California Polytechnic State University (Cal Poly) and originally co-authored with Stanford. Sets the baseline 1U dimensions (100 × 100 × 113.5 mm) and mass limit (2 kg/U) that most CubeSat hardware and deployers conform to. Latest revision: [CDS 14.1, February 2022](https://www.cubesat.org/s/CDS-REV14_1-2022-02-09.pdf).

### CCSDS
**Consultative Committee for Space Data Systems.** The international body that publishes the standards governing how spacecraft and ground systems exchange data – packet structures, space data link protocols, file delivery, time codes and more. Its "Blue Book" recommended standards are freely available at [ccsds.org](https://ccsds.org/publications/bluebooks/). Adopting CCSDS formats costs a little overhead and buys interoperability with existing ground software and third-party ground stations.

### CDR
**Critical Design Review.** A formal milestone in the spacecraft development lifecycle, typically held after PDR, at which the design is considered mature enough to begin fabrication. At CDR the design should be fully defined, analysis complete, and risk understood. Margins are expected to have tightened from PDR levels (e.g. 20% mass margin at CDR vs. 30% at PDR).

### Cold welding
The spontaneous bonding of two clean metal surfaces pressed together in vacuum. On Earth a thin oxide and adsorbed gas layer keeps metal surfaces apart; in vacuum that layer is absent and the surfaces can fuse. This is why the [CDS](#cds) requires aluminium CubeSat surfaces in contact with the dispenser rails to be hard anodised – a cold-welded CubeSat cannot leave its [deployer](#deployer). See [Structure](../development/structure.md#materials-and-manufacturing).

### Commissioning
The phase immediately after [LEOP](#leop) in which each subsystem is switched on, checked out and calibrated in turn before the mission enters routine operations. Deliberately incremental: sensors verified before actuators are enabled, each actuator's polarity confirmed individually, payload characterised against its ground calibration. Rushing commissioning is how teams turn a recoverable anomaly into a lost mission.

### CONOPS
**Concept of Operations.** A document or narrative describing how a mission is intended to work end-to-end, across all phases from launch to end-of-life. Covers nominal and off-nominal scenarios, how the ground segment interacts with the spacecraft, and what the operators will do and when.

### CSP
**Cubesat Space Protocol.** A small, MIT-licensed network-layer protocol stack written in C for communication between subsystems on a small spacecraft. Modelled on TCP/IP, with a lightweight header carrying both transport and network information, and drivers for CAN, UDP, USART and ZMQ. Originating at Aalborg University and GomSpace, it is the closest thing the CubeSat world has to a standard onboard middleware. See [Flight Software](../development/flight-software.md#inter-subsystem-communication-protocols).

### COCOM limits
Restrictions requiring commercial GNSS receivers to stop reporting a position above roughly 18 km altitude and 1,900 km/h, originally intended to prevent their use in guided missiles. Space-capable receivers have these limits removed or reconfigured, which is precisely what places them under dual-use export control regimes such as the Wassenaar Arrangement and, in the US, ITAR/EAR. A procurement lead-time risk worth identifying early.

### COTS
**Commercial Off-The-Shelf.** Hardware or software purchased as a standard product rather than custom-designed for the mission. COTS components are the norm in CubeSat development –  using tested, available parts reduces cost, schedule, and risk compared to building from scratch. Tradeoffs include radiation tolerance, size/power fit, and availability over the mission lifetime.

---

## D

### Deployer
Also **dispenser** or **pod**. The spring-loaded container that holds one or more CubeSats during launch and ejects them once on orbit. The deployer defines the mechanical envelope the CubeSat must fit, provides the rails it slides along, and actuates the deployment switches that tell the spacecraft it is free. Common families include the Cal Poly [P-POD](#p-pod), ISISPACE's ISIPOD, Exolaunch's EXOpod, and the ISS-based J-SSOD and NanoRacks deployers. The deployer's user manual takes precedence over the [CDS](#cds) wherever the two disagree. See [Structure](../development/structure.md#form-factors-and-the-cubesat-envelope).

### Delta-v
The change in velocity a spacecraft can achieve with its propulsion system, in m/s – the standard currency of orbital manoeuvring, since it maps directly onto what manoeuvres are possible. Most CubeSats have no propulsion and therefore no delta-v budget at all; those that do use it for orbit raising, phasing, collision avoidance or controlled deorbit.

### Deorbit
Removing a spacecraft from orbit at end of life, either passively (letting atmospheric drag decay the orbit) or actively (propulsion, a drag sail or another deorbit device). Increasingly a regulatory requirement rather than good practice: the [FCC](#fcc)'s 5-year rule requires disposal within five years of mission completion for satellites under its jurisdiction, against a long-standing 25-year international guideline. Below roughly 500 km natural decay usually suffices; above about 600 km a passive CubeSat may need help.

### Derating
Deliberately operating a component below its maximum rated voltage, current, power or temperature, to increase reliability and margin. Standard practice in spacecraft design, and particularly important when flying [COTS](#cots) parts whose ratings assume a benign terrestrial environment and a short life.

### Downlink / Uplink
**Downlink** is the direction from spacecraft to ground – telemetry, beacons and payload data. **Uplink** is ground to spacecraft – commands and software updates. The two are strongly asymmetric on a CubeSat: the ground transmitter can be far more powerful than the spacecraft's, so uplink usually closes more easily, while downlink capacity is the binding constraint on how much data a mission can return.

### Detumbling
Reducing the spacecraft's body rotation rates after deployment, when it typically emerges from the [deployer](#deployer) tumbling at a few degrees per second. Nothing else works until this is done: solar generation is poor, star trackers cannot lock, and communications are intermittent. Almost always performed by a [B-dot](#b-dot) controller driving magnetorquers, autonomously and without ground intervention.

### Deployment switch
A switch held actuated by the [deployer](#deployer) walls while the CubeSat is stowed, which releases on ejection and thereby tells the spacecraft it is in orbit. The [CDS](#cds) requires at least one, requires it to electrically disconnect the power system from powered functions while actuated, and requires that if it toggles and returns, the satellite resets to a pre-launch state including its transmission and deployable timers. Also the T-zero for the mandated quiet periods. See [Inhibits and HDRM](../development/inhibits-hdrm.md#deployment-switches-and-separation-detection).

### Doppler shift
The change in received frequency caused by relative motion between spacecraft and ground station. A LEO satellite closes and opens range fast enough to shift a 437 MHz carrier by roughly ±10 kHz across a pass, sweeping through zero at closest approach – where the rate of change is greatest, precisely when the signal is strongest. Correction is required on the downlink and, just as importantly, **pre-compensation is required on the uplink**; forgetting the latter is a classic reason a spacecraft that is being heard perfectly will not accept commands.

### DoD (battery)
**Depth of Discharge.** The fraction of a battery's total capacity that has been discharged relative to its fully charged state. Cycling a lithium battery to high DoD (e.g. >80%) significantly reduces its cycle life. CubeSat designs typically target a maximum DoD of 20–30% to keep the battery healthy across thousands of orbits.

---

## E

### DITL
**Day-In-The-Life testing.** A full rehearsal in which the integrated spacecraft is run through a realistic 24-hour operational timeline – eclipse cycles, ground station passes, payload operations, housekeeping – with the real ground segment on the other end. Routinely finds problems no other test does, because it is the first time every element runs together at realistic timescales. See [AIT – Mission Simulation](../development/ait.md#mission-simulation).

### Duty cycle
The fraction of time a component is actively operating. Central to CubeSat design because very few payloads or transmitters can run continuously on the available power: average power equals peak power times duty cycle, so the duty cycle the [power budget](../development/eps.md#power-requirements-and-budgets) permits is a hard mission parameter determining how much data can be collected at all. Note that peak draw still matters independently – a load that is fine on average can still brown out the bus.

### ECI
**Earth-Centered Inertial frame.** A coordinate frame centered at Earth's center of mass with axes that do not rotate with the Earth. The X-axis points toward the vernal equinox, Z toward the North Pole. Used to describe spacecraft position and velocity in a non-rotating frame. See [GNC](../development/gnc.md).

### ECEF
**Earth-Centered, Earth-Fixed frame.** A coordinate frame centered at Earth's center of mass that rotates with the Earth. Convenient for describing ground station locations but not inertial –  spacecraft state vectors are usually expressed in ECI, not ECEF.

### Earth IR
Also **outgoing longwave radiation (OLR)**. The infrared energy radiated by the Earth itself, which a spacecraft in orbit intercepts as a heat input. Modelled as a roughly 255 K blackbody giving about 241 W/m², with thermal analysis values typically spanning 214–267 W/m². Unlike [albedo](#albedo), Earth IR continues during eclipse, and is therefore what keeps the cold case from being colder than it is.

### Eclipse fraction
The proportion of an orbit spent in Earth's shadow and therefore receiving no solar power. Typically 30–35% for low-beta-angle LEO orbits. A key input to power budget sizing. See [EPS –  Power Requirements and Budgets](../development/eps.md#power-requirements-and-budgets) and [beta angle](#beta-angle).

### Engineering model
A functionally equivalent, non-flight copy of the spacecraft or a subsystem, used for software development, procedure rehearsal, destructive testing and troubleshooting. Frequently the single best investment a CubeSat team can make: it unblocks software work from hardware availability, and it means every procedure has been rehearsed before it touches the flight article. Distinct from a [flatsat](#flatsat), which is a bench layout rather than a built spacecraft.

### Ephemeris
A table or model giving a spacecraft's position and velocity as a function of time. On a CubeSat it is usually not stored as a table but generated onboard by propagating a [TLE](#tle) with [SGP4](#sgp4), or taken directly from a [GNSS](#gnss) receiver. Needed by anything that has to know where the spacecraft is: attitude determination, pointing, payload scheduling and pass planning.

### Epoch
The reference instant at which a set of orbital elements or a state vector is valid. Orbit predictions degrade with time since epoch – a [TLE](#tle) is accurate to roughly a kilometre near its epoch and tens of kilometres a week or two later – which is why operational tracking requires regularly refreshed element sets.

### EGSE
**Electrical Ground Support Equipment.** The bench-side hardware and software used to power, command and monitor a spacecraft during assembly and test: supplies, umbilicals, breakout boards, RF loopback paths and the test console. Best built around the same command-and-telemetry software that will be used for flight operations, so the operations tooling is exercised throughout the [AIT](../development/ait.md) campaign rather than written at the end.

### Emissivity (ε)
The efficiency with which a surface radiates heat in the infrared, relative to a perfect blackbody (ε = 1). High emissivity is what makes a radiator work. Paired with [absorptivity](#absorptivity) as the α/ε ratio that governs equilibrium temperature. Note that α is measured in the solar spectrum and ε in the infrared, which is why a surface can be highly reflective to sunlight and highly emissive in the IR at the same time.

### EDAC
**Error Detection And Correction.** Memory protection that appends check bits to each stored word so that single-bit errors can be corrected and double-bit errors detected. Standard mitigation against [single-event upsets](#seu) in spacecraft memory, usually paired with [scrubbing](#scrubbing) so errors are corrected before a second upset makes them uncorrectable.

### EPS
**Electrical Power System.** The subsystem responsible for generating (solar panels), storing (batteries), conditioning, and distributing electrical power to all other subsystems. See [EPS](../development/eps.md).

---

## F

### Finite element analysis (FEA)
A numerical method for predicting how a structure responds to loads, by subdividing it into many small elements and solving the resulting system of equations. Used on CubeSats mainly for modal analysis (finding natural frequencies) and for demonstrating positive [margin of safety](#margin-of-safety) under launch loads. Also referred to as FEM (finite element method/modelling). See [Structure – Structural Analysis and FEM](../development/structure.md#structural-analysis-and-fem).

### Flight heritage
Evidence that a component or design has already operated successfully in space. Heritage reduces perceived risk and is a major factor in [COTS](#cots) component selection, but it is specific: heritage applies to a particular configuration, in a particular orbit, for a particular duration. A part with heritage in [LEO](#leo) for six months tells you little about a three-year mission at a different altitude.

---

## G

### G/T
**Gain-to-noise-temperature ratio**, in dB/K. The standard figure of merit for a receiving station, combining antenna gain and system noise temperature into a single number that can be dropped straight into a [link budget](#link-budget). Higher is better. Representative values for commercial ground networks range from about 11 dB/K for small S-band apertures to 37 dB/K for large X-band dishes.

### GSaaS
**Ground-Station-as-a-Service.** Commercial ground network capacity sold per pass or per minute, rather than built and operated by the mission. Providers include KSAT, ATLAS, Leaf Space, SSC and AWS Ground Station. Attractive for missions needing S-band or above, where building comparable capability is expensive, and for short missions where capital cost cannot be amortised. Generally does not serve amateur UHF/VHF bands. See [Ground Segment](../development/ground-segment.md#ground-station-architectures).

### GEVS
**General Environmental Verification Standard**, NASA document GSFC-STD-7000. Defines generalised environmental test levels and verification requirements for spacecraft hardware – random vibration, shock, thermal vacuum, EMC and more. Widely used as the default qualification envelope by CubeSat teams that do not yet know their launch vehicle. The component-level random vibration qualification level is 14.1 Grms; acceptance levels sit 3 dB lower in PSD (≈10 Grms). See [Structure](../development/structure.md#structural-analysis-and-fem) and [AIT](../development/ait.md#environmental-testing).

### GMSK
**Gaussian Minimum Shift Keying.** A continuous-phase frequency modulation scheme with a Gaussian filter applied to reduce spectral bandwidth. Used in CubeSat communications for its spectral efficiency and compatibility with amateur radio infrastructure.

### GNC
**Guidance, Navigation, and Control.** See [GNC](../development/gnc.md). Sometimes used interchangeably with [ADCS](#adcs) in the CubeSat context, though strictly GNC is broader (includes navigation and trajectory) while ADCS focuses on attitude.

### GNSS
**Global Navigation Satellite System.** Umbrella term for satellite navigation systems including GPS (US), GLONASS (Russia), Galileo (EU), and BeiDou (China). CubeSats in LEO can use GNSS receivers for onboard position and time determination, though high-altitude or fast-maneuvering spacecraft may require special receiver modes.

### FDIR
**Fault Detection, Isolation and Recovery.** The onboard machinery that notices something has gone wrong, works out which element is responsible, and takes action to restore a working state – without waiting for a ground contact that may be hours away. Usually built as an escalation ladder from retry, through subsystem reset and power cycle, to [safe mode](#safe-mode) and full spacecraft reset. See [Flight Software](../development/flight-software.md#fault-detection-isolation-and-recovery-fdir).

### ESPA ring
**EELV Secondary Payload Adapter.** A ring-shaped structural adapter mounted between a launch vehicle's upper stage and its primary payload, carrying secondary payloads on ports around its circumference – six 38 cm ports each supporting up to 257 kg in the standard configuration, with larger ESPA Grande variants. The standard way spacecraft above CubeSat scale fly as secondary payloads; CubeSat dispensers are often themselves mounted on an ESPA port.

### FCC
**Federal Communications Commission.** The United States regulator for radio spectrum, including satellite communications. Relevant well beyond the US because a great many missions are licensed by or communicate through the US, which brings them under FCC rules – notably its orbital debris requirements. Its counterparts elsewhere include Ofcom (UK), BNetzA (Germany) and OFCOM (Switzerland).

### FEC
**Forward Error Correction.** Adding structured redundancy to transmitted data so the receiver can detect and correct errors without asking for a retransmission – essential when the round trip is a satellite pass. Convolutional, Reed-Solomon, LDPC and turbo codes are common, often concatenated. The resulting coding gain of several dB is frequently the difference between a link that closes and one that does not.

### Flatsat
A spacecraft's full electronics set laid out flat on a bench, wired as flown but fully accessible for probing, reprogramming and fault injection. The primary integration and software development environment for most CubeSat teams, used long before and long after the flight hardware is assembled. See [AIT](../development/ait.md#flatsat-and-integration-test-setups).

### Gravity gradient stabilisation
A passive attitude stabilisation technique exploiting the torque that a gravity field exerts on an elongated body, tending to align its long axis with the local vertical. Requires no power and no actuators, typically achieves a few degrees of nadir pointing, provides no yaw control, and is bistable – the spacecraft will settle happily either way up. Often enhanced with a deployed boom and tip mass, and usually paired with magnetic hysteresis damping.

### Ground track
The path traced on the Earth's surface directly beneath a spacecraft's orbit. Because the Earth rotates underneath, successive orbits shift westward, which is what determines revisit times over a target and how often a given ground station gets a pass.

### Gimbal lock
A loss of one rotational degree of freedom that occurs when two of three rotation axes align, a known singularity in Euler angle representations. Avoided in flight software by using [quaternions](#quaternion) for attitude representation.

### Grms
**Root-mean-square acceleration**, in units of g. A single number summarising the overall energy of a [random vibration](#random-vibration) environment, obtained by integrating the acceleration power spectral density across the test frequency band and taking the square root. Useful for comparing environments at a glance, but it says nothing about *where* in frequency the energy sits – two very different PSDs can share a Grms value.

---

## H

### Heat pipe
A sealed passive device that transports heat with a very high effective thermal conductivity, using a working fluid that evaporates at the hot end, travels as vapour to the cold end, condenses, and returns via a capillary wick. Standard on larger spacecraft; flat-plate and conformable micro variants have been demonstrated on 6U CubeSats. No moving parts and no power required, but orientation-sensitive during ground testing.

### Hot case / cold case
The two bounding thermal scenarios a spacecraft design is analysed against. The **hot case** combines maximum solar flux, high [albedo](#albedo) and [Earth IR](#earth-ir), worst-case attitude, maximum internal dissipation and degraded (end-of-life) surface properties. The **cold case** combines minimum environmental inputs, maximum eclipse and minimum internal dissipation – typically safe mode, when the spacecraft has shed exactly the loads whose waste heat it needs. See [Thermal](../development/thermal.md#hot-case-and-cold-case).

### Golden image
A minimal, known-good software image held in write-protected memory that can never be overwritten in flight. It does not need to be capable of running the mission – only of booting, charging the battery, and listening for commands – so that a corrupted or faulty software update is always recoverable. Usually paired with a boot counter that falls back to the golden image automatically after repeated failed boots. See [Flight Software](../development/flight-software.md#bootloaders-and-the-golden-image).

### HDRM
**Hold-Down and Release Mechanism.** A mechanical device that keeps deployable structures (antennas, solar panels, booms) stowed during launch and releases them on command in orbit. See [Inhibits and HDRM](../development/inhibits-hdrm.md).

---

## I

### Harness
The wiring assembly connecting a spacecraft's subsystems – wires, connectors, shielding, strain relief and labelling. A disproportionate source of integration problems, largely because it is often improvised rather than designed. A harness that accreted during integration cannot be verified or rebuilt identically; one that was drawn, documented and built to a schedule can be.

### HAL
**Hardware Abstraction Layer.** The software layer that isolates all register-level hardware access behind interfaces, so application logic never touches hardware directly. Beyond portability, its real value is testability: application code written against a HAL can be compiled and run on a development machine against simulated hardware, turning bugs that would otherwise surface slowly on a [flatsat](#flatsat) into ones caught by an automated test suite.

### HIL
**Hardware-In-the-Loop.** A test configuration in which real flight hardware runs against a simulated environment – synthetic sensor data, modelled orbital dynamics and actuator responses – so that control loops and mode logic can be exercised across many orbits without leaving the lab. See [AIT](../development/ait.md#hardware-in-the-loop-hil-testing).

### Hyperspectral imaging
Imaging in hundreds of contiguous, narrow spectral bands, producing a full spectrum for every pixel rather than a few discrete colour channels. Scientifically rich and a severe data-volume problem for a small spacecraft: a single scene can exceed a CubeSat's entire daily downlink capacity, which is why onboard filtering and standards such as CCSDS 123.0-B-2 matter. Contrast **multispectral** imaging, which uses a handful of bands chosen for a specific application.

### IARU
**International Amateur Radio Union.** The body that coordinates amateur satellite frequency use, reviewing proposed missions to avoid interference with existing satellites and issuing a coordinated frequency assignment. The process is free and well documented but takes months, and passing through it is expected practice for any CubeSat using amateur bands. Distinct from, and usually a precursor to, national licensing and [ITU](#itu) notification.

### Inclination
The angle between an orbital plane and the Earth's equator, in degrees. It determines the range of latitudes the spacecraft passes over: a 0° orbit stays over the equator, a 51.6° orbit (the ISS inclination, and therefore that of ISS-deployed CubeSats) reaches ±51.6°, and a polar or [sun-synchronous](#sso) orbit near 98° covers the whole planet. Inclination is set by the launch and is expensive to change.

### ICD
**Interface Control Document.** A document that defines the interface between two subsystems or between the spacecraft and an external system (e.g. the launch vehicle). Specifies mechanical, electrical, and data connections, pin-outs, signal levels, protocols, and environmental boundaries. ICDs are the contracts between subsystem teams.

### IMU
**Inertial Measurement Unit.** A sensor package combining accelerometers and gyroscopes to measure linear acceleration and angular velocity. Used in ADCS for short-term attitude propagation. IMUs drift over time and are typically fused with absolute sensors (magnetometers, sun sensors, star trackers) for long-term accuracy.

### Inhibit
A physical device interrupting the power path between an energy source and a hazard, preventing that hazard from occurring. The [CDS](#cds) requires at least three independent inhibits against inadvertent RF transmission and three against inadvertent deployable release. Crucially, **a timer does not count as an inhibit** – software delays are separately required but do not contribute to the count. Independence is what reviewers check: three switches driven by one mechanism are one inhibit. See [Inhibits and HDRM](../development/inhibits-hdrm.md#what-counts-as-an-inhibit).

### ITU
**International Telecommunication Union.** The UN specialized agency that coordinates spectrum use globally. Frequency assignments for space missions require ITU notification and coordination, typically handled at the national level through regulators such as the FCC (US) or Ofcom (UK).

---

## L

### Kalman filter
A recursive estimator that combines a dynamic model with noisy measurements to produce a best estimate of a system's state, together with an estimate of its own uncertainty. In spacecraft attitude determination the standard variant is the **multiplicative extended Kalman filter (MEKF)**, which propagates attitude using gyro data, corrects it when absolute observations (sun, magnetic field, stars) arrive, and simultaneously estimates gyro bias – which is why a good filter with a cheap MEMS gyro outperforms an expensive gyro used open-loop.

### LCL
**Latching Current Limiter.** A protected power switch that limits output current to a set value for a defined period and then latches off, staying off until explicitly commanded to reset. The standard spacecraft approach to fault containment on a distributed power bus: it isolates a faulty load without the one-shot permanence of a fuse. See [EPS – Power Switching and Protection](../development/eps.md#power-switching-and-protection).

### LNA
**Low-Noise Amplifier.** The first amplifier in a receive chain, whose noise figure dominates the noise performance of the whole system. Mounting it at the antenna, ahead of the feedline, is the single highest-value improvement to a marginal ground station: feedline loss before the LNA adds directly to system noise figure, while the same loss after it is nearly irrelevant.

### LEO
**Low Earth Orbit.** Roughly defined as orbits with altitudes between ~200 km and ~2000 km. The vast majority of CubeSats fly in LEO. Orbital periods are typically 90–120 minutes, eclipse fractions 30–35% at low beta angles, and radiation environments are relatively benign compared to higher orbits (though the South Atlantic Anomaly can be significant for some missions).

### LEOP
**Launch and Early Orbit Phase.** The period immediately after deployment, covering first acquisition of signal, detumbling, initial health assessment and establishing routine contact. The highest-workload and highest-risk phase of a CubeSat mission, and the one where automation is least useful and rehearsal most valuable. Complicated for rideshare CubeSats by the fact that the spacecraft may not yet be individually identified in the catalogue.

### Link budget
An accounting of all gains and losses along a communications path, from transmitter to receiver. The result is a **link margin** –  how many dB of headroom exist above the minimum required SNR. Positive link margin means the link should close; the required margin depends on how much uncertainty is in the system. See [Comms –  Link Budget](../development/comms.md#link-budget).

### Link margin
The difference (in dB) between the received signal level and the minimum signal level required to achieve the target bit error rate. A link margin of 0 dB means the link is exactly at threshold; margins of 3–6 dB are typical for well-designed CubeSat links.

### LVLH
**Local Vertical, Local Horizontal frame.** An orbital reference frame centered on the spacecraft, with one axis pointing toward Earth's center (local vertical) and another along the velocity vector (local horizontal). Commonly used to define attitude modes such as nadir-pointing or velocity-pointing.

---

## M

### Margin of safety
A normalised measure of how much structural capability remains beyond what the applied load requires: **MS = allowable / (factor of safety × applied) − 1**. A margin of safety must be positive; zero means the structure is exactly at its limit with no headroom. Reported separately against yield and ultimate allowables. Distinct from the [margins](../development/systems-engineering.md#budgets-and-margins) tracked in mass and power budgets, which are bookkeeping reserves rather than structural quantities.

### Magnetorquer
An attitude actuator that generates torque by producing a magnetic dipole which interacts with the Earth's magnetic field, following **τ = m × B**. Simple, robust, power-efficient and with no moving parts or consumables. The cross product means no torque can be produced about the field direction, so magnetorquers are underactuated at any instant and rely on the field direction changing around the orbit – which makes magnetic-only control slow but workable. Implemented as air-core coils, rods wound on a ferromagnetic core, or traces embedded in a PCB. See [GNC](../development/gnc.md#magnetorquers).

### MLI
**Multi-Layer Insulation.** Thin layers of reflective foil (typically aluminized Mylar or Kapton) separated by spacer netting, used to reduce radiative heat transfer between a spacecraft and its environment. Common in thermal control but requires careful design around conductive pathways and grounding.

### Momentum desaturation
Also **momentum dumping**. The process of removing accumulated angular momentum from [reaction wheels](#reaction-wheel) by exerting an external torque on the spacecraft – on a CubeSat, using [magnetorquers](#magnetorquer) against the Earth's magnetic field. Necessary because persistent disturbance torques continuously spin the wheels up; once a wheel saturates it can produce no further torque and control authority about that axis is lost. A reaction wheel system without a working desaturation path will eventually stop working.

### MPPT
**Maximum Power Point Tracking.** A power electronics technique that continuously adjusts the electrical operating point of a solar panel array to extract maximum available power. The maximum power point shifts with illumination intensity and temperature. MPPT is standard on most modern CubeSat EPS boards.

---

## O

### Nanosatellite
A satellite with a mass between roughly 1 and 10 kg. Most CubeSats from 1U to 6U fall in this class. Neighbouring classes are picosatellites (0.1–1 kg, including [PocketQubes](#pocketqube)), microsatellites (10–100 kg) and minisatellites (100–500 kg), though the boundaries are conventions rather than standards.

### Nadir
The direction from a spacecraft straight down toward the centre of the body it orbits – for a CubeSat, the centre of the Earth. **Nadir-pointing** holds a chosen body axis along this direction, which is the standard attitude for Earth observation payloads and downward-facing antennas. The opposite direction is **zenith**.

### Nodal model
Also **lumped-parameter model**. The standard method of spacecraft thermal analysis: the spacecraft is divided into a number of isothermal nodes, each with a thermal capacitance, linked by conductive and radiative couplings and driven by environmental and internal heat loads. Model fidelity ranges from a single node (useful for a first feasibility estimate) through 6–20 nodes (typical for a CubeSat) to hundreds for gradient-critical payloads. See [Thermal – Thermal Modelling and Simulation](../development/thermal.md#thermal-modelling-and-simulation).

### OAP
**Orbit Average Power.** The time-weighted average power consumed (or generated) over a complete orbit, accounting for different operational modes, duty cycles, and eclipse/sunlight fractions. The headline figure a power budget must balance: average generation ≥ average consumption. See [EPS –  Power Requirements and Budgets](../development/eps.md#power-requirements-and-budgets).

### OBC
**On-Board Computer.** The central processing unit of the spacecraft, responsible for executing flight software, managing mode transitions, handling telecommands, collecting telemetry, and coordinating subsystem activity. See [OBC](../development/obc.md).

### Orbit

A closed (or near-closed) path followed by a spacecraft around a celestial body under the influence of gravity. For CubeSats, this almost always means an orbit around Earth. Key parameters that define an orbit include its **altitude** (how far above Earth's surface), **inclination** (the angle between the orbital plane and the equator), **eccentricity** (how circular vs. elliptical the path is), and **period** (the time to complete one revolution –  typically 90–120 minutes in LEO).

The orbital parameters determine almost everything else about the mission environment: how long each pass lasts over a ground station, what fraction of each orbit is spent in eclipse, how intense the radiation environment is, how quickly the orbit decays from atmospheric drag, and what beta angle the spacecraft sees at different times of year. See [LEO](#leo), [beta angle](#beta-angle), [eclipse fraction](#eclipse-fraction), and [TLE](#tle).

### OTV
**Orbital Transfer Vehicle**, also OMV (orbital manoeuvring vehicle). A propulsive "space tug" that carries payloads from a rideshare drop-off orbit to a different altitude, inclination or phasing. Flown examples include D-Orbit's ION, Rocket Lab's Photon, Impulse Space's Mira and Momentus's Vigoride. An increasingly practical answer when the available rideshare orbit is wrong for the mission.

### Outgassing
The release of trapped gases and volatile compounds from materials exposed to vacuum. The escaping molecules condense on the coldest nearby surfaces – typically optics, radiators and solar cells – degrading their performance. Non-metals are the main offenders: adhesives, tapes, cable ties, conformal coatings, printed parts and potting compounds. Materials are screened using **ASTM E595**, which reports **TML** (total mass loss) and **CVCM** (collected volatile condensable material) after 24 hours at 125 °C in vacuum; the commonly applied screening criteria are TML ≤ 1.00% and CVCM ≤ 0.10%. The [NASA Goddard Outgassing Database](https://etd.gsfc.nasa.gov/capabilities/outgassing-database/) publishes results for thousands of materials.

---

## P

### Payload user guide (PUG)
The document issued by a launch provider defining what a payload must do to fly on their vehicle: mechanical envelope, mass and centre-of-mass limits, environmental levels, electrical interfaces, safety requirements and delivery schedule. Together with the [deployer](#deployer) manual, it supersedes the [CDS](#cds) wherever they conflict. Read it before finalising any external geometry.

### PC/104
An embedded computing form factor, originally for industrial PCs, whose stacking-connector concept was adapted by the CubeSat community into a de facto internal board standard – roughly 90 × 96 mm boards joined by a 104-pin stacking header. The mechanical convention is widely shared; the **pinout is not standardised**, so boards from different vendors may mate physically and still be electrically incompatible. See [Structure – Mounting and Mechanical Interfaces](../development/structure.md#mounting-and-mechanical-interfaces).

### PocketQube
A satellite form factor smaller than a CubeSat, based on a 5 cm cube (1P) rather than a 10 cm one. Cheaper to build and launch, correspondingly more constrained in power, volume and communications. Shares most of the engineering considerations described on this site, at a harder scale.

### Pointing accuracy / pointing knowledge
Two distinct requirements that are frequently conflated. **Pointing accuracy** (or control) is how precisely the spacecraft actually points at the time. **Pointing knowledge** is how precisely you can determine, afterwards, where it was pointing – which can be reconstructed on the ground from recorded sensor data. Knowledge is much cheaper than accuracy: an imaging mission that georeferences its images in post-processing may need tight knowledge but only loose control. Specifying accuracy where knowledge would do is a common way to make an ADCS needlessly expensive.

### Pass
A single opportunity to communicate with a satellite, from the moment it rises above the station's usable horizon until it sets. A typical LEO CubeSat gives a mid-latitude ground station roughly four to six usable passes a day, each lasting 5–12 minutes – on the order of 30–60 minutes of daily contact, which is the fundamental constraint on how much data a mission can return. Pass quality varies enormously with maximum elevation.

### Passivation
Permanently de-energising a spacecraft at end of life – discharging batteries, venting or depleting any stored pressure, and disabling transmitters – so that it cannot later explode or fragment and generate debris. Increasingly a licensing requirement rather than good practice, and it needs to be a commandable function that has actually been tested.

### PCM
**Phase Change Material.** A substance used to buffer thermal transients by absorbing latent heat as it melts and releasing it as it solidifies, holding a near-constant temperature meanwhile. Paraffins melting between 20 and 60 °C store roughly 140–333 kJ/kg. Useful for payloads that dissipate hard in short bursts; the cost is the mass of the containment housing.

### PDR
**Preliminary Design Review.** A formal milestone in the spacecraft development lifecycle, typically held after concept design when the architecture is established and preliminary analysis exists but detailed design is not yet complete. At PDR the design should be feasible and requirements-compliant, with conservative margins (e.g. 30% on mass, power). CDR follows once the design matures.

### P-POD
**Poly-Picosatellite Orbital Deployer.** The original CubeSat [deployer](#deployer), developed at California Polytechnic State University alongside the [CDS](#cds). It holds up to 3U of CubeSats and ejects them with a spring. Largely superseded by newer commercial deployers, but its interface conventions – rails, deployment switches, the 3U tube – shaped the standard that everything since has followed.

### Protoflight
A test philosophy in which the actual flight hardware is tested at qualification *levels* but for reduced *duration*, rather than qualifying a separate dedicated test article. Standard practice for CubeSats, where building a second full spacecraft purely to break it is rarely affordable. The tradeoff is that the flight article accumulates some fatigue life during testing. See [AIT](../development/ait.md#environmental-testing).

---

## Q

### Quasi-static load
The steady, low-frequency acceleration a spacecraft experiences during launch, expressed as a constant g-load along each axis. Taken from the launch vehicle's user guide and applied in structural analysis as a simple static load case. For CubeSats it is usually less demanding than [random vibration](#random-vibration), which tends to be the sizing case.

### PUS
**Packet Utilization Standard**, ECSS-E-ST-70-41C. The European standard defining a service-based model for spacecraft telemetry and telecommand: standardised services for command verification, housekeeping reporting, event reporting, onboard scheduling, parameter management and more. Comprehensive to the point of being heavy for a 1U, but explicitly designed to be tailored – adopting a handful of its services is a common middle path.

### Qualification testing
Environmental testing performed to demonstrate that a *design* has margin, by testing at levels above those expected in service – typically maximum expected random vibration spectrum +3 dB for two minutes per axis, and a larger number of thermal cycles. Conducted on a dedicated qualification model, unless a [protoflight](#protoflight) approach is used. Contrast [acceptance testing](#acceptance-testing).

### Quaternion
A four-element mathematical representation of orientation in 3D space, widely used in spacecraft ADCS for its numerical stability and freedom from the [gimbal lock](#gimbal-lock) singularities that affect Euler angles. A unit quaternion q = [q₀, q₁, q₂, q₃] encodes a rotation axis and angle in a form convenient for onboard computation.

---

## R

### Rail
The four load-bearing edges running along a CubeSat's Z axis, which slide against the matching rails inside the [deployer](#deployer). The [CDS](#cds) requires them to be at least 8.5 mm wide, with a surface roughness below 1.6 µm and edges rounded to at least 1 mm radius, and requires aluminium rails to be hard anodised against [cold welding](#cold-welding). At least 75% of the rail length should contact the deployer. Rails are simultaneously the most tolerance-critical and the most easily damaged surfaces on the spacecraft.

### Rideshare
Flying as a secondary payload alongside a primary mission, sharing the cost of a launch. The dominant route to orbit for CubeSats, and the origin of most of their constraints: the primary's orbit is the orbit you get, and a set of "do no harm" requirements – restricting transmitters, deployments and hazardous materials – is imposed to protect the primary payload. See [Qualification and Launch](../development/launch.md#launch-procurement).

### Radiometric calibration
Establishing the relationship between an instrument's raw output counts and the physical quantity being measured, using reference sources of known output – integrating spheres for imagers, radioactive sources of known energy for particle and gamma-ray detectors, blackbodies for thermal instruments. Without it, instrument output is a number rather than a measurement. Ground calibration shifts during launch and drifts in orbit, so it must be verified and repeated on orbit.

### Random vibration
A broadband, statistically described vibration environment – the dominant structural load case for most CubeSat hardware. Specified as an acceleration power spectral density (PSD) in g²/Hz across a frequency band, and summarised by an overall [Grms](#grms) value. [GEVS](#gevs) gives 14.1 Grms for 2 minutes per axis as the component qualification level. See [Structure](../development/structure.md#structural-analysis-and-fem).

### RBF pin
**Remove-Before-Flight pin.** A physical insert that cuts all power to the spacecraft while in place, fitted with a large brightly coloured streamer so it cannot be overlooked. Removed before launch – before deployer integration if the deployer has no access port. The [CDS](#cds) requires it to cut *all* power and to protrude no more than 6.5 mm from the rail surface when fully inserted.

### Radiator
A surface designed to reject heat to space, characterised by high infrared [emissivity](#emissivity) and low solar [absorptivity](#absorptivity), with a clear view of deep space and a good conduction path to whatever it is cooling. Scarce on CubeSats, because the external faces are usually already committed to solar cells.

### RAAN
**Right Ascension of the Ascending Node.** One of the six classical orbital elements: the angle, measured in an inertial frame, to the point where the orbit crosses the equatorial plane travelling north. Together with inclination it defines the orientation of the orbital plane in space. RAAN precesses over time due to Earth's oblateness – an effect deliberately exploited by [sun-synchronous orbits](#sso).

### Requirements traceability
The practice of linking every requirement to the parent objective it derives from, the design element that satisfies it, and the verification activity that proves it. Usually maintained as a matrix – a spreadsheet is perfectly adequate on a CubeSat. Its practical value shows up twice: when a late change forces you to identify what it breaks, and when the [V&V](#vv) programme needs to demonstrate that every requirement has been closed out.

### Reaction wheel
A spinning flywheel used as an attitude actuator. By accelerating or decelerating the wheel, angular momentum is exchanged with the spacecraft body, producing a controlled torque without expelling propellant. Reaction wheels can become saturated (spin at their maximum rate) and must be periodically desaturated using magnetorquers or thrusters.

---

## S

### RTOS
**Real-Time Operating System.** A small operating system providing pre-emptive task scheduling with priorities and bounded, predictable response times – the property a general-purpose OS does not guarantee. FreeRTOS, Zephyr and RTEMS are the common choices in CubeSat flight software, with RTEMS carrying the most spaceflight heritage. See [Flight Software](../development/flight-software.md).

### Scrubbing
Periodically reading through memory (or an SRAM-based FPGA's configuration) and rewriting corrected values, so that accumulated [single-event upsets](#seu) are removed before a second upset in the same word makes them uncorrectable. Usually paired with [EDAC](#edac).

### Safe mode
The fallback operating state a spacecraft enters autonomously when something goes wrong: non-essential loads off, attitude control reduced to something power-positive or passive, battery charging, receiver listening and beacon transmitting. Safe mode must be reachable from every other mode, must be entered without ground intervention, and must be sustainable indefinitely – it is the state the mission is recovered *from*. See [Flight Software – Modes](../development/flight-software.md#modes-state-machines-and-autonomy).

### SatNOGS
**Satellite Networked Open Ground Station.** An open-source, community-driven global network of ground stations that receive and share satellite signals, including CubeSat beacons. Operated by the Libre Space Foundation. A de facto standard for beacon reception in academic and open-source missions. [satnogs.org](https://satnogs.org/).

### SPOF
**Single Point of Failure.** Any element whose failure alone ends the mission. CubeSats have many – the battery, the EPS, the OBC, the radio, the antenna deployment, the bus linking OBC to EPS – and the useful exercise is not eliminating them, which mass and volume rarely permit, but knowing where they are and ensuring each is as simple, well-tested and recoverable as possible.

### SSO
**Sun-Synchronous Orbit.** A near-polar orbit whose plane precesses at the same rate as the Earth orbits the Sun, so that the local solar time of each pass stays constant. Valuable for imaging missions because lighting conditions are repeatable, and in the **dawn–dusk** variant it keeps the spacecraft in near-continuous sunlight – which transforms the [power budget](../development/eps.md#power-requirements-and-budgets) while making the thermal hot case harder.

### Solar constant
The solar radiant flux at 1 AU, averaging about 1367 W/m². It varies seasonally by roughly ±3.5% with Earth's orbital distance – approximately 1422 W/m² at perihelion and 1318 W/m² at aphelion – and these bounds are used as the hot and cold case values in thermal analysis.

### SEL
**Single-Event Latch-up.** A radiation-induced fault in which an energetic particle triggers a parasitic thyristor structure in a CMOS device, creating a low-impedance path between supply and ground. Current rises sharply and the device is destroyed unless power is removed promptly. The standard mitigation on CubeSats is a current-limiting switch that trips and power-cycles the affected channel. See [EPS](../development/eps.md#power-switching-and-protection) and [OBC](../development/obc.md#redundancy-and-fault-tolerance).

### SMA
**Shape Memory Alloy.** A nickel-titanium alloy that changes crystal phase when heated, producing a strong, repeatable mechanical stroke. Used in release mechanisms (release nuts, pin pullers, frangibolts) as a cleaner alternative to [burn wires](#burn-wire): no debris, no melting residue, high actuation force, and many devices are resettable on the ground – which greatly improves how thoroughly they can be tested. Costs more and draws more power, and actuation timing depends on starting temperature.

### SGP4
**Simplified General Perturbations model 4.** The analytical orbit propagator that [TLEs](#tle) are designed to be used with. TLE element values are fitted to SGP4's specific internal assumptions, so feeding them into a general-purpose Keplerian propagator produces plausible-looking but wrong results. SGP4 outputs coordinates in the TEME frame rather than J2000, another common source of quiet errors.

### SDR
**Software-Defined Radio.** A radio in which demodulation, filtering and decoding are performed in software on digitised samples rather than in fixed analogue hardware. This makes one piece of hardware able to receive almost any waveform, which is why SDRs dominate CubeSat ground stations. Common devices range from the very low-cost RTL-SDR (the SatNOGS reference radio) through Airspy and Adalm-Pluto to full-duplex USRP hardware.

### SEFI
**Single-Event Functional Interrupt.** A radiation-induced fault that puts a device into a non-functional state – a hung processor, a corrupted control register, a peripheral that stops responding – without physically damaging it. Cleared by a reset, which is the main reason spacecraft carry layered [watchdogs](#watchdog).

### SEU
**Single-Event Upset.** A bit flip in a memory cell or register caused by a single energetic particle. Non-destructive but silently corrupting: the device keeps working, with wrong data. Mitigated by [EDAC](#edac), [scrubbing](#scrubbing) and [TMR](#tmr).

### Slew
A commanded reorientation of the spacecraft from one attitude to another. Slew rate – how fast the spacecraft can turn – determines how much of a ground station pass or imaging opportunity can actually be used, and is set by available actuator torque against the spacecraft's moment of inertia.

### SNR
**Signal-to-Noise Ratio.** The ratio of signal power to noise power at a receiver input, usually expressed in dB. A key figure in link budget analysis –  the received SNR must exceed the minimum required for the chosen modulation and coding scheme.

---

## T

### Standoff
A threaded spacer that separates and supports stacked circuit boards inside a spacecraft, carrying both the mechanical load and, frequently, the electrical ground path between boards. Standoff material is a deliberate thermal design choice: metal standoffs couple a board to the structure as a heat sink, polymer ones isolate it. Where the structure is hard anodised and therefore non-conductive, the ground return must be designed explicitly rather than assumed through the standoffs.

### Telecommand
An instruction sent from the ground to a spacecraft. Because the spacecraft cannot be reached physically and contact is intermittent, telecommands are validated at several levels – packet integrity, command validity, argument range, and whether the command makes sense in the current state – and irreversible ones are typically guarded by an arm-then-fire sequence with an independent timeout. See [Flight Software](../development/flight-software.md#commands).

### TID
**Total Ionising Dose.** The cumulative radiation dose a component absorbs over a mission, measured in rad or gray (1 krad(Si) = 10 Gy). TID causes gradual parameter drift and eventual failure in semiconductors. A typical [LEO](#leo) CubeSat mission accumulates on the order of a few krad(Si) behind normal shielding, which is why carefully screened [COTS](#cots) parts are viable where they would not be in a higher-radiation orbit.

### Thermal strap
A flexible conductive link that carries heat between two points while allowing them to move relative to one another, decoupling thermal and mechanical design. Typically copper or aluminium braid, or pyrolytic graphite sheet (PGS), which offers higher conductivity than either metal in the same geometry.

### TMR
**Triple Modular Redundancy.** Implementing a function three times in parallel and taking a majority vote on the output, so that a fault in any single instance is outvoted. Common inside radiation-tolerant FPGA designs, at roughly three times the resource cost.

### Star tracker
An attitude sensor that images the star field and matches the observed pattern against an onboard catalogue to determine absolute orientation, typically to a few arcseconds. The most accurate attitude sensor available, and the most demanding: it needs real onboard compute, careful baffle design against stray light from the Sun, Earth and Moon, and it loses lock above a few degrees per second of body rate – so it cannot help during [detumbling](#detumbling).

### Sun sensor
An attitude sensor measuring the direction to the Sun, and the cheapest useful attitude sensor available. Ranges from cosine detectors (a bare photodiode, 2–5° accuracy – often just a solar panel's current) through quadrant detectors (0.2–0.5°) to digital sun cameras (0.1° down to 0.01°). Needs several units for full sky coverage, can be confused by Earth albedo, and is useless in eclipse.

### TLE
**Two-Line Element set.** A standardized format for encoding a satellite's orbital parameters at a given epoch, used as input to propagators such as SGP4. TLEs are published by the US Space Surveillance Network (via Space-Track) and used widely for tracking and pass prediction. See [GNC –  Orbit Representation / TLEs](../development/gnc.md#orbit-representation-tles).

### Triple-junction solar cell
A photovoltaic cell stacking three semiconductor junctions of different bandgaps, so each converts a different portion of the solar spectrum. Built from Group III-V materials (typically GaInP/GaAs/Ge) rather than silicon, these reach around 30% beginning-of-life efficiency against roughly 20% for single-junction silicon, and are the flight standard for CubeSat solar arrays. Often abbreviated **TJ**. See [EPS – Solar Power Generation](../development/eps.md#solar-power-generation).

### Trade study
A structured comparison of design options against criteria that are chosen and weighted *before* scoring. The lasting value is less the numerical result than the recorded rationale, which is what allows a team – often a different team – to understand a design later rather than reverse-engineer it. Worth the effort for decisions that are hard to reverse (form factor, bus architecture, attitude control approach) and not for ones that are cheap to change.

### TVAC
**Thermal Vacuum testing.** Environmental testing in a vacuum chamber with a controlled thermal environment – the only realistic way to verify spacecraft thermal behaviour, since removing convection fundamentally changes how heat moves. Two distinct tests are run under this heading: **thermal cycling**, which demonstrates survival and function across the temperature range and exposes workmanship defects, and **thermal balance**, which reaches steady state at a predicted case so the [nodal model](#nodal-model) can be correlated against measurement. See [AIT](../development/ait.md#environmental-testing).

### TRL
**Technology Readiness Level.** A scale from 1 to 9 used to assess the maturity of a technology, from basic principles (TRL 1) through lab demonstration (TRL 4–5), relevant environment testing (TRL 6–7), to flight-proven (TRL 9). Originally developed by NASA. Commonly used in CubeSat procurement and mission risk assessment.

### TT&C
**Telemetry, Tracking, and Command.** The fundamental communication function between a spacecraft and its ground segment. Telemetry is housekeeping data downlinked from the spacecraft; tracking determines its position and velocity; command is the uplink of instructions. See [Comms](../development/comms.md).

### Tuna can
The additional cylindrical volume permitted beyond the nominal CubeSat envelope on certain form factors, so named for its shape and size. Commonly used to house a deployable antenna, a propulsion nozzle or a radiator that will not fit inside the rails. Availability and dimensions vary by [deployer](#deployer) – confirm against the [payload user guide](#payload-user-guide-pug) rather than assuming.

---

## U

### U (CubeSat unit)
The standard size increment in the CubeSat form factor system. 1U is defined as 100 × 100 × 113.5 mm with a mass limit of 2 kg. Larger form factors (1.5U, 2U, 3U, 6U, 12U, 16U…) scale linearly in one or more dimensions. Defined in the [CDS](#cds).

### UHF / VHF
**Ultra-High Frequency / Very High Frequency.** Radio frequency bands commonly used in CubeSat communications. VHF covers 30–300 MHz (uplinks often around 145–146 MHz); UHF covers 300 MHz–3 GHz (downlinks often around 437 MHz). Both bands are popular with amateur missions due to favorable propagation, lower required transmit power, and the availability of the [SatNOGS](#satnogs) network.

---

## V

### Watchdog
A timer that resets or power-cycles a device unless it is periodically "kicked" by software that is proving itself healthy. The single most important reliability mechanism on a CubeSat, usually implemented as a hierarchy: an internal MCU watchdog, an external timer IC, and an [EPS](#eps)-level watchdog that cuts power to the whole processor. Kicking the watchdog from a bare timer interrupt defeats its purpose, since it will keep firing while the rest of the system is deadlocked. See [OBC](../development/obc.md#watchdogs).

### V&V
**Verification and Validation.** Two complementary processes. *Verification* confirms that the system was built correctly (meets requirements, as demonstrated by test, analysis, inspection, or similarity). *Validation* confirms that the right system was built (meets the mission need). See [Systems Engineering](../development/systems-engineering.md).

---

*This glossary is community-maintained. To add or correct an entry, see the [contributing guide](../contributing.md).*