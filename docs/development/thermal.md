# Thermal Management

CubeSats are thermally awkward for reasons that follow directly from their size. There is very little thermal mass, so temperatures track the environment quickly instead of averaging it out. External surface area is scarce and already contested by solar cells, antennas and apertures, so there is rarely a spare face to use as a radiator. Everything is packed close together, so isolating a hot component from a cold-sensitive one is difficult. And the power budget rarely has room for active cooling.[^nasa-soa-thermal] The result is that most CubeSat thermal design is passive, and most of the work happens in the layout rather than in dedicated hardware.

## Thermal Environment in Orbit

In vacuum there is no convection. A spacecraft exchanges heat with its surroundings by radiation only, plus conduction internally between its own parts. That single fact drives everything else.

### Environmental heat sources

A CubeSat in [LEO](../references/glossary.md#leo) sees three external heat inputs:

- **Direct solar** – the dominant term. The [solar constant](../references/glossary.md#solar-constant) is **1367.5 W/m²** nominal at 1 AU, varying seasonally by about ±3.5% as Earth's distance from the Sun changes. NASA's recommended hot and cold design values sit at the ends of that swing: **1422 W/m² at perihelion** (northern winter) and **1318 W/m² at aphelion**, each 4.0% from nominal.[^gsfc-2301][^tfaws-environments]
- **[Albedo](../references/glossary.md#albedo)** – sunlight reflected off the Earth. Conventionally modelled as a fraction of the solar constant, with a nominal albedo factor of **0.30** and a recommended analysis range of **0.25 (cold) to 0.35 (hot)**.[^gsfc-2301] Real instantaneous values vary far more widely – from about 0.06 over ocean to 0.50 over cloud and ice – but short excursions matter less than they might, because a CubeSat's thermal time constant smooths them.[^tfaws-environments]
- **[Earth infrared](../references/glossary.md#earth-ir) (outgoing longwave radiation)** – the planet radiating as a roughly 255 K blackbody, giving about **241 W/m²** nominal, with analysis values typically spanning **214–267 W/m²**.[^gsfc-2301] Unlike albedo, Earth IR does not switch off in eclipse, which makes it the thing keeping your cold case from being much colder.

Internally, every watt the electronics consume becomes heat. On a small spacecraft this is not a rounding error. A 3U at 100 × 100 × 340.5 mm has about **0.16 m²** of external surface in total, so 6 W of internal dissipation is roughly 38 W/m² leaving the spacecraft – and radiation is the only route it has. That is the whole reason a CubeSat runs hot in sunlight and cold in eclipse with very little in between.

### Orbit and attitude effects

- **Eclipse cycling** is the fundamental driver. In LEO the spacecraft passes into and out of Earth's shadow every 90–105 minutes, spending **37–40% of each orbit in eclipse** at low [beta angles](../references/glossary.md#beta-angle) across the 300–600 km band where most CubeSats fly. The more useful number is the duration, which barely moves: **35 to 36 minutes** at every altitude in that band, because a higher orbit trades a longer period against a smaller shadow. Size heaters against those 35 minutes. Each cycle is a full thermal transient.
- **Beta angle** sets how much eclipse you get. Near β = 0° the eclipses are longest and the cold case is coldest. At high beta – a dawn–dusk sun-synchronous orbit, for instance – the spacecraft may see continuous sunlight, eliminating the cold case but making the hot case much harder. Both extremes need analysing, because beta angle changes over the year.
- **Attitude decides which face gets the Sun.** A nadir-pointing spacecraft has one face permanently looking at a 255 K Earth and another looking at deep space at 4 K. A sun-pointing one concentrates the solar load on a single face. A tumbling one averages everything, which is thermally benign and electrically terrible. See [GNC](gnc.md).
- **Altitude** affects both the fraction of sky filled by the Earth (and therefore how much albedo and IR you intercept) and the eclipse geometry.

### Hot case and cold case

Almost all CubeSat thermal analysis reduces to bounding two scenarios:

- **[Hot case](../references/glossary.md#hot-case-cold-case)**: maximum solar constant, high albedo, high Earth IR, worst-case attitude, all high-power modes active, end-of-life surface properties (degraded coatings absorb more).
- **Cold case**: minimum solar constant, low albedo and Earth IR, maximum eclipse, minimum internal dissipation – typically safe mode, where the spacecraft has shed load precisely when it most needs the waste heat.

The cold case catches teams out more often than the hot case, because safe mode looks like a good thing until you realise it means the battery is being kept warm by nothing.

<!-- CSR-RESOURCES:START dev-thermal-environment -->
- **[Introduction to On-Orbit Thermal Environments (TFAWS)](https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf)** `PDF` – Steven Rickman (NASA NESC) lecture on orbital thermal environments, with real albedo and outgoing longwave radiation distributions rather than the condensed design values. Free PDF
- **[Earth Orbit Environmental Heating (NASA GD-AP-2301)](https://extapps.ksc.nasa.gov/Reliability/Documents/Preferred_Practices/2301.pdf)** `PDF` – NASA preferred-practice guideline giving the recommended hot and cold design values for solar flux, albedo and Earth IR, with the combinations tabulated. Free PDF
- **[Intro to thermal balance for spacecraft by Scott Manley](https://www.youtube.com/watch?v=FlQYU3m1e80)** `Link` – Accessible video introduction to spacecraft thermal balance. Free
<!-- CSR-RESOURCES:END dev-thermal-environment -->

## Thermal Requirements and Limits

Thermal requirements come from components, and they come in two flavours that are frequently confused.

- **Operating limits** – the range over which a component meets its specification. Outside it, behaviour is undefined but the part is not necessarily damaged.
- **Survival limits** – the range the component can be exposed to while switched off without permanent damage. Always wider than the operating range.

Your thermal design must keep every component within its **survival** range at all times, and within its **operating** range whenever it is being used. These are different requirements and produce different analyses.

### Typical ranges

- **Industrial-grade electronics**: −40 to +85 °C operating. Most COTS CubeSat avionics.
- **Batteries**: the binding constraint on almost every CubeSat. A representative commercial space pack specifies roughly **0 to 45 °C for charging** against a materially wider discharge window.[^satsearch-batteries] Charging a lithium cell below 0 °C plates metallic lithium on the anode – permanent, cumulative damage rather than a derate – which is why battery heaters are near-universal. Use your own cell's datasheet; the shape is universal but the numbers are not. See [EPS – Energy Storage](eps.md#energy-storage).
- **Solar cells**: tolerant of wide swings, but output falls as they heat – the AZUR 3G30-Advanced loses **6.7 mV/°C on Vmp** and 6.2 mV/°C on Voc.[^azur-3g30] A panel in full sun can easily sit **40–60 °C above its cold-case temperature**, so string voltage has to be sized for the hot case. See [EPS – Cell technologies and efficiencies](eps.md#cell-technologies-and-efficiencies).
- **Optical payloads and star trackers**: often the tightest requirements, both absolute and in terms of gradients and stability, because focus and alignment shift with temperature.
- **Mechanisms and deployables**: lubricants, shape-memory actuators and burn wires all have temperature-dependent behaviour. See [Inhibits and HDRM](inhibits-hdrm.md).

### Margins

Analysis is uncertain, so requirements carry margin. A common approach is to require predicted temperatures to stay within component limits by a margin of around **±10 °C** at the analysis stage, tightening once the model has been correlated against thermal balance test data. Different programmes use different numbers – what matters is that the margin is stated, tracked and reduced deliberately as evidence accumulates, in the same way as the [budgets and margins](systems-engineering.md#budgets-and-margins) tracked elsewhere.

Build a **thermal limits table** early: every component, its operating and survival range, its dissipation in each mode, and where it sits in the spacecraft. It is a small document that prevents a lot of late surprises.

## Approaches to Thermal Management

### Passive Thermal Control

Passive control is the default and usually the whole answer. It costs no power, has no failure modes worth speaking of, and at CubeSat scale it is generally sufficient.

#### Surface finishes and coatings

Every external surface is characterised by two numbers: **solar [absorptivity](../references/glossary.md#absorptivity) (α)**, the fraction of incident sunlight absorbed, and **infrared [emissivity](../references/glossary.md#emissivity) (ε)**, how efficiently it radiates heat away. Their ratio **α/ε** determines equilibrium temperature in sunlight.

- **Low α/ε (cold coatings)** – matte white paint has low solar absorptivity and IR emissivity close to 1.0, making it the classic radiator finish. Second-surface silver FEP tape reaches solar absorptivity of about **0.08** with high emissivity, which is why it is the go-to radiator tape.[^nasa-soa-thermal]
- **High α/ε (hot coatings)** – polished or bare metal absorbs sunlight while radiating poorly, running hot. Sometimes exactly what you want on a cold-biased surface.
- **Metallised tapes** span a wide range, roughly **0.07 to 0.56 solar absorptivity** depending on the material.[^nasa-soa-thermal]

The critical caveat: **optical properties degrade in orbit**. Atomic oxygen erosion, UV darkening and contamination all tend to raise α while leaving ε roughly unchanged, so surfaces get hotter with age. NASA's survey puts it plainly – "thermal performance at beginning-of-life may not be the same at end-of-life."[^nasa-soa-thermal] Analyse both.

#### Conduction paths and thermal coupling

Inside a CubeSat, conduction through the structure is usually the dominant heat transfer mechanism, which makes the mechanical design and the thermal design the same design.

- **Deliberate coupling**: bolt a dissipating component hard to the frame with metal standoffs and thermal interface material, and the frame becomes its heat sink.
- **Deliberate isolation**: mount on polymer standoffs, use washers with low conductivity, or minimise contact area to keep a component thermally independent.
- **Thermal interface materials** – gap pads, greases and graphite sheets – matter far more than people expect. A bolted joint conducts through a small number of asperity contacts; the interface material fills the gaps. Check outgassing before selecting one (see [Structure – Materials](structure.md#materials-and-manufacturing)).
- **[Thermal straps](../references/glossary.md#thermal-strap)** move heat between points that must remain mechanically decoupled. Copper and aluminium braid are common; pyrolytic graphite sheet (PGS) offers higher conductivity than either in the same geometry.[^nasa-soa-thermal]

#### Radiators and geometry

A radiator is simply a surface with high ε and low α, with a clear view of deep space, coupled to whatever needs cooling. On a CubeSat the constraint is brutal: the faces are already covered in solar cells. Practical options are the anti-sun face on a sun-pointing spacecraft, the zenith face on a nadir-pointing one, or a deployed radiator that trades a mechanism for area.

#### Insulation and isolation

**[MLI](../references/glossary.md#mli)** works well at spacecraft scale and works poorly at CubeSat scale. NASA notes performance "drops drastically if compressed" and that edge effects create thermal short circuits – and on a 10 cm cube almost everything is edge.[^nasa-soa-thermal] It still has a role on specific components, but a blanket over a whole 1U is rarely the win it appears to be.

**[Phase change materials](../references/glossary.md#pcm)** buffer transients by absorbing latent heat: paraffins melting between 20 and 60 °C store **140–280 kJ/kg** depending on the formulation.[^nasa-soa-thermal] Attractive for a payload that pulses hard for a short period, at the cost of the containment housing's mass.

### Active Thermal Control

Active control costs power and adds failure modes, so it is used where passive genuinely cannot cope.

#### Heaters

Electrical heaters are by far the most common active element on a CubeSat, and for most missions the only one. Kapton polyimide flexible heaters offer power densities of **0.02–7.75 W/cm²** and are flight-proven at [TRL](../references/glossary.md#trl) 7–9 in LEO.[^nasa-soa-thermal]

Control approaches:

- **Thermostatic (bang-bang)** – a mechanical or solid-state thermostat closes below a set point and opens above it. Simple, and independent of software, which is exactly what you want protecting a battery.
- **Software-controlled** – the OBC reads temperature and drives a switched channel. More flexible, supports duty cycling and telemetry, but depends on software being alive.
- **Both.** The common pattern is a software loop for normal operation plus an independent hardware thermostat as a backstop, on the reasoning that the battery must survive even if the flight computer does not.

Heaters draw power exactly when the spacecraft is coldest, which is when it is in eclipse and generating nothing. This coupling has to appear explicitly in the [power budget](eps.md#power-requirements-and-budgets) cold case.

#### Other active techniques

Mostly out of reach at 1U–3U scale, but relevant for larger platforms and payload-driven missions:

- **Heat pipes** – passive two-phase devices moving heat with high effective conductivity. Flat-plate and conformable micro heat pipe variants have been demonstrated on 6U CubeSats, with flight heritage on larger smallsats.[^nasa-soa-thermal]
- **Cryocoolers** – for infrared detectors needing sub-100 K. Roughly 1U or smaller: Lockheed Martin's MICRO1-1 gives 1 W at 150 K for 0.35 kg and 15 W input; Ricor's K508N gives 0.2 W at 80 K for 0.475 kg and 5.5 W.[^nasa-soa-thermal] The input power is the problem.
- **Thermoelectric coolers** – solid-state Peltier devices, no moving parts, but inefficient and mechanically fragile.[^nasa-soa-thermal]
- **Louvers and pumped fluid loops** – standard on large spacecraft, generally too heavy and power-hungry below microsat scale, though sub-1U pumped loop demonstrators exist.[^nasa-soa-thermal]

## Thermal Modelling and Simulation

### Lumped-parameter models

Nearly all CubeSat thermal analysis uses a **[nodal (lumped-parameter) model](../references/glossary.md#nodal-model)**: the spacecraft is divided into a modest number of isothermal nodes, each with a thermal capacitance, connected by conductive and radiative couplings, driven by environmental and internal heat loads. The result is a set of coupled ordinary differential equations integrated forward in time.

The useful insight is that **model fidelity should follow the question**:

- A **single-node model** treats the whole spacecraft as one lump. It takes an afternoon, and it answers the first question that matters – roughly what temperature will this thing be? For an early feasibility check it is often enough.
- A **6-to-20-node model** (typically one node per external face plus a few internal masses) captures gradients between faces and identifies which surface needs which finish. This is where most CubeSat missions end up.
- A **detailed model** with dozens or hundreds of nodes is worth building when a payload has tight gradient requirements or when a specific component is marginal.

### Steady-state and transient

Steady-state solutions tell you where temperatures settle; transient solutions show the eclipse cycle. Because CubeSats have low thermal mass, they rarely reach steady state within one orbit – **transient analysis over several orbits is the meaningful case**, and it should be run until the orbit-to-orbit variation has converged.

### Tools

<!-- CSR-RESOURCES:START dev-thermal-modelling-tools -->
- **[Single-node thermal analysis Python script](https://github.com/MelbourneSpaceProgram/single-node-thermal-analysis)** `Link` – Melbourne Space Program's minimal single-node CubeSat thermal model in Python. MIT licence, open source
- **[SATMO](https://github.com/alexchipps/SATMO)** `Link` – Open-source MATLAB thermal analysis tool for CubeSats in low circular orbits, with analysis options for all major planets plus the Moon and Pluto. MIT licence, open source
- **[SATMO: a Multi-Planet Thermal Analysis Tool for CubeSat Missions](https://arxiv.org/abs/2512.07896)** `Link` – AIAA SciTech 2026 paper describing SATMO and its validation against Thermal Desktop. Open access preprint
<!-- CSR-RESOURCES:END dev-thermal-modelling-tools -->

SATMO is worth knowing about specifically because it closes a real gap: it is open source, needs only base MATLAB with no additional toolboxes, and its authors report agreement with Thermal Desktop to **within 1.17 °C** for a 1U CubeSat, validated at Venus, Earth and Mars.[^satmo] For a student team without access to commercial thermal software, that is a defensible analysis path rather than a rough estimate.

The commercial standards – ESATAN-TMS, Thermal Desktop (with SINDA/FLUINT), and Systema/Thermica – are what most reviewers expect to see, and several offer academic licensing. Many teams also build their own nodal solver in Python or MATLAB, which is a legitimate approach provided it is validated against a known case.

### Using models to inform design

A model that only produces a final answer has been under-used. The valuable outputs are sensitivities: which surface finish actually moves the hot case, how much the cold case depends on safe-mode dissipation, how much margin an extra thermal strap buys. Run parameter sweeps rather than single cases.

## Thermal Monitoring and Telemetry

### Sensor placement

Thermistors are cheap, small and low-power, so the usual mistake is fitting too few rather than too many. Prioritise:

- **The battery** – ideally more than one sensor, on the cells themselves rather than the board.
- **Each external face**, which is how you validate the model and diagnose attitude problems.
- **High-dissipation components** – transmitter PA, payload, [OBC](../references/glossary.md#obc).
- **Anything with a tight requirement** – optics, star tracker, oscillator.
- **The structure** at one or two reference points, as a baseline for everything else.

### Sampling and interpretation

- Sample fast enough to resolve an eclipse transient. Once per minute is usually plenty for structure; a fast-pulsing payload may need more.
- Record min/max between downlinks. Peak temperatures are what violate limits, and they are exactly what averaged telemetry hides.
- **Trend across orbits and months.** Slow warming over a mission is the classic signature of coating degradation; a step change usually means an attitude or configuration change.
- Correlate telemetry back to the model. On-orbit data is the final validation of your thermal model and is worth publishing – it is genuinely scarce in the literature.

## Thermal Interaction with Other Subsystems

Thermal design touches everything, which is why it belongs in [systems engineering](systems-engineering.md) rather than in a corner:

- **[EPS](eps.md)** – battery temperature limits are usually the tightest constraint on the spacecraft, heater power lands in the cold-case budget, and solar cell efficiency falls with panel temperature. Power and thermal converge or both fail.
- **[Payload](payload.md)** – often both the largest heat source and the component with the tightest requirements. Detectors in particular may need cooling or tight stability.
- **[OBC](obc.md)** – high-power compute concentrates dissipation in a small area. An SBC running a machine-learning workload is a thermal design driver, not just a power one.
- **[Comms](comms.md)** – transmitter power amplifiers are inefficient by nature, dumping most of their input as heat in short bursts during passes. Transient, localised, and easy to underestimate.
- **[Structure](structure.md)** – the frame is the primary conduction path and the mounting interface is where coupling is decided. Differential expansion between materials is a structural consequence of thermal design.
- **[GNC](gnc.md)** – attitude determines the thermal environment, and thermal gradients can distort optical bench alignment.

## Thermal Testing and Validation

### Thermal vacuum (TVAC) testing

**[TVAC](../references/glossary.md#tvac)** places the spacecraft in a vacuum chamber with a controlled thermal environment and is the only way to verify thermal behaviour realistically, because removing convection changes the answer completely.

Two distinct tests are often conflated:

- **Thermal cycling** demonstrates that the hardware survives and functions across its temperature range, and shakes out workmanship defects – cracked solder joints, marginal connectors. Driven by cycle count and range, not by matching flight conditions. A representative CubeSat campaign runs **8 cycles from −35 to +75 °C, with 2-hour dwells at the extremes and ramp rates below 2 K/min**.[^endurosat-qual]
- **Thermal balance** aims to reach steady-state conditions matching a specific predicted case, so the measured temperatures can be compared against the model and used to correct it. This is a **model correlation exercise**, and it is the one that tells you whether your analysis was right.

Most CubeSat programmes do cycling; fewer do balance. If your design has thermal margin, cycling may be enough. If it is marginal, balance is what turns an assumption into evidence. See [AIT – Environmental Testing](ait.md#environmental-testing).

### Correlating models to test

The point of correlation is to adjust uncertain model parameters – contact conductances, effective emissivities, interface resistances – until predictions match measurements, then re-run flight predictions with the corrected model. A correlation within a few degrees is a good result. A model that disagrees by 20 °C is telling you something important about your assumptions.

### Common pitfalls

- **Testing without vacuum.** Convection in air can carry away several times the heat that radiation does, so an ambient test tells you almost nothing about flight temperatures.
- **Chamber-induced artefacts.** Support fixtures conduct heat, and a poorly designed one becomes a heat leak that dominates the result. Design the test setup as carefully as the spacecraft.
- **Not reaching steady state.** Thermal balance requires genuine equilibrium; stopping early gives a number that looks like data but is not.
- **Insufficient instrumentation.** Add test thermocouples beyond the flight sensors – you cannot correlate what you did not measure.
- **Testing only the hot case.** The cold case with minimum dissipation is often the harder one and is easier to skip.

## Thermal Design Tradeoffs

- **Simplicity versus controllability.** A fully passive design has nothing to fail but also nothing to adjust once in orbit. Adding a heater gives you a control handle and a new failure mode. At CubeSat scale, favour passive until analysis proves you cannot.
- **Mass, power and complexity.** Thermal straps and PCM buy performance with mass; heaters buy it with power; deployable radiators buy it with mechanism risk. Each is a trade against budgets that other subsystems also want.
- **Worst case versus typical case.** Designing for the absolute worst-case combination of every parameter produces a heavy, over-constrained spacecraft. Designing for the typical case produces one that fails in a particular season. The usual compromise is bounding cases with explicit, stated margin.
- **Surface allocation is the real fight.** Every square centimetre is contested between solar cells, radiators, antennas and apertures. This is a systems-level decision that should be made explicitly and early, not settled by whoever finalises their CAD first.
- **Late changes cascade.** Changing a coating changes the hot case; adding a payload changes the internal dissipation; moving the battery changes everything. Keep the model current, because a stale thermal model is worse than none – it gives false confidence.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-thermal]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 7: Thermal Control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) (revision dated 7 May 2026). Open access. Source for coating optical properties, MLI limitations at small scale, heater power densities, phase change material latent heat figures, and cryocooler performance data.

[^gsfc-2301]: NASA Goddard Space Flight Center, [*Earth Orbit Environmental Heating*, Preferred Reliability Practice GD-AP-2301](https://extapps.ksc.nasa.gov/Reliability/Documents/Preferred_Practices/2301.pdf). Free PDF. Gives recommended design values: solar constant 1367.5 W/m² nominal with ±3.5% seasonal variation, and hot and cold cases of 1422.0 W/m² and 1318.0 W/m² at ±4.0% from nominal; albedo factor 0.30 nominal, 0.25 cold and 0.35 hot; and Earth-emitted IR of 241 W/m² for a 255 K Earth. Table 1 tabulates the nine solar-constant and albedo combinations, giving Earth-emitted energy from 214 W/m² (summer solstice, albedo 0.35) to 267 W/m² (winter solstice, albedo 0.25).

[^tfaws-environments]: Steven L. Rickman, NASA Engineering and Safety Center, [*Introduction to On-Orbit Thermal Environments*](https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf), Thermal and Fluids Analysis Workshop, 2014. Useful for showing how much real albedo and outgoing longwave radiation vary with location and averaging period, and how that variation is condensed into hot and cold design cases.

[^satmo]: Alexander Chipps, Daniel Forgette and Kerri Cahoy, ["SATMO: a Multi-Planet Thermal Analysis Tool for CubeSat Missions"](https://arxiv.org/abs/2512.07896), AIAA SciTech Forum 2026, DOI 10.2514/6.2026-2269. The AIAA version is paywalled; the arXiv preprint (submitted 4 December 2025) is open access and is what is linked here. Describes an open-source MATLAB thermal model representing the spacecraft as a six-sided box with one face-centred node per surface, validated against Thermal Desktop to within 1.17 °C for a 1U at Venus, Earth and Mars. The tool itself carries analysis options for all major planets plus the Moon and Pluto; those three are the validated set. Code at [github.com/alexchipps/SATMO](https://github.com/alexchipps/SATMO), MIT licence.

[^satsearch-batteries]: satsearch, ["Satellite batteries - for CubeSats, nanosats, and other form factors"](https://blog.satsearch.co/2021-06-23-satellite-batteries-for-cubesats-nanosats-and-other-form-factors) (June 2021). Open access. Vendor-by-vendor comparison of commercially available CubeSat battery packs with capacities, voltages, masses and operating temperature ranges. Useful for calibrating what is actually purchasable, but now several years old – confirm capacities, masses and temperature limits against the current datasheet before designing against them.

[^azur-3g30]: AZUR SPACE Solar Power GmbH, [*30% Triple-Junction GaAs Solar Cell Assembly, Type: TJ Solar Cell Assembly 3G30A*](https://www.azurspace.com/media/uploads/file_links/file/bdb_00010891-01-00_tj3g30-advanced_4x8.pdf) datasheet. Free PDF. Gives 29.5% BOL efficiency, full IV parameters, temperature coefficients of 6.2 mV/°C on Voc and 6.7 mV/°C on Vmp, and radiation degradation data against 1 MeV electron fluence.

[^endurosat-qual]: EnduroSat, ["Space Qualification – Satellite Testing Program"](https://www.endurosat.com/space-qualification/). Open access. Publishes the actual test levels used for its qualification and protoflight campaigns, including thermal vacuum cycling of 8 cycles from −35 to +75 °C with 2-hour dwells and ramp rates below 2 K/min. Useful as a concrete worked example of what a CubeSat qualification campaign actually consists of.