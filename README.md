# Obedience Unleashed website

The new obedienceunleashed.com, built with [Astro](https://astro.build) in the "Sunshine" design.
It is tested on **obuk9.com** (hidden from search engines) before replacing the WordPress site.

## Editing content (Marie / office)

Go to **/admin** on the site (e.g. https://obuk9.com/admin) and sign in with GitHub.

| Section in the editor | What it changes |
|---|---|
| Class dates | Upcoming class starts on every class, location and home page. Past dates show "TBA". |
| Group walks | Walk dates and places. |
| Locations, prices & teams | Prices, hours, booking links, Google review link (QR code) and team members with photos and bios. |
| Business settings | Phone, hours, policies, leadership bios, holiday premium. |
| Reviews | Client reviews (real ones only, word for word). |
| Training programs | What each class covers. |
| Blog posts | Add or edit articles. |
| Page text & SEO | Search titles/descriptions and extra text per page. |

Every save rebuilds the site in about a minute.

## Where things live

- `src/data/` – business data (JSON) edited through /admin
- `src/content/pages/` – one Markdown file per page URL (SEO + migrated text)
- `src/content/blog/` – blog posts
- `src/templates/` – page layouts; `src/components/` – shared pieces; `src/styles/global.css` – the design
- `public/_redirects` – old WordPress URLs (courses, ?p= links, categories) redirected
- `scripts/` – one-time migration from WordPress (already run)

## Hosting (Netlify)

- Build: `npm run build`, publish `dist` (see `netlify.toml`).
- `NOINDEX=true` keeps search engines out while testing. Set it to `false` at cut-over to obedienceunleashed.com.
- Contact forms use Netlify Forms (form name `contact`). Email notifications go to office.obedienceunleashed@gmail.com and andy@obedienceunleashed.com (set in Netlify > Forms > Notifications).

## Local development

```
npm install
npm run dev
```
