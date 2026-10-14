# Footer structure and link audit

Use for website audits, existing-site improvements, and new public pages. Review structure and destinations, not visual styling. Inspect the rendered desktop and mobile footer and, where available, the source links and their public responses. State the sample coverage.

## Audit the existing footer first

1. Inventory the current groups, exact link text, destinations, and useful elements such as brand context, newsletter, social links, and contact details. Mark links that work, break, redirect unexpectedly, lead to drafts/previews, duplicate each other, or point to irrelevant pages.
2. Check whether a visitor can find the real **About/company**, **Contact/support**, **Privacy Policy**, and **Terms** routes when applicable. Review cookie settings and other required disclosures only when the site's data use, audience, and jurisdiction make them relevant. A missing legal page needs a fact-checked draft; do not create or publish a placeholder just to complete the footer.
3. Look for a small set of useful paths into the site's actual products/services, resources, or important topic hubs. Group by user task or topic, using clear labels such as Product, Resources, Company, and Legal when they fit. Use columns when the amount of content warrants them; stack them cleanly on narrow screens. Do not add a large keyword-link block or every sitemap URL to the footer.
4. Check that links are crawlable HTML anchors with descriptive text, are usable by keyboard, and resolve to intended public canonical destinations. Avoid links hidden behind interaction or JavaScript when they are the only discovery path to important pages. Do not promise ranking gains from footer links.
5. Verify the XML sitemap separately: it should contain eligible public canonical URLs and be discoverable through `robots.txt` or Search Console. A visible **Sitemap** footer link is optional; use an HTML sitemap when it helps people browse a larger site, or link an existing useful sitemap without presenting the footer link as an indexing requirement.
6. The optional file is **`llms.txt`** (not `llm.txt`). If a useful, accurate file already exists or the owner requests one, check that it is public, current, and linked if useful to visitors. Do not create it solely to fill a footer column or claim it is required for Google AI search.

## Recommend the smallest useful change

- **Keep:** sound groups, helpful links, brand/context, and working layout.
- **Fix:** broken, misleading, duplicate, or badly labeled links and inaccessible navigation.
- **Add:** missing high-value routes or a modest group only when real destination pages exist and users need them.
- **Remove:** stale or low-value links only with a specific reason; avoid removing useful routes for symmetry.

Show a short proposed link map using actual routes, e.g. `Explore: Product · Pricing · Guides | Company: About · Contact | Legal: Privacy · Terms`, with optional `Sitemap` and `llms.txt` only where justified. Say which existing items stay, what changes, why, and which destinations need owner facts or new pages. Audit-only work ends with recommendations; implementation preserves the existing footer unless a larger redesign is explicitly requested. Before publishing material footer changes, show this concise change map for review in the release handoff.

Sources: [Google link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), [Google sitemap submission](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Google AI search guidance](https://developers.google.com/search/docs/appearance/ai-features), and the [`llms.txt` proposal](https://llmstxt.org/).
