# Communications

The Communications section covers the radio link between a CubeSat and its operators: bands and their regulatory constraints, link budgets, modulation and coding, and the flight-side hardware that implements them. Ground station design lives on the [Ground Segment](ground-segment.md) page; this page stops at the antenna.

The communications subsystem is unusual in that its hardest constraints are legal rather than technical. Which band you may use, what you may send over it, and whether you may encrypt it are decided by your licence and your [IARU](../references/glossary.md#iaru) coordination, not by your design. Settle that first – see [Qualification and Launch – Frequency licensing](launch.md#frequency-licensing) – because it determines the transceiver you buy.

## Radio Frequency Communications (RF) Overview

**Telemetry, Tracking, and Command ([TT&C](../references/glossary.md#ttc))** is the fundamental link between a spacecraft and its ground segment:

- **Telemetry** – downlinked data about the spacecraft's health, status and environment (temperature, voltage, mode, position).
- **Tracking** – ground-based determination of the satellite's orbit and signal, often using [Doppler shift](../references/glossary.md#doppler-shift) and time-of-flight data.
- **Command** – uplinked instructions that control the spacecraft's behaviour: mode changes, resets, payload activation.

TT&C is normally implemented as a robust, low-data-rate link in UHF or VHF, so that it keeps working when the spacecraft is tumbling, power-starved or partially failed. It operates independently of any high-rate payload downlink and remains active for the whole mission. A mission that loses its payload downlink is disappointing; one that loses TT&C is over.

A special case is the **[beacon](../references/glossary.md#beacon)**: a low-rate signal, transmitted periodically and continuously during commissioning, carrying basic telemetry such as battery voltage, temperature, timestamp and spacecraft ID. Beacons confirm the satellite is alive and aid identification and tracking. The **[SatNOGS](../references/glossary.md#satnogs)** network has become the de facto standard for receiving and sharing beacon data in open-source and academic missions, giving small teams global coverage they could never build themselves. Publishing your beacon format before launch is one of the highest-value, lowest-cost things a CubeSat team can do.

Beacons are most commonly found in the UHF amateur segment around 437 MHz, using simple modulation such as [AFSK](../references/glossary.md#afsk), [BPSK](../references/glossary.md#bpsk) or [GMSK](../references/glossary.md#gmsk), and often conform to [AX.25](../references/glossary.md#ax25) for compatibility with existing amateur ground stations.

## Frequency Bands

### Amateur-satellite service

Used by most university and research missions, under IARU coordination. Two things are easy to get wrong here. First, **the amateur-satellite allocation is narrower than the amateur allocation** – the fact that your handheld transmits on 145.2 MHz does not mean a satellite may. Second, **the IARU band plan is what binds you in practice**, because coordination is granted against it.[^iaru-spectrum]

| Band | Segment available to satellites | Notes |
| :---- | :---- | :---- |
| VHF (2 m) | **145.800–146.000 MHz**, plus 144.000–144.025 MHz | Both directions. The rest of 144–146 MHz is not available for satellite use in practice. |
| UHF (70 cm) | **435–438 MHz** | Both directions – uplink and downlink are separate channels inside the same segment, not separate bands. By far the most used CubeSat segment. |
| L-band (23 cm) | **1260–1270 MHz** | **Earth-to-space only** under ITU footnote 5.282. There is no amateur-satellite downlink at 23 cm. |
| S-band (13 cm) | **2400–2450 MHz** | Both directions. A real option for higher-rate amateur missions, and often overlooked. |

!!! warning "What the amateur service costs you"
    Amateur-satellite operation is free of spectrum fees and comes with a global network of people who will listen for you – but the rules constrain the mission, not just the radio. There is **no commercial use** of the link, and obscuring the meaning of your transmissions is **generally prohibited**, so assume your telemetry is readable by anyone with a receiver. Telecommand is the exception worth knowing: several administrations treat it separately from ordinary amateur traffic, and in the US a space telecommand station "may transmit special codes intended to obscure the meaning of telecommand messages".[^fcc-telecommand] Either way, **authentication matters more than encryption here** – signing commands so they cannot be forged is legal everywhere and addresses the actual threat. Design your command handling around this from the start – see [Flight Software – Commands](flight-software.md#commands). If your mission has a commercial purpose, the amateur route is closed to you and you are in the next section.

### Non-amateur bands

These require a spectrum authorisation from your national regulator, which files with the [ITU](../references/glossary.md#itu) on your behalf. Slower, more expensive, and with a genuine risk of not getting what you asked for – start at least 18 months out.

- **S-band, 2025–2110 MHz up / 2200–2290 MHz down** – the space operation and space research allocations, and the conventional home for higher-rate TT&C. A typical COTS CubeSat S-band transceiver works across exactly this pair.[^endurosat-sband]
- **X-band, 8025–8400 MHz down** – the Earth exploration-satellite allocation, and where data-intensive imaging missions downlink.
- **Ka-band, 26–40 GHz** – rare on CubeSats because of the pointing precision and power required, but demonstrated: NASA's ISARA reflectarray mission exceeded 100 Mbps.[^nasa-soa-comms]

<!-- CSR-RESOURCES:START dev-comms-bands-and-coordination -->
- **[Amateur and Amateur-Satellite Service Spectrum (IARU)](https://www.iaru.org/wp-content/uploads/2020/01/Amateur-Services-Spectrum-2020_.pdf)** `PDF` – The allocations and the ITU footnotes that govern them, including 5.282 and the 1260–1270 MHz Earth-to-space restriction
- **[IARU Satellite Frequency Coordination](https://www.iaru.org/reference/satellites/)** `Link` – The coordination process, the current request form, and the panel's meeting schedule. Requests are submitted through your national member society
- **[NASA State of the Art – Communications](https://www.nasa.gov/smallsat-institute/sst-soa/soa-communications/)** `Link` – Annually revised survey of small spacecraft RF and optical communications, including COTS transceiver classes and demonstrated data rates
<!-- CSR-RESOURCES:END dev-comms-bands-and-coordination -->

## Expected Data Rates

Achievable rates vary widely with band, modulation, available power, antenna gain, ground station capability and regulatory constraints. As orders of magnitude:

- **VHF / UHF** – TT&C and beacons. Commonly **300 bps to 19.2 kbps**, with 9600 bps GMSK the workhorse. Reliability and [link margin](../references/glossary.md#link-margin) are prioritised over throughput.
- **S-band** – higher-rate telemetry and modest payload data. Typically **100 kbps to a few Mbps**; COTS CubeSat units often sit in the 5–125 kbps range, with megabit-class links requiring better antennas and pointing.[^endurosat-sband]
- **X-band** – data-intensive payloads. **Tens to hundreds of Mbps** are possible, but require precise attitude control, high-gain antennas, significant power and professional ground stations.

Usable throughput is always well below the physical-layer rate once packetisation, forward error correction, duty cycle and pass duration are accounted for. The number that matters is **bits per day**, not bits per second: four 8-minute passes at 9600 bps is about 2.3 MB per day before overhead, and that figure – not the link rate – is what your payload data volume has to fit inside. See [Flight Software – Telemetry](flight-software.md#telemetry) and [Payload – Data reduction and compression](payload.md#data-reduction-and-compression).

## Link Budget

A **[link budget](../references/glossary.md#link-budget)** accounts for every gain and loss between transmitter and receiver, and tells you whether the link closes with margin. It is the single most important design tool in CubeSat communications, and it couples directly to the power budget, the antenna design and the pointing requirement.

A basic budget includes transmit power, transmit antenna gain, free-space path loss, atmospheric and polarisation losses, receive antenna gain, receiver noise figure and bandwidth, and the [signal-to-noise ratio](../references/glossary.md#snr) required by your modulation and coding. The result is a **link margin** in dB.

Budgets are calculated for the worst case – maximum slant range at low elevation – and iterated alongside antenna, power and ADCS design.

### A worked example

A conventional UHF downlink, to show the shape of the arithmetic:

| Term | Value | Note |
| :---- | :---- | :---- |
| Transmit power | +30.0 dBm | 1 W |
| Feeder and matching loss | −1.0 dB | |
| Satellite antenna gain | 0.0 dBi | Deployed monopole, no pointing assumed |
| **EIRP** | **+29.0 dBm** | |
| Free-space path loss | −145.3 dB | 437 MHz at 1000 km slant range |
| Polarisation mismatch | −3.0 dB | Linear satellite antenna, circular ground antenna |
| Atmospheric and implementation loss | −1.0 dB | |
| Ground antenna gain | +14.0 dBi | Crossed Yagi |
| **Received power** | **−106.3 dBm** | |
| Noise density | −171.0 dBm/Hz | 3 dB system noise figure, LNA at the antenna |
| **C/N₀** | **64.7 dB-Hz** | |
| Data rate | 9600 bps | −39.8 dB |
| **E_b/N₀ available** | **24.9 dB** | |
| E_b/N₀ required | 9.6 dB | GMSK, 10⁻⁵ BER, uncoded |
| **Margin** | **+15.3 dB** | |

Two things to take from it. First, free-space path loss dominates everything else, and it grows as the square of both range and frequency – moving the same link to 2.25 GHz costs another 14 dB before anything else changes. Second, the comfortable-looking margin evaporates at the horizon: at 2000 km slant range you lose 6 dB of it, plus more to atmospheric loss at low elevation. Recompute at your worst-case geometry, not at zenith.

Note that the above budget is illustrative and computed from the stated assumptions rather than taken from a flown mission. The required Eb/N0 figure is the textbook uncoded value; real receivers have implementation loss, and coding gain moves it the other way. Use the Jan King spreadsheet for actual numbers.

<!-- CSR-RESOURCES:START dev-comms-link-budget -->
- **[Jan King Link Budget Calculators](https://iaru.amsat-uk.org/spreadsheet.htm)** `Link` – The standard amateur satellite link budget spreadsheets, and the best starting point for a first calculation
<!-- CSR-RESOURCES:END dev-comms-link-budget -->

## Doppler, Oscillators and Acquisition

A LEO satellite closes and opens range at up to roughly 7 km/s relative to a ground station, which shifts the carrier by about 2.3 parts in 100,000:

| Band | Approximate Doppler shift across a pass |
| :---- | :---- |
| 145 MHz | ±3.4 kHz |
| 437 MHz | ±10 kHz |
| 2.25 GHz | ±53 kHz |
| 8.2 GHz | ±190 kHz |

The shift is largest at acquisition, sweeps through zero at closest approach, and is fastest exactly when you most want lock. Three consequences for the flight side:

- **Your receiver needs capture range to match.** A narrowband receiver that cannot search ±10 kHz will not hear an uplink at the start of a pass, which is when you most need it.
- **Oscillator stability is comparable to Doppler.** A 10 ppm TCXO at 437 MHz is ±4.4 kHz of frequency uncertainty on its own, and it drifts with temperature across an orbit. The ground station can correct for predicted Doppler; it cannot correct for an unknown offset in your radio.
- **The ground station corrects, the satellite usually does not.** Standard practice is to pre-compensate the uplink and post-correct the downlink on the ground, from a [TLE](../references/glossary.md#tle) and SGP4 propagation. That works only if your TLE identification is right – see [Ground Segment – Tracking and Pass Prediction](ground-segment.md#tracking-and-pass-prediction).

## Modulation, Coding and Protocols

**Modulation.** AFSK at 1200 bps is the simplest and the most widely receivable, at the cost of throughput. BPSK and GMSK at 9600 bps are the practical workhorses. Higher-order schemes buy rate at the cost of required signal-to-noise ratio, which your link budget has to pay for.

**Coding.** [Forward error correction](../references/glossary.md#fec) buys several dB of effective margin for a modest overhead, and is close to free on modern radios. Convolutional coding with Reed-Solomon, or an LDPC scheme where the hardware supports it, are the common choices. Coding gain is usually cheaper than transmit power, which costs you battery, and cheaper than antenna gain, which costs you pointing.

**Framing.** Two families, and the choice has consequences beyond the wire format:

- **AX.25** is the amateur standard. Every amateur ground station and most SatNOGS decoders already speak it, which turns strangers into a tracking network. It is inefficient and has no built-in error correction, so it is usually wrapped in an FEC layer.
- **CCSDS** is what the professional world uses – proper space data link protocols, framing and coding, and interoperability with agency ground stations. Heavier to implement, and the right choice for missions with a non-amateur link. The Blue Books are free; see [Standards & Protocols](../references/standards.md#communication-protocols-and-data-formats).

Onboard, [CSP](../references/glossary.md#csp) (the CubeSat Space Protocol) is the de facto network layer between subsystems, and it can extend over the radio link so that the ground addresses subsystems the same way flight software does. See [Flight Software – Inter-Subsystem Communication Protocols](flight-software.md#inter-subsystem-communication-protocols).

## Flight Segment Hardware

### Transceivers

The realistic options, in ascending order of effort:

- **COTS CubeSat transceivers** – a module in a standard stack format, with a driver, a datasheet and flight heritage. The default for a first mission, and the choice that lets you spend your effort elsewhere. EnduroSat, GomSpace, ISISPACE, AAC Clyde and NanoAvionics all sell UHF and S-band units; [SatSearch](https://satsearch.co/) and the [CubeSat Shop](https://www.cubesatshop.com/) are the places to compare them.
- **Open-source hardware** – the Libre Space Foundation's SatNOGS-COMMS is an open communications subsystem developed alongside the SatNOGS ground network, and is the most credible open option currently available.
- **[SDR](../references/glossary.md#sdr)-based, built in-house** – maximum flexibility and a genuine research contribution, but you are now responsible for the PA, the filtering, the EMC behaviour and the radiation tolerance of the whole chain. Reasonable for a process-oriented mission, expensive for a result-oriented one.

Whatever you choose, check three things early: the actual RF output power at the connector rather than at the PA, the current draw during transmit (see below), and whether the unit's default configuration is legal in the band you have coordinated.

<!-- CSR-RESOURCES:START dev-comms-transceivers -->
- **[SatNOGS-COMMS (Libre Space Foundation)](https://www.libre.space/projects/satnogs-comms/)** `Link` – Open-source communications subsystem for CubeSats, developed alongside the SatNOGS ground station network
- **[EnduroSat UHF Transceiver II](https://www.endurosat.com/products/uhf-transceiver-ii/)** `Link` – Widely used COTS UHF transceiver for CubeSats
- **[EnduroSat S-Band Transceiver](https://www.endurosat.com/products/s-band-transceiver/)** `Link` – Full-duplex S-band unit, 2025–2110 MHz up and 2200–2290 MHz down, 5–125 kbps
- **[GomSpace NanoCom AX100](https://gomspace.com/product/nanocom-ax100/)** `Link` – Long-established UHF transceiver with extensive flight heritage
<!-- CSR-RESOURCES:END dev-comms-transceivers -->

### Antennas

Nearly every CubeSat UHF or VHF antenna is a deployable: tape-spring monopoles, dipoles and turnstiles, stowed under a burn-wire or similar restraint and released after the mandatory delay. That makes the antenna a mechanism as much as an RF component, with all the qualification that implies – see [Structure – Deployable Structures and Mechanisms](structure.md#deployable-structures-and-mechanisms) and [Inhibits and HDRM](inhibits-hdrm.md).

Two design points that recur. A tumbling spacecraft has no fixed antenna orientation, so a near-omnidirectional pattern and an honest 0 dBi assumption in the link budget are worth more than a higher-gain pattern you cannot point. And a linearly polarised satellite antenna against a circularly polarised ground antenna costs a fixed 3 dB, which is cheaper to accept in the budget than to engineer away – see [Ground Segment – Polarisation](ground-segment.md#polarisation).

Higher bands change the picture: patch antennas at S-band and reflectarrays at X- and Ka-band offer real gain, and immediately impose a pointing requirement on [GNC](gnc.md).

<!-- CSR-RESOURCES:START dev-comms-antenna-design -->
- **[Antennas for CubeSat Communication (Miroslav Veljovic, EPFL doctoral thesis, 2020)](https://storage.googleapis.com/cubesat-resources/resources/antenna-design-papers/epfl-th7489.pdf)** `PDF` – Book-length treatment of CubeSat antenna design and the integration constraints that shape it; thesis no. 7489, DOI 10.5075/epfl-thesis-7489. Open access
- **[S-Band RHCP Patch Antenna – GitHub repository](https://github.com/ICDT-Inatel-Cubesat-Design-Team/S-Band-Antenna)** `Link` – Open-source S-band patch antenna repository
<!-- CSR-RESOURCES:END dev-comms-antenna-design -->

### Power, duty cycle and heat

The transmitter is usually what breaks the power budget. A 1 W RF output at 30–40% PA efficiency draws 3 W or more from the bus, which for a 1U is often more than the orbit-average generation. The resolution is duty cycle: transmit during passes, beacon sparsely between them, and size the battery for the burst rather than the average. Model it explicitly – see [EPS – Power Requirements and Budgets](eps.md#power-requirements-and-budgets).

The same inefficiency appears as heat, concentrated in one component. PA dissipation is a recognised CubeSat thermal problem, particularly during long transmit windows; see [Thermal Management](thermal.md).

### RF silence and inhibits

The CDS requires that no RF signal is generated or transmitted earlier than **45 minutes after deployment**, and launch providers enforce their own, sometimes stricter, version of this. That is a flight software and hardware requirement, not a procedural one: the transmitter must be inhibited by design and the timer must be demonstrable to your provider. See [Inhibits and HDRM – Timers and Delayed Activation](inhibits-hdrm.md#timers-and-delayed-activation) and [Structure – What the CDS actually requires](structure.md#what-the-cds-actually-requires).

## Ground Segment

Ground station architecture, antennas and rotators, tracking and pass prediction, decoding and automation are covered in full on the [Ground Segment](ground-segment.md) page. The interface between the two is the link budget above: the ground station's gain and noise figure are terms in it, and improving them is often far cheaper than improving anything on the spacecraft.

## Communication via Satellite Constellations

Some missions use an existing commercial constellation as a relay rather than talking directly to their own ground station. The CubeSat communicates with a constellation satellite, which forwards the data to the provider's infrastructure.

### Low-data-rate relay

LEO relay constellations such as **Iridium** are used by some CubeSats for housekeeping telemetry, basic commanding and mission monitoring, typically via compact modem modules originally built for terrestrial and maritime use.

- Near-global coverage and frequent contact opportunities
- Very low data rates – bytes to a few kilobytes per message
- Simple antennas and relaxed pointing requirements
- Commercial service contracts, with per-message or per-byte costs

Not suitable for payload data, but attractive as a secondary or backup channel, or for missions that value availability over throughput. One caveat worth resolving early: these modules and their airtime plans are sold for terrestrial use, and orbital use is a separate question of both the provider's service terms and your own licensing. Confirm it in writing before designing around it.

### Direct-to-device and broadband constellations

Large broadband and direct-to-cell constellations are beginning to explore space-to-space connectivity beyond the traditional ground station model, which would in principle offer near-continuous connectivity, less dependence on custom ground stations, and higher rates than existing relay services.

In practice these options remain limited by regulatory constraints, service availability, hardware compatibility, power requirements and commercial access models. Treat them as forward-looking rather than as an operational baseline.

## Optical Communications

Optical (laser) communications transmit data on a tightly focused beam instead of a radio carrier, offering very high data rates for the size and power, narrow beamwidths that reduce interference and interception, and no spectrum allocation to coordinate.

That last point is often overstated. Optical links avoid ITU frequency coordination and IARU coordination, but they do not avoid regulation: the mission still needs national authorisation, and directed-energy transmission brings its own approvals, including coordination to protect aircraft and other spacecraft from the beam.

The engineering costs are substantial: extremely tight pointing and stability requirements that feed straight back into [GNC](gnc.md), sensitivity to cloud cover and atmospheric conditions, complex acquisition and tracking, and very few compatible ground stations. NASA's state-of-the-art survey treats free-space optical as a compelling alternative for high-rate links while noting it remains at low maturity for small spacecraft.[^nasa-soa-comms]

Still uncommon on CubeSats, but an active area of demonstration, and increasingly relevant as ADCS performance, onboard processing and ground infrastructure improve.

<!-- CSR-RESOURCES:START dev-comms-optical -->
- **[NASA State of the Art – Communications](https://www.nasa.gov/smallsat-institute/sst-soa/soa-communications/)** `Link` – Includes a dedicated treatment of free-space optical communications for small spacecraft, with maturity assessments
- **[Lasercom terminal open-source model and simulation software](https://www.reddit.com/r/lasercom/comments/1godxou/lasercom_terminal_open_source_modelsimulation_sw/)** `Link` – Community thread collecting open-source starting points for laser communication terminal development
<!-- CSR-RESOURCES:END dev-comms-optical -->

---

👉 **Please consider [contributing](../contributing.md)!**

[^iaru-spectrum]: International Amateur Radio Union, [*Amateur and Amateur-Satellite Service Spectrum*](https://www.iaru.org/wp-content/uploads/2020/01/Amateur-Services-Spectrum-2020_.pdf) (revised January 2020). Free PDF. Source for the amateur-satellite allocations and the ITU Radio Regulations footnotes governing them, including No. 5.282 and its restriction of amateur-satellite operation in 1260–1270 MHz to the Earth-to-space direction. Practical satellite segments in the 2 m band – 145.800–146.000 MHz and 144.000–144.025 MHz – follow the IARU band plan rather than the ITU allocation, which covers the whole of 144–146 MHz.

[^nasa-soa-comms]: NASA Small Spacecraft Systems Virtual Institute, [*State-of-the-Art of Small Spacecraft Technology*, Chapter 9: Communications](https://www.nasa.gov/smallsat-institute/sst-soa/soa-communications/) (revision dated May 2026). Source for the ISARA Ka-band demonstration exceeding 100 Mbps, the MarCO X-band relay, COTS transceiver classes, and the maturity assessment of free-space optical communications for small spacecraft.

[^endurosat-sband]: EnduroSat, [*S-Band Transceiver*](https://www.endurosat.com/products/s-band-transceiver/) product documentation. Cited as a representative COTS CubeSat S-band unit: 2025–2110 MHz receive, 2200–2290 MHz transmit, configurable 5–125 kbps, 24–33 dBm output. Named as an example rather than a recommendation.

[^fcc-telecommand]: [47 CFR § 97.211 – Space telecommand station](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97/subpart-C/section-97.211). Paragraph (b): "A telecommand station may transmit special codes intended to obscure the meaning of telecommand messages to the station in space operation." This is an explicit exception to the general prohibition in §97.113(a)(4) on messages encoded to obscure their meaning. Other administrations treat telecommand separately to varying degrees; check your own licence conditions rather than generalising from this one.