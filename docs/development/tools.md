# Tools and Helpers

This section collects practical tools that support CubeSat development and assembly. It includes physical tools (like crimpers, torque drivers, microscopes), custom jigs and fixtures for alignment or testing, as well as helpful software tools (ECAD, CAD, code, simulation, visualization) and calculators. Whether you're wiring harnesses, assembling PCBs, or measuring fastener torque, this is where the hands-on helpers live.

A note on priorities: a CubeSat lab does not need everything listed here on day one. The ordering that generally serves teams best is **measurement before fabrication** — a decent multimeter, a caliper and an oscilloscope earn their keep long before a reflow oven does — and **buy the tool that makes a job repeatable** rather than the one that makes it possible. Repeatability is what separates a spacecraft from a prototype.

## Hand Tools and Assembly Equipment

### Fastener tools

- **Calibrated torque driver.** The single most important tool on this page. CubeSats live on M2.5 and M3 fasteners in aluminium, where the gap between "not tight enough" and "stripped" is small. A driver covering roughly 0.2–2 Nm handles most CubeSat work. Have it calibrated, and record the torque applied to every fastener. See [Structure – Fasteners and Assembly](structure.md#fasteners-and-assembly).
- **Quality hex and Torx drivers.** Cheap drivers round out socket heads, and a rounded fastener in a nearly finished spacecraft is a genuinely bad afternoon.
- **Thread repair kit** — helicoils or thread inserts. Aluminium threads do not survive many cycles, and being able to repair one is much better than replacing a machined part.

### Wiring and harness tools

- **Proper crimp tools**, matched to the specific contact. A generic crimper produces joints that pass a continuity test and fail after vibration. This is the classic false economy in CubeSat assembly.
- **Wire strippers** sized for the small gauges used in flight harness (typically AWG 24–30), which ordinary strippers nick.
- **Contact insertion and extraction tools** for the connector families you use.
- **Heat gun** for heat-shrink, and a supply of appropriately rated shrink and sleeving — check outgassing before anything flies. See [AIT – Electrical Assembly and Harnessing](ait.md#electrical-assembly-and-harnessing).

### Soldering and rework

- **Temperature-controlled soldering station** with fine tips.
- **Hot air rework station** for surface-mount work and component removal.
- **Flux, braid, and a genuinely good extraction fan.** Fume extraction is a safety item, not a comfort one.
- A **reflow oven or hotplate** if you assemble your own boards.

### ESD control

Non-negotiable for flight hardware, and cheap: an ESD mat, a wrist strap with a verified ground, ESD-safe tools and storage bags, and humidity control where the climate makes static a problem. The failures ESD causes are usually latent — the part works, then fails weeks later — which makes them nearly impossible to diagnose after the fact.

### Cleanliness and handling

Nitrile gloves, lint-free wipes, isopropyl alcohol, and covered storage for anything that flies. Gloves for everything, without the exceptions that gradually erode over a long build. See [Structure – Cleanliness](structure.md#cleanliness-handling-and-contamination).

## Inspection and Measurement

- **Digital calipers** (0.01 mm resolution) as the everyday dimensional tool, and a **micrometer** where the tolerance genuinely warrants it. [Rail](../references/glossary.md#rail) dimensions are specified to ±0.1 mm, which calipers can just about resolve and a micrometer resolves comfortably.
- **A precision scale.** Mass is a tracked budget item, and per-component measured mass is far more useful than datasheet values. Something reading to 0.1 g covers most CubeSat components; a 0.01 g scale is better for small parts.
- **Stereo microscope or digital inspection camera** for solder joint inspection, connector examination and general "what actually happened here" work. A USB microscope is inexpensive and transforms board debugging.
- **Feeler gauges and pin gauges** for clearance and hole checks.
- **A surface plate and height gauge**, if you want to verify rail flatness and envelope dimensions without CMM access.
- **CMM access**, if you have it, for the definitive dimensional verification — but a fit check in a test pod is the answer that actually matters. See [Structure – Tolerancing and Stack-Up](structure.md#tolerancing-and-stack-up).
- **Mass properties measurement.** Centre of mass can be determined adequately with a knife-edge balance or a three-point scale setup and some arithmetic; commercial mass properties benches exist but are rarely justified at CubeSat scale. See [Structure – Mass Properties](structure.md#mass-properties-and-centre-of-mass).

Visual inspection remains the highest-yield inspection method for a small team. Photograph everything at every stage — it costs nothing and repeatedly turns out to be the only record of how something was before it was disturbed.

## Jigs, Fixtures, and Test Aids

Fixtures are where a little design effort produces disproportionate returns, because they convert a delicate operation into a repeatable one.

- **Assembly and alignment jigs** hold the stack square while standoffs are torqued, or locate a payload precisely during bonding.
- **Handling fixtures** protect the rails — the most tolerance-critical and most easily damaged surfaces on the spacecraft — and give somewhere safe to set the satellite down.
- **Test fixtures and breakout boards** exposing every bus and rail on accessible headers. Build these properly; you will use them for years. See [AIT – Flatsat](ait.md#flatsat-and-integration-test-setups).
- **Vibration test adapters** interfacing the spacecraft or its test pod to the shaker table.
- **Deployment test rigs**, including gravity offloading where the geometry allows, since a mechanism that deploys on a bench may be relying on gravity to help.
- **Thermal test fixtures** with low conductivity, so the fixture does not become the dominant heat leak in a [TVAC](../references/glossary.md#tvac) run — a common source of misleading thermal balance results.

**3D printing versus machining**: printed fixtures are cheap, fast to iterate and perfectly adequate for handling aids and soft jigs. Machined fixtures are worth it where dimensional accuracy or stiffness matters, or where the fixture will see load. Print first, machine what proves worth keeping.

Design fixtures with the same care as flight hardware in one respect: **they should make the wrong assembly impossible**, not merely make the right one convenient.

## Electrical and RF Test Equipment

### Power

- **A bench power supply with adjustable current limit** is the most important electrical instrument you own. The current limit is what prevents a wiring error from destroying a board.
- **A solar array simulator** is what a bench supply is *not*. A supply provides effectively unlimited current at a fixed voltage; a solar array does not, and that difference is precisely what [MPPT](../references/glossary.md#mppt) and brownout behaviour depend on. A programmable supply with an I-V curve capability, or a purpose-built simulator, changes the fidelity of EPS testing completely. See [EPS – Ground testing](eps.md#ground-testing).
- **An electronic load** for characterising battery packs and converters.
- **Current probes or shunt-based measurement** for per-channel current, ideally logged over hours so that mode transitions and duty cycles are visible.

### Signals

- **Oscilloscope.** Two channels is a minimum, four is much better — power rail, clock and two bus signals simultaneously is a common need. Bandwidth requirements for CubeSat work are modest; channel count and memory depth matter more.
- **Logic analyser**, ideally with protocol decoding for I²C, SPI, UART and CAN. A low-cost USB logic analyser is one of the highest-value-per-euro instruments available for debugging exactly the bus problems described in [OBC – Interfaces and Buses](obc.md#interfaces-and-buses).
- **Multimeter**, or several. Continuity and isolation checks on harness are performed constantly.

### RF

- **Spectrum analyser** for verifying transmitter output, spurious emissions and, importantly, the RF silence period during [inhibit](inhibits-hdrm.md#verification-and-testing) verification. A low-cost analyser or even an [SDR](../references/glossary.md#sdr) with calibrated attenuation covers a lot of ground.
- **Vector network analyser** for antenna matching and filter characterisation. Inexpensive VNAs covering VHF/UHF are now widely available and are entirely adequate for CubeSat antenna work.
- **Attenuators and dummy loads**, so that end-to-end RF testing can be done without transmitting into the air — which also keeps you legal. See [AIT – Mission Simulation](ait.md#mission-simulation).
- **An SDR** doubles as a receiver, a spectrum monitor and a signal-analysis tool. See [Ground Segment](ground-segment.md#sdr-rf-software).

**Practical tradeoffs for small teams:** buy the current-limited supply, the logic analyser and the caliper first. Borrow the shaker table and the TVAC chamber. Second-hand test equipment is generally excellent value, since instruments age well. And an instrument you cannot use is worth less than a cheaper one you understand.

## Software Tools

### Mechanical CAD and analysis

<!-- CSR-RESOURCES:START dev-tools-cad-and-fem -->
- **[FreeCAD](https://www.freecad.org/)** `Link` – Open-source parametric CAD with an integrated FEM workbench; increasingly capable and licence-free for student teams
- **[CalculiX](https://www.calculix.de/)** `Link` – Free three-dimensional structural finite element solver with static, dynamic and thermal capability (GPL)
- **[PrePoMax](https://prepomax.fs.um.si/)** `Link` – Open-source pre- and post-processor giving CalculiX a modern user interface
- **[Code_Aster](https://code-aster.org/)** `Link` – Open-source structural mechanics and thermomechanics solver developed by EDF R&D
- **[Elmer FEM](https://www.elmerfem.org/)** `Link` – Open-source multiphysics finite element software
<!-- CSR-RESOURCES:END dev-tools-cad-and-fem -->

Commercial options — SolidWorks, Fusion, Onshape, Ansys, Nastran/Femap — dominate in industry and most offer free or heavily discounted educational licences. See [Structure – Toolchains](structure.md#toolchains).

### Electronics design

<!-- CSR-RESOURCES:START dev-tools-ecad -->
- **[KiCad](https://www.kicad.org/)** `Link` – Free, open-source PCB design suite with schematic capture, PCB layout, 3D viewer, integrated SPICE simulation and a Gerber viewer; the default choice for open-hardware CubeSat projects
- **[cubestack.dev (beta)](https://cubestack.dev)** `Link` – Browser-based PC/104 stack configuration and validation tool with a board library, physical stack editor and power budget simulator
<!-- CSR-RESOURCES:END dev-tools-ecad -->

Using KiCad has a specific advantage for this community beyond cost: **open-hardware CubeSat designs are overwhelmingly published as KiCad projects**, so it is the format in which you can actually read other people's work. See the open-source missions in [CubeSat Missions](../references/missions.md).

### Orbital mechanics and mission analysis

<!-- CSR-RESOURCES:START dev-tools-orbital-analysis -->
- **[NASA GMAT (General Mission Analysis Tool)](https://software.nasa.gov/software/GSC-17177-1)** `Link` – Open-source mission design, optimisation and navigation tool used for real mission operations as well as analysis and teaching
- **[Basilisk](https://avslab.github.io/basilisk/)** `Link` – Open-source modular astrodynamics simulation framework from the University of Colorado AVS Lab, well suited to spacecraft dynamics and ADCS simulation
- **[CelesTrak](https://celestrak.org/)** `Link` – Orbital element sets, SGP4 references and a large body of astrodynamics documentation
<!-- CSR-RESOURCES:END dev-tools-orbital-analysis -->

Python has become the default language for this work, with mature libraries for SGP4 propagation, coordinate transformations and pass prediction. For a CubeSat team, a short Python script that propagates a TLE with [SGP4](../references/glossary.md#sgp4) and predicts passes is usually more useful than a large commercial package, and much easier to integrate with the [ground segment](ground-segment.md#tracking-and-pass-prediction).

### Thermal analysis

See [Thermal – Tools](thermal.md#tools) for open-source and commercial thermal modelling options, including SATMO and the single-node approach.

### Firmware and software development

- **Toolchains**: GCC for ARM, PlatformIO, vendor IDEs, and the build systems around them. Whatever you choose, make the build **reproducible** — a build that only works on one person's laptop is a bus-factor risk. See [Flight Software – Documentation and Maintainability](flight-software.md#documentation-and-maintainability).
- **Debuggers**: a JTAG/SWD probe is essential. Plan physical access to the debug header early. See [OBC – Integration and Testing](obc.md#obc-integration-and-testing).
- **Version control**: Git, for everything — firmware, ground scripts, documents, test procedures, CAD where practical.
- **Simulation and test harnesses**: the ability to compile flight software for the host and run it against simulated hardware is worth building deliberately.

## Calculators and Reference Tools

A small but growing collection of templates and worked examples that save you from rebuilding the wheel. Most are free; a few are reference documents rather than fillable templates, but all are useful starting points.

### Stack builders

- **[cubestack.dev (currently in beta)](https://cubestack.dev)** (Patrik Senkyr) – Interactive, browser-based [PC/104](../references/glossary.md#pc104) stack configuration and validation tool. Includes a board library, a physical stack editor and power budget simulator.

### Power Budget Templates

A power budget tracks energy consumption and generation across mission modes. See [EPS – Power Requirements and Budgets](eps.md#power-requirements-and-budgets) for the underlying methodology.

- **[Artemis CubeSat Kit Power Budget](https://docs.google.com/spreadsheets/d/1nS07D4-2hFsfBfmfiYS8sjpTHMR5pUvH-NhnE5spPVY)** (Hawaii Space Flight Lab) – multi-sheet template covering component-level draws, operational modes, and generation/storage balance. Free to copy in Google Sheets or download as `.xlsx`. The companion textbook chapter at [pressbooks-dev.oer.hawaii.edu/epet302](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-9-power-budget-and-profiling/) walks through how to use it step by step.
- **[BIRDS Project power analysis](https://birds-project.com/open-source/pdf/Power-Budget-Analysis-for-1U-satellit20220514.pdf)** (Kyushu Institute of Technology) – published power budget PDF for a 1U mission, with real beta angle assumptions and eclipse timing. Less of a template, more a worked example showing what a defensible analysis actually looks like.
- **["Power Budgets for Mission Success"](http://mstl.atl.calpoly.edu/~workshop/archive/2011/Spring/Day%203/1610%20-%20Clark%20-%20Power%20Budgets%20for%20CubeSat%20Mission%20Success.pdf)** (Craig Clark & Ritchie Logan, Clyde Space, 2011) – slide deck on the Cal Poly CubeSat workshop archive. Practical walkthrough on estimating orbit average power, managing loads, and avoiding negative power budgets.

### Mass Budget Template

- **[CubeSat Resources Mass Budget Template](https://docs.google.com/spreadsheets/d/1WSWPbPNYgs54KLPaoDrw7uAXzCtGm3vM/edit?usp=sharing&ouid=116943914669204149113&rtpof=true&sd=true)** – annotated spreadsheet with component-level mass tracking, automatic margin calculation, and form-factor limits for 1U through 6U.

### RF Link Budget Template

- **[Jan King Link Budget Calculators](https://iaru.amsat-uk.org/spreadsheet.htm)** (Jan King, VK4GEY/W3GEY / AMSAT-UK) – a collection of Excel spreadsheets for satellite link budget analysis, freely available for amateur and non-commercial use. The flagship tool is the *AMSAT/IARU Annotated Link Model System*, a detailed multi-sheet workbook that walks through every gain and loss term – path loss, antenna gains, noise figure, Eb/N₀, modulation – with explanatory notes alongside each calculation. Widely cited in CubeSat comms literature and used as a reference in the [Hawaii CubeSat textbook](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/software-lab-for-communications/). Free to download; `.xls` format. See also [Comms – Link Budget](comms.md#link-budget) and the [link budget](../references/glossary.md#link-budget) glossary entry.

### Other Budgets

- **Thermal**: see [Thermal – Tools](thermal.md#tools) for the single-node Python script and SATMO, both of which serve as worked thermal estimation examples rather than blank templates.
- **Data budget**: data generated per orbit versus downlink capacity. There is no widely used template for this — a spreadsheet with payload data rates, duty cycles, pass count, pass duration and link rate covers it, and it is worth building early because it constrains the mission more than teams expect. See [Comms – Expected Data Rates](comms.md#expected-data-rates).
- **PV budget**: a panel-by-panel photovoltaic generation analysis over the orbit and over the mission. See [EPS – Estimating generation](eps.md#estimating-generation).
- **Battery sizing**: the relation in [EPS – Sizing](eps.md#sizing) is straightforward enough to implement in a few spreadsheet cells; the difficulty is in the assumptions rather than the arithmetic.

<!-- CSR-RESOURCES:START dev-tools-additional-calculators -->
- **[Jan King Link Budget Calculators](https://iaru.amsat-uk.org/spreadsheet.htm)** `Link` – Collection of Excel link budget spreadsheets including the AMSAT/IARU Annotated Link Model System
<!-- CSR-RESOURCES:END dev-tools-additional-calculators -->

## Automation and Workflow Helpers

Automation is where a small team buys back time, and the returns compound over a multi-year project.

- **Automated functional tests.** A scripted test that runs in twenty minutes will be run after every change; a manual one that takes a day will be skipped under schedule pressure. This is the highest-return automation available to a CubeSat team. See [AIT – Functional and Integration Testing](ait.md#functional-and-integration-testing).
- **Continuous integration** for firmware and ground software — build on every commit, run the host-based unit tests, flag regressions. Free for open repositories.
- **Documentation CI.** This site is itself an example: MkDocs building from a Git repository on every push. The same pattern works for mission documentation, and it means the published document always matches the repository.
- **Test data collection scripts.** Instrument the bench: log currents, temperatures and telemetry to a file automatically rather than by hand. Long-duration tests are only useful if the data is captured.
- **Reproducible environments.** Containerised or scripted toolchain setup, so a new team member is productive in an hour and a build from three years ago still works. On a project with complete team turnover every few years, this is a reliability measure.
- **Automated ground operations** — pass scheduling, tracking, decoding and ingest. See [Ground Segment – Automation and Operations](ground-segment.md#automation-and-operations).

The general principle: **anything done more than about five times should be automated**, and anything whose manual execution could damage flight hardware should be automated sooner than that.

## Documentation and Knowledge Management

University CubeSat teams turn over completely in two to four years, which is comparable to the development timeline. Knowledge management is therefore not administrative overhead — it is the mechanism by which the project survives its own team.

- **Lab notebooks and build logs.** Dated, specific, and including the things that did not work. "Tried X, it failed because Y" is often more valuable than the record of what eventually worked.
- **Written procedures** for every repeated operation — assembly steps, test setups, operations. Two people: one performing, one recording.
- **Checklists** for anything with irreversible consequences. Pre-integration, pre-delivery, pre-pass. Checklists are how aviation stopped losing aircraft to forgotten steps, and the reasoning transfers directly.
- **Version control for hardware too.** Board revisions, mechanical drawings, BOMs and assembly instructions all belong in the repository alongside the code. See [Systems Engineering – Configuration and Change Management](systems-engineering.md#configuration-and-change-management).
- **A single source of truth for interfaces.** The command and telemetry dictionary, the [ICD](../references/glossary.md#icd) set, and the pin assignments should live in one place that both flight and ground software derive from.
- **An anomaly log** capturing every unexpected behaviour with its investigation and resolution. See [Systems Engineering – Lessons Learned](systems-engineering.md#lessons-learned-and-common-pitfalls).
- **Onboarding documentation** so a new member can get productive without a founder's attention. Write it the first time somebody joins, then keep it current.

A useful test: **if the three people who know most about the project left tomorrow, could the remaining team finish it?** For most CubeSat projects the honest answer is no, and closing that gap is documentation work.

---

👉 **Please consider [contributing](../contributing.md)!**
