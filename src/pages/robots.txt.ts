import type { APIRoute } from "astro";
import { NOINDEX } from "../lib/site";

// While testing on obuk9.com (NOINDEX=true) search engines are told to stay out.
export const GET: APIRoute = () =>
  new Response(
    NOINDEX
      ? "User-agent: *\nDisallow: /\n"
      : "User-agent: *\nDisallow: /admin/\nDisallow: /thank-you/\n\nSitemap: https://obedienceunleashed.com/sitemap-index.xml\n",
    { headers: { "Content-Type": "text/plain" } },
  );
