---
layout: default
title: "Tracker"
lede: "Public reports and labeled merchant submissions about checkout hijacking and other incidents, with documented platform updates."
lang: en
slug: tracker
permalink: /tracker/
alt: /uk/tracker/
---

Incident times are in UTC, as in the original sources.

## What the statuses mean

- <span class="badge badge-ok">confirmed by vendor</span> the app developer has publicly acknowledged an incident.
- <span class="badge badge-warn">unconfirmed</span> merchants or researchers report it, but we have not verified a public vendor statement.
- <span class="badge badge-off">removed without report</span> the app is no longer listed on the Shopify App Store, and neither the vendor nor merchants link it to this incident.
{: .legend}

A documented Shopify platform update is not an app incident status.

A delisting does not mean an app was compromised, and it does not remove the app from stores that already have it.

## Table

<div class="search" id="app-search" role="search" hidden>
<label for="q" class="sr-only">Search apps by name or developer</label>
<svg class="search-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="M20 20l-3.5-3.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
<input id="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search apps or developers...">
<button type="button" class="search-clear" aria-label="Clear search" hidden>&times;</button>
<kbd class="search-kbd" aria-hidden="true">/</kbd>
</div>
<p class="search-count" id="search-count" aria-live="polite"></p>
<div class="search-empty" id="search-empty" hidden>
<p><strong>No apps match your search.</strong></p>
<p>Not being in this tracker does not mean an app is safe. Reports and their source limits are labeled in each row. <a href="{{ '/checklist/' | relative_url }}">Run the self-check on your store.</a></p>
</div>

