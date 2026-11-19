from ui import *
from data import SITE, SERVICES, INDUSTRIES, PROJECTS, PROJECT_CATS, ARTICLES, INSIGHT_CATS, TECH


# ================================================================ ABOUT
def about():
    b = ""
    values = [("bulb", "Innovation", "We explore new ideas and modern technologies to create solutions that keep our clients ahead."), ("shield", "Reliability", "We build secure, stable systems and deliver on the commitments we make."),
              ("eye", "Transparency", "Clear communication, honest estimates and full visibility of progress."), ("handshake", "Collaboration", "We work as one team with our clients, sharing knowledge and ownership."),
              ("star", "Excellence", "We hold our craft to a high standard, from code quality to user experience.")]
    expertise = [("code", "Software Engineering", "Web, mobile and enterprise applications built with modern, maintainable code."), ("cloud", "Cloud & DevOps", "Scalable cloud infrastructure, automation and continuous delivery."),
                 ("cpu", "AI & Data", "Practical AI features, intelligent automation and data platforms."), ("palette", "Product & UX Design", "Research-led, accessible design that people enjoy using."),
                 ("chart", "Strategy & Consulting", "Technology roadmaps and architecture that align with business goals."), ("lock", "Security & Quality", "Secure-by-design development, testing and code review.")]
    approach = [("search", "Understand first", "We start with your goals, users and constraints before proposing any technology."), ("layers", "Design for change", "Modular, well-documented architecture that is easy to extend."),
                ("zap", "Deliver in increments", "Working software every sprint, so you see progress and can steer early."), ("trend", "Measure and improve", "We track outcomes after launch and keep improving what matters.")]
    body = page_hero(b, "About NexTech Digital", "Engineering Digital Solutions That Last", "A London-based technology company helping businesses build, modernise and scale since 2018.", "About Us", "nx-team") + f'''
<section class="sec"><div class="container two-col">
  <div>{eyebrow("Who We Are")}<h2 class="sec-title" data-split>Technology Partners for Ambitious Businesses</h2>
    <p data-reveal>NexTech Digital was established in London in {SITE["founded"]} with a simple belief: technology should make businesses better at what they do. We bring together software engineers, cloud specialists, designers and strategists to deliver digital solutions that solve real problems.</p>
    <p data-reveal style="--d:.08s">We work with start-ups, growing companies and established organisations across technology, finance, healthcare, retail, education, manufacturing and logistics. Whether it is a new product, a cloud migration or an AI-powered workflow, we focus on outcomes, quality and long-term partnership.</p>
    <ul class="ticks" data-reveal style="--d:.16s"><li>{icon("check")}Headquartered in London, supporting clients globally</li><li>{icon("check")}End-to-end delivery: strategy, design, build and support</li><li>{icon("check")}Transparent, collaborative ways of working</li></ul>
  </div>
  <div class="collage" data-reveal="zoom">
    <div class="cl-a img-frame" data-parallax="-.06">{img(b, "developers", "Developers collaborating at a desk")}</div>
    <div class="cl-b img-frame" data-parallax=".08">{img(b, "office", "Bright modern office")}</div>
    <div class="cl-badge"><b>{SITE["founded"]}</b><span>Established in London</span></div>
  </div>
</div></section>

<section class="sec sec-light"><div class="container">
  <div class="mv big">
    <article class="mv-card" data-reveal data-glow><span class="mv-ic">{icon("target")}</span><div><h3>Our Mission</h3><p>To empower businesses with innovative, reliable and scalable technology solutions that create measurable value.</p></div></article>
    <article class="mv-card" data-reveal data-glow style="--d:.1s"><span class="mv-ic">{icon("eye")}</span><div><h3>Our Vision</h3><p>To be a globally trusted digital partner, driving business growth through technology and innovation.</p></div></article>
  </div>
</div></section>

<section class="sec"><div class="container">
  {head_block("Core Values", "The Principles Behind Everything We Build", "", True)}
  <div class="values">{"".join(f'<article class="value" data-reveal data-glow style="--d:{i * .07:.2f}s"><span class="v-num">0{i + 1}</span><span class="svc-ic">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(values))}</div>
</div></section>

<section class="sec sec-dark"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container">
  {head_block("Our Expertise", "Technical Capabilities Across the Digital Lifecycle", "Multidisciplinary skills that let us take an idea from first workshop to a product in production.", True)}
  <div class="exp-grid">{"".join(f'<article class="exp" data-reveal data-glow style="--d:{i * .06:.2f}s">{icon(ic)}<h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(expertise))}</div>
</div></section>

<section class="sec"><div class="container two-col rev">
  <div class="img-frame tall" data-reveal="zoom">{img(b, "whiteboard", "Team planning a project on a whiteboard")}</div>
  <div>{eyebrow("Our Approach")}<h2 class="sec-title" data-split>Our Approach to Digital Innovation</h2><p class="sec-sub" data-reveal>Innovation is not about using the newest tool. It is about solving the right problem in a way that lasts.</p>
    <ol class="approach">{"".join(f'<li data-reveal style="--d:{i * .08:.2f}s"><span>{icon(ic)}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (ic, t, d) in enumerate(approach))}</ol>
  </div>
</div></section>

<section class="sec sec-light"><div class="container two-col">
  <div>{eyebrow("Our People")}<h2 class="sec-title" data-split>A Team of Builders, Thinkers and Problem-Solvers</h2>
    <p data-reveal>Our team combines engineering depth with business understanding. We hire curious people who care about craft, communicate openly and enjoy solving hard problems together.</p>
    {flag("Leadership profiles (names, roles, photos and bios) will be added here once confirmed. No team members are shown until real information is available.")}
    <div data-reveal>{btn("careers.html", "Join Our Team", "soft")}</div></div>
  <div class="img-frame" data-reveal="zoom" data-tilt>{img(b, "team-laptops", "Team members working together on laptops")}</div>
</div></section>
''' + cta_band(b, "Let&#8217;s Work Together", "Build What&#8217;s Next.", "Tell us about your goals and we will help you find the right technology path.", "Let&#8217;s Work Together")
    return page("about.html", "About Us", "Learn about NexTech Digital, a London-based technology company established in 2018: our mission, vision, core values, expertise and approach to digital innovation.", body, "about.html", og_img="nx-team")


