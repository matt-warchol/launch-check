# Application launch readiness

Read for a full launch or directly relevant launch risks. Keep checks proportionate: a static page and a paid multi-user application have different requirements. Use the existing framework and host; neither Next.js nor Vercel is required.

## Business facts, trust, and privacy

Establish the operator's identity and contact, audiences/jurisdictions, collected data, purposes, processors, retention/deletion practices, cookies/local storage/pixels, and any sensitive or children's data. Review actual integrations and data flows, not just the wording of a footer.

Draft disclosures and terms only from known facts. Mark missing facts for the operator; do not publish unresolved placeholders or certify compliance from boilerplate. Whether particular terms, cookie controls, or age safeguards are required depends on the service and applicable rules. Obtain specialist review where the application's risk or unresolved legal question warrants it; this skill is not a legal opinion.

Check current regulator guidance for the applicable jurisdiction before asserting a legal requirement. UK rules and EU member-state rules must not be treated as identical. Even within analytics, exemptions can depend on purpose, configuration, and jurisdiction; “cookieless” or a vendor's marketing claim is not enough.

Where consent is required, test an actual clean-browser flow: no consent-dependent storage or transmission before consent, usable acceptance and rejection, honoring the selected categories, persistence, and withdrawal. Inspect network requests as well as cookies. If relying on an exemption, document its source and conditions and verify any required notice or opt-out. A banner's appearance does not establish compliance.

For GDPR/UK GDPR and ePrivacy-style cookie reviews, explicitly inventory cookies, local storage, pixels, SDKs, and server-side tracking; classify each as strictly necessary, preferences, analytics, or marketing; record provider, purpose, data sent, retention, and international transfers; and link the privacy/cookie notice to the actual behavior. Non-essential analytics/marketing storage or access generally needs prior, freely given, specific, informed consent where the applicable law requires it. Test reject-all, granular choices, withdrawal, and a clean first visit. Do not call a site “GDPR compliant” from a banner screenshot or boilerplate policy; state jurisdiction, evidence, and unresolved facts.

## Security checks within launch scope

- Check ignore rules, tracked files, build output, logs, source maps where relevant, and client-visible environment variables for exposed credentials without printing secret values. Keep sanitized environment examples. `.gitignore` does not remove tracked secrets or undo historical exposure. For a detected leak, report location/type with redaction and coordinate revocation/rotation; do not rewrite history or rotate live credentials without appropriate authorization.
- Verify server-side authorization on private data and mutation endpoints, including cross-user access where applicable. Authentication alone is insufficient. Check sessions/cookies and CSRF defenses according to the application architecture.
- Validate untrusted inputs on the server. Review upload constraints, rate limits, expensive endpoints, and abuse controls if those surfaces exist. Do not introduce a validation library just to satisfy the checklist.
- Inspect dependencies and relevant advisories using the project's tools. Triage findings by exposure; avoid broad unrequested upgrades or a claim that an automated scan establishes security.
- Configure headers for the actual resources and integrations. Review CSP in a preview/report-only stage where appropriate, test scripts/forms/embeds, and tighten deliberately. Use `frame-ancestors` and compatible framing controls as needed. Enable HSTS only after validating HTTPS readiness; `includeSubDomains` and preload have broader consequences. Consider `nosniff`, referrer policy, and necessary permissions. Do not paste a universal policy that breaks the app.

## Analytics and error reporting

When the user selects GA4, use [the Google Analytics module](google-analytics.md) for authorized account/property/stream setup, website tagging, consent, events, and receipt verification.

Use the user's existing or selected provider. Define the success action, event name, trigger, minimal properties, consent category, and how to verify it. Distinguish CTA clicks from completed outcomes. Test event delivery, duplication on retries/navigation, and sensitive data exposure. Public measurement IDs are different from secret administrative/server credentials.

Inspect URLs, query strings, payloads, logs, and session replay for personal data leakage. Set retention and access according to actual needs. Check basic error reporting and alert ownership for applications that need them. A missing analytics account may remain unverified without blocking a static page launch; explain the consequence rather than inventing configuration.

## Build, release, and rollback

1. Inspect the working tree and package manager/lockfile, repository scripts, deployment settings, environment variable names, and required services. Run the actual build, lint, type checks, and relevant tests separately where applicable. Capture results, not secrets. A repository without a particular check gets `N/A` or `UNVERIFIED` with a reason.
2. Use a preview for end-to-end smoke checks. Verify signup/login, forms, payment sandbox flow, exports, email, or other critical behavior only as applicable and authorized. Avoid generating real charges or messages as a casual smoke test.
3. Verify production environment and DNS/TLS configuration through the host's actual status and public responses when available. Do not declare a certificate ready solely because the provider normally provisions one.
4. Before deployment, identify the previous working release or first-release disable/rollback path. For data migrations, review backup/restore and compatibility. Record release blockers and residual risk in the report.
5. Review the diff. Commit, push, change DNS, publish policies, and deploy only within the user's authorization. Do not stage unrelated local work. After deployment, verify the live public URL and critical flow; roll back within authorization if an agreed critical condition fails, otherwise report and seek the needed decision.
6. When authorized and access exists, verify the site's Search Console property, submit its sitemap, and inspect a representative URL. Otherwise provide exact next steps and label them pending. Submission is not proof of indexing. Consider another search engine's webmaster tools when relevant to the market; do not require every provider.

## Follow-up handoff

Suggest a check shortly after launch for availability, errors, consent, conversions, and crawl controls; then a later review of indexing/query data and conversion quality once sufficient observations exist. A 7/30-day review can be a practical starting point, not a ranking deadline. Assign an owner and proposed date. Do not silently create a recurring automation or claim to monitor after the task ends.

## Primary references

Checked 2026-09-29; recheck regulator/provider documentation for the actual project.

- [ICO storage and access technologies guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/) — UK-specific reference, not a universal privacy rule.
- [ICO April 2026 guidance update](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/04/final-storage-and-access-technologies-guidance-published/)
- [OWASP HTTP header guidance](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [ICO storage and access technologies guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/) — consent and cookie behavior reference.
