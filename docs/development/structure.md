# Structure

The structure forms the mechanical backbone of a CubeSat, supporting all subsystems and ensuring compatibility with deployers. This section covers standard CubeSat frames, custom designs, materials, fasteners, mounting strategies, and mechanical interfaces. It also includes deployable elements such as antennas, booms, and solar panels, along with the mechanisms and constraints involved in their reliable release. Structural analysis, tolerancing, and environmental resilience (e.g. vibration and thermal effects) are also addressed.

The structure is unusual among CubeSat subsystems in that most of its requirements come from outside the mission. The [deployer](../references/glossary.md#deployer) dictates the envelope, the launch vehicle dictates the loads, and both are fixed long before your design is finished. Getting the external interface right early is cheap; discovering at the fit check that your antenna protrudes 2 mm too far is not.

## Form Factors and the CubeSat Envelope

Every CubeSat is defined by two things: how many [U](../references/glossary.md#u-cubesat-unit) it is, and whose deployer it flies in.

The [CubeSat Design Specification](../references/glossary.md#cds) (CDS) Rev. 14.1 defines a 1U CubeSat as **100.0 × 100.0 × 113.5 mm**. The 13.5 mm of extra height in the Z axis is the part newcomers most often miss – a "10 cm cube" is a useful shorthand, not a dimension you can machine to. Larger form factors scale this base cell: a 3U is 100 × 100 × 340.5 mm, a 6U doubles the cross-section, and a 12U reaches roughly 226.3 × 226.3 × 366 mm.[^nasa-soa-structures] Several form factors also offer extra volume beyond the nominal envelope – the **[tuna can](../references/glossary.md#tuna-can)** space on 3U, 6U and 12U variants, commonly used for antennas, thrusters or radiators.[^nasa-soa-structures] Form factors up to 16U are routinely supported by commercial deployers, and the community's centre of gravity has drifted steadily upward – NASA's state-of-the-art survey notes the shift "from 1U to 3U, to include 6U and 12U" over the last decade.[^nasa-soa-structures]

### What the CDS actually requires

The parts of the CDS that constrain your mechanical design most directly:

- **[Rails](../references/glossary.md#rail)**: the four Z-axis edges that slide against the deployer. They must be at least **8.5 mm wide**, should have a surface roughness below **1.6 µm**, and should have edges rounded to a radius of at least **1 mm** (CDS §2.2.5–2.2.7).
- **Rail end contact**: the rail ends on the ±Z faces need a minimum **6.5 × 6.5 mm** contact area, because in a stacked deployer they bear against the neighbouring CubeSat (§2.2.8).
- **Rail engagement**: at least **75% of the rail** should be in contact with the deployer rails; up to 25% may be recessed (§2.2.9).
- **Protrusions**: components on the side faces shall not protrude more than **6.5 mm** normal to the plane of the rail (§2.2.3). This is the budget your solar cells, connectors, antennas and [standoffs](../references/glossary.md#standoff) all share.
- **Mass**: 2.00 kg for 1U, 6.00 kg for 3U, 12.00 kg for 6U (§2.2.10, Table 1). Rev. 14 raised the long-standing 1.33 kg/U figure to 2 kg/U, and a lot of older material still quotes the old number.
- **Materials and finish**: the structure should be aluminium alloy – typically 7075, 6061, 6082, 5005 or 5052 – and aluminium surfaces in contact with the dispenser rails **shall be hard anodised** to prevent [cold welding](../references/glossary.md#cold-welding) inside the deployer (§2.2.12.1, §2.2.13).
- **Deployment timing**: deployables must wait a minimum of **30 minutes** after the deployment switches are activated, and no RF signal may be generated or transmitted earlier than **45 minutes** after on-orbit deployment (§2.4.4–2.4.5).

<!-- CSR-RESOURCES:START dev-structure-specifications -->
- **[CubeSat Design Specification Rev. 14.1](https://static1.squarespace.com/static/5418c831e4b0fa4ecac1bacd/t/62193b7fc9e72e0053f00910/1645820809779/CDS+REV14_1+2022-02-09.pdf)** `PDF` – The baseline CubeSat mechanical and operational specification from Cal Poly SLO
- **[ISO 17981:2024 – Space systems: Cube satellite (CubeSat) interface](https://www.iso.org/standard/85136.html)** `Link` – International standard formalising the CubeSat interface
- **[NASA State of the Art in Small Spacecraft Technology – Structures, Materials and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)** `Link` – Annually updated survey of CubeSat structures, materials and mechanism technology
<!-- CSR-RESOURCES:END dev-structure-specifications -->

Since 2024 there is also an ISO standard covering the CubeSat interface, **ISO 17981:2024**, which brings the form factor into the formal international standards system alongside the Cal Poly specification.
<!-- NEEDS HUMAN VERIFICATION: ISO 17981:2024 definitely exists (confirmed via ISO, BSI and SIS catalogue entries) but the standard is paywalled and I could not read its scope directly, so I have deliberately not characterised what it covers beyond its title. Worth a sentence describing its actual scope if you have access. -->

### The launch provider always wins

The CDS is the common language, but it is not the contract. Your **[payload user guide](../references/glossary.md#payload-user-guide-pug)** (PUG) or deployer manual is, and where the two disagree, the deployer manual is what gets checked at the fit check.

Exolaunch's EXOpod Nova manual makes this explicit: *"if there is any conflicting information between the CDS and the Nova User Manual, the Nova User Manual takes priority."*[^exopod] The differences are not cosmetic. Nova allows **2.5 kg for a 1U, 7.0 kg for a 3U and 14 kg for a 6U** – meaningfully more generous than the CDS – and permits lateral protrusions of **25 mm for 1U–4U** and **39.5 mm for 6U and larger**, versus the CDS's 6.5 mm.[^exopod] A design that assumes CDS protrusion limits will work anywhere; a design that assumes Nova's will not.

Practical consequence: **pick your deployer family before you finalise the external geometry.** If you cannot, design to the CDS and treat every extra millimetre a specific provider offers as margin you have not spent.

## Frames and Primary Structure

### Buy or build

Most teams should buy. A commercial frame is a solved problem with [flight heritage](../references/glossary.md#flight-heritage), correct rail geometry and anodising already applied, and it removes an entire category of fit-check risk for a cost that is small next to a launch slot. EnduroSat, for instance, advertises over 590 structures in orbit across its product line.

Building in-house makes sense when the payload drives an unusual internal layout, when machining capacity is free (a university shop), or when the learning *is* the mission. It is a reasonable first project: a 1U frame is well within the reach of a competent 3-axis mill, and the tolerances that matter are few and clearly specified.

<!-- CSR-RESOURCES:START dev-structure-frame-suppliers -->
- **[ISISPACE CubeSat Structures](https://www.isispace.nl/product-category/cubesat-structures/)** `Link` – Modular CubeSat structures with multiple internal mounting configurations
- **[EnduroSat CubeSat Structures](https://www.endurosat.com/products-category/structures/)** `Link` – CubeSat frames from 1U through 16U with extensive flight heritage
- **[NanoAvionics CubeSat Structural Frame](https://nanoavionics.com/cubesat-components/cubesat-structural-frame/)** `Link` – 6U–16U frames in hard-anodised 7075-T7351 aluminium, tested to NASA GEVS
- **[Pumpkin Space Systems](https://www.pumpkinspace.com/)** `Link` – Sheet-metal and skeletonised CubeSat structures; originators of the CubeSat Kit and the PC/104-derived stack convention
<!-- CSR-RESOURCES:END dev-structure-frame-suppliers -->

NASA's state-of-the-art survey lists 2NDSpace, AAC Clyde Space, C3S Electronics, EnduroSat, GomSpace, NanoAvionics, Pumpkin Space Systems and ISISPACE as representative primary-structure suppliers, while noting the list "is not all-encompassing and does not constitute an endorsement."[^nasa-soa-structures] [SatSearch](https://satsearch.co/), [SatCatalog](https://www.satcatalog.com/) and [CubeSatShop](https://www.cubesatshop.com/) are the practical places to compare what is currently available.

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

**6061-T6** is the default for CubeSat frames: readily machinable, weldable, corrosion-resistant, and cheap. **7075-T73** (and the T7351 temper used by NanoAvionics) is stronger and stiffer, and is the alloy most deployer rails are made from – matching alloys on both sides of the sliding interface keeps thermal expansion behaviour predictable. The CDS also permits 6082, 5005 and 5052.

**Hard anodising is not optional on the rails.** Bare aluminium sliding against bare aluminium in vacuum can cold weld – the surface oxide that normally keeps two metal surfaces apart is absent, and the surfaces bond. A hard anodic coating (typically Type III) is both electrically insulating and hard enough to survive the deployer slide. Note that this creates a design tension: the same coating that prevents cold welding also breaks the electrical bonding path, so grounding must be handled deliberately through defined contact points rather than assumed through the frame.

### Non-metals and additive manufacturing

Polymer additive manufacturing has moved from jigs and fixtures into flight structures, though mostly for secondary rather than primary load paths. NASA's survey gives useful comparative figures:[^nasa-soa-structures]

- **PLA** – TRL 3–4, deflection temperature only ~55 °C. Fine for ground support equipment, marginal for flight.
- **ABS** – deflection temperature 100–106 °C, tensile strength 21–47 MPa; flown as deployed structures on KickSat-2.
- **PEI (Ultem)** – deflection temperature 153–212 °C, tensile strength 62–81 MPa. Low outgassing and dimensionally stable; the usual choice when a printed part has to be near optics.
- **Windform (SLS)** – deflection temperature 173–187 °C, tensile strength 48–84 MPa, with flight heritage on KySat-2, TANCREDO-1 and GPX-2.

The important caveat is that [TRL](../references/glossary.md#trl) attaches to a *part*, not a material: NASA notes it "depends on the material, the configuration of the actual part, the manufacturing process used, the postprocessing... the testing and qualification process, and many other factors."[^nasa-soa-structures] A printed bracket that flew on someone else's mission tells you very little about yours unless the process is the same.

Electrostatic discharge is a second constraint on polymers. Surface resistivity should sit between **10⁶ and 10⁹ ohms**; materials above 10¹² ohms accumulate charge.[^nasa-soa-structures]

### Outgassing

Anything non-metallic – adhesives, conformal coatings, cable ties, printed parts, tapes, potting compounds – outgasses in vacuum. The escaping volatiles condense on the coldest, most valuable surfaces available: optics, radiators, solar cells.

Materials are screened using **ASTM E595**, which measures **[total mass loss](../references/glossary.md#outgassing) (TML)** and **collected volatile condensable material (CVCM)** after 24 hours at 125 °C in vacuum. The widely used screening criteria are **TML ≤ 1.00%** and **CVCM ≤ 0.10%**.
<!-- NEEDS HUMAN VERIFICATION: The 1%/0.10% figures are the universally quoted screening criteria and are what the NASA outgassing database filters default to, but I could not find NASA stating them verbatim on an openly accessible page — the authority appears to be NASA-STD-6001B Test 7, which I could not read. Worth confirming against that document before treating the numbers as normative. -->

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

Alternatives exist. The **[LibreCube board specification](https://librecube.gitlab.io/standards/board_specification/)** defines a deliberately different open standard – 95.89 × 90.17 mm boards, two 52-pin headers, 16 mm board pitch, with component height limited to 8.76 mm above and 4.83 mm below – on the grounds that if the internal interface is going to be a convention anyway, it should at least be a documented one. Backplane and harness-based architectures are also used, particularly where a large payload dominates the internal volume.

### Mounting practice

- **Standoffs** carry both the mechanical load and, often, the electrical ground path. If the frame is anodised, the ground return has to be designed explicitly – through a dedicated bonding strap or a deliberately masked contact area.
- **Thermal coupling is a design choice made at the mounting interface.** A board bolted hard to the frame through metal standoffs is thermally coupled to it; the same board on nylon standoffs is not. Decide which you want per board rather than by default. See [Thermal](thermal.md).
- **Alignment-critical items** – star trackers, cameras, antennas – should reference the frame directly through dowel pins or machined features, not through a stack of tolerances. See [GNC – ADCS Integration Considerations](gnc.md#adcs-integration-considerations).
- **Plan for late access.** You will need to reach the [remove-before-flight pin](inhibits-hdrm.md#remove-before-flight-rbf-pins), the charge port and the debug connector after the satellite is fully assembled, and in some cases after it is inside the deployer. Locate them on an accessible face early; retrofitting an access port into a finished frame is miserable.

## Mass Properties and Centre of Mass

Mass is tracked by the [mass budget](systems-engineering.md#budgets-and-margins); *where* that mass sits is a structural requirement in its own right, and one that tends to be discovered late.

The CDS constrains the centre of mass relative to the geometric centre (§2.2.11, Table 2):

| Form factor | X | Y | Z |
|---|---|---|---|
| 1U | ±2 cm | ±2 cm | ±2 cm |
| 3U | ±2 cm | ±2 cm | ±7 cm |
| 6U | ±4.5 cm | ±2 cm | ±7 cm |

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
- **Booms** – for magnetometers (getting the sensor away from the spacecraft's own magnetic field), gravity-gradient stabilisation, or drag sails. NASA's Deployable Composite Boom work reports roughly 25% mass reduction versus metallic equivalents, with the ACS3 mission demonstrating 7 m booms extensible to 16.5 m.[^nasa-soa-structures]
- **Drag sails and deorbit devices** – increasingly common as end-of-life disposal requirements tighten. See [Qualification and Launch](launch.md#regulatory-requirements).

### Release mechanisms

The mechanism itself is covered in depth under [Inhibits and HDRM](inhibits-hdrm.md); from the structural side the questions are: what preload does the stowed configuration need, what carries that preload, and what happens to the released energy.

<!-- CSR-RESOURCES:START dev-structure-deployment-mechanisms -->
- **[DCUBED release actuators](https://www.dcubed.space/)** `Link` – Shape-memory-based nano release nuts and pin pullers for CubeSat deployables
- **[Oxford Space Systems AstroTube](https://oxford.space/)** `Link` – Deployable boom reaching TRL 9, first deployed on orbit from the AlSat-Nano 3U in 2016; AstroTube Max scales from 0.5 m to 15 m
<!-- CSR-RESOURCES:END dev-structure-deployment-mechanisms -->
<!-- NEEDS HUMAN REVIEW: DCUBED's site is confirmed live but publishes no mass, power or preload figures publicly, so the entry is descriptive only. -->

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

NASA's **[GEVS](../references/glossary.md#gevs)** (GSFC-STD-7000) provides the generalised levels most CubeSat teams work to in the absence of a specific launcher manifest. The component-level **qualification** level is **14.1 Grms for 2 minutes in each of three orthogonal axes**; the **acceptance** level sits 3 dB lower in PSD, which works out to almost exactly **10 Grms**.[^gevs][^nasa-soa-structures]

Real launchers are usually gentler than the GEVS envelope. EnduroSat publishes a Falcon 9-referenced [protoflight](../references/glossary.md#protoflight) level of **7.877 Grms for 1 minute per axis** alongside its 14.1 Grms batch-qualification campaign – a useful illustration that GEVS is a bounding envelope, not a prediction.[^endurosat-qual] Qualifying to GEVS means you are covered almost anywhere; qualifying to your actual launcher's levels means you are covered where you are actually going.

### Doing the analysis

- **Modal analysis first.** Find the first natural frequency and check it against whatever your launch provider requires. Note that deployer manuals are often unhelpful here – Exolaunch states that "modelling the dynamic behavior of a CubeSat-Deployer coupled system is challenging and not recommended for most missions,"[^exopod] which in practice means most teams demonstrate compliance by test rather than by analysis.
- **[Margin of safety](../references/glossary.md#margin-of-safety)** is the output that matters: MS = (allowable / (factor of safety × applied)) − 1, and it must be positive. Typical factors of safety for test-verified metallic structures are around 1.25 on yield and 1.4 on ultimate.
<!-- NEEDS HUMAN VERIFICATION: the 1.25 yield / 1.4 ultimate figures are the values I believe GEVS Table 2.2-3 gives for test-verified metallic structures, but the table did not render in the copy of GSFC-STD-7000A I could fetch, so I could not confirm them. Please check against the standard before publishing, or soften to "check the factors of safety in your applicable standard". -->
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
- **Thermal cycling as a fatigue driver.** In [LEO](../references/glossary.md#leo), a spacecraft sees an eclipse cycle every 90 to 120 minutes – roughly 5,500 thermal cycles per year. Joints, solder and bonded interfaces experience this as low-amplitude fatigue loading. Qualification campaigns compress this into a handful of cycles: EnduroSat's, for example, runs 8 cycles from −35 to +75 °C with 2-hour dwells at the extremes and ramp rates below 2 K/min.[^endurosat-qual]
- **The structure is a thermal element.** Conduction paths through the frame are frequently the dominant heat transfer mechanism inside a CubeSat. Structural and thermal design cannot be sequenced; they have to converge together. See [Thermal](thermal.md).

### Space environment

- **Atomic oxygen** erodes polymers and some coatings on ram-facing surfaces below roughly 600 km. Metals and most anodised surfaces are largely unaffected.
- **Radiation** matters far more to electronics than to structure, but it does embrittle some polymers and darken optical coatings over time.
- **Vacuum** drives the outgassing and cold-welding concerns already covered, and removes convection entirely from your thermal design.

---

👉 **Please consider [contributing](../contributing.md)!**

[^nasa-soa-structures]: NASA Small Spacecraft Systems Virtual Institute, [*State of the Art in Small Spacecraft Technology*, Chapter 6: Structures, Materials, and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) (revision dated 4 August 2026). Open access, updated annually, and the single best general-purpose survey of CubeSat structural technology – covering form factor dimensions and structural masses, additive manufacturing material properties and TRLs, deployable boom technology, and a representative (explicitly non-endorsing) list of commercial suppliers.

[^exopod]: Exolaunch, [*EXOpod Nova User Manual*, Rev. 1.2](https://exolaunch.com/documents/EXOpod_Nova_User_Manual_June_2024.pdf) (June 2024). Openly published deployer manual covering 1U–16U, with mass and centre-of-mass allowances, rail dimensions and protrusion limits. Section 1.2 states that where the manual conflicts with the CDS, the manual takes priority. A good example of the class of document that actually governs a CubeSat's mechanical design.

[^gevs]: NASA Goddard Space Flight Center, *General Environmental Verification Standard (GEVS)*, [GSFC-STD-7000](https://standards.nasa.gov/standard/gsfc/gsfc-std-7000). Table 2.4-3 gives the generalised random vibration test levels for components; the qualification level for components below 22.7 kg is 14.1 Grms, with acceptance levels 3 dB lower in PSD (≈10 Grms).

[^endurosat-qual]: EnduroSat, ["Space Qualification – Satellite Testing Program"](https://www.endurosat.com/space-qualification/). Publishes the actual test levels used for its qualification and protoflight campaigns, including the 14.1 Grms / 2 min per axis GEVS batch qualification, a Falcon 9-referenced protoflight level of 7.877 Grms / 1 min per axis, and thermal vacuum cycling parameters. Useful as a concrete worked example of what a CubeSat qualification campaign actually consists of.
