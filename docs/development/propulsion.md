# Propulsion

This page covers propulsion on a CubeSat: whether a mission needs it at all, the [delta-v](../references/glossary.md#delta-v) it buys and what that costs in propellant, the options that exist at CubeSat scale and how they trade thrust against efficiency and power, and the safety and regulatory requirements that arrive with the first pressurised tank. Attitude actuators are on [GNC](gnc.md); drag devices for disposal are on [Qualification and Launch](launch.md#space-debris-mitigation).

Most CubeSats fly without propulsion, and most of them are right to. A propulsion system is the one subsystem that changes your safety review, your launch options and your regulatory position all at once, so the first question is not which thruster but whether the mission can be flown without one. Increasingly the answer is no – disposal rules, constellation phasing and collision avoidance are pulling propulsion down into form factors that never carried it – which is why the question deserves an answer rather than an assumption.

## Do You Need It?

The reasons a CubeSat carries propulsion, roughly in order of how often they decide it:

- **Disposal compliance.** The five-year disposal rules now applied by the FCC and ESA put the commonly available 500–600 km sun-synchronous orbit on the wrong side of the line for a passive CubeSat. Lowering perigee at end of mission is one of the ways to comply; a drag device or a lower drop-off orbit are the others. See [Qualification and Launch – Space debris mitigation](launch.md#space-debris-mitigation).
- **Orbit maintenance and lifetime.** A CubeSat deployed low – from the ISS at 400–420 km, for instance – decays in months to a couple of years. Propulsion can buy back lifetime, at the cost of carrying the propellant to do it.
- **Phasing and constellation deployment.** Several spacecraft released from the same deployer share an orbit; spreading them around it needs a small delta-v applied at the right time, or a long wait for differential drag to do it slowly.
- **Collision avoidance.** Operators of large constellations increasingly expect other objects near them to be able to manoeuvre, and some regulators are beginning to ask.
- **Formation flying and rendezvous** – CanX-4/CanX-5 and the CPOD pair are the reference demonstrations.
- **Deep space and high orbits.** MarCO, BioSentinel, ArgoMoon and CAPSTONE all carried propulsion because there was no alternative.
- **Attitude control** – rarely on a CubeSat, because propellant is finite and magnetorquers are not. See [GNC – Thrusters](gnc.md#thrusters).

What it costs is less obvious than what it buys. A tank consumes internal volume that is scarcer than mass on a CubeSat. Electric propulsion consumes power at a scale most CubeSat buses cannot supply. The centre of mass moves as propellant is used, which the [ADCS](../references/glossary.md#adcs) has to know about. Plume impingement on solar cells, star trackers and optics has to be analysed. And the safety data package grows: a propulsion system is a stored-energy hazard in the same class as a battery, and it is reviewed as one – see [Safety and Launch Requirements](#safety-and-launch-requirements).

## Delta-v: The Currency

Every propulsion question reduces to delta-v – the velocity change the system can deliver – and the numbers at CubeSat scale are worth having in your head. From the vis-viva equation, for a circular orbit at 500 km:[^deltav]

- Raising or lowering the orbit by **100 km** costs about **55 m/s** as a two-burn Hohmann transfer – roughly **0.55 m/s per kilometre** anywhere in the CubeSat band.
- Dropping perigee from **550 km to 300 km** for disposal costs about **70 m/s** in a single burn at apogee. Circularising at 300 km would cost the same again, and is unnecessary: once perigee is in the denser atmosphere, drag finishes the job.
- Changing the orbital plane by **1°** costs about **130 m/s**, and 5° costs over 650 m/s. This is why a rideshare CubeSat lives with the primary's inclination: plane changes are unaffordable at this scale.

Delta-v turns into propellant mass through the rocket equation, and the [specific impulse](../references/glossary.md#specific-impulse-isp) is what sets the exchange rate. For a 10 kg 6U needing 70 m/s:[^deltav]

| Propulsion class | Representative Isp | Propellant for 70 m/s |
| :---- | ----: | ----: |
| Cold gas | 60 s | ~1.1 kg |
| Green monopropellant | 230 s | ~0.3 kg |
| Electrospray or ion | 1,000 s | ~70 g |
| Ion, high end | 2,000 s | ~35 g |

Two things to take from the table. Cold gas is simple but propellant-hungry: 70 m/s costs more than a tenth of the spacecraft's mass. And electric propulsion's advantage is large but is paid for in power and time – at 1 mN of thrust, the same 70 m/s on the same 10 kg is eight days of continuous thrusting, which is eight days of the power budget and eight days of holding the thrust vector.

A **delta-v budget** – allocated across phasing, maintenance, collision avoidance and disposal, with margin – is the propulsion equivalent of the power budget, and it belongs in [systems engineering](systems-engineering.md#the-main-budgets) from the first concept.

## Options at CubeSat Scale

NASA's state-of-the-art survey sorts small spacecraft propulsion into chemical, electric and propellant-less classes, and its summary table gives the ranges below.[^nasa-soa-propulsion] Read them as the spread of what has been built rather than what a particular product delivers.

| Class | Technology | Thrust | Isp (s) |
| :---- | :---- | :---- | ----: |
| Chemical | Hydrazine monopropellant | 0.25–28 N | 180–285 |
| Chemical | Alternative ("green") mono- and bipropellants | 50 mN–22 N | 150–310 |
| Chemical | Hybrids | 8–222 N | 215–300 |
| Chemical | Cold gas | 10 µN–3.6 N | 40–110 |
| Chemical | Solid motors | 37–461 N | 187–269 |
| Electric | Electrothermal (resistojets, arcjets) | 0.1 mN–1 N | 20–350 |
| Electric | Electrosprays | 20 µN–20 mN | 225–3,000 |
| Electric | Gridded ion | 0.1–20 mN | 500–3,000 |
| Electric | Hall-effect | 0.25–55 mN | 200–1,920 |
| Electric | Pulsed plasma and vacuum arc | 4–500 µN | 87–3,200 |
| Electric | Ambipolar | 0.5–17 mN | 400–1,100 |

### Cold gas

A pressurised gas – nitrogen, or a liquefied propellant such as R236fa that stores as a liquid and expands through the nozzle as a gas – released through a valve. The lowest Isp on the table and the simplest hardware on it. NASA's survey calls cold gas "often attractive and suitable for small buses due to their relatively low cost and complexity", and it has the deepest CubeSat flight record of any class:[^nasa-soa-propulsion] the two MarCO CubeSats carried VACCO R236fa systems to Mars in 2018, BioSentinel flew a Lightsey R236fa system on Artemis I in November 2022, and the CPOD pair demonstrated rendezvous with VACCO cold gas in 2022. The trade is the propellant mass above.

### Chemical monopropellants

Hydrazine is the incumbent on larger spacecraft and the exception on CubeSats. NASA's survey is direct about why: hydrazine and its derivatives "are corrosive, toxic, and potentially carcinogenic", and handling them requires self-contained protective suits, which few CubeSat programmes or launch sites will accommodate for a secondary payload.[^nasa-soa-propulsion] CAPSTONE, a 12U at 25 kg, flew a hydrazine system, but it was a primary payload on a dedicated launch.

The CubeSat-relevant alternatives are the **[green propellants](../references/glossary.md#green-propellant)** – ionic-liquid monopropellants such as LMP-103S and AF-M315E (ASCENT), and ADN-based blends – which deliver comparable or better Isp with far lower toxicity. The survey notes the practical consequence: under Air Force range safety requirements, external hydrazine leakage is classed as catastrophic, whereas ionic-liquid propellants reduce the hazard severity to critical or marginal, which "may enable projects to take a Design for Minimum Risk (DFMR) approach" and require fewer serial valves.[^nasa-soa-propulsion] LituanicaSAT-2 flew a NanoAvionics ADN monopropellant system on a 3U in 2017. Water electrolysis – PTD-1's HYDROS-C, which splits stored water into hydrogen and oxygen and burns them as a bipropellant – is the other route to a benign propellant, launched in January 2021.[^nasa-soa-propulsion]

### Electric propulsion

Electric propulsion buys Isp with electrical power, and on a CubeSat the power is the constraint. NASA's survey puts the thrust-to-power of electric systems "below 75 mN/kW", so that "a small spacecraft capable of delivering 500 W to an electric propulsion system may generate no more than 38 mN of thrust" – and 500 W is an order of magnitude beyond what a 6U generates.[^nasa-soa-propulsion] At the tens of watts a CubeSat can spare, thrust is in the tens of micronewtons to a few millinewtons, and manoeuvres take days to weeks of continuous operation.

Within that constraint the classes differ in what they demand:

- **Electrosprays** and **pulsed plasma / vacuum arc thrusters** are the smallest and lowest-power options, with Isp into the thousands of seconds, and are the natural fit below 6U.
- **Gridded ion** and **Hall-effect** thrusters are the mature high-Isp technologies from larger spacecraft, scaled down; **iodine** as a solid-stored propellant removes the pressurised tank, and the ThrustMe I2T5 flown in 2019 was the first iodine system spaceflight-tested.[^nasa-soa-propulsion]
- **Resistojets** and other electrothermal devices heat a propellant electrically for a modest Isp gain over cold gas at modest power.

The systems consequence is that electric propulsion is a power and thermal design problem before it is a propulsion problem: the [EPS](eps.md#power-requirements-and-budgets) has to supply it, the [thermal design](thermal.md) has to reject its inefficiency, and the [ADCS](gnc.md) has to hold the thrust vector for the whole burn.

### Solid motors

High thrust, single use, and rare on CubeSats – they bring energetic material into the safety package and offer no restart. Relevant mainly for a one-off orbit-raising or a fast deorbit.

### Propellant-less

Solar sails, electrodynamic tethers and drag devices carry no propellant and are, strictly, not propulsion, but they compete with it for the disposal job. NASA's survey notes that propellant-less technologies "have yet to move beyond small-scale demonstrations" as propulsion,[^nasa-soa-propulsion] whereas drag devices are an established disposal answer: deployable for suitable area-to-mass ratios at altitudes up to about 800 km to meet a five-year requirement.[^nasa-soa-deorbit] If disposal is the only reason you were considering a thruster, a drag sail is usually the lighter, safer and cheaper answer – see [Qualification and Launch – Space debris mitigation](launch.md#space-debris-mitigation) and [Structure – Deployable Structures and Mechanisms](structure.md#deployable-structures-and-mechanisms).

<!-- CSR-RESOURCES:START dev-propulsion-surveys-and-standards -->
- **[NASA State of the Art – In-Space Propulsion](https://www.nasa.gov/smallsat-institute/sst-soa/in-space-propulsion/)** `Link` – Chapter 4 of NASA's small spacecraft survey: chemical, electric and propellant-less systems with thrust and Isp ranges, flight examples and maturity assessments. Open access
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – Section 2.1 carries the propulsion requirements: AFSPCMAN 91-710 Volume 3 compliance and at least three inhibits to activation. Free PDF
<!-- CSR-RESOURCES:END dev-propulsion-surveys-and-standards -->

## Choosing

The decision usually falls out of three questions, in order:

1. **How much delta-v, and by when?** Disposal at end of life tolerates a slow, low-thrust system; collision avoidance and phasing do not. If a manoeuvre has to happen inside a day, electric propulsion at CubeSat power levels is out.
2. **How much power and volume can the bus spare?** A cold gas or green monopropellant system needs almost no power and a tank; an electric system needs a power processing unit, tens of watts sustained, and a thermal path for the losses.
3. **What will the launch provider accept?** Pressurised systems, hazardous propellants and stored energy all appear in the safety review, and ISS deployment routes are the most restrictive of all. A propulsion choice that your provider will not fly is not a choice. Ask before you design, not after.

For a first mission with a modest disposal requirement, the ranking is: a lower orbit or a drag device first, cold gas or a green monopropellant second, electric propulsion only when the delta-v cannot be carried any other way.

## Safety and Launch Requirements

The [CDS](../references/glossary.md#cds) treats propulsion as its own hazard class. CubeSats with propulsion "shall be designed, integrated and tested in accordance with AFSPCMAN 91-710 Volume 3" (§2.1.3), the Air Force range safety standard, and must carry **at least three inhibits to activation** (§2.1.4) – the same independence rules that apply to RF and deployable inhibits, covered in full under [Inhibits and HDRM](inhibits-hdrm.md#how-many-are-required).[^cds-rev14]

<!-- NEEDS HUMAN VERIFICATION: CDS 14.1 §2.1 also constrains pressure vessels and total stored energy (Rev. 13 §3.1.4 limited stored chemical energy; the pressure vessel factor of safety and the 14.1 clause numbers could not be confirmed from a fetch). A read of §2.1.1–2.1.2 in the local PDF would let the limits be quoted here. -->

In practice the review turns on the hazard classification of the propellant and the pressure in the system, and the classification decides how many barriers you owe – which is the argument for green propellants and for iodine or liquefied propellants that store at low pressure. Expect to supply the same class of evidence as for batteries: a description of the system, its pressures and materials, the inhibit block diagram showing three physical breaks in the power path to the valves, proof-pressure and leak test results, and a hazard analysis. See [Inhibits and HDRM – Documentation and Compliance](inhibits-hdrm.md#documentation-and-compliance).

Two more consequences reach beyond the safety package. A propulsive spacecraft is expected to have a plan for what it does with that capability – which orbits it may occupy, how it avoids other objects, how it disposes of itself – and your licensing authority may ask for it as part of the debris assessment. And it changes the [export control](launch.md#export-control) picture: propulsion components are among the items most likely to be controlled.

## Integration Considerations

- **Volume before mass.** A tank is a rigid, incompressible block in a spacecraft where every cubic centimetre is contested. Reserve it in the first layout; it will not fit later.
- **Centre of mass moves.** Propellant is consumed from a fixed location, so the centre of mass shifts through the mission and the thrust vector rarely passes through it. The offset is a disturbance torque the [ADCS](gnc.md#disturbances-and-space-environment) has to absorb during every burn, and the [structure page's](structure.md#mass-properties-and-centre-of-mass) advice to keep dense items central applies with force.
- **Plume impingement.** Thruster exhaust that reaches solar cells, optics, radiators or a star tracker baffle degrades them. Model the plume against the deployed configuration, not the stowed one.
- **Power and thermal.** Valves and heaters for chemical systems are modest; the power processing unit of an electric system is not, and neither is its waste heat. Both belong in the [power](eps.md) and [thermal](thermal.md) budgets from the start.
- **Propellant thermal limits.** Liquid and liquefied-gas propellants freeze, and their vapour pressure – and therefore the thrust – depends on temperature. The tank usually needs a heater and a survival-limit entry in the [thermal limits table](thermal.md#thermal-requirements-and-limits).
- **Inhibits and timers.** The propulsion inhibit chain is part of the power architecture, alongside the RF and deployable chains, and it has to survive the first boot in orbit without a valve opening. See [EPS – Inhibits and Deployment Safety](eps.md#inhibits-and-deployment-safety).
- **Attitude coupling.** Every burn is an attitude manoeuvre: the spacecraft must point the thrust vector, hold it for the burn, and dump whatever momentum the offset thrust deposits. Plan the [ADCS modes](gnc.md#modes-of-operation) with the propulsion system, not after it.
- **Software.** Firing a thruster is an irreversible command in the same class as a deployment: arm-then-fire, time-limited, and never able to run without an attitude solution. See [Flight Software – Commands](flight-software.md#commands).

## Testing

- **Leak and proof-pressure tests** on the assembled system, before and after vibration, are what the safety review will ask for first.
- **Hot-fire or thrust characterisation in vacuum**, because the thrust and Isp of most CubeSat systems are not what they are in air. For electric systems this means a vacuum chamber with a thrust balance – a facility most teams borrow.
- **Valve cycling and dry-actuation counts**, with the same discipline as any mechanism: many cycles, at temperature extremes, after vibration. See [AIT – Environmental Testing](ait.md#environmental-testing).
- **Inhibit verification** through the full state matrix, exactly as for RF and deployables. See [Inhibits and HDRM – Verification and Testing](inhibits-hdrm.md#verification-and-testing).
- **Day-in-the-life** rehearsals that include a burn sequence end to end – command, attitude, firing, momentum dump, telemetry – on the flatsat with a simulated thruster, before the real one is ever powered.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-propulsion]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 4: In-Space Propulsion](https://www.nasa.gov/smallsat-institute/sst-soa/in-space-propulsion/) (revision dated 7 May 2026). Open access. Source for the thrust and specific impulse ranges in Table 4-1 (hydrazine, alternative mono- and bipropellants, hybrids, cold gas, solids, electrothermal, electrosprays, gridded ion, Hall-effect, pulsed plasma and vacuum arc, ambipolar), the thrust-to-power statement for electric propulsion ("below 75 mN/kW", 500 W giving "no more than 38 mN"), the hydrazine hazard description, the range-safety hazard classification of ionic-liquid propellants and the Design for Minimum Risk approach, the assessment of cold gas for small buses, the mission examples (MarCO, BioSentinel, CPOD, CanX-4/5, CAPSTONE, ArgoMoon, LituanicaSAT-2, PTD-1) and the ThrustMe I2T5 iodine module, and the statement that propellant-less technologies remain at small-scale demonstration.

[^deltav]: Worked from first principles rather than cited, so the assumptions are visible. Circular velocity v = √(μ/r) with μ = 398,600 km³/s² and R_E = 6,371 km; transfer velocities from the vis-viva equation v² = μ(2/r − 1/a). A Hohmann transfer from 400 to 500 km costs 28.1 + 28.0 = 56 m/s; from 500 to 600 km, 55 m/s. Lowering perigee from a 550 km circular orbit to 300 km is a single burn of 70 m/s at apogee; circularising at 300 km would cost a further 71 m/s. A plane change of Δi at 7.62 km/s costs 2v·sin(Δi/2): 133 m/s for 1°, 664 m/s for 5°. Propellant mass from the rocket equation, m_p = m₀(1 − e^(−Δv/(Isp·g₀))) with m₀ = 10 kg and Δv = 70 m/s: 1.12 kg at Isp 60 s, 0.31 kg at 230 s, 71 g at 1,000 s, 36 g at 2,000 s. Thrusting time at constant 1 mN for 70 m/s on 10 kg: 7.0 × 10⁵ s, about 8.1 days.

[^cds-rev14]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 14.1*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (9 February 2022). Free PDF. Source for the propulsion requirements: design, integration and testing in accordance with AFSPCMAN 91-710 Volume 3 (§2.1.3) and at least three inhibits to activation of a propulsion system (§2.1.4).

[^nasa-soa-deorbit]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 13: Deorbit Systems](https://www.nasa.gov/smallsat-institute/sst-soa/deorbit-systems/). Open access. States that drag devices can be deployed "for certain area-to-mass ratios in altitudes equal to or lower than 800 km" to meet the five-year requirement, and that natural decay in under five years "can be achieved for most SmallSats at altitudes <400 km".
