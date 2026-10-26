# Every public URL on the new site, with its template and SEO text.
# Used once by migrate_wp.py to create src/content/pages/*.md (after that, edit the .md files or use /admin).
# (slug, template, service, location, town, title, description, h1, lead)

P = []
def add(slug, template, title, description, h1, lead="", service="", location="", town="", noindex=False):
    P.append(dict(slug=slug, template=template, service=service, location=location, town=town,
                  title=title, description=description, h1=h1, lead=lead, noindex=noindex))

add("index", "home", "Dog Training, Daycare & Boarding in BC and Alberta",
    "Family-run dog training, daycare and boarding since 2009. Puppy classes, obedience bootcamps, Board and Train and more at 5 locations in Maple Ridge / Mission, Chilliwack, Kamloops and Cochrane.",
    "Happier dogs. Calmer homes.")
add("training", "training", "Dog Training Classes & Programs",
    "Puppy classes, Obedience Bootcamp Level 1 and 2, Off Leash Freedom, behaviour consultations and Board and Train in Maple Ridge / Mission, Chilliwack, Kamloops and Cochrane.",
    "Training that fits where your dog is today",
    "Small group classes with written notes and video, private consultations, and our live-in Board and Train program. Every program is taught by trainers who complete 40+ hours of professional education a year.")

# ---- Puppy Class
add("puppy-class", "service", "Puppy Classes: 5-Week Foundation Course",
    "Join our Puppy Class for comprehensive training on important life skills. Say goodbye to unwanted behaviours and hello to a well-behaved pup! 4 locations in BC and Alberta.",
    "The foundation every puppy needs.", service="puppy")
add("puppy-class-mission", "service-location", "Puppy Class in Mission, BC",
    "Puppy classes in Mission on the Maple Ridge / Mission border. 5 one-hour classes, max 8 puppies, notes and video every week. Book your spot today.",
    "Puppy Class in Mission", "Start your puppy off on the right paw with puppy classes on the Maple Ridge / Mission border.", service="puppy", location="silverdale", town="Mission")
add("puppy-class-silverdale", "service-location", "Puppy Class in Silverdale (Maple Ridge / Mission)",
    "Puppy classes at our Silverdale facility on the Maple Ridge / Mission border. 5 one-hour classes, max 8 puppies, notes and video every week.",
    "Puppy Class in Silverdale", "Start training with puppy classes on the Maple Ridge / Mission border to build obedience, good manners and a lifelong bond.", service="puppy", location="silverdale", town="Silverdale")
add("puppy-class-maple-ridge", "service-location", "Puppy Class in Maple Ridge, BC",
    "Puppy classes for Maple Ridge dog owners at our Silverdale facility on the Maple Ridge / Mission border. 5 one-hour classes, max 8 puppies.",
    "Puppy Class in Maple Ridge", "Start the training journey with puppy classes for Maple Ridge to build confidence, good manners and a lifelong bond.", service="puppy", location="silverdale", town="Maple Ridge")
add("puppy-class-chilliwack", "service-location", "Puppy Class in Chilliwack & Abbotsford",
    "Puppy classes in Chilliwack on the Abbotsford / Chilliwack border. Train your puppy with our head trainer for effective communication and lifelong success.",
    "Puppy Class in Chilliwack", "Start your puppy off on the right paw with puppy classes in Chilliwack.", service="puppy", location="chilliwack", town="Chilliwack")
add("puppy-class-kamloops", "service-location", "Puppy Class in Kamloops",
    "Looking for a puppy class in Kamloops? Learn valuable skills to train your puppy and build a strong bond with trainers Heidi and Daymon in Barnhartvale.",
    "Puppy Class in Kamloops", "Meet our trainers Heidi and Daymon for puppy class in Kamloops.", service="puppy", location="kamloops", town="Kamloops")
add("puppy-class-cochrane", "service-location", "Puppy Class in Cochrane, AB",
    "Puppy classes in Cochrane, AB, 30 minutes from Calgary. 5 one-hour classes with trainer Kim to set your pup up for a lifetime of success.",
    "Puppy Class in Cochrane, AB", "Meet our trainer Kim for puppy class to set your pup up for a lifetime of success.", service="puppy", location="cochrane", town="Cochrane")

# ---- Level 1
add("obedience-bootcamp-level-1", "service", "Obedience Bootcamp Level 1: Group Dog Training",
    "Train your dog for obedience in a group setting. Our Obedience Bootcamp covers engagement, loose leash walking, recall and more. Dogs 7 months to 10 years.",
    "A dog that listens the first time.", service="l1")
