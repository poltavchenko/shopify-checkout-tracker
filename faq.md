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

No, according to independent researchers. Shopify's own checkout was not broken. The malicious code ran on the storefront, before the Checkout button, through third-party apps. Sources: [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG). We have not found a separate statement from Shopify to merchants.

</details>

<details markdown="1">
<summary>How did the code get onto stores?</summary>

In confirmed cases, through an app's settings: a field like "custom JS" that the app fetches from its own server and runs on the page. The theme code could stay clean. Sources: [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).

</details>

<details markdown="1">
<summary>Which apps have confirmed an incident?</summary>

Hulk Product Options, Selleasy and Swym Wishlist Plus. See the [tracker]({{ '/tracker/' | relative_url }}) for the full list and statuses.

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

A delisting on its own proves nothing. As of 21 Oct, HeyApps counts 429 delisted apps, including one of Shopify's own. Delisting also does not remove the app from your store. Run the checklist and ask the vendor. Sources: [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG).

</details>

<details markdown="1">
<summary>Should I uninstall the app just in case?</summary>

Think first. Swym warns that uninstalling can lose data (wishlists), and Boost asks merchants not to uninstall and reinstall. A safer first step is to turn off the app embed in the theme editor and contact the vendor. Sources: [Swym statement summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack), [Boost status](https://status.boostcommerce.net).

</details>

<details markdown="1">
<summary>What has Shopify done?</summary>

On 15 Oct it released a security check for app developers. On 20 Oct it published "Securing your app, together" for developers, marked Action required. It also says Shopify will tighten the boundaries for storefront app code and raise App Store security requirements. Sources: [15 Oct](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check), [20 Oct](https://shopify.dev/changelog/blog/securing-your-app-together).

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
5. Talk to your payment provider. If customer data may have reached third parties, assess your notification duties with a lawyer (in the EU, GDPR [Art. 33](https://gdpr-info.eu/art-33-gdpr/) and [Art. 34](https://gdpr-info.eu/art-34-gdpr/)).

## For shoppers

If you typed card details on a payment page with an unfamiliar address, contact your bank. Swym says payments through Shop Pay, PayPal, Google Pay and similar wallets were not affected the same way in its incident. Source: [statements summary](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).