# ================================================================ SERVICES
def services():
    b = ""
    tabs = "".join(f'<a href="#{s["id"]}" data-spy="{s["id"]}">{icon(s["icon"])}<span>{s["name"]}</span></a>' for s in SERVICES)
    blocks = []
    for i, s in enumerate(SERVICES):
        rev = " rev" if i % 2 else ""
        offers = "".join(f'<li>{icon("check")}{o}</li>' for o in s["offerings"])
        bens = "".join(f'<div class="ben" data-reveal style="--d:{j * .06:.2f}s"><h4>{t}</h4><p>{d}</p></div>' for j, (t, d) in enumerate(s["benefits"]))
        tech = "".join(f'<span>{t}</span>' for t in s["tech"])
        blocks.append(f'''<section class="svc-detail{rev}" id="{s["id"]}">
  <div class="sd-media" data-reveal="zoom"><div class="img-frame" data-tilt>{img(b, s["img"], s["name"])}</div><span class="sd-num">0{i + 1}</span><div class="sd-float">{icon(s["icon"])}</div></div>
  <div class="sd-copy">
    <p class="eyebrow" data-reveal>Service 0{i + 1}</p><h2 class="sec-title sm" data-split>{s["name"]}</h2>
    <p class="sd-ov" data-reveal>{s["overview"]}</p>
    <h3 class="mini-h" data-reveal>Key offerings</h3><ul class="offer" data-reveal>{offers}</ul>
    <h3 class="mini-h" data-reveal>Business benefits</h3><div class="bens">{bens}</div>
    <div class="pills" data-reveal><b>Technologies:</b>{tech}</div>
    <div data-reveal>{btn(f"contact.html?service={s['id']}#enquiry", "Discuss Your Project")}</div>
  </div>
</section>''')
    faqs = [("How do you price projects?", "Most projects are priced as a fixed scope for a defined phase, or as a monthly team for ongoing product work. After an initial discovery call we provide a clear, written estimate."),
            ("How long does a typical project take?", "A focused website or prototype can take a few weeks; larger platforms are delivered in phases over several months. We always aim to ship something usable early."),
            ("Can you work with our existing team and systems?", "Yes. We regularly integrate with in-house teams, existing codebases and third-party systems, and can hand over fully documented work."),
            ("Do you provide support after launch?", "Yes. We offer maintenance, monitoring and continuous improvement plans tailored to the solution and your needs."),
            ("Who owns the code?", "You do. On full payment, the intellectual property in the bespoke work we create for you is transferred to you, as set out in your contract.")]
    body = page_hero(b, "Our Services", "Six Services. One Trusted Technology Partner.", "From strategy to software, cloud and AI, everything you need to build, modernise and scale.", "Services", "nx-dashboard") + f'''
<div class="subnav" data-subnav><div class="container"><nav aria-label="Services">{tabs}</nav></div></div>
<section class="sec sec-dark services-ov"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container">
  {head_block("What We Do", "End-to-End Digital Solutions", "Choose a service to explore its offerings, benefits and the technologies we use.", True)}
  <div class="svc-grid three">{"".join(svc_card(b, s, i).replace('href="services.html#', 'href="#') for i, s in enumerate(SERVICES))}</div>
</div></section>
<div class="container svc-details">{"".join(blocks)}</div>
{showcase_band(b, "nx-cube", "One Partner", "Every Layer of Your Technology, <span class='grad'>Connected.</span>", "Strategy, software, cloud and AI delivered by one team, so nothing gets lost between suppliers.", [("chart", "Strategy &amp; roadmaps"), ("code", "Engineering"), ("cloud", "Cloud &amp; DevOps"), ("cpu", "AI &amp; automation")], btn("contact.html?type=consultation#enquiry", "Book a Consultation", "white"))}
<section class="sec sec-light"><div class="container two-col faq-wrap">
  <div>{eyebrow("FAQs")}<h2 class="sec-title" data-split>Questions About Working With Us</h2><p class="sec-sub" data-reveal>Can&#8217;t find what you&#8217;re looking for? <a href="contact.html">Get in touch</a>.</p></div>
  <div class="faqs">{faq(faqs)}</div>
</div></section>''' + cta_band(b, "Ready to Start?", "Let&#8217;s Discuss Your Project.", "Share your idea and we will recommend the right service mix.", "Discuss Your Project")
    return page("services.html", "Services", "Custom software development, web and app development, cloud computing, IT consulting, digital transformation and AI automation services from NexTech Digital, London.", body, "services.html", og_img="nx-dashboard")


# ================================================================ INDUSTRIES
def industries():
    b = ""
    cards = "".join(f'''<a class="ind-card" href="#{x["id"]}" data-reveal style="--d:{(i % 4) * .07:.2f}s">{img(b, x["img"], "")}<div class="ic-ov"><span class="ind-ic">{icon(x["icon"])}</span><h3>{x["name"]}</h3><p>{x["intro"]}</p><span class="more">Explore {icon("arrow")}</span></div></a>''' for i, x in enumerate(INDUSTRIES))
    rows = "".join(f'''<article class="ind-row" id="{x["id"]}">
  <div class="ir-media" data-reveal="zoom"><div class="img-frame">{img(b, x["img"], x["name"])}</div><span class="ind-ic big">{icon(x["icon"])}</span></div>
  <div class="ir-copy"><p class="eyebrow" data-reveal>Industry 0{i + 1}</p><h2 class="sec-title sm" data-split>{x["name"]}</h2><p data-reveal>{x["intro"]}</p>
    <div class="cs-cols">
      <div class="cs ch" data-reveal><h3>{icon("zap")}Common challenges</h3><ul>{"".join(f"<li>{c}</li>" for c in x["challenges"])}</ul></div>
      <div class="cs so" data-reveal style="--d:.1s"><h3>{icon("check")}NexTech solutions</h3><ul>{"".join(f"<li>{c}</li>" for c in x["solutions"])}</ul></div>
    </div>
    <a class="link-arrow" href="contact.html?type=consultation&amp;industry={x["id"]}#enquiry" data-reveal>Book a {x["name"]} consultation {icon("arrow")}</a>
  </div></article>''' for i, x in enumerate(INDUSTRIES))
    body = page_hero(b, "Industries We Serve", "Technology Built for Your Industry", "We combine technical expertise with an understanding of each sector&#8217;s challenges, regulations and customers.", "Industries", "cyber") + f'''
<section class="sec"><div class="container">
  {head_block("Sectors", "Seven Industries, One Focus: Results", "Select an industry to see the challenges we help solve.", True)}
  <div class="ind-cards">{cards}<div class="ind-card ind-cta" data-reveal><div><span class="ind-ic">{icon("sparkle")}</span><h3>Don&#8217;t see your industry?</h3><p>Our approach works across sectors. Let&#8217;s talk about your challenge.</p>{btn("contact.html?type=consultation#enquiry", "Talk to Us", "white")}</div></div></div>
</div></section>
{showcase_band(b, "nx-team", "Sector Expertise", "Industry Knowledge Meets <span class='grad'>Engineering Depth.</span>", "Our teams pair domain understanding with modern engineering, so solutions fit your regulations, customers and day-to-day operations.", [("shield", "Compliance-aware delivery"), ("users", "Domain-focused teams"), ("layers", "Integrates with your systems"), ("trend", "Measurable outcomes")], btn("contact.html?type=consultation#enquiry", "Book a Consultation", "white"))}
<section class="sec sec-light"><div class="container ind-rows">{rows}</div></section>''' + cta_band(b, "Industry Challenge?", "Book a Free Consultation.", "Speak with our team about the technology challenges in your sector.", "Book a Consultation", "contact.html?type=consultation#enquiry")
    return page("industries.html", "Industries We Serve", "NexTech Digital delivers technology solutions for technology & IT, financial services, healthcare, retail & e-commerce, education, manufacturing and logistics.", body, "industries.html", og_img="cyber")