add("obedience-bootcamp-level-1-mission", "service-location", "Obedience Classes in Mission, BC (Level 1)",
    "Obedience Bootcamp Level 1 for adult dogs in Mission. Learn essential obedience commands and improve your bond with your dog in a small group class.",
    "Obedience Bootcamp Level 1 in Mission", "Obedience classes for your adult dog at our Silverdale facility on the Maple Ridge / Mission border.", service="l1", location="silverdale", town="Mission")
add("obedience-bootcamp-level-1-maple-ridge", "service-location", "Obedience Classes in Maple Ridge, BC (Level 1)",
    "Obedience Bootcamp Level 1 for Maple Ridge dog owners. Train your adult dog in a small group class to build a strong bond and practise obedience.",
    "Obedience Bootcamp Level 1 in Maple Ridge", "Obedience classes for your adult dog, held at our Silverdale facility on the Maple Ridge / Mission border.", service="l1", location="silverdale", town="Maple Ridge")
add("obedience-bootcamp-level-1-chilliwack", "service-location", "Obedience Classes in Chilliwack & Abbotsford (Level 1)",
    "Obedience Bootcamp Level 1 in Chilliwack for dogs 7 months to 10 years. Enhance your dog's obedience skills and build a strong relationship.",
    "Obedience Bootcamp Level 1 in Chilliwack", "Obedience training for your adult dog with our head trainer Deb.", service="l1", location="chilliwack", town="Chilliwack")
add("obedience-bootcamp-level-1-kamloops", "service-location", "Obedience Classes in Kamloops (Level 1)",
    "Enrol your dog in our Obedience Bootcamp Level 1 class in Kamloops. Strengthen your bond and develop obedience skills in a group setting.",
    "Obedience Bootcamp Level 1 in Kamloops", "Obedience Bootcamp Level 1 for adult dogs with our trainers Heidi and Daymon.", service="l1", location="kamloops", town="Kamloops")
add("obedience-bootcamp-level-1-cochrane", "service-location", "Obedience Classes in Cochrane, AB (Level 1)",
    "Join our Obedience Bootcamp Level 1 in Cochrane, AB and give your dog the training they need. Register now for upcoming classes.",
    "Obedience Bootcamp Level 1 in Cochrane, AB", "Group obedience classes for your adult dog with our trainer Kim.", service="l1", location="cochrane", town="Cochrane")

# ---- Level 2
add("obedience-bootcamp-level-2", "service", "Obedience Bootcamp Level 2: Advanced Group Class",
    "Take obedience into the real world. Level 2 uses toys as rewards and proofs your dog's skills around real-life distractions. Mission, Chilliwack and Cochrane.",
    "Take it out into the real world.", service="l2")
add("obedience-unleashed-bootcamp-level-2-mission", "service-location", "Obedience Bootcamp Level 2 in Mission / Maple Ridge",
    "Advanced Obedience Bootcamp Level 2 at our Silverdale facility on the Maple Ridge / Mission border. Toy rewards and proofing around real-life distractions.",
    "Obedience Bootcamp Level 2 in Mission / Maple Ridge", "Our advanced Level 2 class for Maple Ridge and Mission dogs.", service="l2", location="silverdale", town="Mission")
add("obedience-bootcamp-level-2-chilliwack", "service-location", "Obedience Bootcamp Level 2 in Chilliwack & Abbotsford",
    "Advanced Obedience Bootcamp Level 2 in Chilliwack with head trainer Deb. Toy rewards and proofing around real-life distractions.",
    "Obedience Bootcamp Level 2 in Chilliwack", "Our advanced Level 2 class with head trainer Deb.", service="l2", location="chilliwack", town="Chilliwack")

# ---- Off Leash, consult
add("off-leash-freedom", "service", "Off Leash Freedom: Off-Leash Recall Training",
    "Take your dog's training to the next level with off-leash recall. Practical exercises to improve obedience and address behaviour issues.",
    "Let them run. Know they'll come back.", service="ol")
add("behavioural-consultation", "service", "Behavioural Consultation for Dogs: $50",
    "Private in-person behavioural consultations in Mission, Chilliwack, Kamloops and Cochrane. A trainer observes your dog and recommends a plan of action.",
    "Not sure where to start? Start here.", service="consult")
