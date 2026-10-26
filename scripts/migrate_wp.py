"""One-time migration from the live WordPress site (obedienceunleashed.com) into this Astro site.

Reads the public WordPress REST API, then writes:
  src/content/pages/*.md     one file per URL (SEO title/description + migrated page text)
  src/content/blog/*.md      the blog posts, with their images
  src/data/locations/*.json  team rosters merged into each location
  src/data/reviews.json      testimonials found on the pages
  public/img/team, public/img/blog

Usage: python3 scripts/migrate_wp.py [cache_dir]
After launch, edit content in /admin (or the files directly). Re-running overwrites those files.
"""
import html, io, json, os, re, sys, urllib.request
from bs4 import BeautifulSoup
from markdownify import markdownify as mdify
from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(__file__))
from pages_registry import P
from locations_base import LOCATIONS, LEADERSHIP_NAMES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WP = "https://obedienceunleashed.com"
CACHE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, ".wp-cache")
os.makedirs(CACHE, exist_ok=True)


def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": "obu-migration", "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


def wp(kind):
    path = os.path.join(CACHE, f"{kind}.json")
    if not os.path.exists(path):
        open(path, "w").write(get(f"{WP}/wp-json/wp/v2/{kind}?per_page=100"))
    return {p["slug"]: p for p in json.load(open(path))}


def txt(el):
    return re.sub(r"\s+", " ", html.unescape(el.get_text(" ", strip=True))).strip()


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def save_image(url, out, size=None, square=False):
    dest = os.path.join(ROOT, "public", out)
    if os.path.exists(dest):
        return "/" + out
    try:
        im = Image.open(io.BytesIO(get(url, binary=True)))
    except Exception as e:  # missing or broken image on the old site
        print("  ! image failed", url, e)
        return ""
    im = ImageOps.exif_transpose(im).convert("RGB")
    if square:
        im = ImageOps.fit(im, (size, size), centering=(0.5, 0.35))
    elif size and im.width > size:
        im = im.resize((size, round(im.height * size / im.width)))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest, "JPEG", quality=80, optimize=True, progressive=True)
    return "/" + out


# ---------- page parsing ----------
def parse(raw):
    s = BeautifulSoup(raw, "lxml")
    out = {"testimonials": [], "team": []}
    for t in s.select(".et_pb_testimonial"):
        c = t.select_one(".et_pb_testimonial_content")
        a = t.select_one(".et_pb_testimonial_author")
        if c:
            paras = [txt(p) for p in c.find_all("p") if txt(p)] or [txt(c)]
            out["testimonials"].append({"text": "\n\n".join(paras), "author": txt(a) if a else ""})
        t.decompose()
    for m in s.select(".et_pb_team_member"):
        img = m.select_one("img")
        h = m.select_one(".et_pb_module_header")
        pos = m.select_one(".et_pb_member_position")
        desc = m.select_one(".et_pb_team_member_description")
        for e in (h, pos):
            if e: e.extract()
        for ul in desc.select("ul"): ul.decompose()
        src = img.get("src") if img else ""
        out["team"].append({"name": txt(h) if h else "", "role": txt(pos).replace(" | ", ", ") if pos else "",
                            "img": "" if src.startswith("data:") else src, "bio": txt(desc)})
        m.decompose()
    for e in s.find_all(string=re.compile(r"^\s*We put your pup first!\s*$")):
        e.parent.decompose()
    for sel in ["script", "style", "noscript", "iframe", "form", "svg", "button", ".et_pb_fullwidth_header", ".et_pb_button",
                ".et_pb_video", ".et_pb_video_box", ".et_pb_code", ".et_pb_social_icon", ".et_pb_post", ".et_pb_slide", "h1", "video"]:
        for e in s.select(sel): e.decompose()
    for tm in s.select(".et_pb_text"):
        t = tm.get_text()
        if "To build and enhance the relationship" in t or "Learn what people say about us" in t:
            tm.decompose()
    out["soup"] = s
    return out