# ================================================================ WORK
def work():
    b = ""
    filt = '<button type="button" class="chip-btn on" data-filter="all" aria-pressed="true">All Projects</button>' + "".join(f'<button type="button" class="chip-btn" data-filter="{c}" aria-pressed="false">{c}</button>' for c in PROJECT_CATS)
    cards = "".join(project_card(b, p, i, True) for i, p in enumerate(PROJECTS))
    dlgs = []
    for p in PROJECTS:
        dlgs.append(f'''<dialog class="case" id="dlg-{p["id"]}" aria-labelledby="t-{p["id"]}">
  <div class="case-in" id="{p["id"]}">
    <button class="case-x" type="button" data-close aria-label="Close">{icon("close")}</button>
    <div class="case-media">{img(b, p["img"], p["title"])}<span class="tag">{p["tag"]}</span></div>
    <div class="case-body">
      <p class="ill">Illustrative project &middot; concept demonstration, not a real client engagement</p>
      <h2 id="t-{p["id"]}">{p["title"]}</h2><p class="case-lead">{p["summary"]} <span class="muted">Sector: {p["industry"]}.</span></p>
      <div class="case-grid">
        <div><h3>{icon("target")}Objectives</h3><ul>{"".join(f"<li>{o}</li>" for o in p["objectives"])}</ul></div>
        <div><h3>{icon("zap")}The challenge</h3><p>{p["challenge"]}</p></div>
        <div><h3>{icon("bulb")}Our solution</h3><p>{p["solution"]}</p></div>
        <div><h3>{icon("trend")}Intended outcomes</h3><ul>{"".join(f"<li>{o}</li>" for o in p["outcomes"])}</ul></div>
      </div>
      <div class="pills"><b>Technologies used:</b>{"".join(f"<span>{t}</span>" for t in p["tech"])}</div>
      <div class="learn"><h3>Key learning</h3><p>{p["learnings"]}</p></div>
      {btn("contact.html?type=project#enquiry", "Start a Similar Project")}
    </div>
  </div>
</dialog>''')
    body = page_hero(b, "Our Work", "Real Solutions. Tangible Impact.", "Explore illustrative projects that show how we approach software, mobile, cloud and AI challenges.", "Our Work", "nx-dashboard") + f'''
<section class="sec"><div class="container">
  <div class="notice" data-reveal>{icon("bulb")}<p>The projects below are <strong>illustrative concept demonstrations</strong> of our capabilities. They do not represent real clients or real results. Real case studies will be published here with client permission.</p></div>
  <div class="filters" role="group" aria-label="Filter projects by category" data-filters="proj">{filt}</div>
  <div class="proj-grid three" data-filter-grid="proj">{cards}</div>
  <p class="empty" hidden data-empty="proj">No projects in this category yet.</p>
</div></section>
{"".join(dlgs)}
<section class="sec sec-dark"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container">
  {head_block("How We Deliver", "Every Project Follows a Proven Path", "", True)}
  <ol class="process light" data-process>{"".join(f'<li data-reveal style="--d:{i * .1:.2f}s"><span class="p-ic">{icon(ic)}<em>{i + 1:02d}</em></span><h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate([("search", "Discover", "Goals, users and constraints."), ("clipboard", "Plan", "Scope, roadmap and architecture."), ("code", "Develop", "Agile sprints with demos."), ("rocket", "Launch", "Tested, monitored release."), ("headset", "Support", "Continuous improvement.")]))}<span class="p-line" aria-hidden="true"><i></i></span></ol>
</div></section>''' + cta_band(b, "Your Project Could Be Next.", "Start Your Project Today.", "Tell us about your idea and we will help you shape it.", "Start Your Project")
    return page("work.html", "Our Work & Portfolio", "Explore illustrative NexTech Digital projects across web development, custom software, mobile apps, cloud and AI, with objectives, solutions and technologies used.", body, "work.html", og_img="nx-dashboard")


