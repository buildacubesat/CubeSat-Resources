# Inhibits and Hold Down & Release Mechanisms (HDRM)

This section covers inhibit systems and Hold Down and Release Mechanisms (HDRM) used in CubeSats to ensure launch safety and controlled deployment. Topics include remove-before-flight (RBF) pins, deployment switches, separation detection, timers for delayed RF operations, burn wires, and other release mechanisms. Proper inhibit design is critical for regulatory compliance, launch vehicle safety, and mission success.

This is the part of a CubeSat that exists entirely for other people's benefit. Inhibits do nothing for your mission — their only job is to guarantee that your spacecraft cannot do anything hazardous while it is inside someone else's rocket, next to someone else's payload, and sometimes inside a crewed vehicle. They are also, for the same reason, the part of your design most likely to be examined line by line in a safety review.

## Purpose and Safety Context

### The hazards being controlled

A CubeSat inside a [deployer](../references/glossary.md#deployer) is a sealed box containing stored electrical energy, a radio transmitter, and spring-loaded mechanisms. Three things must not happen before deployment:

- **Inadvertent RF transmission**, which could interfere with launch vehicle telemetry and range safety systems at exactly the moment when nobody can afford interference.
- **Inadvertent deployment**, where an antenna or solar panel releasing inside the deployer jams it — destroying your mission and potentially the co-passengers in the same pod.
- **Uncontrolled energy release** — a battery fault, thermal runaway, or unexpected current draw inside a sealed volume.

### Mission phases

The inhibit architecture divides the mission's early life into distinct states:

1. **Ground handling and transport** — the [RBF pin](../references/glossary.md#rbf-pin) is inserted and the spacecraft is completely dead.
2. **Integration into the deployer** — RBF removed (if the deployer has no access port), [deployment switches](../references/glossary.md#deployment-switch) held actuated by the deployer walls. The spacecraft remains off.
3. **Launch and ascent** — unchanged. The CubeSat is a passive mass.
4. **Ejection** — the deployment switches release, power reaches the spacecraft, and the timers start.
5. **Post-deployment quiet period** — powered and booting, but not transmitting and not deploying anything.
6. **Commissioning** — after the mandated delays, RF and deployables are enabled.

### Relationship to reviews and licensing

Inhibit design is reviewed by your launch provider as part of the safety data package, and the evidence you supply — diagrams, test results, photographs — is what gets accepted or rejected. It also intersects with your frequency licence, since regulators care about when you start transmitting. See [Qualification and Launch](launch.md#regulatory-requirements).

## Inhibit Types and Architectures

### What counts as an inhibit

The [CDS](../references/glossary.md#cds) is precise about this, and the precision matters:

> "An inhibit is a physical device between a power source and a hazard." (CDS 14.1 §2.3.7.1)

And equally important:

> "A timer is not considered an independent inhibit." (CDS 14.1 §2.3.7.2)

This second point catches many first-time teams. Software delays and timers are required by the specification for the post-deployment quiet period, but they do **not** count toward the inhibit count. An inhibit must be a physical interruption in the power path.

### How many are required

CDS Rev 14.1 requires:

- **At least three independent RF inhibits** to prevent inadvertent transmission (§2.3.7).
- **At least three independent inhibits** to prevent inadvertent release of any deployable structure such as antennas or solar panels (§2.3.8).

Independence is the operative word: three switches in series driven by the same mechanism are one inhibit, not three. Each must be capable of failing independently of the others.
<!-- NEEDS HUMAN VERIFICATION: Rev 14.1 clearly states three independent inhibits. A great deal of older CubeSat material quotes two, which I believe reflects earlier CDS revisions and some non-crewed launch provider requirements — but I could not confirm the exact history, so I have not asserted it. Worth a sentence if you know the provenance, since readers will encounter the older figure. -->

Your launch provider may require more, particularly for ISS deployment where the CubeSat spends time inside a crewed vehicle. As always, **the payload user guide takes precedence over the CDS** — see [Structure – The launch provider always wins](structure.md#the-launch-provider-always-wins).

### Architectural patterns

The conventional CubeSat implementation uses three physically distinct devices in the power path:

- **Deployment switch A** — released by the deployer wall or door.
- **Deployment switch B** — a second, independently located switch.
- **RBF pin** — removed before flight, and a third independent break while present.

Some designs substitute a separate hardware timer or a latching relay for one of these. What matters to a reviewer is that you can draw the power path, show three physical breaks in it, and demonstrate that no single failure closes more than one.

Design principles:

- **Normally-open is the safe default.** The hazard is disabled unless something actively enables it. A normally-closed inhibit that must be actively held open fails dangerous.
- **Inhibit the source, not the sink.** Break the power path high in the tree, not at the last device before the antenna.
- **Separate the deployable and RF inhibit chains** where practical, so a fault in one does not compromise the other.
- **Keep it dumb.** Inhibits should be verifiable with a multimeter, not by reading code.

### Inhibit Interaction with the Electrical Power System (EPS)

Inhibits are, physically, part of the power architecture, which means the [EPS](eps.md) and inhibit designs have to be developed together.

- **The CDS requires the power system to be off throughout launch**: "the CubeSat power system shall be at a power off state from the time of delivery to the LV through on-orbit deployment" (§2.3.1). Powered functions in scope include command and data handling, RF communication, attitude determination and control, and deployable actuation (§2.3.1.2).
- **The deployment switch must electrically disconnect the power system from the powered functions** when actuated (§2.3.2.1) — not merely signal software that it is time to stay quiet.
- **Battery self-discharge** over what may be months of storage and launch delay is a real planning problem. Confirm the pack will still be above its minimum voltage at deployment, and check whether your deployer's access port allows top-up charging late in the flow (§2.3.4).
- **Controlled energisation on release.** When the switches open, everything comes up at once, on a cold battery, in the worst condition of the mission. See [EPS – Startup and brownout behaviour](eps.md#startup-and-brownout-behaviour).
- **Battery circuit protection** is separately required by the CDS (§2.3.6) to prevent unbalanced cell conditions. See [EPS – BMS](eps.md#battery-management-systems-bms).

### Remove-Before-Flight (RBF) Pins

The RBF pin is a physical object inserted into the spacecraft that breaks the power path, with a large brightly coloured streamer attached so that nobody can possibly forget it is there.

The CDS requirements are specific:

- "The CubeSat shall include an RBF pin, which cuts **all** power to the satellite once it is inserted." (§2.3.5) — all power, not most of it.
- It "shall be removed from the CubeSat before integration into the dispenser, if the dispenser does not have access ports." (§2.3.5.1)
- It "shall protrude no more than 6.5 mm from the CubeSat rail surface when it is fully inserted." (§2.3.5.2)

Practical implementation notes:

- The usual mechanism is an insulating blade that separates two spring contacts. Simple, inspectable, and with no failure mode more subtle than "bent".
- **Position it in an accessible face** consistent with your deployer's access port geometry. Retrofitting an RBF port into a finished structure is painful — see [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **Human factors are the actual risk.** The pin gets removed at a busy moment, by someone who may not be from your team, often under time pressure. Make it impossible to reinsert backwards, impossible to leave half-inserted without it being obvious, and make the streamer big.
- **Verify continuity, don't assume it.** A pin can be present and not making contact; a pin can be absent and the contacts stuck closed. Measure.
- Repeated insertion wears the contacts. Track the cycle count and inspect before flight.

### Deployment Switches and Separation Detection

Deployment switches are how the spacecraft knows it has left the deployer.

CDS requirements:

- "The CubeSat shall have, at a minimum, one deployment switch, which is actuated while integrated in the dispenser." (§2.3.2)
- "The deployment switch shall be in the actuated state at all times while integrated in the dispenser." (§2.3.2.2)
- It should sit at or below the external surface that interfaces with the dispenser, so it cannot be damaged during integration (§2.3.2.3).
- Critically: "If the CubeSat deployment switch toggles from the actuated state and back, the satellite shall reset to a pre-launch state, including reset of transmission and deployable timers." (§2.3.2.4)

That last requirement is the interesting one. It exists because a switch can bounce or momentarily open during vibration, and the specification refuses to allow a transient to start your quiet-period timers early. **Your implementation must genuinely reset the timers, not just note the event** — and it must do so in a way that survives whatever state the software was in.

Implementation notes:

- **Two switches, independently located** — commonly on separate rails or on a rail and the deployer door face — so a single mechanical failure does not release the inhibit.
- **Debounce in hardware where the signal gates power**, and in software where it feeds logic. Contact bounce during ejection is real.
- **The separation signal is also useful telemetry.** Record the time of separation and the switch states; it is the T-zero for everything that follows and one of the few pieces of ground-truth data you get about deployment.
- Test the switches after vibration, not only before. Their whole job is to survive that environment and still work.

### Timers and Delayed Activation

The CDS mandates two quiet periods, and they are measured from different events:

- **Deployables**: "All deployables such as booms, antennas, and solar panels shall wait to deploy a minimum of 30 minutes after the CubeSat's deployment switch(es) are activated during dispenser ejection." (§2.4.4)
- **RF**: "CubeSats shall not generate or transmit a signal earlier than 45 minutes after on-orbit deployment." (§2.4.5)

The spacecraft may power on immediately after deployment (§2.4.5.1) — the restriction is on transmitting and deploying, not on being alive. Use that time: boot, assess health, start charging, begin detumbling.

Implementation:

- **Hardware timers are preferred** for the RF inhibit release, because a hardware timer cannot be defeated by a software fault, a reset loop, or a corrupted image. A dedicated timer IC that must expire before the transmitter's power path can close is easy to demonstrate to a reviewer.
- **Software timers must survive resets.** If the OBC reboots at T+20 minutes and the timer restarts from zero, you have not violated the requirement — you have merely delayed yourself. If it reboots and *loses* the fact that it has not yet waited, you have violated it. Store elapsed time in non-volatile memory and treat the requirement conservatively.
- **Watchdog interaction** is the subtle case. A watchdog reset during the quiet period must not clear the inhibit state. Think through the interaction explicitly. See [OBC – Watchdogs](obc.md#watchdogs).
- **Add margin.** Waiting 35 and 50 minutes rather than exactly 30 and 45 costs nothing and removes any argument about clock accuracy.
- **Check your provider's numbers.** Some require longer, and ISS deployment has its own regime.

## Hold Down and Release Mechanisms (HDRM)

An HDRM holds a deployable stowed against launch loads and releases it on command. From the structural side it must carry real preload; from the electrical side it must not fire early; from the reliability side it is a single-use, single-point-of-failure device on which the mission may depend.

The context worth keeping in mind: NASA's state-of-the-art survey attributes **more than 10% of reported small satellite failures to mechanisms**, and recommends "design simplicity, margin, supplier selection, and testing" as the mitigations. See [Structure – Deployable Structures and Mechanisms](structure.md#deployable-structures-and-mechanisms).

### Functional requirements

- **Preload**: enough to prevent any relative motion under launch vibration. A deployable that rattles will fret, generate debris, and may fail its own hinge.
- **Release reliability**: it must actuate on command, in vacuum, at whatever temperature it happens to be.
- **Non-actuation reliability**: equally important — it must *not* actuate before commanded, including during vibration and thermal cycling.
- **Contained release**: no fragments, no debris. This rules out several mechanisms that would otherwise be attractive.
- **Ground resettability** is a practical requirement rather than a flight one, but it matters enormously: a mechanism you can only test once is a mechanism you have effectively not tested.

### Burn Wire–Based HDRM

The classic CubeSat mechanism, and still the most common: a synthetic line under tension restrains the deployable; a resistive element heats and melts or severs the line; springs do the rest.

- **Principle.** A nichrome wire or resistor is pressed against a loop of Dyneema, Vectran or similar. Current through the heater raises it above the line's melting point and the line parts.
- **Power.** Typically a few watts for a few seconds — modest energy, but a significant *peak* draw at a moment when the battery may be cold and partly discharged. Budget it explicitly and consider requiring a state-of-charge threshold before actuation. See [EPS](eps.md#power-requirements-and-budgets).
- **Vacuum changes the thermal behaviour completely.** With no convection, the heater runs much hotter for the same power, and burn times measured in air are not valid. **Always characterise burn wire release in vacuum.**
- **Redundancy.** NASA's CubeSat 101 recommends using **two separate burn wires** for a constrained deployable.[^cubesat101] Better still is two independent heaters on independent power channels, so neither a heater failure nor a switch failure prevents release.
- **Failure modes**: line not fully severed and snagging; heater open-circuit; line creeping under preload and going slack over months of storage; melted line residue contaminating a nearby optical surface; heater damaging adjacent structure.
- **Verification.** Test many times, after vibration, at temperature extremes, in vacuum. This is a cheap mechanism to test to statistical confidence, so do it.

### Shape Memory Alloy (SMA)–Based HDRM

[SMA](../references/glossary.md#sma) devices use a nickel-titanium alloy that changes crystal phase when heated, producing a strong, repeatable stroke that can release a pin, a nut or a clamp.

- **Advantages**: clean, contained release with no debris; high and repeatable actuation force; many devices are **resettable on the ground**, which transforms your ability to test; and there is no melting line to leave residue.
- **Disadvantages**: higher cost than a burn wire, and greater power draw. Ensign-Bickford's TiNi Frangibolt is listed at 7 g and 15 W at 9 V.[^nasa-soa-structures-hdrm]
- **Timing and repeatability** depend on the starting temperature, since the actuator works by reaching a transition temperature. A cold spacecraft takes longer to actuate; make sure your timeout accommodates the cold case.
- **Suppliers** in this space include DCUBED (shape-memory release nuts and pin pullers, marketed as resettable), Ensign-Bickford, and others listed in NASA's survey.

<!-- CSR-RESOURCES:START dev-inhibits-release-mechanisms -->
- **[DCUBED release actuators](https://www.dcubed.space/)** `Link` – Shape-memory nano release nuts and pin pullers for CubeSat deployables, advertised as resettable
- **[NASA State of the Art – Structures, Materials and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)** `Link` – Survey chapter covering release mechanisms and actuators, with mass and power figures and a failure-rate discussion
<!-- CSR-RESOURCES:END dev-inhibits-release-mechanisms -->

### Other mechanisms

- **Pyrotechnic devices** are standard on larger spacecraft but are generally avoided on CubeSats: they introduce an energetic material into your safety data package, produce shock, and are single-use.
- **Motor-driven and paraffin actuators** appear occasionally, offering controlled and resettable actuation at the cost of mass and complexity.
- **Fusible link and melting-pellet devices** sit conceptually between burn wire and SMA.

### Redundancy and Fault Tolerance

- **Dual actuation paths.** Two heaters, two switches, ideally two power channels. The most common real failure is not the mechanism itself but the path that drives it.
- **Electrical and mechanical redundancy are different things.** Two heaters on the same line address a heater failure but not a switch failure. Walk the whole chain.
- **Verify independence explicitly** — this is exactly what a safety reviewer will ask you to demonstrate, and "they're on separate boards" is not a demonstration.
- **Design a degraded mode.** If a solar panel fails to deploy, can the mission continue at reduced power? If an antenna fails to deploy, is the stowed pattern good enough for a beacon? Answering these questions in design is much better than answering them in operations. See [Flight Software – FDIR](flight-software.md#fault-detection-isolation-and-recovery-fdir).
- **Retry logic.** Allow multiple actuation attempts with rest intervals — a burn wire that did not part in 4 seconds may part in 8, and a second attempt after the battery has recovered is often successful. Bound the retries so a stuck mechanism cannot drain the battery.

### Verification and Testing

Inhibit verification is unusual in that it is mostly about proving a *negative* — that something cannot happen.

- **Continuity and resistance testing.** With the RBF inserted, measure and record open circuit at defined test points. With switches actuated, likewise. Do this at every configuration change and keep the records; this is the evidence your launch provider wants.
- **State matrix testing.** Enumerate every combination of RBF in/out and each deployment switch actuated/released, and verify the spacecraft's actual state in each. There are only a handful of combinations and each one should have a documented expected result.
- **End-to-end deployment tests** with the flight-like configuration, in vacuum, at temperature extremes, and after vibration.
- **Timer verification** through a real ejection simulation: release the switches, then confirm nothing transmits and nothing deploys until the full period has elapsed. Measure with a spectrum analyser rather than trusting the software.
- **Test after every change.** Inhibit verification results are only valid for the configuration they were taken in.

Common mistakes worth avoiding:

- Testing the switch and the timer separately but never together.
- Verifying the inhibit chain with the RBF out and never with it in.
- Using a bench supply that masks the real behaviour of a discharged battery.
- Deploying in air, in one orientation, once, and calling it verified.
- Forgetting that after a successful deployment test the mechanism is now used — flight mechanisms need a defined number of allowable ground cycles.

## Documentation and Compliance

What launch providers typically ask for:

- **An inhibit block diagram** showing the power path from every energy source to every hazard, with each inhibit marked and its independence evident at a glance.
- **A state table** listing each configuration and the resulting spacecraft state.
- **Test evidence**: continuity measurements, deployment test records, RF silence verification, with dates, configurations and signatures.
- **Battery documentation** — cell datasheets, pack design, protection circuits, and test results. See [EPS – Safety and launch requirements](eps.md#safety-and-launch-requirements).
- **Deployment mechanism description** with actuation method, power, and redundancy.
- **Photographs** of the as-built hardware, especially the RBF port and deployment switches.

Common reasons reviews go badly:

- **Counting a timer as an inhibit.** Explicitly excluded by the CDS, and reviewers know it.
- **Inhibits that are not genuinely independent** — a common shared failure point discovered during review.
- **Missing or undated test evidence**, or evidence taken on a configuration that has since changed.
- **A diagram that does not match the hardware**, which immediately calls the rest of the package into question.
- **Late submission.** Safety review is on the critical path, and iterations take weeks. Start early.

The underlying advice is simple: **design the inhibit architecture so that it is easy to explain.** A reviewer who can follow your block diagram in two minutes will approve it. One who cannot will ask questions for a month.

---

👉 **Please consider [contributing](../contributing.md)!**

[^cubesat101]: NASA CubeSat Launch Initiative, [*CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers*](https://www.nasa.gov/wp-content/uploads/2017/03/nasa_csli_cubesat_101_508.pdf). Defines an electrical inhibit as "a physical device that interrupts the 'power path' needed to turn on your CubeSat and/or other potentially hazardous devices", describes burn wire constraint methods, and recommends using two separate burn wires for redundancy. Points to the CDS as the authoritative source for specific numerical requirements.

[^nasa-soa-structures-hdrm]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 6: Structures, Materials, and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/). Reports that mechanisms account for over 10% of documented small satellite failures, and lists representative release actuators including the Ensign-Bickford TiNi Frangibolt at 7 g and 15 W at 9 V.
