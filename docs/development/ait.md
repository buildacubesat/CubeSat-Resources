# Assembly, Integration, and Testing (AIT)

Assembly, Integration, and Testing (AIT) covers the practical work of turning individual CubeSat subsystems into a functioning spacecraft and verifying that it meets mission and launch requirements. This includes mechanical assembly, electrical integration, incremental bring-up, functional verification, simulation, and environmental testing. A structured AIT approach helps catch interface issues early, reduces risk during launch and operations, and improves overall mission reliability.

## Assembly

This section covers the mechanical and electrical assembly of CubeSat subsystems into the final spacecraft. Topics include assembly order, tooling, cleanliness, documentation, and verification steps during build-up. Good assembly practices reduce rework, prevent damage, and simplify later integration and testing.

### Mechanical Assembly

To be added here:

- Assembly sequence and access planning
- Fastener selection, torque, and locking methods
- Handling sensitive components and deployables
- Inspection and documentation during assembly

### Electrical Assembly and Harnessing

To be added here:

- Cable routing and strain relief
- Connector mating and verification
- Harness labeling and documentation
- Avoiding common integration and handling errors

## Integration

This section focuses on combining individual subsystems into a coherent system and verifying that interfaces behave as expected. Integration is typically iterative and closely coupled to functional testing and troubleshooting.

### Subsystem Integration

To be added here:

- Incremental integration strategies
- Power-first and compute-first bring-up approaches
- Managing shared resources (power, buses, timing)
- Identifying and isolating interface issues

### Flatsat and Integration Test Setups

To be added here:

- Flatsat configurations and use cases
- Breakout boards and test harnesses
- Safe testing of flight hardware outside the structure
- Transitioning from flatsat to integrated spacecraft

## Simulation and Testing

This section covers simulation and testing methods used during CubeSat design, integration, and verification. Topics include functional simulation, hardware-in-the-loop (HIL) testing, flatsat setups, environmental testing, vibration and thermal considerations, and software test strategies. Simulation and testing are essential for catching integration issues early and reducing mission risk.

### Environmental Testing

To be added here:

- Vibration, thermal, and vacuum testing
- Common standards (e.g. NASA GEVS, ECSS)
- Access to testing facilities vs. DIY methods

### Functional and Integration Testing

To be added here:

- Subsystem-level vs. system-level testing
- Flatsat setups and incremental bring-up
- Interface validation between boards and subsystems
- Regression testing during hardware and software iteration

### Hardware-in-the-Loop (HIL) Testing

To be added here:

- Using simulators to emulate sensors, actuators, and space environment inputs
- Mixing real flight hardware with simulated subsystems
- Timing, latency, and fault-injection testing
- Common tools and frameworks for HIL setups

### Software Testing and Validation

To be added here:

- Unit testing and integration testing for flight software
- On-target vs. host-based testing
- Handling real-time constraints and watchdog behavior
- Test strategies for fault detection, isolation, and recovery (FDIR)

### Mission Simulation

To be added here:

- End-to-end mission simulations and timelines
- Orbit and attitude propagation inputs
- Power, thermal, and data budget simulation
- Using simulations to validate CONOPS and edge cases

---

👉 **Please consider [contributing](../contributing.md)!**