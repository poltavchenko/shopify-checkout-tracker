---
layout: default
title: "Self-check"
lede: "A 15-20 minute check of your own Shopify store. Safe owner actions only. Progress is saved in this browser."
lang: en
slug: checklist
permalink: /checklist/
alt: /uk/checklist/
---

Before you start: do not visit the phishing domains, do not enter real card details while testing, and do not delete anything in a hurry. Only test stores you own or have written permission to test.

## 1. Test checkout as a new shopper (5 min)

- [ ] Open a **new private (incognito) window**.
- [ ] Open your store, add a product to the cart, click Checkout.
- [ ] Look at the address bar. It should show your domain or a Shopify domain (shopify.com, myshopify.com, shop.app). Do not type anything on the page.
- [ ] Close the window and repeat **2 more times**, each in a new private window. The script fires once per visitor. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Try different paths: cart page, cart drawer, quick-buy buttons, phone and desktop. ([Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG), [Flagship](https://flagship.inc/en/columns/shopify-checkout-redirect-third-party-app-security))

Limits: a clean test does not prove past shoppers were safe, and it cannot rule out an attack that targets certain countries, devices or times. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))

Two notes for this test:

- Shopify documents the "Are you sure you want to leave …?" confirmation before an external website. The message alone does not establish a hack or mean the destination is unsafe. If it names an unfamiliar site or appears on Add to cart or Checkout, go back, review recent apps and theme code, and contact Shopify Support. It cannot be turned off or given custom exceptions at this time. Rollout timing, all-store coverage and a link to the incident remain unverified. [Shopify Help Center](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation).
- Test in a real browser. Fetching HTML does not execute storefront JavaScript or test a click on Checkout. A clean HTML scan is not a runtime checkout test.

## 2. Apps (5 min)

- [ ] **Settings > Apps and sales channels**: list every installed app. Compare with the [tracker]({{ '/tracker/' | relative_url }}).
- [ ] Any apps you no longer use? Mark them to turn off (do not uninstall until you know you will not lose data).
- [ ] Open each app's settings and look for **"custom JS"**, **"custom code"**, **"custom HTML"** or **"advanced"** fields. You should know who added every line and why. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG))
- [ ] Change passwords and turn on 2FA for app vendor dashboards, if you have them. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack))
- [ ] Check which AI tools and custom apps have access to your admin and API tokens. Remove what you do not need. ([statements summary, Qikify's advice](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack))

## 3. Theme and theme app extensions (5 min)

- [ ] **Online Store > Themes > Customize > App embeds**: list everything that is on. Temporarily turn off anything unknown or unused, then save.
- [ ] In the same editor, review any **Custom Liquid** blocks in sections.
- [ ] **Online Store > Themes > ... > Edit code**: search all files for `__ctf_`, `checkout-guard`, `.top/check-out`, the domains from the [tracker]({{ '/tracker/' | relative_url }}), and `onerror=`. ([Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Look for theme file edits made by an app that you do not recognize. Shopify keeps older versions of each file, so you can revert them with your developer. ([Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq))
- [ ] Remember: code that an app fetches from its own server when the page loads is **not visible** in theme files. That is why steps 1 and 2 matter more than a code search. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] **Online Store > Navigation**: check menu item labels for HTML or code. One merchant reported code inside menu labels (unverified). ([r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/))

## 4. Custom pixels and app pixels (2 min)

- [ ] **Settings > Customer events**: review custom pixels and app pixels. You should know who added each one and where it sends data.
- [ ] Custom pixels run in a Lax sandbox. Review their code, consent settings and the sandbox limitations. ([Shopify Help Center](https://help.shopify.com/en/manual/promoting-marketing/pixels/custom-pixels), [sandbox limitations](https://help.shopify.com/en/manual/promoting-marketing/pixels/overview#limitations-of-the-pixels-sandbox))

## 5. Checkout and access (3 min)

- [ ] **Settings > Checkout**: confirm the settings and checkout extensions are the ones you expect.
- [ ] **Settings > Users** (staff and collaborator accounts): remove people who no longer need access, turn on 2FA for everyone, give minimum permissions. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Change your Shopify password. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack))

## 6. If you find something

- [ ] Do not type anything on the suspicious page.
- [ ] Save evidence: screenshots, the full address, date and time, the list of enabled apps and app embeds.
- [ ] Temporarily turn off the suspicious app embed or password-protect the storefront (Online Store > Preferences).
- [ ] Contact Shopify Support and the app vendor. Ask in writing for the incident window, the code and the domains.
- [ ] Talk to your payment provider and a lawyer about any duty to notify shoppers or regulators.

App statuses: [tracker]({{ '/tracker/' | relative_url }}). Background: [FAQ]({{ '/faq/' | relative_url }}).
