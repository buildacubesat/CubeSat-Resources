# Payload

The payload is the purpose of the mission – whether it's a sensor, imager, experiment, or technology demo. This section covers payload subsystems, with a focus on single-board computers (SBCs) often used for data collection and processing. It also includes topics like mechanical mounting, electrical interfacing, and resource constraints such as power and data throughput.

Everything else on this site describes a *bus* — the machinery that keeps a spacecraft alive. The payload is the reason the bus exists. That relationship should shape how you design: the payload's needs generate the bus requirements, not the other way round. Teams that pick a bus first and then discover what their payload actually needs tend to spend the rest of the project negotiating with their own earlier decisions.

## What Constitutes a Payload

A payload is anything aboard that serves the mission objective rather than the spacecraft's own survival. The distinction is functional rather than physical: the same camera is a payload on an imaging mission and a bus component on a mission that uses it for star tracking.

### Primary vs. secondary payloads

- **Primary payload** — the reason the mission exists. Its requirements dominate the design and drive orbit selection, pointing, power and data budgets.
- **Secondary payloads** — additional experiments carried because there is room. Common on university missions, where flying three student experiments on one bus multiplies the educational return.

Secondary payloads are worth carrying but need explicit rules. Define upfront how resources are allocated when they conflict, and make sure a secondary payload cannot compromise the primary mission or the bus — which in practice means it should be on its own switchable power channel and unable to hang a shared bus. See [OBC – Interfaces and Buses](obc.md#interfaces-and-buses).

### Mission categories

- **Science** — measuring something about the universe. Tight requirements on calibration, pointing knowledge and data integrity, because the data must be defensible to other scientists.
- **Technology demonstration** — proving that a component or technique works in space, usually to raise its [TRL](../references/glossary.md#trl). Often the most forgiving category: the payload failing in an informative way is still a useful result.
- **Commercial** — Earth observation, IoT relay, RF sensing. Driven by data quality, revisit rate and unit economics rather than novelty.
- **Educational** — where the learning is the objective, and the payload's job is partly to be instructive to build.

Being honest about which of these you are doing is genuinely useful, because it sets how much rigour a given requirement deserves. A technology demonstrator that spends a year on radiometric calibration has misallocated its effort.

### Active and passive payloads

Not every payload draws power. Materials exposure experiments, retroreflectors for laser ranging, passive drag devices and deployed structures all count as payloads while presenting almost no electrical interface — but they still consume mass, volume, external surface area and, in the case of deployables, a release mechanism and its associated [inhibits](inhibits-hdrm.md).

## Common Payload Types

### Imaging

By far the most common CubeSat payload, and the one that most strongly stresses the rest of the bus.

- **Visible-light cameras** — from a COTS image sensor with a small lens up to diffraction-limited telescopes. Ground sample distance is set by aperture, focal length and altitude; the physics is unforgiving, and a 1U cannot carry an aperture large enough for sub-metre imaging regardless of how good the sensor is.
- **Multispectral** — a handful of discrete bands chosen for a specific application (vegetation indices, water quality, fire detection). Modest data volumes, well-understood processing.
- **[Hyperspectral](../references/glossary.md#hyperspectral-imaging)** — hundreds of contiguous narrow bands, producing a spectrum per pixel. Scientifically rich and a data-volume problem: a single hyperspectral scene can exceed an entire day's [downlink](../references/glossary.md#downlink-uplink) capacity, which is exactly why onboard processing has become interesting. See [Data reduction](#data-reduction-and-compression).
- **Thermal infrared** — often requires a cooled detector, which brings a [cryocooler](thermal.md#other-active-techniques) and a large power and thermal problem with it.

Imaging payloads drive pointing requirements ([GNC](gnc.md#guidance)), stability requirements (wheel jitter blurs images), thermal stability (focus shifts with temperature), and downlink ([Comms](comms.md#expected-data-rates)). They are the classic case where the payload's needs cascade into every other subsystem.

### Scientific instruments

Particle detectors, magnetometers, spectrometers, radiation monitors, dosimeters, GNSS radio occultation receivers.

A good worked example is EIRSAT-1's **GMOD** gamma-ray detector: a compact 25 × 25 × 40 mm cerium bromide scintillator coupled to a 4×4 tiled array of silicon photomultipliers with custom front-end electronics, achieving an energy resolution of **5.4% at 662 keV** in ground testing with radioactive sources.[^eirsat-gmod] The design was explicitly made so that "the electronic and mechanical interfaces are compatible with many off-the-shelf CubeSat systems and structures" — a good instinct, and one that makes the difference between an instrument that flies and one that stays in a lab.

Science payloads typically need the tightest calibration, and often need magnetic or electromagnetic cleanliness from the whole spacecraft rather than just from themselves.

### Communications payloads

AIS ship tracking, ADS-B aircraft tracking, IoT data relay, store-and-forward messaging, amateur radio transponders, RF spectrum monitoring. These blur the line between payload and bus, since they use similar hardware to the [comms](comms.md) subsystem but serve the mission rather than housekeeping. Watch for self-interference: a receive payload and a transmit bus radio on the same small spacecraft will find each other.

### Technology demonstration

Propulsion units, deployable structures, new solar cells, novel avionics, in-orbit demonstration of components a vendor wants to sell with [flight heritage](../references/glossary.md#flight-heritage). Often the payload *is* a bus component being tested, which makes the boundary interestingly circular.

### Biological and materials payloads

Materials exposure racks, radiation-effects experiments, and biological experiments. Biological payloads are unusual in demanding tight thermal control (often actively heated), sometimes pressure containment, and a hard deadline — the science degrades whether or not the spacecraft is ready.

## Payload Computing and Data Handling

### When the payload needs its own computer

Separating payload compute from the [OBC](obc.md) is usually right when:

- The payload generates data faster than the OBC can handle.
- It needs an operating system, libraries or frameworks unsuitable for the flight computer.
- Its processing is bursty and would disrupt the OBC's real-time behaviour.
- It comes as a sealed unit from a supplier, which is common.
- You want the freedom to develop and update payload software without touching flight-critical code.

The countervailing argument is that a second computer means more power, mass, integration effort and failure modes. On a simple 1U with a low-rate sensor, letting the OBC read it directly is the right answer.

The prevailing pattern mirrors the one described under [OBC – Single-Board Computers](obc.md#single-board-computers-sbcs): **a simple, always-on OBC owns the spacecraft, and a more capable payload processor is a switchable resource that can be powered off entirely without endangering the mission.** This keeps the mission-critical software small and the experimental software quarantined.

### Data reduction and compression

The fundamental asymmetry of a CubeSat mission is that **collection is cheap and downlink is not**. At 9600 bps over four eight-minute passes you have on the order of 2 MB per day before overhead. A single 12-bit 2048×2048 image is 6 MB. The arithmetic forces a decision, and there are only four levers:

1. **Collect less** — duty-cycle the payload, target specific areas, trigger on conditions.
2. **Compress** — lossless where the science demands it, lossy where it does not.
3. **Reduce onboard** — extract the derived product rather than downlinking raw data.
4. **Downlink faster** — a higher-rate link, which costs power, pointing accuracy and ground infrastructure. See [Comms](comms.md#expected-data-rates).

For compression, [CCSDS](../references/glossary.md#ccsds) publishes standards designed for exactly this: **CCSDS 123.0-B-2**, "Low-Complexity Lossless and Near-Lossless Multispectral and Hyperspectral Image Compression", handles three-dimensional multispectral and hyperspectral arrays, in both lossless mode and a near-lossless mode where the maximum reconstruction error per band is bounded to a user-specified value.[^ccsds123] A bounded-error mode is often exactly what a scientist can accept when unbounded lossy compression is not.

Onboard filtering is the highest-leverage option where it applies. [PhiSat-1](obc.md#advanced-and-emerging-computing-concepts) discarded cloud-covered hyperspectral scenes onboard and cut downlink volume by roughly 30% — a large gain from a simple, well-chosen criterion.

**Store what you cannot send.** Onboard storage is cheap relative to bandwidth. Log everything, downlink a prioritised subset, and keep the rest available for targeted retrieval once the ground has seen the summary.

See also: [Onboard Computing](obc.md)

## Mechanical Integration

- **Mounting and structural support.** Payloads are frequently the densest and heaviest single item aboard, which makes them the dominant term in the [centre of mass](structure.md#mass-properties-and-centre-of-mass) calculation and a driver of the inertia tensor the [ADCS](gnc.md) has to work with. Position them centrally where you can.
- **Alignment.** Optical and pointing-sensitive payloads must be aligned to the spacecraft body frame — and to the [star tracker](../references/glossary.md#star-tracker), if there is one, since that is what converts pointing knowledge into science. Reference machined features or dowel pins, not clearance-hole fasteners, and measure the achieved alignment rather than assuming it. See [Structure – Tolerancing](structure.md#tolerancing-and-stack-up).
- **Vibration sensitivity.** Optics, detectors and any mechanism need to survive launch, and some need to be protected from the spacecraft's own vibration afterwards — reaction wheel jitter being the usual culprit. Isolators solve one problem and create alignment uncertainty, so use them deliberately.
- **Thermal coupling is a choice made at the mounting interface.** Decide whether the payload should be tied to the structure as a heat sink or isolated from it for stability, and implement that choice with the standoff and interface material selection. See [Thermal](thermal.md#conduction-paths-and-thermal-coupling).
- **Access.** Payloads often need late access — a lens cap removed, a calibration source fitted, a desiccant changed, a final functional check. Plan the assembly order so the payload can be reached, or at least removed and refitted, without dismantling the spacecraft.
- **Contamination.** Optical payloads are ruined by [outgassing](../references/glossary.md#outgassing) deposits and particulates from elsewhere on the spacecraft. If you have optics, the whole spacecraft's material selection becomes a payload requirement. See [Structure – Cleanliness](structure.md#cleanliness-handling-and-contamination).
- **Apertures and field of view.** An instrument needs an unobstructed view, and so does everything else — solar cells, antennas, radiators, star trackers. External surface allocation is a systems-level fight that should be settled early and explicitly.

## Electrical and Data Interfaces

- **Power.** Specify the payload's voltage, nominal and peak current, inrush behaviour and any sequencing requirements, and check them against what the [EPS](eps.md#power-distribution-and-buses) provides. Payloads should be on a dedicated switchable channel with current limiting, both so they can be power-cycled to recover and so a payload fault cannot take down the bus.
- **Data interface.** Match the interface to the rate: I²C or UART for a slow sensor, SPI for moderate rates, LVDS or a parallel bus for an imager. Given the reliability record of I²C on CubeSats, avoid putting a payload on the same I²C bus as critical bus subsystems — a payload hanging that bus should not be a mission-ending event. See [OBC – The bus reliability problem](obc.md#the-bus-reliability-problem).
- **Command and control.** Define the command set, the telemetry set, and the payload's own state machine. A payload that can be commanded into a state the bus does not know about is a diagnostic nightmare.
- **Isolation and fault containment.** Optical or galvanic isolation on payload interfaces is cheap insurance, particularly for a payload developed by a different team or supplier. Assume it will misbehave at some point.
- **Grounding.** Sensitive analogue payloads and switching converters coexist badly. Agree the grounding topology and any required separation of analogue and digital returns early, and check it on a [flatsat](../references/glossary.md#flatsat).

## Power, Thermal, and Resource Constraints

This is where payload ambitions meet the bus, and it is worth doing the arithmetic honestly before committing.

- **Power and duty cycling.** Few CubeSat payloads can run continuously. The [duty cycle](../references/glossary.md#duty-cycle) that the [power budget](eps.md#power-requirements-and-budgets) permits is a hard mission parameter — it determines how much data you can collect at all — and it should be computed early rather than discovered late. Peak draw matters as much as average: a payload that pulls 8 W for 30 seconds may be fine on average and still brown out the bus.
- **Thermal.** Payload dissipation goes somewhere, and payload temperature requirements are often tighter than anything else on the spacecraft. Both directions of this coupling need to be in the thermal model from the start. See [Thermal – Interaction with Other Subsystems](thermal.md#thermal-interaction-with-other-subsystems).
- **Mass and volume.** Payload mass fraction is a good sanity check on a design: if the payload is a small fraction of the total, ask whether the form factor is right.
- **Data.** The data budget — generated per orbit versus downlinked per orbit — is as binding as power, and less often tracked. See [Systems Engineering – Budgets and Margins](systems-engineering.md#budgets-and-margins).
- **Pointing.** Tighter pointing requirements cascade into ADCS cost, mass and power faster than almost anything else. Check whether you need pointing *accuracy* or merely pointing *knowledge* — see [GNC – Turning objectives into requirements](gnc.md#turning-objectives-into-requirements).

**Performance versus survivability** is the recurring trade. A payload optimised for maximum performance may need power, pointing and thermal conditions the bus can only occasionally provide. One optimised for robustness collects less but collects it reliably, for longer. On a first mission, robustness usually wins on total science return.

## Payload Operations and Modes

- **Operational modes.** Define them explicitly — off, standby, warm-up, acquiring, processing, downlinking — with the resource profile of each. Payload modes must be integrated into the spacecraft mode structure rather than running in parallel to it. See [Flight Software – Modes](flight-software.md#modes-state-machines-and-autonomy).
- **Warm-up and settling.** Detectors, oscillators and thermally stabilised optics need time to reach a stable state. That time is part of the power budget for every acquisition, and it is easy to forget.
- **Coordination with ADCS.** An acquisition typically needs a slew, a settling period, the acquisition itself, and a return to a power-positive attitude. The whole sequence has to fit within available power, momentum and time.
- **Coordination with comms.** Acquisition and downlink often compete for power and for attitude. Sequencing them across an orbit is a real planning exercise.
- **Autonomy versus ground control.** With a handful of passes a day, most acquisitions are executed from an uplinked timeline. Conditional autonomy — acquire when over a target, in daylight, with battery above a threshold — extends what is possible considerably. Full onboard decision-making is where onboard AI is heading. See [OBC – Advanced and Emerging Computing Concepts](obc.md#advanced-and-emerging-computing-concepts).
- **Safe states.** The payload must have a defined safe state, must enter it autonomously on fault or on spacecraft [safe mode](../references/glossary.md#safe-mode), and must never be able to prevent the spacecraft from recovering. Every payload operation should be time-limited, so a lost ground link cannot leave the payload running indefinitely.

## Calibration and Validation

Uncalibrated data is not a measurement; it is a number. For science payloads this is the difference between a result and an anecdote.

### Ground calibration

- **[Radiometric calibration](../references/glossary.md#radiometric-calibration)** relates raw detector counts to physical units, using reference sources — integrating spheres for imagers, radioactive sources for detectors (as with GMOD's characterisation against known lines[^eirsat-gmod]), blackbodies for thermal instruments.
- **Spectral calibration** establishes which wavelength each channel actually responds to.
- **Geometric calibration** relates pixel position to look direction, and the instrument frame to the spacecraft body frame — without which pointing knowledge cannot be turned into georeferenced data.
- **Dark, bias and flat-field characterisation**, ideally across the operating temperature range, since every one of these varies with temperature.

Calibrate in flight-like conditions where you can. A calibration taken at 20 °C in air may not describe an instrument at −10 °C in vacuum.

### In-orbit calibration

Ground calibration shifts during launch and drifts in orbit, so plan for on-orbit verification:

- **Onboard calibration sources** — LEDs, reference sources, a shutter for dark frames. Cheap to include, impossible to add later.
- **Celestial references** — the Moon, bright stars and the deep-space background are stable, well-characterised targets.
- **Vicarious calibration** — imaging well-instrumented ground sites with known reflectance.
- **Cross-calibration** against an established instrument observing the same target.
- **Commissioning campaign.** Budget real time for this. The first weeks in orbit should be spent characterising the instrument as it actually is, not assuming it matches the lab.

### Drift and degradation

Detectors accumulate radiation damage, optics darken, gains shift. Repeat calibration measurements throughout the mission, trend them, and treat a sudden change as a diagnostic signal. **Record enough metadata that data can be recalibrated later** — if you discover a calibration error in year two, you want to be able to fix year one's data rather than discard it.

## Testing and Verification

- **Functional testing** of the payload standalone, then integrated, then in the full spacecraft. Each step finds different problems.
- **End-to-end data flow** is the test teams most often skip and most often regret: payload → onboard storage → downlink → ground station → decoder → archive → analysis, with real data through the real chain. Byte-order mismatches, truncation and metadata loss all surface here and nowhere else.
- **Environmental testing.** Payloads often need instrument-specific environments beyond the standard campaign — optical alignment verified after vibration, detector performance measured under [TVAC](../references/glossary.md#tvac). Verify performance after environmental exposure, not just survival. See [AIT – Environmental Testing](ait.md#environmental-testing).
- **Realistic stimulus.** Give the payload something it can actually detect: a target scene for an imager, a radioactive source for a detector, an RF signal for a receiver. "The payload powers on and reports healthy" is not a functional test.
- **Long-duration operation** at realistic duty cycles, to catch thermal build-up, memory leaks and storage exhaustion.
- **Failure injection** — power cut mid-acquisition, corrupted data, sensor returning garbage. See [Flight Software – Software Testing](flight-software.md#software-testing-and-validation).

Common pitfalls: testing the payload only with its own ground support equipment and never through the flight data path; discovering the payload's power draw only after integration; and never testing what happens when a payload operation is interrupted by a [safe mode](../references/glossary.md#safe-mode) entry.

See also: [Assembly, Integration and Testing (AIT)](ait.md).

## Payload Documentation and Data Products

### Interface documentation

The payload [ICD](../references/glossary.md#icd) is the contract between the payload and the bus, and it matters most when those are built by different people. It should cover mechanical envelope, mounting and alignment; mass properties; power (nominal, peak, inrush, sequencing); the data interface and protocol; the full command and telemetry dictionary; thermal limits and dissipation; and the modes with their resource profiles.

Write it early, version it, and treat changes as changes rather than as clarifications.

### Data products and metadata

- **Define the product levels** — raw (Level 0), calibrated (Level 1), derived (Level 2) — and be explicit about which the mission actually promises to deliver.
- **Metadata is what makes data reusable**: acquisition time, spacecraft position and attitude, instrument mode and settings, temperatures, calibration version. Data without metadata may be worthless a year later, and the missing field is always the one nobody thought to record.
- **Use standard formats where they exist** — FITS for astronomy, GeoTIFF or NetCDF for Earth observation, CCSDS for transport. A custom binary format guarantees that nobody outside the team will ever use your data.
- **Version the calibration** applied to each product, so data can be reprocessed when calibration improves.

### Archiving and sharing

- **Archive raw data permanently**, alongside the processing chain. Derived products can always be regenerated; raw data cannot.
- **Plan for reproducibility** — version-control the processing code and record which version produced which product.
- **Publish.** Many CubeSat missions produce genuinely useful data that never reaches anyone outside the team, usually because nobody planned for it. Deciding early to publish shapes the metadata and format choices that make publishing possible. The mission examples in [CubeSat Missions](../references/missions.md) show what open publication looks like in practice.
- **Consider the ground segment side of this from the start** — telemetry storage, dashboards and public data access are part of the payload's success. See [Ground Segment – Data Handling and Archiving](ground-segment.md#data-handling-and-archiving).

<!-- CSR-RESOURCES:START dev-payload-standards-and-examples -->
- **[CCSDS 123.0-B-2: Low-Complexity Lossless and Near-Lossless Multispectral and Hyperspectral Image Compression](https://ccsds.org/Pubs/123x0b2e2c3.pdf)** `PDF` – CCSDS standard for lossless and bounded-error compression of multispectral and hyperspectral image data
- **[A compact instrument for gamma-ray burst detection on a CubeSat platform II: Detailed design, assembly and validation](https://arxiv.org/abs/2203.03502)** `Link` – Detailed design and validation of EIRSAT-1's GMOD gamma-ray detector, a well-documented CubeSat science instrument
- **[A compact instrument for gamma-ray burst detection on a CubeSat platform I: Design drivers and expected performance](https://arxiv.org/abs/2108.08203)** `Link` – Companion paper covering the design drivers and expected performance of the same instrument
<!-- CSR-RESOURCES:END dev-payload-standards-and-examples -->

---

👉 **Please consider [contributing](../contributing.md)!**

[^eirsat-gmod]: ["A compact instrument for gamma-ray burst detection on a CubeSat platform II: Detailed design, assembly and validation"](https://arxiv.org/abs/2203.03502), *Experimental Astronomy*, 2022 (preprint arXiv:2203.03502). Describes EIRSAT-1's GMOD instrument: a 25 × 25 × 40 mm cerium bromide scintillator read out by a 4×4 tiled silicon photomultiplier array, achieving 5.4% energy resolution at 662 keV, with electrical and mechanical interfaces deliberately made compatible with off-the-shelf CubeSat systems.
<!-- NEEDS HUMAN VERIFICATION: I have deliberately omitted author names from this citation because I could not retrieve them reliably and did not want to guess. Please add the author list from the paper before publishing. -->

[^ccsds123]: Consultative Committee for Space Data Systems, [*Low-Complexity Lossless and Near-Lossless Multispectral and Hyperspectral Image Compression*, CCSDS 123.0-B-2](https://ccsds.org/Pubs/123x0b2e2c3.pdf). Defines lossless and near-lossless compression for three-dimensional multispectral and hyperspectral arrays, with the near-lossless mode bounding maximum reconstruction error to a user-specified value per band, and three entropy coding options (sample-adaptive, hybrid and block-adaptive).
