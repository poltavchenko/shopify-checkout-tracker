---
layout: default
title: "Tracker"
lede: "Public reports about the October 2026 checkout hijack and separate earlier incidents, each with a status, a date and a source, plus documented platform updates."
lang: en
slug: tracker
permalink: /tracker/
alt: /uk/tracker/
---

Incident times are in UTC, as in the original sources.

## What the statuses mean

- <span class="badge badge-ok">confirmed by vendor</span> the app developer has publicly acknowledged an incident.
- <span class="badge badge-warn">unconfirmed</span> merchants or researchers report it, but the vendor has not acknowledged it (or we have not found a statement).
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
<p>Not being in this tracker does not mean an app is safe. Only incidents with public reports are listed. <a href="{{ '/checklist/' | relative_url }}">Run the self-check on your store.</a></p>
</div>

| App or episode | Status | Event date | What is known | Source |
|---|---|---|---|---|
| <button type="button" class="app-open" data-app="hulk-product-options">Hulk Product Options (HulkApps)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 10 Oct 2026 | Vendor: "unauthorized configurations" in the theme extension redirected some checkouts to a fake page. Vendor says no other HulkApps app was involved | HulkApps comment on [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (15 Oct); [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack) (19 Oct) |
| <button type="button" class="app-open" data-app="selleasy">Selleasy (Logbase)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 13 Oct 2026, 07:47-15:00 UTC | An unauthorized party accessed an internal tool and added a script to the settings of some stores | [Logbase](https://www.logbase.io/selleasy/updates/incident-20261013) (16 Oct); [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack) (19 Oct) |
| <button type="button" class="app-open" data-app="swym-wishlist-plus">Swym Wishlist Plus</button> | <span class="badge badge-ok">confirmed by vendor</span> | 14 Oct 2026, ~10:06-11:56 UTC | Unauthorized configuration change; fixes fully deployed by 16:32 UTC. On 20 Oct the vendor paused the app for all merchants. At 16:47 UTC on 21 Oct: actively monitoring and continuing to restore merchants in batches | [Swym Security Update](https://www.getswym.com/resources/security-response) (16 Oct); [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (20 Oct); [Swym status](https://status.getswym.com/) (21 Oct) |
| <button type="button" class="app-open" data-app="qikify">Qikify</button> | <span class="badge badge-ok">confirmed by vendor</span> | 22 Jul 2026 | Separate July incident, resolved the same day per the vendor; apps relisted on 21 Aug. The vendor says it is not part of the October wave | [Qikify](https://qikify.com/pages/security-incident-notice); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (list; Lauren-Qikify comment, 16 Oct) |
| <button type="button" class="app-open" data-app="hextom">Hextom</button> | <span class="badge badge-warn">unconfirmed</span> | August 2026 | Zipp and Taylor Page describe a similar incident resolved in August. We have not opened a vendor statement | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19 Oct); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20 Oct) |
| <button type="button" class="app-open" data-app="orichi">Orichi (OC Quantity Breaks &amp; Limit)</button> | <span class="badge badge-ok">confirmed by vendor</span> | 11 Sep 2026 | Separate September incident: malicious code redirected shoppers to shopfily[.]shop; removed the same day. Relisted on 8 Oct. A link to the October wave is unverified | [Orichi incident notice](https://orichi.crisp.help/en/article/malicious-code-served-to-storefronts-through-oc-quantity-breaks-limit-ep2drz/) (8 Oct report; URL returns 404 when checked 21 Oct) |
| <button type="button" class="app-open" data-app="boost">Boost AI Search & Filter</button> | <span class="badge badge-warn">unconfirmed</span> | 17 Oct 2026 | Merchants report a redirect. The vendor's status page reports an incident on 17-18 Oct and a disabled theme extension, with no mention of security. On 19 Oct at 15:53 UTC it reported storefront functionality restored since 18 Oct, 18:48 UTC | [Shopify Community 698208](https://community.shopify.com/t/urgent-checkout-phishing-redirect-anyone-else-affected/698208) (#16, 17 Oct); [Boost status](https://status.boostcommerce.net) (19 Oct) |
| <button type="button" class="app-open" data-app="privy">Privy</button> | <span class="badge badge-warn">unconfirmed</span> | 17 Oct 2026 | One merchant reports a redirect. Privy's status page reports popups and embedded forms restored on 19 Oct at 20:28 UTC (16:28 EDT), with no security finding | Comment on [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (17 Oct); [Privy status](https://status.privy.com) (19 Oct) |
| <button type="button" class="app-open" data-app="consentmo">Consentmo GDPR Compliance</button> | <span class="badge badge-warn">unconfirmed</span> | 19-20 Oct 2026 | Zipp cites a confidential source; one merchant comment | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19-20 Oct) |
| <button type="button" class="app-open" data-app="17track">17TRACK Order Tracking</button> | <span class="badge badge-warn">unconfirmed</span> | 20 Oct 2026 | A merchant reports code in navigation menu labels and the checkout button, domain cartassure[.]top; a merchant says Shopify identified 17TRACK (not publicly confirmed). Zipp lists it as "unconfirmed but de-listed"; Urban Alcove's comments on Zipp (21 Oct) say 17TRACK "maybe compromised" and name the same domain. Whether the reports concern different stores is unverified. HeyApps shows it delisted on 20 Oct. No public statement from the vendor or Shopify | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/); [merchant update](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/comment/phy8mey/) (20-21 Oct); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (21 Oct); [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21 Oct) |
| <button type="button" class="app-open" data-app="color-swatch-king">Color Swatch King (StarApps)</button> | <span class="badge badge-warn">unconfirmed</span> | Reported 18 Oct 2026, 23:24 UTC | A merchant calls the app "swathe king" and says the redirect code was inside it. App identity and incident attribution are unconfirmed | [Merchant comment](https://www.reddit.com/r/shopify/comments/1x8m5d8/comment/phlefr5/) (18 Oct) |
| <button type="button" class="app-open" data-app="hulk-advanced-wishlist">Hulk Advanced Wishlist</button> | <span class="badge badge-warn">unconfirmed</span> | a few weeks before 10 Oct 2026 (per the merchant) | One merchant reports the whole store redirecting to a spam site | [r/shopify](https://www.reddit.com/r/shopify/comments/1x2f4kx/comment/pf4d079/) (10 Oct) |
| <button type="button" class="app-open" data-app="unknown-checkout-guard">Unknown app, three stores of one owner</button> | <span class="badge badge-warn">unconfirmed</span> | 19 Oct 2026 | Redirect to checkout-guard[.]top, source not found | [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) (19 Oct) |
| <button type="button" class="app-open" data-app="rebuy">Rebuy Personalization Engine</button> | <span class="badge badge-off">removed without report</span> | 18 Oct 2026 | Delisted. Taylor Page says Rebuy's scripts came back clean on his client stores | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21 Oct); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20 Oct) |
| <button type="button" class="app-open" data-app="shopify-product-network">Shopify Product Network (Shopify's own app)</button> | <span class="badge badge-off">removed without report</span> | 15 Oct 2026 | Delisted | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21 Oct) |
{: #apps-table}

The separate [HeyApps catalog]({{ '/apps/' | relative_url }}) contains {{ site.data.heyapps.counts.delisted }} delisted and {{ site.data.heyapps.counts.recovered }} listed-again apps in the snapshot captured at {{ site.data.heyapps.captured_local }}. Being delisted does not by itself mean an app was compromised. Being listed again does not establish safety. See [Roman Zipp's 22 Oct update](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) on the limits of delisting evidence.

All apps in this snapshot were delisted between 14 and 21 Oct 2026. [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) gives no reasons for the individual delistings.

## Platform observations

| Platform change | Source status | Checked | What is known | Source |
|---|---|---|---|---|
| Storefronts: leave-store confirmation | announced by Shopify; all-store coverage not verified | 20 Oct 2026 (changelog announcement; checked 22 Oct) | An "Are you sure you want to leave [store name]?" confirmation can open when shoppers click links to other websites. Shopify documents it as protection against code that sends shoppers to a fake checkout or phishing site. Merchants cannot turn it off or choose websites that skip it at this time. Merchants report store switchers, headless redirects and partner links are affected. Coverage of all stores and any link to the checkout redirect incident: not verified | [Shopify changelog, 20 Oct](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects); [Shopify Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation); [Developer community 38776](https://community.shopify.dev/t/shopify-exit-interstitial-popup-modal/38776); [r/shopify](https://www.reddit.com/r/shopify/comments/1xbncwn/) |

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
- 20 Oct 2026: Shopify announced its [leave-store confirmation](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects). Its [Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation) describes the controls and exceptions. Checked 22 Oct: the message cannot be turned off or given custom exceptions. All-store coverage and a link to the checkout incident are unverified; the changelog does not mention the incident.
- As of 21 Oct 2026 we have not found a separate merchant notice about the checkout incident.
