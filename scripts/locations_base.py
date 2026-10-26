# Starting data for each location (prices, hours, booking links). Copied from the live site and the approved design.
# After migration these live in src/data/locations/*.json and are edited in /admin.
LEADERSHIP_NAMES = {"Andy Krzus", "Marie Therese Krzus", "Thea"}


def loc(**k):
    k.setdefault("team", [])
    k.setdefault("reviewUrl", "")
    return k


LOCATIONS = {
    "stavefalls": loc(key="stavefalls", order=1, name="Stave Falls", slug="stave-falls", area="Maple Ridge / Mission",
        areaNote="North end of the Maple Ridge / Mission border", color="#FFC83D",
        street="12658 Powell St", city="Mission", region="BC", postal="", country="CA",
        blurb="On the north end of the Maple Ridge / Mission border: 10 acres of forest trails and open fields. A licensed and inspected commercial kennel with permits from the City of Mission and the Fraser Valley Regional District.",
        dropOff="7:45–10am", pickUp="4:30–7:15pm", bookingUrl="https://obedienceunleashed.propetware.com",
        daycare={"one": 48, "two": 86.40, "three": 124.80}, daycareHours=12,
        boarding={"one": 63, "two": 113.40, "three": 163.80}, boardTrain=4000,
        classes={"puppy": 0, "l1": 0, "l2": 0, "ol": 0}, consult=False,
        classNote="Maple Ridge / Mission group classes run at our Silverdale location, on the south end of the border.",
        offers=["Daycare", "Boarding", "Daycare bus", "Board and Train", "Group walks"], bus=True, walks="mission",
        teamPage="/meet-the-team-stave-falls/", daycarePage="/dog-daycare-maple-ridge-mission/", boardingPage="/dog-boarding-mission/"),
    "silverdale": loc(key="silverdale", order=2, name="Silverdale", slug="silverdale", area="Maple Ridge / Mission",
        areaNote="South end of the Maple Ridge / Mission border", color="#7FD8B0",
        street="9221 Woodward St", city="Mission", region="BC", postal="", country="CA",
        blurb="On the south end of the Maple Ridge / Mission border. The Silverdale Doggy Vacation Lodge: 5 acres with 3 acres of outdoor yards, a 4,000 sq ft covered arena and a water park. Home of our Maple Ridge / Mission group classes.",
        dropOff="7–10am", pickUp="4–6pm", bookingUrl="https://silverdaleobedienceunleashed.propetware.com",
        daycare={"one": 48, "two": 86.40, "three": 124.80}, daycareHours=12,
        boarding={"one": 63, "two": 113.40, "three": 163.80}, boardTrain=4000,
        classes={"puppy": 328, "l1": 328, "l2": 328, "ol": 834.75}, consult=True, classNote="",
        offers=["Daycare", "Boarding", "Daycare bus", "Puppy Class", "Bootcamp Level 1 & 2", "Off Leash Freedom", "Behaviour consults", "Board and Train"],
        bus=True, walks="mission",
        teamPage="/meet-the-team-silverdale/", daycarePage="/dog-daycare-silverdale-mission/", boardingPage="/dog-boarding-silverdale-mission/"),
    "chilliwack": loc(key="chilliwack", order=3, name="Chilliwack", slug="chilliwack", area="Chilliwack / Abbotsford",
        areaNote="Greendale, on the Abbotsford / Chilliwack border", color="#8CCBFF",
        street="6933 Chadsey Rd", city="Chilliwack", region="BC", postal="V2R 4K8", country="CA",
        blurb="5 acres just off Hwy 1 in Greendale, on the Abbotsford / Chilliwack border, with fenced yards and a climate-controlled area.",
        dropOff="7–10am", pickUp="3–6pm", bookingUrl="https://chilliwackobedienceunleashed.propetware.com",
        daycare={"one": 45, "two": 81, "three": 117}, daycareHours=10,
        boarding={"one": 60, "two": 108, "three": 156}, boardTrain=4000,
        classes={"puppy": 328, "l1": 328, "l2": 328, "ol": 834.75}, consult=True, classNote="",
        offers=["Daycare", "Boarding", "Puppy Class", "Bootcamp Level 1 & 2", "Off Leash Freedom", "Behaviour consults", "Board and Train", "Group walks"],
        bus=False, walks="chilliwack",
        teamPage="/meet-the-team-chilliwack/", daycarePage="/dog-daycare-chilliwack/", boardingPage="/chilliwack-boarding-and-daycare/"),
    "kamloops": loc(key="kamloops", order=4, name="Kamloops", slug="kamloops", area="Kamloops",
        areaNote="Barnhartvale, east Kamloops", color="#FFB394",
        street="9015 Barnhartvale Rd", city="Kamloops", region="BC", postal="", country="CA",
        blurb="6 acres in Barnhartvale with a dedicated 80 x 25 ft boarding building, 4 x 4 ft suites and a birch-chip yard.",
        dropOff="7:15–9am", pickUp="5:30–7pm", bookingUrl="https://kamloopsobedienceunleashed.propetware.com",
        daycare={"one": 35, "two": 0, "three": 0}, daycareHours=10,
        boarding={"one": 47.50, "two": 70, "three": 90}, boardTrain=3500,
        classes={"puppy": 379.99, "l1": 379.99, "l2": 0, "ol": 0}, consult=True, classNote="",
        offers=["Daycare", "Boarding", "Puppy Class", "Bootcamp Level 1", "Behaviour consults", "Board and Train", "15-min training walk add-on ($15)"],
        bus=False, walks="",
        teamPage="/meet-the-team-kamloops/", daycarePage="/dog-daycare-kamloops/", boardingPage="/dog-boarding-kamloops/"),
    "cochrane": loc(key="cochrane", order=5, name="Cochrane, AB", slug="cochrane", area="Cochrane / Calgary",
        areaNote="About 30 minutes from Calgary", color="#C9B8FF",
        street="#101 – 12 Griffin Industrial Point", city="Cochrane", region="AB", postal="", country="CA",
        blurb="Opened in 2019, with about 2,000 sq ft of indoor play, rest kennels and an outdoor potty area. Double-gated entry and play groups by size and temperament.",
        dropOff="7:15–9am", pickUp="4:45–6:30pm", bookingUrl="https://cochraneobedienceunleashed.propetware.com",
        daycare={"one": 42, "two": 0, "three": 0}, daycareHours=10,
        boarding={"one": 52, "two": 93.60, "three": 135.20}, boardTrain=3500,
        classes={"puppy": 295, "l1": 295, "l2": 295, "ol": 834.75}, consult=True, classNote="",
        offers=["Daycare", "Boarding", "Puppy Class", "Bootcamp Level 1 & 2", "Off Leash Freedom", "Behaviour consults", "Board and Train", "Group walks", "30-min private walk add-on ($15)"],
        bus=False, walks="cochrane",
        teamPage="/meet-the-team-cochrane/", daycarePage="/dog-daycare-cochrane-ab/", boardingPage="/dog-boarding-cochrane/"),
}
