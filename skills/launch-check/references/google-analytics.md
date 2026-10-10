# Google Analytics setup and verification

Use when the user selects Google Analytics 4 (GA4) for the website. This is an optional module used by Audit, Implement, and Launch modes, not a new mode or a requirement to add another tracker. Reuse existing analytics unless the user requests GA4. Autopilot means completing authorized steps with available access, not inventing accounts or bypassing authentication.

## Inputs and access

- Confirm canonical public URL, selected Analytics account/property, event goals, and access to code and deployment. For a new property, obtain its display name, reporting time zone, and currency from the operator; do not infer business settings from device location.
- Inventory existing Google tags, Tag Manager containers, consent controls, GA4 properties/streams, and any other trackers. Check actually usable account permissions with a read-only probe or visible browser state. A Data API/reporting connector is not necessarily Admin API write access.
- Prefer an authenticated, supported Admin API connection for setup. Browser UI can complete the same task when available and authorized. For API writes, Google documents the `analytics.edit` OAuth scope and appropriate account/property permissions. API enablement or an OAuth grant may need owner setup. Never ask the user to paste passwords, OAuth tokens, service-account keys, or secrets into chat.
- If account access is missing, request the public measurement ID (`G-…`) from an existing web stream, or give the operator the setup steps below. A measurement ID allows tagging but does not grant property creation or report verification. Continue independent code work; report account setup/receipt verification separately as pending.

## Autopilot account setup

1. Confirm the selected existing account and inspect its properties/streams. Reuse the correct property and stream where possible. If multiple candidates match, ask for the choice rather than attaching tracking to the wrong business.
2. When creation is authorized and no suitable property exists, create one in that account with the agreed name, time zone, and currency. Create a WEB data stream with its display name and canonical site URL. Read the stream's generated measurement ID from the response/UI; never guess it.
3. Before retrying a creation after an ambiguous timeout, re-list and reconcile existing resources. Do not blindly duplicate properties or streams. Keep a sanitized record of resource IDs and which steps created or reused them.
4. Obtain any mandatory terms acceptance or new sensitive access grant through the host's required user confirmation flow. Do not enable advertising integrations, Google Signals, cross-domain tracking, extra data sharing, paid services, or broad permissions just because setup is on autopilot.

## Website integration

- Reuse the site's tag architecture: add GA4 through its existing Tag Manager container or a supported framework/Google tag integration. Do not install both paths for the same stream. Keep administrative credentials server-side/out of the repository; the browser measurement ID is public.
- Define a small event plan: page views and the actual primary action. A mailto/contact/booking click can be `contact_click` or `booking_click`; `generate_lead` belongs to a verified completed lead flow, not a click that merely opens another app. Mark agreed key events only when authorized.
- Test client-side navigation and full reloads for duplicate/missing page views. Explicitly coordinate enhanced measurement, automatic configuration page views, manual events, and framework routing. Avoid sending email addresses, form text, client names, sensitive URL/query data, or other personal identifiers.
- Apply [launch privacy guidance](launch.md) to the operator's real markets and data flows. Reuse existing consent controls; when new controls are required, prepare them and factual disclosures without inventing a legal policy. Consent Mode communicates consent state; it does not itself collect consent or establish compliance. Basic mode blocks the Google tag before consent; advanced mode can send cookieless pings while consent is denied. Do not quietly choose advanced mode if the requirement is no pre-consent transmission.
- Restrict test/preview traffic as agreed rather than silently contaminating production reports. Use a test stream or intentional debug traffic where appropriate. Avoid unrelated provider replacement/removal.

## Verification and handoff

- Test the actual browser flow: fresh visit, consent grant/rejection/withdrawal as applicable, page navigation, and the primary action. Inspect relevant storage and collection requests, measurement ID, event name, parameters, and duplicates. Add relevant tests for changed event or consent behavior.
- Confirm receipt in GA4 Realtime/DebugView with actual account access, or the supported reporting API when suitable. A tag in HTML, loaded script, network request, or successful build alone does not prove an event appeared in the selected property. Separate `installed`, `request delivery verified`, and `receipt verified` statuses.
- Without browser/account access, report the exact unverified checks and give the owner a reproducible test. Do not label tracking operational from code inspection alone.
- Record account/property/stream IDs, public measurement ID, installed tag path, event meanings, key-event choices, consent behavior, environments checked, and remaining owner action in the report. Keep secrets out. Include a reversible way to disable the tag, not account deletion.

## Manual fallback for the owner

In Google Analytics Admin, select the correct account/property. If needed, create a property with your business's reporting time zone and currency. Go to Data streams → Add stream → Web, enter the canonical website URL and stream name, and copy the generated `G-…` measurement ID. Labels can change; use the current visible UI. Share only that public ID with the agent. After deployment, visit the site with the intended consent state and check Realtime/DebugView for page and primary-action events.

## Primary references

Checked 2026-10-10; consult current documentation before implementing provider-specific calls.

- [GA4 website setup](https://developers.google.com/analytics/devguides/collection/ga4/web)
- [Admin API property creation](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/properties/create)
- [Admin API web-stream creation](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/properties.dataStreams/create)
- [Tag configuration and page views](https://developers.google.com/analytics/devguides/collection/ga4/reference/config)
- [Consent Mode setup](https://developers.google.com/tag-platform/security/guides/consent)
- [Verify GA4 setup](https://developers.google.com/analytics/devguides/collection/ga4/troubleshoot)
