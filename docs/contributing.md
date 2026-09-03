# Contributing

## Add Resources
Thanks for helping improve this collection of resources!

_CubeSat Resources_ is hosted on GitHub: https://github.com/buildacubesat/CubeSat-Resources

To add a resource:

1. Clone the repo
2. Pick the most appropriate markdown file
3. Add your link with a short description
4. Submit a pull request

Alternatively, if you don't want to use git, you can submit your resource via this form: [Google Forms](https://forms.gle/KbrwNRWWMJXiBpk96).

For problems with the site, [open an issue on GitHub](https://github.com/buildacubesat/CubeSat-Resources/issues).

### Citing Sources

Name up to three authors in full – first name and surname, as they publish – and beyond three, the first author in full and `et al.` The same form is used everywhere:

- **Reference list entries** (the `references/` pages) give authors, venue and year: `Jasper Bouwmeester, Martin Langer and Eberhard Gill, *CEAS Space Journal* 9(2), 2017`, or `Thyrso Villela et al., *International Journal of Aerospace Engineering*, 2019`.
- **Footnotes** on development pages add the title, the link and a sentence on exactly what the source supports: `Jasper Bouwmeester, Martin Langer and Eberhard Gill, "Survey on ..."`, or `Maximillian Holliday et al., "PyCubed: ..."`.

Please state whether a source is free to read – `Open access`, `Free PDF`, or `paywalled` – so nobody follows a link into a paywall unwarned. Where the same source is cited from more than one page, use the same footnote slug on each, so the pair stays greppable.

### House Style

- **Spelling:** US English (`behavior`, `center`, `optimize`, `program`, `license`). Direct quotations keep the spelling of their source.
- **Dashes and quotes:** a spaced en dash (` – `) is the sentence dash and the dash in resource entries; en dashes in numeric ranges (`30–35%`); straight apostrophes and quotation marks only; U+2212 for a minus sign in numbers (`−35 °C`).
- **Glossary links** on the first use of a term on a page: `[term](../references/glossary.md#anchor)`. Anchors are the heading text lower-cased, ASCII-folded, with punctuation removed and spaces as hyphens: `AX.25` → `#ax25`, `DoD (battery)` → `#dod-battery`.
- **Resource blocks** between `<!-- CSR-RESOURCES:START <id> -->` and `<!-- CSR-RESOURCES:END <id> -->` are synced from a separate source. Keep each entry on one line as ``- **[Title](url)** `Link` – Description`` (or `` `PDF` `` for a PDF), with no full stop at the end and an access marker last: `Free`, `Free PDF`, `Open access`, `Paywalled`, or a license such as `Open source (MIT)`. Block IDs are `dev-` or `ref-` followed by the page name.
- **Hard numbers** get a footnote (`[^slug]`) whose text says what the source supports and whether it is free to read; the same source cited from several pages uses the same slug on each.
- **Uncertainty:** where a claim could not be confirmed, leave an HTML comment – `<!-- NEEDS HUMAN VERIFICATION: what was tried and what would settle it -->` – rather than hedging in the prose.
- **Page openers:** the first paragraph of a development page says what the page covers and what it hands off to which other page; the hook comes second.
- **Headings are anchors.** Pages link into each other's headings, so do not rename a heading without updating every link to it.
- **Footers:** development pages end with `---` and the contributing line; references pages end with `---` and "Know a … that belongs here? Please [contribute](contributing.md)."

## Support This Project
If you are looking for a way to support _CubeSat Resources_ financially, leave a tip or become a member over at _Build a CubeSat_.

- [Patreon](https://bac.page/patreon)
- [Ko-fi](https://bac.page/kofi)
- [PayPal](https://bac.page/paypal-donate)
- [YouTube Channel Membership](https://bac.page/youtube-join)

## Contributors

Thanks to everyone who's helped improve this collection!

- Brett Muir, <https://www.cubesource.space/>
- Manuel Imboden, <https://buildacubesat.space/>