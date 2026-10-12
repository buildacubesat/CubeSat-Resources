---
title: Notebook embed preview
hide:
  - navigation
  - toc
search:
  exclude: true
---

# Notebook embed preview

Temporary page, not in the navigation – a look at what an embedded notebook would be like on this site. The frame below is the same URL the `App` link on [Tools – Engineering notebooks](development/tools.md#engineering-notebooks) opens: the marimo playground loading `bac_link_budget.py` straight from `bac-utils` on GitHub, read-only, code hidden. Nothing is copied into this repository; the frame runs Pyodide in the browser, so the first load takes a while.

!!! warning "Work in progress – planning estimates only"

    First-order figures for early mission planning, not validated against flight data or a qualified reference tool.

<iframe
  src="https://marimo.app/gh/buildacubesat/bac-utils/main/e?embed=true&entrypoint=notebooks%2Fbac-link-budget%2Fbac_link_budget.py&mode=read&show-code=false"
  title="BAC Link Budget"
  width="100%"
  height="1000"
  style="border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px;"
  loading="lazy"
  allow="clipboard-write; fullscreen">
</iframe>

Open the same thing outside the frame: [bac.page/molab-link-budget-app](https://bac.page/molab-link-budget-app).

What a production version would add, if we went this way: one such page per notebook under *Development* or *Tools*, `height` tuned per notebook (the budgets are long – 1000 px still scrolls inside the frame), and a fallback link above the frame for browsers that block third-party frames.
