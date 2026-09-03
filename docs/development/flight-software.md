# Flight Software

Flight software is what coordinates everything onboard: data handling, command execution, mode management, fault response and telemetry. This page covers architecture and execution models, boot and update strategy, commanding, autonomy, FDIR, timing and testing, for both bare-metal and RTOS-based designs.

Flight software differs from ordinary embedded software in one way that changes every design decision: **you cannot attach a debugger, and you cannot ship a hotfix quickly.** Your only interface is a few minutes of low-bandwidth radio contact per day, and that interface only works if the software is already running correctly. Everything below follows from that.

## Software Architecture and Execution Model

### Layering

The single most valuable architectural decision is separating the software into layers with clean boundaries:

- **Hardware abstraction layer ([HAL](../references/glossary.md#hal))** – register-level drivers, isolated behind interfaces. Everything hardware-specific lives here and nowhere else.
- **Services** – the reusable machinery: telemetry collection, command dispatch, storage, time, scheduling, communications.
- **Application logic** – what your mission actually does: mode management, payload operations, control loops.

The payoff is testability. If the application layer talks only to interfaces, you can compile and run it **on a development machine** against simulated hardware, which turns a category of bugs that would otherwise be found on a flatsat (slowly, one at a time) into ones found by a test suite in seconds. Teams that get this right ship dramatically better software than teams that do not, and the difference compounds over a multi-year project.

### Execution models

- **Superloop (bare metal).** A `while(1)` cycling through tasks, with interrupts for time-critical work. Completely deterministic and small enough to hold in your head – a reliability advantage in itself. It degrades when one task needs to block, since everything else stops with it.
- **Cooperative scheduling.** Tasks voluntarily yield. Retains much of the simplicity of a superloop while allowing more structure. No pre-emption means no surprise race conditions, but a misbehaving task still stalls the system.
- **Pre-emptive [RTOS](../references/glossary.md#rtos).** Priority-based pre-emption with real-time guarantees. The mainstream choice above modest complexity, at the cost of having to reason about priority inversion, stack sizing per task, and shared-state races.
- **Event-driven.** Tasks triggered by events from a queue. Maps well onto command handling and fault response, and combines naturally with a state machine design.

Most CubeSat flight software ends up as a **time-triggered schedule with event handling layered on**: a periodic tick drives housekeeping, control loops and telemetry at fixed rates, while commands and faults are handled as they arrive. This is predictable, easy to reason about in a fault investigation, and easy to reproduce on the ground.

### Frameworks vs. writing your own

Writing your own is the norm on small missions and is entirely defensible – the total functionality needed by a 1U technology demonstrator is modest, and full comprehension of your own stack has value when debugging from 500 km away.

Adopting a framework such as NASA's [Core Flight System](#open-source-flight-software-projects) buys architecture, flight heritage across 40+ NASA missions, and a component model that scales. It costs a substantial learning curve and pulls in more machinery than a small CubeSat needs. The test is team size and mission duration: a two-person 1U project is usually better served writing something small and comprehensible; a university programme flying successive missions over a decade benefits enormously from a framework it can carry forward.

### Language and coding standards

- **C** remains the default: every RTOS and framework targets it, toolchains for space-grade parts assume it, and its behaviour is predictable. It also offers no protection whatsoever, which is why the coding standards below exist.
- **C++** is used in larger stacks, cFS-adjacent tooling and PUS implementations. Workable with a restricted subset – no exceptions, no RTTI, no dynamic allocation after initialisation – and a liability without one.
- **MicroPython and CircuitPython** trade determinism and memory headroom for development speed, and have flight heritage on small missions through PyCubed. A reasonable choice for a technology demonstrator where iteration speed matters more than hard real-time behaviour, and a poor one where control loops must close on schedule.
- **Rust** is increasingly credible for new work, with memory safety that removes a whole class of the bugs the standards below try to prevent by discipline. The constraint is ecosystem: fewer vendor HALs, fewer eyes on your code within the team, and a smaller pool of people who can maintain it after you graduate.

Two coding standards are worth knowing even if you do not adopt them formally. **MISRA C** is the automotive-derived rule set that most safety-critical embedded work references, and **NASA's Power of Ten** is a much shorter set of rules for safety-critical code – no recursion, fixed loop bounds, no dynamic allocation after initialisation, functions short enough to read whole, check every return value.[^power-of-ten] The full apparatus is disproportionate for a 1U, but the individual rules are not: **no dynamic allocation after startup** and **bounded loops** alone eliminate the two failure modes most likely to strand a spacecraft, and cost nothing to adopt on day one. Whatever you choose, run a static analyser in CI and treat compiler warnings as errors.

## Boot, Reset, and Update Strategy

### Bootloaders and the golden image

The rule is simple: **there must always be a path back to a known-good state that no in-flight action can destroy.**

- A **[golden image](../references/glossary.md#golden-image)** in write-protected or read-only memory, which always boots to a minimal state capable of receiving commands, charging the battery and accepting a new upload. It is never updated in flight. It does not need to be capable of the mission – only of recovery.
- A **primary application image**, updatable, holding the flight software proper.
- Ideally a **backup application image**, so a bad update can be rolled back without falling all the way to golden.

Every image should be **checksummed and verified before execution**, not after. A corrupted image that gets executed can do arbitrary damage; a corrupted image that fails a CRC check is merely a failed update.

### Boot counting and autonomous fallback

Keep a boot counter in non-volatile memory. Increment it on every boot; clear it only once the system has run stably for a defined period (say, an hour) and has had contact with the ground. If the counter passes a threshold, boot the golden image instead.

This one mechanism converts the classic CubeSat boot loop – the spacecraft resetting endlessly and never surviving long enough to hear a command – from mission-ending into self-healing.

### The first boot in orbit

The first hours after deployment are the only part of the mission that is entirely unattended and entirely unrepeatable, and the sequence needs to be written down and rehearsed as deliberately as any other procedure.

- **Respect the timers before anything else.** No deployables for 30 minutes and no RF for 45 minutes after release from the deployer, or whatever stricter figure your provider imposes. These are contractual, not preferences, and the timer must survive a reset during the wait – count from persisted state, not from boot. See [Inhibits and HDRM – Timers and Delayed Activation](inhibits-hdrm.md#timers-and-delayed-activation).
- **Retry antenna deployment, and keep retrying.** Attempting deployment once, failing, and giving up has ended missions. Design for escalating attempts: repeat the burn with increasing duration, spaced over hours and then days, alternating redundant burn circuits if you have them. Keep the attempt counter and success flag in non-volatile memory so a reset does not restart the sequence from zero or, worse, re-run a successful deployment.
- **Verify deployment, don't assume it.** A deployment switch, a continuity break in the burn wire, or a change in received signal strength gives you evidence. Telemeter it, because "no signal" and "antenna still stowed" need different responses from the ground.
- **Charge before you talk.** A spacecraft deployed into eclipse on a partly discharged pack should establish power positive before it starts transmitting. Sequence the first beacon behind a state-of-charge threshold, with a timeout so a faulty sensor cannot suppress it forever.
- **Beacon early and simply.** The first beacon should require the least possible machinery to produce – ideally it works from the golden image. Everything else about commissioning depends on someone hearing you.

### In-flight updates

Updating software in orbit is possible, valuable, and dangerous.

- **Design for it from the start.** Retrofitting an update path onto software that never had one is much harder than building it in.
- **Uplink in verified chunks**, with per-chunk checksums and the ability to resume. Remember that the uplink is usually far slower than the downlink: a 1200 bps command channel carries about 90 kB across a 10-minute pass, so a 200 kB image is a multi-pass operation that must survive interruption between passes.
- **Stage, verify, then commit.** Write to inactive storage, verify the whole image, and only then switch the boot pointer.
- **Always keep a rollback.** Automatic reversion if the new image fails to check in within a timeout is the standard pattern, and it is what makes updating survivable.
- **Update only when there is a reason.** Every update is a chance to lose the spacecraft. Batch fixes, test exhaustively on a flatsat with the same hardware, and rehearse the full procedure through the real comms path before doing it in flight.

### Brownouts and partial failures

A brownout is more dangerous than a clean power cycle because the processor may execute unpredictably on the way down – [OBC – Brownout and reset behaviour](obc.md#brownout-and-reset-behaviour) covers the hardware side. For software the rule is to assume any non-volatile write can be interrupted: use atomic update patterns (write, verify, then update a pointer), keep redundant copies of critical configuration, and never leave a single half-written record able to prevent boot. See [OBC – Boot, Power, and Reset Management](obc.md#boot-power-and-reset-management).

### Storage and filesystems

The same reasoning extends to bulk storage, and this is where a surprising number of CubeSats lose data or fail to boot.

- **A general-purpose filesystem is a liability.** FAT in particular has no crash consistency: an interrupted write can corrupt the allocation table and take the whole volume with it, not just the record being written. If you must use FAT for ground-side convenience, keep flight-critical state somewhere else.
- **Prefer append-only logs or a journaling filesystem.** An append-only ring buffer with per-record checksums degrades gracefully – a torn record at the end is discardable, and everything before it is still readable. LittleFS and similar power-loss-resilient filesystems are designed for exactly this.
- **Raw flash needs wear levelling and bad-block handling.** NAND blocks fail with use, and a naive driver that rewrites the same block for every telemetry record will find its limits within a mission.
- **Separate the critical from the bulk.** Boot configuration, the golden image and the mode state belong in small, redundant, checksummed storage that is written rarely. Telemetry and payload data belong in bulk storage whose corruption costs you data but never the spacecraft.
- **Test with power cuts.** Pull power mid-write, repeatedly, and confirm the system boots and the log is readable afterwards. This is the single most informative storage test and almost nobody runs it.

## Command and Telemetry Handling

### Commands

A [telecommand](../references/glossary.md#telecommand) is an instruction to do something irreversible on a spacecraft you cannot reach. Treat it accordingly.

- **Validate before executing**: checksum the packet, check the command is known, range-check every argument, and verify the spacecraft is in a state where the command makes sense. Rejecting a command is nearly always safer than half-executing one.
- **Authenticate.** Validation asks whether a command is well-formed; authentication asks whether it came from you. Your uplink frequency, modulation and frame format are public – they are in your IARU coordination and very likely in a paper you published – so anyone with a transmitter can construct a plausible command. The standard answer is a message authentication code (an HMAC over the command payload) plus a monotonically increasing counter or timestamp to defeat replay of a previously captured command. Note the regulatory asymmetry: obscuring the *meaning* of general amateur transmissions is prohibited, but telecommand is treated separately, and in the US a space telecommand station "may transmit special codes intended to obscure the meaning of telecommand messages".[^fcc-telecommand] Check your own administration's equivalent. Authentication alone is legal everywhere and sufficient for the threat, so start there.
- **Acknowledge in stages** – received, accepted, started, completed – so the ground can tell the difference between a command that never arrived and one that arrived and failed.
- **Time-tagged commands** let you schedule activity outside contact windows, which is essential given a few passes a day. This means the command store needs its own management: listing, clearing, and surviving reset.
- **Guard dangerous commands.** Anything that could end the mission – disabling the radio, changing inhibit state, erasing memory, commanding a deployment – should require an arm-then-fire sequence, and should carry an independent timeout that undoes it if nothing further is heard. **Never allow a command that can permanently disable your only recovery path.**
- **Idempotency.** Given a lossy link, the ground will resend. Design commands so a duplicate is harmless.

### Telemetry

- **Housekeeping** – periodic health data at a fixed cadence: voltages, currents, temperatures, mode, error counters. This is your primary diagnostic channel and should be small enough to fit in a [beacon](../references/glossary.md#beacon).
- **Event/log data** – discrete occurrences with timestamps: mode changes, faults, resets, command receipts. Log to non-volatile storage; downlink on request.
- **Payload data** – usually the bulk, downlinked on a different schedule and often a different link.

Design principles worth adopting early:

- **Downlink budget is the constraint.** At 9600 bps over four 8-minute passes you have on the order of 2.3 MB per day *before* protocol overhead and retries. See [Comms – Expected Data Rates](comms.md#expected-data-rates).
- **Store far more than you send.** Log at high rate onboard, downlink summaries routinely, and dump full-rate data only when investigating.
- **Beacon something useful.** A short periodic beacon with the most important values gives you and the [SatNOGS](../references/glossary.md#satnogs) community a health picture even when you have no pass.
- **Never let telemetry storage fill up and block.** Define ring-buffer behaviour explicitly.

### Inter-Subsystem Communication Protocols

Middleware sits above the physical bus and gives subsystems addresses and services instead of raw bytes, so that moving a function between processors does not rewrite everything.

- **[CSP](../references/glossary.md#csp) (Cubesat Space Protocol)** is the de facto CubeSat standard. A small C stack modelled on TCP/IP with a very lightweight header carrying both transport and network-layer information, connection-oriented and connectionless modes, ICMP-like ping and buffer-status requests, a QoS router, zero-copy buffers and a thread-safe socket API. It runs over CAN, UDP, USART and ZMQ, on FreeRTOS, Zephyr and Linux, and is MIT-licensed.[^libcsp] Originating at Aalborg University and GomSpace, it is widely flown.
- **SpaceCAN**, from LibreCube, takes a different approach: a deliberately simplified derivative of the ECSS CANbus extension standard (ECSS-E-ST-50-15C), on the reasoning that the full ECSS protocol is "too complex in terms of implementation and usage" for small spacecraft. It defines a nominal and redundant bus pair (A and B) with one controller and up to 127 responder nodes, and uses controller heartbeats for cold redundancy – responders that stop hearing the heartbeat switch buses automatically.[^spacecan]

The tradeoff between them is characteristic: CSP gives you a flexible network abstraction over almost any transport; SpaceCAN gives you a tightly specified, redundancy-aware bus with less flexibility and fewer ways to get it wrong. Either is better than inventing an ad-hoc byte protocol, which is what most first missions do and later regret.

Whatever you choose, **fault isolation is the property that matters**: one subsystem misbehaving must not silently corrupt or block traffic for everyone else. See [OBC – Interfaces and Buses](obc.md#interfaces-and-buses) for the physical-layer half of this problem.

### Data Serialisation and Message Formats

- **Custom binary structs** are compact and fast, and are what most CubeSats use. The risk is versioning: the moment ground software and flight software disagree about a struct layout, your telemetry becomes silently wrong rather than obviously broken. Never rely on compiler struct packing across platforms – serialise field by field, explicitly.
- **[CCSDS](../references/glossary.md#ccsds) Space Packet Protocol** is the international standard for spacecraft packet structure, with a defined primary header carrying an application process identifier, sequence flags and length. Adopting it costs a little overhead and buys interoperability with existing ground tooling and, potentially, third-party ground stations.
- **[PUS](../references/glossary.md#pus) (ECSS-E-ST-70-41C)** layers a full service model on top: standardised services for telecommand verification, housekeeping, event reporting, on-board scheduling, parameter management and more. It is the European operational standard, and it is comprehensive to the point of being heavy for a 1U – but PUS is designed to be *tailored*, and adopting a handful of its services is a legitimate middle path that gives you a well-thought-out design instead of an invented one.
- **Self-describing formats** (CBOR, MessagePack, Protocol Buffers) trade a few bytes for forward and backward compatibility. Worth considering for payload data and configuration; usually too heavy for high-rate housekeeping.

**Versioning is the requirement people forget.** Put a schema or version field in every packet type from day one. You will change telemetry formats during development, and possibly in flight, and without a version field you will not be able to tell which format an archived file is in.

<!-- CSR-RESOURCES:START dev-flight-software-protocols-and-standards -->
- **[LibCSP documentation](https://libcsp.github.io/libcsp/)** `Link` – Documentation for the Cubesat Space Protocol reference implementation
- **[libcsp on GitHub](https://github.com/libcsp/libcsp)** `Link` – MIT-licensed CSP source, running on FreeRTOS, Zephyr and Linux
- **[SpaceCAN (LibreCube)](https://librecube.gitlab.io/standards/spacecan/)** `Link` – Simplified redundant CAN bus standard for small spacecraft, derived from ECSS-E-ST-50-15C
- **[ECSS-E-ST-70-41C](https://ecss.nl/standard/ecss-e-st-70-41c-space-engineering-telemetry-and-telecommand-packet-utilization-15-april-2016/)** `Link` – The ECSS Packet Utilization Standard for telemetry and telecommand
- **[AcubeSAT ECSS PUS implementation](https://gitlab.com/acubesat/obc/ecss-services)** `Link` – MIT-licensed C++ implementation of the PUS standard from the AcubeSAT team
- **[CCSDS Blue Books](https://ccsds.org/publications/bluebooks/)** `Link` – Freely available recommended standards for space data systems
- **[TM Space Data Link Protocol (CCSDS 132.0-B)](https://ccsds.org/Pubs/132x0b3.pdf)** `PDF` – Telemetry space data link protocol
- **[TC Space Data Link Protocol (CCSDS 232.0-B)](https://ccsds.org/Pubs/232x0b4e1c1.pdf)** `PDF` – Telecommand space data link protocol
<!-- CSR-RESOURCES:END dev-flight-software-protocols-and-standards -->

See also: [Communications](comms.md).

## Modes, State Machines, and Autonomy

### Mission modes

Most CubeSats have four to eight modes. A representative set:

- **Boot / initialisation** – minimal, transient, establishing basic health.
- **Detumble** – reducing body rates after deployment. See [GNC](gnc.md).
- **[Safe mode](../references/glossary.md#safe-mode)** – the fallback: everything non-essential off, sun-pointing or tumbling, battery charging, radio listening, beacon transmitting. Safe mode must be reachable from every other mode, must be entered autonomously, and must be able to sustain itself indefinitely.
- **Nominal** – routine operations, housekeeping, attitude control.
- **Payload** – payload active, with whatever pointing and power that requires.
- **Comms / downlink** – transmitter active, possibly with a slew to point an antenna.

### Implementing modes

- **Make the state machine explicit.** A single, readable table of states, permitted transitions and their guard conditions, in one place. Mode logic that emerges from flags scattered across the codebase is the most common source of unreproducible in-flight behaviour.
- **Guard every transition.** Do not enter payload mode below a battery threshold. Do not slew while the [ADCS](../references/glossary.md#adcs) is unconverged.
- **Add hysteresis.** A mode boundary at exactly 7.2 V will oscillate. Enter safe mode at 7.0 V and leave it at 7.5 V.
- **Telemeter the mode and the reason for the last transition.** "Entered safe mode" is not diagnostic; "entered safe mode due to battery under-voltage at T+4213 s" is.
- **Time-limit every non-safe mode.** If payload mode is entered and nothing ends it, a timeout should. This protects against a lost ground link during a risky operation.

### Autonomy

CubeSat autonomy is mostly a bandwidth-and-contact problem rather than an ambition. With four passes a day, the spacecraft is on its own 97% of the time, so anything that must happen promptly must happen onboard.

Sensible levels, roughly in order of adoption:

1. **Autonomous safety** – enter safe mode on fault. Non-negotiable.
2. **Autonomous housekeeping** – thermal control, battery management, momentum desaturation.
3. **Scheduled autonomy** – execute a ground-uplinked timeline.
4. **Conditional autonomy** – take payload data when conditions are met (over a target, in daylight, battery above threshold).
5. **Onboard decision-making** – data-driven selection of what to keep and downlink. See [OBC – Advanced and Emerging Computing Concepts](obc.md#advanced-and-emerging-computing-concepts).

The design constraint on all of them is the same: **autonomy must never be able to prevent recovery.** However clever the logic, an independent path back to a commandable state must survive it.

## Fault Detection, Isolation, and Recovery (FDIR)

[FDIR](../references/glossary.md#fdir) is the machinery that keeps a spacecraft alive between contacts. It is worth designing deliberately rather than accumulating as a set of ad-hoc checks.

### Detection

- **[Watchdogs](../references/glossary.md#watchdog)**, layered – internal, external, and EPS-level. See [OBC – Watchdogs](obc.md#watchdogs).
- **Limit checking** on every telemetry point, with defined warning and alarm thresholds.
- **Consistency checks** between independent sources – a magnetometer and a sun sensor disagreeing about attitude, a current reading inconsistent with a commanded switch state.
- **Heartbeats** from every subsystem, so silence is itself detectable.
- **Counters and error rates** rather than single events: one CRC failure is noise, a rising CRC failure rate is a symptom.

### Isolation

The point of isolation is to identify the smallest thing that needs action. A power draw anomaly could be the payload, its switch, or the current sensor. Per-channel telemetry is what makes this distinguishable – see [EPS – Monitoring and Telemetry](eps.md#eps-monitoring-and-telemetry).

### Recovery

Escalate, and escalate slowly:

1. **Retry** the operation.
2. **Reset the subsystem** in software.
3. **Power-cycle** the subsystem.
4. **Enter safe mode.**
5. **Reset the OBC.**
6. **Full power cycle** by the EPS watchdog.

Three rules that matter more than the ladder itself:

- **Every recovery action must be counted, rate-limited and telemetered.** A recovery that fires continuously is worse than the fault.
- **Recovery must be reversible or timed out.** A subsystem disabled by FDIR should be re-enabled after a period, not left off forever because nobody uplinked a command.
- **Prefer degraded operation to shutdown.** A spacecraft running on two of three magnetorquers, or with a failed payload but a healthy bus, is still a mission.

### Design for partial failure

Assume every sensor will eventually give bad data, every actuator will eventually fail, and every subsystem will eventually stop responding. For each, ask: does the spacecraft still charge its battery, keep warm, and listen for commands? If yes, the failure is survivable. If no, that is where redundancy or a fallback belongs.

## Timing, Scheduling, and Timekeeping

- **Task scheduling.** Assign priorities deliberately: control loops highest, housekeeping middling, payload processing lowest. Size stacks with margin and measure high-water marks – stack overflow in an RTOS produces corruption that looks like anything but a stack overflow.
- **Time sources, drift and RTC backup** are hardware questions, covered under [OBC – Timing and Timekeeping](obc.md#timing-and-timekeeping); the software has to cope with whatever they deliver.
- **Timestamp everything**, and carry both wall-clock time and a monotonic uptime/boot counter. Wall-clock time can be wrong or lost after a reset; the monotonic counter always lets you order events.
- **Handle time discontinuities explicitly.** When the clock is corrected, time can jump backwards. Any code computing elapsed time by subtracting timestamps needs to cope with that, or it will occasionally compute a negative interval and behave bizarrely.
- **Correct for drift in software** from the temperature characterisation the OBC page describes, because even a compensated crystal drifts enough over a day to degrade attitude determination and Doppler correction if left alone.

## Software Testing and Validation

Flight software is the one subsystem you can test essentially for free and essentially without limit. Very few CubeSat teams exploit that fully.

### The test pyramid

- **Unit tests** on host, covering logic in isolation – mode transitions, command validation, packet encoding, limit checking. Fast, numerous, run on every commit.
- **Integration tests** on host with simulated hardware, covering subsystem interaction and protocol handling.
- **On-target tests** on the flight processor, catching everything the host cannot: timing, memory constraints, compiler differences, actual driver behaviour.
- **[Flatsat](../references/glossary.md#flatsat) tests** with all the hardware connected. The closest thing to flight, and where interface assumptions go to die.
- **[HIL](../references/glossary.md#hil) tests** with simulated orbital dynamics and sensor data, which is the only practical way to exercise a full mission timeline. See [AIT](ait.md#hardware-in-the-loop-hil-testing).

### What to test that teams usually don't

- **Fault paths.** Inject the faults: hold a bus low, corrupt a packet, return garbage from a sensor, cut power mid-write. FDIR that has never been triggered on the ground is a hypothesis.
- **Long-duration runs.** Leave a flatsat running for a week. Memory leaks, counter overflows, log rotation bugs and slow drift only appear over time.
- **Boundary and rollover conditions.** Time rollovers, counter wraps, storage full, command buffer full.
- **The first-boot sequence**, from a cold, deeply discharged start, including the deployment retry logic and the inhibit timers. It runs once, unattended, and you only get one attempt.
- **The update procedure**, end to end, through the flight comms path – not over a bench cable.
- **Regression.** Every bug found in flight or on the flatsat should become a test, so it cannot come back.

### Software testing methodologies

<!-- CSR-RESOURCES:START dev-flight-software-testing-methodologies -->
- **[The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)** `Link` – Overview of the software test pyramid
<!-- CSR-RESOURCES:END dev-flight-software-testing-methodologies -->

See also: [Assembly, Integration and Testing (AIT)](ait.md).

## Flight Software and Hardware Interaction

- **Drivers and HAL.** Keep every register access behind an interface. This is what makes host-based testing possible, and it also makes a late hardware change survivable.
- **Power and inhibit awareness.** Software must know which loads are enabled, must not command a device on a powered-down rail, and must respect [inhibit](inhibits-hdrm.md) state – including the RF silence period after deployment, which is a launch provider requirement and not a preference.
- **[ADCS](gnc.md) coupling.** Control loops need deterministic timing and consistent sensor timestamps. Sensor data with unknown latency produces control instability that is very hard to diagnose from telemetry.
- **Thermal and EPS feedback.** Heater control loops, load shedding on low battery, and duty-cycling to manage dissipation all live in software but are governed by physics defined elsewhere. See [Thermal](thermal.md) and [EPS](eps.md).
- **Never trust a peripheral to respond.** Every hardware transaction needs a timeout and a defined failure behaviour. A blocking read from a hung I²C device will hang the spacecraft.

## Documentation and Maintainability

University teams turn over on the same timescale as a CubeSat project – see [Systems Engineering – Organisational pitfalls](systems-engineering.md#organisational-pitfalls) – so **bus factor is a design constraint, not a soft concern.**

- **Document interfaces, not implementations.** [ICDs](../references/glossary.md#icd) between subsystems, telemetry and command dictionaries, and the mode state machine are the artefacts that outlive their authors. Code comments explaining *why* age far better than ones explaining *what*.
- **Keep a machine-readable command and telemetry dictionary** – a single source of truth generating both flight and ground code. This eliminates an entire class of desynchronisation bugs and makes ground tooling nearly free.
- **Configuration over code.** Thresholds, limits and timings in a parameter table that can be updated in flight, rather than compiled-in constants. Changing a safe-mode threshold should not require a software upload. The [libparam](https://github.com/spaceinventor/libparam) approach from Space Inventor is one worked example.
- **Version control everything**, including ground scripts, test procedures and configuration. Tag what actually flew.
- **Write the operations handbook while you build**, not the week before launch. Nominal procedures, contingency procedures, and what each telemetry point means – the person on console at 3 a.m. may not be the person who wrote the code.

## Resources

### Open-source Flight Software Projects

<!-- CSR-RESOURCES:START dev-flight-software-open-source-projects -->
- **[NASA Core Flight System (cFS)](https://etd.gsfc.nasa.gov/capabilities/core-flight-system)** `Link` – Layered, flight-proven framework (Core Flight Executive, OSAL, PSP) used on 40+ NASA missions including Roman Space Telescope and Lunar Gateway; runs on Linux, RTEMS, VxWorks and QNX
- **[cFS Basecamp](https://github.com/cfs-tools/cfs-basecamp)** `Link` – Lightweight environment for learning cFS and assembling app-based solutions, with a Python GUI, an app-store-style repository of plug-in cFS apps and integrated tutorials. From the Open STEMware Foundation. A smaller starting point than OpenSatKit – it does not bundle COSMOS or the 42 simulator ([SmallSat Conference paper](https://digitalcommons.usu.edu/smallsat/2023/all2023/46/))
- **[LibreCube Software](https://librecube.gitlab.io/standards/overview/)** `Link` – Open CubeSat components built around space communication standards
- **[OpenSatKit](https://github.com/OpenSatKit/OpenSatKit)** `Link` – Development, education and operations platform wrapping cFS together with Ball Aerospace's COSMOS command-and-control system and Eric Stoneking's 42 spacecraft simulator
- **[PyCubed](https://github.com/pycubed/software)** `Link` – A fully open-source CubeSat avionics and software stack in Python/MicroPython
- **[OreSat](https://github.com/oresat/oresat-c3-software)** `Link` – Modular open-source flight software stack developed by students at Portland State University
- **[Space Inventor stack](https://github.com/spaceinventor/)** `Link` – MIT-licensed libcsp, csh and libparam
<!-- CSR-RESOURCES:END dev-flight-software-open-source-projects -->

### RTOS and Embedded Platforms

<!-- CSR-RESOURCES:START dev-flight-software-rtos -->
- **[FreeRTOS](https://www.freertos.org/)** `Link` – Lightweight, widely used real-time OS for microcontrollers
- **[Zephyr Project](https://zephyrproject.org/)** `Link` – Scalable, secure RTOS with a growing presence in aerospace
- **[RTEMS](https://www.rtems.org/)** `Link` – Real-time OS used in space flight and other high-reliability embedded domains; one of the operating systems supported by NASA's cFS
- **[RIOT OS](https://www.riot-os.org/)** `Link` – Real-time OS for low-power, resource-constrained devices
<!-- CSR-RESOURCES:END dev-flight-software-rtos -->

### Commercial Platforms

<!-- CSR-RESOURCES:START dev-flight-software-commercial -->
- **[Rocket Lab MAX](https://rocketlabcorp.com/space-systems/space-software/)** `Link` – Commercial flight software platform
<!-- CSR-RESOURCES:END dev-flight-software-commercial -->

---

👉 **Please consider [contributing](../contributing.md)!**

[^libcsp]: [LibCSP – The Cubesat Space Protocol](https://libcsp.github.io/libcsp/), official documentation. Describes CSP as a small C protocol stack following the TCP/IP model, with a lightweight header carrying transport and network-layer information, connection-oriented and connectionless operation, ICMP-like ping and buffer status, a QoS router, zero-copy buffers and a thread-safe socket API. MIT licensed; runs on FreeRTOS, Zephyr and Linux over CAN, UDP, USART and ZMQ.

[^spacecan]: LibreCube, [SpaceCAN standard](https://librecube.gitlab.io/standards/spacecan/). A deliberately simplified derivative of ECSS-E-ST-50-15C, defining a nominal and redundant bus pair with one controller and up to 127 responder nodes, using controller heartbeat monitoring for cold redundancy. The rationale given is explicit: the full ECSS CANbus standard is "deemed too complex in terms of implementation and usage" for small spacecraft.

[^power-of-ten]: Gerard J. Holzmann (NASA/JPL Laboratory for Reliable Software), ["The Power of 10: Rules for Developing Safety-Critical Code"](https://spinroot.com/gerard/pdf/P10.pdf), *IEEE Computer*, vol. 39, no. 6, June 2006. Free PDF. Ten rules intended to be checkable by static analysis: simple control flow, fixed loop bounds, no dynamic memory allocation after initialisation, functions short enough to print on one page, a minimum assertion density, smallest possible data scope, checked return values, restricted preprocessor use, restricted pointer use, and compilation with all warnings enabled from day one.

[^fcc-telecommand]: [47 CFR § 97.211 – Space telecommand station](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97/subpart-C/section-97.211). Paragraph (b): "A telecommand station may transmit special codes intended to obscure the meaning of telecommand messages to the station in space operation." Paragraph (c) lists the authorised telecommand segments, including 144–146 MHz, 435–438 MHz, 1260–1270 MHz and 2400–2450 MHz. This is the US rule; other administrations treat telecommand separately from the general prohibition on obscured amateur communications, but the details differ and should be checked against your own licence conditions.