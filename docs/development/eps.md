# Electrical Power Systems (EPS)

This section covers power generation (solar panels), storage (batteries and BMS), conditioning and distribution (EPS and power buses).

## Power Requirements and Budgets

A **power budget** is the bookkeeping exercise that tells you whether your spacecraft will stay alive in orbit. On one side: how much energy each subsystem draws and for how long, across every mission mode. On the other: how much your solar panels and batteries can supply across every [orbit](../references/glossary.md#orbit) phase. If the second number isn't comfortably bigger than the first, you don't have a flyable design.

Power budgets are rarely a one-pass calculation. They evolve from coarse estimates at concept stage to detailed worst-case-orbit analyses by [CDR](../references/glossary.md#cdr), and they're updated continuously as components are selected, tested, and replaced.

### Estimating consumption

- **Component-level draws**: collect current and voltage figures for every active component from datasheets – receivers, transmitters, [OBC](../references/glossary.md#obc), [ADCS](../references/glossary.md#adcs) sensors and actuators, payload, heaters. Use worst-case (max) values, not typical.
- **Operational modes**: most CubeSats have 4–6 modes (e.g. safe, nominal, comms, payload, detumble). Each mode activates a different set of components and so has a different power profile.
- **Duty cycles**: many components don't run continuously. A transmitter might be active 5 minutes per orbit; a payload might pulse for 10 seconds per minute. Average power = peak power × duty cycle.
- **Orbit-average power ([OAP](../references/glossary.md#oap))**: the time-weighted sum of consumption across all modes over a representative orbit. This is the headline number generation must beat.[^hawaii-budget]

### Estimating generation

- **Solar input**: depends on cell efficiency, panel area, sun-incidence angle, and [beta angle](../references/glossary.md#beta-angle) (which drives eclipse fraction).
- **[Eclipse fraction](../references/glossary.md#eclipse-fraction)**: a [LEO](../references/glossary.md#leo) orbit at low beta angle spends 37–40% of its period in eclipse – about 35 minutes – but this varies seasonally and with orbit geometry. Eclipse duration falls as the magnitude of the beta angle rises, and above a critical value the orbit is sunlit continuously – see [Illumination, eclipse and incidence angle](#illumination-eclipse-and-incidence-angle).
- **Pointing**: a tumbling spacecraft generates far less than a stable, sun-pointing one. Account for this honestly during early phases – assuming nominal pointing before you've proven your [ADCS](../references/glossary.md#adcs) works is a classic source of negative-budget surprises.[^clyde-space]
- **Degradation**: solar cell efficiency drops over time in the LEO radiation environment. The rate varies significantly by cell technology and orbital altitude – triple-junction (TJ) cells degrade the least, silicon cells the most, with small satellites (under 10 kg) experiencing higher rates than larger ones due to lower thermal inertia and shielding.[^degradation] A common planning figure is 1–3% per year for quality cells with coverglass; size your panels for end-of-life, not beginning-of-life.[^hawaii-gen]

A more detailed photovoltaic generation analysis (often called a **PV budget**) breaks out these factors panel-by-panel and over time, and is worth doing separately once orbit and attitude assumptions firm up.

### Margins and derating

- 30% margin at [PDR](../references/glossary.md#pdr) is conservative; 20% at [CDR](../references/glossary.md#cdr) is typical; 10% at flight is acceptable if the budget has been validated against test data.[^nasa-margins] See [Systems Engineering – Margin philosophy](systems-engineering.md#margin-philosophy) for how margins are held and accounted across the project.
- Hold power margin against end-of-life generation, not beginning-of-life. This is how GSFC states its own requirement, and it is the difference between a budget that closes in year one and one that closes for the whole mission.
- Battery [depth-of-discharge](../references/glossary.md#dod-battery) is usually kept below 20–30% to preserve cycle life over the mission.
- Worst-case scenarios worth checking explicitly: maximum eclipse, off-nominal attitude, transmitter active during eclipse, end-of-life cell efficiency, all heaters on at coldest case.

### Coupling to other budgets

Power is just one of many connected things to consider:

- **Thermal**: every watt consumed becomes heat. Heater duty cycles change with thermal environment, which changes with orbit and attitude. See [Thermal](thermal.md).
- **[ADCS](../references/glossary.md#adcs)**: detumble and slew operations are power-hungry, and pointing accuracy directly affects solar generation. See [GNC](gnc.md).
- **Comms**: transmit power often dominates the budget during pass windows. See [Comms – Link Budget](comms.md#link-budget).
- **Mission ops**: payload duty cycles and downlink schedules need to fit within what the power system can sustain across an orbit, a day, and a season.

### Templates and worked examples

For ready-to-use templates and reference analyses, see [Calculators and Reference Tools](tools.md#power-budget-templates).

## Solar Power Generation

Solar cells are the only meaningful source of energy for almost every CubeSat. Everything else in the [EPS](../references/glossary.md#eps) exists to store, condition and ration what the panels collect.

### Cell technologies and efficiencies

Space solar cells are not terrestrial solar cells. The flight standard is the **[triple-junction](../references/glossary.md#triple-junction-solar-cell) (TJ) III–V cell**, which stacks three semiconductor junctions with different bandgaps so each captures a different part of the spectrum. NASA's state-of-the-art survey puts multi-junction cells at a "nominal efficiency of 30% and a high of 34%", against roughly 20% for single-junction silicon.[^nasa-soa-power]

Concrete numbers help. AZUR SPACE's widely flown **3G30-Advanced** cell is specified at **29.5% BOL efficiency** with Voc 2700 mV, Isc 520 mA and Vmp 2411 mV over a 30.18 cm² cell measuring 40 × 80 mm, weighing ≤86 mg/cm² (about 2.6 g per cell).[^azur-3g30] Current-generation parts push further – AZUR's 4G32-Advanced at 31.5%, Rocket Lab's Z4J at 31.3%, Boeing-Spectrolab's XTE-SF at 32.2%.[^nasa-soa-power]

Two properties matter as much as efficiency:

- **Temperature coefficients.** Cell voltage falls as the cell heats up. The 3G30-Advanced loses **6.2 mV/°C on Voc** and **6.7 mV/°C on Vmp**, while current rises very slightly.[^azur-3g30] A panel in full sun can easily sit 40–60 °C above its cold-case temperature, so the operating voltage on a hot sunlit pass is materially lower than the datasheet's 28 °C figure. Size your string voltage for the hot case.
- **Radiation degradation.** The same cell drops to roughly **18.6% efficiency at 1 × 10¹⁶ e/cm² of 1 MeV electron fluence**.[^azur-3g30] Real [LEO](../references/glossary.md#leo) missions see far less than that, but the principle stands: size the array for **[end of life](../references/glossary.md#bol-eol), not beginning of life**. See [Power Requirements and Budgets](#power-requirements-and-budgets) for planning figures.

Emerging options – perovskites (26.7% single-junction in the lab, tandem silicon-perovskite approaching 35%), flexible CIGS thin film (23.64% in the lab) and organic PV (~20%) – are worth watching but are not yet flight baselines for a mission you need to fly.[^nasa-soa-power]

### Body-mounted vs deployable arrays

- **Body-mounted** cells are bonded directly to the structure's side panels. Simple, robust, no mechanism, no deployment failure mode. The catch is area: a 1U has at most four usable side faces of 100 × 100 mm, and once rails, connectors and access ports are accounted for, a commercial 1U panel carries just **two** cells – EnduroSat's 1U X/Y panel is two CESI CTJ30 cells rated at up to 2.4 W per panel in LEO.[^endurosat-1u] A 3U face takes six or seven of the same cells. NASA quotes specific power of **36–76 W/kg** for body-mounted designs.[^nasa-soa-power]
- **Deployable** arrays fold panels against the body for launch and swing them out on orbit, multiplying collecting area severalfold. Specific power runs **31–140 W/kg**, with flexible roll-out systems such as Redwire's ROSA reaching ~100 W/kg at much larger scale.[^nasa-soa-power] The cost is a hinge, a release mechanism, a stowed-volume allocation and a new single-point failure. See [Structure – Deployable Structures and Mechanisms](structure.md#deployable-structures-and-mechanisms).
- **Sun-tracking** arrays add a drive mechanism to keep panels normal to the Sun. Rare below 6U – the mass, power and complexity rarely pay back at CubeSat scale.

A useful sanity check before committing: at normal incidence a single 1U panel produces around 2.4 W, so a 1U with body-mounted 30% cells realistically averages **1–2 W across an orbit** once eclipse and incidence angle are accounted for. Two to three watts is achievable only with a genuinely favourable and stable attitude, and a tumbling spacecraft will do considerably worse than 1 W. If your [power budget](#power-requirements-and-budgets) needs 8 W, no amount of MPPT tuning will save it – you need deployables or a bigger bus.

### Illumination, eclipse and incidence angle

Generated power scales with the cosine of the angle between the panel normal and the Sun vector. A panel 60° off-Sun produces half its rated output; at 80° it produces almost nothing. This makes generation an **[ADCS](../references/glossary.md#adcs) problem as much as an EPS problem** – see [GNC](gnc.md).

- A tumbling spacecraft averages far below its nominal figure, because faces spend much of their time edge-on or shadowed. Assume tumbling for the commissioning phase, because that is what you will actually have.
- **[Eclipse fraction](../references/glossary.md#eclipse-fraction)** is 37–40% for low-[beta-angle](../references/glossary.md#beta-angle) LEO orbits across the 300–600 km band – roughly 35 minutes of eclipse, almost independent of altitude – and falls as the magnitude of the beta angle rises. Above a critical beta angle of β\* = arcsin(R_E / (R_E + h)) the orbit is sunlit continuously – roughly 70° at 400 km and 68° at 500 km. This is why dawn–dusk sun-synchronous orbits, which hold a high beta angle for much of the year, are so popular for power-hungry missions.
- **Self-shadowing** by deployed panels, antennas and the body itself is easy to miss in a spreadsheet and obvious in a CAD-based illumination analysis. Do the analysis if your margin is thin.
- **Albedo and [Earth IR](../references/glossary.md#earth-ir)** add a modest amount of extra input on nadir-facing panels. Nice to have; not something to rely on.

### Panel electrical design

- **Strings.** Cells are wired in series to build a useful voltage. With Vmp ≈ 2.4 V per TJ cell, a two-cell string gives ~4.8 V and a three-cell string ~7.2 V – enough to charge a 2-cell lithium pack through a boost or MPPT stage. String length is chosen against the *hot* Vmp, not the nominal.
- **Blocking diodes** prevent current flowing backwards from the battery into a shadowed or failed string. They cost 0.3–0.7 V of forward drop, which is significant on a 5 V string; Schottky parts or ideal-diode controllers reduce the penalty.
- **Bypass diodes** across cells or sub-strings let current route around a shadowed cell instead of reverse-biasing it. Without them, one shadowed cell in a series string can throttle the whole string and dissipate power as heat in the shadowed cell.
- **Harnessing.** Panel wiring runs across hinges on deployables and around the structure on body-mounted panels. Route it with service loops and strain relief, and keep it away from magnetometers – panel current loops generate magnetic dipoles that your [ADCS](gnc.md#magnetometers) will see.
- **Temperature sensors on the panels** are cheap and disproportionately useful: they let you correct telemetry, validate your thermal model, and diagnose illumination problems from the ground.

### Solar cell datasheets

<!-- CSR-RESOURCES:START dev-eps-solar-cell-datasheets -->
- **[LightFoundry Space Grade 30% Efficiency GaAs 14466 Solar Cell Datasheet](https://storage.googleapis.com/cubesat-resources/resources/development-eps-solar-cell-datasheets/datasheet-lightfoundry-space-grade-30-efficiency-gaas-6-inch-solar-cell-assembly-g2qiev.pdf)** `PDF` – Space-grade 30 percent GaAs solar cell datasheet
- **[AZUR SPACE 3G30-Advanced triple-junction cell datasheet](https://www.azurspace.com/media/uploads/file_links/file/bdb_00010891-01-00_tj3g30-advanced_4x8.pdf)** `PDF` – 29.5% BOL efficiency 4x8 cm cell with full electrical, thermal and radiation degradation data
<!-- CSR-RESOURCES:END dev-eps-solar-cell-datasheets -->

## Energy Storage

The battery carries the spacecraft through eclipse, supplies peak loads the array cannot (transmit bursts, magnetorquer pulses, deployment actuations), and keeps the bus alive during off-nominal attitudes. It is also the component most likely to end your mission early.

### Chemistries

**Lithium-ion in its various forms is the only realistic choice.** NASA's survey puts commercial Li-ion at **150–270 Wh/kg**, with advanced designs reaching 450–500 Wh/kg, and notes that NiCd and NiH₂ have been essentially fully displaced.[^nasa-soa-power] Within that family:

- **Li-ion cylindrical cells (18650, 21700)** – the workhorse. Cheap, extremely well characterised, high energy density, and available with flight heritage from Panasonic, LG Chem, Samsung and Sony. Most CubeSat packs are two or four of these in series/parallel.
- **Lithium polymer (LiPo)** – pouch cells, better volumetric packing, but they swell with age and need mechanical restraint. Widely used commercially: AAC Clyde Space's OPTIMUS range spans 30 Wh (268 g) to 80 Wh (670 g) at 8.26 V.[^satsearch-batteries]
- **Lithium iron phosphate (LFP/LiFePO₄)** – lower energy density (~3.2 V nominal, less Wh/kg), but excellent cycle life, high discharge-rate capability and a much better safety profile. A good trade when the mission is long and the power demand modest.
- **Primary (non-rechargeable) cells** – LiSOCl₂, LiSO₂, LiCFₓ. Used for very short missions or for a one-shot deployment function, not for a spacecraft that has to survive thousands of orbits.

### Sizing

Capacity sizing follows from the [power budget](#power-requirements-and-budgets), and is driven by three things: eclipse energy, peak load support, and [depth of discharge](../references/glossary.md#dod-battery) limits.

The basic sizing relation is:

> **Capacity (Wh) ≥ (eclipse duration × orbit-average load during eclipse) / (max allowable DoD × discharge efficiency)**

With DoD held to 20–30% to preserve cycle life, a mission drawing 2 W through a 35-minute eclipse needs roughly 1.17 Wh of *usable* energy and therefore about **4–6 Wh of installed capacity**. Most 1U–3U missions land somewhere between 10 and 40 Wh, which is why that is exactly the range commercial packs cluster in.

Add margin for:

- **Capacity fade over the mission.** Lithium cells lose capacity with cycling and calendar age. For a typical 95-minute orbit, a LEO mission accumulates roughly **5,500 charge-discharge cycles per year**.
- **Cold operation.** Usable capacity falls sharply below 0 °C.
- **Peak loads.** A transmitter drawing 5 W for 3 minutes during eclipse is a bigger instantaneous demand than the orbit-average figure suggests.

### Temperature is the whole game

Lithium cells have asymmetric temperature limits, and the charge limit is the tight one. A representative commercial space battery specifies roughly **0 to 45 °C for charging** against a materially wider window for discharge.[^satsearch-batteries] Exact numbers vary by cell, so use your own datasheet – but the shape is universal: the charge window is narrower than the discharge window, and its lower bound is the one that bites.

The consequences are structural:

- **Charging a lithium cell below 0 °C plates metallic lithium on the anode.** This is permanent, cumulative, and eventually causes an internal short. It is not a performance derate; it is damage.
- Therefore almost every CubeSat needs **battery heaters** with an interlock that inhibits charging until the pack is above its minimum charge temperature. This is one of the few places where a hardware interlock rather than a software check is genuinely justified.
- Heaters draw power at exactly the moment power is scarcest – cold means eclipse. Budget for it explicitly in the coldest case. See [Thermal](thermal.md#thermal-interaction-with-other-subsystems).
- Place the battery centrally where thermal swings are smallest, and couple it deliberately rather than by accident. See [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).

### Safety and launch requirements

Batteries are the one CubeSat component that can hurt people, and launch providers treat them accordingly.

- Expect to supply cell datasheets, pack design details, protection circuit descriptions and test evidence as part of your safety data package.
- Missions deploying from the ISS face the most stringent requirements, since the pack sits inside a crewed vehicle before deployment.
- Design for **containment of a single-cell failure**: fusing between parallel cells, adequate spacing, and no path for a thermal runaway to propagate.
- Deep discharge is also a hazard: a lithium cell taken below its minimum voltage can be damaged such that recharging it is unsafe. Under-voltage lockout is a protection requirement, not a nicety.
- **Plan for months of storage.** Flight hardware is typically delivered one to six months before launch and then sits inside the deployer, untouched. Confirm the pack will still be above its minimum deployment voltage after that interval at the expected storage temperature, and establish early whether the deployer allows late access for charging. See [Qualification and Launch – Fit checks and delivery](launch.md#fit-checks-and-delivery).

### End-of-life passivation

Disposal rules increasingly require that a spacecraft be left unable to fragment at end of mission: batteries discharged, stored energy released, transmitters silenced. [Passivation](../references/glossary.md#passivation) is an EPS function, and it has to be designed in rather than improvised once the mission is over.

- It must be a **commandable function that actually works**, and it conflicts directly with the protections you built: under-voltage lockout exists precisely to prevent the pack being deeply discharged. Decide early how passivation overrides it, and make that path hard to trigger by accident.
- It has to work in the state the spacecraft will actually be in at end of life – degraded, possibly tumbling, possibly with a partly failed pack.
- Test it on the flatsat. A passivation command that has never been exercised is a claim, not a capability.

See [Qualification and Launch – End of Life](launch.md#end-of-life).

## Battery Management Systems (BMS)

The [BMS](../references/glossary.md#bms) is the set of functions that keeps the pack within its safe operating area. On CubeSats it is usually integrated onto the EPS board rather than being a separate unit.

### Cell balancing

Series cells drift apart in state of charge over thousands of cycles. Without balancing, the weakest cell hits its voltage limits first and dictates the usable capacity of the whole pack – and eventually gets over-charged or over-discharged while the pack as a whole looks healthy.

- **Passive balancing** bleeds charge from the higher cells through a resistor until they match. Simple, cheap, universally used at CubeSat scale, and wastes a small amount of energy as heat.
- **Active balancing** transfers charge from stronger to weaker cells. More efficient, more complex, rarely justified on a 2S pack.
- Balancing only works if you can **measure individual cell voltages**. A pack monitored only at the terminals gives you no visibility into divergence, and divergence is the failure you are trying to catch.

### Protections

The standard set, each of which should be implemented in hardware and *reported* to software rather than depending on software to act:

- **Over-voltage** cutoff on charge, per cell.
- **Under-voltage** lockout on discharge, per cell, with hysteresis so the bus does not oscillate at the threshold.
- **Over-current** and short-circuit protection on both charge and discharge paths.
- **Over-temperature** cutoff, and the **under-temperature charge inhibit** described above.

### Interaction with EPS logic and flight software

The BMS's job is to protect the pack; the EPS's job is to keep the mission alive. These goals conflict, and the conflict has to be resolved deliberately.

- Define what happens when the BMS cuts off: does the bus brown out, does the [OBC](../references/glossary.md#obc) get a clean warning first, does the spacecraft enter a low-power mode? A pack that disconnects without notice looks identical to a total power failure from the ground.
- Expose cell voltages, pack current, temperature and balancing state as telemetry. This is your primary early-warning channel for degradation.
- Make sure recovery is automatic. A spacecraft that under-voltage-locks out and needs a ground command to come back has just made recovery impossible, because it cannot talk to you. See [Flight Software – FDIR](flight-software.md#fault-detection-isolation-and-recovery-fdir).

## Power Conditioning and Regulation

### Maximum power point tracking

A solar array's power output peaks at one particular operating voltage, and that point moves with illumination and temperature. **[MPPT](../references/glossary.md#mppt)** continuously hunts for it.

- **Perturb-and-observe** is the classic algorithm: nudge the operating point, see whether power went up, keep going in that direction. Simple, robust, and what most CubeSat EPS boards actually run.
- **Incremental conductance** converges faster under rapidly changing illumination – relevant coming out of eclipse or while tumbling.
- **Fixed-voltage / direct energy transfer (DET)** skips tracking entirely and clamps the array to the battery voltage. Less efficient, but simpler, with fewer failure modes and no risk of the tracker losing lock. Perfectly defensible on a small, power-rich mission.

MPPT typically buys 10–30% more energy than a naive fixed operating point, with the gain largest when panel temperature swings widely. Whether that justifies the complexity depends on how tight your budget is.

<!-- CSR-RESOURCES:START dev-eps-mppt-algorithms -->
- **[Deep Learning-Based MPPT Approach to Enhance CubeSat Power Generation](https://ieeexplore.ieee.org/document/10904144)** `Link` – Abdulazez Abagero et al., *IEEE Access* 13, 2025. Deep-learning maximum power point tracking for CubeSat solar arrays. Open access (CC BY 4.0)
<!-- CSR-RESOURCES:END dev-eps-mppt-algorithms -->

### Converters

- **Buck (step-down)** converters generate the 3.3 V and 5 V rails from the battery bus. Efficient, well understood, and the workhorse of any CubeSat EPS.
- **Boost (step-up)** converters are needed when a short solar string must charge a higher-voltage pack.
- **Buck-boost** handles the case where input voltage crosses the output voltage – common with an unregulated lithium bus that swings from 8.4 V down to 6.0 V across a discharge.

**Efficiency versus noise is the core tradeoff.** Switching converters run at 85–95% efficiency but inject switching noise onto the bus and radiate it. That noise lands directly on your receiver's noise floor and on your analogue sensors. Mitigations: keep switching frequencies away from sensitive bands, filter aggressively at the point of load, use separate quiet rails for RF and analogue sections, and pay attention to layout and return paths. Linear regulators are wasteful but quiet, and are still the right answer for a low-current, noise-critical sensor rail.

### Startup and brownout behaviour

The most dangerous moment in a CubeSat's electrical life is the first power-up in orbit, on a cold, deeply discharged battery, while tumbling.

- **Cold-start from a dead battery** must work with only solar input and no help from the ground. Verify it on the bench with a solar array simulator and an actually-flat pack, not a charged one.
- **Brownout loops** are a classic CubeSat killer: the bus comes up, the OBC boots, the boot sequence draws more than the array can supply, the bus collapses, and the cycle repeats indefinitely. Defend against it by sequencing loads, keeping the minimum boot configuration genuinely minimal, and requiring a charge threshold before non-essential loads are enabled.
- **Inrush current** at switch-on – capacitor charging, motor stall currents – can trip protection or collapse the bus. Soft-start on every switched load. See [Power Switching and Protection](#power-switching-and-protection).
- Give the EPS the authority to hold the OBC off until conditions are safe, and make that behaviour independent of the OBC's own software.

## Power Distribution and Buses

### Bus architecture

Two broad patterns dominate:

- **Unregulated battery bus.** Loads take the raw pack voltage – typically 6.0–8.4 V for a 2S lithium pack – and regulate locally. Simple, efficient (no conversion stage in the main path), and inherently fail-soft. The cost is that every load must tolerate the full voltage swing.
- **Regulated distribution.** The EPS provides fixed 3.3 V and 5 V rails. Easier for load designers, and the norm for COTS [PC/104](../references/glossary.md#pc104) stacks, but each rail is a conversion stage with its own efficiency loss and failure mode.

Most CubeSats use both: an unregulated bus for high-power loads that have their own front end (transmitters, magnetorquers, heaters) and regulated rails for logic.

Higher bus voltages (12 V, 28 V) start to make sense at 6U and above, where currents on a 3.3 V rail become inconveniently large. Below that, the [harness](../references/glossary.md#harness) losses rarely justify the extra conversion.

### Practical distribution concerns

- **Switched versus always-on.** A very small always-on domain – the EPS itself, the watchdog, the [inhibit](inhibits-hdrm.md) logic, the RTC – plus everything else on switchable channels. A [propulsion](propulsion.md) system, if you carry one, sits on the switched side behind its own inhibit chain. The always-on domain is your last line of defence: it must be simple enough that you are confident it cannot fail.
- **High-side switching** (interrupting the positive rail) is standard, because it leaves the load's ground reference intact. Low-side switching is simpler and cheaper but leaves the load floating at ground potential with the supply still connected, which causes leakage paths and confusing failure modes.
- **Harness and connectors** deserve more attention than they get. Voltage drop on a 3.3 V rail carrying 2 A through thin wire is not negligible, and connector contact resistance drifts with thermal cycling and vibration. Use connectors with positive retention, keep power and signal separated, and label everything. See [AIT – Electrical Assembly and Harnessing](ait.md#electrical-assembly-and-harnessing).
- **Grounding.** Decide on a grounding topology early (single-point star ground is the usual CubeSat answer) and document it. Anodised structures do not conduct, so the return path must be designed rather than assumed – see [Structure – Materials](structure.md#materials-and-manufacturing).

## Power Switching and Protection

Every switched load needs to be independently controllable and independently protected, because the point of switching is fault containment.

- **Load switches** – integrated high-side switches with built-in current limiting, soft-start and fault reporting are widely available and worth using over a discrete MOSFET plus gate drive. The fault flag is the valuable part: it tells you *which* load misbehaved.
- **Latching current limiters ([LCLs](../references/glossary.md#lcl))** are the standard spacecraft pattern: the channel limits current for a defined period, then latches off and stays off until commanded to reset. This contains a fault without the mission-ending permanence of a fuse.
- **Fuses** are simple and absolutely reliable, and they are one-shot. Use them where a fault should genuinely end that function's life – battery pack protection, for instance – and not where a transient overcurrent is plausible.
- **Polyfuses (PPTC)** self-reset, but their trip characteristics vary strongly with temperature, which is awkward across a −40 to +80 °C range. Know the derating before relying on one.
- **Inrush management** – soft-start ramps, series resistance during startup, or staged enabling. A large bulk capacitor on a payload looks like a dead short at the instant of switch-on.
- **Latch-up protection.** [Single-event latch-up](../references/glossary.md#sel) in a CMOS device creates a low-impedance path that will destroy the part unless power is removed. A current limiter that trips and power-cycles the affected channel is the standard mitigation, and it is a strong argument for putting each susceptible device on its own switched channel. See [OBC – Redundancy and Fault Tolerance](obc.md#redundancy-and-fault-tolerance).

Design rule worth internalising: **no single load failure should be able to take down the bus.** Walk each channel and ask what a dead short there does. If the answer is "the spacecraft dies", add protection.

## Inhibits and Deployment Safety

The EPS is where launch safety is physically implemented: the inhibits that keep the spacecraft electrically dead inside the deployer, the deployment switches that tell it it has been released, and the timers that hold the transmitter and any deployables off afterwards. Inhibit verification evidence is the most scrutinised item in a launch delivery package, and it is EPS hardware that has to produce it.

Treat the inhibit chain as part of the power architecture from the first schematic rather than as a late addition: it determines which domain is always-on, where the switches sit in the battery path, and what the spacecraft does in the first seconds after separation. See [Inhibits and HDRM – Inhibit interaction with the EPS](inhibits-hdrm.md#inhibit-interaction-with-the-electrical-power-system-eps).

## EPS Monitoring and Telemetry

Power telemetry is the highest-value housekeeping data on a CubeSat. It is often the only insight you have into what actually happened between passes.

### What to measure

- **Per-channel current** on every switched load, not just total bus current. Aggregate current tells you something is wrong; per-channel current tells you what.
- **Individual cell voltages**, not just pack voltage.
- **Battery current with sign**, so charge and discharge can be distinguished and integrated.
- **Temperatures**: battery pack, EPS board, each solar panel.
- **Per-string solar input current and voltage**, which is how you detect a failed string or a stuck deployment – and which doubles as a coarse sun sensor, since the relative currents across faces indicate where the Sun is. See [GNC – Sun sensors](gnc.md#sun-sensors).
- **Latch-off events and protection trips**, with a counter that survives reset.

### Resolution and sampling

- Sample fast enough to catch transients you care about. A transmitter keying on for 200 ms will not appear in 30-second telemetry, and its inrush will not appear in 1-second telemetry either. Consider peak-hold or min/max accumulators between samples for the fastest events.
- Store more than you downlink. Downlink bandwidth is scarce (see [Comms – Expected Data Rates](comms.md#expected-data-rates)), so log at high rate onboard, downlink summaries routinely, and reserve full-rate dumps for when you are investigating something.
- Timestamp everything against a monotonic counter as well as wall-clock time, so telemetry stays interpretable across clock resets. See [Flight Software – Timing](flight-software.md#timing-scheduling-and-timekeeping).

### Using power telemetry

- **Trending is the point.** A single battery voltage reading tells you very little; the same reading over 200 orbits tells you about capacity fade, illumination changes and load growth.
- **Charge accounting (coulomb counting)** – integrating battery current over an orbit – gives a far better state-of-charge estimate than voltage alone, particularly for LFP chemistries with flat discharge curves.
- **Power signatures identify behaviour.** Each subsystem draws a characteristic current profile; a deviation is often the first symptom of a fault, and sometimes the only one.
- Build a ground-side dashboard early. The [SatNOGS dashboards](../references/missions.md#satnogs-dashboard) collection shows what real missions publish and is a good source of ideas for what to plot.

## EPS Integration Considerations

### Choosing an EPS

Buying an EPS is the default for good reason: it is a dense, safety-critical, hard-to-test board, and the commercial options have flown many times.

<!-- CSR-RESOURCES:START dev-eps-commercial-eps -->
- **[GomSpace NanoPower P60](https://gomspace.com/product/nanopower-p60/)** `Link` – Modular high-power EPS for larger CubeSat platforms
- **[GomSpace NanoPower P80](https://gomspace.com/product/nanopower-p80/)** `Link` – High-power modular EPS for 6U and larger platforms
- **[AAC Clyde Space STARBUCK-Nano](https://www.aac-clyde.space/what-we-do/space-products-components/pcdu/cubesat-eps-starbuck-nano)** `Link` – MPPT EPS with 3.3/5/12 V regulated buses and 10 configurable latching current limiters, 86 g
- **[EnduroSat power modules](https://www.endurosat.com/products-category/power-modules/)** `Link` – CubeSat and SmallSat EPS boards and battery packs
<!-- CSR-RESOURCES:END dev-eps-commercial-eps -->

AAC Clyde Space describes the STARBUCK-Nano lineage as the most-flown CubeSat EPS, with heritage back to 2014; it is a reasonable reference point for what a commercial board provides – MPPT charging, 3.3 V, 5 V and 12 V regulated buses, ten configurable [latching current limiters](../references/glossary.md#lcl), and a mass of 86 g for the base variant.

Open-source options are genuinely usable and worth studying even if you buy:

<!-- CSR-RESOURCES:START dev-eps-open-source-eps -->
- **[PyCubed](https://github.com/pycubed)** `Link` – Open-source PC/104-compatible board integrating power, computing, radio and ADCS, programmable in CircuitPython
- **[PyCubed: An Open-Source, Radiation-Tested CubeSat Platform](https://github.com/pycubed/documentation/blob/master/PyCubed_smallsat-paper.pdf)** `PDF` – The SmallSat paper documenting the design and its radiation test campaign
- **[OreSat hardware](https://github.com/oresat)** `Link` – Fully open-source CubeSat bus including power hardware, from Portland State University
- **[Build a CubeSat EPS](https://codeberg.org/buildacubesat-project/bac-hardware/src/branch/main/eps)** `Link` – Another fully open-source CubeSat bus including power hardware, in development and not flown yet. Prototype hardware available for purchase
<!-- CSR-RESOURCES:END dev-eps-open-source-eps -->

The PyCubed paper is a useful read for the radiation question specifically: the team established a 10 krad(Si) TID threshold for a 300 km LEO mission, tested the ATSAMD51 microcontroller and its power MOSFETs past 35 krad, and found flash memory issues emerging around 16 krad while power and logic remained functional.[^pycubed] That is the kind of evidence that lets you use COTS parts defensibly rather than hopefully.

### Coupling with other subsystems

- **Thermal.** Every watt consumed becomes heat, and the battery has the tightest temperature limits on the spacecraft. Power and thermal design converge or both fail. See [Thermal](thermal.md).
- **Flight software.** Mode transitions are usually power-driven: state of charge crossing a threshold enters or exits safe mode. The thresholds, hysteresis and authority need to be agreed between EPS and software, not assumed. See [Flight Software – Modes](flight-software.md#modes-state-machines-and-autonomy).
- **Comms.** Transmit power dominates the budget during passes, and the pass schedule is therefore a power-planning problem. See [Comms – Link Budget](comms.md#link-budget).
- **ADCS.** Detumbling is power-hungry and happens exactly when generation is worst. Check that specific case explicitly. See [GNC](gnc.md).

### Ground testing

- **Use a solar array simulator**, not a bench supply, wherever you can. A bench supply has effectively infinite current capability at a fixed voltage; a solar array does not, and the difference is precisely what MPPT and brownout behaviour depend on.
- **Test with a real, discharged battery.** Cold-start behaviour with a flat pack is a different circuit from cold-start with a charged one.
- **Run day-in-the-life tests** with realistic eclipse cycling and mode transitions, over many orbits, rather than testing each function once. Most EPS bugs are sequence-dependent.
- **Instrument the bench setup** as thoroughly as the flight telemetry. If you cannot see a brownout on the bench, you certainly will not diagnose it from orbit.

### Common pitfalls

- Assuming nominal pointing before the ADCS has been proven, and discovering in orbit that a tumbling spacecraft generates a third of the modelled power.
- Sizing the array for beginning-of-life efficiency.
- Forgetting heater power in the coldest case, which is exactly when the budget is tightest.
- Software that can disable its own recovery path – a command that turns off the radio with no independent timeout to turn it back on.
- Testing only with a charged battery and a bench supply, so the two hardest cases never get exercised.
- Leaving passivation until after launch, and discovering that under-voltage lockout makes it impossible.

---

👉 **Please consider [contributing](../contributing.md)!**

[^hawaii-budget]: University of Hawaiʻi, *A Guide to CubeSat Mission and Bus Design*, §5.9 ["Power Budget and Profiling"](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-9-power-budget-and-profiling/) – walks through the OAP methodology step by step using the Artemis CubeSat Kit as a worked example. Open access.

[^clyde-space]: Craig Clark and Ritchie Logan (Clyde Space), ["Power Budgets for Mission Success"](http://mstl.atl.calpoly.edu/~workshop/archive/2011/Spring/Day%203/1610%20-%20Clark%20-%20Power%20Budgets%20for%20CubeSat%20Mission%20Success.pdf), Cal Poly CubeSat Workshop, 28 April 2011. Free PDF. Practical slide deck on estimating OAP, managing loads, and avoiding negative budgets, including a worked budget carrying 20% design margin and 14% margin at end of life. One of the most-cited introductory treatments.

[^nasa-margins]: The 30/20/10 curve is a CubeSat convention rather than a published requirement. Its closest formal analogue is the NASA NTRS paper by David A. Di Pietro, ["Techniques for Conducting Effective Concept Design and Design-to-Cost Trade Studies"](https://ntrs.nasa.gov/api/citations/20150018331/downloads/20150018331.pdf) (2015), which describes project managers holding 25% margins for power and dry mass at the start of Phase B, with targets of ≥20% at end of Phase B and ≥15% at end of Phase C. Free PDF. NASA's binding requirements are lower than both and are set per resource rather than as a single curve: [GSFC-STD-1000 Rev H](https://standards.nasa.gov/sites/default/files/standards/GSFC/H/0/GSFC-STD-1000RevH_Approved.pdf) requires mass margin above 10% at PDR and above 5% at CDR, and power margin above 15% at PDR and above 10% at CDR, the latter measured against end-of-life capacity. Free PDF. CubeSat teams carry more early margin than any of these to compensate for short schedules, little flight heritage, and datasheet figures standing in for test data. See [Systems Engineering – Margin philosophy](systems-engineering.md#margin-philosophy).

[^degradation]: Yermek Amangeldi et al., ["Degradation Modeling and Telemetry-Based Analysis of Solar Cells in LEO for Nano- and Pico-Satellites"](https://www.mdpi.com/2076-3417/15/16/9208), *Applied Sciences*, 15(16), 2025. Open access. Reports that GaAs cells degrade 4.5–7.0% over typical mission lifetimes at 300–700 km altitude, with TJ cells showing the highest radiation resistance and Si cells the most pronounced loss below 500 km. Smaller satellites (<10 kg) show higher rates than larger ones.

[^hawaii-gen]: University of Hawaiʻi, *A Guide to CubeSat Mission and Bus Design*, §5.5 ["Power Generation"](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-5-power-generation/). Notes that ionizing radiation effects on solar cells can be mitigated by coverglass, with typical loss figures of 1–10% per year depending on cell technology and shielding. Open access.

[^nasa-soa-power]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 3: Power](https://www.nasa.gov/smallsat-institute/sst-soa/power/) (revision dated May 2026). Open access. Source for multi-junction cell efficiencies (30% nominal, 34% high), specific power figures for body-mounted (36–76 W/kg) and deployable (31–140 W/kg) arrays, and Li-ion energy density ranges (150–270 Wh/kg commercial).

[^azur-3g30]: AZUR SPACE Solar Power GmbH, [*30% Triple-Junction GaAs Solar Cell Assembly, Type: TJ Solar Cell Assembly 3G30A*](https://www.azurspace.com/media/uploads/file_links/file/bdb_00010891-01-00_tj3g30-advanced_4x8.pdf) datasheet. Free PDF. Gives 29.5% BOL efficiency, full IV parameters, temperature coefficients and radiation degradation data against 1 MeV electron fluence. A good example of the level of detail a real space cell datasheet provides.

[^endurosat-1u]: EnduroSat, [*1U CubeSat Solar Panel X/Y*](https://satsearch.co/products/endurosat-1u-cubesat-solar-panel), via satsearch. Specifies two CESI CTJ30 cells per 1U panel at up to 29.5% efficiency, delivering up to 2.4 W per panel in LEO. Cited as a representative commercial 1U panel to calibrate what fits on a 100 × 100 mm face.

[^satsearch-batteries]: satsearch, ["Satellite batteries - for CubeSats, nanosats, and other form factors"](https://blog.satsearch.co/2021-06-23-satellite-batteries-for-cubesats-nanosats-and-other-form-factors) (June 2021). Open access. Vendor-by-vendor comparison of commercially available CubeSat battery packs with capacities, voltages, masses and operating temperature ranges. Useful for calibrating what is actually purchasable, but now several years old – confirm capacities, masses and temperature limits against the current datasheet before designing against them.

[^pycubed]: Maximillian Holliday et al., ["PyCubed: An Open-Source, Radiation-Tested CubeSat Platform Programmable Entirely in Python"](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf), *33rd Annual AIAA/USU Conference on Small Satellites*, SSC19-WKIII-04, 2019. Free PDF. Documents the integrated power/compute/radio/ADCS board and its total ionising dose test campaign – a rare published example of a CubeSat team justifying COTS part selection with real radiation data.