# Search research and page strategy

Read for research, content planning, or naming work. Use the report template's research tables; omit irrelevant columns rather than filling them with guesses.

## Inputs and available evidence

Before researching, run the capability preflight in `SKILL.md`. Use a free-first Google workflow: Google Trends for relative interest and seasonality, then Google Keyword Planner for Google's volume ranges and keyword ideas. Numeric keyword demand and competitor traffic/rankings are separate requirements from qualitative search-result inspection. If the requested report includes them, verify access to the relevant Google service or a sanitized export first. Do not start the research and discover at the end that no numbers can be produced.

Establish product value, likely buyers/users, conversion, target market/language, existing URLs, known alternatives, and constraints. Preserve an existing identity. Use Search Console and analytics if already accessible; otherwise work from the brief, public pages, and authorized exports.

Capability tiers:

| Access | Valid output | Limitation |
| --- | --- | --- |
| Brief only | Query hypotheses, initial clusters, research plan | Demand and search-result intent unverified |
| Browser/search | Observed competitors, result formats, question themes, qualitative opportunity | No numeric volume/difficulty without an actual data source |
| Google Trends | Relative interest, trend direction, seasonality, related queries | Not monthly volume; values are normalized and locale/time-range dependent |
| Google Keyword Planner | Google volume ranges/metrics, related ideas, advertiser competition/CPC fields | Requires Google Ads account setup; billing information may be required; advertiser metrics are not organic difficulty |
| Other SEO tool or export | Provider-reported metrics with settings and date | Use only when the user requests it; estimates and ranges remain estimates |
| Search Console/analytics | Existing query/page performance and conversions | Current site performance is not total market demand |

Use this setup gate:

| Requested output | Minimum capability to run that check | If missing at preflight |
| --- | --- | --- |
| Search intent, result formats, visible competitors | Browser/search access | Offer a qualitative plan only, labeled as such |
| Relative trends and seasonality | Google Trends access or a user-supplied Trends export | Mark `NOT RUN — prerequisite unavailable`; offer a qualitative plan |
| Monthly volume/ranges, keyword ideas, CPC | Google Keyword Planner with completed Google Ads setup, or a user-supplied export | Tell the user that Google Ads setup/billing information may be required; mark `NOT RUN — prerequisite unavailable` and offer Trends-only or setup/export |
| Organic keyword difficulty (KD) | A provider/export that explicitly defines an organic KD metric | Mark `unknown` in the query table; do not relabel Keyword Planner's advertiser competition as KD |
| Competitor traffic/rankings | A connected provider with those fields or an authorized export | Mark `NOT RUN — prerequisite unavailable`; do not infer from SERPs or traffic-estimate pages |
| Domain registration status | An actual registrar/RDAP capability | Mark `NOT RUN — prerequisite unavailable`; do not treat DNS or a search link as a result |
| Trademark clearance | A relevant official trademark search and jurisdiction | Mark `NOT RUN — prerequisite unavailable`; state that name brainstorming is not clearance |

If a user supplies a tool or connector name, verify it is present and authenticated in the current host before referring to it as available. “Can be installed” is not “available now.” Do not recommend a paid SEO tool as a prerequisite when the user requested Google-only research.

Do not request passwords or paste API secrets into reports. Use available authenticated tools or ask for a sanitized export when data matters. Lack of a paid SEO tool does not prevent qualitative research.

## Research method