| App or episode | Status | Event date | What is known | Source |
|---|---|---|---|---|
| <button type="button" class="app-open" data-app="triple-whale">Triple Whale</button> | <span class="badge badge-warn">unconfirmed</span> | 30 Oct-1 Nov 2026 reported; merchant submission 4 Nov | **Merchant-reported data incident.** A merchant reports a direct vendor response describing unauthorized access and customer-data exfiltration; we have not authenticated the original correspondence. On 12 Nov, Geek Native reported that Sneak Energy notified customers of access to customer contact details and total spend at its analytics provider Triple Whale between 30 Oct and 1 Nov. According to that report, the merchant did not know if data was copied. We have not found a public vendor incident statement or established a link to checkout hijacking. HeyApps reports delisting on 2 Nov; Shopify says the app is unavailable (checked 18 Nov). Availability does not establish a compromise | Merchant-supplied text (4 Nov, original not independently authenticated); [Geek Native](https://www.geeknative.com/244332/dungeons-dragons-partner-sneak-energy-reports-customer-data-breach-starting-on-launch-day/) (12 Nov, reporting a customer notice); [HeyApps](https://heyapps.dev/apps/triplewhale-1); [Shopify App Store](https://apps.shopify.com/triplewhale-1) |
| <button type="button" class="app-open" data-app="hulk-product-options">Hulk Product Options, Variants (HulkApps)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 10 Oct 2026 | Vendor: "unauthorized configurations" in the theme extension redirected some checkouts to a fake page. Vendor says no other HulkApps app was involved. [HeyApps](https://heyapps.dev/apps/delisted?view=recovered) reports the app listed again on 28 Oct; that does not establish security | HulkApps comment on [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (15 Oct); [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack) (19 Oct) |
| <button type="button" class="app-open" data-app="selleasy">Selleasy (Logbase)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 13 Oct 2026 | Vendor: an unauthorized script was added through a legacy support tool; redirects stopped at 12:22 UTC and affected stores were cleaned by 15:58 UTC. Logbase reports an independent assessment and re-listing on 27 Oct; [HeyApps](https://heyapps.dev/apps/delisted?view=recovered) reports 26 Oct. A return does not establish security | [Logbase](https://www.logbase.io/selleasy/updates/incident-20261013) (updated 28 Oct) |
| <button type="button" class="app-open" data-app="swym-wishlist-plus">Swym Wishlist Plus</button> | <span class="badge badge-ok">confirmed by vendor</span> | 14 Oct 2026, ~10:06-11:56 UTC | Unauthorized configuration change; fixes fully deployed by 16:32 UTC. On 20 Oct the vendor paused the app for all merchants. 27 Oct, 14:41 UTC: Swym reports security patches applied and access open to all merchant stores; a third-party audit was in progress. HeyApps reports it listed again on 6 Nov; the Shopify listing offers installation. Relisting does not establish security | [Swym Security Update](https://www.getswym.com/resources/security-response) (16 Oct); [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (20 Oct); [Swym status](https://status.getswym.com/) (27 Oct; checked 30 Oct); [HeyApps](https://heyapps.dev/apps/delisted?view=recovered); [Shopify App Store](https://apps.shopify.com/swym-relay) |
| <button type="button" class="app-open" data-app="qikify">Qikify</button> | <span class="badge badge-ok">confirmed by vendor</span> | 22 Jul 2026 | Separate July incident, resolved the same day per the vendor; apps relisted on 21 Aug. The vendor says it is not part of the October wave | [Qikify](https://qikify.com/pages/security-incident-notice); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (list; Lauren-Qikify comment, 16 Oct) |
| <button type="button" class="app-open" data-app="hextom">Hextom</button> | <span class="badge badge-warn">unconfirmed</span> | August 2026 | Zipp and Taylor Page describe a similar incident resolved in August. We have not opened a vendor statement | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19 Oct); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20 Oct) |
| <button type="button" class="app-open" data-app="orichi">Orichi (OC Quantity Breaks &amp; Limit)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 11 Sep 2026 | Separate September incident: malicious code redirected shoppers to shopfily[.]shop; removed the same day. Relisted on 8 Oct. A link to the October wave is unverified | [Orichi incident notice](https://orichi.crisp.help/en/article/malicious-code-served-to-storefronts-through-oc-quantity-breaks-limit-ep2drz/) (8 Oct report; URL returns 404 when checked 21 Oct) |
| <button type="button" class="app-open" data-app="boost">Boost AI Search & Filter</button> | <span class="badge badge-warn">unconfirmed</span> | 17 Oct 2026 | Merchants report a redirect. The vendor status page reported an incident and disabled theme extension, without a security finding; functionality was restored on 18 Oct. HeyApps reports the app listed again on 9 Nov, and Shopify offers installation (checked 18 Nov). Relisting does not establish safety or incident attribution | [Shopify Community 698208](https://community.shopify.com/t/urgent-checkout-phishing-redirect-anyone-else-affected/698208) (17 Oct); [Boost status](https://status.boostcommerce.net); [HeyApps](https://heyapps.dev/apps/product-filter-search); [Shopify App Store](https://apps.shopify.com/product-filter-search) |
| <button type="button" class="app-open" data-app="privy">Privy</button> | <span class="badge badge-warn">unconfirmed</span> | 17 Oct 2026 | One merchant reports a redirect. Privy's status page reports popups and embedded forms restored on 19 Oct at 20:28 UTC (16:28 EDT), with no security finding | Comment on [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (17 Oct); [Privy status](https://status.privy.com) (19 Oct) |
| <button type="button" class="app-open" data-app="consentmo">Consentmo GDPR Compliance</button> | <span class="badge badge-warn">unconfirmed</span> | 19-20 Oct 2026 | Zipp cites a confidential source; one merchant comment. [HeyApps](https://heyapps.dev/apps/delisted?view=recovered) reports the app listed again on 28 Oct; incident attribution remains unconfirmed | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19-20 Oct) |
| <button type="button" class="app-open" data-app="17track">17TRACK Order Tracking</button> | <span class="badge badge-warn">unconfirmed</span> | 20 Oct 2026 | A merchant reported code in menu labels and a checkout button. Sansec reports that a recorded store had malicious code in a menu item linking to 17TRACK; it says whether the app's access was used remains unconfirmed. HeyApps reports delisting on 20 Oct and relisting on 27 Oct. Relisting does not establish safety; no public vendor or Shopify statement about the attribution was found | [Merchant update](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/comment/phy8mey/); [Sansec](https://sansec.io/research/shopify-app-supply-chain-attack) (checked 18 Nov); [HeyApps](https://heyapps.dev/apps/17track) |
| <button type="button" class="app-open" data-app="color-swatch-king">Color Swatch King (StarApps)</button> | <span class="badge badge-warn">unconfirmed</span> | 17-18 Oct 2026 | Sansec reports malicious scripts in this app's settings on 44 observed stores on 17 Oct; its findings and the access path have not been independently verified here, and no public vendor statement was found. Separately, a merchant used the name "swathe king"; that report's app identity is unverified. HeyApps reports relisting on 6 Nov; relisting does not establish safety | [Sansec](https://sansec.io/research/shopify-app-supply-chain-attack) (checked 18 Nov); [merchant comment](https://www.reddit.com/r/shopify/comments/1x8m5d8/comment/phlefr5/) (18 Oct); [HeyApps](https://heyapps.dev/apps/variant-swatch-king) |
| <button type="button" class="app-open" data-app="hulk-advanced-wishlist">Hulk Advanced Wishlist</button> | <span class="badge badge-warn">unconfirmed</span> | a few weeks before 10 Oct 2026 (per the merchant) | One merchant reports the whole store redirecting to a spam site | [r/shopify](https://www.reddit.com/r/shopify/comments/1x2f4kx/comment/pf4d079/) (10 Oct) |
| <button type="button" class="app-open" data-app="unknown-checkout-guard">Unknown app, three stores of one owner</button> | <span class="badge badge-warn">unconfirmed</span> | 19 Oct 2026 | Redirect to checkout-guard[.]top, source not found | [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) (19 Oct) |
| <button type="button" class="app-open" data-app="rebuy">Rebuy Personalization Engine</button> | <span class="badge badge-off">removed without report</span> | 18 Oct 2026 | Delisted. Taylor Page says Rebuy's scripts came back clean on his client stores | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21 Oct); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20 Oct) |
| <button type="button" class="app-open" data-app="shopify-product-network">Shopify Product Network (Shopify's own app)</button> | <span class="badge badge-off">removed without report</span> | 15 Oct 2026 | Delisted | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21 Oct) |
| <button type="button" class="app-open" data-app="aftersell">Aftersell (Rokt)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 21 Oct 2026 | Aftersell (part of Rokt) reports unauthorized access to some merchant upsell configurations, staff email addresses and discount codes. The vendor says no shopper personal data was compromised, no malware or phishing was involved, and this incident is separate from the phishing attacks elsewhere in the Shopify ecosystem. It says the vulnerability was patched; its app remained functional for existing merchants but was temporarily unavailable on the Shopify App Store during a security review with Shopify. Vendor statement, not an independent audit. [HeyApps](https://heyapps.dev/apps/delisted?view=recovered) reports it listed again on 30 Oct; that does not establish security. | [Aftersell](https://www.aftersell.com/blog/incident-disclosure-protecting-our-merchants-and-their-customers) |
{: #apps-table}

[Sansec](https://sansec.io/research/shopify-app-supply-chain-attack) also reports a script in AVADA Air Reviews on 23 observed stores on 9 Oct and a test script in Trustify Reviews on two stores on 11 Sep. These are researchers' findings, checked against their report on 18 Nov; we found no public statements from those vendors and have not independently verified the cases.

The separate [HeyApps catalog]({{ '/apps/' | relative_url }}) contains {{ site.data.heyapps.counts.delisted }} delisted and {{ site.data.heyapps.counts.recovered }} listed-again apps in the snapshot captured at {{ site.data.heyapps.captured_local }}. Being delisted does not by itself mean an app was compromised. Being listed again does not establish safety. See [Roman Zipp's 22 Oct update](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) on the limits of delisting evidence.

All apps in this snapshot were delisted between 14 Oct and 18 Nov 2026. [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) gives no reasons for the individual delistings.

## Platform observations

| Platform change | Source status | Checked | What is known | Source |
|---|---|---|---|---|
| Storefronts: link protection | documented by Shopify | Announced 20 Oct; updated 23 Oct; checked 30 Oct 2026 | Shopify says links to sites it identifies as malicious are blocked, suspicious sites may trigger confirmation, and other sites open directly. Its Help Center says protection is on for all online stores; we have not independently verified coverage. The changelog does not link it to the checkout incident | [Shopify changelog](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects); [Shopify Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation) |

## Known phishing domains (do not visit)

| Domain | Source |
|---|---|
| biliing[.]top, checkout-confirm[.]top, order-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/) |
| account-confirm[.]top, billing-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) |
| checkout-guard[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) |
| checkout-secure[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (single source) |
| cartassure[.]top | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/) (20 Oct); Urban Alcove's comments on [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (21 Oct). Unverified: two public mentions; whether they concern different stores is unknown |

## What Shopify has done

- 15 Oct 2026: `shopify app security check` for app developers. [Shopify changelog](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check)
- 20 Oct 2026: "Securing your app, together", Action required for all app developers. It does not name the incident or any app. [Shopify changelog](https://shopify.dev/changelog/blog/securing-your-app-together)
- 20 Oct 2026: Shopify announced [link protection](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects). Its 23 Oct update says malicious links are blocked, suspicious sites may require confirmation, and other sites open directly. The [Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation) says protection is on for all online stores; independent coverage was not verified. The changelog does not mention the incident.
- 14 Nov 2026: Shopify said public apps calling the Admin API must enable an IP allowlist by 20 Nov at 11:59 PM ET. Apps without one will be delisted and blocked from new installs; existing installs keep working. This is a platform requirement, not evidence of an incident. [Shopify](https://shopify.dev/changelog/blog/app-security-updates-thank-you-plus-what-s-required-next)
- As of 21 Oct 2026 we have not found a separate merchant notice about the checkout incident.
