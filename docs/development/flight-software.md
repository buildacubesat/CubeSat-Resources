# Flight Software

Flight software coordinates all onboard systems, from data handling and command execution to fault management and telemetry. This section explores software architectures, real-time operating systems, bootloaders, state machines, and common libraries used in CubeSat missions. Both bare-metal and RTOS-based approaches are included.

## Open-source Flight Software Projects

- [NASA Core Flight System (cFS)](https://cfs.gsfc.nasa.gov/) – Modular, flight-proven framework used in many missions.
- [LibreCube Software](https://librecube.gitlab.io/standards/overview/) – Open CubeSat components built around space communication standards.
- [OpenSatKit](https://github.com/OpenSatKit/OpenSatKit) – Full dev environment based on cFS, with simulation and testing tools.
- [PyCubed](https://github.com/pycubed/software) – A fully open-source CubeSat avionics and software stack in Python/MicroPython.
- [OREsat](https://github.com/oresat/oresat-c3-software) – Modular open-source flight software stack developed by students at Portland State University.

## RTOS and Embedded Platforms

- [FreeRTOS](https://www.freertos.org/) – Lightweight, widely used real-time OS for microcontrollers.
- [Zephyr Project](https://zephyrproject.org/) – Scalable, secure RTOS with a growing presence in aerospace.
- [RIOT OS](https://www.riot-os.org/) – Real-time OS for low-power, resource-constrained devices.

## Commercial Platform

- [Rocket Lab MAX](https://rocketlabcorp.com/space-systems/space-software/)

## Related Docs and Specs

- [ECSS-E-ST-70-41C](https://ecss.nl/standard/ecss-e-st-70-41c-space-segment-operational-procedures/) – Standard for spacecraft operational procedures.
- [CCSDS Recommendations](https://public.ccsds.org/publications/default.aspx) – Core documents for space data and communication protocols.
