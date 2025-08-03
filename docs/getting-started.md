# Getting Started

CubeSats are satellites in the nanosat class built around established design specifications (the CubeSat Design Specification, or CDS). The basic “1U” CubeSat is a 10×10×10 cm cube. These standardized form factors use common deployer hardware, which lowers the cost of development and launch, making access to space more attainable – even for small teams or individuals. It’s important to note that launch provider capabilities and requirements may deviate from the CDS and will ultimately determine the allowable volume and weight of the satellite.

This section is for those new to CubeSats or small satellite development. It gives you a broad overview of what CubeSats are, what goes into building one, and where to begin your journey.

## Where to Start

- [NASA's CubeSat 101](https://www.nasa.gov/sites/default/files/atoms/files/cubesat_101_508.pdf) is a great beginner-friendly overview of CubeSat design and mission planning, and a highly recommended starting point.
- The [CubeSat Design Specification (CDS)](https://www.cubesat.org/cubesatinfo), maintained by Cal Poly, provides the official framework for CubeSat form factors. Reading through it helps you understand the physical and operational constraints of a CubeSat mission.
- Check the [Wikipedia](https://en.wikipedia.org/wiki/CubeSat) page for some history and context.
- For a general intro to the New Space economy, [this course by EPFL on edX](https://www.edx.org/learn/economics/ecole-polytechnique-federale-de-lausanne-new-space-economy) is a good place to start.
- [Nano Avionic's CubeSat 101](nanoavionics.com/blog/cubesat-101-the-comprehensive-guide-to-understanding-satellite-technology) provides a brief, high-level overview.
- To keep up to date with the space economy and space research at large, subscribing to the [Orbital Index](https://orbitalindex.com/) is highly recommended.
- If you're building a company and looking to hire people, [Space Crew](https://spacecrew.com/) is a good place to start.
- Shameless plug: I am developing an open source CubeSat and documenting the process on YouTube. You may find this relevant: [Build a CubeSat Channel](https://www.youtube.com/@buildacubesat).

## Development Flow

CubeSat projects usually fall into one of two categories: either you have a specific goal to achieve in orbit (e.g. a business case), or you're part of an academic program where the learning process is just as important as the outcome. In either case, it’s important to think of all parts of a CubeSat mission holistically, as they are interdependent:

### Project Phases

- Feasibility Study
- Fundraising
- Mission Design and Development
- Launch Provider Procurement
- Flight Segment Design and Development
- Ground Segment Design and Development
- Mission Insurance Procurement (optional)
- Regulatory Approval
- Assembly, Integration and Testing
- Launch
- Operations

### Milestones
- [ ] Feasibility studies completed
- [ ] Funding is secured
- [ ] Preliminary Design Review (PDR) completed
- [ ] Critical Design Review (CDR) completed
- [ ] Flight/qualification hardware procured
- [ ] Flight/qualification hardware tested
- [ ] FlatSat testing completed
- [ ] Functional tests performed at system level
- [ ] Environmental tests performed at system level
- [ ] Launch service provider selected and contract signed
- [ ] Mission insurance policy secured (optional)
- [ ] All regulatory approvals granted
- [ ] Flight ready
- [ ] Launch opportunity is secured
- [ ] Launched
- [ ] Commissioned
- [ ] Entered Nominal Operations
- [ ] Passivated
- [ ] Deorbited

!!! note
    A full CubeSat development project typically takes 1-2 years or more from initial planning to launch and operations. That includes everything from prototyping and documentation to regulatory approvals and environmental testing. Most likely, **the process will not be linear**, and different aspects of your system will be in different stages.

If your CubeSat mission is result-oriented, you probably have a payload that needs to reach orbit and send data back. In that case, it's advisable to source a bus with flight heritage – i.e. structure and subsystems that have been flight-proven – from an established vendor. Check out [SatSearch](https://satsearch.co/) and [CubeSat Shop](https://www.cubesatshop.com/) for help with sourcing.

If your mission is process-oriented, you’re more likely to build a large portion of the flight segment yourself. This is absolutely feasible, but the process tends to be more iterative and may involve more work in integration, qualification, and testing. It’s common to build a FlatSat or engineering model first – a functional layout of all your subsystems on a testbench – for easier debugging and early verification.

## Launch Provider Procurement

Starting the process of finding a rideshare opportunity early will help you align with your launch provider’s requirements, avoid costly redesigns, and fully leverage their support offerings. The CDS provides a guideline, but the launch provider’s specifications always take precedence.

A common path to orbit is via a [SpaceX rideshare mission](https://www.spacex.com/rideshare), often coordinated through a launch services provider like [Exolaunch](https://exolaunch.com/).

Note: Once you’re booked on a mission, launch integration begins. You’ll need to meet all interface and safety requirements and typically deliver your flight hardware well in advance – anywhere from 1 to 6 months before liftoff. If your CubeSat isn’t ready, it simply won’t fly.

## Regulatory Approval

Regulatory approval depends on your location, your launch provider's location, and what you intend to do in orbit.

!!! warning
    Nothing on this site is legal advice. You will need to familiarize yourself with your countries legislation, rules and best practices around launching and operating a CubeSat.

### Radio Frequency Usage

The most common way to communicate with a CubeSat is via UHF in the 430–440 MHz band. Someone on your team must hold an amateur radio license (HAM) or a Commercial Operator License. This person is responsible for compliance with national and international regulations.

At a minimum, you’ll need authorization from your national regulatory body (e.g. the [FCC](https://www.fcc.gov/document/guidance-obtaining-licenses-small-satellites) in the USA). If you're using amateur bands, you’ll also need coordination through the [International Amateur Radio Union (IARU)](https://www.iaru.org/on-the-air/satellites/). Generally, either the IARU or your national regulator will handle coordination with the [International Telecommunication Union (ITU)](https://www.itu.int/en/ITU-R/space/support/smallsat/Pages/default.aspx). If you use non-amateur bands, you may have to file with the ITU directly.

If required approvals aren't in place by launch day, your CubeSat will not be allowed to deploy. Start the licensing process early.

### Remote Sensing

If you plan on performing Earth Observation (EO) with cameras or sensors, you may require a remote sensing license from a national body such as [NOAA](https://space.commerce.gov/regulations/commercial-remote-sensing-regulatory-affairs/licensing/) in the USA.

## Mission Operations

Once your CubeSat is deployed into orbit, you’ll begin the commissioning phase: acquiring the signal, establishing contact, and checking that all subsystems are operational. After that, your mission enters its operational phase – collecting data, sending commands, and maintaining the satellite. Plan time and resources for this part too: missions can last anywhere from a few months to several years, depending on your orbital lifetime and system performance.

## Communities & Learning Resources

- [CubeSat Resources](/topics/) – Head over to the main content to start learning.
- [r/CubeSats](https://www.reddit.com/r/CubeSats/) – Active Reddit community.  
- [SatNOGS](https://satnogs.org/) – Open-source satellite ground station network.  
- [Build a CubeSat Discord](https://discord.gg/yeusgM75ys) – Community focused on open-source hardware and software in CubeSat development.
- [NASA CubeSat Launch Initiative](https://www.nasa.gov/kennedy/launch-services-program/cubesat-launch-initiative) – If you are based in the USA, NASA may help you get your CubeSat launched.
- [ESA Fly Your Satellite!](https://www.esa.int/Education/CubeSats_-_Fly_Your_Satellite) – Resources, events and support for CubeSat devs based in an ESA member state.
