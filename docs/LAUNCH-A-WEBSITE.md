# How to launch a website with Launch Check

Version 1.8.0. This workflow turns a brief or an existing landing page into a tested production release. It works with the framework and hosting provider you choose; Next.js, GitHub, and Vercel were used for Armando but are not prerequisites.

## Choose a mode and where to type it

After installation, paste `$launch-check` followed by your request into the coding agent's **chat**, not your terminal. There are no `launch-check build` or `launch-check audit` shell subcommands. The agent infers the mode from the request.

- **Build landing page:** `$launch-check build a landing page for [product]. Prepare a preview; do not push or deploy.`
- **Research:** `$launch-check research SEO for [product] and [audience]. Do not change files.`
- **Audit:** `$launch-check audit [URL] for conversion and SEO. Audience: [buyer]. Primary action: [goal]. Do not change files.`
- **Implement:** `$launch-check implement these fixes: [list]. Preserve the design; do not push or deploy.`
- **Launch:** `$launch-check push the agreed changes to [repo/branch] and deploy to [host/project] at [domain]. Verify production and run Is Agentic.`

The [README has complete copy-paste examples for all five modes](../README.md#copy-paste-examples-for-every-mode). The terminal command `npx is-agentic [domain]` is a separate public audit tool, not the command to build or deploy a page.

## 1. Install or update

Follow the installation instructions in [the README](../README.md). Copy the entire `skills/launch-check` folder, including references and assets. Replace an existing installation rather than adding another copy with the same name. This repository update does not automatically update installations on other machines.

## 2. Give the agent a brief

Provide product name, audience, problem, benefits, differentiator, primary action and destination, brand references, approved proof/photos, repository, and preferred host/domain. Supply privacy/data-flow facts if the page collects data or tracks users. For an existing page, say whether visual design should be preserved.

```text
Use $launch-check to build a simple landing page for [product].
Audience: [who]. Main benefit: [benefit]. Differentiator: [why us].
Primary action: [action] linking to [destination].
Use these brand references and approved proof: [materials].
Repository: [repo]. Hosting: [project]. Domain: [domain].
Preserve the existing design where applicable. Prepare a preview and
run relevant tests. Do not push or deploy until I ask.
```

The agent checks only capabilities needed for this scope. Keyword metrics, new domain research, or a full application audit are not automatic requirements for a landing page. Missing credentials block only their dependent actions.

For a new public site intended for search discovery, the agent also prepares [IndexNow automatic notifications](../skills/launch-check/references/indexnow.md) in its actual CMS or deployment flow. They stay inactive on previews.

## 3. Review the page and checklist

Review the page's promise, benefits, proof, mobile readability, and main action. The [landing-page checklist](../skills/launch-check/references/landing-page.md) covers meaningful HTML, headings, subtle motion, downloads/forms, SEO, social previews, analytics delivery, and release settings. Do not approve claims or policies whose facts are still unknown.

For an existing page, the [audit module](../skills/launch-check/references/audit.md) inventories visible conversion CTAs and checks message consistency, page flow, friction, trust, and search readability. For a public URL, it also opens Is Agentic, copies the applicable **Prompt to improve** into the audit output, and maps its findings to fixes. It returns evidence-backed **FIX / TEST / BUILD / MONITOR** actions. Supply the intended audience and conversion goal; text or HTML is enough for a copy review, while live behavior and an Is Agentic scan need a public page. An audit alone does not change the site or establish launch readiness.

Ask the agent to resolve agreed issues and provide the preview URL, test results, pending decisions, and rollback route. Browser checks and HTTP checks are different evidence: blocked browser access must be disclosed.

## 4. Authorize delivery

```text
Push the agreed changes to [repository/branch] and deploy to
[hosting project] at [public domain]. Verify DNS, HTTPS, the deployed
version, and the main conversion path. Run the Is Agentic check and
fix applicable issues within the agreed landing-page scope.
Set up Google Analytics in [account/property] if selected; install
page-view and primary-action tracking and verify receipt. For a new
property use [time zone] and [currency].
Enable IndexNow for this public site and verify that a later new or
updated page sends a notification automatically.
```

Existing authorization does not need to be repeated. If the registrar or account requires your action, the agent should give the exact pending setup and continue independent work. A DNS record alone does not prove a working certificate or correct production site.

IndexNow needs a verified key on the production host unless the platform manages it. The agent checks the first accepted notification and the ongoing publish hook. `200` or `202` confirms receipt or pending key validation, **not indexing**. Keep the sitemap and Google Search Console checks; Google is not an IndexNow participant.

## 5. Run the public agent-readiness check

From a terminal with Node/npm and network access:

```bash
npx is-agentic example.com
```

To save the JSON evidence:

```bash
mkdir -p reports
npx is-agentic example.com --json > reports/is-agentic.json
```

Replace the example domain. Reports are public; use only public URLs. The [Is Agentic workflow](../skills/launch-check/references/is-agentic.md) explains freshness, failures, verification, and published protocol sources.

Work through applicable Essential failures first, then partial checks and Recommended findings. Do not create fictitious developer interfaces, addresses, testimonials, or policy facts just to improve a score. Follow current file formats and verify each public endpoint changed.

The CLI can return a report from before your deployment. Record `scanned_at` and compare it with release time; a second invocation may still return the same report. A stale score stays a baseline until a newer scan exists. Use direct production checks for immediate evidence and the service's supported rescan flow for a fresh report; do not claim a score improvement without one.

## Legal pages for every website launch

The module includes [neutral privacy/terms/GDPR templates and a checklist](../skills/launch-check/references/legal-pages.md). Ask the agent to adapt them to the website and its actual operator, then add footer and consent links. Reuse correct existing policies; a GDPR notice can be merged into the privacy policy where appropriate.

Provide the operator's legal name, address and relevant registration details, public/privacy contact, markets, and known data-processing facts. The agent inspects integrations and asks only for material unknowns: purposes, lawful bases, providers, retention, transfers, and actual consent controls. It does not copy Brainhub's identity, recruitment practices, provider list, or governing-law assumptions.

Draft first while missing facts are pending. Before an authorized publication, resolve placeholders, reconcile the documents with actual behavior, and test public routes, links, and consent controls. A site-specific draft is not legal-compliance certification. The [README has a complete legal-pages prompt](../README.md#add-legal-pages-to-a-website).

## Optional: set up Google Analytics automatically

Ask for the [GA4 autopilot workflow in the README](../README.md#google-analytics-on-autopilot). It works within Implement or Launch mode when you select Google Analytics; it is not mandatory for every website.

Supply the selected Analytics account/property, canonical URL, and event goals. For a new property, also supply the name, reporting time zone, and currency. Authorize property/stream creation and website deployment if you want the full setup. With account access, the agent checks for duplicates, reuses or creates the correct property/web stream, retrieves the measurement ID, adds tagging, and verifies events and consent.

If account access is unavailable, follow the [manual fallback](../skills/launch-check/references/google-analytics.md#manual-fallback-for-the-owner) and share the public `G-…` ID. Never share passwords, keys, or OAuth tokens in chat. Tag installation and property receipt are reported separately; a browser/network block must remain explicit.

## 6. Get a launch handoff

Request a concise summary with:

- Live URL, Git commit, hosting deployment, and rollback route.
- Build/tests, browser conversion checks, metadata/social assets, DNS/HTTPS, and analytics delivery results.
- Is Agentic score and scan date, applicable issues, fixes, and current versus stale evidence.
- Remaining credentials or product decisions, with an owner and next action.
- Search Console/sitemap submission status and a proposed indexing/conversion follow-up.

A passing local build is not a completed launch. A high agent score does not prove sales, indexing, accessibility, security, or legal compliance. Monitoring is created only when requested.

## Armando lesson

During validation on 2026-10-10, the CLI successfully returned Armando's stored 61/100 report with `scanned_at` 07:57:29 UTC, earlier than its 08:30 UTC production deployment. This demonstrates why freshness must be checked: the retrieved score did not establish the result of the deployed fixes. It is an example of interpreting evidence, not a target score for other sites.
