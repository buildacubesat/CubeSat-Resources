# Structure

The structure is unusual among CubeSat subsystems in that most of its requirements come from outside the mission. The [deployer](../references/glossary.md#deployer) dictates the envelope, the launch vehicle dictates the loads, and both are fixed long before your design is finished. Getting the external interface right early is cheap; discovering at the fit check that your antenna protrudes 2 mm too far is not.

## Form Factors and the CubeSat Envelope

Every CubeSat is defined by two things: how many [U](../references/glossary.md#u-cubesat-unit) it is, and whose deployer it flies in.

The [CubeSat Design Specification](../references/glossary.md#cds) (CDS) Rev. 14.1 defines a 1U CubeSat as **100.0 × 100.0 × 113.5 mm**. The 13.5 mm of extra height in the Z axis is the part newcomers most often miss – a "10 cm cube" is a useful shorthand, not a dimension you can machine to. Larger form factors scale this base cell: a 3U is 100 × 100 × 340.5 mm, a 6U doubles the cross-section, and a 12U reaches roughly 226.3 × 226.3 × 366 mm.[^nasa-soa-structures] Several form factors also offer extra volume beyond the nominal envelope – the **[tuna can](../references/glossary.md#tuna-can)** space on 3U, 6U and 12U variants, commonly used for antennas, thrusters or radiators.[^nasa-soa-structures] Form factors up to 16U are routinely supported by commercial deployers, and the community's centre of gravity has drifted steadily upward – NASA's state-of-the-art survey notes the shift "from 1U to 3U, to include 6U and 12U" over the last decade.[^nasa-soa-structures]

### What the CDS actually requires

The parts of the CDS that constrain your mechanical design most directly:[^cds-rev14]

- **[Rails](../references/glossary.md#rail)**: the four Z-axis edges that slide against the deployer. They must have a minimum width of **8.5 mm** measured from the rail edge to the first protrusion on each face, should have a surface roughness below **1.6 µm**, and should have edges rounded to a radius of at least **1 mm** (§2.2.5–2.2.7).
- **Rail end contact**: the rail ends on the ±Z faces need a minimum **6.5 × 6.5 mm** contact area, because in a stacked deployer they bear against the neighbouring CubeSat's rails (§2.2.8).
- **Rail engagement**: at least **75% of the rail** should be in contact with the dispenser rails; 25% may be recessed (§2.2.9).
- **Protrusions**: no component shall protrude farther than **6.5 mm** normal to the surface from the plane of the rail (§2.2.3). This is the budget your solar cells, connectors, antennas and [standoffs](../references/glossary.md#standoff) all share.
- **Materials and finish**: aluminium 7075, 6061, 6082, 5005 and 5052 are the alloys typically used for both the main structure and the rails (§2.2.12.1), and any external aluminium surfaces in contact with the dispenser rails **shall be hard anodised** to prevent [cold welding](../references/glossary.md#cold-welding) within the dispenser (§2.2.13).
- **Deployment timing**: deployables must wait a minimum of **30 minutes** after the deployment switches are activated, and no RF signal may be generated or transmitted earlier than **45 minutes** after on-orbit deployment (§2.4.4–2.4.5). See [Inhibits and HDRM](inhibits-hdrm.md#timers-and-delayed-activation).

Mass is capped per form factor (§2.2.10, Table 1):

| Configuration | Maximum mass |
| :---- | ----: |
| 1U | 2.00 kg |
| 1.5U | 3.00 kg |
| 2U | 4.00 kg |
| 3U | 6.00 kg |
| 6U | 12.00 kg |
| 12U | 24.00 kg |

Rev. 14 raised the long-standing 1.33 kg/U figure to 2 kg/U, and a lot of older material still quotes the old number.

<!-- CSR-RESOURCES:START dev-structure-specifications -->
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – The baseline CubeSat mechanical and operational specification from Cal Poly SLO. Free PDF
- **[NASA State of the Art in Small Spacecraft Technology – Structures, Materials and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)** `Link` – Annually updated survey of CubeSat structures, materials and mechanism technology. Open access
<!-- CSR-RESOURCES:END dev-structure-specifications -->

### The launch provider always wins

The CDS is the common language, but it is not the contract. Your **[payload user guide](../references/glossary.md#payload-user-guide-pug)** (PUG) or deployer manual is, and where the two disagree, the deployer manual is what gets checked at the fit check.

Exolaunch's EXOpod Nova manual makes this explicit: *"if there is any conflicting information between the CDS and the Nova User Manual, the Nova User Manual takes priority."*[^exopod] The differences are not cosmetic. Nova allows **2.5 kg for a 1U, 7.0 kg for a 3U and 14 kg for a 6U** – meaningfully more generous than the CDS – and permits lateral protrusions of **25 mm for 1U–4U** and **39.5 mm for 6U and larger**, versus the CDS's 6.5 mm.[^exopod] A design that assumes CDS protrusion limits will work anywhere; a design that assumes Nova's will not.

Practical consequence: **pick your deployer family before you finalise the external geometry.** If you cannot, design to the CDS and treat every extra millimetre a specific provider offers as margin you have not spent.

## Frames and Primary Structure

### Buy or build

Most teams should buy. A commercial frame is a solved problem with [flight heritage](../references/glossary.md#flight-heritage), correct rail geometry and anodising already applied, and it removes an entire category of fit-check risk for a cost that is small next to a launch slot. EnduroSat, for instance, advertises "590+ CubeSat structures in orbit" across its product line.

Building in-house makes sense when the payload drives an unusual internal layout, when machining capacity is free (a university shop), or when the learning *is* the mission. It is a reasonable first project: a 1U frame is well within the reach of a competent 3-axis mill, and the tolerances that matter are few and clearly specified.

<!-- CSR-RESOURCES:START dev-structure-frame-suppliers -->
- **[ISISPACE CubeSat Structures](https://www.isispace.nl/product-category/cubesat-structures/)** `Link` – Modular CubeSat structures with multiple internal mounting configurations
- **[EnduroSat CubeSat Structures](https://www.endurosat.com/products-category/structures/)** `Link` – CubeSat frames from 1U through 16U with extensive flight heritage
- **[NanoAvionics CubeSat Structural Frame](https://nanoavionics.com/cubesat-components/cubesat-structural-frame/)** `Link` – 6U–16U frames in hard-anodised 7075-T7351 aluminium, tested to NASA GEVS
- **[Pumpkin Space Systems](https://www.pumpkinspace.com/)** `Link` – Sheet-metal and skeletonised CubeSat structures; originators of the CubeSat Kit and the PC/104-derived stack convention
<!-- CSR-RESOURCES:END dev-structure-frame-suppliers -->

NASA's state-of-the-art survey lists 2NDSpace, AAC Clyde Space, C3S Electronics, EnduroSat, GomSpace, NanoAvionics, Pumpkin Space Systems and ISISPACE among its representative primary-structure suppliers, while noting that "the list of organizations/companies in this chapter is not all-encompassing and does not constitute an endorsement from NASA."[^nasa-soa-structures] [SatSearch](https://satsearch.co/), [SatCatalog](https://www.satcatalog.com/) and [CubeSatShop](https://www.cubesatshop.com/) are the practical places to compare what is currently available.

### Construction styles

- **Monolithic / machined-from-solid frames**: a single milled aluminium body, sometimes with removable side panels. Stiff, dimensionally reliable, and easy to analyse, but expensive in machining time and awkward for late access to internal boards.
- **Skeletonised rail-and-rib frames**: four corner rails tied together by ribs or end plates. The most common commercial pattern. Lighter, cheaper, and the side faces stay open for solar panels and access.
- **Sheet-metal / folded frames**: cheap and light, but harder to hold tolerance on and generally less stiff. Pumpkin says it pioneered sheet-metal CubeSat structures back in 2000 and still offers both solid-wall and skeletonised versions, so the approach has genuine heritage – but it rewards good tooling.
- **Secondary structures**: an internal sub-assembly (a board stack or payload cage) built and tested separately, then dropped into the load-carrying frame. This is what ISISPACE means by "multiple mounting configurations", and it is a good pattern for keeping integration reversible.

For scale: commercial CubeSat primary structures average roughly **0.118 kg for a 1U and 1.84 kg for a 12U**.[^nasa-soa-structures] If your frame is far heavier than that, you are spending [mass budget](systems-engineering.md#budgets-and-margins) that the payload would rather have.

### Open-source designs worth reading

<!-- CSR-RESOURCES:START dev-structure-open-source-designs -->
- **[Build a CubeSat – bac-structure](https://codeberg.org/buildacubesat-project/bac-structure)** `Link` – Open structural designs for 1U–4U in aluminium 6061, with fastener, adhesive and manufacturing notes (CC BY-SA 4.0)
- **[BIRDS-3 CAD](https://github.com/BIRDSOpenSource/BIRDS3-CAD)** `Link` – CAD documentation for the BIRDS-3 1U satellite and its integration stand
- **[CAD_SUCHAI_II](https://github.com/spel-uchile/CAD_SUCHAI_II)** `Link` – Mechanical CAD for the SUCHAI-II 3U mission, including the structure assembly
<!-- CSR-RESOURCES:END dev-structure-open-source-designs -->

Reading a complete open design is the fastest way to understand what a structure package actually contains: not just a frame model, but fastener schedules, torque values, adhesive selections and assembly order. See also [CubeSat Missions](../references/missions.md) for the wider list of open-source projects.

## Materials and Manufacturing

### Aluminium alloys

**6061-T6** is the default for CubeSat frames: readily machinable, weldable, corrosion-resistant, and cheap. **7075-T73** (and the T7351 temper used by NanoAvionics) is stronger and stiffer, and is the alloy most deployer rails are made from – matching alloys on both sides of the sliding interface keeps thermal expansion behaviour predictable. The CDS also names 6082, 5005 and 5052 as alloys typically used.[^cds-rev14]

**Hard anodising is not optional on the rails.** Bare aluminium sliding against bare aluminium in vacuum can cold weld – the surface oxide that normally keeps two metal surfaces apart is absent, and the surfaces bond. A hard anodic coating (typically Type III) is both electrically insulating and hard enough to survive the deployer slide. Note that this creates a design tension: the same coating that prevents cold welding also breaks the electrical bonding path, so grounding must be handled deliberately through defined contact points rather than assumed through the frame.

### Non-metals and additive manufacturing

Polymer additive manufacturing has moved from jigs and fixtures into flight structures, though mostly for secondary rather than primary load paths. NASA's survey tabulates commercially available filaments; the ranges below are across every product listed for each material, so treat them as the spread of what you can buy rather than a specification:[^nasa-soa-structures]

- **PLA** – TRL 3–4, deflection temperature **50–55 °C**. Fine for ground support equipment, marginal for flight.
- **ABS** – deflection temperature **97–106 °C**, tensile strength **21–58 MPa**; flown as deployed structures on KickSat-2.
- **PEI (Ultem)** – deflection temperature **153–212 °C**, tensile strength **54–145 MPa**, the spread depending heavily on whether the grade is carbon-filled. Low outgassing and dimensionally stable; the usual choice when a printed part has to be near optics.
- **Windform (SLS)** – three grades listed (XT 2.0, RS, SP), spanning deflection temperature **173–187 °C** and tensile strength **48–85 MPa**, with flight heritage on KySat-2 and GPX-2.

Polycarbonate is absent from NASA's tables but worth knowing about, because one PC filament has been put through the qualification a CubeSat team would otherwise have to pay for itself. **Prusament PC Space Grade Black**, developed with TRL Space, is a carbon-filled polycarbonate with a heat deflection temperature of **137.6 °C** at 0.45 MPa and a tensile strength of **75 MPa** – above every ABS grade in NASA's table and in the same band as mid-range PEI. Its outgassing was measured by Aerospace & Advanced Composites GmbH to the ESA criteria at **CVCM 0.00%** and **RML 0.12%**, against limits of 0.10% and 1.0% (reported TML was 0.25%).[^prusament] It is also dissipative as printed, without post-processing, at a volume resistivity of **2.2 × 10⁶ Ω·cm** – six orders of magnitude below the threshold NASA says to avoid, and comfortably inside the range the flight-used Windform grades occupy.

That combination is unusual and worth being explicit about why: this is not a recommendation, and a filament passing a screening test is not a qualified part. What it does buy you is a starting point where the outgassing evidence already exists, on a material you can buy in 850 g spools and print on a desktop machine, rather than one that needs an industrial SLS bureau.

The important caveat is that [TRL](../references/glossary.md#trl) attaches to a *part*, not a material: NASA notes it "depends on the material, the configuration of the actual part, the manufacturing process used, the postprocessing... the testing and qualification process, and many other factors."[^nasa-soa-structures] A printed bracket that flew on someone else's mission tells you very little about yours unless the process is the same.

Electrostatic discharge is a second constraint on polymers, and the relevant quantity is volume resistivity. NASA's guidance is that dielectric materials above **10¹² Ω·cm** "should be avoided because charge accumulation occurs regardless"; the flight-used Windform grades sit around **10⁸ Ω·cm**.[^nasa-soa-structures]

### Outgassing

Anything non-metallic – adhesives, conformal coatings, cable ties, printed parts, tapes, potting compounds – outgasses in vacuum. The escaping volatiles condense on the coldest, most valuable surfaces available: optics, radiators, solar cells.

Materials are screened using **ASTM E595**, which measures **[total mass loss](../references/glossary.md#outgassing) (TML)**, **collected volatile condensable material (CVCM)** and **water vapour recovery (WVR)** after 24 hours at 125 °C in vacuum. NASA-STD-6016C sets the acceptance criteria, and the exact wording is worth having:[^nasa-std-6016]

- **CVCM ≤ 0.1%**
- **TML less WVR ≤ 1.0%** – note the subtraction. Many materials contain absorbed water, and losing it does not normally affect functionality, so the water is taken out of the mass-loss figure before the limit is applied. Screening against raw TML is stricter than the requirement and will reject materials that are actually compliant. Europe does the same bookkeeping under a different name: ECSS reports **recovered mass loss (RML)** as its own quantity, with the water already taken out, and sets the limit there – so an ESA-screened material quoting RML and a NASA-screened one quoting TML less WVR are being held to the same thing.

Two qualifications matter more than the numbers. The requirement applies to non-metallic materials exposed to space vacuum, **excluding** ceramics, metal oxides, inorganic glasses and cetyl alcohol fastener lubricants outside closed compartments. And it is a floor, not a ceiling: for materials with line of sight to contamination-sensitive surfaces – "windows, lenses, star trackers, solar arrays, radiators, and other surfaces with highly controlled optical properties" – NASA notes that more stringent treatment may be needed, which can mean tightening CVCM to **≤ 0.01%**, or characterising deposition directly with ASTM E1559 and an integrated vehicle model rather than relying on a screening pass at all. If you carry optics or a precision radiator, assume you are in that second category. A spacecraft with cryogenic optics is stricter again: there the WVR is *not* subtracted, because deposited water is exactly the problem.

Failing the CVCM limit is also not automatically fatal, which is worth knowing before you rule a material out. The remedy is **vacuum bakeout** of the assembled hardware, and the requirement carries exemptions that cover a good deal of what actually goes into a small satellite:[^nasa-std-6016]

- anything with an exposed surface area below **1.6 cm²**, unconditionally;
- materials **not near a critical surface**, with CVCM between 0.1 and 1.0% and an exposed area below **13 cm²**;
- materials that are unexposed, overcoated or encapsulated with approved materials;
- anything inside a sealed container leaking less than 1 × 10⁻⁴ cm³/s.

A bead of threadlocker, a conformal coating fillet or a cable tie usually falls inside the first exemption. Where bakeout is needed, ASTM E2900 is the recommended guide, and the temperature is chosen as the highest the hardware tolerates rather than a fixed value – baking at the E595 screening temperature of 125 °C can damage flight hardware. Re-run a functional bench test afterwards.

One scoping note, because it is easy to read all of this as law: NASA-STD-6016C is a NASA requirements document, and it binds you where NASA or ISS requirements flow down to your mission. On a commercial rideshare it is reference practice rather than a rule – good reference practice, and what most of the industry has converged on, but your launch provider's own materials requirements are what actually govern. See [Qualification and Launch](launch.md#documentation-checklist).

The **[NASA Goddard Outgassing Database](https://etd.gsfc.nasa.gov/capabilities/outgassing-database/)** holds E595 results for thousands of materials and is the first place to check before committing to an adhesive or a tape. Check it *before* you design the part, not after – substituting a compliant adhesive late usually means requalifying the joint.

## Fasteners and Assembly

CubeSats are almost entirely bolted assemblies, and fasteners are a disproportionate source of both mass and risk.

### Selection

- **Size**: M2.5 and M3 socket-head cap screws dominate. The Build a CubeSat structure package, for example, standardises on M3 socket-head screws to ISO 14579/14580 with ISO 4032 nuts and ISO 7092 washers.
- **Material**: A2 (304) or A4 (316) stainless is the normal choice – strong, non-magnetic enough for most purposes, and dimensionally stable. Titanium saves mass where it matters and reduces thermal conduction; aluminium fasteners are rarely worth the strength penalty.
- **Magnetic cleanliness**: avoid ferritic (400-series) stainless anywhere near magnetometers. Even "non-magnetic" austenitic stainless can become slightly magnetic after cold working. See [GNC](gnc.md#magnetometers).
- **Thread engagement**: aim for at least 1.5–2× the nominal diameter in aluminium. Where a joint will be opened and closed repeatedly during integration, use threaded inserts or helicoils rather than tapping the aluminium directly – the frame will outlast the threads otherwise.

### Keeping them done up

Launch vibration will undo anything that is merely tight. The options, roughly in order of how commonly they appear on CubeSats:

- **Liquid threadlocker** – Loctite 271 or Vibra-Tite VC-3 are common; VC-3 has the advantage of being pre-applied and repositionable, which suits hardware that gets disassembled during integration. Threadlockers are non-metallic and therefore an outgassing item: check the specific product against the NASA database.
- **Belleville / conical spring washers** – maintain preload as joints settle and as thermal cycling works against the clamp. Frequently specified for flight assemblies.
- **Staking** – a dab of qualified adhesive (3M 2216 and similar epoxies are common) bridging fastener head to substrate. Reliable and inspectable, but destructive to remove.
- **Prevailing-torque nuts** – effective, but nylon-insert (Nyloc) types are generally avoided for flight because the nylon outgasses and does not tolerate the temperature range.
- **Safety wire** – rare at CubeSat scale; the fasteners are usually too small to drill sensibly.

**Torque control matters more than torque value.** Use a calibrated torque driver, record the value applied to every fastener, and use the same value at every reassembly. An under-torqued screw loses preload and backs out; an over-torqued one strips an M3 thread in 6061 with very little warning.

### Vented volumes

Every enclosed volume must be able to vent during ascent, or the trapped air will try to burst it. Vented (drilled) screws, deliberate vent holes, and avoiding blind tapped holes with a sealed fastener are the standard answers. Check enclosures, potted assemblies and any payload housing specifically.

## Mounting and Mechanical Interfaces

### The PC/104-derived stack

The CDS specifies the outside of a CubeSat and says nothing about the inside. In that vacuum, the community converged on a **[PC/104](../references/glossary.md#pc104)**-derived board stack, popularised by the Pumpkin CubeSat Kit: boards roughly **90 × 96 mm** carrying a 104-pin stacking header, mounted on standoffs so that each board's connector mates with the one below.

The advantages are real – it is why almost every COTS CubeSat board you can buy uses it. Boards from different vendors physically stack; the bus is available at every level; and adding a subsystem is mechanically trivial.

The disadvantages are equally real, and worth knowing before you commit:

- **The pinout is not standardised.** The connector is common; what each pin carries is not. Two "PC/104 CubeSat" boards from different vendors will mate mechanically and may still be electrically incompatible. Always check pin assignments against each vendor's [ICD](../references/glossary.md#icd).
- **Access is serial.** Reaching the third board down means removing the two above it. Plan assembly order and debug access together.
- **Stack height accumulates.** Standoff length, connector mated height and component height all add up; see [Tolerancing and Stack-Up](#tolerancing-and-stack-up).

### Documented alternatives

Two efforts address the pinout problem from opposite directions, and neither changes the board footprint much.

The **LibreCube board specification** keeps a board of roughly the same **90 × 96 mm** size but replaces the single 104-pin header with **two 52-pin headers**, on a **16 mm board pitch**, with component height limited to **8.5 mm above and 4.5 mm below** the board. The point is not a different shape – it is that the pin assignments are written down and open, which is precisely what PC/104-derived CubeSat boards are not.

**ISO 17981:2024, "Space systems – Cube satellite (CubeSat) interface"**, published October 2024 by ISO/TC 20/SC 14, tackles the same gap from the standards side. It covers interfaces between components, the interface between the CubeSat platform and its mission payload, umbilical connectors used as access ports, and datasheet requirements for CubeSat components and platforms sold as commercial products. Note what it deliberately leaves alone: it **does not** cover the interface between the CubeSat and the deployer.[^iso17981] It is an internal-interface standard, not a replacement for or companion to the CDS's envelope – which makes it relevant here and nowhere else on this page.

<!-- CSR-RESOURCES:START dev-structure-internal-interface-standards -->
- **[LibreCube board specification](https://librecube.gitlab.io/standards/board_specification/)** `Link` – Open board and connector specification defining board size, two 52-pin headers, 16 mm pitch and component height limits, with a published pinout
- **[ISO 17981:2024 – Space systems: Cube satellite (CubeSat) interface](https://www.iso.org/standard/85136.html)** `Link` – International standard for CubeSat internal interfaces, platform-to-payload interfaces, umbilical connectors and commercial product datasheets. Explicitly excludes the CubeSat-to-deployer interface. Paywalled
<!-- CSR-RESOURCES:END dev-structure-internal-interface-standards -->

Backplane and harness-based architectures are also used, particularly where a large payload dominates the internal volume.

### Mounting practice

- **Standoffs** carry both the mechanical load and, often, the electrical ground path. If the frame is anodised, the ground return has to be designed explicitly – through a dedicated bonding strap or a deliberately masked contact area.
- **Thermal coupling is a design choice made at the mounting interface.** A board bolted hard to the frame through metal standoffs is thermally coupled to it; the same board on nylon standoffs is not. Decide which you want per board rather than by default. See [Thermal](thermal.md).
- **Alignment-critical items** – star trackers, cameras, antennas – should reference the frame directly through dowel pins or machined features, not through a stack of tolerances. See [GNC – ADCS Integration Considerations](gnc.md#adcs-integration-considerations).
- **Plan for late access.** You will need to reach the [remove-before-flight pin](inhibits-hdrm.md#remove-before-flight-rbf-pins), the charge port and the debug connector after the satellite is fully assembled, and in some cases after it is inside the deployer. Locate them on an accessible face early; retrofitting an access port into a finished frame is miserable.

## Mass Properties and Centre of Mass

Mass is tracked by the [mass budget](systems-engineering.md#budgets-and-margins); *where* that mass sits is a structural requirement in its own right, and one that tends to be discovered late.

The CDS constrains the centre of mass relative to the geometric centre (§2.2.11, Table 2):[^cds-rev14]

| Configuration | X | Y | Z |
| :---- | ----: | ----: | ----: |
| 1U | ±2 cm | ±2 cm | ±2 cm |
| 1.5U | ±2 cm | ±2 cm | ±3 cm |
| 2U | ±2 cm | ±2 cm | ±4.5 cm |
| 3U | ±2 cm | ±2 cm | ±7 cm |
| 6U | ±4.5 cm | ±2 cm | ±7 cm |
| 12U | ±4.5 cm | ±4.5 cm | ±7 cm |

Deployers care because an off-centre mass causes the CubeSat to bind or tumble on ejection, and imparts unwanted tip-off rates. Your [ADCS](../references/glossary.md#adcs) cares because a large offset increases gravity-gradient and aerodynamic disturbance torques that the magnetorquers then have to fight for the whole mission.

Practical handling:

- Track centre of mass in CAD from the first layout, not as a check before delivery. Batteries and payloads are dense and are exactly the things that move late in the design.
- Measure it on the real spacecraft. CAD densities are approximations, harnesses are never where the model says, and adhesives and conformal coating add unmodelled mass.
- Moments of inertia matter to [GNC](gnc.md) even where the deployer does not check them; export them from the same CAD model and keep them under version control alongside the mass budget.
- Balance mass is legitimate but is a last resort – it is mass that does nothing. Prefer relocating something heavy.

## Deployable Structures and Mechanisms

Deployables are where structural design gets genuinely risky. NASA's survey is blunt about it: **mechanisms account for more than 10% of reported small satellite failures**, and its recommended mitigations are unglamorous – "design simplicity, margin, supplier selection, and testing."[^nasa-soa-structures]

### Common deployables

- **Antennas** – tape-spring UHF/VHF monopoles and dipoles are the most common deployable on any CubeSat, usually held by a burn wire and released after the mandated 30-minute delay. See [Comms](comms.md).
- **Solar arrays** – deployed panels multiply available area severalfold and are often the difference between a closing and a non-closing [power budget](eps.md#power-requirements-and-budgets). They also add stowed volume, a release mechanism, hinge stiffness questions and a new failure mode.
- **Booms** – for magnetometers (getting the sensor away from the spacecraft's own magnetic field), gravity-gradient stabilisation, or drag sails. NASA's Deployable Composite Boom work reports **25% less weight than metallic booms**, and states that the "DCB/ACS3 7-m boom technology is extensible to 16.5 m deployable boom lengths" following that mission's launch in April 2024.[^nasa-soa-structures]
- **Drag sails and deorbit devices** – increasingly common as end-of-life disposal requirements tighten. See [Qualification and Launch](launch.md#space-debris-mitigation).

### Release mechanisms

The mechanism itself is covered in depth under [Inhibits and HDRM](inhibits-hdrm.md); from the structural side the questions are: what preload does the stowed configuration need, what carries that preload, and what happens to the released energy.

<!-- CSR-RESOURCES:START dev-structure-deployment-mechanisms -->
- **[DCUBED release actuators](https://www.dcubed.space/)** `Link` – Shape-memory-based nano release nuts and pin pullers for CubeSat deployables
- **[Oxford Space Systems AstroTube](https://oxford.space/)** `Link` – Deployable boom reaching TRL 9, validated on orbit in November 2016 on the AlSat-Nano 3U mission; AstroTube scales 0.3–3 m and AstroTube Max 0.5–15 m
<!-- CSR-RESOURCES:END dev-structure-deployment-mechanisms -->

NASA's survey additionally lists Beyond Gravity, Comat, DHV Technology, Ensign-Bickford, Sierra Space and Revolv Space as mechanism suppliers, and Composite Technology Development and Redwire as boom suppliers.[^nasa-soa-structures]

### Design rules that earn their keep

- **Deploy it hundreds of times on the ground.** Deployment mechanisms are one of the few things you can test to statistical confidence cheaply. Do it, and do it after vibration, not only before.
- **Gravity lies.** A mechanism that deploys reliably on a bench may be relying on gravity to help or being hindered by it. Test in the orientation that is hardest, and use gravity offloading where the geometry allows.
- **Strain-relieve everything that crosses a hinge.** Harness routed across a deployable is a classic single-point failure. Give it a service loop, secure it on both sides of the joint, and check the bend radius through the full range of motion.
- **Decide what happens if it does not deploy.** A satellite that survives a failed solar array deployment in a reduced-power safe mode is a partial success. One that browns out is not. See [Flight Software – FDIR](flight-software.md#fault-detection-isolation-and-recovery-fdir).

## Structural Analysis and FEM

[Finite element analysis](../references/glossary.md#finite-element-analysis-fea) on a CubeSat has a narrow and achievable purpose: show that the spacecraft survives launch without shedding parts, and that it does not interact badly with the launch vehicle.

### Load cases

- **[Quasi-static loads](../references/glossary.md#quasi-static-load)** – the steady acceleration envelope during ascent, taken from the launcher's user guide. Simple to apply and usually not the driving case for something as small and stiff as a CubeSat.
- **[Random vibration](../references/glossary.md#random-vibration)** – the driving case for most CubeSat hardware. Applied as a power spectral density and characterised by an overall **[Grms](../references/glossary.md#grms)** value.
- **Shock** – from stage separation and deployer actuation. Rarely sizing for the primary structure, but relevant for crystals, relays and optics.
- **Acoustic** – generally not sizing at CubeSat scale, where surface area is small.

NASA's **[GEVS](../references/glossary.md#gevs)** (GSFC-STD-7000A) provides the generalised levels most CubeSat teams work to in the absence of a specific launcher manifest. Its component-level table specifies a flat **0.16 g²/Hz from 50 to 800 Hz**, rolling off at ±6 dB/octave to 0.026 g²/Hz at 20 Hz and 2000 Hz, giving an overall **14.1 Grms** for qualification. The acceptance level is the same shape at half the spectral density – 3 dB down – for an overall **10.0 Grms**. Qualification is run for **2 minutes in each of three orthogonal axes**.[^gevs]

Real launchers are usually gentler than the GEVS envelope. EnduroSat publishes a Falcon 9-referenced [protoflight](../references/glossary.md#protoflight) level of **7.877 Grms for 1 minute per axis** alongside its 14.1 Grms GEVS batch-qualification campaign – a useful illustration that GEVS is a bounding envelope, not a prediction.[^endurosat-qual] Qualifying to GEVS means you are covered almost anywhere; qualifying to your actual launcher's levels means you are covered where you are actually going.

### Doing the analysis

- **Modal analysis first.** Find the first natural frequency and check it against whatever your launch provider requires. Note that deployer manuals are often unhelpful here – Exolaunch states that "modelling the dynamic behavior of a CubeSat-Deployer coupled system is challenging and not recommended for most missions,"[^exopod] which in practice means most teams demonstrate compliance by test rather than by analysis.
- **[Margin of safety](../references/glossary.md#margin-of-safety)** is the output that matters: MS = (allowable / (factor of safety × applied)) − 1, and it must be positive. **Check which load case you are applying the factor to**, because GEVS does not use one number: for metallic structures the factors are **1.25 on yield and 1.4 on ultimate for static and sine loads, but 1.6 and 1.8 for random and acoustic loads**.[^gevs] Since random vibration is the driving case for most CubeSats, the higher pair is usually the one that applies. Composite structures and bonded inserts carry 1.5 on ultimate for static and sine, 1.9 for random and acoustic.
- **Model the stack, not just the frame.** For a CubeSat, most of the mass is boards, batteries and payload. A frame-only model will give you a first mode far higher than reality. Represent boards as plates with realistic mass and standoff stiffness, or lump them as point masses at their mounting points.
- **Correlate to test.** An uncorrelated model is a hypothesis. After the first vibration campaign, compare predicted and measured modes and adjust. See [AIT – Environmental Testing](ait.md#environmental-testing).

### Toolchains

<!-- CSR-RESOURCES:START dev-structure-fem-tools -->
- **[FreeCAD](https://www.freecad.org/)** `Link` – Open-source parametric CAD with an integrated FEM workbench
- **[CalculiX](https://www.calculix.de/)** `Link` – Open-source three-dimensional structural finite element solver with Abaqus-like input syntax
- **[PrePoMax](https://prepomax.fs.um.si/)** `Link` – Open-source pre- and post-processor for CalculiX with a modern user interface
- **[Code_Aster](https://code-aster.org/)** `Link` – Open-source structural mechanics and thermomechanics solver developed by EDF
- **[Elmer FEM](https://www.elmerfem.org/)** `Link` – Open-source multiphysics finite element software
<!-- CSR-RESOURCES:END dev-structure-fem-tools -->

Commercial options – Ansys Mechanical, MSC Nastran/Patran, Siemens Femap, Autodesk Fusion's simulation environment – are what most launch providers' reviewers are used to seeing, and many are available under free or heavily discounted academic licences. For a CubeSat the deciding factor is usually which tool someone on the team already knows well enough to be confident in the results, not which solver is technically superior. See [Tools – Software Tools](tools.md#software-tools).

## Tolerancing and Stack-Up

The CDS gives tight tolerances on the features that touch the deployer: rail dimensions are specified to **±0.1 mm**, and Exolaunch quotes ±0.1 mm on rail width and ±0.5 mm on rail length for the Nova envelope.[^exopod] These are machining tolerances, not assembly tolerances, and that distinction is the whole subject.

Where teams get caught:

- **Accumulated stack height.** Six boards, seven sets of standoffs, connector mated heights and a lid: each with its own tolerance. Tolerances add across the stack, and an assembly that is nominally fine can be 1.5 mm too tall at the extremes. Do the stack-up arithmetic explicitly, worst-case first, and only then decide whether a statistical (RSS) treatment is defensible.
- **Anodising thickness.** Hard anodising grows the surface – roughly half the coating thickness is above the original surface. On a rail machined to nominal, that can push you out of tolerance. Machine undersize by the expected growth and confirm with your finisher.
- **Fasteners as a datum.** Clearance holes give the assembly somewhere between 0.2 and 0.5 mm of freedom in every joint. If a payload needs to be aligned better than that, it needs dowel pins or a machined register, not screws.
- **Deployables in the stowed state.** The envelope check that matters is the stowed one, with the deployable compressed against its restraint and the [harness](../references/glossary.md#harness) routed as flown.

Verification is mostly unglamorous measurement: calipers and a surface plate for a 1U, a CMM if you have access, and a **fit check in a test pod** as the definitive answer. Deployer providers supply test pods for exactly this – Exolaunch's TestPod, ISISPACE's equivalents, and the original Cal Poly [P-POD](../references/glossary.md#p-pod) lineage – and a fit check early in the programme is worth far more than a re-measured drawing.

## Cleanliness, Handling and Contamination

Structures work is dirty work, and the spacecraft it produces has to be clean.

- **Particulate contamination** from machining, drilling and deburring finds its way into connectors, mechanisms and optics. Deburr and clean parts before they enter the integration area, never after.
- **Molecular contamination** – skin oils, fingerprints, mould release, cutting fluid – degrades thermal coatings and optical surfaces and is much harder to remove than dust. Nitrile gloves for everything that will fly, without exceptions that erode over the course of a build.
- **Cleanliness levels** should be set by the most sensitive item aboard. An optical payload or a precision radiator may justify a controlled environment; a technology demonstration with no optics probably does not. Decide deliberately rather than by default.
- **Handling fixtures** protect the rails, which are both the most tolerance-critical and the most easily damaged surfaces on the spacecraft. A scratched or dinged rail is a fit-check problem.
- **Foreign object debris.** Every loose washer, offcut of wire and dropped screw is a potential short in orbit. Count fasteners in and out, and inspect before closing any volume you cannot reopen.

See [AIT – Mechanical Assembly](ait.md#mechanical-assembly) for the assembly-side practices.

## Environmental Considerations

### Launch

Launch is short, violent, and the only time the structure is genuinely loaded. Everything above – load cases, fasteners, deployable restraint – exists for those few minutes. The verification counterpart is covered under [AIT](ait.md#environmental-testing).

### Thermal

- **Differential expansion.** Aluminium expands roughly twice as much as steel and several times as much as FR4 across the same temperature swing. A long bolted joint between dissimilar materials will move, and either the fastener preload changes or something warps. Slotted holes, flexures and compliant washers are the usual answers.
- **Thermal cycling as a fatigue driver.** In [LEO](../references/glossary.md#leo), a spacecraft sees an eclipse cycle every orbit – for a typical 95-minute orbit, roughly **5,500 cycles per year**. Joints, solder and bonded interfaces experience this as low-amplitude fatigue loading. Qualification campaigns compress this into a handful of cycles: EnduroSat's, for example, runs 8 cycles from −35 to +75 °C with 2-hour dwells at the extremes and ramp rates below 2 K/min.[^endurosat-qual]
- **The structure is a thermal element.** Conduction paths through the frame are frequently the dominant heat transfer mechanism inside a CubeSat. Structural and thermal design cannot be sequenced; they have to converge together. See [Thermal](thermal.md).

### Space environment

- **Atomic oxygen** erodes polymers and some coatings on ram-facing surfaces below roughly 600 km. Metals and most anodised surfaces are largely unaffected.
- **Radiation** matters far more to electronics than to structure, but it does embrittle some polymers and darken optical coatings over time.
- **Vacuum** drives the outgassing and cold-welding concerns already covered, and removes convection entirely from your thermal design.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-structures]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 6: Structures, Materials, and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) (revision dated 4 August 2026). Open access, updated annually, and the single best general-purpose survey of CubeSat structural technology. Source for form factor dimensions and average structural masses (Table 6-1: 0.118 kg for a 1U, 1.84 kg for a 12U), the additive manufacturing filament tables (6-7 PLA, 6-8 ABS, 6-12 PEI, and the Windform SLS table), the 10¹² Ω·cm electrostatic discharge threshold, the deployable composite boom figures, the mechanism failure statistic, and a representative and explicitly non-endorsing list of commercial suppliers.

[^cds-rev14]: Cal Poly CubeSat Program, [*CubeSat Design Specification Rev. 14.1*](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf) (9 February 2022). Free PDF. Source for the rail geometry requirements (§2.2.5–2.2.9), the 6.5 mm protrusion limit (§2.2.3), the alloys typically used (§2.2.12.1), the hard anodising requirement (§2.2.13), the mass limits in Table 1 (§2.2.10), the centre of mass limits in Table 2 (§2.2.11), and the deployment and RF quiet periods (§2.4.4–2.4.5).

[^exopod]: Exolaunch, [*EXOpod Nova User Manual*, Rev. 1.2](https://exolaunch.com/documents/EXOpod_Nova_User_Manual_June_2024.pdf) (June 2024). Openly published deployer manual covering 1U–16U, with mass and centre-of-mass allowances, rail dimensions and protrusion limits. Section 1.2 states that where the manual conflicts with the CDS, the manual takes priority. A good example of the class of document that actually governs a CubeSat's mechanical design.

[^iso17981]: International Organization for Standardization, [*ISO 17981:2024 – Space systems – Cube satellite (CubeSat) interface*](https://www.iso.org/standard/85136.html), Edition 1, published 1 October 2024 by ISO/TC 20/SC 14. Covers interfaces between CubeSat components, the interface between the CubeSat platform and its mission payload, umbilical connectors serving as access ports, and datasheet requirements for CubeSat components and platforms offered as commercial products. It explicitly does not address the interface between CubeSats and deployers, and applies to CubeSats of all sizes. Paywalled; this description is taken from the published scope.

[^gevs]: NASA Goddard Space Flight Center, *General Environmental Verification Standard (GEVS)*, [GSFC-STD-7000A](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000). Table 2.4-3, "Generalized Random Vibration Test Levels, Components", specifies 0.026 g²/Hz at 20 Hz rising at 6 dB/octave to 0.16 g²/Hz from 50 to 800 Hz, then falling at 6 dB/octave to 0.026 g²/Hz at 2000 Hz, for an overall 14.1 Grms at qualification; the acceptance spectrum is half the spectral density throughout for an overall 10.0 Grms. Table 2.2-3, "Flight Hardware Design/Analysis Factors of Safety Applied to Limit Loads", gives metallic yield and ultimate factors of 1.25 and 1.4 for static and sine loads and 1.6 and 1.8 for random and acoustic loads, with composite and bonded-joint ultimate factors of 1.5 and 1.9 respectively. Revision A is the revision CubeSat practice and vendor qualification campaigns generally reference.

[^nasa-std-6016]: NASA, *Standard Materials and Processes Requirements for Spacecraft*, [NASA-STD-6016C w/Change 1](https://standards.nasa.gov/standard/nasa/nasa-std-6016), §4.2.3.6 "Thermal Vacuum Stability", requirement [MPR 95]. Requires non-metallic materials exposed to space vacuum – excluding ceramics, metal oxides, inorganic glasses and cetyl alcohol lubricants used on fasteners outside closed compartments – to be tested per ASTM E595-15, with acceptance at "≤0.1 percent collected volatile condensable materials (CVCM)" and "≤1.0 percent total mass loss (TML) less water vapor recovery (WVR)", the latter permitting a higher mass loss where it demonstrably affects nothing. Also sets out the stricter treatment for materials with line of sight to contamination-sensitive surfaces, including a ≤0.01 percent CVCM option and ASTM E1559 deposition characterisation, and notes that WVR is not subtracted where cryogenic optics are involved. Requirement [MPR 96] in the same section covers the remedy: hardware containing materials that fail the CVCM requirement, or containing unidentified materials, is vacuum baked, subject to exemptions for exposed areas below 1.6 cm², for materials away from critical surfaces with CVCM between 0.1 and 1.0 percent and exposed area below 13 cm², for unexposed, overcoated or encapsulated materials, and for sealed containers leaking less than 1 × 10⁻⁴ cm³/s. It recommends ASTM E2900 as the bakeout guide and cautions that baking at the ASTM E595-15 screening temperature of 125 °C may damage spaceflight hardware. Note that NASA-STD-6001 defines the test methods; 6016 is where the acceptance criteria live.

[^prusament]: Prusa Research, [*Prusament PC Space Grade*](https://prusament.com/materials/prusament-pc-space-grade/) material page and [launch article](https://blog.prusa3d.com/prusament-pc-space-grade-black_121877/). Carbon-filled polycarbonate developed with TRL Space. Heat deflection temperature 137.6 °C at 0.45 MPa, tensile strength 75 MPa, tensile modulus 3.7 GPa. Outgassing tested by Aerospace & Advanced Composites GmbH against the ESA criteria: TML 0.25%, CVCM 0.00%, RML 0.12%. Volume resistivity 2.2 × 10⁴ Ω·m (2.2 × 10⁶ Ω·cm) and surface resistivity 6 × 10⁷ Ω/sq, measured on printed samples without post-processing. Vendor-published, but the outgassing figures come from a third-party laboratory against a named standard, which is more than most filament datasheets offer.

[^endurosat-qual]: EnduroSat, ["Space Qualification – Satellite Testing Program"](https://www.endurosat.com/space-qualification/). Publishes the actual test levels used for its qualification and protoflight campaigns, including 14.1 Grms for 2 minutes per axis referenced to NASA GEVS GSFC-STD-7000A, a Falcon 9-referenced protoflight level of 7.877 Grms for 1 minute per axis, and thermal vacuum cycling of 8 cycles from −35 to +75 °C with 2-hour dwells and ramp rates below 2 K/min. Useful as a concrete worked example of what a CubeSat qualification campaign actually consists of.