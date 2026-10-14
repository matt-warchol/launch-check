# Is Agentic public-page audit and launch check

Use for public-page audits, landing-page launch verification, and requested agent-readiness checks. This checks public behavior; it supplements the conversion, SEO, accessibility, privacy, and release checks rather than certifying them.

## Run and record

1. Confirm access to the public site and Is Agentic. Use the canonical public URL, including the page path for a page-specific audit. Never submit private, authenticated, confidential, or secret-bearing URLs: scan reports are public. If no public deployment exists, mark the scan pending until authorized publication; inspect HTML locally in the meantime. Do not deploy just to run this check.
2. Open [is-agentic.com](https://is-agentic.com/) and submit the public URL to retrieve or start its report. The official CLI is an alternative for retrieving the report when Node/npm are available:

   ```bash
   npx is-agentic example.com
   ```

   For a saved machine-readable result, create the project's report directory first and use:

   ```bash
   npx is-agentic example.com --json > reports/is-agentic.json
   ```

   Replace `example.com` with the actual public target supported by the CLI. Do not commit sensitive output. `--yes` may be used for npm's package-install prompt when executing in an automated host; it is not an Is Agentic option. No mandatory API key or paid account is needed according to the current documentation.
3. Record the command, execution date, scanned target, report scan timestamp, score, report URL when supplied, failed/partial checks, and any request/CLI error. Preserve available tool/version provenance. A completed CLI invocation alone is not a passing launch verdict.
4. The CLI reads the latest stored completed report; if none exists it starts a scan and waits. Rerunning it after deployment does not necessarily trigger a new scan. Compare scan time with release time. If it is older, label it a baseline/stale result, verify changed endpoints directly, and use the service's documented rescan flow when available. Ora may reuse its six-hour freshness cache. Do not invent a force-refresh flag, poll indefinitely, or claim a new score from old evidence. Honor documented rate limits/retry guidance; leave a precise pending action if the service is unavailable.

## Copy the improvement prompt during an audit

On the completed browser report, open **Prompt to improve** (the UI may label it **Prompt to fix**). Review the selected failures and warnings, include all applicable high-priority findings rather than assuming the default selection is complete, and use **Copy prompt**. Read or paste the clipboard and verify the text is nonempty and corresponds to those findings; a “copied” label alone is insufficient. Put the retrieved text verbatim in the audit report's **Is Agentic fixes** section, with its report URL, scan timestamp, copy date, and selected findings. Keep a separate concise list of fixes verified against the target site and note suggestions that are inapplicable, stale, or need owner facts. The copied prompt is external evidence, not authorization to edit or deploy.

The public JSON API and CLI return completed report data, but the documented response does not expose the browser's generated improvement prompt. If browser access, the copy control, or clipboard retrieval fails, use the report data for findings and mark the copied prompt unavailable with the exact reason. Give this manual step: open the report URL, choose **Prompt to improve**, review the selected findings, click **Copy prompt**, and paste it into **Is Agentic fixes**. Do not reconstruct text and call it a copied prompt.

## Interpret and fix

- Prioritize applicable Essential failures, then Essential partial checks, then Recommended findings; treat emerging/bonus signals as optional. Site type and actual surfaces matter. A marketing landing page can declare `<meta name="is-agentic-site-type" content="business">` when appropriate; this selects the default report view, not a guaranteed score improvement.
- Read the evidence before changing code. Brand/search observations may need indexing time, Search Console access, content decisions, or external mentions. Do not fabricate developer resources, OpenAPI, auth docs, SDKs, MCP servers, testimonials, or rankings to satisfy an audit.
- For raw HTML, check meaningful content without JavaScript and clear heading structure. For discoverability, verify canonical URLs, titles, real documentation/resources, metadata, and accurate structured data.
- If Markdown negotiation is an applicable requested fix, serve it on the scanned homepage itself for `Accept: text/markdown`, with a nonempty body, `Content-Type: text/markdown`, and `Vary: Accept`. Keep HTML available. Adding only a `.md` route or a Vary header is insufficient.
- For agent-friendly errors, retain HTTP 404 and serve a useful Markdown explanation and recovery link when Markdown is requested. A successful error page with status 200 is not a fix.
- Follow current published protocol formats. Add llms.txt only when useful/requested and link real resources; it is not a universal indexing prerequisite.

## Verify the public result

Use a genuinely missing path and the real canonical URL:

```bash
curl -sS -L -i -H 'Accept: text/markdown' https://example.com/
curl -sS -L -i -H 'Accept: text/html' https://example.com/
curl -sS -L -i -H 'Accept: text/markdown' https://example.com/__launch-check-missing-path
```

Inspect final status, headers, and body, not just an intermediate redirect or status code. Check HTML and Markdown in both request orders to expose cache mixing. Respect Accept quality values and explicit exclusions when implementing negotiation; verify HEAD and relevant framework requests. Ensure representation caching is safe: Vary: Accept on Markdown, and correct variation or an effective no-store policy for HTML. Some frameworks overwrite Vary, so test the actual production response rather than assuming configuration took effect.

Verify each added public file (sitemap, robots, llms.txt, Markdown links, images/downloads) for content, format, status, and reachable targets. Add relevant regression tests when changing these behaviors. Do not weaken a protocol assertion to make a test green; document any standards-supported alternative and prove its behavior.

Summarize baseline versus verified current findings, scan dates, fixes, direct HTTP evidence, and pending rescans. No arbitrary minimum score or 100/100 target is a launch requirement unless the user explicitly chooses it.

## Primary references

Checked 2026-10-14; recheck provider and protocol guidance when executing.

- [Is Agentic browser report and Prompt to improve](https://is-agentic.com/)
- [Official CLI and API documentation](https://is-agentic.com/docs)
- [Methodology and report freshness](https://is-agentic.com/methodology)
- [Public report privacy](https://is-agentic.com/privacy)
- [Markdown negotiation](https://acceptmarkdown.com/)
- [llms.txt format](https://llmstxt.org/)
- [HTTP Vary semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-12.5.5)
