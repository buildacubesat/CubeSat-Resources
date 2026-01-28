# Inhibits and Hold Down & Release Mechanisms (HDRM)

This section covers inhibit systems and Hold Down and Release Mechanisms (HDRM) used in CubeSats to ensure launch safety and controlled deployment. Topics include remove-before-flight (RBF) pins, deployment switches, separation detection, timers for delayed RF operations, burn wires, and other release mechanisms. Proper inhibit design is critical for regulatory compliance, launch vehicle safety, and mission success.

## Purpose and Safety Context

To be added here:

- Why inhibits exist (launch vehicle and range safety)
- Separation between launch, early orbit, and nominal operations
- Typical failure scenarios inhibits are designed to prevent
- Relationship to licensing and launch provider reviews

## Inhibit Types and Architectures

To be added here:

- Electrical vs. mechanical inhibits
- Single-point vs. redundant inhibit chains
- Normally-open vs. normally-closed strategies
- Common architectural patterns in CubeSats

### Inhibit Interaction with the Electrical Power System (EPS)

To be added here:

- Launch inhibits and remove-before-flight pins as power-domain controls
- Power-up sequencing and controlled energisation after deployment
- Electrical interaction between EPS, HDRM, and deployment switches
- Power-related regulatory and launch provider requirements

### Remove-Before-Flight (RBF) Pins

To be added here:

- Purpose and typical implementation
- Electrical characteristics and wiring patterns
- Handling, procedures, and human factors
- Common failure and misuse cases

### Deployment Switches and Separation Detection

To be added here:

- Spring-loaded deployment switches
- Rail or door contact detection
- Redundancy and switch placement
- Using separation signals in flight software

### Timers and Delayed Activation

To be added here:

- RF silence timers after deployment
- Hardware vs. software timers
- Watchdog interaction and reset behavior
- Launch provider timing requirements

## Hold Down and Release Mechanisms (HDRM)

To be added here:

- Purpose and functional requirements
- Typical loads and preload strategies
- Single-use vs. resettable mechanisms
- Interaction with deployables and structure

### Burn Wire–Based HDRM

To be added here:

- Principle of operation
- Wire materials and routing
- Power requirements and EPS interaction
- Redundancy, verification, and failure modes

### Shape Memory Alloy (SMA)–Based HDRM

To be added here:

- SMA actuation principles
- Power and thermal considerations
- Actuation timing and repeatability
- Advantages and limitations vs. burn wire systems

### Redundancy and Fault Tolerance

To be added here:

- Dual inhibits and independent actuation paths
- Electrical vs. mechanical redundancy
- Single-event and partial-failure handling
- Verification of inhibit independence

### Verification and Testing

To be added here:

- Ground verification of inhibit states
- Continuity and resistance testing
- End-to-end deployment testing
- Common testing mistakes and risks

## Documentation and Compliance

To be added here:

- What launch providers typically ask for
- Inhibit diagrams and state descriptions
- Test evidence and traceability
- Common reasons for review rejection

---

👉 **Please consider [contributing](../contributing.md)!**
