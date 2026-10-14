# Build and launch a landing page

Use for a new landing page or a launch of an existing one. Keep the existing brand, framework, host, and design unless the user requests a change. Next.js and Vercel are examples, not requirements. Use [technical SEO](technical-seo.md) and [launch guidance](launch.md) for their respective checks; do not repeat a full research or application audit for a simple marketing page.

## Brief and page

- [ ] Identify audience, problem, main benefit, differentiator, brand references, primary conversion, approved proof, and contact or booking destination. Confirm missing inputs only when they affect the work; do independent work meanwhile.
- [ ] Lead with a clear promise in simple language, explain how it works, and give one primary action. Section order and page count should fit the product, not a fixed template.
- [ ] Use real founder stories, attributable metrics, and approved photos or testimonials. Separate historical founder achievements from current product results. Do not invent customer logos, pricing, interfaces, or guaranteed outcomes.
- [ ] Make supporting content useful: FAQs, comparison with existing workflows, resources or docs only where they help users. Label demos/sample data and explain what their controls actually do.
- [ ] Preserve progressive enhancement: meaningful HTML and usable links without JavaScript. Use a clear H1 and sequential section headings; keep visible answers consistent with any structured data.

## Experience and conversion

- [ ] Inspect desktop and narrow mobile layouts for readable copy, overflow, spacing, contrast, keyboard focus, accessible names, and meaningful image alternatives. Use 16px as a body-copy starting point, then assess the actual font and layout. A CSS font-size assertion alone is not a visual pass.
- [ ] Keep microanimations subtle, honor reduced motion, and ensure content remains visible if animation scripts fail.
- [ ] Test the primary contact/booking/form path, brand link to home, navigation, downloads, and interactive examples. Distinguish a CTA click from an actual delivered lead or booking. Avoid sending real messages as a casual test without authorization.
- [ ] Verify metadata, canonical URLs, sitemap, robots, social image, real 404s, and applicable structured data using the linked SEO guidance. Check publicly served output as well as source files.
- [ ] When GA4 is selected, use [the Google Analytics module](google-analytics.md) to reuse/create its property and stream, add tagging and agreed events, and verify actual receipt.
- [ ] Verify privacy and measurement behavior in proportion to the actual integrations. An installed analytics package or enabled dashboard is not evidence of event delivery.

## Release

- [ ] Run [the legal-pages module](legal-pages.md): adapt privacy/terms and the applicable GDPR notice to actual operator/data flows, resolve publication facts, link from the footer/consent controls, and verify public routes.
- [ ] Prepare [IndexNow](indexnow.md) for each new public search-discoverable site: reuse native support or wire added/updated/deleted page events to a post-publish notification. Keep it inactive on previews.

- [ ] Inspect the working tree and correct repository, branch, package manager, build directory, hosting project/account, and environment. Keep credentials out of commits and reports. Run the project's actual build and relevant tests; add meaningful tests for changed behavior.
- [ ] Establish a preview and rollback route. Review the intended diff. Push and deploy only when authorized, honoring authorization already given.
- [ ] Verify DNS, custom-domain routing, HTTP-to-HTTPS behavior, certificate validity, and provider readiness. Do not assume SSL is ready because the host provisions it automatically.
- [ ] Run the [Is Agentic check](is-agentic.md) on the canonical public domain. Fix applicable essential failures first, then partial results and recommendations; verify the deployed responses directly and check report freshness.
- [ ] Repeat critical checks on production: conversion path, HTML/404 status, canonical and social metadata, sitemap/robots, images/downloads, telemetry, and any added Markdown/agent files. Local success does not prove production behavior.
- [ ] After an authorized launch, verify the IndexNow key and first accepted submission, then confirm a later publish event triggers the sender automatically. Report notification status separately from indexing.
- [ ] Compare the deployed version with the intended Git commit using available provider metadata. Record URL, commit, deployment, checks, remaining decisions, and rollback owner.

## Handoff

Use the [report template](../assets/report-template.md). Mark each applicable item PASS, FAIL, UNVERIFIED, NOT RUN, or N/A with environment and evidence. Do not convert a browser/tool block into a pass. Give a concise change summary, top remaining actions, and links to the repository and live site.

When Search Console access is available and submission is authorized, verify ownership and submit the sitemap. Otherwise give the owner the exact pending step. Suggest an early availability/conversion check and a later indexing review; create monitoring only if requested. Neither a launch nor an agent score guarantees indexing, rankings, or sales.
