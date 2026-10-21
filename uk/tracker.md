---
layout: default
title: "Трекер"
lede: "Публічні повідомлення про перехоплення checkout у жовтні 2026 та окремі попередні інциденти: статус, дата і джерело в кожному рядку, а також документовані оновлення платформи."
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

Документоване оновлення платформи Shopify не є статусом інциденту застосунку.

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
| <button type="button" class="app-open" data-app="swym-wishlist-plus">Swym Wishlist Plus</button> | <span class="badge badge-ok">підтверджено вендором</span> | 14.10.2026, ~10:06-11:56 UTC | Несанкціонована зміна конфігурації; виправлення завершено до 16:32 UTC. 20.10 вендор поставив застосунок на паузу для всіх мерчантів. 21.10 о 14:30 UTC: триває моніторинг і відновлення доступу мерчантів групами | [Swym Security Update](https://www.getswym.com/resources/security-response) (16.10); [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (20.10); [статус Swym](https://status.getswym.com/) (21.10) |
| <button type="button" class="app-open" data-app="qikify">Qikify</button> | <span class="badge badge-ok">підтверджено вендором</span> | 22.07.2026 | Окремий липневий інцидент, за словами вендора вирішений того ж дня; застосунки повернуто 21.08. Вендор каже, що це не частина жовтневої хвилі | [Qikify](https://qikify.com/pages/security-incident-notice); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (список; коментар Lauren-Qikify, 16.10) |
| <button type="button" class="app-open" data-app="hextom">Hextom</button> | <span class="badge badge-warn">не підтверджено</span> | серпень 2026 | Zipp і Taylor Page пишуть про схожий інцидент, вирішений у серпні. Заяви вендора ми не відкривали | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19.10); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20.10) |
| <button type="button" class="app-open" data-app="orichi">Orichi (OC Quantity Breaks &amp; Limit)</button> | <span class="badge badge-ok">підтверджено вендором</span> | 11.09.2026 | Окремий вересневий інцидент: шкідливий код перенаправляв покупців на shopfily[.]shop; його видалено того ж дня. Повернуто в App Store 08.10. Зв'язок із жовтневою хвилею не перевірено | [Orichi incident notice](https://orichi.crisp.help/en/article/malicious-code-served-to-storefronts-through-oc-quantity-breaks-limit-ep2drz/) (звіт від 08.10; при перевірці 21.10 URL віддає 404) |
| <button type="button" class="app-open" data-app="boost">Boost AI Search & Filter</button> | <span class="badge badge-warn">не підтверджено</span> | 17.10.2026 | Мерчанти пишуть про редирект. Вендор на статус-сторінці повідомив про інцидент 17-18.10 і вимкнення theme extension, без згадки про безпеку. 19.10 о 15:53 UTC повідомив про відновлення роботи вітрин з 18.10, 18:48 UTC | [Shopify Community 698208](https://community.shopify.com/t/urgent-checkout-phishing-redirect-anyone-else-affected/698208) (#16, 17.10); [статус Boost](https://status.boostcommerce.net) (19.10) |
| <button type="button" class="app-open" data-app="privy">Privy</button> | <span class="badge badge-warn">не підтверджено</span> | 17.10.2026 | Один мерчант пише про редирект. Статус-сторінка Privy: поп-апи та вбудовані форми відновлено 19.10 о 20:28 UTC (16:28 EDT), без висновку про безпеку | Коментар у [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (17.10); [статус Privy](https://status.privy.com) (19.10) |
| <button type="button" class="app-open" data-app="consentmo">Consentmo GDPR Compliance</button> | <span class="badge badge-warn">не підтверджено</span> | 19-20.10.2026 | Zipp посилається на конфіденційне джерело, один коментар мерчанта | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (19-20.10) |
| <button type="button" class="app-open" data-app="17track">17TRACK Order Tracking</button> | <span class="badge badge-warn">не підтверджено</span> | 20.10.2026 | Мерчант пише про код у назвах пунктів меню і на кнопці checkout, домен cartassure[.]top; мерчант пише, що Shopify назвав 17TRACK (публічно не підтверджено). Zipp позначає його як "unconfirmed but de-listed"; Urban Alcove у коментарях до Zipp (21.10) пише, що 17TRACK "maybe compromised", і називає той самий домен. Чи йдеться про різні магазини, не перевірено. HeyApps показує зняття 20.10. Публічної заяви вендора чи Shopify немає | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/); [оновлення мерчанта](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/comment/phy8mey/) (20-21.10); [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (21.10); [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10) |
| <button type="button" class="app-open" data-app="color-swatch-king">Color Swatch King (StarApps)</button> | <span class="badge badge-warn">не підтверджено</span> | Повідомлення 18.10.2026, 23:24 UTC | Мерчант називає застосунок "swathe king" і пише, що код редиректу був у ньому. Ідентичність застосунку та причетність до інциденту не підтверджені | [Коментар мерчанта](https://www.reddit.com/r/shopify/comments/1x8m5d8/comment/phlefr5/) (18.10) |
| <button type="button" class="app-open" data-app="hulk-advanced-wishlist">Hulk Advanced Wishlist</button> | <span class="badge badge-warn">не підтверджено</span> | за кілька тижнів до 10.10.2026 (за словами мерчанта) | Один мерчант пише про редирект магазину на спам-сайт | [r/shopify](https://www.reddit.com/r/shopify/comments/1x2f4kx/comment/pf4d079/) (10.10) |
| <button type="button" class="app-open" data-app="unknown-checkout-guard">Невідомий застосунок, три магазини одного власника</button> | <span class="badge badge-warn">не підтверджено</span> | 19.10.2026 | Редирект на checkout-guard[.]top, джерело не знайдено | [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) (19.10) |
| <button type="button" class="app-open" data-app="rebuy">Rebuy Personalization Engine</button> | <span class="badge badge-off">знято без звіту</span> | 18.10.2026 | Знято з App Store. Taylor Page пише, що скрипти Rebuy чисті на магазинах його клієнтів | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10); [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) (20.10) |
| <button type="button" class="app-open" data-app="shopify-product-network">Shopify Product Network (застосунок самого Shopify)</button> | <span class="badge badge-off">знято без звіту</span> | 15.10.2026 | Знято з App Store | [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) (21.10) |
{: #apps-table}

Окремий [каталог HeyApps]({{ '/uk/apps/' | relative_url }}) містить {{ site.data.heyapps.counts.delisted }} знятих і {{ site.data.heyapps.counts.recovered }} повернених застосунків у знімку від {{ site.data.heyapps.captured_local }}. Доступність сама по собі не є доказом зламу чи безпеки.

Усі застосунки у цьому знімку зняті між 14 і 21.10.2026. [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews) не наводить причин окремих зняттів.

## Спостереження за платформою

| Зміна платформи | Статус джерела | Перевірено | Що відомо | Джерело |
|---|---|---|---|---|
| Вітрини: підтвердження виходу | описано в довідці Shopify; деталі розгортання не перевірено | 21.10.2026 (перевірено; дата запуску невідома) | При кліку на інший сайт може відкриватися вікно «Are you sure you want to leave [назва магазину]?». Довідка Shopify описує захист від коду, що веде на підроблений checkout або фішинговий сайт. Зараз мерчанти не можуть вимкнути вікно чи вибрати сайти-винятки. Мерчанти повідомляють про перемикачі між магазинами, headless-редиректи й партнерські посилання. Дата початку, охоплення всіх магазинів і зв'язок з інцидентом підміни checkout: не перевірено | [Довідка Shopify](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation); [Спільнота розробників 38776](https://community.shopify.dev/t/shopify-exit-interstitial-popup-modal/38776); [r/shopify](https://www.reddit.com/r/shopify/comments/1xbncwn/) |

## Відомі фішингові домени (не відкривайте їх)

| Домен | Джерело |
|---|---|
| biliing[.]top, checkout-confirm[.]top, order-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/) |
| account-confirm[.]top, billing-confirm[.]top | [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) |
| checkout-guard[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903) |
| checkout-secure[.]top | [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq) (одне джерело) |
| cartassure[.]top | [r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/) (20.10); коментарі Urban Alcove у [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack) (21.10). Не перевірено: дві публічні згадки; чи це різні магазини, не встановлено |

## Що зробив Shopify

- 15.10.2026: перевірка безпеки `shopify app security check` для розробників застосунків. [Shopify changelog](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check)
- 20.10.2026: "Securing your app, together", Action required для всіх розробників застосунків. Інциденту і застосунків не називає. [Shopify changelog](https://shopify.dev/changelog/blog/securing-your-app-together)
- Перевірено 21.10.2026: Shopify описує [підтвердження виходу з магазину](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation). Дати публікації немає. Початок розгортання, охоплення всіх магазинів і зв’язок з інцидентом не перевірено.
- Окремого звернення до мерчантів про інцидент підміни checkout станом на 21.10.2026 ми не знайшли.
