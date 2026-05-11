# Tools and Helpers

This section collects practical tools that support CubeSat development and assembly. It includes physical tools (like crimpers, torque drivers, microscopes), custom jigs and fixtures for alignment or testing, as well as helpful software tools (ECAD, CAD, code, simulation, visualization) and calculators. Whether you're wiring harnesses, assembling PCBs, or measuring fastener torque, this is where the hands-on helpers live.

## Hand Tools and Assembly Equipment

To be added here:

- Torque drivers and fastener tools
- Crimpers, wire strippers, and insertion tools
- ESD-safe tools and workstations
- Repeatability and calibration considerations

## Inspection and Measurement

To be added here:

- Microscopes and cameras
- Calipers, micrometers, and gauges
- Electrical measurement tools
- Visual inspection vs. automated methods

## Jigs, Fixtures, and Test Aids

To be added here:

- Alignment and assembly jigs
- Test fixtures and breakout boards
- 3D-printed vs. machined fixtures
- Designing fixtures for repeatability

## Electrical and RF Test Equipment

To be added here:

- Power supplies and electronic loads
- Oscilloscopes and logic analysers
- Spectrum analysers and VNAs
- Practical tradeoffs for small teams

## Software Tools

To be added here:

- ECAD and CAD tools
- Firmware and software development environments
- Simulation and modelling tools
- Data visualisation and analysis software

## Calculators and Reference Tools

A small but growing collection of templates and worked examples that save you from rebuilding the wheel. Most are free; a few are reference documents rather than fillable templates, but all are useful starting points.

### Stack builders

- **[cubestack.dev (currently in beta)](https://cubestack.dev)** (Patrik Senkyr) – Interactive, browser-based PC/104 stack configuration and validation tool. Includes a board library, a physical stack editor and power budget simulator.

### Power Budget Templates

A power budget tracks energy consumption and generation across mission modes. See [EPS – Power Requirements and Budgets](eps.md#power-requirements-and-budgets) for the underlying methodology.

- **[Artemis CubeSat Kit Power Budget](https://docs.google.com/spreadsheets/d/1nS07D4-2hFsfBfmfiYS8sjpTHMR5pUvH-NhnE5spPVY)** (Hawaii Space Flight Lab) – multi-sheet template covering component-level draws, operational modes, and generation/storage balance. Free to copy in Google Sheets or download as `.xlsx`. The companion textbook chapter at [pressbooks-dev.oer.hawaii.edu/epet302](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/5-9-power-budget-and-profiling/) walks through how to use it step by step.
- **[BIRDS Project power analysis](https://birds-project.com/open-source/pdf/Power-Budget-Analysis-for-1U-satellit20220514.pdf)** (Kyushu Institute of Technology) – published power budget PDF for a 1U mission, with real beta angle assumptions and eclipse timing. Less of a template, more a worked example showing what a defensible analysis actually looks like.
- **["Power Budgets for Mission Success"](http://mstl.atl.calpoly.edu/~workshop/archive/2011/Spring/Day%203/1610%20-%20Clark%20-%20Power%20Budgets%20for%20CubeSat%20Mission%20Success.pdf)** (Craig Clark & Ritchie Logan, Clyde Space, 2011) – slide deck on the Cal Poly CubeSat workshop archive. Practical walkthrough on estimating orbit average power, managing loads, and avoiding negative power budgets.

### Mass Budget Template

- **[CubeSat Resources Mass Budget Template](https://docs.google.com/spreadsheets/d/1WSWPbPNYgs54KLPaoDrw7uAXzCtGm3vM/edit?usp=sharing&ouid=116943914669204149113&rtpof=true&sd=true)** – annotated spreadsheet with component-level mass tracking, automatic margin calculation, and form-factor limits for 1U through 6U.

### RF Link Budget Template

- **[Jan King Link Budget Calculators](https://iaru.amsat-uk.org/spreadsheet.htm)** (Jan King, VK4GEY/W3GEY / AMSAT-UK) — a collection of Excel spreadsheets for satellite link budget analysis, freely available for amateur and non-commercial use. The flagship tool is the *AMSAT/IARU Annotated Link Model System*, a detailed multi-sheet workbook that walks through every gain and loss term — path loss, antenna gains, noise figure, Eb/N₀, modulation — with explanatory notes alongside each calculation. Widely cited in CubeSat comms literature and used as a reference in the [Hawaii CubeSat textbook](https://pressbooks-dev.oer.hawaii.edu/epet302/chapter/software-lab-for-communications/). Free to download; `.xls` format. See also [Comms — Link Budget](comms.md#link-budget) and the [link budget](../references/glossary.md#link-budget) glossary entry.

### Other Budgets

To be added here:
- Other RF calculators
- Thermal estimation worksheets
- PV budget
- Battery calculators

## Automation and Workflow Helpers

To be added here:

- Scripts for testing and data collection
- CI and automation for firmware and docs
- Reproducible build and test environments
- Reducing manual error through tooling

## Documentation and Knowledge Management

To be added here:

- Lab notebooks and build logs
- Checklists and procedures
- Version control for hardware and software
- Knowledge transfer and long-term maintainability

---

👉 **Please consider [contributing](../contributing.md)!**