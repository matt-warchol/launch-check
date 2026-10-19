# Changelog

## 1.13.0 — 2026-10-19

- Added a top-result format check to SEO research and substantial page rebuild audits. Briefs now separate search intent from page format, cite inspected organic results, and explain why the proposed guide, table, calculator, template, or tool fits the visitor's task.
- Added format evidence to the report template and an illustrative brief image to the README. Uninspected results remain hypotheses.

## 1.12.0 — 2026-10-17

- Added `references/content-sites.md`: scheduled-publish triggers and link gating, build-time broken-link checks, Sources lists for legal/tax/platform claims, authorship without invented first-hand stories, audit-tool false positives, `lastmod` and overlap handling, and merge order for parallel PRs.
- SKILL.md links the module for sites with guides, articles or tools.

## 1.11.0 — 2026-10-17

- Added stack-aware automatic sitemap generation and post-publication Google Search Console/Bing Webmaster Tools submission checks.
- Clarified truthful `lastmod`, canonical-only URLs, IndexNow versus Google, and ChatGPT crawler controls.

## 1.10.0 — 2026-10-16

- Added `scripts/ui_layout_audit.py`: a Playwright layout audit (sideways scroll, cramped text in boxes, boxes stuck together, text overflow, tiny text, small tap targets at 390/768/1280 px) for built folders or live URLs.
- Technical SEO and launch checks now point to it; results are leads to confirm by eye, not proof.

## 1.9.0 — 2026-10-14

- Added a footer structure audit for existing and new sites: real company/contact/legal destinations, useful topic groups, link checks, and mobile/keyboard access.
- Made preserve-first recommendations and a concise proposed link map part of audit output and release review.
- Clarified that a footer Sitemap link and `llms.txt` are optional; XML sitemap discovery is checked separately.

## 1.8.0 — 2026-10-14

- Added a self-contained GitHub update workflow to the skill, including the source repository, branch, install locations, and “launch-skill” alias.
- Added a check/apply updater that backs up old installs, avoids downgrades, and leaves same-version local changes for review.
- Added repository guidance for Codex/ChatGPT and Claude Code, plus installation/update instructions.

## 1.7.0 — 2026-10-14

- Added IndexNow as the default notification setup for new public, search-discoverable websites built or launched with the skill.
- Added a publication-event workflow for new, changed, and removed pages, with native-integration detection, host-key verification, retries, and live evidence.
- Clarified that IndexNow acceptance is not indexing and does not replace Google sitemap/Search Console work.

## 1.6.0 — 2026-10-14

- Made the Is Agentic public-page report part of audit mode and added its copied, selected improvement prompt to the audit output.
- Added source URL, scan freshness, selected findings, and an evidence-checked fix list; unavailable prompts are reported rather than fabricated.
- Updated the audit instructions, report template, usage docs, and validation record.

## 1.5.0 — 2026-10-14

- Added a dedicated conversion audit module for messaging, CTA hierarchy, page flow, friction, trust, and search/AI readability.
- Added a scoped CTA inventory and evidence-based FIX / TEST / BUILD / MONITOR actions to the report template.
- Made text/HTML-only audits possible without claiming live behavior, measured uplift, or launch readiness; agency/B2B criteria apply only when relevant.
- Updated audit prompts, UI description, usage docs, and package validation while retaining the 1.4.0 legal-pages module.

## 1.4.0 — 2026-10-10

- Added a legal-pages module to each website build/launch: privacy, terms, and applicable GDPR notices.
- Added three original neutral, plain-language draft templates informed by the supplied Brainhub references; removed source-company and activity-specific assumptions.
- Added factual gap handling, operator identification, consent/footer integration, public verification, and safeguards against publishing unresolved placeholders.
- Updated README module bullets/prompts, launch guide, report evidence fields, and package validation.

## Launch-prompt reminder — 2026-10-10

- Included GA4 setup and receipt verification directly in the example launch prompt so analytics is not forgotten; other providers remain supported.

## 1.3.0 — 2026-10-10

- Added optional GA4 autopilot guidance for authorized property/web-stream setup, tagging, consent, events, and verified receipt.
- Added bullet-point checklists describing every mode and GA4 chat examples.
- Added analytics evidence fields, access-aware fallback, current Google documentation, and required resource validation.

## Documentation update — 2026-10-10

- Added chat commands, mode selection, concrete inputs, and expected outputs for all five modes.
- Distinguished skill invocation in agent chat from the separate Is Agentic terminal CLI.
- Linked the expanded examples from the website-launch guide; runtime instructions remain unchanged.

## 1.2.0 — 2026-10-10

- Added a landing-page build/launch module covering brief, copy, attributable proof, readability, conversion, release, and public verification.
- Added the official `npx is-agentic <domain>` workflow, JSON evidence, applicability-based priorities, cached-report handling, and production protocol checks.
- Added a website-launch usage guide and report fields for agent-readiness evidence.
- Updated skill discovery/UI metadata and package validation to include the new references.
- Retained existing research/audit boundaries; publishing and implementation still follow actual user authorization.

## 1.1.0 — 2026-09-29

- Renamed the skill from `web-app-launch-seo`/`launch-seo` to `launch-check` to reflect its broader SEO, privacy, security, SSL/TLS, analytics, and release-readiness scope.
- Promoted the release from candidate status to `1.1.0`.

## 1.0.0-rc.3 — 2026-09-29

- Added GDPR/UK GDPR and cookie/storage inventory and consent-flow checks.
- Standardized free-first SEO research around Google Trends and Google Keyword Planner.
- Added a preflight warning that Keyword Planner may require Google Ads setup and billing information.
- Added logo-to-home verification and Open Graph/Twitter link-preview checks.
- Added concrete fix ownership and a shorter founder-facing decision/action format.
- Reduced trademark/name output to a short note unless deeper clearance is requested.

## 1.0.0-rc.2 — 2026-09-29

- Added a mandatory capability preflight before research, audits, implementation, or external checks.
- Added setup gates for keyword volume, competitor metrics, domain status, trademark research, and other tool-dependent evidence.
- Added `NOT RUN — prerequisite unavailable` to distinguish known missing setup from an attempted but inconclusive check.
- Added a capability matrix to the report template and documented the first-run correction.

## 1.0.0-rc.1 — 2026-09-29

- Converted the supplied checklist into a named Agent Skill with frontmatter and Codex presentation metadata.
- Added scope selection, sourced keyword research, intent/page mapping, and explicit evidence states.
- Corrected FAQ/GEO, privacy, secret handling, build verification, and deployment assumptions.
- Added technical SEO, launch references, and a reusable report template.
- Added installation, review, validation, licensing-status, and publishing documentation.
- Preserved the original attachment and made no public deployment or repository submission.
