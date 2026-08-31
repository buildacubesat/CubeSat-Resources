# Getting Started

CubeSats are satellites in the nanosat class built around a published standard, the CubeSat Design Specification (CDS). Standardised form factors share common deployer hardware, which lowers the cost of development and launch and makes access to space attainable for small teams, universities and even individuals.

This page is for those new to CubeSats or small satellite development. It gives you a broad overview of what a CubeSat is, how a project runs, which constraints decide your design before you start drawing, and where to go next.

## The Standard in Numbers

The current revision is [CDS Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (February 2022), maintained by the Cal Poly CubeSat Laboratory. It covers 1U, 1.5U, 2U, 3U, 6U and 12U in a single document.

- A 1U is nominally a 10 cm cube. The actual envelope is **100 × 100 × 113.5 mm** – the extra height is the rails, and designing to a flat 100 mm is a common first mistake.
- Mass is **2 kg per U** in Rev. 14.1: 2 / 3 / 4 / 6 / 12 / 24 kg for 1U / 1.5U / 2U / 3U / 6U / 12U. Older material still quotes the Rev. 13 figure of 1.33 kg per U.
- Deployables stay stowed for the first 30 minutes after deployment, and the radio stays silent for the first 45 minutes.

!!! warning "Your launch provider outranks the CDS"
    The CDS is the baseline, not the contract. Deployer capabilities, mass limits, inhibit counts, materials and outgassing rules all vary between providers, and the payload user guide you sign against always takes precedence. Get that document early and design to it.

See [Standards & Protocols](references/standards.md) for the specification itself and the testing standards that go with it.

## Where to Start

### Read first

- [NASA's CubeSat 101](https://www.nasa.gov/wp-content/uploads/2017/03/nasa_csli_cubesat_101_508.pdf) – beginner-friendly overview of CubeSat design and mission planning, and the single best starting point. Written by Cal Poly for NASA.
- [NASA CubeSat Launch Initiative Resources](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative/cubesat-launch-initiative-resources/) – a curated list of documents covering nearly everything a new project needs.
- [The CubeSat Design Specification](https://www.cubesat.org/cubesatinfo) – the official framework for CubeSat form factors, and the source of the physical and operational constraints on your mission.
- [Nano Avionics' CubeSat 101](https://nanoavionics.com/blog/cubesat-101-the-comprehensive-guide-to-understanding-satellite-technology) – a shorter, higher-level overview if the NASA document is too much at once.
- [Wikipedia](https://en.wikipedia.org/wiki/CubeSat) – history and context.
- [The case for open source in CubeSat development](https://visionspace.com/how-to-build-a-cubesat-and-use-open-source-101/) – summary of an interview with Artur Scholz of LibreCube.

### Courses and training

- [New Space Economy](https://www.edx.org/learn/economics/ecole-polytechnique-federale-de-lausanne-new-space-economy) – EPFL on edX, a good general introduction to the commercial space sector.
- [ESA Academy](https://www.esa.int/Education/ESA_Academy) – CubeSat Hands-On Training Weeks and Concurrent Engineering Workshops for students in ESA member states.
- More options on the [Courses](references/courses.md) page.

### Stay current

- A few well-chosen [newsletters](references/newsletters.md) will keep you up to date with the industry at large.
- Shameless plug: I am developing an open source CubeSat and documenting the process. If that is useful to you, see the [Build a CubeSat channel](https://youtube.com/@buildacubesat), the [website](https://buildacubesat.space/) and the [source on Codeberg](https://codeberg.org/buildacubesat-project).

## Development Flow

CubeSat projects usually fall into one of two categories, and knowing which one you are in shapes almost every decision that follows.

**Result-oriented missions** have a payload that needs to reach orbit and return data. Here it is usually advisable to source a bus with flight heritage – structure and subsystems that have flown before – from an established vendor, and spend your effort on the payload and the ground segment.

**Process-oriented missions** treat the learning as the point. You will build a larger share of the flight segment yourself. This is absolutely feasible, but it is more iterative and shifts effort into integration, qualification and testing. Expect to build a FlatSat or engineering model first – all subsystems laid out on a bench – for easier debugging and early verification.

Most academic missions land in between: source the parts where failure is expensive and schedule-critical (typically structure and EPS), build the rest in-house.

### Project Phases

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
- [ ] Preliminary Design Review (PDR) completed
- [ ] Critical Design Review (CDR) completed
- [ ] Frequency coordination and licence applications submitted
- [ ] Export control classification established
- [ ] End-of-life and debris mitigation plan documented
- [ ] Flight/qualification hardware procured
- [ ] Flight/qualification hardware tested
- [ ] FlatSat testing completed
- [ ] Functional tests performed at system level
- [ ] Environmental tests performed at system level
- [ ] Launch service provider selected and contract signed
- [ ] Interface Control Document agreed with the launch provider
- [ ] Ground station operational and tracking test satellites
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

These four decisions are cheap to make at the start and expensive to revisit. Teams that get into trouble usually got into it here.

**Orbit and disposal.** Your altitude decides your lifetime, and your lifetime is now a regulatory matter. Anything licensed through or accessing the market via the United States falls under the FCC's five-year post-mission disposal rule, and the FCC's streamlined small satellite licence caps in-orbit lifetime at six years. Below roughly 450 km a passive 1U typically re-enters within a couple of years; at 550 km and above natural decay can take a decade or more. Model it properly with a decay tool such as ESA's DRAMA before you commit to an orbit.

**Spectrum.** Amateur or commercial – see below. This is not just a radio decision: the amateur satellite service prohibits commercial use of the link, so choosing amateur bands constrains your business model as well as your hardware.

**Export control.** If your team includes non-nationals, or you ship hardware across a border, or you buy US-origin components, export control applies to you. See below.

**Launch safety.** Inhibits, deployment switches, remove-before-flight pin and battery qualification (lithium cells generally need UN 38.3 transport testing) are structural design drivers, not paperwork you add at the end. The [Inhibits and HDRM](development/inhibits-hdrm.md) page covers the details.

## Sourcing and Building

For sourcing subsystems and components, start with [SatSearch](https://satsearch.co/), [SatCatalog](https://www.satcatalog.com/) (rebranding to SatBase) and the [CubeSat Shop](https://www.cubesatshop.com/).

On the open-source side, a considerable amount of flight-relevant work is freely available:

- [LibreCube](https://librecube.gitlab.io/) – open standards and building blocks for space systems, including SpaceCAN.
- [F Prime](https://github.com/nasa/fprime) – NASA JPL's flight software framework, flown on Ingenuity and a growing number of CubeSats.
- [NASA cFS](https://github.com/nasa/cFS) – the core Flight System, a mature flight software platform.
- [PyCubed](https://github.com/pycubed) – open-source, radiation-tested CubeSat avionics programmable entirely in Python.
- [libcsp](https://libcsp.github.io/libcsp/) – the de facto CubeSat onboard networking protocol.
- [SatNOGS](https://satnogs.org/) – open-source global ground station network, run by the Libre Space Foundation.

See [Flight Software](development/flight-software.md), [Ground Segment](development/ground-segment.md) and [Tools and Helpers](development/tools.md) for more.

## Getting to Orbit

Start looking for a ride early. It aligns you with your provider's requirements, avoids costly redesigns, and gives you access to their support and documentation while there is still time to use it.

Common paths:

- **Rideshare on a dedicated smallsat mission.** [SpaceX Transporter and Bandwagon](https://www.spacex.com/rideshare) missions are the highest-volume option, usually booked through a launch services provider such as [Exolaunch](https://exolaunch.com/), [D-Orbit](https://www.dorbit.space/) or [ISILAUNCH](https://www.isilaunch.com/).
- **Dedicated small launchers.** [Rocket Lab](https://www.rocketlabusa.com/) and others sell dedicated or shared missions with more control over your orbit, at a higher price.
- **Deployment from the ISS.** Via JAXA's J-SSOD or commercial providers. The orbit is low, so lifetime is short and disposal compliance is easy, but you inherit crewed-vehicle safety requirements.
- **Education and access programmes.** [NASA CSLI](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative) for US educational and non-profit developers, [ESA Fly Your Satellite!](https://www.esa.int/Education/Educational_Satellites) for teams in ESA member states, and [UNOOSA Access to Space for All](https://www.unoosa.org/oosa/en/ourwork/access2space4all/index.html) for developing countries.

As a budget anchor: SpaceX's published rideshare rate to SSO is around USD 350,000 for up to 50 kg with roughly USD 7,000 per kilogram above that, as of early 2026. There is a 50 kg minimum, which is why a lone 1U is expensive per kilogram and why aggregators exist. Check current pricing directly – it has risen repeatedly.

!!! note "Once you are manifested"
    Launch integration begins. You will need to meet every interface and safety requirement in the payload user guide and deliver flight hardware well in advance – anywhere from 1 to 6 months before liftoff. If your CubeSat is not ready, it does not fly.

More detail on the [Qualification and Launch](development/launch.md) page.

## Regulatory Approval

What applies to you depends on where your team is based, where your launch provider is based, and what you intend to do in orbit.

!!! warning
    Nothing on this site is legal advice. You will need to familiarise yourself with your own country's legislation, rules and best practices around launching and operating a satellite.

### Radio Frequency Usage

The most common CubeSat link is UHF in the 435–438 MHz amateur satellite allocation. There are two distinct routes, and the first decision is which one you are on:

**Amateur satellite service.** A licensed radio amateur on your team takes responsibility for the station and its compliance. The link may not be used for commercial purposes. You request frequency coordination from the [IARU](https://www.iaru.org/reference/satellites/) through your national member society, using their coordination request form. IARU coordination is a peer process, not a licence.

**Commercial or experimental service.** You apply to your national regulator for a spectrum authorisation – in the United States, the [FCC's streamlined small satellite process](https://www.fcc.gov/space/small-satellite-and-small-spacecraft-licensing-process) under 47 CFR § 25.122, which covers up to ten satellites of no more than 180 kg each, with a maximum six-year in-orbit lifetime and deployment below 600 km or a collision avoidance capability.

In both cases, the international filing with the [ITU](https://www.itu.int/en/ITU-R/space/support/smallsat/Pages/default.aspx) – advance publication information, then coordination and notification – is submitted **by your national administration**, not by you and not by the IARU. Budget months, not weeks, and start before your radio design is frozen. If required approvals are not in place by launch day, your CubeSat will not be allowed to deploy.

### Deorbit and Debris Mitigation

You will be asked to show that your satellite comes down and that it does not fragment. That means a documented end-of-life plan, passivation of batteries and any stored energy at end of mission, and a re-entry casualty risk assessment. The FCC's five-year rule is currently the strictest widely applicable requirement; ESA's Zero Debris approach and ISO 24113 point in the same direction.

### Export Control

Space hardware is controlled hardware. In the United States that means ITAR and the EAR – Munitions List Categories IV and XV and the corresponding Commerce Control List entries were substantially revised in October 2024, adding the CSA licence exception. The EU and Switzerland have their own dual-use regimes. Practical triggers for a small team: non-national team members with access to technical data, shipping hardware abroad for testing or integration, and buying US-origin parts. Establish your classification before you publish designs or hand hardware to a foreign integrator.

### National Authorisation and Registration

Under the Outer Space Treaty a state is responsible for, and liable for, the space activities of its nationals, and under the Registration Convention the launching state registers the object. In practice you need a national authorisation and your satellite must be entered in a national registry, which is forwarded to the UN. Some countries have a well-defined licensing regime; others, Switzerland among them, have no national space law yet, and teams there typically route authorisation via another state, often through the launch provider. Find out which situation you are in early – it can determine which provider you can fly with.

### Remote Sensing

If you plan Earth observation with cameras or sensors, you may need a separate remote sensing licence from a national body – for example [NOAA CRSRA](https://space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/licensing/), administered under the US Office of Space Commerce.

## Mission Operations

Once deployed, you begin commissioning: acquiring the signal, establishing two-way contact, and checking that each subsystem is alive and behaving. Only then does the mission enter its operational phase – collecting data, sending commands, and managing the satellite's health.

Plan time, money and people for this. Missions run from a few months to several years, and operations require someone available to take passes, including at inconvenient hours during commissioning. Getting your satellite into the [SatNOGS](https://satnogs.org/) database before launch is one of the cheapest things you can do for your mission: it gives you a global network of receivers listening for your first beacon.

## Budget Expectations

Rough orders of magnitude, excluding labour:

| Type | Typical range |
| :---- | :---- |
| Academic 1U–3U, largely in-house, sponsored or donated launch | tens of thousands |
| Academic or small-commercial 3U–6U, sourced bus, purchased rideshare | low hundreds of thousands to ~1 million |
| Commercial 6U–12U with a capable payload and full qualification | several million |

Launch, environmental testing and licensing are the line items teams most often underestimate.

## Communities and Next Steps

- [Development](development/index.md) – the technical content of this site, by subsystem.
- [References](references/index.md) – glossary, standards, books, papers, missions and courses.
- [Build a CubeSat Discord](https://bac.page/discord) – community focused on open-source hardware and software in CubeSat development.
- [Libre Space Community](https://community.libre.space/) – the most technically substantive open forum in this space.
- [r/CubeSats](https://www.reddit.com/r/CubeSats/) – active Reddit community.
- [AMSAT](https://www.amsat.org/) and its national counterparts – decades of amateur satellite engineering experience.
- More on the [Communities](references/communities.md) page.

The CubeSat and amateur satellite communities are unusually willing to help. A well-posed question with real data attached almost always gets a useful answer.