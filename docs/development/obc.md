# Onboard Computing (OBC)

This section covers onboard computing elements for CubeSats, including MCUs, FPGAs, and SBCs. Topics include architecture choices, redundancy strategies, power and boot sequencing, fault tolerance, real-time vs. high-level OS tradeoffs, and interfacing with payloads and subsystems. Compute selection and integration strongly influence system reliability, power budget, and software complexity.

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

- **[Total ionising dose](../references/glossary.md#tid) (TID)** is cumulative damage causing gradual parameter drift and eventual failure. A typical [LEO](../references/glossary.md#leo) CubeSat mission behind normal aluminium shielding accumulates on the order of a few krad(Si) — modest, which is precisely why [COTS](../references/glossary.md#cots) parts are viable. The PyCubed team, for example, established a **10 krad(Si)** threshold for a 300 km mission and tested their parts past 35 krad.[^pycubed-obc]
- **[Single-event upsets](../references/glossary.md#seu) (SEU)** are bit flips in memory or registers from a single particle strike. Not damaging, but silently corrupting.
- **[Single-event latch-up](../references/glossary.md#sel) (SEL)** creates a destructive low-impedance path. Mitigated by current-limited, power-cyclable supply rails — see [EPS – Power Switching and Protection](eps.md#power-switching-and-protection).
- **[Single-event functional interrupt](../references/glossary.md#sefi) (SEFI)** puts a device into a non-functional state that only a reset clears. This is what watchdogs exist for.

The practical consequence: **assume your processor will be corrupted, hang, and reset — repeatedly — over the mission.** Design so that each of those events is survivable and automatically recoverable, rather than trying to prevent them with part selection alone.

## Microcontrollers (MCUs)

For most CubeSats, a microcontroller is the right answer. Low power, deterministic, bootable in milliseconds, and simple enough to reason about completely.

### Common families

- **ARM Cortex-M** dominates. STM32 parts are ubiquitous; the Microchip ATSAMD51 (Cortex-M4) is the PyCubed processor; Cortex-M7 parts appear where more headroom is needed. Huge ecosystems, good toolchains, plenty of community knowledge.
- **TI MSP430** has strong heritage in early CubeSats, chosen for very low power. Still seen, though increasingly displaced.
- **Radiation-hardened MCUs** exist — Vorago's Arm-based rad-hard families, Microchip's SAMRH71, Frontgrade/Cobham's LEON-based devices — and buy you predictable behaviour rather than statistical hope. The tradeoff is cost (often 100× a COTS part), lead time, lower performance for the same generation, and smaller ecosystems.
<!-- NEEDS HUMAN VERIFICATION: The rad-hard part families named here (Vorago VA-series, Microchip SAMRH71, Frontgrade LEON devices) are real products, but I could not pull TID or SEL immunity figures from vendor pages, so I have deliberately not quoted any numbers. If you want specifics, they need to come from the datasheets. -->

### COTS with screening: the CubeSat default

Very few CubeSats fly rad-hard silicon. The prevailing approach is to select COTS parts and manage the risk:

- **Test what you fly.** The PyCubed campaign is a good published model: MOSFETs (IRLML5103, IRLML2803) tested beyond 35 krad, the ATSAMD51 showing flash memory issues from about **16 krad** while power and logic stayed functional past 35 krad.[^pycubed-obc] That is enough evidence to justify a part for a short LEO mission — and it also tells you which failure to expect first.
- **Prefer parts with published heritage.** Somebody else's radiation test report is cheap.
- **Derate.** Run below maximum clock, voltage and temperature ratings.
- **Design for the failure rather than against it.** A part that occasionally upsets, in a system that detects and resets it, is more reliable overall than an expensive part in a system with no recovery path.

### Resources

<!-- CSR-RESOURCES:START dev-obc-mcu-selection -->
- **[Hubble: CubeSat vs SmallSat vs Microsatellite: Satellite Sizes and the Chips Inside Them](https://hubble.com/community/comparisons/cubesat-vs-smallsat-vs-microsatellite-satellite-sizes-and-the-chips-inside-them/)** `Link` – Overview of satellite size classes and the processors typically used in each
- **[PyCubed: An Open-Source, Radiation-Tested CubeSat Platform](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf)** `PDF` – Documents a full COTS radiation screening campaign, with per-part TID results
<!-- CSR-RESOURCES:END dev-obc-mcu-selection -->

## Single-Board Computers (SBCs)

An SBC — a Linux-capable applications processor with hundreds of MB of RAM — is a different class of machine, and brings different problems.

**When it makes sense:** image processing, onboard machine learning, complex payload data reduction, running software that already exists and would be painful to port. If your payload produces more data than you can downlink (see [Comms – Expected Data Rates](comms.md#expected-data-rates)), onboard reduction is often the only way to make the mission work.

**What it costs:**

- **Power.** An SBC running a real workload draws watts, not milliwatts. On a 3U generating 5–8 W orbit-average, that is a large fraction of the budget and usually means duty cycling.
- **Boot time.** Linux takes seconds to tens of seconds. After an unexpected reset, that is a long time to be unresponsive.
- **Non-determinism.** A general-purpose OS makes no hard real-time guarantees, so control loops should not live here.
- **Filesystem corruption.** Power loss mid-write corrupts filesystems. Use read-only root filesystems, journaling, and treat writable storage as expendable.
- **Complexity.** More software means more failure modes and a much larger surface you cannot fully test.

**The standard pattern is to pair them:** a small, reliable, always-on MCU owns the spacecraft — power, safe mode, comms, watchdogs — and the SBC is a switchable payload-class resource that can be powered off entirely without endangering the mission. This keeps the thing that must never fail simple, and quarantines the thing that will occasionally misbehave.

## FPGAs and Programmable Logic

FPGAs earn their place where you need deterministic, parallel, high-throughput processing: SDR baseband processing, image compression, sensor interfaces at rates a CPU cannot service, or custom high-speed payload interfaces.

- **Flash-based FPGAs** (Microchip/Microsemi ProASIC3, IGLOO2, PolarFire) hold configuration in non-volatile flash cells, which are far less susceptible to configuration upsets. The usual choice for space.
- **SRAM-based FPGAs** (much of the Xilinx/AMD range) hold configuration in SRAM, which *can* be upset by radiation — a bit flip changes the circuit itself, not just data. Usable, but requires **configuration [scrubbing](../references/glossary.md#scrubbing)**: continuously reading back and correcting the configuration memory.
- **SoC devices** combine hard ARM cores with FPGA fabric on one die. OPS-SAT's Altera Cyclone V SoC — dual ARM-9 cores above 500 MHz, 500 MB RAM and 10 GB storage — is a good example of what this class enables.[^opssat]

Mitigation techniques worth knowing:

- **[Triple modular redundancy](../references/glossary.md#tmr) (TMR)** instantiates logic three times and votes on the output, at roughly 3× the resource cost.
- **[EDAC](../references/glossary.md#edac)** on memories detects and corrects single-bit errors and detects double-bit ones.
- **Memory scrubbing** walks through memory periodically, correcting errors before a second upset in the same word makes them uncorrectable.

The honest counterweight: FPGA development is slow, verification is hard, and the toolchains are unfriendly. For most CubeSats, an FPGA is justified by a specific payload requirement, not by general capability.

## Redundancy and Fault Tolerance

Redundancy at CubeSat scale is a genuine trade, not an automatic good — every redundant element adds mass, power, and the switching mechanism itself becomes a failure point.

- **Cold redundancy**: a second unit, unpowered, switched in on failure. Cheap in power, and the spare is protected from wear and radiation while off. Requires reliable failure detection and switching.
- **Warm/hot redundancy**: both units powered, one active. Faster failover, but double the power and no protection for the spare.
- **Functional redundancy**: no duplicate hardware, but another subsystem can do the job in degraded form — the radio's microcontroller able to run a minimal safe mode, for instance. Often the best value at CubeSat scale.
- **Supervisor architectures**: a very small, very simple watchdog processor whose only job is to monitor the main OBC and reset or power-cycle it. Cheap, effective, and easy to verify precisely because it does almost nothing.

### Watchdogs

A **[watchdog](../references/glossary.md#watchdog)** is the single most important reliability feature on a CubeSat, and worth designing as a hierarchy:

1. **Internal watchdog** in the MCU — catches software hangs, cannot catch a wedged processor.
2. **External watchdog** — a separate timer IC that pulls reset if not kicked. Catches more, but not a latched-up power domain.
3. **EPS-level watchdog** — the power system cuts the OBC's rail entirely if it has not heard from it. Catches essentially everything, including latch-up.
4. **Ground-commanded reset** — a last resort that requires the radio to work independently of the OBC.

Design rules that repay themselves: **kick the watchdog from a task that proves the system is healthy**, not from a timer interrupt that will happily keep running while everything else is deadlocked. And ensure watchdog resets are **counted and telemetered** — a spacecraft quietly resetting every 40 minutes looks fine from the ground until you notice the uptime counter never exceeds 2,400 seconds.

## Boot, Power, and Reset Management

### Power-up sequencing

The order matters. Rails coming up out of sequence can forward-bias protection diodes and latch devices into undefined states. Establish an explicit sequence, implement it in the EPS hardware rather than software, and verify it on the bench with a scope.

The most important case is the **first boot in orbit**: cold, tumbling, and on a battery that has been discharging in a deployer for weeks. See [EPS – Startup and brownout behaviour](eps.md#startup-and-brownout-behaviour) and [Inhibits and HDRM](inhibits-hdrm.md).

### Bootloaders and safe boot

- **A bootloader that can be updated is a bootloader that can be bricked.** The standard answer is an immutable **golden image** in write-protected memory that always boots to a minimal state capable of receiving commands, plus a separate updatable application image.
- **Boot counting.** Increment a counter in non-volatile memory on each boot, and reset it once the system has been stable for a while. If it exceeds a threshold, fall back to the golden image. This turns a boot loop from a mission-ender into a recoverable event.
- **Minimal safe boot path** should bring up only what is needed to charge the battery, keep warm, and listen for commands.

### Brownout and reset behaviour

Brownouts — where supply voltage sags below the operating threshold but not to zero — are more dangerous than clean power cycles, because a processor can execute unpredictably on the way down and corrupt non-volatile memory as it goes.

- Use brownout detection to force a clean reset before the processor misbehaves.
- Treat every write to non-volatile memory as potentially interrupted: use atomic update patterns, checksums, and redundant copies.
- **Distinguish reset causes** — power-on, brownout, watchdog, software, external — and telemeter them. It is often the only diagnostic you get.

## Interfaces and Buses

### The bus reliability problem

This deserves emphasis, because it is one of the best-documented CubeSat failure modes. A survey of 60 launched and 44 in-development CubeSats found **I²C the most widely implemented bus**, ahead of SPI and RS-232, with CAN then rare but growing — and found that for I²C, "bus lockups appear to be a major issue", with one confirmed catastrophic mission failure and two further probable cases, including Delfi-C3 and Delfi-n3Xt.[^bouwmeester]

The mechanism: I²C is a shared, open-drain bus with no arbitration recovery built in. A single device that glitches mid-transaction can hold SDA low indefinitely and take down communication for **every** device on the bus. On a spacecraft where that bus links the OBC to the EPS and the radio, that is a mission-ending event.

### Choosing and hardening a bus

- **I²C** — simple, few pins, universally supported. Use it, but harden it: bus recovery routines that clock out stuck devices, timeouts on every transaction, bus multiplexers to segment critical devices, watchdog-triggered power cycling of a hung peripheral, and pull-up sizing that has actually been checked.
- **SPI** — point-to-point with separate chip selects, so a failed device cannot hang the bus. More pins, no addressing, but markedly more robust. Preferred for critical links where pin count allows.
- **UART/RS-232/RS-422/RS-485** — simple, well isolated, good for subsystem-to-subsystem links. RS-422/485 differential signalling is far more noise-immune than single-ended.
- **CAN** — designed for automotive fault tolerance: differential, multi-master, with built-in error detection and automatic fault confinement that removes a misbehaving node from the bus. This is exactly the property I²C lacks, and it is why CAN adoption has grown.
- **SpaceWire** — high-speed point-to-point standard used on larger spacecraft. Overkill for most CubeSats, but relevant for high-rate payload data.

**Practical rule: do not put your most critical link on your least fault-tolerant bus.** If the OBC↔EPS link fails, the mission is over — so that link deserves the most robust interface, not the most convenient one.

<!-- CSR-RESOURCES:START dev-obc-bus-reliability -->
- **[Survey on the implementation and reliability of CubeSat electrical bus interfaces](https://link.springer.com/article/10.1007/s12567-016-0138-0)** `Link` – Bouwmeester, Langer & Gill (CEAS Space Journal, 2017). Open-access survey of 104 CubeSats with in-orbit failure data by bus type
- **[Fault Analysis and Mitigation Techniques of the I2C Bus for Nanosatellite Missions](https://ieeexplore.ieee.org/document/10082916/)** `Link` – Detailed treatment of I²C failure modes and mitigations for nanosatellites
<!-- CSR-RESOURCES:END dev-obc-bus-reliability -->

## Timing and Timekeeping

Accurate time matters more than newcomers expect: telemetry is uninterpretable without it, attitude determination needs it to evaluate orbit position and magnetic field models, and payload data is often worthless without an accurate timestamp.

- **Time sources.** The MCU's internal oscillator drifts badly with temperature. A dedicated **RTC with a temperature-compensated crystal** is much better. **[GNSS](../references/glossary.md#gnss)** gives absolute time to sub-microsecond accuracy when a fix is available. Ground stations can uplink time corrections at each pass.
- **Drift.** An uncompensated crystal drifting 20 ppm accumulates about 1.7 seconds per day. Characterise your oscillator against temperature and correct in software.
- **Resets destroy time.** An RTC without a backup supply loses time on every power cycle. Either give it one, or accept that time restarts and design telemetry so it remains interpretable — which means **carrying a monotonic boot counter and uptime alongside wall-clock time**, so events can always be ordered even when absolute time is unknown.
- **Distribution.** Every subsystem timestamping with its own clock produces telemetry that cannot be correlated. Distribute time from one authority, or record the offsets.

See [Flight Software – Timing, Scheduling, and Timekeeping](flight-software.md#timing-scheduling-and-timekeeping).

## Software Stack and OS Choices

- **Bare metal** — a main loop plus interrupts, no scheduler. Completely deterministic and fully comprehensible, which is a real reliability advantage. Gets unwieldy as concurrent activities multiply.
- **[RTOS](../references/glossary.md#rtos)** — FreeRTOS, Zephyr, RTEMS. Pre-emptive scheduling with priorities and real-time guarantees, at the cost of needing to reason about priority inversion, stack sizing and race conditions. The mainstream CubeSat choice above trivial complexity. RTEMS in particular has substantial spaceflight heritage.
- **Linux** — only on an SBC, and generally for payload-class work rather than spacecraft control.

Whatever you choose, a **hardware abstraction layer** separating drivers from application logic is worth the effort: it lets you run the same flight software on a host machine for testing, which is the single biggest multiplier on software quality. See [Flight Software](flight-software.md) and [AIT – Software Testing](ait.md#software-testing-and-validation).

### Middleware and open stacks

<!-- CSR-RESOURCES:START dev-obc-open-software-stacks -->
- **[Space Inventor open-source stack](https://github.com/spaceinventor/)** `Link` – libcsp (CubeSat Space Protocol), csh (command shell) and libparam (parameter system), MIT-licensed
- **[NASA Core Flight System (cFS)](https://cfs.gsfc.nasa.gov/)** `Link` – Modular, flight-proven flight software framework
- **[PyCubed software](https://github.com/pycubed/software)** `Link` – CircuitPython-based avionics stack for the PyCubed board
<!-- CSR-RESOURCES:END dev-obc-open-software-stacks -->

## Advanced and Emerging Computing Concepts

Onboard processing has moved from research to demonstrated capability, driven by the same bottleneck every time: **you can collect far more data than you can downlink.**

- **PhiSat-1** (6U, launched September 2020) flew an Intel Movidius Myriad 2 vision processing unit — a COTS part radiation-tested at CERN — running a cloud-detection neural network on hyperspectral imagery. By discarding cloudy scenes onboard, it cut downlink volume by roughly **30%** and claimed the first hardware-accelerated AI inference of Earth observation imagery in orbit.[^phisat]
- **PhiSat-2** carries the same processor with a framework allowing AI applications to be deployed and updated in orbit without restarting the system.[^phisat]
- **OPS-SAT** (3U, ESA, 2019–2024) existed to let experimenters run software on a platform ESA described as ten times more powerful than any preceding ESA satellite, with 256 kbit/s uplink enabling a full software reload in under three passes.[^opssat] It is the clearest demonstration that the barrier to onboard autonomy has been operational caution rather than available compute.

Current limitations are honest ones: power (an inference accelerator running continuously will dominate a CubeSat budget), thermal (see [Thermal](thermal.md)), radiation tolerance of accelerators, and the difficulty of validating a model whose behaviour you cannot exhaustively test. The pragmatic pattern today is **duty-cycled inference on a switchable processor**, with the [spacecraft bus](../references/glossary.md#bus-spacecraft) kept firmly under the control of something simple.

## OBC Integration and Testing

- **Flatsat first.** Lay every board out on a bench, connected as flown but accessible, and bring the system up incrementally. See [AIT – Flatsat and Integration Test Setups](ait.md#flatsat-and-integration-test-setups).
- **Keep a debug path** — JTAG/SWD headers, a serial console, test points on every bus. You will need them long after the spacecraft is closed up, so plan physical access early. See [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **EMI and signal integrity.** A CubeSat is a dense stack of switching converters a few centimetres from a sensitive receiver. Keep high-speed digital away from RF and analogue, mind return paths, and test with the radio actually running — self-interference is common and easiest to find on a [flatsat](../references/glossary.md#flatsat).
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

[^pycubed-obc]: Maximillian Holliday et al., ["PyCubed: An Open-Source, Radiation-Tested CubeSat Platform Programmable Entirely in Python"](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf), *33rd Annual AIAA/USU Conference on Small Satellites*, SSC19-WKIII-04, 2019. Establishes a 10 krad(Si) TID threshold for a 300 km LEO mission and reports per-part results, including flash memory issues in the ATSAMD51 from around 16 krad with power and logic functional beyond 35 krad.

[^bouwmeester]: Jasper Bouwmeester, Martin Langer and Eberhard Gill, ["Survey on the implementation and reliability of CubeSat electrical bus interfaces"](https://link.springer.com/article/10.1007/s12567-016-0138-0), *CEAS Space Journal*, 9(2), 163–173, 2017. Open access. Surveys 60 launched and 44 in-development CubeSats, finding I²C the most implemented data bus and bus lockups a major in-orbit issue, with one confirmed catastrophic failure and two probable cases.

[^opssat]: ESA, [OPS-SAT mission page (eoPortal)](https://www.eoportal.org/satellite-missions/ops-sat). 3U CubeSat launched 18 December 2019, operated until May 2024, built around an Altera Cyclone V SoC with dual ARM-9 cores above 500 MHz, 500 MB RAM and 10 GB storage — described by ESA as ten times more powerful than any preceding ESA satellite.

[^phisat]: ESA / eoPortal, [PhiSat-1 mission page](https://www.eoportal.org/satellite-missions/phisat-1). 6U CubeSat launched 3 September 2020 as part of FSSCat, carrying an Intel Movidius Myriad 2 VPU radiation-tested at CERN, running onboard cloud detection that reduced downlinked data volume by roughly 30%.
