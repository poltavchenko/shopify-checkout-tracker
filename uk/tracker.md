---
layout: default
title: "Трекер"
lede: "Застосунки й епізоди, пов'язані з перехопленням checkout у жовтні 2026: статус, дата і публічне джерело в кожному рядку."
lang: uk
slug: tracker
permalink: /uk/tracker/
alt: /tracker/
---

Час інцидентів подано в UTC, як у першоджерелах.

## Що це за статуси

- <span class="badge badge-ok">підтверджено вендором</span> розробник застосунку публічно визнав інцидент.
- <span class="badge badge-warn">не підтверджено</span> є повідомлення мерчантів чи дослідників, але вендор інцидент не визнав (або ми не знайшли заяви).
- <span class="badge badge-off">знято без звіту</span> застосунок зник з Shopify App Store, але ні вендор, ні мерчанти не пов'язують його з цим інцидентом.
{: .legend}

Зняття з App Store не означає злам і не видаляє застосунок з магазинів, де він уже встановлений.

## Таблиця

<div class="search" id="app-search" role="search" hidden>
<label for="q" class="sr-only">Пошук застосунків за назвою або розробником</label>
<svg class="search-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="M20 20l-3.5-3.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
<input id="q" type="search" autocomplete="off" spellcheck="false" placeholder="Пошук застосунку чи розробника...">
<button type="button" class="search-clear" aria-label="Очистити пошук" hidden>&times;</button>
<kbd class="search-kbd" aria-hidden="true">/</kbd>
</div>
<p class="search-count" id="search-count" aria-live="polite"></p>
<div class="search-empty" id="search-empty" hidden>
<p><strong>Нічого не знайдено.</strong></p>
<p>Відсутність у трекері не означає, що застосунок безпечний. Тут лише випадки з публічними повідомленнями. <a href="{{ '/uk/checklist/' | relative_url }}">Пройдіть самоперевірку свого магазину.</a></p>
</div>

