// Upcoming class starts from the Obedience Unleashed portal (owner, 2026-11-10: the office adds
// classes in the portal, and they must show here). The portal's public class list (approved by the
// owner on 2026-11-09: name, type, location, start date and time, sessions, price, spots and an
// enroll link; no client details) covers Chilliwack, Maple Ridge / Mission (Silverdale; Stave
// Falls classes run there) and Cochrane. Those locations show the portal's classes; Kamloops isn't
// in the portal and keeps the dates typed in /admin (Class dates). The tables are filled when the
// site is built and again in the visitor's browser, so a class added in the portal shows without a
// rebuild. If the portal can't be reached, every location falls back to the /admin dates.
//
// Each class and location shows once: a location with no upcoming start shows the class under way
// there (owner, 2026-11-10: "the moment a new class is published" it shows instead), else one "TBA"
// row (two past Silverdale dates used to show as two identical TBA rows); a class entered twice in
// the portal (same class, place, day and time) shows once.
//
// No imports from site.ts: this file also runs in the browser, and site.ts pulls in every data file.

export const PORTAL_CLASSES_URL = "https://obedienceunleashedportal.com/api/public/classes";

/** The website's locations whose classes come from the portal. */
export const PORTAL_LOCATIONS: readonly string[] = ["chilliwack", "silverdale", "cochrane"];

/** The portal's class types the website has pages for, as the website's course keys. */
const COURSE_BY_TYPE: Record<string, string> = {
  "Puppy Classes": "puppy",
  "Obedience Bootcamp 1": "l1",
  "Obedience Bootcamp 2": "l2",
  "Off-leash Freedom": "ol",
};

/** The portal's facility names, as the website's location keys. */
const LOCATION_BY_NAME: Record<string, string> = {
  chilliwack: "chilliwack",
  silverdale: "silverdale",
  "stave falls": "silverdale",
  cochrane: "cochrane",
};

export const COURSES: readonly string[] = ["puppy", "l1", "l2", "ol"];

/** One class start as the tables show it; `start` is "YYYY-MM-DD", or "" when not set; `end` is its last class, from the portal. */
export type ClassRow = { course: string; location: string; start: string; time: string; dates: string; end?: string };
/** `running`: a class under way, shown while its location has no new start. */
export type ShownRow = ClassRow & { tba: boolean; running?: boolean };

/** Which rows a table shows. */
export interface SchedScope {
  courses?: string[];
  location?: string;
  datedOnly?: boolean;
  limit?: number;
}

/** What the tables need to know about the site, also handed to the browser. */
export interface SchedSite {
  /** Today in BC, "YYYY-MM-DD"; a start before it shows as TBA. */
  today: string;
  locations: Record<string, { label: string; order: number; bookingUrl: string; prices: Record<string, number> }>;
  courses: Record<string, { name: string; page: string; localPages: Record<string, string> }>;
}

/** Classes for Stave Falls clients run at Silverdale. */
export const classLocation = (key: string) => (key === "stavefalls" ? "silverdale" : key);

/** Today in BC as "YYYY-MM-DD". */
export const bcToday = () => new Date().toLocaleDateString("en-CA", { timeZone: "America/Vancouver" });

/** "5:00 PM" → "5:00pm", as the /admin dates are written. */
const shortTime = (t: unknown) => (typeof t === "string" ? t.trim().replace(/\s*([AP])M$/i, (_, m: string) => `${m.toLowerCase()}m`) : "");

const isDay = (v: unknown): v is string => typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v);

/** The portal's list as table rows, or null when it isn't the expected shape. */
export function portalRows(feed: unknown): ClassRow[] | null {
  const classes = (feed as { classes?: unknown })?.classes;
  if (!Array.isArray(classes)) return null;
  const rows: ClassRow[] = [];
  for (const c of classes as Record<string, unknown>[]) {
    const course = COURSE_BY_TYPE[String(c?.type ?? "")];
    const location = LOCATION_BY_NAME[String(c?.location ?? "").trim().toLowerCase()];
    const start = isDay(c?.startDate) ? c.startDate : "";
    if (!course || !location || !start) continue;
    const sessions = Number(c.sessions);
    const row: ClassRow = { course, location, start, time: shortTime(c.startTime), dates: sessions > 1 ? `${sessions} sessions` : "" };
    if (isDay(c.endDate)) row.end = c.endDate;
    rows.push(row);
  }
  return rows;
}

/** Minutes after midnight for "5:00pm", to order classes on the same day. */
function minutes(time: string): number {
  const m = /^(\d{1,2}):(\d{2})\s*([ap])m$/i.exec(time.trim());
  if (!m) return 24 * 60;
  return ((Number(m[1]) % 12) + (m[3].toLowerCase() === "p" ? 12 : 0)) * 60 + Number(m[2]);
}

/**
 * The rows a table shows. Locations the portal covers take the portal's classes (when it answered,
 * `live` isn't null): the upcoming starts; for a class with none, the class under way there; else one
 * TBA row for a class they offer. Other locations keep the /admin dates. Upcoming starts come first
 * by day and time, then classes under way, then TBA rows by location.
 */
