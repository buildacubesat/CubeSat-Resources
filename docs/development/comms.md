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

### Amateur Bands  
Used primarily by university and research missions under IARU coordination:

- **UHF**  
  - Uplink: 435–438 MHz  
  - Downlink: ~437 MHz (very common)

- **VHF**  
  - Uplink: 145.9–146.0 MHz  
  - Downlink: 144.0–146.0 MHz

- **L-band**  
  - Occasionally used (e.g. 1.2–1.3 GHz); less common in CubeSats

### Licensed Scientific and Commercial Bands**  
Require coordination through ITU and national regulatory agencies:

- **S-band (2–4 GHz)**  
  - Common for high-data-rate downlinks (e.g. 2.2–2.3 GHz)

- **X-band (8–12 GHz)**  
  - Used for high-rate payload data and remote sensing missions

- **Ka-band (26–40 GHz)**  
  - Rare in CubeSats due to pointing precision and power constraints

## Expected Data Rates

Achievable data rates for CubeSat communications vary widely depending on frequency band, modulation scheme, available power, antenna gain, ground station capability, and regulatory constraints. As a rough order of magnitude:

- **VHF / UHF**  
  Typically used for TT&C and beacons.  
  Data rates commonly range from **300 bps to ~19.2 kbps**, with higher rates possible under ideal conditions and advanced modulation/coding. Reliability and link margin are usually prioritised over throughput.

- **S-band**  
  Commonly used for higher-rate telemetry and payload data.  
  Typical CubeSat downlink rates range from **100 kbps to a few Mbps**, depending on antenna design, pointing accuracy, and ground infrastructure.

- **X-band**  
  Used for data-intensive payloads (e.g. imaging).  
  Data rates of **tens to hundreds of Mbps** are possible, but require precise attitude control, high-gain antennas, significant power, and professional ground stations.

Actual usable throughput is often much lower than the raw physical layer rate once packetisation, forward error correction, duty cycles, and pass duration are taken into account.

## Link Budget

A **link budget** is an accounting of all gains and losses between a transmitter and receiver, used to estimate whether a communication link will close with sufficient margin. It is one of the most important design tools for CubeSat communications.

A basic link budget typically includes:

- Transmit power
- Transmit antenna gain
- Free-space path loss (distance and frequency dependent)
- Atmospheric and polarization losses
- Receive antenna gain
- Receiver noise figure and bandwidth
- Required signal-to-noise ratio for the chosen modulation and coding

The result is a **link margin**, usually expressed in dB, indicating how much headroom exists above the minimum required signal level. Positive margin means the link should work under nominal conditions; additional margin is often added to account for pointing errors, degradation, and real-world inefficiencies.

Link budgets are usually calculated for worst-case scenarios (e.g. maximum slant range at low elevation angles) and iterated alongside antenna, power, and ADCS design.

## Ground Segment (Hardware and Software)

See also: [Ground Segment](ground-segment.md).

## Optical Communications

Optical (laser-based) communications are an emerging technology for CubeSats and small spacecraft. Instead of RF, data is transmitted using tightly focused laser beams, enabling extremely high data rates with minimal spectrum congestion.

Potential advantages include:

- Very high data rates relative to size and power
- Narrow beamwidths, reducing interference and interception
- No RF spectrum licensing requirements

However, optical comms also introduce significant challenges:

- Extremely tight pointing and stability requirements
- Sensitivity to cloud cover and atmospheric conditions
- Complex acquisition, tracking, and pointing systems
- Limited availability of compatible ground stations

While still uncommon in CubeSat missions, optical communications are an active area of research and demonstration, and are expected to become more relevant as ADCS performance, onboard processing, and ground infrastructure improve.

---

👉 **Please consider [contributing](../contributing.md)!**