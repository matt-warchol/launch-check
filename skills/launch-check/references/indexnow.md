# IndexNow on public website launches

Use for each new website built or launched with launch-check when its public pages should be discoverable in search. The aim is an **ongoing publication hook**, not a one-time ping. During a preview-only build, prepare and test the integration without notifying search engines. Activate it after the user-authorized production launch. Skip private sites, authenticated content, staging/preview hosts, and sites whose owner opts out. For an audit-only request, report the current setup and gaps without making changes.

## Choose the site's publication path

1. Check whether the CMS, SEO plugin, or host already sends IndexNow notifications for added, updated, and deleted pages. If it does, configure and verify that path instead of installing a second sender. [IndexNow recommends checking platform support first](https://www.indexnow.org/faq).
2. Otherwise, integrate with the actual **successful publish event**. For a CMS, use its publish/update/unpublish event. For a static/code site with no native integration, add the bundled [`scripts/indexnow_sitemap.py`](../scripts/indexnow_sitemap.py) to the project and run it as a post-deploy step against the public production sitemap. It compares sitemap URLs and truthful `<lastmod>` values with a persisted prior snapshot, so new pages and meaningfully updated pages are picked up after they are live. Persist its state file between deployments using the host's durable storage or CI artifact/cache; serialize production runs. The first run records a baseline without submitting the whole site unless `--submit-initial` is explicitly selected. A removed URL disappearing from a sitemap is not enough evidence to submit a deletion; use the CMS unpublish event or verify the old URL is 404/410 or redirects to its intended live replacement. Do not send on a build, preview, failed deploy, every page view, or every deploy that leaves a URL unchanged.
3. Set up one random hexadecimal IndexNow key per production host (8–128 characters). Serve a UTF-8 text file at `https://<host>/<key>.txt` whose body is exactly the key. Verify it is publicly reachable with the expected content. If it must live elsewhere, set `keyLocation` and respect its path scope. Keep the key out of logs and reports. Do not reuse the key across unrelated hosts. A platform-managed integration may manage this itself.
4. Queue the final absolute canonical URLs for newly published or meaningfully changed public pages. For removed pages, queue the former URL only after its public response is 404/410 or an intended redirect. Exclude drafts, `noindex`, robots-blocked, authenticated, preview, staging, and noncanonical URLs. Group only URLs owned by the verified host; deduplicate and batch changes. Respect the protocol's maximum of 10,000 URLs per POST.
5. A static-site integration runs after the production deploy succeeds, with `INDEXNOW_KEY` supplied from a deployment secret and `--sitemap https://<canonical-host>/sitemap.xml --state <persisted-path>`. The script verifies the public key file, checks changed URLs against live status, robots.txt, noindex, and canonical signals, then sends eligible URLs in batches of at most 10,000. For custom integrations, send one POST to `https://api.indexnow.org/indexnow` with `Content-Type: application/json; charset=utf-8` and `{ "host": "www.example.com", "key": "<key>", "urlList": ["https://www.example.com/new-page"] }`. Add `keyLocation` only when needed. One participating endpoint shares accepted notifications with the other participating engines; do not send the same change to every endpoint. Handle retries with bounded backoff for temporary errors and `429`, without creating duplicate floods. Record URL, event, time, response code, and retry status without logging the key.
6. After launch, verify the key file, a real eligible publish/change event, the resulting request, and its response. `200` means received; `202` means received with key validation pending. Investigate `400`, `403`, and `422` rather than retrying blindly. Check that the URL remains in the sitemap and internal links where appropriate. Report `configured`, `event verified`, and `accepted by IndexNow` separately. A successful submission does **not** prove crawling, indexing, ranking, or delivery to Google.

For a brand-new site launched with this skill, run the first script invocation with `--submit-initial` after verifying the deployed sitemap and pages, then rely on publish/change events. When adding the script to an existing site's deployment, default to baseline-only so unchanged historical URLs are not resubmitted. Keep the sitemap and Google Search Console workflow for Google; Google is not listed among the IndexNow participating endpoints. An agent skill cannot run in the background by itself: the CMS/host/deployment integration and persistent state are what make future pages submit automatically. If the site or host cannot support that hook, leave it `PENDING SETUP` with the exact integration point and owner instead of claiming autopilot.

### Static-site script setup

Copy `scripts/indexnow_sitemap.py` into each site's deployment tooling. It uses only the Python standard library. Generate a random 32-character hexadecimal key, publish a UTF-8 file named `<key>.txt` at the site root containing exactly that key, and put the same key in the production secret `INDEXNOW_KEY`. Set `INDEXNOW_KEY_LOCATION` only when the key file is not at `https://<host>/<key>.txt`. The script does not log the key. Run it after the deploy provider confirms production success:

```sh
python3 scripts/indexnow_sitemap.py \
  --sitemap https://www.example.com/sitemap.xml \
  --state .launch-check/indexnow-state.json
```

The state file must survive between deploys. In GitHub Actions, one option is to restore a state cache at the start of a serialized production job and save a new cache after the notification step, using a unique cache key per run and a stable restore prefix. A durable host KV or artifact store is preferable when cache eviction would be a problem. If there is no previous state, the script saves the current sitemap as a baseline and sends nothing; `--submit-initial` explicitly opts into submitting all eligible URLs on that first run. Existing page updates are detectable only when a reliable `<lastmod>` changes; if the generator omits it, use a native publish event or pass a release change list to a custom hook. Use `--dry-run` to inspect sitemap additions before connecting production secrets. Never execute the submit step for pull-request previews, staging, or failed deployments.

Serialize production runs by adding this at the workflow's top level:

```yaml
concurrency:
  group: indexnow-production-${{ github.ref_name }}
  cancel-in-progress: false
```

Add these steps inside the production job, with the notification step **after** the successful deploy step:

```yaml
- uses: actions/cache@v4
  with:
    path: .launch-check
    key: indexnow-${{ github.ref_name }}-${{ github.run_id }}
    restore-keys: indexnow-${{ github.ref_name }}-
# Run the provider's production deployment step before this step.
- name: Notify IndexNow after production deploy
  if: success() && github.ref == 'refs/heads/main'
  env:
    INDEXNOW_KEY: ${{ secrets.INDEXNOW_KEY }}
  run: >-
    python3 scripts/indexnow_sitemap.py
    --sitemap https://www.example.com/sitemap.xml
    --state .launch-check/indexnow-state.json
    --submit-initial
```

Remove `--submit-initial` after the first successful production run. Replace `main`, the production host, script path, and persistent-state mechanism to match the project. GitHub cache entries can expire; use durable storage for sites where missing a state snapshot would be costly.

For providers with automatic Git deployments outside GitHub Actions, connect the provider's **production deployment completed successfully** hook to a protected runner or serverless function that runs this script and persists the state. A Next.js/Astro/Hugo build finishing is not sufficient; the public production sitemap and pages must already be available.

## Primary sources

Checked 2026-10-20; verify current protocol details before implementation.

- [Bing IndexNow implementation guide](https://www.bing.com/indexnow/getstarted#implementation) — native CMS/CDN support, key setup, posting, verification, and indexing limitation.
- [IndexNow documentation](https://www.indexnow.org/documentation) — key verification, request formats, response codes, and batch limit.
- [IndexNow FAQ](https://www.indexnow.org/faq) — native integrations, participating endpoints, and automation guidance.
- [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq) — discovery and submission do not guarantee indexing.
