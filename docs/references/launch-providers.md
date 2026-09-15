# Launch Providers

Who will actually fly your CubeSat, how to reach them, and what happens after you do. This page covers the routes to orbit as organizations rather than as engineering constraints – for the requirements a launch imposes on the spacecraft, see [Qualification and Launch](../development/launch.md).

The market is unusually opaque for something this consequential. Most providers publish no price, several publish capacity figures against an orbit they do not name, and the list of who is flying changes every few months. What follows is organized by how you would actually buy: through a broker, directly from an operator, on a dedicated vehicle, or through a program that does not charge you at all.

!!! warning "Figures here go stale"

    Prices, capacities and flight status in this field move faster than any list can track. Treat every number below as a starting point for a conversation rather than a quotation – and always check which orbit a capacity figure refers to, because vendors are inconsistent about this and the sun-synchronous number is almost always the smaller one.

## How to Approach a Provider

### Making first contact

Almost every organization on this page has a web enquiry form, and that is the right way in. A cold email to a generic address usually reaches the same inbox more slowly. Brokers in particular are used to hearing from university teams and first missions, and a serious enquiry gets a serious answer even from a team that has no money yet.

What to have ready before you write, because the first reply will ask for most of it:

- **Form factor and mass.** 1U through 16U, and your current best mass estimate with its uncertainty. Say that it is an estimate.
- **Target orbit**, and how much of it is negotiable. Altitude, inclination, and whether sun-synchronous genuinely matters to the mission or is simply what you assumed.
- **Earliest and latest readiness dates.** Both. The latest one is what decides whether a given slot fits.
- **Hazards.** Batteries above the usual size, propulsion of any kind, pressurized volumes, deployables, lasers, RF power. These drive the safety review more than anything else, and a provider would much rather hear about them in the first exchange than in month nine.
- **Frequency status.** Whether coordination has started, and with whom.
- **Who you are.** University, company, agency-funded. It determines which programs and which contract forms apply to you.