def to_markdown(s, keep_images=False, image_dir="img/blog"):
    if keep_images:
        for img in s.find_all("img"):
            src = img.get("src", "")
            if not src.startswith("http") or "paw.png" in src:
                img.decompose(); continue
            name = slugify(os.path.splitext(os.path.basename(src.split("?")[0]))[0])[:60]
            local = save_image(src, f"{image_dir}/{name}.jpg", size=1400)
            if local:
                img["src"] = local
                img["alt"] = img.get("alt") or ""
            else:
                img.decompose()
    else:
        for e in s.select("img, .et_pb_image"): e.decompose()
    body = s.body or s
    m = mdify(str(body), heading_style="ATX", bullets="-")
    m = html.unescape(m).replace("\xa0", " ").replace("​", "")
    m = m.replace("https://obedienceunleashed.com/", "/").replace("http://obedienceunleashed.com/", "/")
    m = re.sub(r"\[\s*\]\([^)]*\)", "", m)
    m = re.sub(r"^\s*#+\s*$", "", m, flags=re.M)
    m = re.sub(r"[ \t]+\n", "\n", m)
    return tidy(m)


def tidy(m):
    m = re.sub(r"\n{3,}", "\n\n", m)
    return m.strip() + "\n"


HEAD = re.compile(r"^(#{1,6})\s*(.+?)\s*$|^\*\*([^*]+)\*\*\s*$")
LOCNAMES = r"(silverdale|stave falls|chilliwack|kamloops|cochrane|mission|maple ridge)"
DROP_SECTION = re.compile(r"rates|drop.?off|pick.?up times|upcoming|^address$|ready to get started|book your .* today|^booking$|"
                          r"contact us today|add-ons|class sessions?|^our (training|dog sitting) services|^what drives us|^testimonials$|"
                          r"^our mission$|^\*?read more|^convenient transportation|^new! daycare pick-up|"
                          r"^daycare bus service$|^affordable rates$", re.I)
SHARED_SECTION = re.compile(r"what you.ll learn|q&a topics|class requirements|dog training method", re.I)
DROP_LINE = re.compile(
    r"^\s*-?\s*\*\*(class( #\d)?( dates)?|class start time|class duration|location|age range|cost)\b.*|"
    r"^\s*-?\s*(mon|tue|wed|thu|fri|sat|sun)[a-z]*\.?\s.*(20\d\d|@).*|^\s*-?\s*(address|cost|price|upcoming classes start)\s*:.*|"
    r".*spots are limited.*|.*learn more about what we do.*|.*propetware\.com.*|^\s*(address|price):.*", re.I)


def filter_sections(md, drop_locations=False, drop_shared=False, drop_service_heads=()):
    out, dropping, level = [], False, 9
    for line in md.split("\n"):
        h = HEAD.match(line)
        if h:
            lv = len(h.group(1)) if h.group(1) else 7
            title = (h.group(2) or h.group(3) or "").strip("*: ").strip()
            if dropping and lv > level:
                continue
            dropping = False
            if (DROP_SECTION.search(title) or (drop_shared and SHARED_SECTION.search(title))
                    or (drop_locations and re.fullmatch(LOCNAMES + r".*", title, re.I) and len(title) < 45)):
                dropping, level = True, lv
                continue
            if title.lower() in drop_service_heads:
                continue
        if dropping:
            continue
        if DROP_LINE.match(line):
            continue
        out.append(line)
    return tidy("\n".join(out))


def fm(d):
    lines = ["---"]
    for k, v in d.items():
        if v in (None, "", [], False) and k not in ("title",):
            continue
        lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


SERVICE_HEADS = {"obedience bootcamp level 1", "obedience bootcamp level 2", "private consultation", "puppy class", "board & train",
                 "off leash freedom", "dog daycare", "dog boarding", "group walks"}