| Застосунок або епізод | Статус | Дата події | Що відомо | Джерело |
|---|---|---|---|---|
| <button type="button" class="app-open" data-app="hulk-product-options">Hulk Product Options (HulkApps)</button> | <span class="badge badge-ok">підтверджено вендором</span> | 10.10.2026 | Вендор: "unauthorized configurations" у theme extension, частину переходів на checkout перенаправлено на підроблену сторінку. Інші застосунки HulkApps, за словами вендора, не причетні | Коментар HulkApps у [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (15.10); [зведення заяв](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack) (19.10) |
| <button type="button" class="app-open" data-app="selleasy">Selleasy (Logbase)</button> | <span class="badge badge-ok">підтверджено вендором</span> | 13.10.2026, 07:47-15:00 UTC | Сторонній отримав доступ до внутрішнього інструменту і додав скрипт у налаштування частини магазинів | [Logbase](https://www.logbase.io/selleasy/updates/incident-20261013) (16.10); [зведення заяв](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack) (19.10) |
| <button type="button" class="app-open" data-app="swym-wishlist-plus">Swym Wishlist Plus</button> | <span class="badge badge-ok">підтверджено вендором</span> | 14.10.2026, ~10:06-16:32 UTC | Несанкціонована зміна конфігурації. 20.10 вендор поставив застосунок на паузу для всіх мерчантів | [Swym Security Update](https://www.getswym.com/resources/security-response) (16.10); [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (20.10) |
| <button type="button" class="app-open" data-app="qikify">Qikify</button> | <span class="badge badge-ok">підтверджено вендором</span> | липень 2026 | Схожий інцидент, вирішено до серпня. Вендор каже, що це не частина жовтневої хвилі | [Qikify](https://qikify.com/pages/security-incident-notice); коментар Qikify у [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (16.10) |
| <button type="button" class="app-open" data-app="hextom">Hextom</button> | <span class="badge badge-warn">не підтверджено</span> | серпень 2026 | Zipp і Taylor Page пишуть про схожий інцидент, вирішений у серпні. Заяви вендора ми не відкривали | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19.10); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20.10) |
| <button type="button" class="app-open" data-app="boost">Boost AI Search & Filter</button> | <span class="badge badge-warn">не підтверджено</span> | 17.10.2026 | Мерчанти пишуть про редирект. Вендор на статус-сторінці повідомив про інцидент 17-18.10 і вимкнення theme extension, без згадки про безпеку | [Shopify Community 698208](https://community.shopify.com/t/urgent-checkout-phishing-redirect-anyone-else-affected/698208) (#16, 17.10); [статус Boost](https://status.boostcommerce.net) (19.10) |
| <button type="button" class="app-open" data-app="privy">Privy</button> | <span class="badge badge-warn">не підтверджено</span> | 17.10.2026 | Один мерчант пише про редирект. Статус-сторінка Privy 19.10: форми не показуються, без згадки про безпеку | Коментар у [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (17.10); [статус Privy](https://status.privy.com) (19.10) |
| <button type="button" class="app-open" data-app="consentmo">Consentmo GDPR Compliance</button> | <span class="badge badge-warn">не підтверджено</span> | 19-20.10.2026 | Zipp посилається на конфіденційне джерело, один коментар мерчанта | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19-20.10) |
| <button type="button" class="app-open" data-app="17track">17TRACK Order Tracking</button> | <span class="badge badge-warn">не підтверджено</span> | 20.10.2026 | Мерчант пише про код у назвах пунктів меню і на кнопці checkout, домен cartassure[.]top; за його словами, Shopify назвав джерелом цей застосунок. Zipp позначає його як "unconfirmed but de-listed"; інший мерчант у коментарі до Zipp (21.10) пише, що 17TRACK "maybe compromised". HeyApps показує зняття 20.10. Публічної заяви вендора чи Shopify немає | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/) (20-21.10); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (21.10); [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10) |
| <button type="button" class="app-open" data-app="color-swatch-king">Color Swatch King (StarApps)</button> | <span class="badge badge-warn">не підтверджено</span> | 17-19.10.2026 | Один мерчант пише, що код був у цьому застосунку. Заяв вендора немає | [r/shopify](https://www.reddit.com/r/shopify/comments/1x8m5d8/shopify_issues/) (19.10) |
| <button type="button" class="app-open" data-app="hulk-advanced-wishlist">Hulk Advanced Wishlist</button> | <span class="badge badge-warn">не підтверджено</span> | за кілька тижнів до 10.10.2026 (за словами мерчанта) | Один мерчант пише про редирект магазину на спам-сайт | [r/shopify](https://www.reddit.com/r/shopify/comments/1x2f4kx/) (10.10) |
| <button type="button" class="app-open" data-app="unknown-checkout-guard">Невідомий застосунок, три магазини одного власника</button> | <span class="badge badge-warn">не підтверджено</span> | 19.10.2026 | Редирект на checkout-guard[.]top, джерело не знайдено | [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) (19.10) |
| <button type="button" class="app-open" data-app="rebuy">Rebuy Personalization Engine</button> | <span class="badge badge-off">знято без звіту</span> | 18.10.2026 | Знято з App Store. Taylor Page пише, що скрипти Rebuy чисті на магазинах його клієнтів | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20.10) |
| <button type="button" class="app-open" data-app="shopify-product-network">Shopify Product Network (застосунок самого Shopify)</button> | <span class="badge badge-off">знято без звіту</span> | 15.10.2026 | Знято з App Store | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10) |
| Інші зняті застосунки | <span class="badge badge-off">знято без звіту</span> | 14-21.10.2026 | HeyApps на 21.10 показує 429 знятих і 14 повернених застосунків, усі зняті між 14 і 21.10. Причини не названо | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10) |
{: #apps-table}

## Відомі фішингові домени (не відкривайте їх)

| Домен | Джерело |
|---|---|
| biliing[.]top, checkout-confirm[.]top, order-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/) |
| account-confirm[.]top, billing-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) |
| checkout-guard[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) |
| checkout-secure[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (одне джерело) |
| cartassure[.]top | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/) (одне джерело, не перевірено) |

## Що зробив Shopify

- 15.10.2026: перевірка безпеки `shopify app security check` для розробників застосунків. [Shopify changelog](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check)
- 20.10.2026: "Securing your app, together", Action required для всіх розробників застосунків. Інциденту і застосунків не називає. [Shopify changelog](https://shopify.dev/changelog/blog/securing-your-app-together)
- Окремого звернення до мерчантів станом на 21.10.2026 ми не знайшли.
