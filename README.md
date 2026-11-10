# Obedience Unleashed website

The new obedienceunleashed.com, built with [Astro](https://astro.build) in the "Sunshine" design.
It is tested on **obuk9.com** (hidden from search engines) before replacing the WordPress site.

## Editing content (Marie / office)

Go to **/admin** on the site (e.g. https://obuk9.com/admin) and sign in with GitHub.

| Section in the editor | What it changes |
|---|---|
| Class dates | Kamloops class starts. Chilliwack, Maple Ridge / Mission and Cochrane show the classes the office adds in the Obedience Unleashed portal instead (see below); their dates here are only used if the portal can't be reached. Past dates show "TBA". |
| Group walks | Walk dates and places. |
| Locations & prices | Prices, hours, booking links and Google review link (QR code). |
| Staff | One entry per person: name, role, which locations they work at (tick boxes), photo upload and bio. Move or remove people here. |
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

## Class dates from the portal

Chilliwack, Maple Ridge / Mission (Silverdale; Stave Falls classes run there) and Cochrane take their upcoming class starts from the Obedience Unleashed portal's public class list (`https://obedienceunleashedportal.com/api/public/classes`, read-only, no client details). The tables are filled when the site is built and refreshed in the visitor's browser, so a class added in the portal shows without a rebuild. A location with no upcoming start shows the class under way there ("In progress · last class …", with Get notified), and the new class as soon as it's published in the portal; with neither, one "TBA" row. A class entered twice in the portal shows once. Prices and Book links still come from Locations & prices. Rules: `src/lib/live-classes.ts`; browser refresh: `src/scripts/live-classes.ts`. The portal allows obuk9.com and www.obuk9.com to read the list from a browser; other addresses (deploy previews, obedienceunleashed.com at cut-over) show the classes as of the last build until they are added on the portal's side.

## Hosting (Netlify)

- Build: `npm run build`, publish `dist` (see `netlify.toml`).
- `NOINDEX=true` keeps search engines out while testing. Set it to `false` at cut-over to obedienceunleashed.com.
- Contact forms use Netlify Forms (form name `contact`). Email notifications go to office.obedienceunleashed@gmail.com and andy@obedienceunleashed.com (set in Netlify > Forms > Notifications).

## Local development

```
npm install
npm run dev
```
