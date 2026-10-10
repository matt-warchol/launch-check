# Privacy, terms, and GDPR pages

Run this module for each website build/launch, and for requested legal-page audits or implementation. Produce/adapt simple, site-specific drafts using the templates below; reuse approved existing policies rather than adding contradictory copies. A GDPR notice can be integrated into the privacy policy when applicable. Three separate pages are not a universal legal requirement.

“Anonymize” means remove the reference company's identifying and operational details from reusable templates. The published site must identify its actual operator/controller where required; do not publish an anonymous controller or hide necessary contact information.

## Establish facts before drafting

Inspect the website, repository, integrations, consent implementation, and available provider configuration. Reuse known project facts; ask one concise bundled question for unresolved material facts. Keep drafts moving while answers are pending.

- Operator's legal identity, address, relevant registration details, public contact, privacy contact, and DPO/representative only if applicable.
- Website purpose, countries/audiences, marketing-only versus paid service/store, contracts, download permissions, and operator-approved governing-law/dispute choices. Device location is not jurisdiction evidence.
- Data activities and sources: logs, contact email/forms, newsletter, accounts, purchases, recruitment, uploads, analytics, and embeds only where used.
- Actual providers and roles, recipients, retention periods or meaningful criteria, locations/transfers and verified safeguards, legal grounds per activity, required/optional data, and relevant automated decisions.
- Cookies, storage and tracking: provider, purpose, duration, consent behavior, withdrawal route, and linkable preferences control. Inspect behavior, not just a provider's marketing label.

Do not invent retention periods, lawful bases, processors, transfer guarantees, a DPO, a registered address, or a blanket no-data/no-sharing promise. Missing facts remain in an internal gap list and draft placeholders. A consent banner or policy alone is not GDPR compliance.

## Neutral starter documents

- [Privacy Policy template](../assets/privacy-policy-template.md): operator, processing table, cookies, sharing/transfers, retention, rights, and contact.
- [Terms of Use template](../assets/terms-of-use-template.md): website scope, acceptable use, content/download permissions, applicable services, availability, contact, and disputes.
- [GDPR notice template](../assets/gdpr-notice-template.md): relevant transparency information and rights; use only where applicable, separately or merged without conflicting duplication.

These are original plain-language drafting scaffolds informed by the supplied references, not verbatim copies or ready-to-publish legal advice. Preserve necessary information while simplifying sentences and removing irrelevant sections. Expand the processing table from verified facts; the template's short length is not a completeness target.

## Adapt safely

Remove Brainhub branding, domain, legal entity/address, tax/registration numbers, share capital, privacy mailbox, vendor lists, recruitment details, and Polish governing-law assumptions from generated documents. Keep source attribution links only in internal notes, not as the new site's operator identity.

The supplied GDPR page covers recruitment: do not imply every marketing page collects CVs or conducts hiring. The supplied privacy/terms describe advertising and particular providers: do not copy them into sites that lack those integrations. Do not describe cookies as necessarily encrypted or IP/cookie identifiers as necessarily anonymous.

Match download licensing to the actual offer: commercial starter playbooks must not accidentally become personal-use-only materials. Do not transplant broad warranty/liability waivers or jurisdiction clauses without operator decisions and appropriate review. A marketing website's terms must not quietly replace a paid SaaS/service contract.

Where GDPR applies, check the relevant transparency requirements against current primary guidance. Where consumer, employment, regulated, sensitive-data, or other legal complexity matters, identify the specific review needed. Do not require a generic legal approval ceremony for every reversible edit; pause only unresolved publication or the consequential decision, honoring authorization already given.

## Add to the website and verify

1. Draft pages at the site's established routes, commonly `/privacy-policy/`, `/terms-of-use/`, and `/gdpr-privacy-policy/` if a separate notice is useful/applicable. Preserve established URLs or add intentional redirects when changing them.
2. Add visible footer links; connect consent settings and relevant forms to the privacy notice. Do not treat merely reading terms/privacy as consent to optional tracking. Match [GA4 behavior](google-analytics.md) and [launch privacy checks](launch.md).
3. Give pages clear headings, accessible reading layout, effective dates, canonical metadata, and sitemap/internal discovery where indexable. Include new public pages in any existing Markdown negotiation/agent-discovery scheme as appropriate; test rather than assume route coverage.
4. Before publication, review actual facts, all `{{placeholders}}`, draft markers, source-company leftovers, links, and contradictions against runtime behavior. Do not deploy unresolved placeholders or unsupported promises. Publication follows the user's actual authorization; existing authorization need not be requested again.
5. Add relevant regression tests for changed routes, footer links, correct operator identity, unresolved placeholders, and policy/consent behavior. Verify each live legal endpoint's status and meaningful body after an authorized release. Test consent rejection/withdrawal and actual storage/network behavior separately from policy text.
6. Handoff: record pages/draft status, source/date, confirmed operator facts, unresolved facts, applicable jurisdictions, evidence limits, owner actions, and any required review. Report “drafted” or “verified against observed behavior,” not “legally compliant” from templates alone.

## Sources reviewed 2026-10-10

User-supplied reference templates (not legal authority):

- [Brainhub terms](https://brainhub.eu/terms-of-service)
- [Brainhub privacy policy](https://brainhub.eu/privacy-policy)
- [Brainhub recruitment GDPR notice](https://brainhub.eu/gdpr-privacy-policy)

Current primary guidance; recheck for the site's jurisdiction:

- [European Commission: privacy information and individual rights](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en)
- [European Commission: legal grounds](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en)
- [European Commission: GDPR application and personal data](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en)
- [EDPB cookie-banner taskforce report](https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf)
