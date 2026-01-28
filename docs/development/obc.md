# Onboard Computing (OBC)

This section covers onboard computing elements for CubeSats, including MCUs, FPGAs, and SBCs. Topics include architecture choices, redundancy strategies, power and boot sequencing, fault tolerance, real-time vs. high-level OS tradeoffs, and interfacing with payloads and subsystems. Compute selection and integration strongly influence system reliability, power budget, and software complexity.

## Role of the OBC in a CubeSat

To be added here:

- Central coordination vs. distributed computing
- Responsibilities of the OBC vs. subsystem controllers
- Interaction with EPS, ADCS, Comms, and Payload
- Architectural patterns in small spacecraft

## Microcontrollers (MCUs)

To be added here:

- Common MCU families used in CubeSats
- Industrial vs. space-grade components
- Radiation tolerance, derating, and screening
- Performance, power, and ecosystem tradeoffs

## Single-Board Computers (SBCs)

To be added here:

- When an SBC makes sense in a CubeSat
- Linux-based systems and operational implications
- Power consumption and boot-time considerations
- Reliability challenges and mitigation strategies

## FPGAs and Programmable Logic

To be added here:

- Use cases for FPGAs in CubeSats
- Soft-core vs. hard-core architectures
- Radiation effects and mitigation techniques
- Development complexity and verification effort

## Redundancy and Fault Tolerance

To be added here:

- Cold vs. warm redundancy
- Dual-processor and supervisor architectures
- Voting schemes and watchdog hierarchies
- Reset, isolation, and recovery strategies

## Boot, Power, and Reset Management

To be added here:

- Power-up sequencing and dependency ordering
- Bootloaders and safe boot paths
- Brownout handling and reset behaviour
- Interaction with inhibits and EPS

## Interfaces and Buses

To be added here:

- Common internal buses (I2C, SPI, UART, CAN, SpaceWire)
- Bus arbitration and fault containment
- Electrical and software interface boundaries
- Scaling and performance considerations

## Timing and Timekeeping

To be added here:

- System clocks and time sources
- Synchronisation with GNSS and ground
- Timestamping and time distribution
- Handling resets and clock drift

## Software Stack and OS Choices

To be added here:

- Bare-metal vs. RTOS vs. Linux
- Driver models and hardware abstraction
- Update strategies and configuration management
- Coupling between OBC and flight software architecture

## Advanced and Emerging Computing Concepts

To be added here:

- Onboard AI and ML workloads
- Flying GPUs and accelerators
- Edge processing and data reduction
- Current limitations and research directions

## OBC Integration and Testing

To be added here:

- Electrical and thermal integration
- EMI and signal integrity considerations
- Flatsat and HIL testing
- The [SpaceInventor stack](https://github.com/spaceinventor/) (csp, csh, libparam)
- Common integration pitfalls

---

👉 **Please consider [contributing](../contributing.md)!**