export function scheduleRows(scope: SchedScope, adminRows: readonly ClassRow[], live: readonly ClassRow[] | null, site: SchedSite): ShownRow[] {
  const covered = new Set(live ? PORTAL_LOCATIONS : []);
  const wanted = (r: ClassRow) =>
    (!scope.courses || scope.courses.includes(r.course)) && (!scope.location || classLocation(r.location) === classLocation(scope.location));
  const offered = (course: string, location: string) => (site.locations[location]?.prices[course] ?? 0) > 0;

  const rows: ShownRow[] = [];
  const seen = new Set<string>();
  const add = (r: ClassRow, running = false) => {
    const location = classLocation(r.location);
    const tba = !running && (!r.start || r.start < site.today);
    const key = tba ? `${r.course}|${location}|tba` : `${r.course}|${location}|${r.start}|${r.time}`;
    if (!wanted(r) || seen.has(key)) return;
    seen.add(key);
    rows.push(running ? { ...r, location, tba, running } : { ...r, location, tba });
  };

  const underWay = (live ?? []).filter((r) => r.start < site.today && !!r.end && r.end >= site.today);
  for (const r of live ?? []) if (r.start >= site.today) add(r);
  for (const r of adminRows) if (!covered.has(classLocation(r.location))) add(r);
  for (const location of covered) {
    for (const course of COURSES) {
      const hasStart = rows.some((r) => !r.tba && !r.running && r.course === course && r.location === location);
      if (hasStart) continue;
      const running = underWay.filter((r) => r.course === course && classLocation(r.location) === location);
      for (const r of running) add(r, true);
      if (running.length === 0 && offered(course, location)) add({ course, location, start: "", time: "", dates: "" });
    }
  }

  const order = (r: ShownRow) => site.locations[r.location]?.order ?? 99;
  const rank = (r: ShownRow) => (r.tba ? 2 : r.running ? 1 : 0);
  const sorted = rows
    .filter((r) => !scope.datedOnly || rank(r) === 0)
    .sort((a, b) => {
      if (rank(a) !== rank(b)) return rank(a) - rank(b);
      if (!a.tba) return a.start.localeCompare(b.start) || minutes(a.time) - minutes(b.time) || order(a) - order(b);
      return order(a) - order(b) || COURSES.indexOf(a.course) - COURSES.indexOf(b.course);
    });
  return scope.limit ? sorted.slice(0, scope.limit) : sorted;
}

const escapeHtml = (s: string) =>
  s.replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch]!);

export const money = (n: number) =>
  "$" + (Number.isInteger(n) ? n.toLocaleString("en-CA") : n.toLocaleString("en-CA", { minimumFractionDigits: 2, maximumFractionDigits: 2 }));

/** "Mon, Jan 11" for "2027-01-11", the day as written. */
export const fmtDate = (d: string) =>
  d ? new Date(`${d}T12:00:00Z`).toLocaleDateString("en-CA", { weekday: "short", month: "short", day: "numeric", timeZone: "UTC" }).replace(/\./g, "") : "";

const LINK = 'style="font-weight:700;color:var(--cta)"';

/** The table body for rows: the same at build time and in the browser. */
export function rowsHtml(rows: readonly ShownRow[], showCourse: boolean, site: SchedSite): string {
  return rows
    .map((r) => {
      const loc = site.locations[r.location];
      const course = site.courses[r.course];
      const price = loc?.prices[r.course] ?? 0;
      const label = r.location === "silverdale" ? "Silverdale (Maple Ridge / Mission)" : (loc?.label ?? r.location);
      const page = course?.localPages[r.location] ?? course?.page ?? "";
      // A class under way: its first day, then when it ends; "Get notified" asks about the next one.
      const note = r.running ? `In progress · last class ${fmtDate(r.end ?? "")}` : r.dates;
      const cells = [
        showCourse ? `<td><a href="${escapeHtml(page)}" style="text-decoration:none"><b>${escapeHtml((course?.name ?? r.course).replace("Obedience ", ""))}</b></a></td>` : "",
        `<td>${escapeHtml(label)}</td>`,
        r.tba
          ? '<td class="when"><span class="tba">TBA</span></td>'
          : `<td class="when">${escapeHtml(fmtDate(r.start))}${r.time ? `, ${escapeHtml(r.time)}` : ""}${note ? `<div class="muted" style="font-size:13px">${escapeHtml(note)}</div>` : ""}</td>`,
        `<td class="num">${price ? escapeHtml(money(price)) : "—"}</td>`,
        r.tba || r.running
          ? `<td class="act"><a href="#lead" ${LINK}>Get notified</a></td>`
          : `<td class="act"><a href="${escapeHtml(loc?.bookingUrl ?? "#lead")}" rel="noopener" ${LINK}>Book</a></td>`,
      ];
      // The page turns a row whose start has passed into TBA (Base.astro); a class under way ends instead.
      const marker = r.tba ? "" : r.running ? ` data-end="${escapeHtml(r.end ?? "")}"` : ` data-start="${escapeHtml(r.start)}"`;
      return `<tr${marker}>${cells.join("")}</tr>`;
    })
    .join("");
}

/** The portal's classes, or null when it can't be reached in time. */
export async function fetchPortalRows(timeoutMs = 8000, fetchImpl: typeof fetch = fetch): Promise<ClassRow[] | null> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const res = await fetchImpl(PORTAL_CLASSES_URL, { signal: controller.signal, headers: { Accept: "application/json" } });
    return res.ok ? portalRows(await res.json()) : null;
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}
