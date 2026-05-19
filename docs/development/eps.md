# Electrical Power Systems (EPS)

This section covers power generation (solar panels), storage (batteries and BMS), conditioning and distribution (EPS and power buses).

## Power Requirements and Budgets

A **power budget** is the bookkeeping exercise that tells you whether your spacecraft will stay alive in orbit. On one side: how much energy each subsystem draws and for how long, across every mission mode. On the other: how much your solar panels and batteries can supply across every [orbit](#) phase. If the second number isn't comfortably bigger than the first, you don't have a flyable design.

Power budgets are rarely a one-pass calculation. They evolve from coarse estimates at concept stage to detailed worst-case-orbit analyses by [CDR](../references/glossary.md#cdr), and they're updated continuously as components are selected, tested, and replaced.

### Estimating consumption

- **Component-level draws**: collect current and voltage figures for every active component from datasheets – receivers, transmitters, [OBC](../references/glossary.md#obc), [ADCS](../references/glossary.md#adcs) sensors and actuators, payload, heaters. Use worst-case (max) values, not typical.
- **Operational modes**: most CubeSats have 4-6 modes (e.g. safe, nominal, comms, payload, detumble). Each mode activates a different set of components and so has a different power profile.
- **Duty cycles**: many components don't run continuously. A transmitter might be active 5 minutes per orbit; a payload might pulse for 10 seconds per minute. Average power = peak power × duty cycle.
- **Orbit-average power ([OAP](../references/glossary.md#oap))**: the time-weighted sum of consumption across all modes over a representative orbit. This is the headline number generation must beat.[^hawaii-budget]

### Estimating generation

- **Solar input**: depends on cell efficiency, panel area, sun-incidence angle, and [beta angle](../references/glossary.md#beta-angle) (which drives eclipse fraction).
- **[Eclipse fraction](../references/glossary.md#eclipse-fraction)**: a typical [LEO](../references/glossary.md#leo) orbit spends 30-35% of its period in eclipse, but this varies seasonally and with orbit geometry. Equatorial orbits eclipse longer than high-beta-angle orbits.
- **Pointing**: a tumbling spacecraft generates far less than a stable, sun-pointing one. Account for this honestly during early phases – assuming nominal pointing before you've proven your [ADCS](../references/glossary.md#adcs) works is a classic source of negative-budget surprises.[^clyde-space]
- **Degradation**: solar cell efficiency drops over time in the LEO radiation environment. The rate varies significantly by cell technology and orbital altitude – triple-junction (TJ) cells degrade the least, silicon cells the most, with small satellites (under 10 kg) experiencing higher rates than larger ones due to lower thermal inertia and shielding.[^degradation] A common planning figure is 1-3% per year for quality cells with coverglass; size your panels for end-of-life, not beginning-of-life.[^hawaii-gen]

A more detailed photovoltaic generation analysis (often called a **PV budget**) breaks out these factors panel-by-panel and over time, and is worth doing separately once orbit and attitude assumptions firm up.

### Margins and derating

- 30% margin at [PDR](../references/glossary.md#pdr) is conservative; 20% at [CDR](../references/glossary.md#cdr) is typical; 10% at flight is acceptable if the budget has been validated against test data.[^clyde-space]
- Battery [depth-of-discharge](../references/glossary.md#dod-battery) is usually kept below 20-30% to preserve cycle life over the mission.
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

To be added here:

- Body-mounted vs. deployable solar panels
- Cell technologies and efficiencies
- Illumination, eclipses, and incidence angles
- Wiring, blocking diodes, and degradation over time

### Solar cell datasheets

<!-- CSR-RESOURCES:START development-eps-solar-cell-datasheets -->
-- **[LightFoundry Space Grade 30% Efficiency GaAs 14466 Solar Cell Datasheet](https://storage.googleapis.com/cubesat-resources/resources/development-eps-solar-cell-datasheets/datasheet-lightfoundry-space-grade-30-efficiency-gaas-6-inch-solar-cell-assembly-g2qiev.pdf)** `PDF` – Space-grade 30 percent GaAs solar cell datasheet
<!-- CSR-RESOURCES:END development-eps-solar-cell-datasheets -->

### MPPT and power management

<!-- CSR-RESOURCES:START mppt-algorithms -->
- **[Deep Learning-Based MPPT Approach to Enhance CubeSat Power Generation](https://ieeexplore.ieee.org/document/10904144)** `Link` – Paper on deep-learning MPPT for CubeSats
<!-- CSR-RESOURCES:END mppt-algorithms -->
## Energy Storage

To be added here:

- Battery chemistries used in CubeSats
- Capacity sizing and depth-of-discharge
- Charge and discharge limitations
- Lifetime, degradation, and safety considerations

## Battery Management Systems (BMS)

To be added here:

- Cell balancing approaches
- Over-voltage, under-voltage, and over-current protection
- Temperature monitoring and cutoffs
- Interaction between BMS and EPS logic

## Power Conditioning and Regulation

To be added here:

- Maximum power point tracking (MPPT)
- Buck, boost, and buck-boost converters
- Efficiency vs. noise tradeoffs
- Startup and brownout behaviour

## Power Distribution and Buses

To be added here:

- Common bus voltages (e.g. unregulated battery, 3.3 V, 5 V, 12 V)
- Switched vs. always-on loads
- High-side vs. low-side switching
- Connector and harness considerations

## Power Switching and Protection

To be added here:

- Load switches and current limiters
- Fuses, polyfuses, and electronic protection
- Inrush current management
- Fault containment and isolation

## Inhibits and Deployment Safety

See also: [Inhibits and HDRM](inhibits-hdrm.md).  

## EPS Monitoring and Telemetry

To be added here:

- Voltage, current, and temperature sensing
- Telemetry resolution and sampling rates
- Using power telemetry for fault detection
- Ground-based analysis and trending

## EPS Integration Considerations

To be added here:

- Coupling with thermal design
- Interaction with flight software and modes
- Ground testing and power simulation
- Common integration pitfalls

---

👉 **Please consider [contributing](../contributing.md)!**

[^hawaii-budget]: University of Hawaiʻi, *A Guide to CubeSat Mission and Bus Design*, §5.9 ["Power Budget and Profiling"](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-9-power-budget-and-profiling/) – walks through the OAP methodology step by step using the Artemis CubeSat Kit as a worked example. Open access.

[^clyde-space]: Craig Clark and Ritchie Logan (Clyde Space), ["Power Budgets for Mission Success"](http://mstl.atl.calpoly.edu/~workshop/archive/2011/Spring/Day%203/1610%20-%20Clark%20-%20Power%20Budgets%20for%20CubeSat%20Mission%20Success.pdf), Cal Poly CubeSat Workshop, April 2011. Practical slide deck on estimating OAP, managing loads, and avoiding negative budgets. One of the most-cited introductory treatments.

[^degradation]: Yermek Amangeldi et al., ["Degradation Modeling and Telemetry-Based Analysis of Solar Cells in LEO for Nano- and Pico-Satellites"](https://www.mdpi.com/2076-3417/15/16/9208), *Applied Sciences*, 15(16), 2025. Open access. Reports that GaAs cells degrade 4.5-7.0% over typical mission lifetimes at 300-700 km altitude, with TJ cells showing the highest radiation resistance and Si cells the most pronounced loss below 500 km. Smaller satellites (<10 kg) show higher rates than larger ones.

[^hawaii-gen]: University of Hawaiʻi, *A Guide to CubeSat Mission and Bus Design*, §5.5 ["Power Generation"](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-5-power-generation/). Notes that ionizing radiation effects on solar cells can be mitigated by coverglass, with typical loss figures of 1-10% per year depending on cell technology and shielding. Open access.