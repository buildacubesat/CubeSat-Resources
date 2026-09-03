# Standards & Protocols

The standards, specifications and protocols a CubeSat is designed and tested against: the CubeSat Design Specification and the deployer manuals that outrank it, environmental and materials standards, CCSDS and ECSS protocols, and the regulatory documents.

A practical note: some of these are free, some are paywalled, and the ones that matter most to a CubeSat team – the CDS, GEVS, the ECSS testing standard and the CCSDS Blue Books – are all freely available. Remember that whatever these say, **your launch provider's payload user guide takes precedence**.

## CubeSat specifications

<!-- CSR-RESOURCES:START ref-standards-cubesat-specs -->
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – Cal Poly SLO. The baseline CubeSat specification: envelope and rail geometry, mass and centre-of-mass limits, materials and anodising, deployment switches, inhibits, and the 30-minute deployable and 45-minute RF quiet periods. Free.
- **[CubeSat Design Specification Rev. 13](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/56e9b62337013b6c063a655a/1458157095454/cds_rev13_final2.pdf)** `PDF` – The previous revision, still worth knowing because much older material (and some deployer documentation) quotes its figures, notably the 1.33 kg/U mass limit.
- **[ISO 17981:2024 – Space systems: Cube satellite (CubeSat) interface](https://www.iso.org/standard/85136.html)** `Link` – International standard for CubeSat internal interfaces – component to component, platform to payload, umbilical connectors and commercial product datasheets. It explicitly does not cover the CubeSat-to-deployer interface, which stays with the CDS. Paywalled
- **[Cal Poly CubeSat Program](https://www.cubesat.org/)** `Link` – The source for current CDS revisions and CubeSat programme documentation
<!-- CSR-RESOURCES:END ref-standards-cubesat-specs -->

## Deployer manuals and payload user guides

Whatever the CDS says, the document that governs a CubeSat's mechanical and safety design is the deployer manual or payload user guide of the provider it flies with. Two are openly published and make good worked examples of the class:

<!-- CSR-RESOURCES:START ref-standards-deployer-manuals -->
- **[Exolaunch EXOpod Nova User Manual, Rev. 1.2](https://exolaunch.com/documents/EXOpod_Nova_User_Manual_June_2024.pdf)** `PDF` – Deployer manual covering 1U–16U, with mass and centre-of-mass allowances, rail dimensions and protrusion limits; states that where it conflicts with the CDS, the manual takes priority. Free PDF
- **[NanoRacks CubeSat Deployer (NRCSD) Interface Definition Document](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Nanoracks-CubeSat-Deployer-NRCSD-IDD.pdf)** `PDF` – ISS deployer interface document, and a worked example of a provider layering its own inhibit and timer requirements on top of the CDS. Free PDF
<!-- CSR-RESOURCES:END ref-standards-deployer-manuals -->

## Testing and environmental verification

<!-- CSR-RESOURCES:START ref-standards-testing -->
- **[ECSS-E-ST-10-03C Rev.1 – Space engineering: Testing](https://ecss.nl/wp-content/uploads/2022/05/ECSS-E-ST-10-03-Rev.1(31May2022).pdf)** `PDF` – Defines qualification, acceptance and protoflight approaches, environmental test types and the test sequence. Freely downloadable.
- **[NASA GEVS (GSFC-STD-7000)](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000)** `Link` – General Environmental Verification Standard. The default environmental envelope for CubeSat campaigns without a specific launcher manifest; source of the widely quoted 14.1 Grms qualification level.
- **[ISO 19683:2026 – Design qualification and acceptance tests of small spacecraft and units](https://www.iso.org/standard/86540.html)** `Link` – International standard specifically covering small spacecraft qualification and acceptance testing. Paywalled.
- **[NASA Goddard Outgassing Database](https://etd.gsfc.nasa.gov/capabilities/outgassing-database/)** `Link` – ASTM E595 total mass loss and collected volatile condensable material data for thousands of materials. The first place to check before selecting an adhesive, tape or printed part.
<!-- CSR-RESOURCES:END ref-standards-testing -->

## Communication protocols and data formats

<!-- CSR-RESOURCES:START ref-standards-communication -->
- **[CCSDS Blue Books](https://ccsds.org/publications/bluebooks/)** `Link` – The full set of freely available recommended standards for space data systems
- **[TM Space Data Link Protocol (CCSDS 132.0-B)](https://ccsds.org/Pubs/132x0b3.pdf)** `PDF` – Telemetry space data link protocol
- **[TC Space Data Link Protocol (CCSDS 232.0-B)](https://ccsds.org/Pubs/232x0b4e1c1.pdf)** `PDF` – Telecommand space data link protocol
- **[CCSDS 123.0-B-2 – Low-Complexity Lossless and Near-Lossless Multispectral and Hyperspectral Image Compression](https://ccsds.org/Pubs/123x0b2e2c3.pdf)** `PDF` – Image compression standard designed for the exact problem CubeSat imaging payloads face
- **[ECSS-E-ST-70-41C – Telemetry and telecommand packet utilization (PUS)](https://ecss.nl/standard/ecss-e-st-70-41c-rev-1-dir1-telecommand-and-telemetry-packet-utilization-review-12-december-2024-28-february-2025/)** `Link` – The European service-based standard for spacecraft telemetry and telecommand
- **[CubeSat Space Protocol (libcsp)](https://libcsp.github.io/libcsp/)** `Link` – The de facto CubeSat onboard networking protocol, MIT licensed
- **[SpaceCAN (LibreCube)](https://librecube.gitlab.io/standards/spacecan/)** `Link` – Simplified redundant CAN bus standard for small spacecraft, derived from ECSS-E-ST-50-15C
<!-- CSR-RESOURCES:END ref-standards-communication -->

## Systems engineering and project standards

<!-- CSR-RESOURCES:START ref-standards-systems-engineering -->
- **[NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2)](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)** `PDF` – Requirements, verification and validation, and the Pre-Phase A to Phase F life cycle. Free.
- **[ECSS standards](https://ecss.nl/)** `Link` – The European Cooperation for Space Standardization's full standard set, covering engineering, product assurance and management. Many are freely downloadable.
- **[ECSS-E-ST-70-11C Rev.1 – Space segment operability](https://ecss.nl/standard/ecss-e-st-70-11c-rev-1-space-segment-operability-15-october-2025/)** `Link` – Requirements for the onboard functions an unmanned spacecraft needs in order to be operable in flight, covering nominal and predefined contingency situations. The standard behind much of what modes, safe mode and FDIR design assumes. Free, registration required.
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