# ================================================================ TECHNOLOGY
def technology():
    b = ""
    slug = lambda c: c.lower().replace(" & ", "-").replace(" ", "-")
    cats = []
    total = 0
    for ci, (cat, ic, items) in enumerate(TECH):
        total += len(items)
        cards = "".join(f'<li class="tech" data-reveal data-glow style="--d:{j * .05:.2f}s"><span class="tech-logo"><img src="assets/logos/{f}.svg" alt="" loading="lazy" width="44" height="44"></span><div><h4>{n}</h4><p>{d}</p></div></li>' for j, (n, f, d) in enumerate(items))
        dark = " dark" if ci % 2 else ""
        net = '<canvas class="net net-dim" aria-hidden="true"></canvas>' if dark else ""
        cats.append(f'<section class="tech-cat{dark}" id="{slug(cat)}" data-reveal>{net}<div class="tc-head"><span class="svc-ic">{icon(ic)}</span><div><p class="tc-num">0{ci + 1}</p><h2>{cat}</h2></div><span class="tc-count">{len(items)} technologies</span></div><ul class="tech-grid">{cards}</ul></section>')
    tabs = "".join(f'<a href="#{slug(c)}" data-spy="{slug(c)}">{icon(ic)}<span>{c}</span></a>' for c, ic, _ in TECH)
    inner = ["react", "nextjs", "nodejs", "python", "typescript"]
    outer = ["amazonwebservices", "azure", "docker", "kubernetes", "postgresql", "mongodb", "flutter", "tensorflow"]
    orb = lambda lst, ring: "".join(f'<span class="orb" style="--a:{i * 360 / len(lst):.0f}deg"><img src="assets/logos/{f}.svg" alt="" width="34" height="34"></span>' for i, f in enumerate(lst))
    princ = [("shield", "Proven & supported", "Mature technologies with strong communities and long-term support."), ("trend", "Scalable", "Choices that grow from first users to enterprise scale."),
             ("users", "Maintainable", "Tools your team can hire for, understand and own."), ("lock", "Secure", "Security patches, good defaults and compliance-ready platforms.")]
    body = page_hero(b, "Technology Stack", "Modern Tools. Reliable Foundations.", "The frameworks, platforms and tools we use to build fast, secure and scalable digital products.", "Technology Stack", "nx-cloud") + f'''
<section class="sec tech-intro"><div class="container two-col">
  <div>{eyebrow("Our Ecosystem")}<h2 class="sec-title" data-split>A Modern Stack for Every Layer of Your Product</h2>
    <p data-reveal>From interfaces people love to cloud platforms that scale and AI that automates, we choose proven tools that fit your goals, your team and your budget.</p>
    <ul class="tech-stats" data-reveal style="--d:.1s"><li><b><span data-count="{len(TECH)}">{len(TECH)}</span></b><small>Categories</small></li><li><b><span data-count="{total}">{total}</span>+</b><small>Technologies</small></li><li><b>3</b><small>Major clouds</small></li></ul>
    <div class="notice" data-reveal style="--d:.2s">{icon("bulb")}<p>These are <strong>proposed examples</strong> of the technologies we work with. We recommend the right tools for each project.</p></div>
  </div>
  <div class="orbit" data-reveal="zoom" aria-hidden="true">
    <div class="orbit-glow"></div>
    <div class="ring r2">{orb(outer, 2)}</div><div class="ring r1">{orb(inner, 1)}</div>
    <div class="orbit-core"><img src="assets/img/nx-cube.jpg" alt="" width="1672" height="941"></div>
  </div>
</div></section>
<div class="subnav" data-subnav><div class="container"><nav aria-label="Technology categories">{tabs}</nav></div></div>
<section class="sec tech-cats"><div class="container">{"".join(cats)}</div></section>
{showcase_band(b, "nx-dashboard", "Engineering Excellence", "Modern Stacks. <span class='grad'>Measurable Results.</span>", "We combine proven frameworks with automated testing, CI/CD and observability so your product is fast to build and easy to run.", [("code", "Clean, tested code"), ("zap", "Automated pipelines"), ("shield", "Secure by default"), ("trend", "Built to scale")], btn("contact.html?type=project#enquiry", "Start a Project", "white"))}
<section class="sec sec-light"><div class="container">
  {head_block("How We Choose", "Technology Decisions That Serve Your Business", "", True)}
  <div class="values four">{"".join(f'<article class="value" data-reveal data-glow style="--d:{i * .07:.2f}s"><span class="v-num">0{i + 1}</span><span class="svc-ic">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(princ))}</div>
</div></section>''' + cta_band(b, "Not Sure Which Stack?", "We&#8217;ll Help You Decide.", "Get independent advice on the right technology for your product.", "Talk to an Expert")
    return page("technology.html", "Technology Stack", "The technologies NexTech Digital uses: React, Next.js, Node.js, Python, Java, React Native, Flutter, PostgreSQL, MongoDB, AWS, Azure, Docker and AI frameworks.", body, "technology.html", og_img="nx-cloud")


# ================================================================ INSIGHTS
def insights():
    b = ""
    f = ARTICLES[0]
    filt = '<button type="button" class="chip-btn on" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" class="chip-btn" data-filter="{c}" aria-pressed="false">{c}</button>' for c in INSIGHT_CATS)
    body = page_hero(b, "Insights &amp; Ideas", "Technology Insights From Our Experts", "Practical guides, trends and ideas on software, cloud, AI and digital transformation.", "Insights", "laptop-desk") + f'''
<section class="sec"><div class="container">
  <a class="feat-art" href="insights/{f["slug"]}.html" data-reveal="zoom">
    <div class="fa-media">{img(b, f["img"], f["title"])}</div>
    <div class="fa-body"><span class="tag">Featured &middot; {f["cat"]}</span><h2>{f["title"]}</h2><p>{f["summary"]}</p>
      <div class="meta"><span>{icon("calendar")}<time datetime="{f["date"]}">{f["date_h"]}</time></span><span>{icon("clock")}{f["read"]} min read</span></div><span class="link-arrow">Read article {icon("arrow")}</span></div>
  </a>
  <div class="sec-row mt">{head_block("Latest Articles", "Browse by Topic")}</div>
  <div class="filters" role="group" aria-label="Filter articles by category" data-filters="art">{filt}</div>
  <div class="art-grid three" data-filter-grid="art">{"".join(article_card(b, a, i) for i, a in enumerate(ARTICLES))}</div>
  <p class="empty" hidden data-empty="art">New articles in this category are coming soon.</p>
</div></section>
<section class="sec sec-light"><div class="container"><div class="nl-band" data-reveal="zoom">
  <div><span class="svc-ic">{icon("mail")}</span><h2>Get Insights in Your Inbox</h2><p>Monthly technology insights, practical guides and company news. No spam, unsubscribe anytime.</p></div>
  {newsletter_form("nl-big", "Email address")}
</div></div></section>'''
    return page("insights.html", "Insights & Blog", "Technology insights from NexTech Digital on software development, AI & automation, cloud computing, digital transformation and technology trends.", body, "insights.html", og_img="laptop-desk")