def main():
    pages, posts = wp("pages"), wp("posts")
    reviews = []
    teams = {}
    for p in P:
        slug = p["slug"]
        src = pages.get(slug)
        body = ""
        if src:
            parsed = parse(src["content"]["rendered"])
            t = p["template"]
            for r in parsed["testimonials"]:
                reviews.append({"text": r["text"], "author": r["author"], "pages": [slug],
                                "service": p.get("service", ""), "location": p.get("location", "")})
            if parsed["team"]:
                teams[slug] = parsed["team"]
            md = to_markdown(parsed["soup"], keep_images=(t == "prose"), image_dir=f"img/pages/{slug}")
            if t in ("service-location", "care-location"):
                body = filter_sections(md, drop_shared=(p["service"] in ("puppy", "l1", "l2")), drop_service_heads=SERVICE_HEADS)
            elif t in ("service", "care", "boardtrain", "walks"):
                body = filter_sections(md, drop_locations=True, drop_service_heads=SERVICE_HEADS)
            elif t in ("prose", "servicedogs"):
                body = filter_sections(md)
        meta = {k: p[k] for k in ("title", "description", "h1", "lead", "template", "service", "location", "town")}
        meta["noindex"] = p["noindex"]
        path = os.path.join(ROOT, "src/content/pages", slug + ".md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(fm(meta) + ("\n" + body if body.strip() else ""))

    # teams -> locations
    validators = teams.pop("service-dog-assessments", [])
    for slug, members in teams.items():
        key = slug.replace("meet-the-team-", "").replace("-", "")
        loc = LOCATIONS[key]
        roster = []
        for m in members:
            if m["name"] in LEADERSHIP_NAMES:
                continue
            photo = save_image(m["img"], f"img/team/{key}-{slugify(m['name'])}.jpg", size=360, square=True) if m["img"] else ""
            roster.append({"name": m["name"], "role": m["role"], "photo": photo, "bio": m["bio"]})
        loc["team"] = roster
    for key, loc in LOCATIONS.items():
        json.dump(loc, open(os.path.join(ROOT, "src/data/locations", f"{key}.json"), "w"), indent=2, ensure_ascii=False)
    json.dump({"validators": [{"name": v["name"], "role": v["role"]} for v in validators]},
              open(os.path.join(ROOT, "src/data/validators.json"), "w"), indent=2, ensure_ascii=False)

    # testimonials page and home reviews
    tp = parse(pages["testimonials"]["content"]["rendered"])
    for r in tp["testimonials"]:
        reviews.append({"text": r["text"], "author": r["author"], "pages": ["testimonials"], "service": "", "location": ""})
    seen, uniq = set(), []
    for r in reviews:
        k = r["text"][:80]
        if k in seen:
            for u in uniq:
                if u["text"][:80] == k:
                    u["pages"] = sorted(set(u["pages"] + r["pages"]))
            continue
        seen.add(k); uniq.append(r)
    json.dump({"reviews": uniq}, open(os.path.join(ROOT, "src/data/reviews-migrated.json"), "w"), indent=2, ensure_ascii=False)

    # blog
    from blog_meta import POSTS
    for slug, meta in POSTS.items():
        src = posts[slug]
        s = BeautifulSoup(src["content"]["rendered"], "lxml")
        md = to_markdown(s, keep_images=True, image_dir="img/blog")
        md = re.sub(r"^#\s", "## ", md, flags=re.M)
        front = {"title": html.unescape(src["title"]["rendered"]), "description": meta["description"],
                 "date": src["date"][:10], "author": meta["author"], "category": meta["category"], "also": meta.get("also", ""),
                 "image": f"/img/{meta['img']}.jpg", "summary": meta["summary"], "featured": meta.get("featured", False)}
        open(os.path.join(ROOT, "src/content/blog", slug + ".md"), "w").write(fm(front) + "\n" + md)
    print("done:", len(P), "pages,", len(POSTS), "posts,", len(uniq), "reviews")


if __name__ == "__main__":
    main()
