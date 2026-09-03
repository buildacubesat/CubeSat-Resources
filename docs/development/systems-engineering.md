# Systems Engineering

Every CubeSat starts with a sentence – "measure X", "demonstrate Y", "give students flight experience". Systems engineering is the discipline of turning that sentence into something buildable without losing what mattered about it.

It is what holds the rest of this site together: the requirements that tell each subsystem what it is for, the interfaces where subsystems meet, the budgets that keep the whole thing physically possible, and the evidence that any of it works. On a large programme this is a department. On a CubeSat it is usually one person doing it alongside something else, which makes it easy to skip and expensive to have skipped.

---

## Mission Objectives and Requirements

### From objective to requirement

The chain runs: **mission objectives → mission requirements → system requirements → subsystem requirements**. Each level should be traceable up to the one above, so that when a subsystem requirement is challenged you can answer "because the mission needs it", and when a mission objective changes you can find every requirement it touched.

A workable requirement is:

- **Verifiable.** You can state, before you write it, how you will prove it – by test, analysis, inspection or demonstration. "The spacecraft shall be reliable" is not a requirement; "the spacecraft shall survive 8 thermal cycles between −35 °C and +75 °C" is.
- **Unambiguous.** One reading only. Avoid "adequate", "sufficient", "as required".
- **Necessary.** Traceable to something above it. If nothing above needs it, delete it.
- **Achievable.** Within the physics and the budget – and achievability is a claim you should be able to defend with a number rather than an instinct. A 1U with body-mounted cells averages **1–2 W across an orbit**, so a load that needs 8 W is not a requirement a 1U can hold; it is a decision to fly deployables or a bigger bus, and it should be recorded as one. See [EPS – Body-mounted vs deployable arrays](eps.md#body-mounted-vs-deployable-arrays).
- **Free of implementation.** A requirement states what, not how. "Shall use a reaction wheel" is a design decision that has been smuggled in as a requirement.

**Shall, should, may.** NASA, ECSS and launch providers all use the same convention, and it is worth adopting even in an informal requirements document. **Shall** is binding and will be verified. **Should** is a goal that is not verified and can be traded away. **May** is permission. Use "shall" only for things you intend to prove, because every "shall" becomes a row in the verification matrix – and a document full of "shall" statements nobody plans to verify teaches the team to stop reading them.

### Mission success criteria

Write down what counts as success, early, and at more than one level:

- **Minimum success** – the least outcome that justifies the mission. Often "the spacecraft was commissioned and returned housekeeping telemetry", which for a first flight is a legitimate and honest bar.
- **Full success** – the mission objectives met as stated.
- **Extended goals** – what you would do with a healthy spacecraft once the primary objectives are complete.

Two reasons this earns its place. It is what lets a team call a partially working mission a success without dishonesty, and partial is the normal outcome, so it deserves to be planned for rather than argued about afterwards. And it is the yardstick that [designing for partial failure](#designing-for-partial-failure) is measured against: you cannot design for graceful degradation without having said which capabilities are worth degrading gracefully.

Worth knowing that the published statistics use a similarly modest bar – the widely quoted 75% figure [below](#what-the-statistics-say) counts a CubeSat as a success if it survived [commissioning](../references/glossary.md#commissioning).

### Requirements you do not get to write

Not every requirement comes from your objectives. A substantial fraction is levied from outside, arrives non-negotiable, and lands earlier than teams expect:

- **The launch provider.** The [payload user guide](../references/glossary.md#payload-user-guide-pug) or deployer manual, and the [ICD](../references/glossary.md#icd) you sign against it, govern envelope, mass, centre of mass, materials, [inhibits](../references/glossary.md#inhibit), environmental levels and the evidence you must deliver. The [CDS](../references/glossary.md#cds) is the common language; the payload user guide is the contract, and where they disagree the payload user guide wins. See [Structure – The launch provider always wins](structure.md#the-launch-provider-always-wins).
- **Spectrum and licensing.** [IARU](../references/glossary.md#iaru) coordination, an [ITU](../references/glossary.md#itu) filing submitted through your national administration, and a transmit licence. Lead times run to months and the outcome constrains the [comms](comms.md) design from the start. See [Qualification and Launch – Frequency licensing](launch.md#frequency-licensing).
- **Debris and disposal.** Orbital lifetime limits, a debris assessment, and [passivation](../references/glossary.md#passivation) at end of mission. These bound your orbit choice and can force a deorbit device onto a spacecraft that had not budgeted for one. See [Qualification and Launch – Space debris mitigation](launch.md#space-debris-mitigation).
- **Your funder or institution.** Reporting, review gates, export control, and liability or insurance obligations under national space law.

The practical consequence is that these documents belong in your hands *before* you baseline requirements. External requirements are the ones most often discovered late, and a requirement discovered at integration costs far more than the same requirement discovered in Phase A.

### Science vs. technology demonstration

The distinction shapes everything downstream. A **science mission** has data quality requirements that cascade into pointing, calibration, stability and downlink – and a partial success may be scientifically worthless. A **technology demonstration** aims to raise a [TRL](../references/glossary.md#trl), and a component that fails informatively is still a result. Educational missions add a third dimension: the team's learning is an objective in its own right, which legitimately justifies building things you could have bought.

Being explicit about which you are doing prevents a lot of misallocated effort. See [Payload – Mission categories](payload.md#mission-categories).

### Over- and under-specification

Both failure modes are common, and both are expensive.

**Over-specification** is the more insidious. A pointing requirement of 0.1° when 1° would do can double the ADCS cost, add mass and power, and introduce a subsystem the team cannot debug. The most valuable question in requirements review is: *what actually breaks if this number were three times looser?* If the answer is "nothing", loosen it. See [GNC – Turning objectives into requirements](gnc.md#turning-objectives-into-requirements) for the classic case.

**Under-specification** leaves gaps that get filled by whoever gets there first. If nobody specifies the thermal environment the payload must survive, the payload team will assume something, the thermal team will assume something else, and the disagreement surfaces in [AIT](ait.md).

### Traceability

A **[requirements traceability](../references/glossary.md#requirements-traceability) matrix** links every requirement to its parent, to the design element that satisfies it, and to the verification activity that proves it. On a CubeSat this need not be elaborate – a spreadsheet is fine – but it needs to exist, because it is what tells you what a late change breaks, and it becomes the backbone of the [V&V](#verification-and-validation-vv) programme.

## Concept of Operations (CONOPS)

The **[CONOPS](../references/glossary.md#conops)** is the narrative of how the mission actually works, end to end. It is the most useful document a CubeSat team can write early, and the most commonly skipped.

Its value is that it forces concrete questions that requirements documents let you avoid: How many passes a day do we get, and how long are they? What does the spacecraft do between them? Who is at the console during LEOP? How does a payload observation get scheduled, executed, downlinked and processed? What happens if the battery is flat on first contact?

Some of those answers are already fixed by geometry rather than by choice. A single mid-latitude station sees a typical LEO CubeSat for roughly four to six usable passes a day – see [Ground Segment – The options](ground-segment.md#the-options) – and that number, not the link rate, is usually what caps the mission.

### What it should cover

- **Mission phases**: launch, deployment, [LEOP](../references/glossary.md#leop), [commissioning](../references/glossary.md#commissioning), nominal operations, extended mission, disposal – with what happens in each and what "done" looks like.
- **A nominal day**, in detail: orbits, eclipse cycles, ground station passes, payload operations, housekeeping. Walking through a single realistic day surfaces more design problems than any other exercise.
- **Operational scenarios** for each mission mode, showing how the spacecraft, ground segment and operators interact.
- **Off-nominal scenarios**: [safe mode](../references/glossary.md#safe-mode) entry and recovery, missed passes, a failed deployment, a subsystem lost. These become the contingency procedures.
- **The operations team** – who, how many, when, and with what training.

The CONOPS also feeds directly into [validation](#verification-and-validation-vv): it defines what the system is *for*, which is what validation checks. And it is the natural input to [AIT – Mission Simulation](ait.md#mission-simulation), where the day-in-the-life test is essentially the CONOPS executed against real hardware.

## System Architecture

### Functional and physical

**Functional architecture** describes what the system must do – generate power, store energy, determine attitude, downlink data – independent of how. **Physical architecture** assigns those functions to hardware. Keeping them separate for a while is a genuine discipline: it prevents the team from converging on a familiar block diagram before understanding what the mission needs, and it makes the [trade studies](#trade-studies-and-design-decisions) explicit.

### Recurring architectural choices

- **Centralised vs. distributed computing.** See [OBC – Centralised vs. distributed](obc.md#centralised-vs-distributed).
- **Buy vs. build, per subsystem.** Most CubeSats are hybrids – a bought structure and EPS with in-house avionics is a common pattern, and a defensible one. See [GNC – Integrated ADCS Units](gnc.md#integrated-adcs-units-buy-or-build).
- **Regulated vs. unregulated power distribution.** See [EPS – Bus architecture](eps.md#bus-architecture).
- **Passive vs. active attitude control**, which cascades into power, mass and complexity more than almost any other decision. See [GNC – Passive Stabilization](gnc.md#passive-stabilization-methods).
- **Form factor.** Chosen late by teams who regret it and early by teams who don't. It follows from payload volume, power need (and therefore panel area) and mass – and it is very hard to change once the structure is procured.

### Architectural drivers

Some constraints propagate through everything and are worth identifying explicitly and early:

- **Orbit** drives illumination, eclipse, thermal cases, radiation, contact opportunities and lifetime.
- **Payload** drives pointing, power, data volume and thermal.
- **Downlink capacity** caps what the mission can return regardless of what it collects.
- **Regulatory and provider constraints** arrive from outside and are not negotiable on your schedule. See [Requirements you do not get to write](#requirements-you-do-not-get-to-write).
- **Team size and skills** is a real architectural driver that formal methods rarely acknowledge. A four-person team should not architect a system that needs eight people to build.

### Partitioning

Draw subsystem boundaries where the interfaces are simplest, then assign clear ownership. Every boundary needs a named owner on each side, and every boundary needs an [ICD](#interfaces-and-interface-control-documents-icds). The most common CubeSat architectural failure is not a bad partition but an unowned one – a function that everybody assumed somebody else had.

## Interfaces and Interface Control Documents (ICDs)

Interfaces are where CubeSats fail. Individual subsystems, built by people who understand them, usually work. The problems surface when two of them meet.

### What an ICD covers

- **Mechanical**: mounting points, envelope, mass properties, alignment, thermal interface.
- **Electrical**: voltages, nominal and peak current, inrush, sequencing, connector and pin-out, grounding.
- **Data**: physical bus, protocol, addressing, message formats, timing and rates.
- **Functional**: command and telemetry dictionaries, modes, error behaviour.
- **Environmental**: temperature limits, vibration levels, cleanliness.

### Ownership and discipline

An [ICD](../references/glossary.md#icd) is a **contract between two owners**, and it works only if both sides are named and both sides agree to changes. Some practices that make the difference:

- **One document per interface**, not one giant document. Smaller documents get read.
- **Version everything**, and treat a change as a change requiring both parties' agreement – not a silent edit.
- **Write ICDs even for internal interfaces.** Two boards built by the same three people still benefit, because the ICD outlives the memory of why something was done.
- **Define error behaviour explicitly.** What happens if the other side does not respond? Returns garbage? Draws too much current? Undefined error behaviour is where interfaces actually break.
- **Machine-readable where possible.** A command and telemetry dictionary that generates both flight and ground code eliminates a whole class of desynchronisation bugs. See [Flight Software – Documentation](flight-software.md#documentation-and-maintainability).

### Common interface failure modes

- I²C address collisions between COTS boards. See [OBC – Interfaces and Buses](obc.md#interfaces-and-buses).
- Assumed power sequencing that nobody wrote down.
- Endianness and struct-packing mismatches between flight and ground software.
- Mechanical interference discovered at integration because two CAD models were never merged.
- Grounding assumptions that differ between subsystems, producing intermittent faults that only appear in [TVAC](../references/glossary.md#tvac).
- Firmware updated on one side of an interface without the other side being told.

## Budgets and Margins

Budgets are how systems engineering keeps a CubeSat realistic. Each one tracks a finite resource – mass, power, data rate, link margin, thermal capacity – against the demands placed on it by every subsystem. They start as rough allocations at concept stage and tighten as the design matures, real components are selected, and test data replaces datasheet promises.

### The main budgets

- **Mass budget**: per-component mass summed against the form-factor allocation. [CDS](../references/glossary.md#cds) Rev 14.1 caps mass at **2 kg per U** – 2.00 kg for a 1U through 24.00 kg for a 12U (§2.2.10, Table 1).[^cds-rev14] Older material still quotes Rev 13's figure of 1.33 kg/U, which was the community norm for years and is still repeated by some deployer documentation.[^cds-rev13] Neither is necessarily the number you design to: your launch provider's payload user guide takes precedence over the spec, and is often more restrictive. The mass budget is the simplest to maintain and the one most often neglected until it's too late. See the [Mass Budget Template](tools.md#mass-budget-template) under Tools.
- **Power budget**: [orbit](../references/glossary.md#orbit)-average consumption vs. generation, broken down by mission mode. See [EPS – Power Requirements and Budgets](eps.md#power-requirements-and-budgets) for methodology and [Tools](tools.md#power-budget-templates) for templates.
- **[Link budget](../references/glossary.md#link-budget)**: gain and loss accounting between transmitter and receiver, producing a [link margin](../references/glossary.md#link-margin) in dB. See [Comms – Link Budget](comms.md#link-budget).
- **Data budget**: data generated per orbit vs. downlink capacity given pass duration, ground station availability, and link rate. Tightly coupled to the link budget – you can't plan your downlink schedule without knowing the link rate, and you can't know the link rate without closing the link budget first.
- **Thermal budget**: heat generated by electronics and absorbed from the environment vs. radiated heat at hot and cold cases. See [Thermal](thermal.md).
- **Pointing budget**: the error terms between where the payload needs to point and where it actually points – sensor noise, estimation error, control error, mounting and alignment error, thermal distortion – combined into a single number and compared against the requirement. Missions with a pointing requirement should build one, because it is what reveals when the requirement is being set by a 1° misalignment nobody measured rather than by the control loop. See [GNC – ADCS Integration Considerations](gnc.md#adcs-integration-considerations).
- **Volume budget**: less rigorous than the others, but useful for tracking how much room is genuinely left after structure, harnessing, and mechanical clearances are accounted for. Especially easy to underestimate on dense 1U or 1.5U designs.

Missions carrying propulsion add a **[delta-v](../references/glossary.md#delta-v) budget**, allocated across orbit raising, phasing, collision avoidance and controlled deorbit. Most CubeSats have no propulsion and therefore no such budget.

### Margin philosophy

Margins exist because early estimates are wrong. The shape of a margin plan is always the same – wide early, tight at delivery – but the numbers are programme-specific, and, less obviously, **resource-specific**. A single curve applied to everything is the most common way to get this wrong.

NASA's Goddard sets its required margins per resource rather than as one number. Mass must stay above **15%** before and at the system requirements review, above **10% at [PDR](../references/glossary.md#pdr)**, above **5% at [CDR](../references/glossary.md#cdr)** and above 2% at the systems integration review, reaching zero in Phase D. Power, measured against **end-of-life** capacity, must stay above **15% at PDR** and above **10% at CDR**, and above 5% thereafter. Propellant is held to 3σ, and RF link margin above 3 dB, tightening to 1 dB from Phase C.[^gsfc-1000] Mass margin is spent faster than power margin for a good reason: mass converges as parts are weighed, while generation keeps degrading for the whole mission.

CubeSat practice runs above those figures, and defensibly so. **30% at PDR, 20% at CDR, 10% at flight** is a reasonable curve for a team with a short schedule, little [flight heritage](../references/glossary.md#flight-heritage), and datasheet numbers standing in for test data.[^nasa-margins] Treat it as a starting point that your own measurements replace, not as a rule.

A few principles that age well whichever numbers you start from:

- **Hold margin against the right baseline.** Mass margin belongs against your deployer's limit, not the CDS's. Power margin belongs against end-of-life generation, not beginning-of-life – sizing arrays for BOL efficiency is one of the most common ways a CubeSat power budget fails in year two.
- **Don't disguise growth as margin use**: if a subsystem grows by 100 g, that's 100 g of growth – not 100 g of margin "spent." Track the two separately so growth trends remain visible. A budget where margin only ever shrinks, and never grows back when a component is swapped for something lighter, is not being managed – it's being consumed.
- **Per-subsystem margins are not additive**: 20% margin on every line item is not the same as 20% margin on the total. Decide whether margin lives at the subsystem or system level, and stick to it.
- **Reserves are different from margins**: reserves are unallocated budget held by the systems lead for emerging needs. Margins are buffers within an existing allocation. Mixing them up makes both useless – a subsystem that raids system reserve to cover its own growth has broken the accounting.

### Iterating

Budgets are living documents. Update them after every major design decision, every test that produces real numbers, and every time a vendor delivers a component with different specs than the datasheet advertised. A budget that hasn't moved in months is either a finished design or, more often, an abandoned one.

For ready-to-use templates, see [Calculators and Reference Tools](tools.md#calculators-and-reference-tools).

## Trade Studies and Design Decisions

A **[trade study](../references/glossary.md#trade-study)** is a structured comparison of options against weighted criteria. Its real value is less the numerical answer than the record of *why* a decision was made – which is what lets a team six months (or three years) later understand a design rather than reverse-engineer it.

### Doing one usefully

1. **State the question precisely**, including what is fixed and what is open.
2. **Generate genuinely different options** – at least three, including "do nothing" or "buy it" where those are real.
3. **Choose criteria before scoring**, and weight them before you know how the options score. Weighting after the fact is how a trade study becomes a justification.
4. **Score honestly**, including uncertainty. A criterion where the options differ by 5% with 30% uncertainty is not discriminating.
5. **Sanity-check the answer.** If it feels wrong, either your intuition or your weighting is wrong, and finding out which is the useful part.
6. **Record it** – options, criteria, scores, decision, rationale – in a page or two.

### Criteria worth including

Cost, mass, power, volume, performance, risk, [TRL](../references/glossary.md#trl) and [flight heritage](../references/glossary.md#flight-heritage) are standard. Two that CubeSat teams routinely omit and should not:

- **Team capability and effort.** An option requiring skills the team does not have is more expensive than its price suggests.
- **Schedule and procurement risk.** A part with a nine-month lead time may be the wrong choice regardless of how well it scores otherwise.

### Knowing when to stop

Most CubeSat decisions do not deserve a formal trade study. The judgement call is whether the decision is **hard to reverse** (structure, form factor, bus architecture, ADCS approach) or **cheap to change** (a connector, a sensor part number). Spend the effort on the former.

For the rest, "good enough" is a legitimate engineering conclusion, and an early decision that is 80% right usually beats a perfect decision made three months later – because everything downstream was blocked in the meantime.

## Reliability and Risk Management

### What the statistics say

CubeSat reliability is measurable, and the numbers are sobering but improving. A statistical overview of the first thousand CubeSats put the success rate at **about 75%**, excluding launch failures, and found that **around 20% of all failures occurred during launch or the deployment phase**.[^villela]

The definition behind that 75% is worth knowing, because it is more modest than it sounds: a CubeSat counted as a success if it "survived its early operational stages (deployed and commissioned)" – in the authors' words, if "it did not die as an infant". A spacecraft that failed six months in is inside the 75%. The same paper reports that success rates have risen over time and that its data *suggest* infant mortality is decreasing, which is a softer claim than the headline number and worth reading as such.

The pattern behind those figures is consistent with what teams report anecdotally: a large share of CubeSat failures happen very early, and they are dominated not by exotic space effects but by things that could have been caught on the ground – power system faults, software that cannot recover, interfaces that were never tested together, and deployables that did not deploy.

### Identifying single points of failure

A **[single point of failure](../references/glossary.md#spof) (SPOF)** is any element whose failure ends the mission. On a CubeSat there will be many, and the useful exercise is not eliminating them but knowing where they are.

Walk each subsystem and ask what a total failure does. The mission-ending ones cluster predictably:

- The battery, the EPS, and the power path.
- The OBC, if nothing else can command a recovery.
- The radio, and the antenna deployment that makes it useful.
- The deployment switches and inhibit chain.
- The bus linking OBC to EPS. See [OBC – The bus reliability problem](obc.md#the-bus-reliability-problem).

### Mitigations, roughly in order of value per gram

1. **Simplicity.** The most effective reliability measure available. Every removed component and every removed mode is a removed failure mode.
2. **Test coverage**, especially of fault paths. See [AIT](ait.md) and [Flight Software – Software Testing](flight-software.md#software-testing-and-validation).
3. **Autonomous recovery.** A spacecraft that resets and comes back is far more valuable than one that requires ground intervention it cannot request. See [Flight Software – FDIR](flight-software.md#fault-detection-isolation-and-recovery-fdir).
4. **Functional redundancy** – another element able to do the job in degraded form.
5. **Hardware redundancy** – genuine duplication, which costs mass, power and the switching mechanism.

The honest CubeSat position is that **redundancy is usually the wrong answer and better testing is usually the right one.** Mass and volume are too scarce for meaningful duplication, and the observed failure modes are largely ones testing would have caught.

### Designing for partial failure

Ask, for each subsystem, what a *degraded* mission looks like. A spacecraft that loses one solar panel deployment, one reaction wheel, or its payload but keeps a healthy bus is still returning something. Designing so that failures degrade rather than terminate is cheaper than redundancy and often more effective – and the [success criteria](#mission-success-criteria) you wrote at the start are what tell you which degraded outcomes still count.

### Running a risk register

Keep a simple list: the risk, its likelihood, its consequence, the mitigation, and who owns it. Review it at every milestone. The value is not the scoring – CubeSat risk scoring is largely guesswork – but the discipline of periodically asking "what worries us, and what are we doing about it?" A risk that has been on the list unchanged for six months is either not real or not being managed.

## Configuration and Change Management

Configuration management answers one question: **what, exactly, is this spacecraft?** It sounds bureaucratic until the first time a test result cannot be interpreted because nobody knows which firmware was loaded.

### What to control

- **Hardware**: board revisions, serial numbers, which unit is installed where, modification status.
- **Software and firmware**: version, build, and which hardware it is running on. Tag what flies.
- **Documentation**: requirements, ICDs, procedures, drawings – all versioned.
- **Configuration data**: parameter tables, calibration values, thresholds. These change more often than code and are tracked less often.

### Practices proportionate to a CubeSat

- **Everything in version control**, including documents, ground scripts and test procedures. A repository is cheaper than a process.
- **Baseline at milestones.** Freeze a coherent set at [PDR](../references/glossary.md#pdr), [CDR](../references/glossary.md#cdr) and delivery, and record what changed between them.
- **An as-built record** for the flight article: what is installed, which revision, what torque, which firmware.
- **A change log with rationale.** The *why* is what future readers need.
- **Impact assessment before a change**, using the traceability matrix: what requirements does this touch, and what test evidence does it invalidate?

### Preventing drift

Configuration drift is what happens when the [flatsat](../references/glossary.md#flatsat), the flight model and the documentation slowly stop describing the same thing. It is nearly universal on CubeSat projects and it is what makes test results untrustworthy. The countermeasures are unglamorous: periodic audits comparing as-built against as-documented, one person nominally responsible, and a culture where an undocumented change is treated as a defect.

## Verification and Validation (V&V)

The distinction matters and is easily blurred. NASA's Systems Engineering Handbook puts it cleanly: **verification** demonstrates "proof of compliance with requirements – that the product can meet each 'shall' statement", while **validation** shows "that the product accomplishes the intended purpose in the intended environment" and meets stakeholder expectations, relating back to the [CONOPS](#concept-of-operations-conops).[^nasa-se-handbook]

Informally: verification asks *did we build the thing right?*; validation asks *did we build the right thing?* A spacecraft can pass every verification and still fail validation, if the requirements were wrong.

### The four verification methods

- **Analysis** – mathematical or simulation-based demonstration. Used where testing is impractical, such as on-orbit thermal behaviour or structural margins.
- **Demonstration** – show the function operating, without detailed measurement. Appropriate for operational and procedural requirements.
- **Inspection** – visual or dimensional examination. Appropriate for mass, dimensions, workmanship, markings.
- **Test** – operate the item and measure. The strongest evidence, and the most expensive.

Assign a method to every requirement *when you write it*. A requirement whose verification method cannot be identified is a requirement that needs rewriting.

### Linking to AIT

The verification matrix – requirement, method, activity, evidence, status – is what turns the [AIT](ait.md) campaign from a series of tests into a compliance argument. Each test procedure should state which requirements it verifies, and each result should close them out. Done properly, the evidence package assembles itself as a byproduct of doing the work.

### When is a requirement verified enough?

The pragmatic answer: when the evidence would convince a competent sceptic who did not build it. A single successful run of a mechanism is not verification; a hundred runs across temperature and after vibration is. Analysis alone is weak where testing was feasible. And **verification evidence is only valid for the configuration it was taken in** – after a change, know what you invalidated.

## Mission Phases and Operations

Formal programmes use a phase structure, and while a CubeSat team need not adopt the full apparatus, the underlying sequence is genuinely useful because it tells you what should be settled by when. NASA runs Pre-Phase A through Phase F.[^nasa-se-handbook] ECSS divides the life cycle into seven phases – Phase 0 (mission analysis and needs identification), A (feasibility), B (preliminary definition), C (detailed definition), D (qualification and production), E (utilisation) and F (disposal) – which map onto the NASA sequence closely enough that mixed teams rarely have trouble.[^ecss-m-st-10]

| Phase | Purpose | CubeSat reality |
|---|---|---|
| Pre-Phase A | Concept studies, feasibility | "Could we do this?" – often a semester |
| Phase A | Mission architecture, [baseline](../references/glossary.md#baseline) requirements | Requirements, CONOPS, initial budgets |
| Phase B | Preliminary design, technology development | Ends at [PDR](../references/glossary.md#pdr); 30% margins |
| Phase C | Detailed design, fabrication | Ends at [CDR](../references/glossary.md#cdr); 20% margins |
| Phase D | Assembly, integration, test, launch | [AIT](ait.md); the phase that always overruns |
| Phase E | Mission operations | [LEOP](../references/glossary.md#leop), commissioning, nominal ops |
| Phase F | Decommissioning and closeout | Passivation, disposal, data archiving, publication |

Two observations specific to CubeSats. First, **the phases overlap heavily** – a small team cannot serialise design, build and test, and pretending otherwise produces a fictional schedule. Second, **Phase F is routinely forgotten**, and it is where the mission's lasting value is realised: archived data, published results, and lessons written down while the team still exists. See [Qualification and Launch – End of Life](launch.md#end-of-life).

**Reviews** punctuate the phases, and each asks a different question. Few CubeSat teams hold all of them formally; the point is to know which question is going unasked.

- **[PDR](../references/glossary.md#pdr)**, ending Phase B – is the design likely to meet the requirements, and are the requirements themselves right? The last cheap moment to change the architecture.
- **[CDR](../references/glossary.md#cdr)**, ending Phase C – is the detailed design complete and buildable, and is the verification programme defined?
- **Test readiness review**, before each major environmental campaign – is the article in the configuration you intend to test, is the procedure written and reviewed, and are the pass/fail criteria agreed before the data exists rather than negotiated afterwards?
- **Pre-ship review**, before delivery – is the evidence package the launch provider expects actually complete? See [AIT – Sequencing](ait.md#sequencing) and [Qualification and Launch – Documentation checklist](launch.md#documentation-checklist).

All of them are dramatically more valuable with **external reviewers**. Someone who did not build it will ask the question the team stopped asking a year ago.

<!-- CSR-RESOURCES:START dev-systems-engineering-standards -->
- **[NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2)](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)** `PDF` – Requirements, the four verification methods, validation, and the Pre-Phase A to Phase F life cycle. Written for far larger programmes, but the concepts scale down cleanly. Free PDF
- **[ECSS-M-ST-10C Rev.1 – Project planning and implementation](https://ecss.nl/standard/ecss-m-st-10c-rev-1-project-planning-and-implementation/)** `Link` – The European equivalent, and the source of the Phase 0 to Phase F structure. Free, registration required
- **[ECSS-E-ST-10C Rev.1 – System engineering general requirements](https://ecss.nl/wp-content/uploads/2017/02/ECSS-E-ST-10C-Rev.1(15February2017).pdf)** `PDF` – The engineering-branch companion: requirements engineering, analysis, design, verification and system engineering integration and control. Freely available
- **[GSFC-STD-1000 Rev H](https://standards.nasa.gov/sites/default/files/standards/GSFC/H/0/GSFC-STD-1000RevH_Approved.pdf)** `PDF` – Goddard's design rules, including the technical resource margin table that sets separate mass, power, propellant and link margins per phase. Free PDF
<!-- CSR-RESOURCES:END dev-systems-engineering-standards -->

## Lessons Learned and Common Pitfalls

### Typical failure patterns

Drawn from the statistics above and from the recurring themes across this site:

- **Power system faults and unrecoverable software** account for a large share of early failures. The spacecraft either cannot maintain a positive energy balance or cannot get itself back to a commandable state.
- **Failure during launch or deployment** accounts for roughly a fifth of all failures.[^villela]
- **Mechanisms** are disproportionately represented – over 10% of reported small satellite failures, per NASA's survey.[^nasa-soa-structures] See [Structure – Deployables](structure.md#deployable-structures-and-mechanisms).
- **Bus lockups**, particularly I²C, with documented catastrophic cases. See [OBC](obc.md#the-bus-reliability-problem).
- **Never acquiring signal at all**, which is often a ground segment problem rather than a spacecraft one – wrong [TLE](../references/glossary.md#tle), uncorrected uplink Doppler, an untested decoder.

### Engineering pitfalls

- Assuming nominal attitude before the ADCS is proven, and discovering a tumbling spacecraft generates a third of the modelled power.
- Sizing solar arrays for beginning-of-life efficiency.
- Testing only with a charged battery and a bench supply, so cold-start and brownout are never exercised.
- Software that can disable its own recovery path.
- Deployables tested once, in air, in one orientation, before vibration.
- Ground segment finished after launch.
- Interfaces verified on paper but never with both real subsystems connected.

### Organisational pitfalls

These are as damaging as the technical ones and get discussed far less.

- **Bus factor.** University teams turn over completely in two to four years, comparable to the development timeline. Undocumented knowledge simply evaporates. Documentation is a reliability measure.
- **Unowned interfaces.** Every interface needs a named owner on each side. The gaps between subsystems are where projects fail.
- **Optimistic scheduling.** Every CubeSat project takes longer than planned. Build float, especially into [AIT](ait.md) and the regulatory path.
- **Requirements that were never written down**, so each subsystem designed to a different assumption.
- **Scope growth**, particularly the extra payload added because there was room. Each addition costs more than it appears.
- **Not capturing anomalies.** The problem nobody wrote down is the one that recurs in orbit with no context.

### Capturing and reusing lessons

- **Keep a non-conformance and anomaly log from day one**, and record dispositions.
- **Hold retrospectives at milestones**, not only at the end.
- **Write and publish a lessons-learned paper.** These are among the most valuable documents in the CubeSat literature and among the rarest, because teams disperse before writing them. The mission examples in [CubeSat Missions](../references/missions.md) show what open documentation looks like when teams do follow through.
- **Read other people's.** Nearly every failure described on this page has already happened to somebody who wrote about it.

---

👉 **Please consider [contributing](../contributing.md)!**

[^cds-rev14]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 14.1*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (9 February 2022). Free PDF. Section 2.2.10 and Table 1 set the mass limits: 2.00 kg for a 1U, 3.00 kg for a 1.5U, 4.00 kg for a 2U, 6.00 kg for a 3U, 12.00 kg for a 6U and 24.00 kg for a 12U. Rev 14 raised the long-standing 1.33 kg/U figure to 2 kg/U and reframed many requirements as guidelines rather than hard constraints. Always confirm the applicable limit with your launch provider; ISS deployers and rideshare providers maintain their own mass budgets and may be more restrictive.

[^cds-rev13]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 13*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/56e9b62337013b6c063a655a/1458157095454/cds_rev13_final2.pdf). Free PDF. Section 3.2.10 states that "the maximum mass of a 1U CubeSat shall be 1.33 kg", with §3.2.11 to §3.2.13 setting 2.00 kg, 2.66 kg and 4.00 kg for 1.5U, 2U and 3U respectively. This was the widely adopted figure for most of the CubeSat community and remains the number many deployers still quote.

[^gsfc-1000]: NASA Goddard Space Flight Center, [*GSFC-STD-1000 Rev H – Rules for the Design, Development, Verification, and Operation of Flight Systems*](https://standards.nasa.gov/sites/default/files/standards/GSFC/H/0/GSFC-STD-1000RevH_Approved.pdf) (approved 15 March 2023). Free PDF, approved for public release. Rule 1.06 and Table 1.06-1 set required technical resource margins separately for each resource and phase: mass above 15% through the system requirements review, above 10% at PDR, above 5% at CDR and above 2% at the systems integration review, reaching zero from Phase D; power, with respect to end-of-life capacity, above 25%, 20%, 15%, 10% and 5% from Pre-Phase A through Phase D; propellant to 3σ; and RF link margin above 3 dB through Phase B, tightening to above 1 dB from Phase C. Mass margin is defined as (allowable − predicted) / basic × 100, following AIAA S-120A-2015.

[^nasa-margins]: The 30/20/10 curve is a CubeSat convention rather than a published requirement. Its closest formal analogue is the NASA NTRS paper by David A. Di Pietro, ["Techniques for Conducting Effective Concept Design and Design-to-Cost Trade Studies"](https://ntrs.nasa.gov/api/citations/20150018331/downloads/20150018331.pdf) (2015), which describes project managers holding 25% margins for power and dry mass at the start of Phase B, with targets of ≥20% at end of Phase B and ≥15% at end of Phase C. Free PDF. NASA's binding requirements are lower than both and are set per resource rather than as a single curve: GSFC-STD-1000 Rev H requires mass margin above 10% at PDR and above 5% at CDR, and power margin above 15% at PDR and above 10% at CDR. CubeSat teams carry more early margin than any of these to compensate for short schedules, little flight heritage, and datasheet figures standing in for test data.

[^villela]: Thyrso Villela et al., ["Towards the Thousandth CubeSat: A Statistical Overview"](https://onlinelibrary.wiley.com/doi/10.1155/2019/5063145), *International Journal of Aerospace Engineering*, 2019, Article ID 5063145, DOI 10.1155/2019/5063145. Open access. Estimates the CubeSat success rate at about 75% excluding launch failures, where a mission counts as a success if "it survived its early operational stages (deployed and commissioned)" – in the authors' phrasing, if "it did not die as an infant". Finds that around 20% of all failures occur during launch or the deployment phase, reports that overall success rates are increasing over time, and states that its data "suggest that CubeSat infant mortality is decreasing".

[^nasa-soa-structures]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 6: Structures, Materials, and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/). Open access. States that mechanisms "have contributed to over 10% of reported small satellite failures", with design simplicity, margin, supplier selection and testing given as the mitigations.

[^nasa-se-handbook]: NASA, [*NASA Systems Engineering Handbook*, NASA/SP-2016-6105 Rev 2](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf). Free PDF. The standard reference on the discipline: defines verification as "proof of compliance with requirements – that the product can meet each 'shall' statement" and validation as showing "that the product accomplishes the intended purpose in the intended environment", lists analysis, demonstration, inspection and test as the verification methods, and sets out the Pre-Phase A to Phase F project life cycle. Comprehensive and aimed at much larger programmes than a CubeSat, but the concepts scale down cleanly.

[^ecss-m-st-10]: ECSS, [*ECSS-M-ST-10C Rev.1 – Space project management: Project planning and implementation*](https://ecss.nl/standard/ecss-m-st-10c-rev-1-project-planning-and-implementation/) (6 March 2009). Free, registration required. Clause 4.4.1 divides the life cycle of space projects into seven phases: Phase 0 (mission analysis/needs identification), Phase A (feasibility), Phase B (preliminary definition), Phase C (detailed definition), Phase D (qualification and production), Phase E (utilisation) and Phase F (disposal).