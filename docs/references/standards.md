# Standards & Protocols

The standards, specifications and protocols a CubeSat is designed and tested against: the CubeSat Design Specification and the deployer manuals that outrank it, environmental and materials standards, CCSDS and ECSS protocols, and the regulatory documents.

A practical note: some of these are free, some are paywalled, and the ones that matter most to a CubeSat team – the CDS, GEVS, the ECSS testing standard and the CCSDS Blue Books – are all freely available. Remember that whatever these say, **your launch provider's payload user guide takes precedence**.

## CubeSat specifications

<!-- CSR-RESOURCES:START ref-standards-cubesat-specs -->
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – Cal Poly SLO. The baseline CubeSat specification: envelope and rail geometry, mass and center-of-mass limits, materials and anodizing, deployment switches, inhibits, and the 30-minute deployable and 45-minute RF quiet periods. Free
- **[CubeSat Design Specification Rev. 13](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/56e9b62337013b6c063a655a/1458157095454/cds_rev13_final2.pdf)** `PDF` – The previous revision, still worth knowing because much older material (and some deployer documentation) quotes its figures, notably the 1.33 kg/U mass limit
- **[ISO 17981:2024 – Space systems: Cube satellite (CubeSat) interface](https://www.iso.org/standard/85136.html)** `Link` – International standard for CubeSat internal interfaces – component to component, platform to payload, umbilical connectors and commercial product datasheets. It explicitly does not cover the CubeSat-to-deployer interface, which stays with the CDS. Paywalled
- **[Cal Poly CubeSat Program](https://www.cubesat.org/)** `Link` – The source for current CDS revisions and CubeSat program documentation
<!-- CSR-RESOURCES:END ref-standards-cubesat-specs -->

## Workmanship

The standards that define what a soldered joint, a crimp or a conformal coat has to look like to be accepted on flight hardware. NASA maintained its own soldering standards until 2011, then adopted the space applications addendum to IPC J-STD-001 across all programs and published NASA-STD-8739.6 to cover implementation. The NASA documents are free and the IPC ones are not, which makes the cancelled NASA standards the most accessible statement of the criteria even though they no longer govern anything.

There were two of them, and the split matters: **NASA-STD-8739.3 covers through-hole and wire and cable terminations, NASA-STD-8739.2 covers surface mount**. Both were cancelled together on 17 October 2011 when NASA adopted the IPC space addendum.[^nasa-workmanship] Since most CubeSat boards are predominantly surface mount, 8739.3 alone will not tell you what a good joint looks like on the hardware you are actually building.

One trap worth knowing before you specify anything to a contract assembler: **J-STD-001 Class 3 is not the space class**. NASA-STD-8739.6B states outright that Class 3 is not an authorized substitute for the space addendum, and the same goes for cable and harness work – IPC/WHMA-A-620 Class 3 is not a substitute for its own space addendum.[^nasa-workmanship] Class 3 is high-reliability electronics; the space addendum adds what survives launch vibration and orbital thermal cycling on top of it.

A CubeSat flying as a secondary payload is rarely held to either. Read them anyway: they are specific about wetting, fillet shape and disturbed joints in a way no tutorial is, and they are what an inspector at a partner organization will be applying. Technique itself is covered on [Tools – Soldering and rework](../development/tools.md#soldering-and-rework).

<!-- CSR-RESOURCES:START ref-standards-workmanship -->
- **[NASA-STD-8739.2, Workmanship Standard for Surface Mount Technology](https://standards.nasa.gov/standard/NASA/NASA-STD-87392)** `Link` – The surface mount half of NASA's former soldering pair, covering hand and machine soldering of surface mount connections. The one to read for a CubeSat board, most of which are surface mount. Cancelled 17 October 2011, cleared for public access. Free
- **[NASA-STD-8739.3, Soldered Electrical Connections](https://standards.nasa.gov/standard/NASA/NASA-STD-87393)** `Link` – The through-hole half: hand and wave soldering of discrete wire and cable terminations and through-hole assemblies. Does not cover surface mount, which is 8739.2. Cancelled 17 October 2011 in favor of the IPC space addendum and superseded for any contract citing it, but still the most readable free statement of hand-soldering acceptance criteria. Free
- **[NASA-STD-8739.6B, Implementation Requirements for NASA Approved Workmanship Standards](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/nasa-std-87396b.pdf)** `PDF` – The document that ties the others together, and the most useful of them for a small team. Names which standard applies to what, then gives concrete numbers: ESD work surface and wrist strap resistances, soldering iron tip-to-ground limit, relative humidity bands, solvent rules, inspection and rework requirements. Approved 2021. Free PDF
- **[IPC J-STD-001JS, Space and Military Applications Electronic Hardware Addendum](https://webstore.ansi.org/standards/ipc/ipcstd001js2025)** `Link` – The document that actually governs soldering. Supplements or replaces identified requirements of the base J-STD-001 for hardware that has to survive launch vibration and orbital thermal cycling, including permitted solder alloys and a red plague control plan for silver-coated copper conductors. Paywalled
- **[IPC-A-610J, Acceptability of Electronic Assemblies](https://webstore.ansi.org/standards/ipc/ipc610j2024)** `Link` – The acceptability counterpart, and the one with the photographs. J-STD-001 tells you the process; IPC-A-610 shows you what the result should look like, across three product classes, with criteria for handling and mechanical workmanship that sit outside J-STD-001's scope. Paywalled
<!-- CSR-RESOURCES:END ref-standards-workmanship -->

## Deployer manuals and payload user guides

Whatever the CDS says, the document that governs a CubeSat's mechanical and safety design is the deployer manual or payload user guide of the provider it flies with. Four are openly published and make good worked examples of the class. Read at least one before freezing a structure, and note that a manual can be more permissive as well as more restrictive: the XCD guides allow 6.50 kg in a 3U and 13.00 kg in a 6U, above the 2 kg per U the [CDS](glossary.md#cds) specifies.[^xcd-guide]

<!-- CSR-RESOURCES:START ref-standards-deployer-manuals -->
- **[Exolaunch EXOpod Nova User Manual, Rev. 1.2](https://exolaunch.com/documents/EXOpod_Nova_User_Manual_June_2024.pdf)** `PDF` – Deployer manual covering 1U–16U, with mass and center-of-mass allowances, rail dimensions and protrusion limits; states that where it conflicts with the CDS, the manual takes priority. Free PDF
- **[NanoRacks CubeSat Deployer (NRCSD) Interface Definition Document](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf)** `PDF` – ISS deployer interface document, and a worked example of a provider layering its own inhibit and timer requirements on top of the CDS. Free PDF
- **[XTERRA XCD-3U/6U Hybrid User's Guide, Rev. 1.3.3](https://www.xterra.space/_files/ugd/e66575_0a86422b84984e24be0a5bcb6030cd92.pdf)** `PDF` – The most detailed openly published CubeSat dispenser manual of the three: per-format mass and length allowances, rail and access panel requirements, center-of-gravity offset limits by axis, activation switch placement and minimum travel, preload approach, deployment velocity against payload mass, tip-off, and the electrical interface. Carries a full revision history back to January 2023. Free PDF
- **[XTERRA XCD-12U/16U Hybrid User's Guide, Rev. 1.2.2](https://www.xterra.space/_files/ugd/e66575_eb1c86f8b441485e8cb994fcd05d640c.pdf)** `PDF` – The same document family for the larger form factors, covering satellites from 227 mm to 454 mm in length. Free PDF
<!-- CSR-RESOURCES:END ref-standards-deployer-manuals -->

## Testing and environmental verification

<!-- CSR-RESOURCES:START ref-standards-testing -->
- **[ECSS-E-ST-10-03C Rev.1 – Space engineering: Testing](https://ecss.nl/wp-content/uploads/2022/05/ECSS-E-ST-10-03-Rev.1(31May2022).pdf)** `PDF` – Defines qualification, acceptance and protoflight approaches, environmental test types and the test sequence. Free PDF
- **[NASA GEVS (GSFC-STD-7000)](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000)** `Link` – General Environmental Verification Standard. The default environmental envelope for CubeSat campaigns without a specific launcher manifest; source of the widely quoted 14.1 Grms qualification level
- **[ISO 19683:2026 – Design qualification and acceptance tests of small spacecraft and units](https://www.iso.org/standard/86540.html)** `Link` – International standard specifically covering small spacecraft qualification and acceptance testing. Paywalled
- **[NASA Goddard Outgassing Database](https://etd.gsfc.nasa.gov/capabilities/outgassing-database/)** `Link` – ASTM E595 total mass loss and collected volatile condensable material data for thousands of materials. The first place to check before selecting an adhesive, tape or printed part
<!-- CSR-RESOURCES:END ref-standards-testing -->

## Communication protocols and data formats

<!-- CSR-RESOURCES:START ref-standards-communication -->
- **[CCSDS Blue Books](https://ccsds.org/publications/bluebooks/)** `Link` – The full set of freely available recommended standards for space data systems
- **[TM Space Data Link Protocol (CCSDS 132.0-B)](https://ccsds.org/Pubs/132x0b3.pdf)** `PDF` – Telemetry space data link protocol
- **[TC Space Data Link Protocol (CCSDS 232.0-B)](https://ccsds.org/Pubs/232x0b4e1c1.pdf)** `PDF` – Telecommand space data link protocol
- **[CCSDS 123.0-B-2 – Low-Complexity Lossless and Near-Lossless Multispectral and Hyperspectral Image Compression](https://ccsds.org/Pubs/123x0b2e2c3.pdf)** `PDF` – Image compression standard designed for the exact problem CubeSat imaging payloads face
- **[ECSS-E-ST-70-41C – Telemetry and telecommand packet utilization (PUS)](https://ecss.nl/standard/ecss-e-st-70-41c-rev-1-dir1-telecommand-and-telemetry-packet-utilization-review-12-december-2024-28-february-2025/)** `Link` – The European service-based standard for spacecraft telemetry and telecommand
- **[Cubesat Space Protocol (libcsp)](https://libcsp.github.io/libcsp/)** `Link` – The de facto CubeSat onboard networking protocol. Open source (MIT)
- **[SpaceCAN (LibreCube)](https://librecube.gitlab.io/standards/spacecan/)** `Link` – Simplified redundant CAN bus standard for small spacecraft, derived from ECSS-E-ST-50-15C
<!-- CSR-RESOURCES:END ref-standards-communication -->

## Systems engineering and project standards

<!-- CSR-RESOURCES:START ref-standards-systems-engineering -->
- **[NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2)](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)** `PDF` – Requirements, verification and validation, and the Pre-Phase A to Phase F life cycle. Free
- **[ECSS standards](https://ecss.nl/)** `Link` – The European Cooperation for Space Standardization's full standard set, covering engineering, product assurance and management. Many are freely downloadable
- **[ECSS-E-ST-70-11C Rev.1 – Space segment operability](https://ecss.nl/standard/ecss-e-st-70-11c-rev-1-space-segment-operability-15-october-2025/)** `Link` – Requirements for the onboard functions an unmanned spacecraft needs in order to be operable in flight, covering nominal and predefined contingency situations. The standard behind much of what modes, safe mode and FDIR design assumes. Free, registration required
- **[NASA Technical Standards](https://standards.nasa.gov/)** `Link` – Searchable index of NASA's technical standards
<!-- CSR-RESOURCES:END ref-standards-systems-engineering -->

## Regulatory and spectrum

<!-- CSR-RESOURCES:START ref-standards-regulatory -->
- **[ITU Small Satellites Support](https://www.itu.int/en/ITU-R/space/support/smallsat/Pages/default.aspx)** `Link` – ITU guidance on small satellite spectrum and filing matters
- **[IARU Amateur Satellite Frequency Coordination](https://www.iaru.org/on-the-air/satellites/)** `Link` – The coordination process for amateur-band satellite frequencies
- **[FCC 5-Year Rule for Deorbiting Satellites](https://www.fcc.gov/document/fcc-adopts-new-5-year-rule-deorbiting-satellites-0)** `Link` – FCC Report and Order requiring LEO satellite disposal within five years of mission completion
<!-- CSR-RESOURCES:END ref-standards-regulatory -->

---

Know a standard that belongs here? Please [contribute](../contributing.md).

[^nasa-workmanship]: NASA Office of Safety and Mission Assurance, [*NASA-STD-8739.6B, Implementation Requirements for NASA Approved Workmanship Standards*](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/nasa-std-87396b.pdf), approved 4 February 2021. Free PDF. Section 9.1 names IPC J-STD-001GS as the baseline soldering standard for mission hardware and notes that IPC J-STD-001 Class 3 is not an authorized substitute; Section 10.1.2 makes the equivalent point for IPC/WHMA-A-620C Class 3. Section 9.3 records that NASA-STD-8739.2 and 8739.3 were cancelled in October 2011 and may be used without waiver only by programs whose assurance baseline predates that; NASA's adoption of IPC J-STD-001ES took effect on 17 October 2011, the same date. 8739.2 covered surface mount and 8739.3 covered through-hole and wire and cable terminations, which is why both were needed and both were replaced at once. Table 1 lists the full set of workmanship documents. Note that 8739.6B implements the G revision of the IPC documents while later revisions have since been published.

[^xcd-guide]: XTERRA, *XCD-3U/6U Hybrid User's Guide*, document XTD-100084 Revision 1.3.3, 21 January 2026. Free PDF. Section 4.1 gives maximum satellite masses of 2.17 kg for 1U, 6.50 kg for 3U and 13.00 kg for 6U, against maximum lengths of 113.5 mm, 227 mm and 366 mm rail end to rail end – roughly 2.17 kg per U, above the 2 kg per U of CDS 14.1. Section 4.4 gives center-of-gravity offset limits of ±20 mm on all axes for 1U, ±20/±20/±70 mm for 3U and ±20/±45/±70 mm for 6U. Section 4.5 asks for at least 0.75 mm of activation travel on Z-axis switches and at least 1.5 mm on X or Y axis switches. Section 5.1 gives empty dispenser masses of 7.25 kg in the 3U configuration and 6.50 kg in the 6U. Section 5.11 gives deployment velocities of roughly 0.8–1.15 m/s depending on payload mass, with tip-off typically at or below 5 deg/s.
