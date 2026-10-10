# How to launch a website with Launch Check

Version 1.2.0. This workflow turns a brief or an existing landing page into a tested production release. It works with the framework and hosting provider you choose; Next.js, GitHub, and Vercel were used for Armando but are not prerequisites.

## Choose a mode and where to type it

After installation, paste `$launch-check` followed by your request into the coding agent's **chat**, not your terminal. There are no `launch-check build` or `launch-check audit` shell subcommands. The agent infers the mode from the request.

- **Build landing page:** `$launch-check build a landing page for [product]. Prepare a preview; do not push or deploy.`
- **Research:** `$launch-check research SEO for [product] and [audience]. Do not change files.`
- **Audit:** `$launch-check audit [URL] and this repository. Do not change files.`
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

## 3. Review the page and checklist

Review the page's promise, benefits, proof, mobile readability, and main action. The [landing-page checklist](../skills/launch-check/references/landing-page.md) covers meaningful HTML, headings, subtle motion, downloads/forms, SEO, social previews, analytics delivery, and release settings. Do not approve claims or policies whose facts are still unknown.

Ask the agent to resolve agreed issues and provide the preview URL, test results, pending decisions, and rollback route. Browser checks and HTTP checks are different evidence: blocked browser access must be disclosed.

## 4. Authorize delivery

```text
Push the agreed changes to [repository/branch] and deploy to
[hosting project] at [public domain]. Verify DNS, HTTPS, the deployed
version, and the main conversion path. Run the Is Agentic check and
fix applicable issues within the agreed landing-page scope.
```

Existing authorization does not need to be repeated. If the registrar or account requires your action, the agent should give the exact pending setup and continue independent work. A DNS record alone does not prove a working certificate or correct production site.

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
