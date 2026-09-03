# Inhibits, Hold Down and Release Mechanisms (HDRM)

This page covers launch safety hardware: what the CubeSat Design Specification and launch providers require of inhibits, deployment switches, remove-before-flight pins and timers, how those interact with the power system, the hold-down and release mechanisms that keep deployables stowed, and the evidence a safety review expects.

This is the part of a CubeSat that exists entirely for other people's benefit. Inhibits do nothing for your mission – their only job is to guarantee that your spacecraft cannot do anything hazardous while it is inside someone else's rocket, next to someone else's payload, and sometimes inside a crewed vehicle. They are also, for the same reason, the part of your design most likely to be examined line by line in a safety review.

## Purpose and Safety Context

### The hazards being controlled

A CubeSat inside a [deployer](../references/glossary.md#deployer) is a sealed box containing stored electrical energy, a radio transmitter, and spring-loaded mechanisms. Four things must not happen before deployment:

- **Inadvertent RF transmission**, which could interfere with launch vehicle telemetry and range safety systems at exactly the moment when nobody can afford interference.
- **Inadvertent deployment**, where an antenna or solar panel releasing inside the deployer jams it – destroying your mission and potentially the co-passengers in the same pod.
- **Inadvertent propulsion activation**, if you carry propulsion at all. The [CDS](../references/glossary.md#cds) treats this as its own hazard class with its own inhibit count and its own governing standard (§2.1.3, §2.1.4).[^cds-rev14] See [Propulsion – Safety and Launch Requirements](propulsion.md#safety-and-launch-requirements).
- **Uncontrolled energy release** – a battery fault, thermal runaway, or unexpected current draw inside a sealed volume.

### Mission phases

The inhibit architecture divides the mission's early life into distinct states:

1. **Ground handling and transport** – the [RBF pin](../references/glossary.md#rbf-pin) is inserted and the spacecraft is completely dead.
2. **Integration into the deployer** – RBF removed (if the deployer has no access port), [deployment switches](../references/glossary.md#deployment-switch) held actuated by the deployer walls. The spacecraft remains off.
3. **Launch and ascent** – unchanged. The CubeSat is a passive mass.
4. **Ejection** – the deployment switches release, power reaches the spacecraft, and the timers start.
5. **Post-deployment quiet period** – powered and booting, but not transmitting and not deploying anything.
6. **Commissioning** – after the mandated delays, RF and deployables are enabled.

### Relationship to reviews and licensing

Inhibit design is reviewed by your launch provider as part of the safety data package, and the evidence you supply – diagrams, test results, photographs – is what gets accepted or rejected. It also intersects with your frequency license, since regulators care about when you start transmitting. See [Qualification and Launch](launch.md#regulatory-requirements).

<!-- CSR-RESOURCES:START dev-inhibits-hdrm-requirements -->
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – The document behind almost every requirement on this page. Sections 2.3 and 2.4 cover inhibits, deployment switches, RBF pins and the quiet periods
- **[NASA CubeSat 101](https://www.nasa.gov/wp-content/uploads/2017/03/nasa_csli_cubesat_101_508.pdf)** `PDF` – First-time developer guide from the CubeSat Launch Initiative, with a plain-language treatment of electrical inhibits and burn wire constraint mechanisms
- **[NanoRacks CubeSat Deployer (NRCSD) Interface Definition Document](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf)** `PDF` – An openly published deployer interface document, useful as a worked example of how a provider layers its own inhibit and timer requirements on top of the CDS
<!-- CSR-RESOURCES:END dev-inhibits-hdrm-requirements -->

## Inhibit Types and Architectures

### What counts as an inhibit

The [CDS](../references/glossary.md#cds) is precise about this, and the precision matters:

> "An inhibit is a physical device between a power source and a hazard." (§2.3.7.1)

And equally important:

> "A timer is not considered an independent inhibit." (§2.3.7.2)

This second point catches many first-time teams. Software delays and timers are required by the specification for the post-deployment quiet period, but they do **not** count toward the inhibit count. An inhibit must be a physical interruption in the power path.

### How many are required

CDS Rev. 14.1 requires:[^cds-rev14]

- **At least three independent RF inhibits** to prevent inadvertent transmission (§2.3.7).
- **At least three independent inhibits** to prevent inadvertent release of any deployable structure such as antennas or solar panels (§2.3.8).
- **At least three inhibits to activation** on any propulsion system (§2.1.4), which must additionally be designed, integrated and tested in accordance with AFSPCMAN 91-710 Volume 3 (§2.1.3).

Independence is the operative word: three switches in series driven by the same mechanism are one inhibit, not three. Each must be capable of failing independently of the others.

**You will meet the figure two in older material, and it is not an error – it is an earlier revision.** CDS Rev. 13 §3.3.9 offered a choice: either "one RF inhibit and RF power output of no greater than 1.5W at the transmitting antenna's RF input" (§3.3.9.1) or "two independent RF inhibits" (§3.3.9.2), while noting even then that three was "highly recommended and can reduce required documentation and analysis".[^cds-rev13] Rev. 13 set no inhibit count for deployables at all – only propulsion carried a hard three (§3.1.5). Rev. 14 raised RF to a flat three and added the deployables requirement.

The older logic survives in Rev. 14.1 as a note printed directly under the requirement: "Some launch vehicle providers will only require one or two independent inhibits depending on the CubeSat's RF power output. However, the use of three independent inhibits is highly recommended and can reduce required documentation and analyses" (§2.3.7.3).[^cds-rev14] What sits underneath all of these numbers is hazard severity, which the NanoRacks deployer interface document states plainly: three inhibits is "based on the worst-case assumption that the CubeSat contains a potential catastrophic hazard that exists in the event of an inadvertent power-up", and the design "shall incorporate an appropriate number of inhibits dictated by the hazard potential of the payload".[^nrcsd]

So the count is argued rather than fixed – but it is argued with your provider, against a documented hazard analysis, and the argument is very much easier if you designed for three. Your provider may also require more. As always, **the payload user guide takes precedence over the CDS** – see [Structure – The launch provider always wins](structure.md#the-launch-provider-always-wins).

### Architectural patterns

The conventional CubeSat implementation uses three physically distinct devices in the power path:

- **Deployment switch A** – released by the deployer wall or door.
- **Deployment switch B** – a second, independently located switch.
- **RBF pin** – removed before flight, and a third independent break while present.

A latching relay can stand in for one of these. A timer cannot stand in for any of them (§2.3.7.2), and neither can anything that merely commands an inhibit – the NanoRacks wording is blunt: "A control for an inhibit (electrical or software) cannot be counted as an inhibit or power interrupt device."[^nrcsd] What matters to a reviewer is that you can draw the power path, show three physical breaks in it, and demonstrate that no single failure closes more than one.

!!! warning "Your deployer may not count the RBF pin"

    The three-device pattern above is conventional, not universal. The NanoRacks CubeSat Deployer IDD requires "a minimum of three (3) independent inhibit switches actuated by physical deployment switches" (4.2.1-3),[^nrcsd] and those three are in addition to the RBF pin: the pin covers ground handling, the switches cover the deployer, and a design that leans on the pin as its third break does not meet the requirement. Read your own deployer's interface document for its count before committing to an architecture.

Design principles:

- **Normally-open is the safe default.** The hazard is disabled unless something actively enables it. A normally-closed inhibit that must be actively held open fails dangerous.
- **Inhibit the source, not the sink.** Break the power path high in the tree, not at the last device before the antenna.
- **Separate the deployable and RF inhibit chains** where practical, so a fault in one does not compromise the other.
- **Keep it dumb.** Inhibits should be verifiable with a multimeter, not by reading code.

### Inhibit Interaction with the Electrical Power System (EPS)

Inhibits are, physically, part of the power architecture, which means the [EPS](eps.md) and inhibit designs have to be developed together.[^cds-rev14]

- **The CDS requires the power system to be off throughout launch**: "the CubeSat power system shall be at a power off state from the time of delivery to the LV through on-orbit deployment" (§2.3.1). The powered functions in scope are command and data handling, RF communication, attitude determination and control, and deployable mechanism actuation (§2.3.1.1).
- **The deployment switch must electrically disconnect the power system from the powered functions** when actuated (§2.3.2.1) – not merely signal software that it is time to stay quiet.
- **There are exactly two carve-outs, and both are narrow.** Battery protection circuitry may remain powered (§2.3.1.2, per §2.3.6). A real-time clock may keep running (§2.3.3) provided it is isolated from the main power system, runs below 320 kHz, and is current-limited to less than 10 mA (§2.3.3.1–2.3.3.3). The RTC allowance is worth knowing because it changed: Rev. 13 required the deployment switch to disconnect real-time clocks along with everything else.[^cds-rev13] A compliant RTC is also the cleanest way to make a quiet-period timer survive a reset – see [Timers and Delayed Activation](#timers-and-delayed-activation).
- **Access port geometry is specified, and it constrains your late-flow options.** The RBF pin and all umbilical connectors must sit within the designated access port locations where the dispenser has them (§2.3.4); where it has none, the RBF must be removed before insertion (§2.3.4.1). Decide early, because those connectors are also how you top up the battery late in the flow.
- **Battery self-discharge** over what may be months of storage and launch delay is a planning problem in its own right, and one the CDS does not address at all. Confirm the pack will still be above its minimum voltage at deployment.
- **Controlled energization on release.** When the switches open, everything comes up at once, on a cold battery, in the worst condition of the mission. See [EPS – Startup and brownout behavior](eps.md#startup-and-brownout-behavior).
- **Battery circuit protection** is separately required by the CDS (§2.3.6) to prevent unbalanced cell conditions. See [EPS – BMS](eps.md#battery-management-systems-bms).

### Remove-Before-Flight (RBF) Pins

The RBF pin is a physical object inserted into the spacecraft that breaks the power path, with a large brightly colored streamer attached so that nobody can possibly forget it is there.

The CDS requirements are specific:[^cds-rev14]

- "The CubeSat shall include an RBF pin, which cuts **all** power to the satellite once it is inserted into the satellite." (§2.3.5) – all power, not most of it.
- It "shall be removed from the CubeSat before integration into the dispenser, if the dispenser does not have access ports." (§2.3.5.1)
- It "shall protrude no more than 6.5 mm from the CubeSat rail surface when it is fully inserted into the satellite." (§2.3.5.2)

Practical implementation notes:

- The usual mechanism is an insulating blade that separates two spring contacts. Simple, inspectable, and with no failure mode more subtle than "bent".
- **Position it in an accessible face** consistent with your deployer's access port geometry. Retrofitting an RBF port into a finished structure is painful – see [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **Human factors are the actual risk.** The pin gets removed at a busy moment, by someone who may not be from your team, often under time pressure. Make it impossible to reinsert backwards, impossible to leave half-inserted without it being obvious, and make the streamer big.
- **Verify continuity, don't assume it.** A pin can be present and not making contact; a pin can be absent and the contacts stuck closed. Measure.
- Repeated insertion wears the contacts. Track the cycle count and inspect before flight.

### Deployment Switches and Separation Detection

Deployment switches are how the spacecraft knows it has left the deployer.

CDS requirements:[^cds-rev14]

- "The CubeSat shall have, at a minimum, one deployment switch, which is actuated while integrated in the dispenser." (§2.3.2)
- "The deployment switch shall be in the actuated state at all times while integrated in the dispenser." (§2.3.2.2)
- In the actuated state it should be at or below the level of any external surface that interfaces with the dispenser or a neighboring CubeSat (§2.3.2.3).
- Critically: "If the CubeSat deployment switch toggles from the actuated state and back, the satellite shall reset to a pre-launch state, including reset of transmission and deployable timers." (§2.3.2.4)

That last requirement is the interesting one. It exists because a switch can bounce or momentarily open during vibration, and the specification refuses to allow a transient to start your quiet-period timers early. **Your implementation must reset the timers, not just note the event** – and it must do so in a way that survives whatever state the software was in.

Implementation notes:

- **Two switches, independently located** – commonly on separate rails or on a rail and the deployer door face – so a single mechanical failure does not release the inhibit.
- **Debounce in hardware where the signal gates power**, and in software where it feeds logic. Contact bounce during ejection happens.
- **The separation signal is also useful telemetry.** Record the time of separation and the switch states; it is the T-zero for everything that follows and one of the few pieces of ground-truth data you get about deployment.
- Test the switches after vibration, not only before. Their whole job is to survive that environment and still work.

### Timers and Delayed Activation

The CDS mandates two quiet periods, and they are measured from different events:[^cds-rev14]

- **Deployables**: "All deployables such as booms, antennas, and solar panels shall wait to deploy a minimum of 30 minutes after the CubeSat's deployment switch(es) are activated during dispenser ejection." (§2.4.4)
- **RF**: "CubeSats shall not generate or transmit a signal earlier than 45 minutes after on-orbit deployment." (§2.4.5)

The spacecraft may power on immediately after deployment (§2.4.5.1) – the restriction is on transmitting and deploying, not on being alive. Use that time: boot, assess health, start charging, begin detumbling.

Implementation:

- **Hardware timers are preferred** for the RF inhibit release, because a hardware timer cannot be defeated by a software fault, a reset loop, or a corrupted image. A dedicated timer IC that must expire before the transmitter's power path can close is easy to demonstrate to a reviewer.
- **Software timers must survive resets.** If the OBC reboots at T+20 minutes and the timer restarts from zero, you have not violated the requirement – you have merely delayed yourself. If it reboots and *loses* the fact that it has not yet waited, you have violated it. Store elapsed time in non-volatile memory, or run the count on a CDS-compliant RTC, and treat the requirement conservatively.
- **Watchdog interaction** is the subtle case. A watchdog reset during the quiet period must not clear the inhibit state. Think through the interaction explicitly. See [OBC – Watchdogs](obc.md#watchdogs).
- **Add margin.** Waiting 35 and 50 minutes rather than exactly 30 and 45 costs nothing and removes any argument about clock accuracy.
- **Check your provider's numbers, and expect a different shape rather than simply a longer one.** The NanoRacks deployer, for instance, applies a single 30-minute hold to everything: the CubeSat "shall not operate any system (including RF transmitters, deployment mechanisms or otherwise energize the main power system) for a minimum of 30 minutes where hazard potential exists", implemented by a timer that must itself carry "appropriate fault tolerance".[^nrcsd] That is not the CDS's 30-and-45 split, and a design that satisfies one does not automatically document cleanly against the other.

## Hold Down and Release Mechanisms (HDRM)

An HDRM holds a deployable stowed against launch loads and releases it on command. From the structural side it must carry preload; from the electrical side it must not fire early; from the reliability side it is a single-use, single-point-of-failure device on which the mission may depend.

The context worth keeping in mind: NASA's state-of-the-art survey attributes **more than 10% of reported small satellite failures to mechanisms**, and recommends "design simplicity, margin, supplier selection, and testing" as the mitigations.[^nasa-soa-structures] See [Structure – Deployable Structures and Mechanisms](structure.md#deployable-structures-and-mechanisms).

### Functional requirements

- **Preload**: enough to prevent any relative motion under launch vibration. A deployable that rattles will fret, generate debris, and may fail its own hinge.
- **Release reliability**: it must actuate on command, in vacuum, at whatever temperature it happens to be.
- **Non-actuation reliability**: equally important – it must *not* actuate before commanded, including during vibration and thermal cycling. This is the property behind NASA's CubeSat 101 recommendation to "use two separate burn wires", whose stated purpose is to "reduce the likelihood of a deployable coming loose prematurely".[^cubesat101]
- **Contained release**: no fragments, no debris. This rules out several mechanisms that would otherwise be attractive.
- **Ground resettability** is a practical requirement rather than a flight one, but it matters enormously: a mechanism you can only test once is a mechanism you have effectively not tested.

### Burn Wire–Based HDRM

The classic CubeSat mechanism, and still the most common: a synthetic line under tension restrains the deployable; a resistive element heats and melts or severs the line; springs do the rest.

- **Principle.** A nichrome wire or resistor is pressed against a loop of Dyneema, Vectran or similar. Current through the heater raises it above the line's melting point and the line parts.
- **Power.** Typically a few watts for a few seconds – modest energy, but a significant *peak* draw at a moment when the battery may be cold and partly discharged. Budget it explicitly and consider requiring a state-of-charge threshold before actuation. See [EPS](eps.md#power-requirements-and-budgets).
- **Vacuum changes the thermal behavior completely.** With no convection, the heater runs much hotter for the same power, and burn times measured in air are not valid. **Always characterize burn wire release in vacuum.**
- **Redundancy – be clear which kind you are buying.** Two separate restraint lines improve *retention*, which is what CubeSat 101 is recommending,[^cubesat101] but they do not improve *release*: both must part before the deployable moves, so unless either line alone frees it, doubling the lines makes release less likely rather than more. Release redundancy comes from the drive side – two independent heaters on independent power channels acting on the same line, so that neither a heater failure nor a switch failure prevents actuation. Say in the safety data package which property each pair is there to provide.
- **Failure modes**: line not fully severed and snagging; heater open-circuit; line creeping under preload and going slack over months of storage; melted line residue contaminating a nearby optical surface; heater damaging adjacent structure.
- **Verification.** Test many times, after vibration, at temperature extremes, in vacuum. This is a cheap mechanism to test to statistical confidence, so do it.

Off-the-shelf burn-wire modules exist – CubeSource's BurnWing is one – that package the heater, its redundancy and the protection circuitry, so that your qualification effort goes into the restraint and the release geometry rather than the electronics.

### Shape Memory Alloy (SMA)–Based HDRM

[SMA](../references/glossary.md#sma) devices use a nickel-titanium alloy that changes crystal phase when heated, producing a strong, repeatable stroke that can release a pin, a nut or a clamp.

- **Advantages**: clean, contained release with no debris; high and repeatable actuation force; many devices are **resettable on the ground**, which transforms your ability to test; and there is no melting line to leave residue.
- **Disadvantages**: higher cost than a burn wire, and often – but not always – a larger power draw. NASA's survey lists Ensign-Bickford's TiNi Frangibolt at 7 g and 15 W at 9 V, and their ML50 microlatch at 10 g and 2 W at 7 V in the same table.[^nasa-soa-structures] Size the budget from the specific device, not from the technology.
- **Timing and repeatability** depend on the starting temperature, since the actuator works by reaching a transition temperature. A cold spacecraft takes longer to actuate; make sure your timeout accommodates the cold case.
- **Suppliers** in this space include DCUBED (shape-memory release nuts and pin pullers, marketed as resettable), Ensign-Bickford, and others listed in NASA's survey.

<!-- CSR-RESOURCES:START dev-inhibits-hdrm-release-mechanisms -->
- **[DCUBED release actuators](https://www.dcubed.space/)** `Link` – Shape-memory nano release nuts and pin pullers for CubeSat deployables, advertised as resettable
- **[CubeSource BurnWing](https://www.cubesource.space/product-page/burnwing-flight)** `Link` – Compact burn-wire release module with redundant burn resistors rated for 50+ cycles each, 5 V or 12 V input, ESD, reverse-polarity and over-temperature protection, usable standalone or integrated into a deployable; delivered with an engineering model for testing. Commercial
- **[NASA State of the Art – Structures, Materials and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)** `Link` – Survey chapter covering release mechanisms and actuators, with mass and power figures and a failure-rate discussion
<!-- CSR-RESOURCES:END dev-inhibits-hdrm-release-mechanisms -->

### Other mechanisms

- **Pyrotechnic devices** are standard on larger spacecraft but are generally avoided on CubeSats: they introduce an energetic material into your safety data package, produce shock, and are single-use.
- **Thermal actuators** – paraffin and fusible-link devices – melt or expand a material to release a preloaded pin. They avoid both the burn wire's tensioned line and the pyrotechnic's shock, at the cost of slower and more temperature-dependent actuation.
- **Motor-driven mechanisms** appear occasionally, offering controlled and resettable actuation at the cost of mass and complexity.

### Redundancy and Fault Tolerance

- **Dual actuation paths.** Two heaters, two switches, ideally two power channels. The most common failure in practice is not the mechanism itself but the path that drives it.
- **Electrical and mechanical redundancy are different things.** Two heaters on the same line address a heater failure but not a switch failure. Walk the whole chain.
- **Verify independence explicitly** – this is exactly what a safety reviewer will ask you to demonstrate, and "they're on separate boards" is not a demonstration.
- **Design a degraded mode.** If a solar panel fails to deploy, can the mission continue at reduced power? If an antenna fails to deploy, is the stowed pattern good enough for a beacon? Answering these questions in design is much better than answering them in operations. See [Flight Software – FDIR](flight-software.md#fault-detection-isolation-and-recovery-fdir).
- **Retry logic.** Allow multiple actuation attempts with rest intervals – a burn wire that did not part in 4 seconds may part in 8, and a second attempt after the battery has recovered is often successful. Bound the retries so a stuck mechanism cannot drain the battery.

## Verification and Testing

Verifying inhibits is unusual in that it is mostly about proving a *negative* – that something cannot happen. Verifying mechanisms is the opposite problem, and the two sit together because the same test campaign has to cover both.

- **Continuity and resistance testing.** With the RBF inserted, measure and record open circuit at defined test points. With switches actuated, likewise. Do this at every configuration change and keep the records; this is the evidence your launch provider wants.
- **State matrix testing.** Enumerate every combination of RBF in/out and each deployment switch actuated/released, and verify the spacecraft's actual state in each. There are only a handful of combinations and each one should have a documented expected result.
- **End-to-end deployment tests** with the flight-like configuration, in vacuum, at temperature extremes, and after vibration.
- **Timer verification** through a full ejection simulation: release the switches, then confirm nothing transmits and nothing deploys until the full period has elapsed. Measure with a spectrum analyser rather than trusting the software.
- **Test after every change.** Inhibit verification results are only valid for the configuration they were taken in.

Common mistakes worth avoiding:

- Testing the switch and the timer separately but never together.
- Verifying the inhibit chain with the RBF out and never with it in.
- Using a bench supply that masks the behavior of a discharged battery.
- Deploying in air, in one orientation, once, and calling it verified.
- Forgetting that after a successful deployment test the mechanism is now used – flight mechanisms need a defined number of allowable ground cycles.

## Documentation and Compliance

What launch providers typically ask for:

- **An inhibit block diagram** showing the power path from every energy source to every hazard, with each inhibit marked and its independence evident at a glance.
- **A state table** listing each configuration and the resulting spacecraft state.
- **Test evidence**: continuity measurements, deployment test records, RF silence verification, with dates, configurations and signatures.
- **Battery documentation** – cell datasheets, pack design, protection circuits, and test results. See [EPS – Safety and launch requirements](eps.md#safety-and-launch-requirements).
- **Deployment mechanism description** with actuation method, power, and redundancy.
- **A hazard analysis** for anything that drives the inhibit count, since the number of inhibits you owe follows from the severity you claim.
- **Photographs** of the as-built hardware, especially the RBF port and deployment switches.

Common reasons reviews go badly:

- **Counting a timer as an inhibit.** Explicitly excluded by the CDS, and reviewers know it.
- **Inhibits that are not independent in fact** – a common shared failure point discovered during review.
- **Missing or undated test evidence**, or evidence taken on a configuration that has since changed.
- **A diagram that does not match the hardware**, which immediately calls the rest of the package into question.
- **Designing to the CDS and submitting to a provider whose interface document says something different.** Read theirs first.
- **Late submission.** Safety review is on the critical path, and iterations take weeks. Start early.

The underlying advice is simple: **design the inhibit architecture so that it is easy to explain.** A reviewer who can follow your block diagram in two minutes will approve it. One who cannot will ask questions for a month.

---

👉 **Please consider [contributing](../contributing.md)!**

[^cds-rev14]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 14.1*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (9 February 2022). Free PDF. Source for every section number quoted on this page: the power-off state and its exceptions (§2.3.1–2.3.3.3), access port and RBF pin requirements (§2.3.4–2.3.5.2), battery circuit protection (§2.3.6), the three-inhibit requirements for RF (§2.3.7) and deployables (§2.3.8) with their notes on what counts as an inhibit (§2.3.7.1–2.3.7.3), the propulsion requirements (§2.1.3, §2.1.4), and the quiet periods (§2.4.4, §2.4.5, §2.4.5.1). The current revision as of this writing; no later revision has been published.

[^cds-rev13]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 13*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/56e9b62337013b6c063a655a/1458157095454/cds_rev13_final2.pdf). Free PDF. The source of the widely quoted "two inhibits" figure. §3.3.9 required the CubeSat to meet at least one of §3.3.9.1 (one RF inhibit with RF output no greater than 1.5 W at the transmitting antenna's input) or §3.3.9.2 (two independent RF inhibits), while stating that three independent inhibits was "highly recommended and can reduce required documentation and analysis". Rev. 13 set no inhibit count for deployables; §3.1.5 required at least three for propulsion. §3.3.3 also required the deployment switch to disconnect real time clocks, which Rev. 14.1 relaxed.

[^nrcsd]: NanoRacks, [*NanoRacks CubeSat Deployer (NRCSD) Interface Definition Document*](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf). Free PDF. Cited here as a published example of provider requirements layered on the CDS. Requirement 4.2.1-3 calls for "a minimum of three (3) independent inhibit switches actuated by physical deployment switches", and states that "a control for an inhibit (electrical or software) cannot be counted as an inhibit or power interrupt device". The rationale is given explicitly: three inhibits is "based on the worst-case assumption that the CubeSat contains a potential catastrophic hazard that exists in the event of an inadvertent power-up", and the design "shall incorporate an appropriate number of inhibits dictated by the hazard potential of the payload". Requirement 4.2.1-2 imposes a single minimum 30-minute timer, with appropriate fault tolerance, before operating any system. The three switch-actuated inhibits are required in addition to the RBF pin. Verify the requirement numbering and wording against the revision your mission is actually flown under.

[^cubesat101]: NASA CubeSat Launch Initiative, [*CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers*](https://www.nasa.gov/wp-content/uploads/2017/03/nasa_csli_cubesat_101_508.pdf). Free PDF. Defines an electrical inhibit as "a physical device that interrupts the 'power path' needed to turn on your CubeSat and/or other potentially hazardous devices", and describes the burn wire constraint method. Its recommendation to "use two separate burn wires" is justified on retention grounds – it "should reduce the likelihood of a deployable coming loose prematurely during testing" – not on release reliability. It does not itself state inhibit counts; for those, the CDS governs.

[^nasa-soa-structures]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 6: Structures, Materials, and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/). Open access. States that mechanisms "have contributed to over 10% of reported small satellite failures", with design simplicity, margin, supplier selection and testing given as mitigations. Table 6-5 lists representative release actuators, including the Ensign-Bickford TiNi Frangibolt at 0.007 kg and 15 W at 9 VDC and the Ensign-Bickford TiNi ML50 microlatch at 0.010 kg and 2 W at 7 VDC.