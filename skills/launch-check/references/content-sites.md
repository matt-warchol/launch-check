# Content sites: guides, scheduled pages, sources

Use when a site has guides, articles or tools that make factual claims, uses scheduled publishing, or is edited by more than one person or agent. Lessons from a shipped founder-guides site.

## Scheduled publishing

- A `publishOn` date inside a build only takes effect when a build runs on or after that date. Confirm something triggers one: a host deploy hook called by a daily scheduled job, or the host's own scheduler. If nothing does, mark it `UNVERIFIED` and tell the owner the page will not appear on its own.
- Never leave links to unpublished pages in body copy, related lists, navigation, footers, `llms.txt`, Markdown twins or sitemaps. Gate them in the build: render the link only when its target is live. Hand-removing links is how a 404 ships on publish day.

## Link integrity

- Make the build fail on internal links that do not resolve, across HTML and any alternate formats (Markdown twins, feeds). Add a test that proves links to scheduled pages are absent today.
- Judge orphan pages and inbound links from the built output, not source files: lists, bylines and navigation are often generated at build time.

## Sources and claims

- Every page that makes legal, tax, platform or regulatory claims gets a visible **Sources** list of primary sources (statute, regulator, platform documentation). Fetch and read each one; a search snippet is not a source. Paraphrase and keep quotes short.
- Prefer primary sources over aggregators. Record the version or date of rules that change, and say when a rule is jurisdiction-specific instead of stating it as universal.
- If a source cannot be fetched (robots block, login wall), link it but mark the claim `UNVERIFIED` in the report. Do not describe details you could not read.
- Check that existing copy still matches the source. Fix wrong claims and say so in the handoff.

## Authorship and first-hand experience

- Add a visible byline, a short bio and matching structured data on guides.
- First-hand stories, results and numbers come from the author, never from the assistant. Ask for one real example per page and list it as a dependency. Continue the rest of the work.
- Verify bio claims against what the author actually stated. Flag any "lesson learned" sentence the author did not write.

## Audit tool caveats

- Heuristic content analyzers often expect frontmatter. Sites that keep titles, descriptions and schema in comments or layouts produce false positives (missing title, author, H2). Use their ranking, not their scores, and confirm each finding against the built page.
- Report false positives as such so the owner does not chase them.

## Editing existing pages

- Change `lastmod` only on substantive edits. Do not bump every page.
- Before merging overlapping pages, compare intents (for example crisis response, one asset, setup before a company exists). Keep them separate when intent differs; add a one-line scope statement and cross-links.
- Fix thin pages with worked examples (check the arithmetic by running it), FAQs and relevant internal links. Do not pad.

## Parallel work

- Before editing shared files, list open PRs and branches, including other agents'. Dry-run the merge (`git merge --no-commit --no-ff`) to find conflicts, then agree the merge order.
- A shallow single-branch clone may not track new branches. If a hook reports unpushed commits that are already on the remote, add a fetch refspec for the branch before assuming the push failed.
