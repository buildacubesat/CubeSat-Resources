---
title: Notebook embed preview
hide:
  - navigation
  - toc
search:
  exclude: true
---

# Notebook embed preview

Temporary page, not in the navigation – a look at what embedded notebooks would be like on this site. Each section below holds the same URL the `App` link on [Tools – Engineering notebooks](development/tools.md#engineering-notebooks) opens: the marimo playground loading the file straight from `bac-utils` on GitHub, read-only, code hidden. Nothing is copied into this repository. A frame loads only when its section is opened; it runs Pyodide in the browser, so the first load takes a while.

!!! warning "Work in progress – planning estimates only"

    First-order figures for early mission planning, not validated against flight data or a qualified reference tool.

??? note "BAC Link Budget"

    Open outside the frame: [bac.page/molab-link-budget-app](https://bac.page/molab-link-budget-app) – editable notebook on molab: [bac.page/molab-link-budget](https://bac.page/molab-link-budget)

    <iframe
      src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-link-budget%2Fbac_link_budget.py&mode=read&show-code=false"
      title="BAC Link Budget"
      width="100%"
      height="1000"
      style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
      loading="lazy"
      allow="clipboard-write; fullscreen">
    </iframe>

??? note "BAC Optical Payload"

    Open outside the frame: [bac.page/molab-optical-pld-app](https://bac.page/molab-optical-pld-app) – editable notebook on molab: [bac.page/molab-optical-pld](https://bac.page/molab-optical-pld)

    <iframe
      src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-optical-payload%2Fbac_optical_payload.py&mode=read&show-code=false"
      title="BAC Optical Payload"
      width="100%"
      height="1000"
      style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
      loading="lazy"
      allow="clipboard-write; fullscreen">
    </iframe>

??? note "BAC Power Budget"

    Open outside the frame: [bac.page/molab-power-budget-app](https://bac.page/molab-power-budget-app) – editable notebook on molab: [bac.page/molab-power-budget](https://bac.page/molab-power-budget)

    <iframe
      src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-power-budget%2Fbac_power_budget.py&mode=read&show-code=false"
      title="BAC Power Budget"
      width="100%"
      height="1000"
      style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
      loading="lazy"
      allow="clipboard-write; fullscreen">
    </iframe>

??? note "BAC Orbital Lifetime"

    Open outside the frame: [bac.page/molab-orbit-lifetime-app](https://bac.page/molab-orbit-lifetime-app) – editable notebook on molab: [bac.page/molab-orbital-lifetime](https://bac.page/molab-orbital-lifetime)

    <iframe
      src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-orbital-lifetime%2Fbac_orbital_lifetime.py&mode=read&show-code=false"
      title="BAC Orbital Lifetime"
      width="100%"
      height="1000"
      style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
      loading="lazy"
      allow="clipboard-write; fullscreen">
    </iframe>

??? note "BAC Antenna Visualizer (demo)"

    Open outside the frame: [bac.page/molab-antenna-viz-app](https://bac.page/molab-antenna-viz-app) – editable notebook on molab: [bac.page/molab-antenna-viz](https://bac.page/molab-antenna-viz)

    <iframe
      src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-antenna-visualizer%2Fdemo%2Fbac_antenna_visualizer_demo.py&mode=read&show-code=false"
      title="BAC Antenna Visualizer (demo)"
      width="100%"
      height="1000"
      style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
      loading="lazy"
      allow="clipboard-write; fullscreen">
    </iframe>

What a production version would add, if we went this way: `height` tuned per notebook (the budgets are long – 1000 px still scrolls inside the frame), and a fallback link above each frame for browsers that block third-party frames – the "open outside the frame" line already does that here.
