# Getting Started

CubeSats are satellites in the nanosat class built around a published standard, the [CubeSat Design Specification](references/glossary.md#cds) (CDS). Standardised form factors share common deployer hardware, which lowers the cost of development and launch and makes access to space attainable for small teams, universities and individuals.

This page is for those new to CubeSats or small satellite development. It gives you a broad overview of what a CubeSat is, how a project runs, which constraints decide your design before you start drawing, and where to go next on this site.

!!! tip "Unfamiliar term?"
    The [Glossary](references/glossary.md) defines the acronyms and concepts used across this site. Most pages link into it directly.

## The Standard in Numbers

The current revision is **CDS Rev. 14.1** (February 2022), maintained by the Cal Poly CubeSat Laboratory. It covers 1U through 12U in a single document.[^cds]

- A [1U](references/glossary.md#u-cubesat-unit) is nominally a 10 cm cube. The actual envelope is **100.0 × 100.0 × 113.5 mm** – the extra height is the rails, and designing to a flat 100 mm is the classic first mistake.
- Mass is **2 kg per U** in Rev. 14.1. Older material still quotes the Rev. 13 figure of 1.33 kg/U.
- Deployables stay stowed for the first **30 minutes** after deployment, and the radio stays silent for the first **45 minutes**.

!!! warning "Your launch provider outranks the CDS"
    The CDS is the common language, not the contract. Deployer envelopes, mass limits, inhibit counts and materials rules vary between providers, and the [payload user guide](references/glossary.md#payload-user-guide-pug) you sign against always takes precedence. Get that document early and design to it.

Details on [Structure – Form Factors and the CubeSat Envelope](development/structure.md#form-factors-and-the-cubesat-envelope), and the specification itself on [Standards & Protocols](references/standards.md).

## Where to Start

### Read first

- [NASA's CubeSat 101](https://www.nasa.gov/wp-content/uploads/2017/03/nasa_csli_cubesat_101_508.pdf) – beginner-friendly overview of CubeSat design and mission planning, written by Cal Poly for NASA. The single best starting point.
- [NASA CubeSat Launch Initiative Resources](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative/cubesat-launch-initiative-resources/) – a curated list of documents covering nearly everything a new project needs.
- [The CubeSat Design Specification](https://www.cubesat.org/cubesatinfo) – the official framework for CubeSat form factors, and the source of the physical and operational constraints on your mission.
- [Nano Avionics' CubeSat 101](https://nanoavionics.com/blog/cubesat-101-the-comprehensive-guide-to-understanding-satellite-technology) – a shorter, higher-level overview if the NASA document is too much at once.
- [The case for open source in CubeSat development](https://visionspace.com/how-to-build-a-cubesat-and-use-open-source-101/) – summary of an interview with Artur Scholz of LibreCube.
- [Wikipedia](https://en.wikipedia.org/wiki/CubeSat) – history and context.

### Learn systematically

- [KiboCUBE Academy](https://www.unoosa.org/oosa/en/ourwork/access2space4all/KiboCUBE_Academy_Webinars.html) – UNOOSA/JAXA lecture series covering mission design through subsystems to operations. Free, structured, and the closest thing to a full CubeSat course.
- [A Guide to CubeSat Mission and Bus Design](https://pressbooks-dev.oer.hawaii.edu/epet302/) – University of Hawai'i open textbook with worked examples.
- More on the [Courses, Events and Educational Kits](references/courses.md) page, including educational kits you can build against.

### Stay current

- A few well-chosen [newsletters](references/newsletters.md) will keep you up to date with the industry at large.
- The [Small Satellite Conference proceedings](https://digitalcommons.usu.edu/smallsat/) are freely accessible and are the richest source of CubeSat engineering literature anywhere. See [Papers](references/papers.md).
- Shameless plug: I am developing an open source CubeSat and documenting the process. If that is useful to you, see the [Build a CubeSat channel](https://youtube.com/@buildacubesat), the [website](https://buildacubesat.space/) and the [source on Codeberg](https://codeberg.org/buildacubesat-project).

## Development Flow

CubeSat projects usually fall into one of two categories, and knowing which one you are in shapes almost every decision that follows.

**Result-oriented missions** have a payload that needs to reach orbit and return data. Here it is usually advisable to source a bus with [flight heritage](references/glossary.md#flight-heritage) – structure and subsystems that have flown before – from an established vendor, and spend your effort on the payload and the ground segment.

**Process-oriented missions** treat the learning as the point. You will build a larger share of the flight segment yourself. This is absolutely feasible, but it is more iterative and shifts effort into integration, qualification and testing. Expect to build a [flatsat](references/glossary.md#flatsat) or engineering model first – all subsystems laid out on a bench – for easier debugging and early verification.

Most academic missions land in between: source the parts where failure is expensive and schedule-critical (typically structure and EPS), build the rest in-house.

Whichever you are, the discipline that holds a CubeSat project together is systems engineering – requirements, a [CONOPS](references/glossary.md#conops), interfaces, and the mass, power and link budgets that constrain everything else. If you read one page on this site before starting, make it [Systems Engineering](development/systems-engineering.md).

### Project Phases

Formal programmes use NASA's Pre-Phase A through Phase F or the ECSS equivalent. A CubeSat team does not need the full apparatus, but the sequence tells you what should be settled by when – see [Systems Engineering – Mission Phases and Operations](development/systems-engineering.md#mission-phases-and-operations). In practical terms:

- Feasibility Study
- Fundraising
- Mission and Requirements Definition
- Launch Provider Procurement
- Flight Segment Design and Development
- Ground Segment Design and Development
- Regulatory Approval and Licensing
- Mission Insurance Procurement (optional)
- Assembly, Integration and Testing
- Launch Campaign and Integration
- Launch
- Commissioning and Operations
- Disposal

### Milestones

- [ ] Feasibility studies completed
- [ ] Funding is secured
- [ ] Mission requirements baselined
- [ ] Preliminary Design Review ([PDR](references/glossary.md#pdr)) completed
- [ ] Critical Design Review ([CDR](references/glossary.md#cdr)) completed
- [ ] Frequency coordination and licence applications submitted
- [ ] Export control implications identified
- [ ] End-of-life and debris mitigation plan documented
- [ ] Flight/qualification hardware procured
- [ ] Flight/qualification hardware tested
- [ ] Flatsat testing completed
- [ ] Functional tests performed at system level
- [ ] Environmental tests performed at system level
- [ ] Launch service provider selected and contract signed
- [ ] Interface Control Document ([ICD](references/glossary.md#icd)) baselined with the launch provider
- [ ] Ground station operational and tracking other satellites
- [ ] Mission insurance policy secured (optional)
- [ ] All regulatory approvals granted
- [ ] Flight ready
- [ ] Launch opportunity is secured
- [ ] Delivered to the launch site
- [ ] Launched
- [ ] Commissioned
- [ ] Entered Nominal Operations
- [ ] Passivated
- [ ] Deorbited

!!! note
    A full CubeSat development project typically takes 1–2 years or more from initial planning to launch and operations. That includes everything from prototyping and documentation to regulatory approvals and environmental testing. Most likely, **the process will not be linear**, and different parts of your system will be at different stages at any given time.

## Constraints to Settle Early

Four decisions are cheap to make at the start and expensive to revisit. Teams that get into trouble usually got into it here.

**Orbit and disposal.** Your altitude decides your orbital lifetime, and your lifetime is now a regulatory matter rather than a design preference. At or around 400 km natural decay handles it; beyond 500 km there is no guarantee, and in the commonly available 500–600 km sun-synchronous band a passive CubeSat should expect to demonstrate compliance – with a drag device, propulsion or a lower orbit – rather than assume it. Settle this during design – see [Space debris mitigation](development/launch.md#space-debris-mitigation) – and read [Propulsion](development/propulsion.md) before assuming a thruster is the answer.

**Spectrum.** Amateur or licensed – the choice constrains your business model, not just your radio, because the amateur satellite service prohibits commercial use of the link. It also has the longest lead time of anything on your schedule. See [Communications – RF Overview](development/comms.md#radio-frequency-communications-rf-overview) and [Frequency licensing](development/launch.md#frequency-licensing).

**Export control.** If your team includes non-nationals, you ship hardware across a border, or you buy controlled components – [GNSS receivers that work at orbital velocity](references/glossary.md#cocom-limits) being the classic CubeSat example – export control applies to you. For an open-source project, what you may publish deserves early thought. See [Export control](development/launch.md#export-control).

**Launch safety.** [Inhibits](references/glossary.md#inhibit), deployment switches, the [RBF pin](references/glossary.md#rbf-pin) and battery qualification are structural design drivers, not paperwork added at the end. Inhibit evidence is the most scrutinised item in a delivery package. See [Inhibits and HDRM](development/inhibits-hdrm.md).

## Sourcing and Building

For subsystems and components, start with [SatSearch](https://satsearch.co/), [SatCatalog](https://www.satcatalog.com/) (rebranding to SatBase) and the [CubeSat Shop](https://www.cubesatshop.com/); more on the [Websites](references/websites.md#component-sourcing) page.

On the open-source side there is far more flight-proven material available than most newcomers expect – complete missions with published schematics, software and lessons learned. The [CubeSat Missions](references/missions.md) page collects them, the [educational kits](references/courses.md#educational-kits) are the fastest way to get hardware on a bench, and [Flight Software](development/flight-software.md#open-source-flight-software-projects) lists the frameworks worth building on rather than reinventing. Reading someone else's flown design is the cheapest engineering you will ever do.

## Getting to Orbit

Start looking for a ride early. It aligns you with your provider's requirements, avoids costly redesigns, and gives you access to their documentation while there is still time to act on it. The routes, in rough order of how most CubeSats fly:

- **Rideshare through an aggregator or broker** – Exolaunch, D-Orbit, ISILaunch, SEOPS and others buy capacity in bulk, supply the [deployer](references/glossary.md#deployer) and handle much of the interface work. For a first mission the broker's experience is worth as much as the slot.
- **Dedicated small launchers** – Rocket Lab's Electron, Firefly's Alpha, ISRO's SSLV. More expensive per kilogram, but you choose the orbit and the schedule.
- **[Orbital transfer vehicles](references/glossary.md#otv)** – when the available rideshare orbit is wrong for your mission.
- **ISS deployment** – via NASA's CSLI, JAXA's J-SSOD or commercial providers. Deployment is at 51.6° into a 400–420 km orbit, so lifetime is short and disposal compliance easy, but the safety requirements are the strictest of any route.
- **Free and subsidised programmes** – [NASA CSLI](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative) for US educational and non-profit developers, [ESA Fly Your Satellite!](https://www.esa.int/Education/Educational_Satellites) for teams in ESA member states, and [UNOOSA Access to Space for All / KiboCUBE](https://www.unoosa.org/oosa/en/ourwork/access2space4all/index.html) more widely. Competitive and slow, but genuinely free. Apply early.

!!! warning "The cheap-launch era may be pausing"
    Since 2020, SpaceX's Transporter and Bandwagon missions have set the price of access to orbit – around USD 350,000 for up to 50 kg, roughly USD 7,000/kg above that.[^rideshare-price] In July 2026 SpaceX was reported to have **stopped taking new commercial rideshare bookings beyond late 2028**, with Falcon 9 capacity redirected to next-generation Starlink and other internal payloads.[^rideshare-freeze] No replacement programme has been announced. Dedicated small launchers currently sell at roughly USD 15,000–25,000/kg, and the announced European and US alternatives are not yet flying at the cadence needed to absorb the demand.

    For a team starting now, a 1–2 year development means launching straight into that window. Practical response: talk to brokers earlier than you otherwise would, treat launch cost as a range rather than a number in your funding case, and take the free programmes and ISS routes more seriously than you might have in 2024.

Two things worth internalising before you build a schedule: your real deadline is hardware delivery, not launch day – typically one to six months earlier – and if the CubeSat is not ready, the manifest does not wait. Full detail on what you are actually buying, the working-backwards timeline, deployers, insurance and delivery is on [Qualification and Launch](development/launch.md).

## Regulatory Approval

What applies to you depends on where your team is based, where your launch provider is based, and what you intend to do in orbit. Four things need starting early, and none of them are under your control once started:

- **Frequency authorisation.** [IARU](references/glossary.md#iaru) coordination plus a national licence for amateur bands, or a national filing coordinated with the [ITU](references/glossary.md#itu) for other bands. The international filing is submitted by your national administration, not by you and not by the IARU. Months, not weeks – and **without it your spacecraft will not be permitted to deploy**. This is the most common regulatory reason a finished CubeSat misses its launch.
- **Space object registration** with your national authority, which forwards it to the UN. Administrative, but it has a deadline. Note that some countries, Switzerland among them, have no national space law yet, and teams there typically route authorisation through another state – find out which situation you are in early, because it can determine which providers you can fly with.
- **Export control**, as above.
- **Remote sensing**, if you image the Earth – a separate licence from a national body such as NOAA in the US.

!!! warning
    Nothing on this site is legal advice. You will need to familiarise yourself with your own country's legislation, rules and best practices around launching and operating a satellite.

The full treatment is on [Qualification and Launch – Regulatory Requirements](development/launch.md#regulatory-requirements).

## Mission Operations

Once deployed you begin commissioning: acquiring the signal, establishing two-way contact, and checking that each subsystem is alive and behaving. Only then does the mission enter its operational phase.

Plan time, money and people for this. Missions run from a few months to several years, and operations need someone available to take passes, including at inconvenient hours during [LEOP](references/glossary.md#leop). Two things pay for themselves before launch: rehearsing the first days with your flatsat and real ground station, and publishing your beacon format so the [SatNOGS](references/glossary.md#satnogs) community can help you find your satellite. Many missions have been first detected by a stranger.

See [Ground Segment](development/ground-segment.md) and [Preparing for LEOP](development/launch.md#preparing-for-leop).

## Budget Expectations

Rough orders of magnitude, excluding labour and assuming current launch pricing:

| Type | Typical range |
| :---- | :---- |
| Academic 1U–3U, largely in-house, sponsored or donated launch | tens of thousands |
| Academic or small-commercial 3U–6U, sourced bus, purchased rideshare | low hundreds of thousands to ~1 million |
| Commercial 6U–12U with a capable payload and full qualification | several million |

Launch, environmental testing and licensing are the line items teams most often underestimate – and see the note above on where launch pricing may be heading.

## Communities and Next Steps

- [Development](development/index.md) – the technical content of this site, subsystem by subsystem.
- [References](references/index.md) – glossary, standards, books, papers, missions, courses.
- [Communities](references/communities.md) – forums, organisations and programmes worth joining, including the [Build a CubeSat Discord](https://bac.page/discord) and the [Libre Space Community](https://community.libre.space/).

The CubeSat and amateur satellite communities are unusually willing to help. A well-posed question with real data attached almost always gets a useful answer.

---

👉 **Please consider [contributing](contributing.md)!**

[^cds]: The CubeSat Program, Cal Poly SLO, [*CubeSat Design Specification Rev. 14.1*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (9 February 2022). Source for the 100.0 × 100.0 × 113.5 mm 1U envelope, the 2 kg/U mass table covering 1U–12U, and the 30-minute deployable and 45-minute RF quiet periods.

[^rideshare-price]: SpaceX, [Rideshare Program](https://www.spacex.com/rideshare/); pricing as published for sun-synchronous Transporter missions, with a 50 kg minimum. Corroborated by NASA SSSVI, [*State of the Art in Small Spacecraft Technology*, Chapter 10](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/).

[^rideshare-freeze]: Reported July 2026 by [SatNews](https://satnews.com/2026/07/20/spacex-limits-future-commercial-rideshare-bookings-past-2028-amid-severe-manifest-saturation/) and [SpaceQ](https://spaceq.ca/spacexs-rideshare-freeze-what-it-means-for-the-smallsat-market-and-canada/), among others. SpaceX has not issued an official statement; existing contracts through 2028 are unaffected.