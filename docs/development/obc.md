# Onboard Computing (OBC)

This page covers the onboard computer: microcontrollers, single-board computers and FPGAs and the radiation environment that shapes the choice between them, memory, watchdogs and redundancy, boot and reset behaviour, the buses that link subsystems, and timekeeping. The software the hardware carries is on [Flight Software](flight-software.md).

The governing constraint is that you cannot press the reset button. Every design decision on this page is really an answer to one question: when something goes wrong 500 km up, what brings the spacecraft back?

## Role of the OBC in a CubeSat

The OBC is the spacecraft's decision-maker. It runs the [flight software](flight-software.md), holds the mission state, executes stored and uplinked commands, gathers telemetry, and arbitrates between subsystems that all want power, bus bandwidth and attention at the same time.

### Centralised vs. distributed

- **Centralised.** One processor runs everything: attitude control loops, payload management, comms protocol, housekeeping. Simplest to reason about, cheapest, and the norm on 1U–3U missions. The obvious weakness is that it is a single point of failure, and a busy control loop competing with payload processing creates real-time headaches.
- **Distributed.** Each subsystem carries its own microcontroller and the OBC coordinates. This is what you get by default when you buy COTS boards, since a commercial [EPS](eps.md), radio and [ADCS](../references/glossary.md#adcs) each arrive with firmware already running. Faults are contained naturally, but you now own an inter-processor communication problem, several firmware update paths, and a much harder integration debug.
- **Hybrid** is what most missions actually fly: smart subsystems handling their own real-time work, with a central OBC doing mission management. The design question is not which pattern is better but **where the boundary sits** – which decisions belong to the subsystem and which to the OBC.

### Drawing the boundary

Some useful principles:

- **Safety-critical loops belong close to the hardware.** Battery protection should not depend on the OBC being alive – see [EPS – BMS](eps.md#battery-management-systems-bms).
- **Anything needing hard real-time timing** should not share a processor with a payload that can block for seconds.
- **The OBC should be able to power-cycle every other subsystem**, and something should be able to power-cycle the OBC. See [Boot, Power, and Reset Management](#boot-power-and-reset-management).
- **Interfaces must be documented as [ICDs](../references/glossary.md#icd)** even between two boards built by the same team, because integration is where undocumented assumptions surface.

## The Radiation Environment (and why it shapes everything)

Before comparing processors, it is worth being precise about what space actually does to electronics, because the mitigations dominate OBC architecture.

- **[Total ionising dose](../references/glossary.md#tid) (TID)** is cumulative damage causing gradual parameter drift and eventual failure. NASA defines it as "the ionizing radiation absorbed by the device material over time, causing parametric or functional degradation of the device".[^nasa-soa-avionics] A typical [LEO](../references/glossary.md#leo) CubeSat mission behind normal aluminium shielding accumulates on the order of a few krad(Si) – modest, which is precisely why [COTS](../references/glossary.md#cots) parts are viable. The PyCubed team, for example, established a **10 krad(Si)** threshold for KickSat-2 at 300 km and tested their parts past 35 krad.[^pycubed]
- **[Single-event upsets](../references/glossary.md#seu) (SEU)** are bit flips in memory or registers from a single particle strike – "nondestructive SEEs that can affect the logic state of a memory cell".[^nasa-soa-avionics] Not damaging, but silently corrupting.
- **[Single-event latch-up](../references/glossary.md#sel) (SEL)** creates a destructive low-impedance path – parasitic structures in CMOS logic that produce a high-current state.[^nasa-soa-avionics] Mitigated by current-limited, power-cyclable supply rails – see [EPS – Power Switching and Protection](eps.md#power-switching-and-protection).
- **[Single-event functional interrupt](../references/glossary.md#sefi) (SEFI)** puts a device into a non-functional state that only a reset clears. This is what watchdogs exist for.

The practical consequence: **assume your processor will be corrupted, hang, and reset – repeatedly – over the mission.** Design so that each of those events is survivable and automatically recoverable, rather than trying to prevent them with part selection alone.

## Microcontrollers (MCUs)

For most CubeSats, a microcontroller is the right answer. Low power, deterministic, bootable in milliseconds, and simple enough to reason about completely.

### Common families

- **ARM Cortex-M** dominates. STM32 parts are ubiquitous; the Microchip ATSAMD51 (Cortex-M4) is the PyCubed processor; Cortex-M7 parts appear where more headroom is needed. Huge ecosystems, good toolchains, plenty of community knowledge.
- **TI MSP430** has strong heritage in early CubeSats, chosen for very low power. Still seen, though increasingly displaced.
- **Radiation-hardened MCUs** exist – Vorago's Arm-based rad-hard families, Microchip's SAMRH71, Frontgrade/Cobham's LEON-based devices – and buy you predictable behaviour rather than statistical hope. NASA puts the trade plainly: "COTS components typically offer superior performance, energy efficiency, and affordability compared to their rad-hard alternatives; however COTS devices tend to be highly susceptible to radiation."[^nasa-soa-avionics] The cost of going rad-hard is money, lead time, lower performance for the same generation, and smaller ecosystems.

For scale, NASA's state-of-the-art table (Table 8-4) lists complete avionics products rated at 20 krad, 30 krad and, for the Aitech SP0-S, 100 krad TID – board-level figures rather than the device ratings of the MCUs named above.[^nasa-soa-avionics]

<!-- NEEDS HUMAN VERIFICATION: no cost multiple for rad-hard versus COTS MCUs is quoted because none could be sourced – the NASA avionics survey gives no cost comparison and vendor pricing is quote-only. Device-level TID ratings for the Vorago, SAMRH71 and Frontgrade parts would need the vendors' datasheets; a local copy of any of them would let a figure stand here. -->

### COTS with screening: the CubeSat default

Very few CubeSats fly rad-hard silicon. The prevailing architecture is not simply "COTS instead" but COTS at the core with hardened support around it – NASA describes the default as "COTS components first (e.g., processor and memory), combined with rad-hardened supporting electronics such as ECC, watchdog timers, scrubbing, and redundancy to maximize the benefits of both technologies".[^nasa-soa-avionics] That framing is worth internalising, because it tells you where to spend: not on the processor, but on what watches it.

Alongside that:

- **Test what you fly.** The PyCubed campaign is a good published model: MOSFETs (IRLML5103, IRLML2803) within spec beyond 35 krad, the ATSAMD51 showing flash memory issues from about **16 krad** while power and logic stayed functional past 35 krad.[^pycubed] That is enough evidence to justify a part for a short LEO mission – and it also tells you which failure to expect first.
- **Prefer parts with published heritage.** Somebody else's radiation test report is cheap.
- **Derate.** Run below maximum clock, voltage and temperature ratings.
- **Design for the failure rather than against it.** A part that occasionally upsets, in a system that detects and resets it, is more reliable overall than an expensive part in a system with no recovery path.

### Processor and avionics selection

<!-- CSR-RESOURCES:START dev-obc-mcu-selection -->
- **[NASA State of the Art – Small Spacecraft Avionics](https://www.nasa.gov/wp-content/uploads/2026/05/8-smallsat-avionics-2026-final.pdf)** `PDF` – Chapter 8 of NASA's small spacecraft survey, rewritten in 2026. Covers processor classes, memory technologies, radiation effects and mitigation, onboard AI, and a state-of-the-art table of commercially available avionics with TID ratings
- **[PyCubed: An Open-Source, Radiation-Tested CubeSat Platform](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf)** `PDF` – Documents a full COTS radiation screening campaign, with per-part TID results and the test method used
<!-- CSR-RESOURCES:END dev-obc-mcu-selection -->

## Single-Board Computers (SBCs)

An SBC – a Linux-capable applications processor with hundreds of MB of RAM – is a different class of machine, and brings different problems.

**When it makes sense:** image processing, onboard machine learning, complex payload data reduction, running software that already exists and would be painful to port. If your payload produces more data than you can downlink (see [Comms – Expected Data Rates](comms.md#expected-data-rates)), onboard reduction is often the only way to make the mission work.

**What it costs:**

- **Power.** An SBC running an actual workload draws watts, not milliwatts. Set that against what the bus actually generates: a 1U with body-mounted cells averages 1–2 W across an orbit, and a 3U only a few watts more unless it carries deployables – see [EPS – Solar Power Generation](eps.md#solar-power-generation). On most CubeSats an SBC is therefore a duty-cycled load, not a continuous one.
- **Boot time.** Linux takes seconds to tens of seconds. After an unexpected reset, that is a long time to be unresponsive.
- **Non-determinism.** A general-purpose OS makes no hard real-time guarantees, so control loops should not live here.
- **Filesystem corruption.** Power loss mid-write corrupts filesystems. Use read-only root filesystems, journaling, and treat writable storage as expendable. See [Flight Software – Storage and filesystems](flight-software.md#storage-and-filesystems).
- **Complexity.** More software means more failure modes and a much larger surface you cannot fully test.

**The standard pattern is to pair them:** a small, reliable, always-on MCU owns the spacecraft – power, safe mode, comms, watchdogs – and the SBC is a switchable payload-class resource that can be powered off entirely without endangering the mission. This keeps the thing that must never fail simple, and quarantines the thing that will occasionally misbehave.

## FPGAs and Programmable Logic

FPGAs earn their place where you need deterministic, parallel, high-throughput processing: SDR baseband processing, image compression, sensor interfaces at rates a CPU cannot service, or custom high-speed payload interfaces.

- **Flash-based FPGAs** (Microchip/Microsemi ProASIC3, IGLOO2, PolarFire) hold configuration in non-volatile flash cells, which are far less susceptible to configuration upsets. The usual choice for space.
- **SRAM-based FPGAs** (much of the Xilinx/AMD range) hold configuration in SRAM, which *can* be upset by radiation – a bit flip changes the circuit itself, not just data. Usable, but requires **configuration [scrubbing](../references/glossary.md#scrubbing)**: continuously reading back and correcting the configuration memory.
- **SoC devices** combine hard processor cores with FPGA fabric on one die, and this class is now where much of the market sits – NASA's survey lists multiple vendors offering AMD/Xilinx Zynq and Versal parts that combine "CPUs, GPUs, NPUs, or FPGAs" in a single package.[^nasa-soa-avionics] ESA's OPS-SAT flew an Altera Cyclone V SoC, and is a good illustration of what the class enables.[^opssat]

Mitigation techniques worth knowing:

- **[Triple modular redundancy](../references/glossary.md#tmr) (TMR)** instantiates logic three times and votes on the output, at roughly 3× the resource cost.
- **[EDAC](../references/glossary.md#edac)** on memories detects and corrects single-bit errors and detects double-bit ones.
- **Memory scrubbing** walks through memory periodically, correcting errors before a second upset in the same word makes them uncorrectable.

The counterweight: FPGA development is slow, verification is hard, and the toolchains are unfriendly. For most CubeSats, an FPGA is justified by a specific payload requirement, not by general capability.

## Memory

Choosing memory technology is a design decision in its own right and one that CubeSat teams routinely make by default, which usually means flash for everything. The split NASA draws is between volatile memory for "real-time processing, buffers, and temporary data handling" and non-volatile memory for "telemetry logs, subsystem data, and temporary payload storage".[^nasa-soa-avionics] Within the non-volatile side the technologies are different animals:

- **Flash** – "excels in delivering high-density storage, but has limited write cycles and slower operations".[^nasa-soa-avionics] The right home for payload data, telemetry archives and program images. The wrong home for anything rewritten constantly.
- **FRAM (ferroelectric RAM)** – "offers smaller capacity, yet boasts rapid write speed, low power, and ultra-high endurance – ideal for frequent data logging or sustaining mission-critical parameters".[^nasa-soa-avionics] That description is almost a specification of what this page asks you to keep in non-volatile memory: the boot counter, the reset-cause record, the inhibit and deployment state, the parameter table.
- **MRAM and phase-change memory** – NASA's comparison table gives them on the order of 10¹³ endurance cycles with ten-year retention at 70 °C.[^nasa-soa-avionics] The same use case as FRAM, at larger capacities.
- **EEPROM** – still common for small configuration blocks on COTS boards, and adequate where writes are rare.

The design rule that follows: **match the technology to the write pattern, not to the capacity you happen to need.** A boot counter incremented on every reset, in a spacecraft deliberately designed to reset often, is a wear problem if you put it in flash and a non-problem if you put it in FRAM. Separate the two storage classes physically – small, high-endurance, checksummed memory for state that must survive, and bulk flash for data whose loss costs you science but never the spacecraft.

Whatever the technology, the radiation and power-loss rules still apply: use error detection and correction where the part supports it, keep redundant copies of critical records, and treat every write as potentially interrupted. See [Brownout and reset behaviour](#brownout-and-reset-behaviour) and [Flight Software – Storage and filesystems](flight-software.md#storage-and-filesystems).

## Redundancy and Fault Tolerance

Redundancy at CubeSat scale is a trade, not an automatic good – every redundant element adds mass, power, and the switching mechanism itself becomes a failure point.

- **Cold redundancy**: a second unit, unpowered, switched in on failure. Cheap in power, and the spare is protected from wear and radiation while off. Requires reliable failure detection and switching.
- **Warm/hot redundancy**: both units powered, one active. Faster failover, but double the power and no protection for the spare.
- **Functional redundancy**: no duplicate hardware, but another subsystem can do the job in degraded form – the radio's microcontroller able to run a minimal safe mode, for instance. Often the best value at CubeSat scale.
- **Supervisor architectures**: a very small, very simple watchdog processor whose only job is to monitor the main OBC and reset or power-cycle it. Cheap, effective, and easy to verify precisely because it does almost nothing.

### Watchdogs

A **[watchdog](../references/glossary.md#watchdog)** is the single most important reliability feature on a CubeSat, and worth designing as a hierarchy:

1. **Internal watchdog** in the MCU – catches software hangs, cannot catch a wedged processor.
2. **External watchdog** – a separate timer IC that pulls reset if not petted. Catches more, but not a latched-up power domain.
3. **EPS-level watchdog** – the power system cuts the OBC's rail entirely if it has not heard from it. Catches essentially everything, including latch-up.
4. **Ground-commanded reset** – a last resort that requires the radio to work independently of the OBC.

This hierarchy is not a CubeSat folk practice; it is the mainstream mitigation. NASA lists "watchdog timers, selective power cycling, and software-based fault isolation" as the strategies that improve robustness against single-event effects, and its survey of flight-ready avionics products records radiation-hardened watchdogs as a standard feature.[^nasa-soa-avionics]

Design rules that repay themselves: **pet the watchdog from a task that proves the system is healthy**, not from a timer interrupt that will happily keep running while everything else is deadlocked. And ensure watchdog resets are **counted and telemetered** – a spacecraft quietly resetting every 40 minutes looks fine from the ground until you notice the uptime counter never exceeds 2,400 seconds.

## Boot, Power, and Reset Management

### Power-up sequencing

The order matters. Rails coming up out of sequence can forward-bias protection diodes and latch devices into undefined states. Establish an explicit sequence, implement it in the EPS hardware rather than software, and verify it on the bench with a scope.

The most important case is the **first boot in orbit**: cold, tumbling, and on a battery that has been discharging in a deployer for weeks. See [EPS – Startup and brownout behaviour](eps.md#startup-and-brownout-behaviour), [Inhibits and HDRM](inhibits-hdrm.md) and [Flight Software – The first boot in orbit](flight-software.md#the-first-boot-in-orbit).

### Bootloaders and safe boot

The software side – an immutable **golden image**, boot counting with automatic fallback, and a minimal safe boot path – is covered under [Flight Software – Boot, Reset, and Update Strategy](flight-software.md#boot-reset-and-update-strategy). The hardware's job is to make that design possible:

- **Write-protect the golden image in hardware** where the part allows it – a flash region locked by a fuse or a boot-protection bit, not by a software flag that the same software can clear.
- **Give the boot counter a home built for constant rewriting.** A counter incremented on every reset belongs in FRAM or MRAM, not in the same flash as the application – see [Memory](#memory).
- **Keep a path to the debug port.** A bricked flight computer is recoverable on the bench only if JTAG/SWD is still reachable after the spacecraft is closed up – see [OBC Integration and Testing](#obc-integration-and-testing).

### Brownout and reset behaviour

Brownouts – where supply voltage sags below the operating threshold but not to zero – are more dangerous than clean power cycles, because a processor can execute unpredictably on the way down and corrupt non-volatile memory as it goes.

- Use brownout detection to force a clean reset before the processor misbehaves, and set its threshold above the level at which the non-volatile memory stops writing reliably.
- The software patterns that survive an interrupted write – atomic updates, checksums, redundant copies – are under [Flight Software – Brownouts and partial failures](flight-software.md#brownouts-and-partial-failures).
- **Distinguish reset causes** – power-on, brownout, watchdog, software, external – and telemeter them. It is often the only diagnostic you get.

## Interfaces and Buses

### The bus reliability problem

This deserves emphasis, because it is one of the best-documented CubeSat failure modes. A survey of "60 launched CubeSats and 44 to be launched CubeSats" found I²C the most frequently employed bus, ahead of SPI and RS-232, with CAN then rare but growing – and found that for I²C, "bus lockups appear to be a major issue". Its tally is stark: "I2C has led to a catastrophic failure (proven), while for two more I2C are a likely cause (hypothesis)", the latter including TU Delft's Delfi-C3 and Delfi-n3Xt.[^bouwmeester]

The mechanism: I²C is a shared, open-drain bus with no arbitration recovery built in. A single device that glitches mid-transaction can hold SDA low indefinitely and take down communication for **every** device on the bus. On a spacecraft where that bus links the OBC to the EPS and the radio, that is a mission-ending event.

### Choosing and hardening a bus

- **I²C** – simple, few pins, universally supported. Use it, but harden it: bus recovery routines that clock out stuck devices, timeouts on every transaction, bus multiplexers to segment critical devices, watchdog-triggered power cycling of a hung peripheral, and pull-up sizing that has actually been checked.
- **SPI** – point-to-point with separate chip selects, so a failed device cannot hang the bus. More pins, no addressing, but markedly more robust. Preferred for critical links where pin count allows.
- **UART/RS-232/RS-422/RS-485** – simple, well isolated, good for subsystem-to-subsystem links. RS-422/485 differential signalling is far more noise-immune than single-ended.
- **CAN** – designed for automotive fault tolerance: differential, multi-master, with built-in error detection and automatic fault confinement that removes a misbehaving node from the bus. This is exactly the property I²C lacks, and it is why CAN adoption has grown. See [Flight Software – Inter-Subsystem Communication Protocols](flight-software.md#inter-subsystem-communication-protocols) for the middleware that runs over it.
- **SpaceWire** – high-speed point-to-point standard used on larger spacecraft. Overkill for most CubeSats, but relevant for high-rate payload data.

**Practical rule: do not put your most critical link on your least fault-tolerant bus.** If the OBC↔EPS link fails, the mission is over – so that link deserves the most robust interface, not the most convenient one.

<!-- CSR-RESOURCES:START dev-obc-bus-reliability -->
- **[Survey on the implementation and reliability of CubeSat electrical bus interfaces](https://link.springer.com/article/10.1007/s12567-016-0138-0)** `Link` – Jasper Bouwmeester, Martin Langer and Eberhard Gill (CEAS Space Journal, 2017). Survey of 104 CubeSats with in-orbit failure data by bus type. Open access
- **[Fault Analysis and Mitigation Techniques of the I2C Bus for Nanosatellite Missions](https://ieeexplore.ieee.org/document/10082916/)** `Link` – Detailed treatment of I²C failure modes and mitigations for nanosatellites. Paywalled
<!-- CSR-RESOURCES:END dev-obc-bus-reliability -->

## Timing and Timekeeping

Accurate time matters more than newcomers expect: telemetry is uninterpretable without it, attitude determination needs it to evaluate orbit position and magnetic field models, and payload data is often worthless without an accurate timestamp.

- **Time sources.** The MCU's internal oscillator drifts badly with temperature. A dedicated **RTC with a temperature-compensated crystal** is much better. **[GNSS](../references/glossary.md#gnss)** gives absolute time to sub-microsecond accuracy when a fix is available. Ground stations can uplink time corrections at each pass.
- **Drift.** An uncompensated crystal drifting 20 ppm accumulates about 1.7 seconds per day. Characterise your oscillator against temperature and correct in software.
- **Resets destroy time.** An RTC without a backup supply loses time on every power cycle. Either give it one, or accept that time restarts and design telemetry so it remains interpretable – which means **carrying a monotonic boot counter and uptime alongside wall-clock time**, so events can always be ordered even when absolute time is unknown.
- **Keep the RTC inside the launch rules.** An RTC is the one thing the CDS permits to stay powered through launch, and only within limits – isolated from the main power system, below 320 kHz, current-limited under 10 mA. See [Inhibits and HDRM – Inhibit Interaction with the EPS](inhibits-hdrm.md#inhibit-interaction-with-the-electrical-power-system-eps).
- **Distribution.** Every subsystem timestamping with its own clock produces telemetry that cannot be correlated. Distribute time from one authority, or record the offsets.

See [Flight Software – Timing, Scheduling, and Timekeeping](flight-software.md#timing-scheduling-and-timekeeping).

## Software Stack and OS Choices

- **Bare metal** – a main loop plus interrupts, no scheduler. Completely deterministic and fully comprehensible, which is a reliability advantage in itself. Gets unwieldy as concurrent activities multiply.
- **[RTOS](../references/glossary.md#rtos)** – FreeRTOS, Zephyr, RTEMS. Pre-emptive scheduling with priorities and real-time guarantees, at the cost of needing to reason about priority inversion, stack sizing and race conditions. The mainstream CubeSat choice above trivial complexity. RTEMS in particular has substantial spaceflight heritage.
- **Linux** – only on an SBC, and generally for payload-class work rather than spacecraft control.

Whatever you choose, a **hardware abstraction layer** separating drivers from application logic is worth the effort: it lets you run the same flight software on a host machine for testing, which is the single biggest multiplier on software quality. See [Flight Software](flight-software.md) and [AIT – Software Testing](ait.md#software-testing-and-validation).

### Middleware and open stacks

<!-- CSR-RESOURCES:START dev-obc-open-software-stacks -->
- **[Space Inventor open-source stack](https://github.com/spaceinventor/)** `Link` – libcsp (CubeSat Space Protocol), csh (command shell) and libparam (parameter system), MIT-licensed
- **[NASA Core Flight System (cFS)](https://etd.gsfc.nasa.gov/capabilities/core-flight-system)** `Link` – Modular, flight-proven flight software framework
- **[PyCubed software](https://github.com/pycubed/software)** `Link` – CircuitPython-based avionics stack for the PyCubed board
<!-- CSR-RESOURCES:END dev-obc-open-software-stacks -->

## Advanced and Emerging Computing Concepts

Onboard processing has moved from research to demonstrated capability, driven by the same bottleneck every time: **you can collect far more data than you can downlink.** NASA's avionics survey frames it as a change of kind rather than degree – "this shift from basic data logging to autonomous decision-making is driving the adoption of edge computing, Machine Learning (ML), and Artificial Intelligence (AI)" – and its state-of-the-art table now lists commercially available CubeSat avionics built around NVIDIA Jetson Orin and Xavier NX modules and AMD/Xilinx Zynq and Versal SoCs.[^nasa-soa-avionics]

- **PhiSat-1** (6U, launched 3 September 2020) flew an Intel Movidius Myriad 2 vision processing unit – a COTS part radiation-tested at CERN in off-the-shelf form – running a cloud-detection neural network on hyperspectral imagery. Discarding cloudy scenes onboard saved "about 30% of bandwidth", and ESA described it as the first satellite to demonstrate the use of artificial intelligence in orbit.[^phisat1]
- **PhiSat-2** (6U, Open Cosmos, launched 16 August 2024) carries the model further: multiple AI applications – cloud detection, street-map generation, vessel detection, image compression – installed and operated remotely, with further apps uploaded after launch rather than baked in before it.[^phisat2] That is the interesting part, not the inference itself.
- **OPS-SAT** (3U, ESA, launched 18 December 2019, end of life 22 May 2024) existed to let experimenters run software on a platform ESA described as "10 times more powerful than any other preceding ESA satellite". It was designed for an S-band uplink of at least 256 kbit/s and for "a complete reload of the entire software in less than 3 passes".[^opssat] It is the clearest demonstration that the barrier to onboard autonomy has been operational caution rather than available compute.

The current limitations are practical ones: power (an inference accelerator running continuously will dominate a CubeSat budget), thermal (see [Thermal](thermal.md)), radiation tolerance of accelerators, and the difficulty of validating a model whose behaviour you cannot exhaustively test. The pragmatic pattern today is **duty-cycled inference on a switchable processor**, with the [spacecraft bus](../references/glossary.md#bus-spacecraft) kept firmly under the control of something simple.

## OBC Integration and Testing

- **Flatsat first.** Lay every board out on a bench, connected as flown but accessible, and bring the system up incrementally. See [AIT – Flatsat and Integration Test Setups](ait.md#flatsat-and-integration-test-setups).
- **Keep a debug path** – JTAG/SWD headers, a serial console, test points on every bus. You will need them long after the spacecraft is closed up, so plan physical access early. See [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **EMI and signal integrity.** A CubeSat is a dense stack of switching converters a few centimetres from a sensitive receiver. Keep high-speed digital away from RF and analogue, mind return paths, and test with the radio actually running – self-interference is common and easiest to find on a [flatsat](../references/glossary.md#flatsat).
- **Test the failure paths, not just the functions.** Yank power mid-write. Hold the I²C bus low. Corrupt a firmware image. Let the watchdog fire. These are the behaviours that decide whether the mission survives, and they are the ones that never get exercised by nominal testing.
- **Hardware-in-the-loop** lets you drive the OBC with simulated sensor data and orbital dynamics, which is the only practical way to exercise mode logic across many orbits. See [AIT – HIL Testing](ait.md#hardware-in-the-loop-hil-testing).

### Common integration pitfalls

- I²C address collisions between COTS boards that each assumed they were alone on the bus.
- Pull-up resistors fitted on several boards at once, so the effective bus pull-up is far too strong.
- A ground loop between subsystems producing intermittent, temperature-dependent faults that appear only in TVAC.
- Firmware update procedures that were never tested through the flight comms path, only over a bench cable.
- No way to recover a subsystem that boots into a bad state, because nothing can power-cycle it independently.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-avionics]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 8: Small Spacecraft Avionics](https://www.nasa.gov/wp-content/uploads/2026/05/8-smallsat-avionics-2026-final.pdf) (May 2026 edition, NASA/TP-20260003140; the chapter was formerly titled Command and Data Handling and was rewritten for this edition). Open access. Source for the TID and single-event-effect definitions, the COTS-versus-rad-hard trade and the "COTS first with rad-hardened supporting electronics" default, the memory technology comparison in Table 8-1 (flash density versus write endurance, FRAM endurance and write speed, MRAM and phase-change endurance and retention), the mitigation strategies list, and the state-of-the-art avionics products in Table 8-4 including their TID ratings and AI accelerator hardware.

[^pycubed]: Maximillian Holliday et al., ["PyCubed: An Open-Source, Radiation-Tested CubeSat Platform Programmable Entirely in Python"](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf), *33rd Annual AIAA/USU Conference on Small Satellites*, SSC19-WKIII-04, 2019. Free PDF. Establishes a conservative 10 krad(Si) TID threshold for KickSat-2 at 300 km and reports per-part results, including the IRLML5103 and IRLML2803 MOSFETs within spec beyond 35 krad and flash memory issues in the ATSAMD51 from around 16 krad with power and logic functional beyond 35 krad. Testing used a Shepherd Mark 1 gamma irradiator at 662 keV photon energy per MIL-STD-883 method 1019.8 – worth noting, since "radiation tested" means little without the source and method.

[^bouwmeester]: Jasper Bouwmeester, Martin Langer and Eberhard Gill, ["Survey on the implementation and reliability of CubeSat electrical bus interfaces"](https://link.springer.com/article/10.1007/s12567-016-0138-0), *CEAS Space Journal*, 9(2), 163–173, 2017. Open access. Surveys 60 launched and 44 to-be-launched CubeSats, finds I²C the most frequently employed bus and that "bus lockups appear to be a major issue", and reports one proven catastrophic I²C failure with two further cases where I²C is the likely cause, naming Delfi-C3 and Delfi-n3Xt.

[^opssat]: ESA, [OPS-SAT mission page (eoPortal)](https://www.eoportal.org/satellite-missions/ops-sat). 3U CubeSat launched 18 December 2019, end of life 22 May 2024, built around an Altera Cyclone V SoC. The processing platform is described as "10 times more powerful than any other preceding ESA satellite". Note that the 500+ MHz, 500 MB RAM and 10 GB storage figures widely quoted for OPS-SAT appear in this source as mission *requirements* rather than confirmed as-built specifications, as does the "complete reload of the entire software in less than 3 passes" target; they are presented here as design intent for that reason.

[^phisat1]: ESA / eoPortal, [PhiSat-1 mission page](https://www.eoportal.org/satellite-missions/phisat-1). 6U CubeSat launched 3 September 2020 on the Vega SSMS proof-of-concept flight as part of FSSCat, carrying an Intel Movidius Myriad 2 VPU tested at CERN in late 2018 and passing "in off-the-shelf form, no modifications needed". Onboard cloud filtering saved "about 30% of bandwidth". ESA describes it as "the first satellite to demonstrate the use of artificial intelligence in orbit"; note that this is ESA's framing of its own mission, and earlier missions demonstrated other forms of onboard autonomy.

[^phisat2]: ESA, [*New satellite demonstrates the power of AI for Earth observation*](https://www.esa.int/Applications/Observing_the_Earth/Phsat-2/New_satellite_demonstrates_the_power_of_AI_for_Earth_observation). Φsat-2 launched 16 August 2024 on a Falcon 9 from Vandenberg Space Force Base, on a 6U platform designed and developed by Open Cosmos, carrying "AI apps that can be easily installed and operated remotely from Earth" covering cloud detection, street map generation, maritime vessel detection and image compression, with further apps uploaded after the satellite reached orbit. ESA does not name the processor in this release.