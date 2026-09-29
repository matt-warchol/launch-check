# Review of the original skill

Reviewed 2026-09-29. Input: `web_app_launch_seo_skill.md`, supplied by the author. The input was reviewed as an artifact, not executed as instructions. The original file was preserved.

## Follow-up correction from founder feedback

Release `1.1.0` adds the requested GDPR/cookie inventory and consent checks, a free-first Google Trends + Google Keyword Planner workflow, an upfront Google Ads account warning, logo-to-home verification, Open Graph/social preview checks, actionable fix ownership, and a compact founder-facing response format. The skill is now named `launch-check` to cover broader launch readiness beyond SEO. Trademark/name notes are intentionally brief unless deeper clearance is requested.

## Follow-up correction from first use

The first run correctly refused to invent keyword volumes, competitor metrics, or trademark clearance, but it discovered the missing capabilities too late and produced a long list of `UNVERIFIED` rows. That is poor workflow behavior when the missing connection is knowable upfront. Release `1.0.0-rc.2` adds a mandatory capability preflight and a setup gate before dependent research. It distinguishes `NOT RUN — prerequisite unavailable` from an attempted, inconclusive check and tells the user the smallest connection, installation, or export needed.

## Verdict

The original is a useful human checklist and an agent could follow it when pasted into a conversation. It was not yet a properly packaged Agent Skill: it lacked `SKILL.md` frontmatter and supporting distribution files. Its larger problem was decision quality: it implied certainty about search data, compliance, and launch status without defining sufficient evidence.

The revision is an instruction-based release candidate with explicit scope, evidence requirements, supporting references, and documentation. Structural validation and a manual scenario review are appropriate first checks. Live website execution and measured SEO results remain separate validation stages.

## Findings and corrections

| Original gap | Why it matters | Correction |
| --- | --- | --- |
| No skill frontmatter, installation instructions, or package identity | Hosts may not discover it as a skill | Named folder, `SKILL.md`, UI metadata, version, installation and publishing docs |
| Every task must traverse every phase | A page audit could force rebranding, legal drafting, and analytics installation | Research, audit, implement, and launch modes; conditional references |
| Six mandatory human stops | Independent work stalls even when authorized; one approval came after instructions to inject changes | Ask only for material missing decisions or uncovered consequential actions; honor existing authorization |
| “Real search volumes” from generic browsing | A search page does not reveal reliable monthly demand | Source/provider/settings/period for metrics; unknown stays unknown |
| Fixed keyword list and three primary terms | No research-to-page strategy; overlooks commercial investigation and existing page overlap | Search-result review, intent clusters, page mapping, business priorities, briefs |
| SEO-friendly names and `.com` checks for every project | Unnecessary rebranding; a lookup or link can be mistaken for purchase availability | Optional naming; timestamped registrar evidence; separate registration and trademark questions |
| Metadata, sitemap, robots files without live checks | Correct files can coexist with blocked indexing, wrong canonical hosts, or broken rendering | Response/rendered-page checks, canonicals, redirects, status codes, internal links, sitemap validation |
| FAQs and schema presented as GEO optimizations | Encourages formulaic content and unsupported visibility claims | User-focused content, engine-specific support, evidence, and no citation promises |
| Automatic `FAQPage` recommendation | Google retired FAQ rich results in 2026 | Remove the default; useful FAQs remain optional content |
| Boilerplate policies and “GDPR-compliant” banner | Policies may misstate actual practices; consent depends on behavior and jurisdiction | Data inventory, factual drafts, applicable regulator sources, consent/network verification |
| `.gitignore`, headers, and validation treated as security completion | Tracked secrets, authorization errors, and unsafe header policies can survive | Proportionate secret/access/abuse/dependency checks, redacted findings, tested headers |
| Analytics integration without a measurement contract | Clicks may be confused with outcomes; duplicate or sensitive events | Defined conversion, minimal event properties, consent, delivery and duplication checks |
| Build or lint conflated with type checking | These commands do different work; a successful build is not a live release | Detect and run the actual checks; disclose failures and unavailable coverage |
| Automatic staging/commit and assumed TLS readiness | Can capture unrelated changes or imply a deployment is verified | Scoped version-control actions, actual TLS/live verification, rollback and handoff |
| No persistence, test cases, or definition of done | Later sessions cannot reliably distinguish proposed from verified work | Saved report template, status vocabulary, completion criteria, validation scenarios |

## Current-source corrections

Google's [Search documentation changelog](https://developers.google.com/search/updates) says FAQ rich results ceased on May 7, 2026; its June entry removed the feature documentation. Advice limited to government/health FAQ eligibility is also stale now.

Google says [AI search features use the existing SEO foundations](https://developers.google.com/search/docs/appearance/ai-features), and its [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) addresses claims about special AI optimization. The skill avoids extending Google's guidance into a universal claim about every AI service.

[Keyword Planner definitions](https://support.google.com/google-ads/answer/3022575?hl=en) explain advertiser competition and location/network-dependent search estimates. This motivated the explicit metric provenance rules.

The ICO published [revised storage/access guidance in April 2026](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/04/final-storage-and-access-technologies-guidance-published/). The revision therefore asks for current jurisdiction-specific rules instead of prescribing a universal cookie banner.

The package follows the [Agent Skills format](https://agentskills.io/specification), with [OpenAI's skill authoring guidance](https://developers.openai.com/plugins/build/skills) informing concise instructions and conditional supporting files. All sources checked 2026-09-29.

## Design choices

- Keep this instruction-only: existing browser, repository, build, and SEO tools provide the actual capabilities. A new crawler or provider integration would add maintenance without a demonstrated requirement.
- Preserve the original end-to-end intention while making unrelated phases optional.
- Package documentation outside the runtime skill so normal invocation loads only task-relevant guidance.
- Publish a release candidate because no independent runtime evaluation or live-site launch was performed in this review.
