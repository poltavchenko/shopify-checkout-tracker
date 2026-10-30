# Checkout Hijack Tracker

Independent, sourced summary of the October 2026 checkout hijack via third-party Shopify apps, in English and Ukrainian. Not on behalf of Shopify and not affiliated with Shopify Inc. or any app vendor. Not legal advice.

## Structure

- `index.md`, `tracker.md`, `apps.md`, `faq.md`, `checklist.md`: English pages (default).
- `uk/`: Ukrainian pages with the same structure.
- `_layouts/default.html`: the only layout (sticky header, EN/UA switch, light/dark toggle, hero, footer).
- `_data/i18n.yml`: interface strings in both languages.
- `_data/heyapps.json`, `_includes/apps-catalog.html`: a dated HeyApps availability snapshot and the shared catalog table. Availability is separate from incident evidence in `_data/apps.json`.
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

## HeyApps catalog and offline refresh

`/apps/` and `/uk/apps/` contain one record per HeyApps slug, including both delisted and listed-again apps. Delisting does not establish a compromise. A return does not establish safety. The incident tracker remains a separate curated list of apps and episodes.

The snapshot records capture times, source URLs, each capture's counts and SHA-256 hashes. The 30 October 2026 snapshot contains 577 delisted and 157 listed-again apps. Four delisted sorts exposed up to 400 entries each; four additional apps were verified on their individual HeyApps pages. The importer rejects a partial union or conflicting records. The list does not update in the browser.

Save public DOM captures as JSON objects with `source`, `captured_at` (ISO timestamp with time zone), `reported_count`, `view` (`delisted` or `recovered`) and a nonempty `apps` array. Each app needs `slug`, `name`, `developer` (string or null), `source_url` and `delisted`; `recovered` is required for the recovered view, and `launched` is optional. Dates accept `YYYY-MM-DD` or English dates such as `Oct 20, 2026`. Capture both availability states. Add sorts until each state's unique count equals its reported count.

When the visible sorts omit an app, its individual HeyApps page can supply a separate `kind: "detail"` capture. It must show `observed_status: "Delisted"`, matching dated listing history, one app, and its exact `source_url`. The listing captures still supply the total reported count; an unshown launch date stays null.

Run the offline importer with Python 3.9 or later:

```sh
python3 scripts/import-heyapps.py --output _data/heyapps.json \
  /path/to/delisted-reviews.json /path/to/delisted-date.json \
  /path/to/delisted-launched.json /path/to/recovered.json
```

The importer uses only the Python standard library and makes no network calls. Validation finishes before the output is replaced. Unknown fields are dropped. Only the explicit slug crosswalk in the importer can connect a catalog record to curated incident evidence; there is no vendor or name matching. New incident links require an explicit reviewed crosswalk change, not an availability change. Update the site timestamps after a refresh.

Run the checks with:

```sh
python3 -m unittest discover -s test -p 'test_*.py'
node test/site-url.test.cjs
```

The rendering tests run real Jekyll builds with hostile text fixtures when `jekyll` is on `PATH`. Otherwise, set `JEKYLL_COMMAND` to an existing Jekyll executable or command, with its normal Ruby environment. Without a runtime, the rendering check is reported as skipped. `test/` and `scripts/` are excluded from the published site.
