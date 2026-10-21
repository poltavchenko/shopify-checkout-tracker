# Checkout Hijack Tracker

Independent, sourced summary of the October 2026 checkout hijack via third-party Shopify apps, in English and Ukrainian. Not on behalf of Shopify and not affiliated with Shopify Inc. or any app vendor. Not legal advice.

## Structure

- `index.md`, `tracker.md`, `faq.md`, `checklist.md`: English pages (default).
- `uk/`: Ukrainian pages with the same structure.
- `_layouts/default.html`: the only layout (sticky header, EN/UA switch, light/dark toggle, hero, footer).
- `_data/i18n.yml`: interface strings in both languages.
- `assets/css/style.css`, `assets/js/site.js`: all styles and scripts, self-hosted. No external fonts, CDNs, analytics or trackers.
- `_config.yml`: site settings, update dates, `baseurl` and the Issues link.

GitHub Pages builds the site directly from this repository (Jekyll, kramdown GFM). No theme or plugins are used.

## Features

- Light and dark theme: follows the system setting, the toggle saves the choice in `localStorage`.
- Tracker statuses are badges with text, not color only.
- Checklist checkboxes save progress in `localStorage`, in the visitor's browser only.
- FAQ questions use native `<details>`.

## Local preview (optional)

```
gem install jekyll -v 3.10.0 kramdown-parser-gfm webrick
jekyll serve --baseurl ""
```

## Rules for edits

- Every fact needs a public source and a date.
- App statuses use exactly three values: confirmed by vendor / unconfirmed / removed without report (UA: підтверджено вендором / не підтверджено / знято без звіту). Use the badge markup: `<span class="badge badge-ok">`, `badge-warn`, `badge-off`.
- Do not name a vendor as compromised without a vendor statement.
- Update `updated_en` and `updated_uk` in `_config.yml` when content changes.
- No analytics, cookies or third-party trackers.

## Report an error

Open an issue: https://github.com/poltavchenko/shopify-checkout-tracker/issues
Please do not post store names, customer data or passwords in issues.

## App details and search (tracker)

- `_data/apps.json` holds the data for the app details dialog: developer, support email, short description (EN and UA) and a timeline. Every field stores `source` (URL) and `checked` (date). `verified: false` shows an "unverified" tag; an empty value shows "no data".
- Support emails: only an address the vendor published as a support contact. Never guess or build an address, never use a personal email.
- In the tracker table, the app name is a button: `<button type="button" class="app-open" data-app="ID">Name</button>`, where ID is a key in `apps.json`. `?app=ID` opens the dialog directly.
- The search box filters the first table (`{: #apps-table}`) by app name and developer, ignoring case and diacritics. Press `/` to focus, `Esc` to clear. The query is kept in `?q=`.
