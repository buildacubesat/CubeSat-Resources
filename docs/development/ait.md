# Assembly, Integration, and Testing (AIT)

Assembly, Integration, and Testing (AIT) covers the practical work of turning individual CubeSat subsystems into a functioning spacecraft and verifying that it meets mission and launch requirements. This includes mechanical assembly, electrical integration, incremental bring-up, functional verification, simulation, and environmental testing. A structured AIT approach helps catch interface issues early, reduces risk during launch and operations, and improves overall mission reliability.

AIT is where a design becomes a spacecraft, and where the assumptions made over the preceding two years get tested against reality. It is also, on nearly every CubeSat programme, the phase that takes longer than planned – partly because problems surface here that were created much earlier, and partly because teams underestimate how much of AIT is documentation, procedure and rework rather than assembly.

## Planning the AIT Campaign

### Model philosophy

How many spacecraft you build determines much of what follows:

- **Flight model only** – build one, test it as a [protoflight](../references/glossary.md#protoflight) article. Cheapest, fastest, and the norm for CubeSats. The tradeoff is that your flight hardware absorbs the fatigue of environmental testing, and there is no spare if something breaks.
- **Engineering model + flight model** – a functionally equivalent, non-flight article for development, software work, procedure rehearsal and destructive testing. This is the single best investment a CubeSat team can make if the budget stretches: it means software development is not blocked by hardware availability, and it means every procedure has been rehearsed before it touches flight hardware.
- **Structural/thermal model** – a mass-and-geometry representative article for early environmental testing. Sometimes worth it for a first-of-kind structure.
- **[Flatsat](../references/glossary.md#flatsat)** – not really a model, but the workhorse. See below.

### Sequencing

The general principle is **build up incrementally and functionally test at every step**, so that when something breaks you know which step broke it. A representative flow:

1. Incoming inspection and standalone functional test of every board.
2. Flatsat integration and full system bring-up.
3. Software development and testing on the flatsat.
4. Mechanical assembly of the flight article.
5. Integrated functional test.
6. Environmental test campaign, with functional tests before and after each exposure.
7. Final functional test, mass properties measurement, fit check.
8. Delivery and launch site operations.

**Reserve time.** Every CubeSat programme discovers problems during AIT, and the schedule between "hardware complete" and "delivery" is where they must be absorbed. A campaign planned with no float will slip.

### Ground support equipment

Easy to underestimate, and it needs designing:

- **[EGSE](../references/glossary.md#egse)** (electrical GSE) – power supplies, umbilicals, breakout boards, an RF loopback path, a test console, and the software to drive it all. Ideally the same command-and-telemetry software you will use for operations, so that operations software is exercised throughout AIT rather than written at the end.
- **MGSE** (mechanical GSE) – handling fixtures, vibration adapters, protective covers for rails and optics, a test pod for fit checks, lifting and rotation aids.
- **Simulators** – stand-ins for subsystems not yet available, and for the space environment during [HIL](#hardware-in-the-loop-hil-testing) testing.

## Assembly

This section covers the mechanical and electrical assembly of CubeSat subsystems into the final spacecraft. Topics include assembly order, tooling, cleanliness, documentation, and verification steps during build-up. Good assembly practices reduce rework, prevent damage, and simplify later integration and testing.

### Mechanical Assembly

- **Plan the assembly sequence before you start** – ideally during design, as a CAD exercise. The question that catches teams out is not "can this be assembled?" but "can it be *dis*assembled to reach the board that just failed?" Every CubeSat gets taken apart more times than anyone expects.
- **Access planning.** Confirm that the [RBF pin](../references/glossary.md#rbf-pin), charge port, debug connector and any late-access item remain reachable in the fully assembled configuration. See [Structure – Mounting](structure.md#mounting-and-mechanical-interfaces).
- **Fastener control.** Use a calibrated torque driver, record the torque applied to every fastener, and use the same values on reassembly. Track which fasteners have been cycled – threads in aluminium do not last forever. See [Structure – Fasteners and Assembly](structure.md#fasteners-and-assembly).
- **Handle deployables as the hazard they are.** A stowed antenna or panel under preload can release unexpectedly and injure someone or damage the spacecraft. Use safety restraints during handling, and treat "deployable armed" as a controlled state in the procedure.
- **Cleanliness.** Gloves for everything that flies, deburr and clean parts before they enter the integration area, and control foreign object debris – count fasteners in and out. See [Structure – Cleanliness](structure.md#cleanliness-handling-and-contamination).
- **Document as you go.** Photograph each stage. Record part serial numbers and where they went. Note anything unexpected, however trivial it seems at the time. When something fails four months later, this record is what lets you work out what changed.

### Electrical Assembly and Harnessing

Harnessing is where a surprising share of CubeSat integration problems originate, and it is the least glamorous work in the programme.

- **Design the harness, don't grow it.** Produce a wiring diagram and a connector schedule before cutting wire. A harness that accreted during integration is impossible to verify and impossible to rebuild identically.
- **Label both ends of every wire and every connector.** Use a scheme that survives handling and thermal cycling.
- **Strain relief and routing.** Secure harness at regular intervals, keep service loops at anything that moves, respect minimum bend radii, and keep power and sensitive signal lines apart. Anything crossing a hinge needs particular attention – see [Structure – Deployables](structure.md#deployable-structures-and-mechanisms).
- **Connector selection and retention.** Use connectors with positive locking. Vibration undoes friction-fit connectors, and an intermittent connector is among the hardest faults to diagnose.
- **Crimp properly.** Use the correct tool for the contact, and inspect crimps – a bad crimp passes a continuity check and fails after vibration.
- **Verify before mating.** Continuity and isolation checks on every harness before it is connected to hardware, and a pin-out check against the diagram. A miswired power connector destroys boards.
- **Vent trapped volumes** and avoid materials with poor [outgassing](../references/glossary.md#outgassing) properties – check tapes, sleeving and cable ties against the NASA database. See [Structure – Materials](structure.md#materials-and-manufacturing).

## Integration

This section focuses on combining individual subsystems into a coherent system and verifying that interfaces behave as expected. Integration is typically iterative and closely coupled to functional testing and troubleshooting.

### Subsystem Integration

- **Incoming inspection first.** Every board – bought or built – gets a visual inspection and a standalone functional test before it joins the system. Finding a dead board on arrival is cheap; finding it after integration is not.
- **Power-first bring-up.** Bring up the [EPS](eps.md) alone, verify every rail and every switched channel with a scope and a dummy load before connecting anything that can be damaged. Verify current limits actually limit.
- **Then compute, then one subsystem at a time.** Add the [OBC](obc.md), confirm it boots and communicates, then add subsystems one at a time with a functional test after each. Resist the temptation to connect everything at once – the debugging cost scales badly.
- **Watch the shared resources.** Power budget, bus loading, and I²C address allocation are the three that bite. Address collisions between COTS boards that each assumed exclusive use of the bus are a recurring CubeSat problem. See [OBC – Interfaces and Buses](obc.md#interfaces-and-buses).
- **Isolate interface issues systematically.** When two subsystems misbehave together but work alone, the fault is in the interface – electrical loading, timing, protocol mismatch, or grounding. Instrument the interface rather than guessing.
- **Configuration control from the first integration.** Record which hardware revision, which firmware version and which configuration is installed. A test result is only meaningful if you know what you tested.

### Flatsat and Integration Test Setups

A **flatsat** is the whole avionics set laid out on a bench, wired as flown but fully accessible. It is the most valuable piece of equipment a CubeSat team owns.

- **What it enables:** parallel software development, probing every signal, injecting faults, reprogramming without disassembly, and rehearsing procedures – all without touching flight hardware.
- **Keep it representative.** A flatsat that has drifted from the flight configuration produces test results that do not transfer. Track its configuration as carefully as the flight article's.
- **Flight-spare or engineering-grade?** A flatsat built from engineering-grade parts is cheaper and can be treated roughly; one built from flight spares is more representative and more precious. Many teams end up with both.
- **Breakout boards and test harnesses** that expose every bus and rail on accessible headers are worth building properly – they will be used for years.
- **Safe testing of flight hardware outside the structure** requires discipline: ESD control, current-limited supplies, and a written setup so it is reproducible.
- **Transitioning to the integrated spacecraft** always reveals differences: harness lengths change, grounding changes, thermal behaviour changes completely, and RF self-interference appears that a spread-out flatsat never showed. Plan for a debugging period after first integration.

## Simulation and Testing

This section covers simulation and testing methods used during CubeSat design, integration, and verification. Topics include functional simulation, hardware-in-the-loop (HIL) testing, flatsat setups, environmental testing, vibration and thermal considerations, and software test strategies. Simulation and testing are essential for catching integration issues early and reducing mission risk.

### Test philosophy: qualification, acceptance and protoflight

Three approaches, distinguished by what they are trying to prove:

- **[Qualification testing](../references/glossary.md#qualification-testing)** demonstrates that the *design* has margin, by testing at levels above the expected environment. ECSS defines it as providing evidence that the item "performs in accordance with its specifications in the intended environments with the specified qualification margins", conducted on a dedicated qualification model.[^ecss-testing] Typical margins: maximum expected random vibration spectrum **+3 dB for 2 minutes** per axis.
- **[Acceptance testing](../references/glossary.md#acceptance-testing)** demonstrates that a *specific flight article* is free of workmanship defects, at expected levels: **+0 dB for 1 minute** per axis.[^ecss-testing]
- **Protoflight testing** combines the two on a single article – **qualification levels for acceptance durations**. This is what almost every CubeSat does, because building a second complete spacecraft purely to break it is rarely affordable. The tradeoff is that the flight article accumulates fatigue life during testing.

### Environmental Testing

- **Vibration** – random vibration is the driving mechanical case. NASA's [GEVS](../references/glossary.md#gevs) gives a component qualification level of 14.1 [Grms](../references/glossary.md#grms) for 2 minutes per axis, with acceptance 3 dB lower (~10 Grms), and real launcher levels are often gentler still. See [Structure – Structural Analysis](structure.md#structural-analysis-and-fem).
- **Shock** – from stage separation and deployer actuation. Often covered by analysis or similarity at CubeSat scale.
- **[Thermal vacuum](../references/glossary.md#tvac)** – the essential test, since removing convection changes thermal behaviour fundamentally. See [Thermal – Testing and Validation](thermal.md#thermal-testing-and-validation).
- **EMC** – self-compatibility matters more than external compliance on a CubeSat: your switching converters and your receiver are centimetres apart.
- **Deployment testing** – every deployable, many times, after vibration, in vacuum, at temperature extremes. See [Inhibits and HDRM](inhibits-hdrm.md#verification-and-testing).
- **Mass properties and fit check** – measured mass, centre of mass, and a physical fit check in a test pod. See [Structure – Mass Properties](structure.md#mass-properties-and-centre-of-mass).

**Standards disagree, and knowing that is useful.** A comparison of five widely used standards found thermal-vacuum qualification requirements ranging from 3 to 13 cycles, temperature margins of 5 °C or 10 °C, and dwell times from 1 hour to 24 hours – GSFC-STD-7000 specifying 4 qualification cycles with 10 °C margins and 24-hour dwells, ECSS-E-ST-10-03C 4 cycles with 5 °C margins, and NASA LSP-REQ-317.01 8 cycles with 10 °C margins and 1-hour dwells.[^ices-tvac] The authors' conclusion is the right one: **derive a tailored specification from your own mission's analysis rather than applying a generic one**. In practice, though, your launch provider's requirement is the one you must meet.

**Test sequence** follows a "test like you fly" logic: an initial functional test, mechanical environments, thermal environments, electrical/RF, then a final functional test – with reduced functional tests before and after each environmental block and after transportation, so that intermittent failures can be localised to a specific exposure.[^ecss-testing]

<!-- CSR-RESOURCES:START dev-ait-testing-standards -->
- **[ECSS-E-ST-10-03C Rev.1 – Testing](https://ecss.nl/wp-content/uploads/2022/05/ECSS-E-ST-10-03-Rev.1(31May2022).pdf)** `PDF` – Freely available ECSS testing standard defining qualification, acceptance and protoflight approaches, test types and test sequence
- **[NASA GEVS (GSFC-STD-7000)](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000)** `Link` – General Environmental Verification Standard, the default environmental envelope for many CubeSat campaigns
- **[Method for CubeSat Thermal-Vacuum Cycling Test Specification](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/ICES_2017_102.pdf)** `PDF` – ICES 2017 paper comparing thermal-vacuum requirements across five standards and proposing a tailoring method
- **[ISO 19683:2026 – Design qualification and acceptance tests of small spacecraft and units](https://www.iso.org/standard/86540.html)** `Link` – International standard specifically covering small spacecraft qualification and acceptance testing (paywalled)
<!-- CSR-RESOURCES:END dev-ait-testing-standards -->

#### Facilities and Test Laboratories

Environmental test facilities are expensive, and few CubeSat teams own them. The realistic options are a university lab, a national metrology or space agency facility, a commercial test house, or a programme such as ESA's Fly Your Satellite! that provides access as part of its support. Book early – facility lead times are frequently the long pole in a CubeSat schedule.

<!-- CSR-RESOURCES:START dev-ait-test-facilities -->
- **[ESA - CubeSat Support Facility](https://www.esa.int/Education/Educational_Satellites/CubeSat_Support_Facility)** `Link` – ESA AIT training and test facility
- **[ESA Fly Your Satellite! Test Opportunities](https://www.esa.int/Education/Educational_Satellites/Fly_Your_Satellite!_Test_Opportunities)** `Link` – Programme offering European university teams access to ESA test facilities
<!-- CSR-RESOURCES:END dev-ait-test-facilities -->

**DIY alternatives** have a real role, though not as a substitute for qualification. A shaker table built from a loudspeaker will not reproduce a launch spectrum, but it will find loose fasteners. A vacuum chamber without thermal control still catches [outgassing](../references/glossary.md#outgassing) and corona problems. A [Helmholtz cage](gnc.md#testing-and-validation) is genuinely buildable by a student team. Use DIY testing to find problems early and cheaply, and formal facilities to prove compliance.

### Functional and Integration Testing

- **Define what a functional test *is*, and write it down.** A **full functional test (FFT)** exercises every function and every mode; a **reduced functional test (RFT)** is a shorter check run before and after each environmental exposure. Both should be scripted procedures with recorded pass/fail criteria, not a person prodding at a console.
- **Automate them.** A functional test that takes a day by hand will be skipped under schedule pressure; one that runs in twenty minutes from a script will be run every time. This is one of the highest-return investments in a CubeSat programme.
- **Baseline early and compare.** Keep the results of every functional test. A parameter drifting slowly across a campaign is a warning you can only see if you kept the earlier data.
- **Regression testing.** Every hardware or software change invalidates prior results to some degree. Decide deliberately what needs re-running, and record that decision.
- **Test at every level** – subsystem alone, flatsat, integrated spacecraft – because each level finds different faults.

### Hardware-in-the-Loop (HIL) Testing

[HIL](../references/glossary.md#hil) testing connects real flight hardware to a simulated environment, and is the only practical way to exercise the spacecraft across a realistic mission timeline.

- **What gets simulated:** orbit and attitude dynamics, sensor outputs (magnetic field, sun vector, GNSS, star field), actuator responses, illumination and eclipse, ground station visibility.
- **What stays real:** the flight computer, the flight software, and as much of the avionics as practical.
- **Why it matters:** mode logic, [FDIR](../references/glossary.md#fdir) behaviour, [ADCS](gnc.md) control loops and power management are all *sequence-dependent* and only reveal their problems over many orbits. No amount of static functional testing substitutes.
- **Fault injection** is where HIL earns its keep: simulate a failed sun sensor, a saturated wheel, a dropped bus transaction, a brownout at a specific moment. These are the cases that decide whether the mission survives, and they are the ones that never occur during nominal testing.
- **Timing and latency** in the simulation loop must be representative, or the control loops you validate are not the ones you fly.

Open-source building blocks exist – orbit propagators, [SATMO](thermal.md#tools)-style thermal models, and the 42 spacecraft simulator bundled with [OpenSatKit](flight-software.md#open-source-flight-software-projects) – so a useful HIL rig is well within reach of a student team.

### Software Testing and Validation

Covered in depth under [Flight Software – Software Testing and Validation](flight-software.md#software-testing-and-validation). The AIT-specific points:

- **On-target testing** catches what host-based testing cannot: timing, memory limits, compiler behaviour, real driver interaction.
- **Watchdog and real-time behaviour** must be verified on the flight processor under realistic load, not in a simulator.
- **FDIR verification** requires deliberate fault injection at system level, with the real hardware responding.
- **Test the software you will fly.** The final environmental campaign should run the flight software build, not a test build with extra logging. If you must change it afterwards, re-run the functional tests.

### Mission Simulation

The final rehearsal, and the step most often cut for time.

- **Day-in-the-life ([DITL](../references/glossary.md#ditl)) testing** runs the spacecraft through a realistic 24-hour timeline – eclipse cycles, pass windows, payload operations, housekeeping – with the real ground segment on the other end. It routinely finds problems that no other test does, because it is the first time everything runs together at realistic timescales.
- **End-to-end data flow.** Payload data from acquisition, through storage, downlink, decoding, archiving and analysis, using the real chain. See [Payload – Testing and Verification](payload.md#testing-and-verification).
- **Simulated passes and RF loopback.** Verify the full RF chain with attenuated real signals, including Doppler if your ground software corrects for it. See [Ground Segment – Testing and Validation](ground-segment.md#testing-and-validation).
- **Contingency rehearsals.** Practise the procedures you hope not to need: recovery from safe mode, a software update, a failed deployment. Operators should have executed each at least once before launch.
- **Train the operators.** The people on console during [LEOP](../references/glossary.md#leop) should have run the mission simulation. Commissioning is a bad time to read a procedure for the first time.

## Documentation and Configuration Control

AIT generates the evidence that the spacecraft is what you claim it is, and that evidence is what your launch provider reviews.

- **Written, versioned procedures** for every assembly and test operation, with steps, expected results and space to record actuals. Two people: one performing, one recording.
- **A [baseline](../references/glossary.md#baseline) and as-built configuration record** – hardware revisions, serial numbers, firmware versions, torque values, harness build standard.
- **A non-conformance log.** Every anomaly, however minor, gets recorded with its investigation and disposition. The anomaly nobody wrote down is the one that recurs in orbit with no context.
- **Test reports** with dates, configuration, setup description, raw data and conclusions.
- **Photographs** at every stage, especially of things about to become inaccessible.

Two habits worth building early: **the test evidence package should assemble itself** as a byproduct of doing the work properly, rather than being reconstructed in a panic before delivery; and **a test result is only valid for the configuration it was taken in** – after any change, know what you invalidated.

---

👉 **Please consider [contributing](../contributing.md)!**

[^ecss-testing]: European Cooperation for Space Standardization, [*ECSS-E-ST-10-03C Rev.1 – Space engineering: Testing*](https://ecss.nl/wp-content/uploads/2022/05/ECSS-E-ST-10-03-Rev.1(31May2022).pdf), 31 May 2022. Freely downloadable. Defines qualification, acceptance and protoflight testing approaches, the associated margins (random vibration at maximum expected spectrum +3 dB for 2 minutes for qualification, +0 dB for 1 minute for acceptance), the full catalogue of environmental test types, and the "test like you fly" test sequence with reduced functional tests bracketing each environmental block.

[^ices-tvac]: Roy Stevenson Soler Chisabas, Geilson Loureiro, Carlos de Oliveira Lino and Daniel Fernando Cantor, ["Method for CubeSat Thermal-Vacuum Cycling Test Specification"](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/ICES_2017_102.pdf), *47th International Conference on Environmental Systems*, ICES-2017-102, Charleston SC, July 2017. Compares thermal-vacuum cycling requirements across GSFC-STD-7000, MIL-HDBK-340A, ECSS-E-ST-10-03C, TR-2004(8583)-1 Rev.A and NASA LSP-REQ-317.01, finding qualification cycle counts from 3 to 13, margins of 5–10 °C and dwell times from 1 to 24 hours, and argues for deriving a tailored specification from mission analysis rather than applying a generic standard.