Being early and vague is fine. Being late and precise is not, because the binding constraint is manifest availability: eighteen months before a target launch is a normal time to open the conversation. See [Qualification and Launch – Timeline](../development/launch.md#timeline).

### What comes back

The shape of the process is consistent across providers even where the commercial terms are not:

1. **A capacity questionnaire** or interface data sheet – a longer version of the list above, usually as a spreadsheet.
2. **A quote against one or more candidate missions**, each with its own orbit and readiness date. This is the point at which you find out whether your orbit exists on anybody's manifest.
3. **A contract**, after which you are on a manifest and the deadlines become real.
4. **An ICD and a deployer manual.** The manual governs your mechanical design from here and outranks the [CDS](glossary.md#cds) where the two disagree. See [Qualification and Launch – Interface Control Documents](../development/launch.md#interface-control-documents).
5. **A safety data package**, submitted and iterated. Inhibits and batteries attract the most scrutiny. See [Documentation checklist](../development/launch.md#documentation-checklist).
6. **A fit check**, usually in a test pod first and often in the flight deployer before delivery.
7. **Delivery**, one to six months before launch depending on the provider and the route.

<!-- NEEDS HUMAN VERIFICATION: The commercial terms of this process – deposit size, milestone payment structure, what a customer-side slip costs, and whether a booked slot can be moved to a later mission – are published by none of the providers surveyed and could not be sourced. They vary by provider and by contract. A first-hand account from someone who has signed one of these contracts would make this subsection considerably more useful than the procedural outline above. -->

### The things that catch teams out

- **The deadline is delivery, not launch.** Your whole schedule works backwards from a delivery date that can sit six months ahead of the rocket.
- **A late design change can invalidate test evidence you have already submitted**, and re-testing at that stage is expensive in both time and hardware life.
- **Export control applies to the conversation, not only to the hardware.** Sending technical data to a provider in another jurisdiction can itself require a license. See [Export control](../development/launch.md#export-control).
- **Your orbit may not be compliant.** The commonly available sun-synchronous band at 500–600 km sits above the altitude where passive decay reliably meets current disposal rules. Check before you sign rather than after. See [Space debris mitigation](../development/launch.md#space-debris-mitigation).

## Rideshare Brokers and Integrators

The normal path for a first mission. Brokers buy launch capacity in bulk, supply the [deployer](glossary.md#deployer), handle integration and much of the interface work with the launch provider, and sell you a slot. For a team that has not done this before, the broker's experience is worth as much as the slot itself – they have seen the failure modes and will tell you about yours early.

Scale gives a sense of how concentrated this is: Exolaunch alone managed 45 of the roughly 70 payloads on Transporter-14 in June 2025.[^rideshare-market]

<!-- CSR-RESOURCES:START ref-launch-providers-brokers -->
- **[Exolaunch](https://exolaunch.com/)** `Link` – German broker and the largest single integrator on SpaceX rideshare missions. Supplies the EXOpod Nova and EXOtube deployers and the CarboNIX separation system, and publishes its deployer manual openly, which makes it useful reading even if you fly with somebody else
- **[D-Orbit](https://www.dorbit.space/)** `Link` – Italian provider offering both brokerage and the ION orbital transfer vehicle, so a single contract can cover the ride and the orbit change afterwards
- **[ISILaunch](https://www.isilaunch.com/)** `Link` – Dutch broker, part of the ISISPACE group, with a long CubeSat track record and the ISIPOD and DuoPack deployers. Oriented toward European customers and university missions
- **[Alba Orbital](https://www.albaorbital.com/)** `Link` – Scottish broker specializing in PocketQubes rather than CubeSats, and effectively the only route to orbit for that form factor
- **[Maverick Space Systems](https://maverickspacesystems.com/)** `Link` – US integrator focused on non-standard form factors and custom deployment hardware, alongside the Mercury deployer series
- **[SEOPS](https://seops.space/)** `Link` – US mission integrator covering both rideshare and ISS deployment routes
- **[Voyager Technologies](https://voyagertechnologies.com/space-solutions/smallsat-microsat-deployment/)** `Link` – Brokerage on SpaceX rideshare, PSLV and other vehicles, plus ISS deployment and external payload hosting. The former Nanoracks business, and the origin of the widely referenced NRCSD deployer
- **[Precious Payload](https://preciouspayload.com/)** `Link` – A launch marketplace and mission-planning tool rather than a broker, useful for surveying what is on the manifest before committing to one provider
<!-- CSR-RESOURCES:END ref-launch-providers-brokers -->

## Rideshare Programs You Can Book Directly

Operators selling shared capacity on their own vehicles. You still need a deployer and, in practice, an integrator – booking directly does not remove that step, it only changes who you buy it from.

SpaceX is the outlier in publishing a price you can act on without a conversation: NASA's survey records Transporter rides starting at $350k for around 50 kg, at a high cadence.[^nasa-soa-launch] Transporter missions go to sun-synchronous orbit and Bandwagon missions to mid-inclination, which matters if your mission does not want a polar orbit.

Europe's equivalent is the **Small Spacecraft Mission Service** on Vega-C: a modular dispenser taking any combination from 1 kg CubeSats up to 400 kg minisatellites, whose proof-of-concept flight alone carried seven microsatellites and 46 CubeSats into sun-synchronous orbits at about 515 and 530 km. ESA owns the Vega-C program with Avio as prime contractor, and commercial exploitation of the launch system has been moving from Arianespace to Avio during 2026 – worth knowing, because it changes who you are contracting with.[^vega-ssms]

India's route is through ISRO's commercial arm, NewSpace India Limited, which has been placing customer satellites on PSLV since 1999 and sells both rideshare and dedicated missions across PSLV, SSLV, GSLV and LVM3.[^nsil]

<!-- CSR-RESOURCES:START ref-launch-providers-rideshare-programs -->
- **[SpaceX Rideshare](https://www.spacex.com/rideshare/)** `Link` – Transporter missions to sun-synchronous orbit and Bandwagon missions to mid-inclination, with published pricing and a web booking tool that quotes against a mass and a readiness date
- **[Vega-C and the Small Spacecraft Mission Service](https://www.esa.int/Enabling_Support/Space_Transportation/Vega/Vega-C)** `Link` – Europe's dedicated rideshare route, with a modular dispenser sized from 1 kg CubeSats to 400 kg minisatellites, flying from Europe's Spaceport in French Guiana
- **[NewSpace India Limited](https://www.nsilindia.co.in/launch-services)** `Link` – ISRO's commercial arm, selling rideshare and dedicated missions on PSLV, SSLV, GSLV and LVM3 from Satish Dhawan Space Centre
- **[NASA VADR](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/)** `Link` – Venture-class Acquisition of Dedicated and Rideshare, a NASA launch services contract with a Streamlined CubeSat Launch Services line alongside standard and anchor-payload rideshare. Relevant to NASA-funded missions rather than to the open market
<!-- CSR-RESOURCES:END ref-launch-providers-rideshare-programs -->

## Dedicated Small Launchers

Substantially more expensive per kilogram, and in exchange you choose the orbit and the schedule instead of accepting the primary's. For a single CubeSat this is rarely the economic choice; for a constellation, a mission with an unusual orbit, or one that cannot wait for a manifest, it can be the only one.

Read every capacity figure against the orbit it is quoted for. Rocket Lab publishes 300 kg to LEO for Electron, while Firefly publishes 1,030 kg to a 300 km LEO but 630 kg to a 500 km sun-synchronous orbit for Alpha – and the NASA survey lists both in a single column that silently mixes the two.[^launcher-performance] Electron was the most widely used small vehicle as of April 2026, with ten Electron rideshare missions completed during 2025.[^nasa-soa-launch] It also uses a tab-type dispenser rather than a rail-type pod, so the choice is not transparent to your structure.

<!-- CSR-RESOURCES:START ref-launch-providers-small-launchers -->
- **[Rocket Lab Electron](https://www.rocketlabcorp.com/launch/electron/)** `Link` – 300 kg to LEO from Māhia and Wallops, the highest-cadence small launcher currently flying. Uses the Advanced Satellite Dispenser, a tab-type design rather than a rail-type pod
- **[Firefly Alpha](https://fireflyspace.com/alpha/)** `Link` – 1,030 kg to a 300 km LEO, 630 kg to a 500 km sun-synchronous orbit
- **[ISRO SSLV](https://www.nsilindia.co.in/launch-services)** `Link` – 500 kg to a 500 km low Earth orbit, designed around launch on demand and a short turnaround. Manufacturing and marketing are being transferred to Hindustan Aeronautics Limited
- **[Isar Aerospace Spectrum](https://www.isaraerospace.com/)** `Link` – Up to 1,000 kg to LEO from Andøya in Norway, and the first European commercial launcher to reach orbit from continental Europe
- **[Rocket Factory Augsburg RFA ONE](https://www.rfa.space/)** `Link` – Targeting up to 500 kg to a 500 km sun-synchronous orbit from SaxaVord in Scotland. First flight still ahead
- **[PLD Space Miura 5](https://pldspace.com/)** `Link` – Up to 540 kg to sun-synchronous orbit from Europe's Spaceport in French Guiana, with a partially reusable first stage. In development, following the suborbital Miura 1
<!-- CSR-RESOURCES:END ref-launch-providers-small-launchers -->

!!! note "The European Launcher Challenge is reshaping this list"

    ESA awarded its first European Launcher Challenge contracts in August 2026 – €197.8 million to Isar Aerospace, €186.9 million to Rocket Factory Augsburg and €158.9 million to PLD Space, with MaiaSpace still in negotiation. Participants must reach orbit no later than 2027.[^elc-contracts] Isar met that milestone within days of signing: Spectrum lifted off from Andøya on 5 September 2026 and reached orbit on its second flight, carrying CubeSats and an experimental payload, after a first attempt in March 2025 that ended about thirty seconds after liftoff.[^isar-orbit] The same period removed an option – Orbex entered administration in February 2026 after funding talks collapsed.[^orbex] If you are planning a European launch more than a year out, check the current status of anybody on this list before building a schedule around them.

## Orbital Transfer Vehicles

A tug that takes you from the rideshare drop-off orbit to something closer to what the mission actually wanted. Increasingly relevant because the common sun-synchronous drop-off at 500–600 km sits above the altitude where passive deorbit reliably closes within five years. D-Orbit's ION is the most operationally proven of them, first flown in 2020 and flown 21 times as of December 2025.[^nasa-soa-launch]

<!-- CSR-RESOURCES:START ref-launch-providers-orbital-transfer -->
- **[D-Orbit ION](https://www.dorbit.space/)** `Link` – The most flown orbital transfer vehicle in the small satellite market, carrying CubeSats from the rideshare drop-off to a chosen altitude and phasing
- **[Impulse Space](https://www.impulsespace.com/)** `Link` – Mira, a high-delta-v transfer vehicle for orbit changes beyond what a conventional tug offers
- **[Momentus](https://momentus.space/)** `Link` – Vigoride transfer vehicle and hosted payload services
- **[Rocket Lab Photon](https://www.rocketlabcorp.com/)** `Link` – Spacecraft platform usable as a transfer stage, generally in combination with an Electron launch
<!-- CSR-RESOURCES:END ref-launch-providers-orbital-transfer -->

## ISS Deployment

Deployment from the International Space Station rather than directly from a launch vehicle. The trade is specific: the launch environment is gentler, some interface requirements are easier, and the safety requirements are the strictest of any route because the spacecraft spends time inside a crewed vehicle. The orbit is not negotiable – 51.6° inclination at 400–420 km, deployed one to three months after berthing[^nasa-soa-launch] – which gives a short natural lifetime, convenient for debris compliance and inconvenient for a long mission.

The Japanese route is the most open to outside teams. JAXA's J-SSOD deploys 1U to 6U CubeSats through the Kibo module's airlock and robotic arm, and the reusable J-SSOD-R introduced in March 2021 carries up to 24U per deployment at 6U per deployer. JAXA names the lower launch vibration environment as the main advantage over direct deployment. Since 2018 the commercial slots have been sold not by JAXA but by two selected service providers, Space BD and Mitsui Bussan Aerospace – so for a paying customer, those are the addresses.[^jssod]

<!-- CSR-RESOURCES:START ref-launch-providers-iss-deployment -->
- **[JAXA J-SSOD](https://humans-in-space.jaxa.jp/en/biz-lab/experiment/facility/ef/jssod/)** `Link` – The deployer itself, with its interface requirements and accommodation: 1U through 6U, deployed from the Kibo airlock by the station's robotic arm. Read this before approaching a service provider
- **[Space BD](https://space-bd.com/en/)** `Link` – One of two commercial J-SSOD service providers selected by JAXA, and a common route to a Kibo deployment slot for a non-Japanese customer
- **[Mitsui Bussan Aerospace](https://www.mbac.co.jp/en/)** `Link` – The other JAXA-selected commercial J-SSOD service provider
- **[Voyager Technologies – ISS deployment](https://voyagertechnologies.com/space-solutions/smallsat-microsat-deployment/)** `Link` – NRCSD deployment from the US segment, plus external hosted payload sites on the Bishop Airlock and the NREP platform for experiments that do not need to be free-flying satellites
<!-- CSR-RESOURCES:END ref-launch-providers-iss-deployment -->

## Free and Subsidized Programs

Competitive, slow, and free. The application cycles are annual or less frequent, so these belong in your planning a long way ahead of anything else on this page – and an unsuccessful application is not wasted, because the proposal is most of a mission concept review. KiboCUBE, run by UNOOSA with JAXA, is aimed specifically at institutions in countries without an established satellite capability; its sixth-round awardee, from Mexico, was deployed from Kibo in February 2026.[^kibocube]

<!-- CSR-RESOURCES:START ref-launch-providers-sponsored -->
- **[NASA CubeSat Launch Initiative](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative)** `Link` – Launch opportunities for US educational institutions, non-profits and NASA centers, selected through a recurring announcement of opportunity
- **[ESA Fly Your Satellite!](https://www.esa.int/Education/Educational_Satellites)** `Link` – Support, test facilities, review cycles and launch opportunities for European university teams. The educational structure around it is worth as much as the launch
- **[UNOOSA/JAXA KiboCUBE](https://www.unoosa.org/oosa/en/ourwork/access2space4all/KiboCUBE/KiboCUBE_Index.html)** `Link` – Deployment from Kibo for institutions in countries without an established satellite capability, run in annual rounds
- **[JAXA J-CUBE](https://humans-in-space.jaxa.jp/en/biz-lab/experiment/facility/ef/jssod/)** `Link` – Kibo deployment opportunities established through an agreement between JAXA and the University Space Engineering Consortium (UNISEC)
<!-- CSR-RESOURCES:END ref-launch-providers-sponsored -->

---

Know a launch provider that belongs here? Please [contribute](../contributing.md).

[^nasa-soa-launch]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 10: Integration, Launch, Deployment, and Orbital Transport](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/) (revision dated 18 May 2026). Open access. Source for Transporter rides starting at $350k for roughly 50 kg at a high cadence, Electron being the most widely used small vehicle as of April 2026 with ten Electron rideshare missions in 2025, the NASA VADR contract structure including its Streamlined CubeSat Launch Services line, D-Orbit ION first flying in 2020 and flown 21 times as of December 2025, and ISS deployment at 51.6° inclination into a 400–420 km orbit one to three months after berthing.

[^launcher-performance]: Manufacturer-published performance: Rocket Lab, [*Electron*](https://www.rocketlabcorp.com/launch/electron/), states 300 kg to LEO; Firefly Aerospace, [*Alpha*](https://fireflyspace.com/alpha/), states 1,030 kg to a 300 km LEO and 630 kg to a 500 km SSO. The NASA survey lists both vehicles in a single "performance to LEO" column, which for Alpha is actually its sun-synchronous figure. Always confirm the orbit a quoted capacity refers to.

[^vega-ssms]: European Space Agency, [*Vega-C*](https://www.esa.int/Enabling_Support/Space_Transportation/Vega/Vega-C). Open access. The Small Spacecraft Mission Service dispenser accommodates any combination from 1 kg CubeSats up to 400 kg minisatellites. ESA owns the Vega-C program with Avio as prime contractor and design authority; Arianespace was responsible for commercial exploitation of the launch system until 2026, when Avio began taking it over. The SSMS proof-of-concept flight is described in ESA's [return-to-flight release](https://www.esa.int/Enabling_Support/Space_Transportation/Vega/Vega_return_to_flight_proves_new_rideshare_service), which records seven microsatellites of 15–150 kg and 46 CubeSats released into sun-synchronous orbits at about 515 km and 530 km.

[^nsil]: NewSpace India Limited, [*Launch services (SSLV, PSLV, GSLV-Mk-II and LVM-3)*](https://www.nsilindia.co.in/launch-services). Open access. NSIL is ISRO's commercial arm and has provided launch services for customer satellites on PSLV since 1999, offering both rideshare and dedicated missions from Satish Dhawan Space Centre, with SSLV specified at 500 kg to a 500 km low Earth orbit. Note that the page's date for the 104-satellite PSLV record flight is wrong – it was PSLV-C37 in February 2017 – so treat its historical detail with care.

[^isar-orbit]: European Space Agency, [*Isar Aerospace Achieves First Launch to Orbit from Continental Europe*](https://www.esa.int/Enabling_Support/Space_Transportation/First_contracts_kick_off_European_Launcher_Challenge). Open access. Spectrum lifted off from Andøya Spaceport on 5 September 2026 and reached orbit on its second flight, carrying CubeSats and an experimental payload selected through the German Space Agency's Microlauncher Competition. Isar Aerospace became the first commercial company from Europe to deliver satellites into orbit with its own launcher, and the first European Launcher Challenge participant to meet the orbital milestone. The first flight, in March 2025, ended around thirty seconds after liftoff.

[^elc-contracts]: European Space Agency, [*First contracts kick off European Launcher Challenge*](https://www.esa.int/Enabling_Support/Space_Transportation/First_contracts_kick_off_European_Launcher_Challenge), August 2026. Open access. Isar Aerospace €197.8 million, Rocket Factory Augsburg €186.9 million and PLD Space €158.9 million, with the MaiaSpace contract still in negotiation. Gives Spectrum at up to 1,000 kg to low Earth orbit from Andøya, RFA ONE flying from SaxaVord, and Miura 5 at up to 540 kg to sun-synchronous orbit from Europe's Spaceport. Participants are required to achieve an orbital launch no later than 2027.

[^orbex]: NASASpaceflight, ["ESA awards first European Launcher Challenge contracts"](https://www.nasaspaceflight.com/2026/08/esa-european-launcher-challenge-contracts/), August 2026. Free. Reports that Orbex, one of the original five European Launcher Challenge finalists, entered administration in February 2026 after fundraising and acquisition talks collapsed, received no contract, and that assets tied to its planned Sutherland spaceport have since been sold. Trade press rather than a primary source; the company's own position has not been checked.

[^jssod]: Japan Aerospace Exploration Agency, [*JEM Small Satellite Orbital Deployer (J-SSOD)*](https://humans-in-space.jaxa.jp/en/biz-lab/experiment/facility/ef/jssod/). Open access. Covers the 1U–6U accommodation, the reusable J-SSOD-R introduced in March 2021 with a maximum 24U capability at 6U per deployer, the airlock and robotic-arm deployment sequence, the lower launch vibration environment compared with direct deployment, and JAXA's May 2018 selection of Space BD Inc. and Mitsui Bussan Aerospace Co., Ltd. as commercial J-SSOD service providers. The J-CUBE program is described there as a deployment opportunity established between JAXA and UNISEC.

[^kibocube]: United Nations Office for Outer Space Affairs, [*KiboCUBE*](https://www.unoosa.org/oosa/en/ourwork/access2space4all/KiboCUBE/KiboCUBE_Index.html). Open access. A UNOOSA program run with JAXA, providing ISS deployment opportunities to institutions in countries without an established satellite capability. A CubeSat from Universidad Popular Autónoma del Estado de Puebla, Mexico, selected in the sixth round, was deployed from the ISS on 3 February 2026.

[^rideshare-market]: New Space Economy, ["Satellite Ridesharing Market Analysis 2026"](https://newspaceeconomy.ca/2026/02/27/satellite-ridesharing-market-analysis-2026/), February 2026. Free. Records Exolaunch managing 45 of the roughly 70 payloads on Transporter-14 in June 2025, and traces Transporter pricing from $5,000/kg with a 150 kg minimum in 2019 through a 50 kg minimum at $275,000 in October 2022 to $350,000 for 50 kg from Transporter-16 onward. Trade press rather than a primary source; the pricing figures agree with NASA's survey at the 50 kg entry point but the marginal per-kilogram rate is not independently confirmed.