1. Generate queries from customer problems, product categories, use cases, alternatives, and evaluation questions. Roughly 15–30 candidates can seed a small launch, but coverage matters more than a fixed count. Include branded navigation only where meaningful.
2. For each priority query, capture a current SERP in the target market/language and inspect the first 5–10 organic results where accessible. Record search provider, date, actual locale/device, organic rank, URL, and whether the landing page opened. Classify each opened page by its primary job/format: explanation or guide, comparison table, calculator, template, directory, interactive tool, product page, or a useful combination. Record the concrete interaction (for example inputs and calculated result, downloadable sheet, or side-by-side comparison), not just the title. A redirected, blocked, or inaccessible result is `unverified`; a snippet-based guess is `snippet-only`. Count confirmed formats only among opened, relevant pages and show the denominator (for example `3 of 5 inspected`). Keep ads, SERP features, app listings, forums, and irrelevant results visible but separate so they do not silently skew the format conclusion. Search tools may not reproduce a truly localized SERP; disclose that limitation.
3. Use Trends to compare terms in the same market/time range, identify directionality and seasonality, and inspect related topics/queries. Record its geography, time range, search type, category, date, and whether the term was a topic or exact search term. Use Keyword Planner for volume ranges and ideas; record geography, language, network, date/export, and account settings. If an authorized provider supplies organic KD, record its definition, geography, and retrieval date separately. Do not transform an unavailable number into zero. Trends indices are relative interest, not monthly searches. CPC and advertising competition are separate from organic difficulty. Do not sum grouped close variants as independent demand.
4. Cluster phrases that reflect the same user need and substantially similar result intent. Prioritize with a brief explanation of relevance, business value, observed competition, evidence confidence, and production effort. Keep any subjective score explicitly heuristic; avoid fabricated precision.
5. Map each cluster to a primary existing or proposed page. Check overlap with existing pages before proposing another URL. A homepage can introduce the product while feature, use-case, comparison, and educational pages serve distinct needs.
6. Show one compact decision table before the briefs: query, search intent, estimated monthly volume, organic KD, confirmed top-result formats with coverage, proposed format, and why it fits this product. Put provider, market/language, metric update date, and inspected URLs beside the table or in its evidence appendix. Volume and KD are separate provider estimates; paid-ad competition is not KD. Use `unknown` when a provider omits a query or field, and never read missing KD as zero. Format comes from opened result pages, not the keyword, volume, or KD. If the results are mixed, say so and choose based on the visitor's task and a credible product advantage. If a higher-volume query is outside the product's real scope, recommend `do not build` rather than inventing a feature.
7. Create briefs for the selected pages. State the observed mix of top-result formats and cite inspected URLs, then recommend a primary page format and explain why it serves the user's task and the product's real capabilities. The format can differ from the majority if the gap warrants it; distinguish a content explanation from a tool someone can use. Specify what the visitor needs to learn or do, the proof the page can offer, factual gaps, title/H1, logical sections or interactions, conversion, and links to related pages. If only snippets or no SERP access is available, mark the format recommendation provisional rather than claiming to have reviewed the pages. Do not create testimonials, customer logos, test results, prices, or competitor disadvantages without evidence.

Do not scrape private data, publish bulk near-duplicate location/use-case pages, or recommend paid links as a ranking shortcut. For another language, validate local wording and intent rather than translating keywords mechanically.

## Optional identity and domain work

Suggest names only when appropriate. Consider memorability, pronunciation, differentiation, and audience; exact-match keyword domains are not a prerequisite. Include relevant extensions rather than requiring `.com`.

Use a registrar's live availability result when accessible. Label each domain `reported available`, `registered`, `premium`, or `unverified`, with provider/time and any quoted currency, first-year price, and renewal price separately. DNS absence, an empty website, or a failed WHOIS/RDAP request does not prove availability. A search link is a way to check, not a completed check. Never buy without authorization for the domain and cost.

Flag obvious naming conflicts for investigation. Domain availability does not establish trademark rights. Keep this note to 2–3 lines in the founder-facing output unless a deeper clearance review is requested. Leave final brand selection to the user when it is not already specified.

## Source for metric interpretation

Google's [Keyword Planner metric definitions](https://support.google.com/google-ads/answer/3022575?hl=en) distinguish advertiser competition from other metrics and explain how monthly searches depend on selected settings. Google's [Keyword Planner access guidance](https://support.google.com/google-ads/answer/7337243) says account setup and billing information may be required for keyword suggestions. Use [Google Trends](https://trends.google.com/trends/) for normalized relative interest, not absolute demand. Checked 2026-09-29; recheck when interpreting a new export.