add("behavioural-consultation-maple-ridge-mission", "service-location", "Dog Behaviour Consultation in Maple Ridge / Mission",
    "Private behavioural consultation in Maple Ridge and Mission. Meet with our trainers to address your dog's behaviour and create a training plan.",
    "Behavioural Consultation in Maple Ridge / Mission", "Meet our trainers to discuss your dog's behaviour and create a training plan to meet your needs.", service="consult", location="silverdale", town="Maple Ridge / Mission")
add("behavioural-consultation-chilliwack", "service-location", "Dog Behaviour Consultation in Chilliwack & Abbotsford",
    "Looking for a dog behaviour consultation in Chilliwack? Our experienced trainer will observe your dog's behaviour and create a training plan.",
    "Behavioural Consultation in Chilliwack", "Meet our head trainer Deb for a private initial consultation and a training plan.", service="consult", location="chilliwack", town="Chilliwack")
add("behavioural-consultation-kamloops", "service-location", "Dog Behaviour Consultation in Kamloops",
    "Private dog behaviour consultation in Kamloops with trainers Heidi and Daymon. We observe your dog, discuss options and recommend a training plan.",
    "Behavioural Consultation in Kamloops", "Meet our trainers Heidi and Daymon to discuss your dog's behaviour and create a training plan.", service="consult", location="kamloops", town="Kamloops")
add("behavioural-consultation-cochrane-ab", "service-location", "Dog Behaviour Consultation in Cochrane, AB",
    "Private dog behaviour consultation in Cochrane, AB with trainer Kim. We observe your dog, discuss your goals and recommend a training plan.",
    "Behavioural Consultation in Cochrane, AB", "Meet our trainer Kim to discuss your dog's behaviour and training needs.", service="consult", location="cochrane", town="Cochrane")

add("board-and-train", "boardtrain", "Board and Train: 4-Week Dog Rehabilitation Program",
    "Get your dog trained while they stay with us. Our 4-week Board and Train program tackles aggression, reactivity, anxiety and fear, with follow-up for you.",
    "Board and Train", "Rehabilitation-focused training for dogs with serious behaviour problems. Your dog lives with us for four weeks, then we teach you to keep it going at home.")

# ---- Daycare
add("dog-daycare", "care", "Dog Daycare in BC and Alberta",
    "Give your pup the ultimate doggy daycare experience. Personalized care, playgroups, walks and photo updates at 5 locations in BC and Alberta.",
    "A full, happy day while you work", "Playgroups by size and temperament, walks, one-on-one staff time, toy play and scheduled rest. You get photo updates through the day, and we contact you right away with any concern.", service="daycare")
add("dog-daycare-maple-ridge-mission", "care-location", "Dog Daycare in Maple Ridge / Mission (Stave Falls)",
    "Reliable dog daycare for Mission and Maple Ridge on 10 acres at Stave Falls. A safe, engaging place for your pup to play, socialize and relax. Daycare bus available.",
    "Dog Daycare in Maple Ridge / Mission", "On 10 acres at Stave Falls, at the north end of the Maple Ridge / Mission border.", service="daycare", location="stavefalls", town="Maple Ridge / Mission")
add("dog-daycare-silverdale-mission", "care-location", "Dog Daycare in Silverdale (Maple Ridge / Mission)",
    "Silverdale dog daycare on the Maple Ridge / Mission border: a safe, stimulating space to play, socialize and relax, with a covered arena and water park. Daycare bus available.",
    "Dog Daycare in Silverdale", "At the Silverdale Doggy Vacation Lodge, at the south end of the Maple Ridge / Mission border.", service="daycare", location="silverdale", town="Silverdale")
add("dog-daycare-chilliwack", "care-location", "Dog Daycare in Chilliwack & Abbotsford",
    "Reliable dog daycare in Chilliwack on 5 acres off Hwy 1 in Greendale, on the Abbotsford / Chilliwack border. Supervised social time and personalized care.",
    "Dog Daycare in Chilliwack", "On 5 acres just off Highway 1 in Greendale, on the Abbotsford / Chilliwack border.", service="daycare", location="chilliwack", town="Chilliwack")
add("dog-daycare-kamloops", "care-location", "Dog Daycare in Kamloops",
    "Dog daycare in Kamloops on 6 acres in Barnhartvale. Supervised social time, walks and tailored care to give you peace of mind.",
    "Dog Daycare in Kamloops", "On 6 acres in Barnhartvale, east of Kamloops.", service="daycare", location="kamloops", town="Kamloops")
add("dog-daycare-cochrane-ab", "care-location", "Dog Daycare in Cochrane, AB",
    "Looking for doggy daycare in Cochrane? Our conveniently located facility offers indoor play, rest kennels and play groups by size and temperament.",
    "Dog Daycare in Cochrane, AB", "Conveniently located in Cochrane, about 30 minutes from Calgary.", service="daycare", location="cochrane", town="Cochrane")
