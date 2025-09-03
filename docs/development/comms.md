# Communications

The Communications section focuses on radio communication systems used in CubeSats, including transceivers, antennas, modulation schemes, and ground station interfaces. It covers both UHF/VHF amateur radio systems and higher-bandwidth S-band and X-band setups. Optical communication is not yet common in CubeSats, but emerging concepts will be added here as they develop.

## Radio Frequency Communications (RF) Overview

CubeSats typically employ RF communication for uplink (commands) and downlink (beacon, telemetry and payload data), operating in both amateur and licensed frequency bands. TT&C is a commonly used abbreviation:

A special case is the **beacon**: a low-data-rate, always-on (during commissioning) signal that periodically transmits basic telemetry (e.g. battery voltage, temperature, timestamp, ID). Beacons help confirm the satellite is alive and can be used to aid tracking. The **[SatNOGS](https://satnogs.org/)** network has become a de facto standard for receiving and sharing beacon data in open-source and academic missions, enabling global signal tracking and community-supported downlink coverage.

CubeSat beacons are most commonly found in the **UHF amateur band (~437 MHz)** and typically use simple modulation schemes like **AFSK**, **BPSK**, or **GMSK**. They often conform to protocols such as **AX.25** for compatibility with amateur ground stations.

**Telemetry, Tracking, and Command (TT&C)** refers to the fundamental communication link between a spacecraft and its ground segment. 

- **Telemetry**: Downlinked data about the spacecraft’s health, status, and environment (e.g. temperature, voltage, position).
- **Tracking**: Ground-based tracking of the satellite’s orbit and signal, often using Doppler shift and time-of-flight data.
- **Command**: Uplinked instructions that control the satellite’s behavior, such as mode changes, resets, or payload activation.

TT&C is typically implemented on a robust, low-data-rate RF link—often in UHF or VHF—to ensure reliability even under degraded conditions. It operates independently from high-bandwidth payload downlinks and remains active throughout the mission lifecycle, often independently of high-bandwidth payload links.

**Amateur Bands**  
Used primarily by university and research missions under IARU coordination:

- **UHF**  
  - Uplink: 435–438 MHz  
  - Downlink: ~437 MHz (very common)

- **VHF**  
  - Uplink: 145.9–146.0 MHz  
  - Downlink: 144.0–146.0 MHz

- **L-band**  
  - Occasionally used (e.g. 1.2–1.3 GHz); less common in CubeSats

**Licensed Scientific and Commercial Bands**  
Require coordination through ITU and national regulatory agencies:

- **S-band (2–4 GHz)**  
  - Common for high-data-rate downlinks (e.g. 2.2–2.3 GHz)

- **X-band (8–12 GHz)**  
  - Used for high-rate payload data and remote sensing missions

- **Ka-band (26–40 GHz)**  
  - Rare in CubeSats due to pointing precision and power constraints

## Software (mainly Linux)
- [List of SDR Software and Hardware](https://github.com/Slayingripper/Linux-SDR)
- [Gqrx SDR](https://www.gqrx.dk/)
- [SDR++Brown](https://sdrpp-brown.san.systems/)
- [SkyRoof](https://ve3nea.github.io/SkyRoof/index.html)
- [Airpsy](https://airspy.com/download/)
- [Gpredict](https://oz9aec.dk/gpredict/)
- [OpenwebRX](https://www.openwebrx.de/)
- [SDRangel](https://www.sdrangel.org/)
- [CubicSDR](https://cubicsdr.com/)S
- [GNU Radio](https://www.gnuradio.org/)
- [DragonOS](https://cemaxecuter.com/)

## Hardware
- [UniClOGS](https://www.uniclogs.org/)