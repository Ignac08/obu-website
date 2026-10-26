// Shared data and helpers. All business data lives in src/data (edited through /admin).
import settings from "../data/settings.json";
import scheduleData from "../data/schedule.json";
import walksData from "../data/walks.json";
import servicesData from "../data/services.json";
import reviewsData from "../data/reviews.json";
import validatorsData from "../data/validators.json";

export type Prices = { one: number; two: number; three: number };
export type Member = { name: string; role: string; photo?: string; bio?: string };
export type Location = {
  key: string; order: number; name: string; slug: string; area: string; areaNote: string; color: string;
  street: string; city: string; region: string; postal: string; country: string;
  blurb: string; dropOff: string; pickUp: string; bookingUrl: string; reviewUrl: string;
  daycare: Prices; daycareHours: number; boarding: Prices; boardTrain: number;
  classes: Record<"puppy" | "l1" | "l2" | "ol", number>; consult: boolean; classNote: string;
  offers: string[]; bus: boolean; walks: string; team: Member[]; leadership?: string[];
  teamPage: string; daycarePage: string; boardingPage: string;
};

const locFiles = import.meta.glob<Location>("../data/locations/*.json", { eager: true, import: "default" });
export const LOCATIONS: Location[] = Object.values(locFiles).sort((a, b) => a.order - b.order);
export const LOC: Record<string, Location> = Object.fromEntries(LOCATIONS.map((l) => [l.key, l]));

export const SITE = settings;
export const SERVICES = servicesData.services;
export const SVC = Object.fromEntries(SERVICES.map((s) => [s.key, s]));
export const MARKER = servicesData.markerTraining;
export const REVIEWS = reviewsData.reviews;
export const VALIDATORS = validatorsData.validators;
export const WALKS = walksData;
export const SCHEDULE_NOTE = scheduleData.note;

export const NOINDEX = (import.meta.env.NOINDEX ?? process.env.NOINDEX ?? "true") !== "false";
export const PHONE_HREF = "tel:" + SITE.phone.replace(/[^0-9+]/g, "");

export const money = (n: number) =>
  "$" + (Number.isInteger(n) ? n.toLocaleString("en-CA") : n.toLocaleString("en-CA", { minimumFractionDigits: 2, maximumFractionDigits: 2 }));

export const addressLine = (l: Location) => `${l.street}, ${l.city}, ${l.region}${l.postal ? " " + l.postal : ""}`;
export const mapsUrl = (l: Location) => "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(`Obedience Unleashed ${addressLine(l)}`);
export const locUrl = (l: Location) => `/locations/${l.slug}/`;

// Classes for Stave Falls clients run at Silverdale.
export const classLocation = (key: string) => (key === "stavefalls" ? "silverdale" : key);
export const classPrice = (svc: string, locKey: string): number => {
  const l = LOC[classLocation(locKey)];
  if (!l) return 0;
  if (svc === "consult") return l.consult ? SITE.consultPrice : 0;
  return (l.classes as Record<string, number>)[svc] || 0;
};
export const minClassPrice = (svc: string) => {
  const p = LOCATIONS.map((l) => classPrice(svc, l.key)).filter(Boolean);
  return p.length ? Math.min(...p) : 0;
};

const today = new Date(new Date().toLocaleDateString("en-CA", { timeZone: "America/Vancouver" }));
const parseDate = (d: string) => (d ? new Date(d + "T12:00:00") : null);
export const fmtDate = (d: string, opts: Intl.DateTimeFormatOptions = { weekday: "short", month: "short", day: "numeric" }) => {
  const x = parseDate(d);
  return x ? x.toLocaleDateString("en-CA", { ...opts, timeZone: "UTC" }).replace(/\./g, "") : "";
};

export type ClassRow = { course: string; location: string; start: string; time: string; dates: string; tba: boolean };
// Past start dates show as "TBA" until the office adds the next one.
export const schedule = (filter: (r: ClassRow) => boolean = () => true): ClassRow[] =>
  scheduleData.classes
    .map((c) => {
      const d = parseDate(c.start);
      return { ...c, tba: !d || d < today };
    })
    .filter(filter)
    .sort((a, b) => (a.tba === b.tba ? (a.start || "").localeCompare(b.start || "") : a.tba ? 1 : -1));

export const upcomingWalks = (key: string) => {
  const g = WALKS.groups.find((x) => x.key === key);
  if (!g) return null;
  return { ...g, walks: g.walks.filter((w) => { const d = parseDate(w.date); return d && d >= today; }) };
};

export const reviewsFor = (slug: string, opts: { service?: string; location?: string; limit?: number } = {}) => {
  const lim = opts.limit ?? 6;
  let r = REVIEWS.filter((x) => x.pages.includes(slug));
  if (r.length < 3 && opts.service) r = r.concat(REVIEWS.filter((x) => x.service === opts.service && !r.includes(x)));
  if (r.length < 3 && opts.location) r = r.concat(REVIEWS.filter((x) => x.location === opts.location && !r.includes(x)));
  if (r.length < 3) r = r.concat(REVIEWS.filter((x) => x.featured && !r.includes(x)));
  return r.slice(0, lim);
};

export const initials = (name: string) => name.split(/\s+/).map((s) => s[0]).join("").slice(0, 2).toUpperCase();

export const BLOG_CATS: Record<string, { name: string; color: string; blurb: string; cta: [string, string] }> = {
  puppy: { name: "Puppies", color: "#FFE08A", blurb: "Socialization, potty training and first lessons.", cta: ["Puppy Class", "/puppy-class/"] },
  training: { name: "Training tips", color: "#BFE3FF", blurb: "Fix chewing and digging, teach place, train on the go.", cta: ["Obedience Bootcamp", "/obedience-bootcamp-level-1/"] },
  care: { name: "Daycare & boarding", color: "#C8F0DC", blurb: "Is your dog bored at home? How much daycare is right?", cta: ["Daycare", "/dog-daycare/"] },
  local: { name: "Local guides", color: "#FFD3C2", blurb: "Seasonal and local advice for Mission, Kamloops and Cochrane.", cta: ["Find your location", "/locations/"] },
};

// Location-specific page for a service, if one exists (keeps the old SEO URLs in use).
export const SERVICE_LOCAL_PAGE: Record<string, Record<string, string>> = {
  puppy: { silverdale: "/puppy-class-mission/", stavefalls: "/puppy-class-maple-ridge/", chilliwack: "/puppy-class-chilliwack/", kamloops: "/puppy-class-kamloops/", cochrane: "/puppy-class-cochrane/" },
  l1: { silverdale: "/obedience-bootcamp-level-1-mission/", stavefalls: "/obedience-bootcamp-level-1-maple-ridge/", chilliwack: "/obedience-bootcamp-level-1-chilliwack/", kamloops: "/obedience-bootcamp-level-1-kamloops/", cochrane: "/obedience-bootcamp-level-1-cochrane/" },
  l2: { silverdale: "/obedience-unleashed-bootcamp-level-2-mission/", chilliwack: "/obedience-bootcamp-level-2-chilliwack/" },
  consult: { silverdale: "/behavioural-consultation-maple-ridge-mission/", chilliwack: "/behavioural-consultation-chilliwack/", kamloops: "/behavioural-consultation-kamloops/", cochrane: "/behavioural-consultation-cochrane-ab/" },
};