add("dog-daycare-calgary", "care-location", "Dog Daycare for Calgary (NW Calgary & Cochrane)",
    "Looking for reliable dog daycare near Calgary? Our Cochrane facility, minutes from NW Calgary, offers a safe, engaging place for your pup to play, socialize and relax.",
    "Dog Daycare for Calgary", "Our Cochrane facility is a short drive from NW Calgary.", service="daycare", location="cochrane", town="Calgary")

# ---- Boarding
add("dog-boarding", "care", "Dog Boarding in BC and Alberta",
    "Climate-controlled suites, supervised playgroups and one-on-one time with certified staff. Dog boarding at 5 locations in BC and Alberta.",
    "Peace of mind while you're away", "Climate-controlled overnight suites, supervised playgroups and one-on-one time, with staff certified by Dog Handler Academy and in Pet First Aid. Photo updates included.", service="boarding")
add("dog-boarding-mission", "care-location", "Dog Boarding in Mission / Maple Ridge (Stave Falls)",
    "Dog boarding for Mission and Maple Ridge on 10 acres at Stave Falls. A tailored boarding program with comfort, fun and peace of mind.",
    "Dog Boarding in Mission / Maple Ridge", "On 10 acres at Stave Falls, at the north end of the Maple Ridge / Mission border.", service="boarding", location="stavefalls", town="Mission / Maple Ridge")
add("dog-boarding-silverdale-mission", "care-location", "Dog Boarding in Silverdale (Maple Ridge / Mission)",
    "Dog boarding at the Silverdale Doggy Vacation Lodge on the Maple Ridge / Mission border. Your dog will be cared for and have lots of fun on our 5-acre property.",
    "Dog Boarding in Silverdale", "At the Silverdale Doggy Vacation Lodge, at the south end of the Maple Ridge / Mission border.", service="boarding", location="silverdale", town="Silverdale")
add("chilliwack-boarding-and-daycare", "care-location", "Dog Boarding in Chilliwack & Abbotsford",
    "Convenient and trusted dog boarding in Chilliwack. Spacious overnight suites provide a comfortable and fun stay for your dog on our 5-acre property.",
    "Dog Boarding in Chilliwack", "On 5 acres just off Highway 1 in Greendale, on the Abbotsford / Chilliwack border.", service="boarding", location="chilliwack", town="Chilliwack")
add("dog-boarding-kamloops", "care-location", "Dog Boarding & Kennel in Kamloops",
    "Reliable and fun dog boarding in Kamloops. Individual climate-controlled suites, daily outings and supervised play on 6 acres in Barnhartvale.",
    "Dog Boarding in Kamloops", "On 6 acres in Barnhartvale, about 20 minutes from Kamloops.", service="boarding", location="kamloops", town="Kamloops")
add("dog-boarding-cochrane", "care-location", "Dog Boarding in Cochrane, AB",
    "Enjoy peace of mind while you're away. Our dog boarding program in Cochrane, AB provides a comfortable and fun stay for your dog.",
    "Dog Boarding in Cochrane, AB", "Conveniently located in Cochrane, about 30 minutes from Calgary.", service="boarding", location="cochrane", town="Cochrane")

add("group-walks", "walks", "Group Dog Walks & Socialization Classes",
    "Weekend group walks in Mission, Maple Ridge, Chilliwack and Cochrane. A formal obedience meet-and-greet, then a leashed walk at a local park. $15 drop-in.",
    "Group walks", "Rain or shine. A formal obedience meet-and-greet, then a leashed walk at a local park. Guests welcome.")
add("rates", "rates", "Dog Training, Boarding & Daycare Rates",
    "Compare rates for dog training, boarding and daycare at each Obedience Unleashed location in Maple Ridge / Mission, Chilliwack, Kamloops and Cochrane.",
    "Clear prices, by location", "All prices plus tax. Classes and consultations are paid at booking. Boarding and daycare are paid on the first day.")
add("service-dog-assessments", "servicedogs", "BC Guide & Service Dog Assessments",
    "Obedience Unleashed coordinates BC Guide and Service Dog Assessments for the Province of BC. How to apply, what the assessment covers, fees and testing locations.",
    "BC Guide & Service Dog Assessments", "Since April 1, 2024 we coordinate Guide and Service Dog assessments for the Security Programs Division, Ministry of Public Safety and Solicitor General.")
