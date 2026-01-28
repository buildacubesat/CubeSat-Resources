# Flight Software

Flight software coordinates all onboard systems, from data handling and command execution to fault management and telemetry. This section explores software architectures, real-time operating systems, bootloaders, state machines, and common libraries used in CubeSat missions. Both bare-metal and RTOS-based approaches are included.

## Software Architecture and Execution Model

To be added here:

- Layered vs. monolithic architectures  
- Separation between hardware abstraction, services, and application logic  
- Event-driven vs. time-driven designs  
- Tradeoffs between simplicity and extensibility

## Boot, Reset, and Update Strategy

To be added here:

- Bootloaders and startup sequencing  
- Safe mode and minimal boot paths  
- In-flight software updates (when and when not)  
- Handling brownouts, resets, and partial failures

## Command and Telemetry Handling

To be added here:

- Command validation and execution models  
- Telemetry packet structures and rates  
- Housekeeping vs. payload data  
- Interaction with ground segment protocols

See also: [Communications](comms.md).

### Inter-Subsystem Communication Protocols

To be added here:

- Role of middleware in CubeSats
- CSP vs. SpaceCAN concepts and tradeoffs
- Addressing, routing, and fault isolation
- Interaction with physical buses

### Data Serialisation and Message Formats

To be added here:

- Binary vs. structured formats
- CCSDS packets and conventions
- Lightweight formats (CBOR, protobuf, custom)
- Forward compatibility and versioning

## Modes, State Machines, and Autonomy

To be added here:

- Mission modes and transitions  
- State machines vs. rule-based logic  
- Autonomy levels in CubeSats  
- Guard conditions and mode safety

## Fault Detection, Isolation, and Recovery (FDIR)

To be added here:

- Watchdogs and health monitoring  
- Threshold-based and rule-based fault detection  
- Recovery actions and escalation  
- Designing for partial failures

## Timing, Scheduling, and Timekeeping

To be added here:

- Task scheduling and priorities  
- Time sources (RTC, GNSS, ground sync)  
- Timestamping telemetry  
- Handling clock drift and resets

## Software Testing and Validation

To be added here:

- Unit and integration testing approaches  
- Flatsat and hardware-in-the-loop testing  
- Simulators and test harnesses  
- Regression testing before launch

See also: [Assembly, Integration and Testing (AIT)](ait.md).  

## Flight Software and Hardware Interaction

To be added here:

- Drivers and hardware abstraction layers  
- Power and inhibit awareness  
- ADCS and payload coupling  
- Thermal and EPS feedback loops

## Documentation and Maintainability

To be added here:

- Code documentation practices  
- Configuration vs. code  
- Knowledge transfer and bus factor  
- Preparing software for operations and handover

## Resources

### Open-source Flight Software Projects

- [NASA Core Flight System (cFS)](https://cfs.gsfc.nasa.gov/) – Modular, flight-proven framework used in many missions.
- [LibreCube Software](https://librecube.gitlab.io/standards/overview/) – Open CubeSat components built around space communication standards.
- [OpenSatKit](https://github.com/OpenSatKit/OpenSatKit) – Full dev environment based on cFS, with simulation and testing tools.
- [PyCubed](https://github.com/pycubed/software) – A fully open-source CubeSat avionics and software stack in Python/MicroPython.
- [OREsat](https://github.com/oresat/oresat-c3-software) – Modular open-source flight software stack developed by students at Portland State University.

### RTOS and Embedded Platforms

- [FreeRTOS](https://www.freertos.org/) – Lightweight, widely used real-time OS for microcontrollers.
- [Zephyr Project](https://zephyrproject.org/) – Scalable, secure RTOS with a growing presence in aerospace.
- [RIOT OS](https://www.riot-os.org/) – Real-time OS for low-power, resource-constrained devices.

### Commercial Platforms

- [Rocket Lab MAX](https://rocketlabcorp.com/space-systems/space-software/)

### Related Docs and Specs

- [ECSS-E-ST-70-41C](https://ecss.nl/standard/ecss-e-st-70-41c-space-segment-operational-procedures/) – Standard for spacecraft operational procedures.
- [CCSDS Recommendations](https://public.ccsds.org/publications/default.aspx) – Core documents for space data and communication protocols.

---

👉 **Please consider [contributing](../contributing.md)!**