---
layout: default
title: "Самоперевірка"
lede: "Перевірка власного магазину Shopify за 15-20 хвилин. Лише безпечні дії власника. Прогрес зберігається в цьому браузері."
lang: uk
slug: checklist
permalink: /uk/checklist/
alt: /checklist/
---

Перед початком: не відкривайте фішингові домени зі списку, не вводьте реальні дані картки на тестах, нічого не видаляйте поспіхом. Перевіряйте лише магазини, якими володієте або маєте письмовий дозвіл.

## 1. Тест checkout як новий покупець (5 хв)

- [ ] Відкрийте **нове приватне вікно** (інкогніто).
- [ ] Відкрийте свій магазин, додайте товар у кошик, натисніть Checkout.
- [ ] Подивіться на адресний рядок. Має бути ваш домен або домен Shopify (shopify.com, myshopify.com, shop.app). Нічого не вводьте на сторінці.
- [ ] Закрийте вікно і повторіть ще **2 рази**, щоразу в новому приватному вікні. Скрипт спрацьовує один раз на відвідувача. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Перевірте різні шляхи: сторінка кошика, бічний кошик (cart drawer), кнопки швидкої покупки, телефон і комп'ютер. ([Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG), [Flagship](https://flagship.inc/en/columns/shopify-checkout-redirect-third-party-app-security))

Обмеження: чистий тест не гарантує, що минулі покупці не постраждали, і не виключає атаку, яка вмикається за країною, пристроєм чи часом. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))

Дві примітки до цього тесту:

- Shopify оголосив підтвердження «Are you sure you want to leave …?» 20.10.2026. Саме вікно не доводить злам і не означає, що інший сайт небезпечний. Якщо названо незнайомий сайт або вікно з’являється на «Додати в кошик» чи Checkout, поверніться, перевірте свіжі застосунки й код теми та напишіть у Shopify Support. За перевіркою 22.10 його не можна вимкнути чи вибрати сайти-винятки. Охоплення всіх магазинів і зв’язок з інцидентом не перевірені. [Shopify changelog](https://changelog.shopify.com/posts/new-protection-against-unexpected-redirects), [довідка Shopify](https://help.shopify.com/en/manual/online-store/menus-and-links/leave-store-confirmation).
- Перевіряйте у справжньому браузері. Завантаження HTML не виконує JavaScript вітрини і не перевіряє клік на Checkout. Чистий HTML не замінює перевірку роботи checkout.

## 2. Застосунки (5 хв)

- [ ] **Settings > Apps and sales channels**: випишіть усі встановлені застосунки. Порівняйте з [трекером]({{ '/uk/tracker/' | relative_url }}).
- [ ] Чи є серед них застосунки, якими ви не користуєтесь? Позначте їх на вимкнення (не видаляйте, поки не перевірите, чи не втратите дані).
- [ ] Відкрийте налаштування кожного застосунку і знайдіть поля **"custom JS"**, **"custom code"**, **"custom HTML"**, **"advanced"**. Ви маєте знати, хто і навіщо додав кожен рядок. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/), [Taylor Page](https://www.linkedin.com/posts/tr-page_ive-been-slow-to-say-much-about-the-shopify-activity-7518335672353726464-7KxG))
- [ ] Змініть паролі і ввімкніть 2FA у кабінетах вендорів застосунків, якщо такі кабінети є. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack))
- [ ] Перевірте, які AI-інструменти і кастомні застосунки мають доступ до адмінки і токенів API. Заберіть зайве. ([зведення заяв, порада Qikify](https://romanzipp.com/blog/statements-from-companies-involved-in-shopify-checkout-hijack))

## 3. Тема і theme app extensions (5 хв)

- [ ] **Online Store > Themes > Customize > App embeds**: випишіть усе, що ввімкнено. Незнайоме або непотрібне тимчасово вимкніть і збережіть.
- [ ] Там само перегляньте блоки **Custom Liquid** у секціях.
- [ ] **Online Store > Themes > ... > Edit code**: у пошуку по файлах шукайте `__ctf_`, `checkout-guard`, `.top/check-out`, назви доменів з [трекера]({{ '/uk/tracker/' | relative_url }}) і `onerror=`. ([Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq), [Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Подивіться, чи є правки файлів теми, зроблені застосунком, які ви не впізнаєте. Shopify зберігає старі версії кожного файлу, тож їх можна повернути разом з розробником. ([Swym FAQ](https://www.getswym.com/resources/wishlist-plus-incident-faq))
- [ ] Пам'ятайте: код, який застосунок отримує зі свого сервера під час відкриття сторінки, у файлах теми **не видно**. Тому пункти 1 і 2 важливіші за пошук у коді. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] **Online Store > Navigation**: перегляньте назви пунктів меню на предмет HTML чи коду. Один мерчант повідомив про код у назвах пунктів меню (не перевірено). ([r/shopifyDev](https://www.reddit.com/r/shopifyDev/comments/1xau8w6/))

## 4. Custom pixels і пікселі застосунків (2 хв)

- [ ] **Settings > Customer events**: перегляньте custom pixels і пікселі застосунків. Ви маєте знати, хто додав кожен піксель і куди він шле дані.
- [ ] Кастомні пікселі працюють у Lax sandbox. Перевірте їхній код, налаштування згоди й обмеження sandbox. ([Довідка Shopify](https://help.shopify.com/en/manual/promoting-marketing/pixels/custom-pixels), [обмеження sandbox](https://help.shopify.com/en/manual/promoting-marketing/pixels/overview#limitations-of-the-pixels-sandbox))

## 5. Checkout і доступи (3 хв)

- [ ] **Settings > Checkout**: перевірте, що налаштування і розширення checkout ті, які ви очікуєте.
- [ ] **Settings > Users** (staff і collaborator accounts): приберіть зайвих людей, увімкніть 2FA для всіх, видайте мінімальні права. ([Very Bad Panda](https://verybadpanda.dev/blog/fake-register-shopify-checkout-hijack/))
- [ ] Змініть свій пароль Shopify. ([Zipp](https://romanzipp.com/blog/shopify-hit-with-phishing-attack))

## 6. Якщо щось знайшли

- [ ] Нічого не вводьте на підозрілій сторінці.
- [ ] Збережіть докази: скриншоти, повну адресу, дату і час, список увімкнених застосунків і app embeds.
- [ ] Тимчасово вимкніть підозрілий app embed або закрийте вітрину паролем (Online Store > Preferences).
- [ ] Напишіть у Shopify Support і вендору застосунку. Попросіть письмово вікно інциденту, код і домени.
- [ ] Зверніться до платіжного провайдера і юриста щодо обов'язків повідомити покупців чи наглядовий орган.

Статуси застосунків: [трекер]({{ '/uk/tracker/' | relative_url }}). Пояснення: [FAQ]({{ '/uk/faq/' | relative_url }}).