def article(a):
    b = "../"
    rel = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    url = SITE["domain"] + "/insights/" + a["slug"] + ".html"
    schema = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "datePublished": a["date"], "description": a["summary"],
              "image": SITE["domain"] + "/assets/img/" + a["img"] + ".webp", "author": {"@type": "Organization", "name": "NexTech Digital"}, "publisher": {"@type": "Organization", "name": "NexTech Digital"}, "mainEntityOfPage": url}
    body = f'''<section class="phero art-hero">
  <div class="phero-bg" data-parallax=".25">{img(b, a["img"], "", "", True)}</div>
  <canvas class="net" aria-hidden="true"></canvas><div class="phero-grid" aria-hidden="true"></div>
  <div class="container phero-in narrow">
    <nav class="crumb" aria-label="Breadcrumb"><a href="../index.html">Home</a>{icon("chev")}<a href="../insights.html">Insights</a>{icon("chev")}<span aria-current="page">{a["cat"]}</span></nav>
    <p class="pill" data-reveal>{a["cat"]}</p><h1 data-split>{a["title"]}</h1>
    <div class="meta light" data-reveal style="--d:.2s"><span>{icon("users")}NexTech Digital Team</span><span>{icon("calendar")}<time datetime="{a["date"]}">{a["date_h"]}</time></span><span>{icon("clock")}{a["read"]} min read</span></div>
  </div><div class="blend" aria-hidden="true"></div>
</section>
<article class="sec"><div class="container art-layout">
  <div class="art-cover" data-reveal="zoom">{img(b, a["img"], a["title"])}</div>
  <div class="prose" data-reveal>{a["body"]}</div>
  <aside class="art-side">
    <div class="side-card"><h3>Share this article</h3><div class="share">
      <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" aria-label="Share on LinkedIn">{icon("linkedin")}</a>
      <a href="https://twitter.com/intent/tweet?url={url}" target="_blank" rel="noopener" aria-label="Share on X">{icon("x")}</a>
      <a href="mailto:?subject={esc(a["title"])}&amp;body={url}" aria-label="Share by email">{icon("mail")}</a>
      <button type="button" data-copy="{url}" aria-label="Copy link">{icon("share")}</button></div></div>
    <div class="side-card dark"><h3>Need expert advice?</h3><p>Talk to our team about your project.</p>{btn("../contact.html?type=consultation#enquiry", "Book a Consultation", "white")}</div>
    <div class="side-card"><h3>Newsletter</h3><p>Monthly insights to your inbox.</p>{newsletter_form("nl-side", "Email address")}</div>
  </aside>
</div></article>
<section class="sec sec-light"><div class="container">
  <div class="sec-row">{head_block("Keep Reading", "Related Insights")}<div data-reveal>{btn("../insights.html", "All Insights", "soft")}</div></div>
  <div class="art-grid three">{"".join(article_card(b, x, i) for i, x in enumerate(rel))}</div>
</div></section>''' + cta_band(b)
    return page(f"insights/{a['slug']}.html", a["title"], a["summary"], body, "insights.html", b, schema, a["img"])


# ================================================================ CAREERS
def careers():
    b = ""
    why = [("trend", "Grow your career", "Learning time, mentoring and exposure to a wide range of technologies and industries."), ("sparkle", "Meaningful work", "Build products that solve real problems for real businesses."),
           ("users", "Collaborative team", "Work alongside supportive engineers, designers and strategists."), ("cpu", "Modern technology", "Cloud-native, AI and modern frameworks, not legacy maintenance only."),
           ("clock", "Flexible working", "Flexible and hybrid arrangements around our London base."), ("heart", "Inclusive culture", "We welcome people from every background and value different perspectives.")]
    areas = [("Development", "code", "Software Engineering", "Frontend, backend, mobile and cloud engineers who enjoy building quality software."),
             ("Development", "cpu", "AI & Data", "Data engineers and machine-learning practitioners working on practical AI solutions."),
             ("Design", "palette", "Product & UX Design", "Designers who combine research, interaction design and visual craft."),
             ("Marketing", "megaphone", "Digital Marketing", "Content, SEO and growth specialists who can explain technology clearly."),
             ("Management", "briefcase", "Project & Delivery Management", "Delivery leads who keep projects organised, transparent and on track."),
             ("Management", "chart", "Business & Consulting", "Analysts and consultants who connect technology with business outcomes.")]
    filt = '<button type="button" class="chip-btn on" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" class="chip-btn" data-filter="{c}" aria-pressed="false">{c}</button>' for c in ["Development", "Design", "Marketing", "Management"])
    area_cards = "".join(f'<article class="job" data-cat="{c}" data-reveal style="--d:{(i % 3) * .07:.2f}s"><div class="job-top"><span class="svc-ic">{icon(ic)}</span><span class="job-cat">{c}</span></div><h3>{t}</h3><p>{d}</p><div class="job-meta"><span>{icon("pin")}London / Hybrid</span><span>{icon("briefcase")}Talent pool</span></div><a class="link-arrow" href="#apply" data-area="{t}">Register interest {icon("arrow")}</a></article>' for i, (c, ic, t, d) in enumerate(areas))
    opts = "".join(f'<option>{t}</option>' for _, _, t, _ in areas)
    body = page_hero(b, "Careers at NexTech", "Build Your Future With NexTech", "Join a team that designs, builds and scales technology for businesses around the world.", "Careers", "nx-team", f'<div class="btn-row" data-reveal style="--d:.3s">{btn("#openings", "Explore Opportunities")}</div>') + f'''
<section class="sec"><div class="container two-col">
  <div>{eyebrow("Life at NexTech")}<h2 class="sec-title" data-split>A Culture Built on Curiosity and Collaboration</h2>
    <p data-reveal>We are a team of builders who love learning. We share knowledge openly, review each other&#8217;s work with kindness and celebrate wins together. Every voice matters, and great ideas can come from anyone.</p>
    <ul class="ticks" data-reveal><li>{icon("check")}Small, empowered project teams</li><li>{icon("check")}Regular knowledge-sharing sessions</li><li>{icon("check")}A modern London workspace</li></ul></div>
  <div class="mosaic" data-reveal="zoom">
    <div class="img-frame m1" data-parallax="-.05">{img(b, "nx-team", "NexTech team collaborating")}</div>
    <div class="img-frame m2" data-parallax=".06">{img(b, "developers", "Developers collaborating")}</div>
    <div class="img-frame m3" data-parallax="-.03">{img(b, "office-bright", "Bright office space")}</div>
  </div>
</div></section>
<section class="sec sec-dark"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container">
  {head_block("Why Work With Us", "More Than a Job", "", True)}
  <div class="exp-grid">{"".join(f'<article class="exp" data-reveal data-glow style="--d:{i * .06:.2f}s">{icon(ic)}<h3>{t}</h3><p>{d}</p></article>' for i, (ic, t, d) in enumerate(why))}</div>
  {flag("Confirm working arrangements and any benefits before publishing. Only list benefits the company actually offers.")}
</div></section>
<section class="sec" id="openings"><div class="container">
  {head_block("Current Openings", "Opportunities at NexTech", "", True)}
  <div class="no-roles" data-reveal>{icon("briefcase")}<div><h3>No live vacancies right now</h3><p>We only advertise genuine vacancies. You can still register your interest in the areas below and we will contact you when a suitable role opens.</p></div></div>
  <div class="filters" role="group" aria-label="Filter by job category" data-filters="job">{filt}</div>
  <div class="jobs" data-filter-grid="job">{area_cards}</div>
</div></section>
<section class="sec sec-light" id="apply"><div class="container two-col form-wrap">
  <div>{eyebrow("Apply")}<h2 class="sec-title" data-split>Send Us Your Application</h2><p class="sec-sub" data-reveal>Tell us about yourself and upload your CV. We review every application and will respond if there is a suitable match.</p>
    <ul class="ticks" data-reveal><li>{icon("check")}CV in PDF, DOC or DOCX, up to 5&nbsp;MB</li><li>{icon("check")}Your data is handled under our <a href="privacy-policy.html">Privacy Policy</a></li></ul>
    <h3 class="mini-h" data-reveal>What happens next</h3>
    <ol class="hire-steps">{"".join(f'<li data-reveal style="--d:{i * .08:.2f}s"><span>{icon(ic)}</span><div><h4>{t}</h4><p>{d}</p></div></li>' for i, (ic, t, d) in enumerate([("send", "Apply", "Send your details and CV using the form."), ("search", "Review", "Our team reviews every application carefully."), ("users", "Conversation", "If there is a match, we invite you for a friendly chat."), ("handshake", "Welcome aboard", "Receive an offer and start building with us.")]))}</ol>
    <div data-reveal="wipe"><div class="img-frame apply-img">{img(b, "nx-team", "NexTech team at work")}</div></div></div>
  <form class="form card" data-form="careers" novalidate>
    <div class="f-row"><div class="field"><label for="c-name">Full name *</label><input id="c-name" name="name" required autocomplete="name"></div>
    <div class="field"><label for="c-email">Email *</label><input id="c-email" name="email" type="email" required autocomplete="email"></div></div>
    <div class="f-row"><div class="field"><label for="c-phone">Phone</label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
    <div class="field"><label for="c-area">Area of interest *</label><select id="c-area" name="area" required><option value="">Select an area</option>{opts}<option>Other</option></select></div></div>
    <div class="field"><label for="c-link">LinkedIn or portfolio URL</label><input id="c-link" name="link" type="url" placeholder="https://"></div>
    <div class="field"><span class="lbl">CV / resume *</span><label class="file" for="c-cv">{icon("upload")}<span data-file-label>Click to upload or drag your file here</span><small>PDF, DOC or DOCX &middot; max 5 MB</small><input id="c-cv" name="cv" type="file" accept=".pdf,.doc,.docx" required data-max="5"></label></div>
    <div class="field"><label for="c-msg">Tell us about yourself *</label><textarea id="c-msg" name="message" rows="4" required minlength="20"></textarea></div>
    <label class="check"><input type="checkbox" name="consent" required><span>I agree to NexTech Digital processing my data for recruitment purposes, as described in the <a href="privacy-policy.html">Privacy Policy</a>. *</span></label>
    <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="btn btn-primary" type="submit"><span>Submit Application</span><span class="btn-ic">{icon("send")}</span></button>
    <p class="form-msg" role="status" aria-live="polite"></p>
  </form>
</div></section>''' + cta_band(b, "Ready for Your Next Challenge?", "Explore Opportunities.", "Register your interest and grow your career with NexTech Digital.", "Explore Opportunities", "careers.html#openings")
    return page("careers.html", "Careers", "Build your future with NexTech Digital. Discover our culture, why to work with us, current opportunities and how to apply.", body, "careers.html", og_img="nx-team")


