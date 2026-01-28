# Ground Segment

The ground segment includes everything on Earth that supports your CubeSat mission: ground stations, antennas, radios, tracking software, and data handling pipelines. This section covers both amateur and professional setups, from SatNOGS to custom stations, and includes tools for decoding, commanding, and archiving telemetry.

## Ground Station Architectures

To be added here:

- Single-station vs. distributed ground station networks like SatNOGS
- Amateur, institutional, and commercial ground segments
- Tradeoffs between availability, cost, and control
- Typical evolution from early mission to routine operations
- Ground-station-as-a-service (GSaaS)

## Antennas and RF Front-End

To be added here:

- Omnidirectional vs. directional antennas
- Polarisation considerations
- Preamplifiers, filters, and feedlines
- Managing noise, interference, and gain staging

## Tracking and Pass Prediction

To be added here:

- TLEs and orbital element sources
- Pass prediction and scheduling
- Doppler shift compensation
- Integration with rotators and radios

## Telemetry Reception and Decoding

To be added here:

- Beacon vs. high-rate downlink reception
- Demodulation and decoding pipelines
- Packet framing and error correction
- Handling partial frames and corrupted data

See also: [Flight Software](flight-software.md)  

## Command Uplink

To be added here:

- Command validation and safety checks
- Uplink timing and access windows
- Authentication and misuse prevention
- Interaction with flight software modes

## Data Handling and Archiving

To be added here:

- Telemetry storage and databases
- Long-term archiving and reproducibility
- Data visualisation and dashboards
- Sharing data with collaborators or the public

## Automation and Operations

To be added here:

- Automated pass scheduling and execution
- Hands-off operations and alerting
- Health monitoring and trend analysis
- Scaling from manual to semi-autonomous ops

## Testing and Validation

To be added here:

- Ground segment testing before launch
- End-to-end mission rehearsals
- Simulated passes and RF loopback testing
- Common failure modes during early operations

## Regulatory and Operational Considerations

To be added here:

- Amateur radio licensing constraints
- Transmit power and duty cycle limits
- Operating procedures and documentation
- Handover between operators and teams

## Resources

### Hardware
- [UniClOGS Ground Station](https://www.uniclogs.org/)
- [Bits and pieces of RF insights](https://www.notblackmagic.com/)

### Software (mainly Linux)
- [List of SDR Software and Hardware](https://github.com/Slayingripper/Linux-SDR)
- [Gqrx SDR](https://www.gqrx.dk/)
- [SDR++Brown](https://sdrpp-brown.san.systems/)
- [SkyRoof](https://ve3nea.github.io/SkyRoof/index.html)
- [Airpsy](https://airspy.com/download/)
- [Gpredict](https://oz9aec.dk/gpredict/)
- [OpenwebRX](https://www.openwebrx.de/)
- [SDRangel](https://www.sdrangel.org/)
- [CubicSDR](https://cubicsdr.com/)
- [GNU Radio](https://www.gnuradio.org/)
- [DragonOS](https://cemaxecuter.com/)

---

👉 **Please consider [contributing](../contributing.md)!**