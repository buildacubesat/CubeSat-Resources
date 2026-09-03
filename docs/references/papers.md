# Papers

Academic papers, technical articles and conference proceedings on CubeSats and small satellite systems – subsystem design, mission analysis, testing and flight results – and where to look for more.

The papers listed here are ones cited across this site's [development](../development/index.md) pages, chosen because they are open access, empirically grounded, or both. Papers supporting only a single specific claim stay as footnotes on the page that uses them.

## Where to look

<!-- CSR-RESOURCES:START ref-papers-archives -->
- **[Small Satellite Conference Proceedings](https://digitalcommons.usu.edu/smallsat/)** `Link` – Utah State University's freely accessible archive of the premier small satellite conference, with proceedings going back to 1987. The single richest source of CubeSat engineering literature, and all of it open
- **[NASA Technical Reports Server (NTRS)](https://ntrs.nasa.gov/)** `Link` – NASA's open archive of technical reports, conference papers and standards
- **[arXiv](https://arxiv.org/)** `Link` – Preprint server; CubeSat instrument and mission papers frequently appear here before or alongside journal publication
<!-- CSR-RESOURCES:END ref-papers-archives -->

## Reliability and statistics

<!-- CSR-RESOURCES:START ref-papers-reliability -->
- **[Towards the Thousandth CubeSat: A Statistical Overview](https://onlinelibrary.wiley.com/doi/10.1155/2019/5063145)** `Link` – Thyrso Villela et al., *International Journal of Aerospace Engineering*, 2019. Open access. Estimates CubeSat mission success at about 75% excluding launch failures, counting a mission as a success if it survived deployment and commissioning, and finds around 20% of failures occur during launch or deployment. Reports success rates increasing over time and data suggesting infant mortality is decreasing
- **[Survey on the implementation and reliability of CubeSat electrical bus interfaces](https://link.springer.com/article/10.1007/s12567-016-0138-0)** `Link` – Jasper Bouwmeester, Martin Langer and Eberhard Gill, *CEAS Space Journal* 9(2), 163–173, 2017. Open access. Surveys 104 CubeSats, finds I²C the most implemented data bus and bus lockups a major in-orbit issue, with one confirmed catastrophic failure and two probable cases
<!-- CSR-RESOURCES:END ref-papers-reliability -->

## Attitude determination and control

<!-- CSR-RESOURCES:START ref-papers-adcs -->
- **[Design and Numerical Validation of an Algorithm for the Detumbling and Angular Rate Determination of a CubeSat Using Only Three-Axis Magnetometer Data](https://onlinelibrary.wiley.com/doi/10.1155/2018/9768475)** `Link` – Stefano Carletta, Paolo Teofilatto and M. Salim Farissi, *International Journal of Aerospace Engineering*, 2018. Open access. Magnetometer-only detumbling reducing rotational kinetic energy by two orders of magnitude in under one orbit for a 3U with a 0.3 A·m² dipole limit
- **[Attitude Analysis of Small Satellites Using Model-Based Simulation](https://www.hindawi.com/journals/ijae/2019/3020581/)** `Link` – Samir A. Rawashdeh, *International Journal of Aerospace Engineering*, 2019. Open access. Describes the SNAP simulation tool and its modelling of gravity gradient, aerodynamic, magnetic and hysteresis damping torques on small satellites
<!-- CSR-RESOURCES:END ref-papers-adcs -->

## Avionics and power

<!-- CSR-RESOURCES:START ref-papers-avionics-and-power -->
- **[PyCubed: An Open-Source, Radiation-Tested CubeSat Platform Programmable Entirely in Python](https://rexlab.ri.cmu.edu/papers/PyCubed-SmallSat.pdf)** `PDF` – Maximillian Holliday et al., *33rd AIAA/USU Conference on Small Satellites*, SSC19-WKIII-04, 2019. A rare published example of a CubeSat team justifying COTS part selection with real total ionising dose test data. Free PDF
- **[Degradation Modeling and Telemetry-Based Analysis of Solar Cells in LEO for Nano- and Pico-Satellites](https://www.mdpi.com/2076-3417/15/16/9208)** `Link` – Yermek Amangeldi et al., *Applied Sciences* 15(16), 2025. Open access. On-orbit solar cell degradation rates by cell technology and altitude
- **[Deep Learning-Based MPPT Approach to Enhance CubeSat Power Generation](https://doi.org/10.1109/ACCESS.2025.3546066)** `Link` – Abdulazez Abagero et al., *IEEE Access* 13, 40076–40089, 2025. Open access (CC BY 4.0). A deep-learning approach to maximum power point tracking for CubeSat solar arrays
<!-- CSR-RESOURCES:END ref-papers-avionics-and-power -->

## Software and flight software

<!-- CSR-RESOURCES:START ref-papers-software -->
- **[The Power of 10: Rules for Developing Safety-Critical Code](https://spinroot.com/gerard/pdf/P10.pdf)** `PDF` – Gerard J. Holzmann, *IEEE Computer* 39(6), 2006. Ten rules for safety-critical embedded code, every one checkable by static analysis. Short, and the origin of the no-dynamic-allocation and bounded-loop rules that most CubeSat coding standards inherit. Free PDF
<!-- CSR-RESOURCES:END ref-papers-software -->

## Thermal, structures and testing

<!-- CSR-RESOURCES:START ref-papers-thermal-and-testing -->
- **[SATMO: a Multi-Planet Thermal Analysis Tool for CubeSat Missions](https://arxiv.org/abs/2512.07896)** `Link` – Alexander Chipps, Daniel Forgette and Kerri Cahoy, AIAA SciTech Forum 2026, DOI 10.2514/6.2026-2269. Describes an open-source six-node MATLAB thermal model validated against Thermal Desktop to within 1.17 °C. The AIAA version is paywalled; the arXiv preprint is open access. Open access preprint
- **[Method for CubeSat Thermal-Vacuum Cycling Test Specification](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/ICES_2017_102.pdf)** `PDF` – Roy Stevenson Soler Chisabas et al., *47th International Conference on Environmental Systems*, ICES-2017-102, 2017. Compares TVAC requirements across five major standards and proposes a tailoring method. Free PDF
- **[Introduction to On-Orbit Thermal Environments](https://tfaws.nasa.gov/wp-content/uploads/On-Orbit_Thermal_Environments_TFAWS_2014.pdf)** `PDF` – Steven L. Rickman, NASA Engineering and Safety Center, TFAWS 2014. How real albedo and outgoing longwave radiation distributions become hot and cold design cases. Free PDF
<!-- CSR-RESOURCES:END ref-papers-thermal-and-testing -->

## Communications and antennas

<!-- CSR-RESOURCES:START ref-papers-comms -->
- **[Antennas for CubeSat Communication](https://storage.googleapis.com/cubesat-resources/resources/antenna-design-papers/epfl-th7489.pdf)** `PDF` – Miroslav Veljovic, EPFL doctoral thesis no. 7489, 2020, DOI 10.5075/epfl-thesis-7489 ([Infoscience record](https://infoscience.epfl.ch/entities/publication/1897a20d-643d-4c6b-a198-9728504c5c55)). Book-length treatment of CubeSat antenna design and the integration constraints that shape it. Open access
<!-- CSR-RESOURCES:END ref-papers-comms -->

## Payload and instruments

<!-- CSR-RESOURCES:START ref-papers-payload -->
- **[A compact instrument for gamma-ray burst detection on a CubeSat platform I: Design drivers and expected performance](https://arxiv.org/abs/2108.08203)** `Link` – David Murphy et al., *Experimental Astronomy* 52(1–2), 59–84, 2021. Companion to paper II below: the science case and sizing behind GMOD, with Monte Carlo estimates giving a sky-average effective area of 10 cm² at 120 keV and 11–14 gamma-ray bursts detected at high significance over a one-year mission. Open access
- **[A compact instrument for gamma-ray burst detection on a CubeSat platform II: Detailed design, assembly and validation](https://arxiv.org/abs/2203.03502)** `Link` – David Murphy et al., *Experimental Astronomy* 53(3), 961–990, 2022. Detailed design, calibration and validation of a well-documented CubeSat science instrument. Open access
<!-- CSR-RESOURCES:END ref-papers-payload -->

---

Found a paper that belongs here? Please [contribute](../contributing.md).