# ================================================================ CONTACT
def contact():
    b = ""
    svc = "".join(f'<option value="{s["id"]}">{s["name"]}</option>' for s in SERVICES)
    info = [("pin", "Headquarters", SITE["city"], None), ("mail", "Email us", SITE["email"], "mailto:" + SITE["email"]), ("phone", "Call us", SITE["phone"], "tel:" + SITE["phone_href"]), ("clock", "Business hours", "Mon &ndash; Fri, 9:00 &ndash; 17:30 (UK)", None)]
    faqs = [("How quickly will you respond?", "We aim to reply to every enquiry within one business day."), ("Do you sign NDAs?", "Yes. We are happy to sign a non-disclosure agreement before you share sensitive details."),
            ("Do you work with clients outside the UK?", "Yes. We are based in London and work with clients internationally, collaborating remotely and across time zones."),
            ("What should I include in my enquiry?", "A short description of your goals, any existing systems, your ideal timeline and, if known, a budget range. Do not worry if you do not have everything yet."),
            ("Is the consultation free?", "Yes. The initial consultation is a free, no-obligation conversation about your needs.")]
    body = page_hero(b, "Contact Us", "Let&#8217;s Build Something Great Together", "Tell us about your project and our team will get back to you within one business day.", "Contact", "office-bright") + f'''
<section class="sec contact-sec"><div class="container">
  <div class="info-cards">{"".join(f'<div class="info" data-reveal data-glow style="--d:{i * .07:.2f}s"><span class="svc-ic">{icon(ic)}</span><div><h3>{t}</h3>{f"<a href={chr(34)}{h}{chr(34)}>{v}</a>" if h else f"<p>{v}</p>"}</div></div>' for i, (ic, t, v, h) in enumerate(info))}</div>
  <div class="contact-grid" id="enquiry">
    <form class="form card" data-form="enquiry" novalidate>
      <h2>Project Enquiry</h2><p class="muted">Fields marked * are required.</p>
      <div class="f-row"><div class="field"><label for="e-name">Full name *</label><input id="e-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="e-email">Business email *</label><input id="e-email" name="email" type="email" required autocomplete="email"></div></div>
      <div class="f-row"><div class="field"><label for="e-company">Company name *</label><input id="e-company" name="company" required autocomplete="organization"></div>
      <div class="field"><label for="e-phone">Phone number</label><input id="e-phone" name="phone" type="tel" autocomplete="tel"></div></div>
      <div class="f-row"><div class="field"><label for="e-service">Service required *</label><select id="e-service" name="service" required><option value="">Select a service</option>{svc}<option value="consultation">General consultation</option><option value="other">Other / not sure</option></select></div>
      <div class="field"><label for="e-budget">Project budget (optional)</label><select id="e-budget" name="budget"><option value="">Prefer not to say</option><option>Under &pound;10,000</option><option>&pound;10,000 &ndash; &pound;25,000</option><option>&pound;25,000 &ndash; &pound;50,000</option><option>&pound;50,000 &ndash; &pound;100,000</option><option>&pound;100,000+</option></select></div></div>
      <div class="field"><label for="e-msg">Project description *</label><textarea id="e-msg" name="message" rows="5" required minlength="20" placeholder="Tell us about your goals, timeline and any existing systems."></textarea></div>
      <label class="check"><input type="checkbox" name="consent" required><span>I agree to NexTech Digital using my details to respond to this enquiry, as described in the <a href="privacy-policy.html">Privacy Policy</a>. *</span></label>
      <input type="hidden" name="type" value="project"><input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary" type="submit"><span>Send Enquiry</span><span class="btn-ic">{icon("send")}</span></button>
      <p class="form-msg" role="status" aria-live="polite"></p>
    </form>
    <aside class="contact-side">
      <div class="side-card dark consult" data-reveal="left"><canvas class="net net-dim" aria-hidden="true"></canvas><span class="svc-ic">{icon("calendar")}</span><h3>Book a Free Consultation</h3><p>A 30-minute call with our team to discuss your goals and the best way forward.</p><button class="btn btn-white" type="button" data-consult><span>Book a Consultation</span><span class="btn-ic">{icon("arrow")}</span></button></div>
      <a class="side-card wa-card" href="#" data-wa data-reveal="left" style="--d:.1s"><span class="wa-ic">{icon("whatsapp")}</span><div><h3>Chat on WhatsApp</h3><p>Quick question? Message us directly.</p></div>{icon("arrow")}</a>
      <div class="map" data-reveal="left" style="--d:.2s">
        <div class="map-art" aria-hidden="true"><svg viewBox="0 0 400 240"><defs><pattern id="mg" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0v20" fill="none" stroke="#C9D5F2" stroke-width=".6"/></pattern></defs><rect width="400" height="240" fill="url(#mg)"/><path d="M-10 150c60-30 90 20 150-10s70-70 130-50 80 40 140 20" fill="none" stroke="#9DB8FF" stroke-width="14" opacity=".45"/><path d="M40 0l60 240M0 70h400M250 0l-40 240M330 0v240" stroke="#DCE4F6" stroke-width="6"/></svg><span class="map-pin">{icon("pin")}</span></div>
        <div class="map-txt"><h3>London, United Kingdom</h3><p>Full office address and interactive map will be added once the address is confirmed.</p><a class="link-arrow" href="https://www.google.com/maps/search/?api=1&amp;query=London%2C+United+Kingdom" target="_blank" rel="noopener">Open in Google Maps {icon("arrow-ur")}</a></div>
      </div>
    </aside>
  </div>
</div></section>
<section class="sec sec-light"><div class="container two-col faq-wrap">
  <div>{eyebrow("FAQs")}<h2 class="sec-title" data-split>Frequently Asked Questions</h2><p class="sec-sub" data-reveal>Quick answers to common questions about getting started.</p></div>
  <div class="faqs">{faq(faqs)}</div>
</div></section>'''
    return page("contact.html", "Contact Us", "Contact NexTech Digital in London. Send a project enquiry, book a free consultation or chat with us on WhatsApp.", body, "contact.html", og_img="office-bright")


