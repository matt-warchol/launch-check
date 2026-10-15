# Launch Check roadmap

Planned work, not behavior included in the current skill. Each item is tracked as a GitHub issue. Account setup and DNS changes will happen only within the authorization and access available for a specific site.

## New-site Google setup — [to do](https://github.com/matt-warchol/launch-check/issues/1)

Make Search Console and GA4 setup repeatable when launching a new public site. First inspect existing properties, streams, tags, and consent. Reuse the correct resources, select the intended Analytics account/time zone/currency, verify Search Console ownership and sitemap submission, then verify GA4 requests and event receipt. Keep missing access or owner choices visible instead of calling an unverified setup complete.

## New-domain email forwarding — [to do](https://github.com/matt-warchol/launch-check/issues/2)

When a newly deployed project uses a new domain, create or reuse an ImprovMX `hi@<domain>` alias that forwards to an owner-selected inbox. Check the domain's existing mail provider and DNS before changing MX/SPF records; never interrupt working mail silently. Verify the domain, alias, and actual forwarding, and make repeat runs safe. Keep the destination address and API credentials out of the repository.

These are separate from the current launch checks. Neither automation is active simply because it appears here.
