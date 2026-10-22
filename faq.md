---
layout: default
title: "FAQ"
lede: "What is known, what is not, and what to do. Plain language, with sources."
lang: en
slug: faq
permalink: /faq/
alt: /uk/faq/
---

## What is known

<details markdown="1">
<summary>What happened?</summary>

Since about 10 Oct 2026, on some Shopify stores, shoppers who clicked Checkout were sent to a fake payment page on another domain. Card details were collected there, then the shopper was sent back to the real checkout. Sources: [Roman Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/).

</details>

<details markdown="1">
<summary>Was Shopify hacked?</summary>

No, according to independent researchers. Shopify's own checkout was not broken. The malicious code ran on the storefront, before the Checkout button, through third-party apps. Sources: [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG). We have not found a separate statement from Shopify to merchants about this checkout incident.

</details>

<details markdown="1">
<summary>How did the code get onto stores?</summary>

In confirmed cases, through an app's settings: a field like "custom JS" that the app fetches from its own server and runs on the page. The theme code could stay clean. Sources: [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).

</details>

<details markdown="1">
<summary>Which apps have confirmed an incident?</summary>

For October 2026: Hulk Product Options, Selleasy and Swym Wishlist Plus. Qikify (July) and Orichi (September) published separate earlier incident reports. See the [tracker]({{ '/tracker/' | relative_url }}) for the full list and statuses.

</details>

<details markdown="1">
<summary>Why does my own test show nothing?</summary>

The script fires once per visitor. After the first redirect it sets a flag in the browser and leaves that tab alone. A second test in the same tab shows nothing. Test in a new private window every time. Sources: [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/).

</details>

<details markdown="1">
<summary>My orders look normal. Am I fine?</summary>

Not necessarily. After the fake page, shoppers were sent back to the real checkout, so orders could look normal in the admin. Source: [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903).

</details>

<details markdown="1">
<summary>An app I use was delisted. Was I hacked?</summary>

A delisting on its own proves nothing. [HeyApps lists {{ site.data.heyapps.counts.delisted }} delisted apps in the catalog snapshot]({{ '/apps/' | relative_url }}) captured at {{ site.data.heyapps.captured_local }}, including one of Shopify's own. Delisting also does not remove the app from your store. Run the checklist and ask the vendor. Sources: [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG).

</details>

<details markdown="1">
<summary>Should I uninstall the app just in case?</summary>

Check with the vendor first. Swym's 20 Oct FAQ says pausing access does not delete wishlist data. Its 21 Oct status reports restoration in batches. Boost asks merchants not to uninstall and reinstall. Temporarily turn off a suspicious app embed in the theme editor while you investigate. Sources: [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Swym status](https://status.getswym.com/), [Boost status](https://status.boostcommerce.net).

</details>

<details markdown="1">
<summary>What has Shopify done?</summary>

On 15 Oct it released a security check for app developers. On 20 Oct it published "Securing your app, together" for developers, marked Action required. It also says Shopify will tighten the boundaries for storefront app code and raise App Store security requirements. Sources: [15 Oct](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check), [20 Oct](https://shopify.dev/changelog/blog/securing-your-app-together).

</details>
<details markdown="1">
<summary>My store asks "Are you sure you want to leave?" on an external link. Was my store hacked?</summary>

Not by itself. Shopify announced this confirmation on 20 Oct 2026. It names the other website and does not open for the store's domains and their subdomains listed in Shopify admin, its checkout, Shopify pages or popular social networks. The message does not mean the other website is unsafe. As checked on 22 Oct, it cannot be turned off, and merchants cannot choose websites that skip it.

Investigate when it names an unfamiliar website or appears on a button that should keep shoppers on your store, such as Add to cart or Checkout. Review recently installed or updated apps and your theme code. Contact Shopify Support with the page, the destination and a screenshot. All-store coverage and any link to the checkout incident remain unverified. The changelog does not mention the incident. Sources: [Shopify changelog, 20 Oct](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects), [Shopify Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation), [Developer community](https://community.shopify.dev/t/shopify-exit-interstitial-popup-modal/38776).

</details>

## Not known yet

- Exactly how the code got into each app, and whether it is one campaign.
- The full list of apps and how many stores were affected.
- Why most of the delisted apps were removed.
- Where the redirect came from on stores that had none of the known apps.

## If you find something

1. Do not enter anything on the suspicious page and do not visit the phishing domains.
2. Save evidence: screenshots, the full page address, date and time, which apps and app embeds are on.
3. Temporarily turn off suspicious app embeds or put the storefront behind a password.
4. Contact Shopify Support and the app vendor. Ask in writing for the incident window, the code that ran and the domains.
5. Talk to your payment provider. If customer data may have reached third parties, assess your notification duties with a lawyer (in the EU, GDPR [Art. 33](https://eur-lex.europa.eu/eli/reg/2016/679/) and [Art. 34](https://eur-lex.europa.eu/eli/reg/2016/679/)).

## For shoppers

If you typed card details on a payment page with an unfamiliar address, contact your bank. Swym says payments through Shop Pay, PayPal, Google Pay and similar wallets were not affected the same way in its incident. Source: [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).
