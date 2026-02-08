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

- **[UniClOGS Ground Station](https://www.uniclogs.org/)**  
  Modular, open-source CubeSat ground-station hardware covering RF, tracking, and control.

- **[Bits and pieces of RF insights](https://www.notblackmagic.com/)**  
  Practical RF engineering notes and hardware experiments focused on real-world SDR use.

- **[SatNOGS Ground Station Hardware](https://wiki.satnogs.org/Ground_Station_Hardware)**  
  Open-source reference designs for rotators, RF front-ends, and full ground-station builds.

- **SDR receivers (Airspy, LimeSDR, HackRF, RTL-SDR, Adalm-Pluto, NI)**  
  Commonly used SDR hardware on Linux, ranging from low-cost monitoring to full-duplex RF work.

- **Az/El antenna rotators (Yaesu, AlfaSpid, Prosistel)**  
  Widely supported commercial rotators with good Hamlib compatibility.

- **DIY rotators (stepper/servo + encoders)**  
  Popular for CubeSat stations, especially when integrated with Hamlib or SatNOGS controllers.

- **Low-noise amplifiers (LNA)**  
  Mast-mounted LNAs are critical for UHF/VHF CubeSat downlinks with modest antennas.

- **Band-pass & SAW filters**  
  Reduce out-of-band interference, especially important in urban RF environments.

- **Timing sources (GPSDO, GNSS receivers)**  
  Provide accurate frequency and time references for Doppler correction and coherent reception.

- **Single-board computers (Raspberry Pi, x86 mini PCs)**  
  Common platforms for running headless Linux ground stations and remote SDR stacks.


### SDR & RF Software

- **[List of SDR Software and Hardware](https://github.com/Slayingripper/Linux-SDR)**  
  A broad, community-maintained index of SDR tools and supported hardware on Linux.

- **[Gqrx SDR](https://www.gqrx.dk/)**  
  Lightweight Qt SDR receiver, great for quick signal inspection and debugging.

- **[SDR++Brown](https://sdrpp-brown.san.systems/)**  
  Modern, modular SDR++ fork with good performance and active development.

- **[SDRangel](https://www.sdrangel.org/)**  
  Advanced multi-channel SDR suite with plugins for satellites, decoding, and control.

- **[CubicSDR](https://cubicsdr.com/)**  
  User-friendly SDR application well suited for learning and casual monitoring.

- **[GNU Radio](https://www.gnuradio.org/)**  
  The de-facto signal-processing framework for building custom CubeSat ground-station pipelines.


### Satellite Tracking & Visualization

- **[Gpredict](https://oz9aec.dk/gpredict/)**  
  Mature satellite tracking software with Doppler correction and Hamlib rotator support.

- **[Look4Sat](https://github.com/rt-bishop/Look4Sat)**  
  Modern Linux satellite tracker with a clean UI and native Hamlib integration.

- **[SkyRoof](https://ve3nea.github.io/SkyRoof/index.html)**  
  High-end Windows-centric tracker, sometimes used via Wine for advanced features.


### Rotator Control (Linux)

- **Hamlib (rotctl / rotctld)**  
  Standard Linux backend for antenna rotator control, offering CLI tools and a network daemon.

- **grotor**  
  Simple GTK GUI frontend for Hamlib, useful for manual az/el control.

- **gr-rotator (GNU Radio block)**  
  GNU Radio block enabling programmatic rotator control directly from signal-processing flows.

- **rotctld web frontends**  
  Small browser-based UIs that expose Hamlib rotator control for headless or remote stations.


### Web-Based & Remote SDR

- **[OpenWebRX](https://www.openwebrx.de/)**  
  Web-based SDR receiver ideal for remote access and shared ground-station setups.

- **[Airspy](https://airspy.com/download/)**  
  Vendor-provided SDR software and tools with solid Linux support for Airspy hardware.


### Integrated / Turnkey Systems

- **[SatNOGS Client](https://satnogs.org/)**  
  Fully open-source Linux ground-station stack combining tracking, SDR, and rotator control.

- **[DragonOS](https://cemaxecuter.com/)**  
  Ubuntu-based SDR Linux distribution bundling GNU Radio, drivers, and satellite tools.


### Typical CubeSat Ground-Station Stack (Linux)

- **Tracking:** Gpredict or Look4Sat  
- **Rotator:** Hamlib (rotctld)  
- **RF:** GNU Radio + SDRangel / SDR++  
- **Remote ops:** OpenWebRX or SatNOGS


---

👉 **Please consider [contributing](../contributing.md)!**