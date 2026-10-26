import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

// The canonical domain stays obedienceunleashed.com even while testing on obuk9.com,
// so nothing changes for SEO at cut-over. Testing builds are kept out of Google with NOINDEX (see netlify.toml).
export default defineConfig({
  site: "https://obedienceunleashed.com",
  trailingSlash: "always",
  build: { format: "directory" },
  integrations: [
    sitemap({
      filter: (page) => !/\/(thank-you|404)\/?$/.test(page),
    }),
  ],
});
