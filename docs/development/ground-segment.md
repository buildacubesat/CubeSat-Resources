# Ground Segment

This page covers everything on Earth that supports your CubeSat mission – ground stations, antennas, radios, tracking, decoding, commanding, automation and data handling – for both amateur and professional setups, from a SatNOGS station to a custom one.

The ground segment is the half of the mission that most CubeSat teams under-resource. A spacecraft you cannot hear is indistinguishable from one that failed, and the difference between a mission that returns data and one that does not is frequently on this side of the link. It is also the only half you can fix after launch.

## Ground Station Architectures

### The options

- **Your own single station.** Full control, no scheduling conflicts, no recurring cost, and the ability to debug the RF chain physically. The limitation is geometry: a single mid-latitude station sees a typical [LEO](../references/glossary.md#leo) CubeSat for roughly four to six usable [passes](../references/glossary.md#pass) a day, each lasting 5–12 minutes. That is on the order of 30–60 minutes of contact per day, and it is the fundamental constraint on your [data budget](systems-engineering.md#budgets-and-margins).
- **[SatNOGS](../references/glossary.md#satnogs).** An open, community-operated global network. Any station can be scheduled to receive your satellite, and the data lands in a public database. For an amateur-band mission this is transformative: you get near-global coverage for free, and other people's stations frequently hear your spacecraft before you do. The tradeoffs are that it is receive-only (you still need your own station to command), and that your telemetry is public – which for most open CubeSat missions is a feature.
- **Partner and institutional networks.** Reciprocal arrangements with other universities give you geographic diversity at the cost of coordination.
- **[Ground-station-as-a-service](../references/glossary.md#gsaas) (GSaaS).** Commercial networks sold per pass or per minute. KSAT operates over 100 3.7 m KSATLITE antennas across more than 15 sites and processed 1.5 million passes in 2023; ATLAS operates 34 ground stations with 51 antennas; AWS Ground Station offers 5.4 m apertures on pay-as-you-go per-minute billing with scheduling as late as 15 minutes before a contact, streaming data directly into cloud storage; Leaf Space runs a distributed network of 3.7–3.9 m antennas with API-driven autonomous scheduling.[^nasa-soa-ground]

### Choosing

The honest decision factors are frequency band, budget, and how much contact time the mission actually needs.

- **Amateur bands (UHF/VHF)** – build your own, and lean on SatNOGS. GSaaS providers largely do not serve these bands.
- **S-band and above** – a capable station becomes expensive quickly, and GSaaS starts to look economical, especially for a short mission.
- **High data volume** – the antenna size and G/T that make a high-rate link close are what commercial providers already own. NASA's survey gives representative figures: AWS at 16 dB/K [G/T](../references/glossary.md#gt) in S-band and 30.5 dB/K in X-band, ATLAS spanning 11.3–36.0 dB/K across 3.0–9.3 m apertures.[^nasa-soa-ground]

**Most missions end up hybrid**: a home station for commanding and daily health checks, SatNOGS for coverage and [beacon](../references/glossary.md#beacon) collection, and possibly a commercial pass or two for bulk downlink.

### Survey the site before you build it

Before committing to a location, sweep the bands you intend to use and record the noise floor. An urban or campus site can be 10–20 dB noisier than a rural one, and a single nearby switching supply, LED lighting installation or solar inverter can raise the floor across the whole UHF band. That figure goes straight into your [link budget](comms.md#link-budget) as receiver system noise, so measuring it early can be worth more than any component choice you make later.

Note also what is *intermittently* present – a pager transmitter or a nearby repeater that only appears at certain hours will not show up in a five-minute survey but will desensitise your front end during a pass.

### Evolution over a mission

Ground segment needs change shape over time. During **LEOP and commissioning** you want maximum coverage and staffed operations – this is when losing contact is most likely and most damaging. During **nominal operations** you want automation, because a human attending four passes a day for two years does not happen. Toward **end of life** you want the archive to be complete and the data published.

Build the automated path early. A ground segment that only works with a person driving it will quietly stop working a few months in.

## Antennas and RF Front-End

### Antenna choice

- **Omnidirectional / low-gain** – turnstile, Lindenblad, QFH, or a simple dipole. No tracking hardware, no pointing, always receiving. Gain is low, so this works for strong beacons and for missions with generous [link margin](../references/glossary.md#link-margin). An excellent starting point: a fixed antenna and an SDR will hear plenty of CubeSats.
- **Directional / high-gain** – Yagi, cross-Yagi, helical, or a dish. Much more gain, and therefore much more link margin, but requires a rotator and accurate tracking. Cross-Yagis with a phasing harness give switchable circular polarisation, which is what you want for a tumbling spacecraft.
- **Dishes** – necessary at S-band and above, where the wavelength makes reasonable gain achievable in a manageable aperture.

### Polarisation

A tumbling CubeSat's linearly polarised antenna presents a constantly changing polarisation angle to the ground. Against a linearly polarised ground antenna this produces deep, repeated fades – theoretically infinite loss at the cross-polarised moment. **Circular polarisation on the ground caps the mismatch loss at about 3 dB** regardless of the spacecraft's orientation, which is why almost every serious amateur satellite station uses circularly polarised antennas, and why switchable RHCP/LHCP is worth the extra relay.

### Front-end design

Receiver sensitivity is set by the first amplifier in the chain, so the ordering matters more than the component quality:

- **Mast-mounted LNA.** A [low-noise amplifier](../references/glossary.md#lna) at the antenna, before the feedline, is the single highest-value improvement to a marginal station. Feedline loss ahead of the LNA adds directly to the system noise figure; the same loss after it is nearly irrelevant.
- **Filtering.** Band-pass and SAW filters ahead of the LNA protect against strong out-of-band signals – pagers, broadcast, mobile – which will otherwise desensitise the receiver. In an urban RF environment this is not optional.
- **Feedline.** Use good coax and keep it short. At 437 MHz, cheap cable over a long run can cost several dB.
- **Gain staging.** Enough gain to overcome the SDR's noise figure, not so much that strong signals overload the front end. SDR dynamic range is usually the binding constraint.
- **Grounding and lightning protection** for anything on a mast.

See [Comms – Link Budget](comms.md#link-budget) for how these terms combine.

## Tracking and Pass Prediction

### Orbital data

Pass prediction needs a current orbit. [TLEs](../references/glossary.md#tle) from Space-Track or CelesTrak, propagated with [SGP4](../references/glossary.md#sgp4), are the standard source. Refresh them at least daily – accuracy degrades from roughly a kilometre near [epoch](../references/glossary.md#epoch) to tens of kilometres after a week or two, which is enough to point a narrow-beam antenna at empty sky.

**The identification problem after launch.** When a rideshare deploys dozens of CubeSats, they are initially catalogued as an unidentified cluster and take days to weeks to be resolved individually. During that window you track several candidate TLEs, listen on each, and use the Doppler signature and beacon content to work out which is yours. Plan for this: it is a normal part of LEOP, not an anomaly. See [GNC – Orbit Representation](gnc.md#orbit-representation-tles).

### Scheduling

- **Elevation mask.** Passes below about 10° elevation suffer long slant ranges, atmospheric loss and terrain obstruction. Setting a realistic mask based on your actual horizon avoids wasting time on passes that were never going to work.
- **Pass quality varies enormously.** A 5° maximum-elevation pass may give two usable minutes; an 80° overhead pass gives ten. Prioritise accordingly, and plan bulk downlink for high-elevation passes.
- **Conflicts** between multiple satellites, or between your commanding and someone else's, need managing once you are operating more than one thing.

### Doppler

A LEO satellite closes and opens range fast enough to shift the carrier significantly. At 437 MHz the total excursion across a pass is roughly **±10 kHz**, sweeping through zero at closest approach – and the rate of change is highest exactly then, at the moment of best signal.

- **Correction is mandatory** for anything but the widest-band modes. The standard approach computes the shift from the propagated orbit and continuously retunes the radio.
- **Correct the uplink too**, pre-compensating so the signal arrives at the spacecraft's expected frequency. Forgetting this is a classic reason a spacecraft that is being heard perfectly will not accept commands.
- Doppler is also **useful**: the shape of the Doppler curve identifies which object you are hearing, which is exactly what resolves the post-launch identification problem.

The flight side of the same problem – receiver capture range and oscillator stability, which determine whether the spacecraft can hear a corrected uplink at all – is covered in [Comms – Doppler, Oscillators and Acquisition](comms.md#doppler-oscillators-and-acquisition).

### Rotator control

**Hamlib** is the de facto standard interface layer, providing `rotctl`/`rotctld` for rotators and `rigctl`/`rigctld` for radios. Almost every tracking program speaks it, which means mixing a tracker from one project with a rotator from another generally works.

Practical points: check that rotator slew rate can keep up with a high-elevation pass (angular rate peaks near zenith and can exceed some rotators' capability); handle the **azimuth wrap** problem, where a pass crossing the 0°/360° boundary sends an unprepared rotator the long way round mid-pass; and set software end stops before you discover the mechanical ones.

## Telemetry Reception and Decoding

### The chain

RF → SDR → demodulation → deframing → forward error correction → packet parsing → telemetry values → storage and display. Each stage can fail quietly, so instrument all of them.

### Beacon vs. high-rate

- **Beacons** are low-rate, periodic, and designed to be receivable with minimal equipment. They are your primary health channel, and the thing SatNOGS stations worldwide will collect for you. Design the beacon to be decodable by strangers: a documented format and a published decoder mean the community can actually help.
- **High-rate downlink** is on-demand, needs a good link and often a directional antenna, and carries payload data.

### Register with SatNOGS before launch

This is a pre-launch deadline, not a nice-to-have. Stations can only be scheduled against a satellite that exists in the **SatNOGS DB**, with its transmitters, frequencies and modulation recorded. Do it before deployment and the network can start collecting your beacon from the first orbit; do it afterwards and you lose exactly the days when the data matters most and when you are least sure your spacecraft is alive.

The full sequence worth completing before launch:

1. **Register the satellite and its transmitters** in [SatNOGS DB](https://db.satnogs.org/), including frequency, mode and baud rate.
2. **Publish the beacon format**, so somebody other than you can interpret a frame.
3. **Contribute a decoder** to gr-satellites (see below).
4. **Set up a dashboard**, so received telemetry is visible without a database query.

Steps 3 and 4 can follow after launch if they have to. Step 1 effectively cannot.

### Decoding software

The single most useful piece of software in this space is **gr-satellites**, a GNU Radio out-of-tree module collecting telemetry decoders for most amateur satellites in orbit. It handles [AX.25](../references/glossary.md#ax25), the GOMspace NanoCom U482C and AX100 modems, CCSDS stack components, the AO-40 protocol used by FUNcube, and many satellite-specific formats – and it can reassemble files such as JPEG images and present telemetry as human-readable values. It is GPL-3.0 licensed.[^gr-satellites]

**SatDump** is the other broadly useful tool, handling a wide range of satellite data processing pipelines.

**Contributing a decoder for your own satellite to gr-satellites, and a dashboard to SatNOGS, is one of the highest-return things a CubeSat team can do.** It converts every SatNOGS station on Earth into a receiving station for your mission.

### Error correction and partial data

- **Forward error correction** – convolutional, Reed-Solomon, LDPC, or the concatenated schemes CCSDS specifies – buys several dB of coding gain, which is often the difference between a closing and a non-closing link.
- **Design for partial reception.** Short, independently decodable frames mean a corrupted frame costs you one frame, not the whole pass. Long frames with a single CRC are all-or-nothing.
- **Keep the bad frames.** Store raw IQ or at least raw demodulated bits. A frame that fails CRC today may be recoverable tomorrow when you understand the format better, and raw recordings are the only way to debug a decoder problem after the fact.
- **Multiple receptions of the same beacon** from different stations can sometimes be combined to recover a frame none of them got cleanly.

See also: [Flight Software](flight-software.md)

## Command Uplink

Uplink is the dangerous direction. Everything on this side can be redone; a bad command cannot.

- **Validate on the ground before transmitting.** Range-check arguments, verify the command is valid in the spacecraft's current state, and simulate the effect where possible. The ground software should make dangerous commands hard to send accidentally.
- **Arm-and-fire for anything irreversible** – deployments, mode changes with no automatic exit, anything touching the radio configuration. See [Flight Software – Commands](flight-software.md#commands).
- **Verify uplink Doppler correction** – see above.
- **Sufficient uplink power.** The link is asymmetric: your ground transmitter can be far more powerful than the spacecraft's, which is why uplink usually closes more easily. But the spacecraft's receive antenna is omnidirectional and possibly shadowed by its own structure.
- **Confirm, don't assume.** Require acknowledgement for every command, and never assume a command was received because you transmitted it.
- **Authenticate the command link.** An unauthenticated uplink means anyone with a transmitter and your published format can command your spacecraft – and your format is public, because it is in your IARU coordination and probably in a paper. Authentication (proving who sent a command) is distinct from encryption (hiding what it says), and it is the more important of the two here. Telecommand is also treated separately from ordinary amateur traffic by at least some regulators: in the US, a space telecommand station "may transmit special codes intended to obscure the meaning of telecommand messages to the station in space operation", which is an explicit carve-out from the general prohibition on obscured amateur communications.[^fcc-telecommand] Check your own administration's rule rather than assuming either way. The implementation belongs on the spacecraft – see [Flight Software – Commands](flight-software.md#commands).
- **Keep a manual path.** However automated operations become, retain the ability to hand-craft and send a single command.

## Data Handling and Archiving

- **Store raw first.** Archive the rawest form you can afford – IQ recordings if storage permits, raw frames as a minimum – before any parsing. Parsers have bugs and formats change; raw data lets you reprocess.
- **Database the parsed telemetry** with timestamps in a consistent time base, tagged with the receiving station and the decoder version. Time-series databases suit this naturally.
- **Discipline the station clock.** Run NTP (or better) on every machine that timestamps a received frame. Ground receipt time is what you correlate against the spacecraft's own clock when reconstructing an anomaly, and a station whose clock is minutes out silently corrupts that correlation – particularly across a distributed network where frames arrive from several stations. See [Flight Software – Timing](flight-software.md#timing-scheduling-and-timekeeping).
- **Dashboards.** A visualisation showing battery voltage, temperatures, mode and reset count over time is how anomalies are actually spotted. The [SatNOGS Dashboards](https://dashboard.satnogs.org/) collection is both a hosting option and a good source of ideas – see the examples in [CubeSat Missions](../references/missions.md).
- **Reproducibility.** Version the decoder and the calibration applied, so a value can be traced back to the raw frame that produced it.
- **Publish.** Open telemetry and open decoders are the reason the amateur satellite community can help you. They also make the mission useful to people who were not on the team, which for an educational mission is much of the point. See [Payload – Archiving and sharing](payload.md#archiving-and-sharing).
- **Back it up off-site.** Mission data that exists only on the lab machine has a well-documented tendency to be lost during a lab move.

## Automation and Operations

- **Automate the pass.** A scheduler that computes upcoming passes, positions the rotator, tunes with Doppler correction, records, decodes and ingests into the database – with no human present – is what makes a multi-year mission sustainable.
- **Alert on exceptions rather than reporting on everything.** A rule engine that notifies someone when battery voltage drops below a threshold, when the reset count jumps, or when a pass produces no frames is far more effective than a daily report nobody reads.
- **Trend analysis** across weeks and months is where slow degradation shows up – capacity fade, coating degradation, rising error rates. See [EPS – Using power telemetry](eps.md#using-power-telemetry).
- **Automate carefully in the uplink direction.** Automated downlink is low-risk; automated commanding needs conservative guard rails.
- **Handover and documentation.** University teams turn over completely every few years. Write the operations handbook, document every procedure, and record why decisions were made. See [Flight Software – Documentation and Maintainability](flight-software.md#documentation-and-maintainability).

## Testing and Validation

The ground segment must be finished and proven *before* launch, and it usually is not.

- **End-to-end RF testing.** Transmit from the spacecraft into an attenuator and a dummy load, receive with the real ground station chain. This validates the whole path, including the parts nobody thought about.
- **Simulate Doppler** in a loopback test by offsetting the transmit frequency, and confirm the tracking software follows it.
- **Rehearse passes** with the real timing constraints. Ten minutes is not long, and the first time you discover your procedure takes fifteen should not be in orbit.
- **Test the automation** against a real spacecraft on the bench, over days, unattended.
- **Verify the decoder against real modulated signals**, not just against synthetic test vectors.
- **Practise contingencies**: no signal at the expected time, a spacecraft in safe mode, a partial frame, an unexpected reset. See [AIT – Mission Simulation](ait.md#mission-simulation).

The most common early-operations failures are mundane: uplink Doppler not corrected, the antenna pointing at the wrong satellite from an ambiguous TLE, a decoder that was never tested against a real signal, and a rotator that ran into its end stops mid-pass.

## Regulatory and Operational Considerations

- **Licensing.** Operating a transmitter requires a licence. Amateur-band operation requires an appropriately licensed operator who takes responsibility for compliance; non-amateur bands require coordination through your national regulator and the [ITU](../references/glossary.md#itu). See [Qualification and Launch – Regulatory Requirements](launch.md#regulatory-requirements) and [Getting Started](../getting-started.md).
- **Amateur service constraints** typically include a prohibition on commercial use, a requirement that communications be open, and restrictions on obscuring the meaning of transmissions. Note that the last of these is not necessarily symmetric: telecommand to a space station is treated separately in at least some jurisdictions, including the US.[^fcc-telecommand] These constraints are not obstacles for an educational mission, but they shape the mission and must be understood before choosing the band.
- **Power and duty cycle limits** apply to your ground transmitter under your licence.
- **Coordination.** The [IARU](https://www.iaru.org/reference/satellites/) coordinates amateur satellite frequencies to avoid interference; going through this process is expected practice.
- **Written procedures.** Nominal and contingency operations documented well enough that someone who was not present at launch can execute them.
- **Handover between operators** needs a shared log – what was commanded, what was observed, what is outstanding. An operations log that everyone writes to is worth more than any single tool.

## Resources

### Hardware

<!-- CSR-RESOURCES:START dev-ground-segment-station-hardware -->
- **[SatNOGS Ground Station Hardware](https://wiki.satnogs.org/Build)** `Link` – Open-source reference designs for rotators, RF front-ends, and full ground-station builds; the Raspberry Pi and RTL-SDR v3 are the reference platform
- **[UniClOGS Ground Station](https://www.uniclogs.org/)** `Link` – Modular, open-source CubeSat ground-station hardware covering RF, tracking, and control
- **[AB1OC Ground Station](https://stationproject.blog/2013/03/19/amateur-radio-station-design-and-construction/)** `Link` – Detailed amateur radio station design and construction blog
- **[Bits and pieces of RF insights](https://www.notblackmagic.com/)** `Link` – Practical RF engineering notes and hardware experiments focused on real-world SDR use
<!-- CSR-RESOURCES:END dev-ground-segment-station-hardware -->

**Component classes worth knowing about:**

- **SDR receivers** (RTL-SDR, Airspy, LimeSDR, HackRF, Adalm-Pluto, USRP) – from very low-cost monitoring to full-duplex RF work. The RTL-SDR v3 is the SatNOGS reference radio and is entirely adequate to start with.
- **Low-noise amplifiers (LNA)** – mast-mounted LNAs are critical for UHF/VHF CubeSat downlinks with modest antennas.
- **Band-pass and SAW filters** – reduce out-of-band interference, especially important in urban RF environments.
- **Timing sources** (GPSDO, GNSS receivers) – accurate frequency and time references for Doppler correction and coherent reception.
- **Single-board computers** (Raspberry Pi, x86 mini PCs) – common platforms for headless Linux ground stations and remote SDR stacks.

<!-- CSR-RESOURCES:START dev-ground-segment-rotators -->
- **[SatNOGS Rotator v3](https://wiki.satnogs.org/SatNOGS_Rotator_v3)** `Link` – Open-source az/el rotator design, the SatNOGS reference rotator
- **[AntRunner](https://github.com/wuxx/AntRunner)** `Link` – Open-source az/el antenna rotator project
- **[SARCNET Satellite-Antenna Rotator Mk2a](https://www.sarcnet.org/mini-satellite-antenna-rotator-mk2.html)** `Link` – Compact DIY satellite antenna rotator design
- **[Discovery Drive](https://www.crowdsupply.com/krakenrf/discovery-drive)** `Link` – Commercial az/el rotator with open interfaces
- **[Yaesu G-5500DC](https://www.yaesu.com/product-detail.aspx?Model=G-5500DC)** `Link` – Widely used commercial az/el rotator with good Hamlib support
<!-- CSR-RESOURCES:END dev-ground-segment-rotators -->

### SDR & RF Software

<!-- CSR-RESOURCES:START dev-ground-segment-sdr-rf-software -->
- **[GNU Radio](https://www.gnuradio.org/)** `Link` – The de facto signal-processing framework for building custom CubeSat ground-station pipelines
- **[SatDump](https://www.satdump.org/)** `Link` – Generic satellite data processing software covering a wide range of downlink formats and pipelines
- **[gr-leo](https://gitlab.com/librespacefoundation/gr-leo)** `Link` – GNU Radio LEO space channel simulator from the Libre Space Foundation, for modelling a link before you have one
- **[Gqrx SDR](https://www.gqrx.dk/)** `Link` – Lightweight Qt SDR receiver, good for quick signal inspection and debugging
- **[SDRangel](https://www.sdrangel.org/)** `Link` – Advanced multi-channel SDR suite with plugins for satellites, decoding and control
- **[SDR++Brown](https://sdrpp-brown.san.systems/)** `Link` – Modern, modular SDR++ fork with good performance and active development
- **[CubicSDR](https://cubicsdr.com/)** `Link` – User-friendly SDR application well suited to learning and casual monitoring
- **[List of SDR Software and Hardware](https://github.com/Slayingripper/Linux-SDR)** `Link` – Community-maintained index of SDR tools and supported hardware on Linux
<!-- CSR-RESOURCES:END dev-ground-segment-sdr-rf-software -->

### Decoders

<!-- CSR-RESOURCES:START dev-ground-segment-decoders -->
- **[gr-satellites](https://github.com/daniestevez/gr-satellites)** `Link` – GNU Radio decoders for most amateur satellites in orbit, covering AX.25, GOMspace AX100/U482C, CCSDS and AO-40 protocols, with file reassembly and human-readable telemetry output (GPL-3.0)
- **[SatNOGS DB](https://db.satnogs.org/)** `Link` – Community database of satellite transmitters, telemetry formats and decoded data. Register your satellite and its transmitters here before launch
- **[SatNOGS Dashboards](https://dashboard.satnogs.org/)** `Link` – Grafana dashboards for current and past missions, and a hosting option for your own
<!-- CSR-RESOURCES:END dev-ground-segment-decoders -->

### Satellite Tracking & Visualization

<!-- CSR-RESOURCES:START dev-ground-segment-tracking-software -->
- **[Gpredict](https://github.com/csete/gpredict)** `Link` – Mature satellite tracking software with Doppler correction and Hamlib rotator support
- **[Look4Sat](https://github.com/rt-bishop/Look4Sat)** `Link` – Modern satellite tracker with a clean UI and Hamlib integration
- **[SkyRoof](https://ve3nea.github.io/SkyRoof/index.html)** `Link` – Windows-centric satellite tracker with advanced features
<!-- CSR-RESOURCES:END dev-ground-segment-tracking-software -->

### Rotator and Radio Control

<!-- CSR-RESOURCES:START dev-ground-segment-rotator-control -->
- **[Hamlib](https://hamlib.github.io/)** `Link` – The standard control layer for antenna rotators and radios, providing a consistent API across hardware. Supplies `rotctl`/`rotctld` for rotators and `rigctl`/`rigctld` for radios, and is what almost every tracking program speaks
<!-- CSR-RESOURCES:END dev-ground-segment-rotator-control -->

Built on top of Hamlib, and worth knowing about:

- **grotor** – simple GTK GUI frontend for Hamlib, useful for manual az/el control.
- **gr-rotator** – GNU Radio block enabling programmatic rotator control directly from signal-processing flows.
- **rotctld web frontends** – browser-based UIs exposing Hamlib rotator control for headless or remote stations.

### Web-Based & Remote SDR

<!-- CSR-RESOURCES:START dev-ground-segment-remote-sdr -->
- **[OpenWebRX](https://www.openwebrx.de/)** `Link` – Web-based SDR receiver ideal for remote access and shared ground-station setups
- **[Airspy](https://airspy.com/download/)** `Link` – Vendor-provided SDR software and tools with solid Linux support for Airspy hardware
<!-- CSR-RESOURCES:END dev-ground-segment-remote-sdr -->

### Integrated / Turnkey Systems

<!-- CSR-RESOURCES:START dev-ground-segment-turnkey -->
- **[SatNOGS Client](https://satnogs.org/)** `Link` – Fully open-source ground-station stack combining tracking, SDR, and rotator control
- **[DragonOS](https://cemaxecuter.com/)** `Link` – Ubuntu-based SDR Linux distribution bundling GNU Radio, drivers, and satellite tools
<!-- CSR-RESOURCES:END dev-ground-segment-turnkey -->

### Typical CubeSat Ground-Station Stack (Linux)

- **Tracking:** Gpredict or Look4Sat
- **Rotator:** Hamlib (rotctld)
- **RF:** GNU Radio + SDRangel / SDR++
- **Decoding:** gr-satellites or SatDump
- **Remote ops:** OpenWebRX or SatNOGS

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-ground]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 11: Ground Data Systems and Mission Operations](https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/) (revision dated May 2026). Open access. Source for commercial ground network scale (KSAT's 100+ 3.7 m KSATLITE antennas across 15+ sites and 1.5 million passes in 2023, ATLAS's 34 stations and 51 antennas, AWS's 5.4 m apertures), G/T figures by provider and band, achievable direct-to-Earth data rates, and GSaaS commercial models.

[^gr-satellites]: Daniel Estévez, [gr-satellites](https://github.com/daniestevez/gr-satellites). A GNU Radio out-of-tree module collecting telemetry decoders for most amateur satellites in orbit, begun in 2015. Supports AX.25, the GOMspace NanoCom U482C and AX100 modems, CCSDS stack components and the AO-40 protocol used by FUNcube, alongside many satellite-specific formats, with file reassembly and human-readable telemetry output. GPL-3.0 licensed.

[^fcc-telecommand]: [47 CFR § 97.211 – Space telecommand station](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97/subpart-C/section-97.211). Paragraph (b): "A telecommand station may transmit special codes intended to obscure the meaning of telecommand messages to the station in space operation." This is the US rule, and it is an explicit exception to the general prohibition in §97.113(a)(4) on messages encoded to obscure their meaning. Other administrations treat telecommand separately from ordinary amateur traffic to varying degrees; check your own licence conditions rather than generalising from this one.