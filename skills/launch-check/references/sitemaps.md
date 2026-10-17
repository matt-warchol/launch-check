# Sitemap generation and search discovery

Use for new public sites, site launches, and requested indexing work. Start by checking the deployed sitemap, `robots.txt`, canonical URLs, existing generator, and publishing path. Preserve a working generator rather than installing a second one.

## Generate from the source of published pages

- For Next.js App Router, prefer `app/sitemap.ts` with `MetadataRoute.Sitemap`. Derive static URLs from actual routes and dynamic URLs from the published database/CMS records. Choose caching or revalidation that matches publication; a cached route is not automatically fresh on every request. For large sites, split sitemaps using the framework's supported mechanism.
- For static sites, generate XML during the existing build/deploy flow from real output pages or their source manifest. If the host deploys committed files directly, connect generation to a reliable pre-publish workflow and verify the deployed artifact. Do not add a Next.js file to a non-Next.js project.
- Include only canonical, public, indexable 200 URLs on the sitemap's own host. Exclude drafts, future scheduled content, login/app shells, `noindex`, errors, redirects, previews, duplicate formats, and other subdomains. Reflect alternate languages only when reciprocal pages really exist.
- Use page-specific `lastmod` only when it tracks a significant page change (for example verified CMS `updated_at` or a suitable source-file revision). Omit it when no trustworthy date exists. Do not set every URL to today's build date. Google ignores `changefreq` and `priority`, so do not use them to simulate freshness.
- Validate well-formed XML, absolute URLs, unique entries, host/canonical alignment, and reasonable sitemap limits. Test representative listed URLs and confirm the served production sitemap matches the expected output. Keep `robots.txt` pointed to the canonical sitemap URL.

## Submit after production publication

1. Verify the production sitemap and `robots.txt` first. In Google Search Console, use the verified property and Sitemaps report (or an authorized supported API) to submit the sitemap URL. In Bing Webmaster Tools, submit it to the verified site, or confirm an imported/discovered sitemap is already present and processing. Re-submit only when needed; ongoing discovery comes from the updated sitemap and normal crawling.
2. Record property/site, sitemap URL, submission or discovery date, processing status, errors, and owner. If authenticated access is missing, mark submission pending with the exact account step. Do not claim submission because the file exists or appears in `robots.txt`.
3. For a new or materially updated page, ensure a relevant internal link, canonical/indexable response, and inclusion in the generated sitemap. Use the existing [IndexNow workflow](indexnow.md) for participating engines when applicable. Google does not use IndexNow; do not call obsolete Google sitemap ping endpoints. Optional URL inspection is for priority pages, not a bulk indexing guarantee.
4. For ChatGPT search, check the site's chosen `robots.txt` policy for **OAI-SearchBot** and make useful public content crawlable. Keep GPTBot (model training) a separate owner choice. There is no general ChatGPT sitemap submission endpoint or guaranteed inclusion. `llms.txt` is optional, not a substitute for crawlable pages or a sitemap.

Submission and IndexNow notifications are discovery signals, not proof of crawling, indexing, rankings, or AI citations.

Sources: [Next.js sitemap convention](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Bing sitemap guidance](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed), and [OpenAI crawler controls](https://developers.openai.com/api/docs/bots).
