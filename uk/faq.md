---
layout: default
title: "Питання і відповіді"
lede: "Що відомо, що ні і що робити. Простою мовою, з джерелами."
lang: uk
slug: faq
permalink: /uk/faq/
alt: /faq/
---

## Відомо

<details markdown="1">
<summary>Що сталося?</summary>

Приблизно з 10.10.2026 у частині магазинів Shopify покупця після кліку на Checkout перенаправляли на підроблену сторінку оплати на іншому домені. Там збирали дані картки, а потім повертали покупця на справжній checkout. Джерела: [Roman Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/).

</details>

<details markdown="1">
<summary>Shopify зламали?</summary>

Ні, за даними незалежних дослідників. Власний checkout Shopify не зламаний. Шкідливий код працював на вітрині, до кнопки Checkout, через сторонні застосунки. Джерела: [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG). Окремої заяви Shopify для мерчантів про цей інцидент підміни checkout ми не знайшли.

</details>

<details markdown="1">
<summary>Як код потрапляв у магазин?</summary>

У підтверджених випадках через налаштування застосунку: поле на кшталт "custom JS", яке застосунок отримує зі свого сервера і виконує на сторінці. Код теми при цьому міг лишатися чистим. Джерела: [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [зведення заяв](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).

</details>

<details markdown="1">
<summary>Які застосунки підтвердили інцидент?</summary>

За жовтень 2026: Hulk Product Options, Selleasy і Swym Wishlist Plus. Qikify (липень) та Orichi (вересень) опублікували звіти про окремі попередні інциденти. Повний список зі статусами дивіться в [трекері]({{ '/uk/tracker/' | relative_url }}).

</details>

<details markdown="1">
<summary>Чому я тестую і нічого не бачу?</summary>

Скрипт спрацьовує один раз на відвідувача: після першого перенаправлення він ставить позначку в браузері і більше не чіпає цю вкладку. Тому тест у тій самій вкладці нічого не покаже. Тестуйте щоразу в новому приватному вікні. Джерела: [Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/).

</details>

<details markdown="1">
<summary>Замовлення виглядають нормально. Значить, усе добре?</summary>

Не обов'язково. Після підробленої сторінки покупця повертали на справжній checkout, тож замовлення в адмінці могли виглядати звично. Джерело: [Shopify Community 700903](https://community.shopify.com/t/customers-redirected-to-cloned-checkout-that-captures-card-details-anyone-else-affected/700903).

</details>

<details markdown="1">
<summary>Застосунок, який я використовую, зняли з App Store. Мене зламали?</summary>

Саме по собі зняття нічого не доводить. [HeyApps показує {{ site.data.heyapps.counts.delisted }} знятих застосунків у знімку каталогу]({{ '/uk/apps/' | relative_url }}) від {{ site.data.heyapps.captured_local }}, серед них навіть застосунок самого Shopify. Зняття також не видаляє застосунок з вашого магазину. Пройдіть чекліст і напишіть вендору. Джерела: [HeyApps](https://heyapps.dev/apps/delisted?sort=reviews), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG).

</details>

<details markdown="1">
<summary>Видалити застосунок про всяк випадок?</summary>

Спершу напишіть вендору. FAQ Swym від 20.10 каже, що пауза доступу не видаляє списки бажань. 27.10 о 14:41 UTC Swym повідомив про відкритий доступ для всіх магазинів мерчантів і аудит третьою стороною. Boost просить не видаляти і не перевстановлювати застосунок. На час перевірки тимчасово вимкніть підозрілий app embed у редакторі теми. Джерела: [Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [статус Swym](https://status.getswym.com/), [статус Boost](https://status.boostcommerce.net).

</details>

<details markdown="1">
<summary>Що зробив Shopify?</summary>

15.10 випустив перевірку безпеки для розробників застосунків, 20.10 опублікував для них "Securing your app, together" з позначкою Action required. Там також сказано, що Shopify звузить межі коду застосунків на вітрині і підніме вимоги App Store. Джерела: [15.10](https://shopify.dev/changelog/blog/build-more-secure-apps-with-shopify-s-ai-toolkit-security-check), [20.10](https://shopify.dev/changelog/blog/securing-your-app-together).

</details>
<details markdown="1">
<summary>Магазин питає «Are you sure you want to leave?» при кліку на зовнішнє посилання. Мене зламали?</summary>

Саме по собі ні. За оновленням Shopify від 23.10, посилання на визначені ним шкідливі сайти блокуються, підозрілі сайти можуть викликати підтвердження, інші відкриваються прямо. Саме вікно не доводить злам або безпеку сайту призначення. Винятки включають домени магазину та їхні піддомени в адмінці, checkout, сторінки Shopify і популярні соцмережі.

Перевірте випадки, коли вікно називає незнайомий сайт або з’являється на кнопці, яка має лишати покупця в магазині, наприклад «Додати в кошик» чи Checkout. Перегляньте нещодавно встановлені або оновлені застосунки та код теми. Напишіть у Shopify Support, додайте сторінку, названий сайт і скриншот. Shopify каже, що захист увімкнено для всіх онлайн-магазинів; незалежно охоплення і зв’язок з інцидентом не перевірені. Джерела: [Shopify changelog](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects), [довідка Shopify](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation).

</details>

## Невідомо

- Як саме код потрапив у кожен застосунок і чи це одна кампанія.
- Повний список застосунків і скільки магазинів постраждало.
- Чому зняли більшість застосунків з App Store.
- Звідки перенаправлення в частині магазинів, де жоден відомий застосунок не встановлений.

## Якщо щось знайшли

1. Не вводьте дані на підозрілій сторінці і не відкривайте фішингові домени.
2. Збережіть докази: скриншоти, повну адресу сторінки, дату і час, які застосунки і app embeds увімкнені.
3. Тимчасово вимкніть підозрілі app embeds або закрийте вітрину паролем.
4. Напишіть у Shopify Support і вендору застосунку. Попросіть письмово вікно інциденту, код, який виконувався, і домени.
5. Зверніться до платіжного провайдера. Якщо дані покупців могли потрапити до третіх осіб, разом з юристом оцініть обов'язки щодо повідомлення (у ЄС це ст. [33](https://eur-lex.europa.eu/eli/reg/2016/679/) і [34](https://eur-lex.europa.eu/eli/reg/2016/679/) GDPR).

## Покупцям

Якщо ви вводили дані картки на сторінці оплати з незнайомою адресою, зверніться до свого банку. Swym пише, що оплати через Shop Pay, PayPal, Google Pay та подібні гаманці в їхньому інциденті не постраждали так само, як ручне введення картки. Джерело: [зведення заяв](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack).
