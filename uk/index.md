---
layout: default
title: "Перехоплення checkout у Shopify: що відомо"
lede: "Приблизно з 10.10.2026 у частині магазинів Shopify покупців після кліку на Checkout перенаправляли на підроблені сторінки оплати. За даними незалежних дослідників, власний checkout Shopify не зламаний: код працював на вітрині через сторонні застосунки."
lang: uk
slug: home
permalink: /uk/
alt: /
---

<div class="cards-grid"><a class="card" href="{{ '/uk/tracker/' | relative_url }}"><h3>Трекер</h3><p>Застосунки, повідомлення про інциденти й оновлення платформи, дата і джерело в кожному рядку.</p></a><a class="card" href="{{ '/uk/faq/' | relative_url }}"><h3>FAQ</h3><p>Що сталося, що зробив Shopify, що робити, якщо щось знайшли.</p></a><a class="card" href="{{ '/uk/checklist/' | relative_url }}"><h3>Самоперевірка</h3><p>Чекліст на 15-20 хвилин для власного магазину. Лише безпечні дії.</p></a></div>

[Каталог HeyApps]({{ '/uk/apps/' | relative_url }}): {{ site.data.heyapps.counts.delisted }} знятих і {{ site.data.heyapps.counts.recovered }} повернених застосунків у датованому знімку. Доступність і докази інциденту є різними даними.

## Статуси

- <span class="badge badge-ok">підтверджено вендором</span> розробник застосунку публічно визнав інцидент.
- <span class="badge badge-warn">не підтверджено</span> повідомляють мерчанти чи дослідники, перевіреної публічної заяви вендора немає.
- <span class="badge badge-off">знято без звіту</span> знято з App Store, ніхто не пов'язує з інцидентом.
{: .legend}

Документоване оновлення платформи Shopify не є статусом інциденту застосунку.

## Першоджерела

[Roman Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG) і вендори, які опублікували заяви. Трекер також позначає непублічні повідомлення мерчантів та межі їхньої перевірки.

## Інші дослідження

9 листопада 2026 року [Guardio Labs](https://site.guard.io/labs/cartjacked---one-in-195-online-shops-we-scanned-was-hijacked) оцінила, що в жовтневій вибірці Common Crawl близько 12 200 із 2,38 млн магазинів на різних платформах містили шкідливий код або вміст. Для магазинів Shopify у цій вибірці автори оцінили 0,75–2,2 на 1000. Оцінки охоплюють різні типи атак, не лише перехоплення checkout; вони не описують усі онлайн-магазини і не встановлюють зв’язку із застосунками цього трекера.
