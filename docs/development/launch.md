# Qualification and Launch

This page covers everything between a finished spacecraft and a deployed one: turning the test campaign into a delivery package, buying a launch, insurance, frequency licensing, registration, export control and debris rules, deployers, delivery, the run-up to first contact, and end of life. The testing itself is on [AIT](ait.md).

The recurring theme of this page is **lead time**. Building the spacecraft is under your control; frequency coordination, export licensing, safety review and manifest availability are not. Teams that treat these as end-of-project paperwork routinely find that their hardware is ready and their spacecraft still cannot legally or contractually fly. Start all of them early – a year or more before launch is not excessive.

## Qualification

Qualification is the process of demonstrating, with evidence, that the spacecraft will survive launch and function in orbit. The testing itself is covered in [AIT](ait.md#environmental-testing); what matters here is that the *outputs* of that campaign become the delivery package your launch provider reviews. The full list is in the [documentation checklist](#documentation-checklist) below.

Two practical points that shape how you plan the campaign. First, **the review is iterative** – expect questions, expect to supply additional evidence, and budget weeks rather than days for each cycle. Second, **test evidence is only valid for the configuration it was taken in**; a late change to the spacecraft may invalidate a report you have already submitted, and re-testing at that stage is expensive in both time and hardware life.

Two items in the package get disproportionate attention:

- **Inhibit verification evidence** is the single most scrutinised part of a CubeSat safety data package. See [Inhibits and HDRM – Documentation and Compliance](inhibits-hdrm.md#documentation-and-compliance).
- **Battery safety documentation** – cell datasheets, pack design, protection circuits, test results. Requirements are considerably stricter for ISS deployment, where the spacecraft spends time inside a crewed vehicle.

## Documentation and Interfaces

### Interface Control Documents

The [ICD](../references/glossary.md#icd) between your spacecraft and the launch provider defines the boundary: mechanical envelope, mass and centre of mass, electrical interfaces (if any – most CubeSats have none in flight beyond the deployment switch), environmental levels, and the deployment sequence.

Your provider will issue their own **payload user guide** and deployer manual, and those documents govern. Where the [CDS](../references/glossary.md#cds) and the provider's manual disagree, the manual wins – Exolaunch states this explicitly for the EXOpod Nova. See [Structure – The launch provider always wins](structure.md#the-launch-provider-always-wins).

### The "do no harm" principle

Rideshare payloads fly alongside someone else's primary mission, and the governing requirement is that you cannot endanger it. NASA's survey describes this directly: "a list of 'do no harm' requirements is imposed on the rideshare satellites by the launch provider, launch integrator, or primary mission owner", and these "usually include restrictions on transmitters, post separation mechanical deployments, and hazardous materials".[^nasa-soa-launch]

In practice this is what generates the [inhibit](../references/glossary.md#inhibit) requirements, the RF silence period, the deployable delay, and the battery scrutiny. Understanding that framing helps: reviewers are not being obstructive, they are protecting a payload worth far more than yours.

### Documentation checklist

The delivery package, in one place:

- Interface control document and dimensional drawings
- Mass properties report – **measured, not calculated**, against the [deployer](../references/glossary.md#deployer)'s limits. See [Structure – Mass Properties](structure.md#mass-properties-and-centre-of-mass)
- Inhibit block diagram and state table with test evidence
- Environmental test reports – vibration, thermal vacuum and any shock testing, with levels, durations, configuration and results
- Battery safety data package
- Materials list with outgassing data, particularly where non-metals sit near sensitive surfaces
- Deployment mechanism description and test results
- Frequency licence and coordination evidence
- Orbital debris assessment / [deorbit](../references/glossary.md#deorbit) plan
- Export control documentation where applicable
- Integration procedures and any late-access requirements
- Fit check results, from a test pod and often from the actual deployer before delivery

## Launch Procurement

### Routes to orbit

- **Rideshare aggregators / brokers** are the normal path. They buy capacity in bulk, provide the deployer, handle integration and much of the interface work, and sell you a slot. Exolaunch, D-Orbit, ISILaunch, Maverick Space Systems, SEOPS and Alba Orbital (for PocketQubes) operate in this space. For a first mission the broker's experience is worth as much as the slot itself – they have seen the mistakes before.
- **Direct with the launch provider.** SpaceX's Transporter programme publishes pricing; NASA's survey, revised May 2026, cites "Falcon 9 rides starting at $350k for ~50 kg, with a high launch cadence".[^nasa-soa-launch] Confirm the current rate with the provider before budgeting – published rideshare pricing has moved upward more than once. You still need a deployer and an integrator in practice.
- **Dedicated small launchers** – Rocket Lab's Electron, Firefly's Alpha, ISRO's SSLV and others. Far more expensive per kilogram, but you choose the orbit and the schedule rather than accepting the primary's. Electron is the most widely used small vehicle as of April 2026.[^nasa-soa-launch] Read the capacity figures carefully, because vendors quote different orbits: Rocket Lab publishes **300 kg to LEO** for Electron, and Firefly publishes **1,030 kg to a 300 km LEO but 630 kg to a 500 km SSO** for Alpha.[^launcher-performance] The sun-synchronous figure is the one that matters for most CubeSat missions, and it is typically the smaller one.
- **[Orbital transfer vehicles](../references/glossary.md#otv)** – D-Orbit's ION (first used in 2020 and flown 21 times as of December 2025), Rocket Lab's Photon, Impulse Space's Mira, Momentus's Vigoride – take you from the rideshare drop-off orbit to something closer to what you wanted.[^nasa-soa-launch] A growing option when the available rideshare orbit is wrong for your mission, including when it is too high to deorbit passively.
- **ISS deployment** via NASA's CubeSat Launch Initiative, JAXA's J-SSOD, or commercial providers such as Nanoracks. CubeSats deploy at **51.6° inclination into a 400–420 km orbit, one to three months after berthing**.[^nasa-soa-launch] The low altitude means a short orbital lifetime (typically months to about two years), which is convenient for debris compliance and inconvenient for a long mission. Safety requirements are the strictest of any route, because the spacecraft spends time inside a crewed vehicle.
- **Free and subsidised programmes** – NASA CSLI, ESA's Fly Your Satellite!, UNOOSA/JAXA KiboCUBE. Competitive, slow, and genuinely free. Worth applying to early. See [Getting Started](../getting-started.md).

### What you are actually buying

- **Orbit.** Rideshare means accepting the primary's orbit. Sun-synchronous at 500–600 km is the most commonly available and suits most Earth-observation and technology missions. Check the [beta angle](../references/glossary.md#beta-angle) behaviour and eclipse profile against your [power budget](eps.md#power-requirements-and-budgets) before committing – **and check the orbital lifetime**, because this altitude band is above the point where passive decay reliably meets current disposal rules. See [Space debris mitigation](#space-debris-mitigation).
- **Schedule, and its slip.** Launch dates move. Build schedule margin, and understand the contractual consequences of *you* slipping rather than the launcher.
- **Integration support.** How much interface work the broker does, and how much falls to you.
- **Deployer.** Which pod, and therefore which envelope, mass and centre-of-mass limits apply.

### Timeline

Working backwards from launch, a realistic ordering:

- **18–24 months before:** start conversations with brokers; begin frequency coordination; identify export control implications.
- **12 months:** contract signed; deployer selected; ICD baselined.
- **6–12 months:** safety data package and qualification evidence submitted; expect iteration.
- **1–6 months:** flight hardware delivered. This varies by provider and is the number to confirm early, because it is the real deadline – not launch day.
- **Launch:** the spacecraft has been out of your hands for months and you may or may not be present.

**If the CubeSat is not ready, it does not fly.** The manifest does not wait.

<!-- CSR-RESOURCES:START dev-launch-procurement -->
- **[NASA State of the Art – Integration, Launch, Deployment and Orbital Transport](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/)** `Link` – Survey of launch vehicles, rideshare pricing, deployer hardware, separation systems and orbital transfer vehicles
- **[SpaceX Rideshare Program](https://www.spacex.com/rideshare/)** `Link` – Transporter and Bandwagon rideshare programme, with published pricing and a booking interface
- **[Exolaunch](https://exolaunch.com/)** `Link` – Launch brokerage, deployer hardware (EXOpod, EXOtube) and integration services for CubeSats
- **[NASA CubeSat Launch Initiative](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative)** `Link` – NASA programme providing launch opportunities to US educational and non-profit CubeSat developers
- **[ESA Fly Your Satellite!](https://www.esa.int/Education/Educational_Satellites)** `Link` – ESA education programme offering support, test facilities and launch opportunities to European university teams
<!-- CSR-RESOURCES:END dev-launch-procurement -->

## Insurance

Insurance for CubeSats is unusual in that most missions carry none, and that is often the right decision.

- **Third-party liability** is the exception. Under the Outer Space Treaty and the Liability Convention, the launching state bears international responsibility for damage caused by objects launched from its territory, and many national space laws pass that liability to the operator and require insurance as a licensing condition. **Check your national law** – in several jurisdictions this is compulsory rather than optional.
- **Pre-launch insurance** covers damage or loss during transport, storage and integration. Relatively cheap, and worth considering for a spacecraft that took three years to build and cannot be quickly rebuilt.
- **Launch and in-orbit insurance** covers loss of the spacecraft itself. Premiums are a substantial fraction of the insured value, and for a CubeSat whose hardware cost is small relative to the labour invested, the economics rarely work. You cannot insure three years of student effort.
- **The realistic risk picture** is that CubeSat mission failures are dominated by the spacecraft's own faults rather than launch failures, and those are not what launch insurance covers.

The UK is a useful worked example of how specific this gets. Under the Outer Space Act 1986 and the Space Industry Act 2018 the standard third-party liability requirement is **€60 million**, and while the insurance requirement "may be waived for low-risk missions", the €60 million indemnity obligation to the government remains either way; operator liability is separately capped in the licence itself.[^uk-caa] Numbers and mechanisms differ substantially elsewhere, so treat this as an illustration of the shape of the obligation rather than a template.

The practical advice: treat third-party liability as a legal question to answer early, treat pre-launch cover as a cheap option worth pricing, and treat in-orbit cover as something most CubeSat missions correctly skip.
<!-- NEEDS HUMAN VERIFICATION: Only the UK position has been checked against a primary source. Country-specific pointers for the US, Switzerland, Germany and the other jurisdictions readers of this site are likely to be in would make this section considerably more actionable, but each needs verifying against the relevant national authority rather than inferred from the UK model. -->

!!! warning
    Nothing on this site is legal advice. Insurance and liability obligations depend on your national legislation and on the launching state, and both should be checked with someone qualified.

## Regulatory Requirements

### Frequency licensing

You need authorisation to transmit, and the process depends on which bands you use.

- **Amateur bands (UHF/VHF).** Coordination through the **[IARU](https://www.iaru.org/reference/satellites/)**, requested via your national member society, plus a licence from your national regulator. A team member must hold an appropriate amateur licence and takes personal responsibility for compliance. Amateur service rules constrain what you may do – no commercial use, and restrictions on encryption. The [IARU](../references/glossary.md#iaru) coordination process is free, well documented and generally straightforward, but it takes months.
- **Non-amateur bands (S-band, X-band).** Filing through your national regulator, who coordinates with the **[ITU](../references/glossary.md#itu)**. Slower, more expensive, and with genuine risk of not obtaining what you asked for. Start at least 18 months out.
- **Remote sensing licences** are separate. If you image the Earth you may need authorisation from a national body – NOAA in the US, and equivalents elsewhere.

A point that is easy to get wrong: **the international filing goes through your national administration in both cases**, amateur included. Advance publication information, then notification and recording with the ITU, is submitted by the administration, not by you and not by the IARU. IARU coordination is a peer process within the amateur satellite service – a prerequisite for using the allocation, and its outcome carries weight with regulators – but it is not a licence and it does not replace the national filing. Teams that treat a successful IARU coordination as "the paperwork is done" discover the gap late, when it is expensive.

**Without frequency authorisation in place, your spacecraft will not be permitted to deploy.** This is the single most common regulatory reason a finished CubeSat misses its launch.

### Space object registration

States are obliged under the Registration Convention to register objects they launch, and your national authority will require information from you: orbital parameters, general function, and identification. This is usually administrative rather than difficult, but it has a deadline.

### Export control

- **ITAR/EAR (US)** and equivalent regimes elsewhere control spacecraft components and technical data. Some CubeSat items – notably **[GNSS receivers capable of operating at orbital velocity](../references/glossary.md#cocom-limits)**, and certain propulsion and imaging components – fall under dual-use control.
- **The Wassenaar Arrangement** is the multilateral regime most European regulations derive from.
- The practical impacts are procurement lead time, restrictions on who may access technical data (relevant for international student teams), and constraints on publishing detailed designs. For an open-source project this last point deserves early thought.

### Space debris mitigation

Debris rules have tightened significantly and now affect CubeSat design directly.

- The long-standing international guideline was disposal within **25 years** of mission end.
- The **[FCC](../references/glossary.md#fcc) adopted a "5-year rule" in 2022 (FCC 22-74, adopted 29 September 2022)**, requiring that spacecraft "ending their mission in, or passing through, the LEO region below 2000 km altitude" complete disposal "as soon as practicable, and no later than five years after the end of the mission".[^fcc-5yr] Note who this catches: it applies to **Part 97 amateur satellites and Part 5 experimental authorisations**, not only commercial Part 25 licences, and to non-US systems seeking US market access. A university mission on amateur UHF is inside it. The two-year grandfathering for already-authorised but unlaunched satellites expired on **29 September 2024**, so there is no transitional relief left.
- **ESA moved in the same direction in November 2023.** Its Space Debris Mitigation Policy and the accompanying requirements (ESSB-ST-U-007) cut the LEO disposal phase "from 25 to a maximum of five years" and require that "the probability of successful disposal must be larger than 90%".[^esa-sdm] These bind missions procured and operated by ESA, which includes Fly Your Satellite! teams.

What this means in practice: **check your orbital lifetime during design, not after, and check it against 400 km rather than 600 km.** NASA's survey is blunt about where the boundary sits – small spacecraft "launched at or around 400 km altitude naturally decay in under five years, however at orbital altitudes beyond 500 km, there is no guarantee the spacecraft will deorbit within that timeframe, and some may not deorbit within 25 years".[^nasa-soa-deorbit] That puts the most commonly available rideshare orbit, sun-synchronous at 500–600 km, on the wrong side of the line for a passive CubeSat. Above roughly 400 km you should expect to demonstrate compliance rather than assume it, with a drag sail or deorbit device (effective up to about 800 km for suitable area-to-mass ratios),[^nasa-soa-deorbit] [propulsion](propulsion.md), an [orbital transfer vehicle](../references/glossary.md#otv) to a lower drop-off, or simply a lower orbit. You will also be asked for an **orbital debris assessment** and an end-of-life plan, including [passivation](../references/glossary.md#passivation) – safely discharging batteries and de-energising the spacecraft so it cannot fragment.

### Regulatory resources

<!-- CSR-RESOURCES:START dev-launch-registration-and-frequency-management -->
- **[Guidance on Space Object Registration and Frequency Management for Small and Very Small Satellites (ITU)](https://storage.googleapis.com/cubesat-resources/resources/registration-and-frequency-management/handout-on-small-satellitese.pdf)** `PDF` – ITU handout introducing the two administrative processes every operator has to complete: registering the object with a national authority and securing frequency authorisation. Free PDF
- **[Handbook on Amateur and Amateur-Satellite Services (ITU-R, 2026 edition)](https://storage.googleapis.com/cubesat-resources/resources/dev-launch-registration-and-frequency-management/itu-handbook-amateur-amateur-satellite-2026.pdf)** `PDF` – ITU-R Handbook R-HDB-52, 2026 edition, covering the regulatory basis of the amateur and amateur-satellite services. Free PDF
- **[Small Satellites Support (ITU-R)](https://www.itu.int/en/ITU-R/space/support/smallsat/Pages/default.aspx)** `Link` – ITU guidance on small satellite spectrum matters
- **[IARU Amateur Satellite Frequency Coordination](https://www.iaru.org/on-the-air/satellites/)** `Link` – The coordination process for amateur-band satellite frequencies
- **[FCC 5-Year Rule for Deorbiting Satellites](https://www.fcc.gov/document/fcc-adopts-new-5-year-rule-deorbiting-satellites-0)** `Link` – FCC Report and Order requiring LEO satellite disposal within five years of mission completion
<!-- CSR-RESOURCES:END dev-launch-registration-and-frequency-management -->

## Launch Integration

### Deployers

The deployer defines your mechanical world. NASA's survey divides them into two families:[^nasa-soa-launch]

- **Rail-type** dispensers are the dominant design, with more than fifteen manufacturers worldwide, supporting form factors up to 16U. Examples include Exolaunch's EXOtube and EXOpod, ISISPACE's DuoPack and ISIPOD, and Maverick's Mercury series. The CubeSat's [rails](../references/glossary.md#rail) slide against matching rails inside the pod.
- **Tab-type** dispensers are a minority design in which the spacecraft is retained by tabs rather than rails – Rocket Lab's Advanced Satellite Dispenser being the notable example. They impose a different mechanical interface, so the choice is not transparent to your structure.

Above CubeSat scale, the **[ESPA ring](../references/glossary.md#espa-ring)** is the standard secondary payload adapter, featuring six 38 cm (15″) ports that can each support up to 257 kg.[^nasa-soa-launch]

The historically important deployer is the Cal Poly **[P-POD](../references/glossary.md#p-pod)**, whose interface conventions shaped the standard everything since has followed.

### Fit checks and delivery

- **Do a fit check early**, in a test pod, before the design is frozen. Providers supply test pods for exactly this – Exolaunch's TestPod and ISISPACE's equivalents. An early fit check is the cheapest possible way to discover an envelope violation.
- **Final inspection and handover.** Expect a joint inspection covering envelope, mass properties, inhibit state, RBF pin condition and general workmanship.
- **Battery state at delivery.** The spacecraft may sit for months. Confirm the pack will still be above its minimum voltage at deployment, and find out whether the deployer's access ports allow late charging. See [EPS – Energy Storage](eps.md#energy-storage).
- **Late access.** Anything you need to do after handover – charging, a final functional check, RBF removal – must be negotiated in advance and documented in the integration procedure.
- **Shipping.** Transporting flight hardware internationally involves customs, possibly export licences, and a real risk of damage. Use a proper transport case with shock and humidity recording, and consider pre-launch insurance.

### Preparing for LEOP

The gap between handover and first contact is often two to four months, during which nothing about the spacecraft can change. Use it:

- **Rehearse [LEOP](../references/glossary.md#leop)** with the flatsat and the real ground segment. See [AIT – Mission Simulation](ait.md#mission-simulation).
- **Confirm your TLE identification strategy.** You will initially be one of many objects from the same deployment. See [Ground Segment – Tracking and Pass Prediction](ground-segment.md#tracking-and-pass-prediction).
- **Get the ground segment fully automated and tested**, because the days after deployment are when you least want to be debugging a rotator.
- **Write and rehearse contingency procedures** – no signal, tumbling faster than expected, safe mode on first contact.
- **Publish your beacon format** so the [SatNOGS](../references/glossary.md#satnogs) community can help find you.

## End of Life

Worth planning during design rather than at the end:

- **Passivation** – discharging batteries and de-energising the spacecraft so it cannot explode or fragment. Increasingly a licensing requirement, and it needs to be a commandable function that actually works.
- **Deorbit compliance** – see the debris rules above. If your orbit does not decay in time, the mitigation is hardware and must be in the design from the start. Note that ESA now also asks for a **probability** of successful disposal, not merely a plan, which makes the reliability of the deorbit mechanism part of the argument.[^esa-sdm]
- **Data archiving** – the mission's data should outlive the spacecraft. See [Ground Segment – Data Handling and Archiving](ground-segment.md#data-handling-and-archiving).
- **Publish what you learned.** Lessons-learned papers from CubeSat missions are disproportionately valuable to the community, and disproportionately rare – most teams disperse before writing one.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-launch]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 10: Integration, Launch, Deployment, and Orbital Transport](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/) (revision dated 18 May 2026). Open access. Source for SpaceX Transporter rideshare pricing (from $350k for ~50 kg), Electron being the most widely used small vehicle as of April 2026, rail-type vs. tab-type dispenser families and manufacturer counts, ESPA ring specifications (six 38 cm ports, 257 kg each), D-Orbit ION flight history, ISS deployment parameters (51.6° inclination, 400–420 km, 1–3 months after berthing), and the "do no harm" rideshare requirement framing. Note that its small-launcher performance table appears to mix LEO and sun-synchronous figures – see the next footnote.

[^launcher-performance]: Manufacturer-published performance, checked against the NASA survey table: Rocket Lab, [*Electron*](https://www.rocketlabcorp.com/launch/electron/), states 300 kg / 661 lb to LEO; Firefly Aerospace, [*Alpha*](https://fireflyspace.com/alpha/), states 1,030 kg to a 300 km LEO and 630 kg to a 500 km SSO. The NASA survey lists both vehicles in a "performance to LEO" column at 200 kg and 630 kg respectively, which for Alpha is its sun-synchronous figure. Always confirm the orbit a quoted capacity refers to.

[^fcc-5yr]: Federal Communications Commission, [*Mitigation of Orbital Debris in the New Space Age*, Second Report and Order, FCC 22-74](https://docs.fcc.gov/public/attachments/FCC-22-74A1.pdf), adopted 29 September 2022. Requires space stations "ending their mission in, or passing through, the LEO region below 2000 km altitude" to complete post-mission disposal "as soon as practicable, and no later than five years after the end of the mission", replacing the 25-year guideline. Applies to US-licensed operators, to non-US systems seeking US market access under 47 CFR § 25.137, to small satellites under the streamlined § 25.122 process, and to Part 5 experimental and Part 97 amateur authorisations. Satellites already in orbit at adoption are exempt; authorised-but-unlaunched satellites had a two-year grandfathering period that ended 29 September 2024. A [plain-language summary](https://www.fcc.gov/document/fcc-adopts-new-5-year-rule-deorbiting-satellites-0) is also published.

[^esa-sdm]: European Space Agency, [*New Space Debris Mitigation Policy and Requirements in effect*](https://esoc.esa.int/new-space-debris-mitigation-policy-and-requirements-effect). The ESA Space Debris Mitigation Policy and the associated requirements standard ESSB-ST-U-007 Issue 1 came into effect in November 2023, reducing the low-Earth-orbit disposal phase "from 25 to a maximum of five years" and requiring that "the probability of successful disposal must be larger than 90%". Applies to missions procured and operated by ESA, and is promoted more widely through the Zero Debris Charter.

[^nasa-soa-deorbit]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 13: Deorbit Systems](https://www.nasa.gov/smallsat-institute/sst-soa/deorbit-systems/). Open access. States that small spacecraft "launched at or around 400 km altitude naturally decay in under five years, however at orbital altitudes beyond 500 km, there is no guarantee the spacecraft will deorbit within that timeframe, and some may not deorbit within 25 years", that natural decay in under five years "can be achieved for most SmallSats at altitudes <400 km", and that drag devices can be deployed "for certain area-to-mass ratios in altitudes equal to or lower than 800 km" to meet the five-year requirement.

[^uk-caa]: UK Civil Aviation Authority, [*Insurance and liability*](https://www.caa.co.uk/space/resources/insurance-and-liability/). Sets the standard third-party liability insurance and indemnity limit for orbital operations under the Outer Space Act 1986 at €60 million, notes that the insurance requirement "may be waived for low-risk missions (but €60m indemnity obligation remains)", and states that all operator licences issued under the Space Industry Act 2018 contain a limit of operator liability. Cited as one worked example; other jurisdictions differ substantially.