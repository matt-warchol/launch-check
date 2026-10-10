# Launch Check

An instruction-based Agent Skill for building landing pages, researching search demand, auditing technical SEO, and verifying website launches, including Is Agentic readiness.

**Version:** 1.3.0 · **Reviewed:** 2026-10-10 · **Distribution:** portable skill folder and GitHub-ready source repository.

The skill guides a coding/research agent using the tools available in its host. It is not a standalone crawler, SEO database, deployment service, or guarantee of rankings. It has no mandatory paid service, API key, MCP server, or runtime script.

## Quick start

Install the `skills/launch-check` folder in your agent's supported skill location. For current Codex, copy it into the target project's `.agents/skills/` directory or your user-level `~/.agents/skills/` directory. Keep its name and supporting files together. Avoid installing a second copy with the same skill name. Codex normally detects changes; restart if it does not appear. These locations follow [official installation guidance](https://learn.chatgpt.com/docs/build-skills), checked 2026-09-29.

For the complete landing-page workflow, see [How to launch a website](docs/LAUNCH-A-WEBSITE.md). Existing installations should replace the whole skill folder with this version, including its supporting references.

## How to run a mode

**Paste the commands below into your coding agent's chat after installing the skill.** In Codex, `$launch-check` selects the skill; the words after it tell the agent what to do. Replace text in square brackets with your details.

There are no terminal commands such as `launch-check audit` or `launch-check --mode launch`. The modes are instructions to the agent, not CLI subcommands. The separate `npx is-agentic` command runs in a terminal and only retrieves/runs the agent-readiness check.

| You want to… | Mode | Short command to paste into chat | What happens |
| --- | --- | --- | --- |
| Create a page | Build landing page | `$launch-check build a landing page for [product]. Prepare a preview; do not push or deploy.` | Creates/changes code, prepares a preview, and runs relevant checks |
| Plan SEO/content | Research | `$launch-check research SEO for [product] aimed at [audience]. Do not change files.` | Produces sourced opportunities and page briefs |
| Find problems | Audit | `$launch-check audit [URL] and this repository. Do not change files.` | Reports prioritized issues and evidence |
| Fix selected problems | Implement | `$launch-check implement these fixes: [list]. Preserve the design; do not push or deploy.` | Changes files and verifies the specified fixes |
| Publish the page | Launch | `$launch-check launch this site: push to [repo/branch] and deploy to [host/project] at [domain]. Verify production and run Is Agentic.` | Checks release readiness, publishes within authorization, and verifies the live site |

You can use one mode on its own or combine them. You do not need to run research before every build. A practical sequence is **Build → Audit → Implement → Launch**; add Research when you need audience/search planning. Launch can also prepare a release without publishing: say “Prepare the launch handoff; do not push or deploy.”

In another Agent Skills host, use that host's skill-selection convention and the same instructions. A regular chat can read these instructions, but that alone does not install an automatically discoverable skill.

## What each mode checks

### Build landing page

- Turns the audience, benefit, differentiator, and main action into a clear page.
- Uses approved proof/photos, readable mobile layouts, accessible controls, and subtle motion.
- Adds essential SEO and social previews; prepares a preview and relevant tests.

### Research

- Investigates audience questions, search intent, competitors, and useful content opportunities.
- Groups queries into page briefs with titles, headings, conversion actions, and internal links.
- Records source/market/date and labels missing demand data; naming/domain research is optional.

### Audit

- Checks readability, navigation, conversion paths, accessibility, HTML, and status codes.
- Reviews canonical URLs, sitemap/robots, metadata, social images, and applicable structured data.
- Checks HTTPS, privacy/tracking, and Is Agentic when in scope; ranks findings with evidence.

### Implement

- Applies the specified audit fixes while preserving existing design and behavior.
- Updates relevant copy, code, metadata, agent files, or selected analytics setup.
- Adds meaningful regression coverage and verifies changed behavior; publishing is separate.

### Launch

- Verifies the correct repository, branch, hosting project, build settings, and rollback route.
- Pushes/deploys when authorized; checks DNS, HTTPS, production conversion paths, and public resources.
- Runs Is Agentic, checks report freshness, verifies analytics when selected, and gives an owner handoff.

### Optional Google Analytics module

- Adds the website to your selected GA4 account: reuses or creates the property and web stream.
- Installs the tag, page views, and agreed action events without duplicate tracking.
- Checks consent behavior and confirms data in Realtime/DebugView when access permits.
- Runs automatically after authorization when account/code access is available; otherwise gives the exact setup step or requests an existing `G-…` measurement ID.

## Copy-paste examples for every mode

### 1. Build landing page — create the page

Use when you have a product brief and need a working page. Give the audience, benefit, conversion destination, brand references, and approved proof.

**Paste into your agent's chat:**

```text
$launch-check build a minimalist Next.js landing page for Armando.
Audience: B2B agencies and consultancies with long-term clients.
Benefits: clearer account processes, shared client context, and better
follow-through. Main action: Let's talk, linking to mailto:m@avo42.com.
Use the brand references and approved founder proof in this project.
Work in the current repository. Prepare a preview and run relevant
checks. Do not push or deploy.
```

**You get:** page code, preview, working contact action, essential SEO, and test results. Missing proof or product facts remain explicit decisions.

### 2. Research — decide what content to create

Use when you need search opportunities, audience questions, or page briefs before building.

**Paste into your agent's chat:**

```text
$launch-check research SEO for an account-management product aimed at
B2B agencies in [target country/language]. Keep our existing brand.
Produce intent clusters and briefs for three useful pages, including
suggested titles, headings, internal links, and calls to action.
Use free sources. First check which research tools are available.
Do not invent search volumes or change website files.
```

**You get:** sourced research, a page plan, and explicit data gaps. If numeric research needs an unavailable account, the agent explains the setup/export options before that work.

### 3. Audit — check an existing site

Use when a page already exists and you want findings before editing.

**Paste into your agent's chat:**

```text
$launch-check audit https://armando.avo42.com and the current repository.
Check mobile readability, the main contact action, essential SEO,
social previews, HTTPS, and analytics delivery where access permits.
Run npx is-agentic armando.avo42.com and record its scan timestamp.
Give prioritized findings with evidence and concrete fixes.
Do not change files, push, or deploy.
```

**You get:** an evidence-backed report with blockers, improvements, and checks that could not run. The Is Agentic score is labeled stale if its scan predates the release.

### 4. Implement — apply specific fixes

Use after an audit or when you already know what needs changing. Name the fixes or attach the report and identify the agreed items.

**Paste into your agent's chat:**

```text
$launch-check implement these fixes in the current repository:
add a valid sitemap, correct canonical and Open Graph metadata,
fix skipped heading levels, and improve small section text.
Preserve the existing visual design and product behavior.
Add relevant regression tests and verify all affected endpoints.
Prepare a preview and summarize the changes. Do not push or deploy.
```

**You get:** scoped changes, verification results, and unresolved decisions. If you also want Markdown negotiation or other agent fixes, include those explicitly or reference the applicable audit findings.

### 5. Launch — publish and verify

Use when you are ready to deliver the page. Specify the repository/branch, hosting project, and canonical domain.

**Paste into your agent's chat:**

```text
$launch-check launch the agreed landing-page changes.
Push to [GitHub repository] on [branch] and deploy to [hosting project]
at https://[public domain]. Verify the build, deployment version,
DNS, HTTPS, main conversion path, metadata, sitemap, and public assets.
Run npx is-agentic [public domain], check report freshness, and fix
applicable issues within the agreed landing-page scope.
Give me the live URL, Git commit, verification results, remaining
owner actions, and rollback route.
```

**You get:** a verified public release when access and authorization permit it, plus a concise handoff. Missing account or DNS access is reported with the exact pending action; a local build alone is not a completed launch.

For the full sequence and checklist, see [How to launch a website](docs/LAUNCH-A-WEBSITE.md).

The agent performs a capability preflight before dependent work. It asks for only the missing setup that the requested deliverables require. SEO research uses Google Trends and Google Keyword Planner by default, without paid SEO tools. Keyword Planner may require a completed Google Ads setup and billing information; if unavailable, the agent tells the user before research and offers Trends-only, an export, or setup instructions. Known missing prerequisites are reported as `NOT RUN — prerequisite unavailable`, while `UNVERIFIED` is reserved for an attempted check with insufficient evidence.

## Package contents

```text
skills/launch-check/
  SKILL.md                    Entry point and decision rules
  agents/openai.yaml          Codex presentation metadata
  references/research.md      Demand, intent, competitors, domains
  references/technical-seo.md Indexing, metadata, AI search, experience
  references/launch.md        Privacy, security, telemetry, release
  references/landing-page.md  Build-to-production checklist
  references/is-agentic.md    CLI audit, freshness, fixes, verification
  references/google-analytics.md GA4 setup, consent, events, verification
  assets/report-template.md   Reusable evidence and handoff template
README.md                     Installation and use
docs/LAUNCH-A-WEBSITE.md      Step-by-step landing-page usage
docs/REVIEW.md                Findings and corrections to the original
docs/VALIDATION.md            Checks, scenario review, and limits
docs/PUBLISHING.md            Release and distribution instructions
docs/RELEASE-NOTES.md         Reusable release description
CHANGELOG.md                  Version history
LICENSE-NOTICE.md             Licensing status
```

Read [the review](docs/REVIEW.md) for what changed, [validation](docs/VALIDATION.md) for the evidence behind readiness, and [publishing](docs/PUBLISHING.md) before distribution. Source links for SEO and launch guidance are kept with the relevant skill references.

## Google Analytics on autopilot

**Paste into agent chat** when you want GA4 set up as part of implementation or launch:

```text
$launch-check set up Google Analytics 4 for https://[domain].
Use [Analytics account/property]. Reuse the correct property and web
stream, or create them if missing. For a new property use [name],
[reporting time zone], and [currency]. Install the tag and track page
views and the primary contact/booking action without duplicate events.
Use the existing consent setup or identify what must be added.
Verify actual receipt in Realtime/DebugView. You may create the
required property/stream and push/deploy the agreed website changes.
If access is unavailable, tell me the exact missing setup.
```

Autopilot needs authenticated Google Analytics access with the required permissions, plus repository/hosting access. It cannot create resources or confirm report receipt from a measurement ID alone. The skill can use a supported Admin API connection or authorized browser UI; it does not bundle a Google connection or a magic one-command installer.

If you already have a web stream and want only the website integration:

```text
$launch-check add GA4 measurement ID [G-…] to this website.
Track page views and contact clicks, respect the applicable consent
setup, and prepare a tested preview. Do not push or deploy yet.
```

Read the [Google Analytics checklist](skills/launch-check/references/google-analytics.md) for setup, events, privacy, verification, and manual fallback steps.

## Is Agentic check

```bash
npx is-agentic example.com
npx is-agentic example.com --json
```

Replace the domain with your canonical public site. The [official CLI](https://is-agentic.com/docs) returns the latest stored report or starts a scan if none exists. The skill records scan freshness, prioritizes applicable failures, and verifies fixes against public HTTP responses. A cached report is not proof of a new post-launch score. Reports are public; never submit confidential or secret-bearing URLs.

## Boundaries and maintenance

The skill does not buy domains, add paid subscriptions, publish legal policies, change DNS, or deploy just because it was invoked. It follows the user's actual authorization. It separates drafting, implementation, and verified results, and does not commit unrelated work.

Privacy text requires true business facts and jurisdiction-specific review; security checks are scoped launch checks. Search volume estimates, AI citations, indexing, and field performance cannot be guaranteed. See the validation report for what has and has not been tested.

Before a release, recheck changing engine features, provider behavior, and regulator guidance. Re-run package validation and representative behavioral scenarios after substantive instruction changes. Keep `SKILL.md` concise and load detailed references only as needed.
