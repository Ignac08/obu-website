// Picks the template for a page entry and builds its structured data.
import Home from "../templates/Home.astro";
import Training from "../templates/Training.astro";
import Service from "../templates/Service.astro";
import Care from "../templates/Care.astro";
import BoardTrain from "../templates/BoardTrain.astro";
import Walks from "../templates/Walks.astro";
import Rates from "../templates/Rates.astro";
import ServiceDogs from "../templates/ServiceDogs.astro";
import Locations from "../templates/Locations.astro";
import Location from "../templates/Location.astro";
import Team from "../templates/Team.astro";
import About from "../templates/About.astro";
import Prose from "../templates/Prose.astro";
import Testimonials from "../templates/Testimonials.astro";
import Contact from "../templates/Contact.astro";
import Blog from "../templates/Blog.astro";
import Thanks from "../templates/Thanks.astro";
import NotFound from "../templates/NotFound.astro";
import { LOC, LOCATIONS, SITE, SVC, addressLine, classPrice, type Location as Loc } from "./site";

export const TEMPLATES: Record<string, any> = {
  home: Home, training: Training, service: Service, "service-location": Service, care: Care, "care-location": Care,
  boardtrain: BoardTrain, walks: Walks, rates: Rates, servicedogs: ServiceDogs, locations: Locations, location: Location,
  team: Team, about: About, prose: Prose, testimonials: Testimonials, contact: Contact, blog: Blog, thanks: Thanks, notfound: NotFound,
};

const SECTION: Record<string, string> = {
  training: "training", service: "training", "service-location": "training", walks: "training", boardtrain: "boardandtrain",
  rates: "rates", servicedogs: "servicedogs", locations: "locations", location: "locations", team: "locations",
  about: "about", prose: "about", testimonials: "about", blog: "blog",
};
export const sectionFor = (d: any) => (d.template === "care" || d.template === "care-location" ? (d.service === "daycare" ? "daycare" : "boarding") : SECTION[d.template] ?? "");

const BASE = "https://obedienceunleashed.com";
export const business = (l: Loc) => ({
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": `${BASE}/locations/${l.slug}/#business`,
  name: `Obedience Unleashed ${l.name}`,
  parentOrganization: { "@id": `${BASE}/#org` },
  url: `${BASE}/locations/${l.slug}/`,
  image: `${BASE}/img/loc-${l.key}.jpg`,
  telephone: SITE.phone,
  priceRange: "$$",
  address: { "@type": "PostalAddress", streetAddress: l.street, addressLocality: l.city, addressRegion: l.region, postalCode: l.postal || undefined, addressCountry: l.country },
  areaServed: l.area.split(" / ").map((n) => ({ "@type": "City", name: n })),
  description: l.blurb,
});

const crumbs = (items: [string, string][]) => ({
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: [["Home", "/"], ...items].map(([name, path], i) => ({ "@type": "ListItem", position: i + 1, name, item: BASE + path })),
});

export function schemaFor(entry: any): any[] {
  const d = entry.data;
  const path = entry.id === "index" ? "/" : `/${entry.id}/`;
  const out: any[] = [];
  if (d.template === "home" || d.template === "locations") out.push(...LOCATIONS.map(business));
  if (d.location && (d.template === "location" || d.template.endsWith("-location"))) out.push(business(LOC[d.location]));
  if (d.template === "service" || d.template === "service-location") {
    const S = SVC[d.service];
    const locs = d.location ? [LOC[d.location]] : LOCATIONS.filter((l) => classPrice(S.key, l.key) && l.key !== "stavefalls");
    out.push({
      "@context": "https://schema.org", "@type": "Service", name: d.h1.replace(/\.$/, "") || S.name, serviceType: S.name,
      provider: { "@id": `${BASE}/#org` }, description: d.description, url: BASE + path,
      areaServed: d.town ? { "@type": "City", name: d.town } : undefined,
      offers: locs.map((l) => ({ "@type": "Offer", price: classPrice(S.key, l.key), priceCurrency: "CAD", availableAtOrFrom: { "@id": `${BASE}/locations/${l.slug}/#business` } })),
    });
  }
  if (d.template !== "home") out.push(crumbs([[d.h1 || d.title, path]]));
  return out;
}
