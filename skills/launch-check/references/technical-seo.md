# Technical SEO and AI-search discoverability

Read for a public-page audit or implementation. Sample each distinct route/template, plus critical conversion and error routes. State sample coverage; do not imply a full crawl from a homepage check.

## Crawl, render, index

- Public landing pages should return the intended successful response and expose meaningful content and real link destinations. Compare the initial response with rendered content for JavaScript apps. Recommend server rendering or prerendering only when the current approach causes a demonstrated problem or serves an agreed requirement.
- Inspect robots meta tags and `X-Robots-Tag` as well as `robots.txt`, including hosting/CDN restrictions. `robots.txt` controls crawling; it is not a confidentiality mechanism. A crawler must fetch a page to see its `noindex`. Protect private routes with authentication and authorization.
- Choose the canonical public origin and consistent path conventions. Check canonical targets are intended, accessible URLs; align redirects, internal links, and sitemap entries. Do not canonicalize every page to the homepage. Treat canonicals as signals rather than guaranteed engine selection.
- Preserve useful existing URLs. For migrations, map old to new destinations with suitable permanent redirects and check for loops/chains. Missing pages need honest error status, not a successful response containing an error message.
- Sitemaps should contain intended canonical, indexable, successful public URLs, not previews, private pages, redirects, or errors. Use accurate `lastmod` values when available; do not rewrite every timestamp on every build. Large sites need the documented sitemap limits and indexing strategy checked.
- Link new pages from relevant discoverable pages using descriptive anchors. Address orphaned pages, internal broken links, and uncontrolled filter/query variants where they exist.
- For multiple languages/regions, validate locale-specific content and reciprocal `hreflang` relationships with appropriate canonicals. Apply this only when localized pages exist or are requested.

## Page content and metadata

Use the framework's existing head/metadata mechanism to avoid duplicate tags. Give each page a descriptive title, useful description, clear primary heading, logical structure, and meaningful content aligned with its search intent. Character counts are editorial heuristics, not guaranteed display limits or ranking rules. Social previews need correct absolute public image URLs and appropriate text, and should be checked for actual accessibility. Verify `og:title`, `og:description`, `og:image`, `og:url`, and an appropriate `twitter:card`; use a preview inspector such as [opengraph.xyz](https://www.opengraph.xyz/) when accessible, otherwise inspect the raw response and label the visual preview check unverified.

Check the global brand link: the upper-left logo/wordmark should link to the canonical homepage/main route, have an accessible name, and work on mobile and keyboard navigation. Report the actual href and whether it resolves successfully. If it is wrong, offer to fix the component or list the exact file/route change needed.

Use structured data only for entities and properties genuinely represented on the page. Distinguish valid Schema.org vocabulary from support for a specific engine's rich result. Never invent ratings, reviews, prices, or organization details to satisfy a validator. Validate syntax and use the relevant engine's testing tool where its feature is supported; record unavailable checks.

**FAQ update, checked 2026-09-29:** Google ended FAQ rich results on May 7, 2026 and removed the feature documentation in June. Do not recommend `FAQPage` for Google rich-result gains. Helpful visible FAQs can still serve visitors; use related markup only for a justified consumer/use case and current support.

## AI search / GEO

Use original evidence, precise product descriptions, useful explanations, attributable expertise, and sources for claims. Direct answers and tables are useful when they fit the reader's task; there is no universal format that earns AI citations.

For Google's AI search features, established SEO practices apply; special AI schema and `llms.txt` are not required. Treat any experiment as such, with an observable outcome. For other engines or assistants, check their current crawler documentation and distinguish search discovery from model-training controls. Preserve the owner's crawler preferences instead of silently allowing every bot.

Measure available referral traffic and conversions, and record any sampled AI answers with prompt, engine, locale, and date. Such samples are volatile observations, not a durable visibility score. Do not claim unavailable engine-specific reporting exists.

## Experience and verification

- Run the visual layout audit when the site can be rendered: `python3 scripts/ui_layout_audit.py --dir <build-folder> --paths / /pricing` (or `--url <public URLs>`). It opens each page at 390, 768 and 1280 px and flags sideways scrolling, text pressed against its box edge, boxes stuck together, text sticking out, text under 11 px and tap targets under 44 px. Treat output as leads: confirm each with a screenshot before reporting, and note false positives (honeypot fields, intentionally scrolling code blocks). Needs `pip install playwright && playwright install chromium`.
- Check mobile navigation, content overflow, forms, error states, keyboard operation, visible focus, labels, useful alternative text, and basic contrast. Automated accessibility checks do not establish full conformance.
- Inspect the main conversion from entry to meaningful success; a button click alone may not represent a completed signup/export/payment.
- Record performance tool, URL, date, device/network profile, and lab versus field data. Current Core Web Vitals targets are LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile, assessed for mobile and desktop. New sites may lack field data. A Lighthouse score does not prove field INP or a Core Web Vitals pass.
- After authorized deployment, inspect the public origin again: status, rendered content, canonical, robots directives, redirects, sitemap, key assets, and conversion. Preview configuration can differ from production.

## Primary references

Checked 2026-09-29. Recheck changing feature support when applying this guide.

- [Google indexing controls](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google Search updates: FAQ retirement](https://developers.google.com/search/updates)
- [Google AI search eligibility](https://developers.google.com/search/docs/appearance/ai-features)
- [Google AI optimization guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Core Web Vitals](https://web.dev/articles/vitals)
- [W3C accessibility first checks](https://www.w3.org/WAI/test-evaluate/preliminary/)