add("locations", "locations", "Our Locations: Maple Ridge / Mission, Chilliwack, Kamloops, Cochrane",
    "Five Obedience Unleashed locations: Stave Falls and Silverdale on the Maple Ridge / Mission border, Chilliwack, Kamloops and Cochrane, AB.",
    "Find your closest Obedience Unleashed", "Each location books through its own system. Accounts don't transfer between locations, so pick the one you'll use most.")
for k, name, title, desc in [
    ("stave-falls", "stavefalls", "Stave Falls: Dog Daycare & Boarding, Maple Ridge / Mission", "Our Stave Falls location on the north end of the Maple Ridge / Mission border: 10 acres of trails and fields for daycare, boarding and Board and Train."),
    ("silverdale", "silverdale", "Silverdale: Dog Training, Daycare & Boarding, Maple Ridge / Mission", "The Silverdale Doggy Vacation Lodge on the south end of the Maple Ridge / Mission border: group classes, daycare, boarding, a covered arena and a water park."),
    ("chilliwack", "chilliwack", "Chilliwack: Dog Training, Daycare & Boarding", "Our Chilliwack location on 5 acres in Greendale, on the Abbotsford / Chilliwack border: classes, daycare, boarding and group walks."),
    ("kamloops", "kamloops", "Kamloops: Dog Training, Daycare & Boarding", "Our Kamloops location on 6 acres in Barnhartvale: puppy and obedience classes, daycare and boarding with Heidi and Daymon Skelton."),
    ("cochrane", "cochrane", "Cochrane, AB: Dog Training, Daycare & Boarding near Calgary", "Our Cochrane, AB location, about 30 minutes from Calgary: classes, daycare, boarding and group walks."),
]:
    add(f"locations/{k}", "location", title, desc, "", location=name)
for slug, loc, town in [("meet-the-team-stave-falls","stavefalls","Stave Falls"),("meet-the-team-silverdale","silverdale","Silverdale"),("meet-the-team-chilliwack","chilliwack","Chilliwack"),("meet-the-team-kamloops","kamloops","Kamloops"),("meet-the-team-cochrane","cochrane","Cochrane, AB")]:
    add(slug, "team", f"Meet the {town} Team", f"Meet the trainers and kennel staff at Obedience Unleashed {town}.", f"Meet the {town} team", location=loc, town=town)
add("about", "about", "About Us: Family-Run Dog Training Since 2009",
    "Founded in 2009 by Marie and Andy Krzus, Obedience Unleashed has grown to five locations and more than 40 staff. Meet our leadership team.",
    "Family-run. Trainer-led.", "Founded by Marie and Andy Krzus during a family camping trip in Golden Ears Park, Obedience Unleashed has grown to five locations and more than 40 staff.")
add("meet-the-trainer", "prose", "Meet the Trainer: Andy Krzus, Maple Ridge Dog Trainer",
    "Andy Krzus is the founder and head trainer of Obedience Unleashed, with a background training police, search and rescue and assistance dogs.",
    "Meet the trainer: Andy Krzus", "Professional dog trainer, owner and founder of Obedience Unleashed Dog Training Inc.")
add("testimonials", "testimonials", "Testimonials & Reviews",
    "What dog owners say about Obedience Unleashed training, daycare and boarding. Rated 4.8 stars from 130 Google reviews.",
    "What dog owners say", "Real words from real clients, across all five locations.")
add("contact-us", "contact", "Contact Us",
    "Call 1-844-900-3647 (Mon–Fri 9am–4pm) or send us a message. We reply within one business day. 5 locations in BC and Alberta.",
    "Let's talk about your dog", "Fill in the form and our office will call or email you back within one business day, or call us during phone hours.")
add("blog", "blog", "Blog: Dog Training Tips from Our Trainers",
    "Practical advice from our trainers on puppies, training, daycare and life with dogs in BC and Alberta.",
    "The Obedience Unleashed blog", "Practical advice from our trainers on puppies, training, daycare and life with dogs in BC and Alberta. Pick a topic to get started.")
add("obu-k9", "prose", "OBU-K9: Search and Rescue Dog Team",
    "OBU-K9 is an independent not-for-profit search and recovery K9 team based in Mission, BC, partnered with Obedience Unleashed.",
    "OBU-K9", "With the hopes of 'Bringing them home'. Located in Mission, BC.")
add("thank-you", "thanks", "Thank You", "Thanks for your message.", "Thanks! We got your message.", noindex=True)
add("404", "notfound", "Page Not Found", "Sorry, that page could not be found.", "We can't find that page", noindex=True)