# ================================================================ LEGAL
def legal(path, title, desc, sections, flags, extra=""):
    b = ""
    toc = "".join(f'<a href="#s{i}">{h}</a>' for i, (h, _) in enumerate(sections))
    secs = "".join(f'<section id="s{i}"><h2>{i + 1}. {h}</h2>{c}</section>' for i, (h, c) in enumerate(sections))
    body = page_hero(b, "Legal", title, f"Last updated: 19 November 2026", title, "office") + f'''
<section class="sec"><div class="container legal">
  <aside class="legal-toc"><h3>On this page</h3>{toc}</aside>
  <div class="prose">{flag(flags)}{extra}{secs}</div>
</div></section>'''
    return page(path, title, desc, body, "")


CONTROLLER = f"NexTech Digital (&ldquo;we&rdquo;, &ldquo;us&rdquo;), {SITE['city']}. [Registered company name, company number and registered office address to be confirmed.]"


def privacy():
    s = [("Who we are", f"<p>{CONTROLLER} We are the data controller for personal data collected through this website. Contact: <a href='mailto:{SITE['email']}'>{SITE['email']}</a>.</p>"),
         ("Data we collect", "<ul><li><strong>Enquiry data:</strong> name, business email, company, phone, service of interest, budget range and project description you submit.</li><li><strong>Recruitment data:</strong> details and CV you submit through the careers form.</li><li><strong>Newsletter data:</strong> your email address.</li><li><strong>Technical data:</strong> with your consent, analytics data such as pages visited and device type.</li></ul>"),
         ("How and why we use it", "<ul><li>To respond to enquiries and provide services (legitimate interests / steps prior to a contract).</li><li>To assess job applications (legitimate interests).</li><li>To send newsletters (consent; you can unsubscribe at any time).</li><li>To improve our website (consent, for analytics cookies).</li></ul>"),
         ("Sharing your data", "<p>We share data only with service providers that help us run our business, such as hosting, email and form-handling providers, under appropriate contracts. We do not sell personal data. [List of processors to be confirmed.]</p>"),
         ("International transfers", "<p>Where data is transferred outside the UK, we use appropriate safeguards such as UK adequacy regulations or the International Data Transfer Agreement.</p>"),
         ("How long we keep it", "<p>Enquiry data: up to 2 years after our last contact. Recruitment data: up to 12 months after the process ends, unless you agree to longer. Newsletter data: until you unsubscribe. [Retention periods to be confirmed.]</p>"),
         ("Your rights", "<p>Under UK GDPR you have rights to access, rectify, erase, restrict and object to processing, to data portability, and to withdraw consent at any time. Contact us to exercise them. You can also complain to the Information Commissioner&rsquo;s Office (ico.org.uk).</p>"),
         ("Security", "<p>We use appropriate technical and organisational measures to protect personal data, including encryption in transit and access controls.</p>"),
         ("Changes", "<p>We may update this policy. The date at the top shows when it was last revised.</p>")]
    return legal("privacy-policy.html", "Privacy Policy", "How NexTech Digital collects, uses and protects personal data under UK GDPR.", s, "registered company details, ICO registration number, processors (hosting, forms, email, analytics), retention periods and international transfers must be confirmed and reviewed by a qualified adviser.")


