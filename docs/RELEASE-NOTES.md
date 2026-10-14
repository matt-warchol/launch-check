# Launch Check — 1.7.0

Audit and launch landing pages with an evidence-based checklist, essential SEO, working conversion paths, and verified production delivery.

Version 1.7.0 adds IndexNow setup by default to new public sites intended for search discovery. The agent checks native CMS/host support first, then wires an eligible page-publish event or post-deploy hook when needed. It verifies the host key, initial notification, and later event-driven notification. Preview/private pages are excluded. IndexNow receipt is reported separately from actual indexing; Google sitemap and Search Console work remains separate.

Version 1.6.0 adds the Is Agentic browser report to public-page audits. The agent copies the selected **Prompt to improve** into the saved audit output, records the report URL and scan time, and turns applicable findings into a checked fix list. If the copy control is unavailable, the prompt remains explicitly unavailable; the JSON API and CLI findings are not passed off as copied text.

Version 1.5.0 adds a dedicated conversion audit: message and CTA consistency, page flow, buying friction, trust, and search/AI readability. It records each visible conversion CTA in the audited scope and groups actions into FIX / TEST / BUILD / MONITOR. The audit works from page text or HTML, while clearly reserving live behavior and outcome claims for checks with the required access and data. Agency/B2B criteria apply only when the actual audience warrants them.

This release adds landing-page and Is Agentic modules to the existing research, audit, implementation, and launch modes. The official `npx is-agentic <domain>` workflow records score and scan date, prioritizes applicable findings, handles cached reports, and verifies deployed endpoints directly. It avoids inventing developer interfaces or customer proof to raise an audit score.

The README and website-launch guide include usable prompts, installation/update instructions, publishing boundaries, and a founder-friendly release handoff. Existing installations must replace the entire skill folder to receive the update.

The skill remains instruction-based and uses its host's available tools. Package validation, manual scenario review, and an actual CLI smoke test are documented in [the validation record](VALIDATION.md). Independent agent evaluation, cross-host activation, ranking improvements, and post-release score improvements have not been established by this release.

Version 1.3.0 adds optional Google Analytics account/stream setup and verification, plus bullet-point descriptions of each mode. Google account provisioning and event receipt were not live-tested: no authenticated Analytics connector was available, and browser access was blocked by an unavailable security-policy check.

Version 1.4.0 adds neutral privacy/terms/GDPR templates and a legal-page checklist to website builds/launches. The supplied reference GDPR page is recruitment-specific; its context is not applied to general sites. Published text must use verified operator/data-flow facts. No live website policy was published, and no jurisdiction-specific legal approval or compliance certification was established by this release.
