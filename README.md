# Launch Check

An instruction-based Agent Skill for researching search demand, planning useful pages, auditing technical SEO, and preparing web applications for launch.

**Version:** 1.1.0 · **Reviewed:** 2026-09-29 · **Distribution:** portable skill folder and GitHub-ready source repository.

The skill guides a coding/research agent using the tools available in its host. It is not a standalone crawler, SEO database, deployment service, or guarantee of rankings. It has no mandatory paid service, API key, MCP server, or runtime script.

## Quick start

Install the `skills/launch-check` folder in your agent's supported skill location. For current Codex, copy it into the target project's `.agents/skills/` directory or your user-level `~/.agents/skills/` directory. Keep its name and supporting files together. Avoid installing a second copy with the same skill name. Codex normally detects changes; restart if it does not appear. These locations follow [official installation guidance](https://learn.chatgpt.com/docs/build-skills), checked 2026-09-29.

Then ask, for example:

```text
Use $launch-check to research SEO for a new invoicing app for
UK freelancers. The main conversion is a free trial. Keep the existing
brand. Produce keyword clusters and briefs for the first three pages.
I do not have a paid keyword tool; label missing volume as unknown.
```

```text
Use $launch-check to audit this repository and preview URL before
launch. Report the blockers and evidence. Do not change files yet.
```

```text
Use $launch-check to implement the agreed SEO fixes and verify the
production build and primary signup flow. Prepare a release handoff.
```

In another Agent Skills host, use that host's skill installation/invocation convention. The portable format is used; this release has not been runtime-tested on every host. A regular chat can read the instructions, but that alone does not install an automatically discoverable skill.

## What it delivers

| Mode | Typical result |
| --- | --- |
| Research | Sourced opportunities, intent clusters, keyword-to-page map, content briefs, optional name/domain research |
| Audit | Prioritized findings with evidence, coverage, and unknowns |
| Implement | Scoped edits, verification results, and unresolved issues |
| Launch | Readiness handoff, authorized deployment verification, rollback and follow-up plan |

The agent performs a capability preflight before dependent work. It asks for only the missing setup that the requested deliverables require. SEO research uses Google Trends and Google Keyword Planner by default, without paid SEO tools. Keyword Planner may require a completed Google Ads setup and billing information; if unavailable, the agent tells the user before research and offers Trends-only, an export, or setup instructions. Known missing prerequisites are reported as `NOT RUN — prerequisite unavailable`, while `UNVERIFIED` is reserved for an attempted check with insufficient evidence.

## Package contents

```text
skills/launch-check/
  SKILL.md                    Entry point and decision rules
  agents/openai.yaml          Codex presentation metadata
  references/research.md      Demand, intent, competitors, domains
  references/technical-seo.md Indexing, metadata, AI search, experience
  references/launch.md        Privacy, security, telemetry, release
  assets/report-template.md   Reusable evidence and handoff template
README.md                     Installation and use
docs/REVIEW.md                Findings and corrections to the original
docs/VALIDATION.md            Checks, scenario review, and limits
docs/PUBLISHING.md            Release and distribution instructions
docs/RELEASE-NOTES.md         Reusable release description
CHANGELOG.md                  Version history
LICENSE-NOTICE.md             Licensing status
```

Read [the review](docs/REVIEW.md) for what changed, [validation](docs/VALIDATION.md) for the evidence behind readiness, and [publishing](docs/PUBLISHING.md) before distribution. Source links for SEO and launch guidance are kept with the relevant skill references.

## Boundaries and maintenance

The skill does not buy domains, add paid subscriptions, publish legal policies, change DNS, or deploy just because it was invoked. It follows the user's actual authorization. It separates drafting, implementation, and verified results, and does not commit unrelated work.

Privacy text requires true business facts and jurisdiction-specific review; security checks are scoped launch checks. Search volume estimates, AI citations, indexing, and field performance cannot be guaranteed. See the validation report for what has and has not been tested.

Before a release, recheck changing engine features, provider behavior, and regulator guidance. Re-run package validation and representative behavioral scenarios after substantive instruction changes. Keep `SKILL.md` concise and load detailed references only as needed.