def terms():
    s = [("About these terms", f"<p>These terms govern your use of this website, operated by {CONTROLLER}</p>"),
         ("Use of the website", "<p>You may use this website for lawful purposes only. You must not attempt to gain unauthorised access, introduce malicious code or disrupt the website.</p>"),
         ("Intellectual property", "<p>Content on this website, including text, graphics and logos, is owned by or licensed to NexTech Digital. Photographs are used under the Unsplash licence. Technology logos are trademarks of their respective owners.</p>"),
         ("Information on this site", "<p>Content is provided for general information only. Projects shown on our website are illustrative unless stated otherwise. See our <a href='disclaimer.html'>Website Disclaimer</a>.</p>"),
         ("Services", "<p>Any services we provide are governed by a separate written agreement. Nothing on this website forms a contract.</p>"),
         ("Links to other sites", "<p>We are not responsible for the content of external websites linked from this site.</p>"),
         ("Limitation of liability", "<p>To the extent permitted by law, we are not liable for any loss arising from use of this website. Nothing limits liability that cannot be limited under English law.</p>"),
         ("Governing law", "<p>These terms are governed by the laws of England and Wales, and the courts of England and Wales have exclusive jurisdiction.</p>")]
    return legal("terms.html", "Terms & Conditions", "Terms and conditions for using the NexTech Digital website.", s, "company legal entity details and liability wording should be reviewed by a qualified legal adviser.")


def cookie_policy():
    s = [("What are cookies?", "<p>Cookies are small files stored on your device that help websites work and provide information to site owners. We also use similar technologies such as local storage.</p>"),
         ("Cookies we use", "<table><thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead><tbody><tr><td>nt_consent</td><td>Strictly necessary (local storage)</td><td>Remembers your cookie choices</td><td>12 months</td></tr><tr><td>_ga, _ga_*</td><td>Analytics (optional)</td><td>Google Analytics, only if you consent and analytics is enabled</td><td>Up to 2 years</td></tr></tbody></table>"),
         ("Managing your choices", "<p>You can change your choices at any time on our <a href='cookie-preferences.html'>Cookie Preferences</a> page, or through your browser settings.</p>"),
         ("Third-party content", "<p>Fonts are loaded from Google Fonts. Opening WhatsApp, Google Maps or social links takes you to third-party services with their own policies.</p>"),
         ("Contact", f"<p>Questions? Email <a href='mailto:{SITE['email']}'>{SITE['email']}</a>.</p>")]
    return legal("cookie-policy.html", "Cookie Policy", "Information about the cookies used on the NexTech Digital website and how to manage them.", s, "confirm the final list of cookies once analytics and any third-party tools are configured.")


def cookie_prefs():
    b = ""
    body = page_hero(b, "Legal", "Cookie Preferences", "Choose which optional cookies you allow. You can change this at any time.", "Cookie Preferences", "office") + f'''
<section class="sec"><div class="container narrow-c">
  <form class="prefs card" data-prefs>
    <div class="pref"><div><h2>Strictly necessary</h2><p>Required for the website to function, such as remembering your cookie choices. These cannot be switched off.</p></div><label class="switch"><input type="checkbox" checked disabled><span></span><b class="sr-only">Always on</b></label></div>
    <div class="pref"><div><h2>Analytics</h2><p>Helps us understand how visitors use the site so we can improve it. Only loaded if you allow it.</p></div><label class="switch"><input type="checkbox" name="analytics"><span></span><b class="sr-only">Allow analytics cookies</b></label></div>
    <div class="pref"><div><h2>Marketing</h2><p>Used to measure campaigns. We do not currently use marketing cookies; this setting is kept for future use.</p></div><label class="switch"><input type="checkbox" name="marketing"><span></span><b class="sr-only">Allow marketing cookies</b></label></div>
    <div class="btn-row"><button class="btn btn-primary" type="submit"><span>Save Preferences</span></button><button class="btn btn-soft" type="button" data-consent="accept"><span>Accept All</span></button><button class="btn btn-soft" type="button" data-consent="reject"><span>Reject Optional</span></button></div>
    <p class="form-msg" role="status" aria-live="polite"></p>
  </form>
  <p class="muted center">Read more in our <a href="cookie-policy.html">Cookie Policy</a>.</p>
</div></section>'''
    return page("cookie-preferences.html", "Cookie Preferences", "Manage your cookie preferences for the NexTech Digital website.", body, "")


def disclaimer():
    s = [("General information", "<p>The information on this website is provided for general information only and does not constitute professional advice. Always seek advice specific to your situation.</p>"),
         ("Illustrative content", "<p>Projects, client logos and some figures shown on this website are <strong>illustrative</strong> and are marked as such. They demonstrate capabilities and do not represent real clients, endorsements or results.</p>"),
         ("Accuracy", "<p>We aim to keep information accurate and up to date but make no warranties about its completeness or accuracy.</p>"),
         ("Trademarks", "<p>Technology names and logos (for example React, AWS, Azure and Docker) are trademarks of their respective owners. Their use does not imply endorsement or partnership.</p>"),
         ("External links", "<p>Links to external websites are provided for convenience; we are not responsible for their content.</p>")]
    return legal("disclaimer.html", "Website Disclaimer", "Website disclaimer for NexTech Digital, including illustrative content and trademarks.", s, "remove the illustrative labels only once real client logos, projects and figures are approved for publication.")


def not_found():
    b = ""
    body = f'''<section class="phero nf"><div class="phero-bg kb">{img(b, "nx-cube", "", "", True)}</div><canvas class="net" aria-hidden="true"></canvas><div class="phero-grid" aria-hidden="true"></div>
  <div class="container phero-in center"><p class="big404" data-reveal="zoom">404</p><h1 data-split>This page drifted into the cloud</h1><p class="phero-sub" data-reveal>The page you are looking for doesn&#8217;t exist or has moved.</p>
  <div class="btn-row center" data-reveal>{btn("index.html", "Back to Home")}{btn("contact.html", "Contact Us", "outline", False)}</div></div><div class="blend" aria-hidden="true"></div></section>'''
    return page("404.html", "Page Not Found", "The page you requested could not be found.", body, "")
