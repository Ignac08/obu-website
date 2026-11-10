// Refreshes the class tables in the visitor's browser with the portal's classes as they are now,
// so a class the office adds in the portal shows without rebuilding the site
// (src/lib/live-classes.ts has the rules). If the portal can't be reached, the tables keep what the
// build showed.
import { bcToday, fetchPortalRows, rowsHtml, scheduleRows, type ClassRow, type SchedScope, type SchedSite } from "../lib/live-classes";

const tables = Array.from(document.querySelectorAll<HTMLElement>("[data-sched]"));
const data = document.querySelector<HTMLScriptElement>("script[data-sched-site]");

if (tables.length > 0 && data?.textContent) {
  const { site, adminRows } = JSON.parse(data.textContent) as { site: SchedSite; adminRows: ClassRow[] };
  site.today = bcToday();
  fetchPortalRows().then((live) => {
    if (!live) return;
    for (const table of tables) {
      const { scope, showCourse } = JSON.parse(table.dataset.sched ?? "{}") as { scope?: SchedScope; showCourse?: boolean };
      const rows = scheduleRows(scope ?? {}, adminRows, live, site);
      const body = table.querySelector("tbody");
      if (body) body.innerHTML = rowsHtml(rows, showCourse !== false, site);
      table.hidden = rows.length === 0;
    }
  });
}
