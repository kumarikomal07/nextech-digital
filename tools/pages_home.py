from ui import *
from data import SITE, SERVICES, HOME_INDUSTRIES, PROJECTS, ARTICLES, HOME_TECH

CHIPS = [("cpu", "AI &amp;<br>Automation", "c1"), ("cloud", "Cloud<br>Computing", "c2"), ("code", "Custom<br>Software", "c3"),
         ("layers", "Digital<br>Transformation", "c4"), ("device", "Web &amp; App<br>Development", "c5"), ("chart", "IT Consulting<br>&amp; Strategy", "c6")]

TRUSTED = [("layers", "TechSphere"), ("chart", "FinanceHive"), ("health", "HealthSync"), ("cart", "RetailFlow"), ("book", "EduNext"), ("settings", "ManufactureX"), ("truck", "LogiCore"), ("cloud", "Cloudora")]


def hero_scene():
    chips = "".join(f'<div class="chip {c}"><span class="chip-ic">{icon(ic)}</span><span>{t}</span></div>' for ic, t, c in CHIPS)
    return f'''<div class="scene" data-scene aria-hidden="true">
  <div class="halo"></div>
  <div class="hero-art"><img src="assets/img/nx-cube.jpg" alt="" width="1672" height="941" fetchpriority="high" decoding="async"></div>
  <div class="beam"></div>
  <div class="cube-wrap"><div class="cube"><i class="f1"></i><i class="f2"></i><i class="f3"></i><i class="f4"></i><i class="f5"></i><i class="f6"></i></div></div>
  <svg class="scene-lines" viewBox="0 0 600 560" preserveAspectRatio="none">
    <defs><linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="#477BFF" stop-opacity="0"/><stop offset=".5" stop-color="#7AA2FF"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></linearGradient></defs>
    <path d="M150 95 C220 130 250 180 300 250"/><path d="M95 230 C170 240 220 250 300 270"/><path d="M110 380 C180 350 240 320 300 290"/>
    <path d="M470 70 C420 130 360 190 300 250"/><path d="M500 200 C430 230 370 250 300 270"/><path d="M500 330 C430 320 370 300 300 290"/>
  </svg>
  {chips}
  <span class="spark s1"></span><span class="spark s2"></span><span class="spark s3"></span><span class="spark s4"></span>
</div>'''


def home():
    b = ""
    hero = f'''<section class="hero" data-hero>
  <canvas class="net" aria-hidden="true"></canvas>
  <div class="hero-floor" aria-hidden="true"></div><div class="aurora a1" aria-hidden="true"></div><div class="aurora a2" aria-hidden="true"></div>
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="pill" data-reveal>{SITE["tagline"]}</p>
      <h1 data-split>Technology That Moves Your Business <span class="grad">Forward</span></h1>
      <p class="hero-sub" data-reveal style="--d:.35s">We design, build and scale digital solutions that solve real business challenges, drive efficiency and create long-term growth.</p>
      <div class="btn-row" data-reveal style="--d:.45s">{btn("services.html", "Explore Services")}{btn("contact.html?type=project#enquiry", "Start a Project", "outline", False)}</div>
      <ul class="hero-stats" data-reveal style="--d:.55s">
        <li>{icon("rocket")}<div><b><span data-count="6">6</span>+</b><small>Core Services</small></div></li>
        <li>{icon("calendar")}<div><b>2018</b><small>Established</small></div></li>
        <li>{icon("pin")}<div><b>London</b><small>Headquarters</small></div></li>
      </ul>
    </div>
    {hero_scene()}
  </div>
  <div class="blend" aria-hidden="true"></div>
</section>'''

    marks = "".join(f'<li>{icon(ic)}<span><b>{n}</b><small>Illustrative</small></span></li>' for ic, n in TRUSTED)
    trusted = f'''<section class="trusted" aria-label="Trusted by growing businesses (illustrative brands)">
  <div class="container"><div class="trusted-card" data-reveal>
    <p class="trusted-label">Trusted By<br>Growing Businesses</p>
    <div class="marquee"><ul class="mq-track">{marks}{marks.replace("<li>", '<li aria-hidden="true">')}</ul></div>
  </div></div>
</section>'''

    about = f'''<section class="sec about-intro"><div class="container about-grid">
  <div class="ai-copy">{eyebrow("About NexTech Digital")}
    <h2 class="sec-title sm" data-split>A Trusted Technology Partner for Modern Businesses</h2>
    <p data-reveal style="--d:.1s">NexTech Digital is a London-based technology company, established in {SITE["founded"]}, helping businesses build, modernise and scale their digital capabilities with software, cloud and AI solutions.</p>
    <ul class="mini-stats" data-reveal style="--d:.2s">
      <li>{icon("users")}<div><b><span data-count="50">50</span>+</b><small>Tech Professionals<em>(illustrative)</em></small></div></li>
      <li>{icon("layers")}<div><b><span data-count="100">100</span>+</b><small>Projects<em>(illustrative)</em></small></div></li>
      <li>{icon("globe")}<div><b>Global</b><small>Client Support</small></div></li>
    </ul>
    <div data-reveal style="--d:.3s">{btn("about.html", "Learn More About Us", "soft")}</div>
  </div>
  <div class="ai-media" data-reveal="wipe"><div class="img-frame" data-tilt>{img(b, "nx-team", "NexTech Digital engineers collaborating in a modern London office")}<div class="frame-badge">{logo_mark("lm-ab")}<span>NexTech<small>Digital</small></span></div></div><div class="orbit-dot" aria-hidden="true"></div></div>
  <div class="mv">
    <article class="mv-card" data-reveal="left" data-glow><span class="mv-ic">{icon("target")}</span><div><h3>Our Mission</h3><p>To empower businesses with innovative, reliable and scalable technology solutions.</p></div></article>
    <article class="mv-card" data-reveal="left" data-glow style="--d:.12s"><span class="mv-ic">{icon("eye")}</span><div><h3>Our Vision</h3><p>To be a globally trusted digital partner, driving business growth through technology and innovation.</p></div></article>
  </div>
</div></section>'''

    services = f'''<section class="sec sec-dark services-ov"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container">
  <div class="sec-row">{head_block("Our Services", "End-to-End Digital Solutions for Your Business", "A comprehensive suite of technology services to build, modernise and grow your business.")}<div data-reveal>{btn("services.html", "All Services", "glass")}</div></div>
  <div class="svc-grid">{"".join(svc_card(b, s, i) for i, s in enumerate(SERVICES))}</div>
</div></section>'''

    why = [("bulb", "Innovation", "Future-ready solutions."), ("shield", "Reliability", "Secure, stable and scalable."), ("code", "Technical Expertise", "Experienced and skilled team."),
           ("layers", "Transparency", "Clear communication and honest delivery."), ("users", "Collaboration", "A true partnership for shared success.")]
    tech = "".join(f'<li data-reveal style="--d:{i * .06:.2f}s"><img src="assets/logos/{f}.svg" alt="" loading="lazy" width="40" height="40"><span>{n}</span></li>' for i, (n, f) in enumerate(HOME_TECH))
    why_stack = f'''<section class="sec sec-light why-stack"><div class="container ws-grid">
  <div class="why" data-reveal="zoom">
    <canvas class="net net-dim" aria-hidden="true"></canvas><div class="why-wave" aria-hidden="true"></div>
    <h2 data-split>Why Choose NexTech Digital?</h2><p class="why-sub">More than a technology provider &mdash; we&#8217;re your long-term digital partner.</p>
    <ul class="why-list">{"".join(f'<li data-reveal style="--d:{.1 + i * .08:.2f}s">{icon(ic)}<h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(why))}</ul>
  </div>
  <div class="stack">{eyebrow("Technology")}<h2 class="sec-title sm" data-split>Our Technology Stack</h2><p class="sec-sub" data-reveal>A modern, reliable and scalable technology ecosystem.</p>
    <ul class="stack-grid">{tech}</ul>
    <div data-reveal>{btn("technology.html", "Explore Full Technology Stack", "soft")}</div>
  </div>
</div></section>'''

    projects = f'''<section class="sec"><div class="container">
  <div class="sec-row">{head_block("Featured Projects", "Real Solutions. Tangible Impact.", "A selection of illustrative projects that showcase our capabilities across industries and technologies.")}<div data-reveal>{btn("work.html", "View All Projects", "soft")}</div></div>
  <div class="proj-grid four">{"".join(project_card(b, p, i) for i, p in enumerate(PROJECTS[:4]))}</div>
</div></section>'''

    showcase = showcase_band(b, "nx-cloud", "Cloud &amp; Infrastructure", "Cloud-Native. AI-Ready. <span class=\"grad\">Built to Scale.</span>",
                             "We architect secure, resilient cloud platforms that grow with your business, from first migration to intelligent, automated operations.",
                             [("cloud", "AWS, Azure &amp; Google Cloud"), ("shield", "Security built in"), ("zap", "Automated CI/CD"), ("trend", "Scales on demand")],
                             btn("services.html#cloud", "Explore Cloud Solutions", "white"))

    ind_tiles = "".join(f'<a class="ind-photo" href="industries.html#{x["id"]}" data-reveal style="--d:{i * .07:.2f}s">{img(b, x["img"], "")}<span class="ind-ic">{icon(x["icon"])}</span><span class="ip-name">{x["name"]}</span><span class="ip-more">Explore {icon("arrow")}</span></a>' for i, x in enumerate(HOME_INDUSTRIES))
    steps = [("search", "Discover", "Understand your goals, challenges and requirements."), ("clipboard", "Plan", "Define the right solution, roadmap and timeline."), ("code", "Develop", "Build, test and refine with agile practices."),
             ("rocket", "Launch", "Deploy your solution with confidence."), ("headset", "Support", "Provide ongoing support, maintenance and improvements.")]
    ind_proc = f'''<section class="sec sec-light ind-proc"><div class="container">
  <div class="sec-row">{head_block("Industries We Serve", "Technology Solutions Across Key Industries", "We build industry-focused digital solutions that solve real challenges and create lasting value.")}<div data-reveal>{btn("industries.html", "Explore All Industries", "soft")}</div></div>
  <div class="ind-strip">{ind_tiles}</div>
  <div class="proc-wrap">
    {head_block("Our Process", "A Clear, Collaborative and Proven Process", "From idea to ongoing success, we follow a structured and transparent approach.", True)}
    <ol class="process" data-process>{"".join(f'<li data-reveal style="--d:{i * .12:.2f}s"><span class="p-ic">{icon(ic)}<em>{i + 1:02d}</em></span><h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(steps))}<span class="p-line" aria-hidden="true"><i></i></span></ol>
  </div>
</div></section>'''

    insights = f'''<section class="sec sec-dark"><canvas class="net net-dim" aria-hidden="true"></canvas><div class="container split-row ins-row">
  <div class="split-head">{eyebrow("Latest Insights")}<h2 class="sec-title sm" data-split>Insights &amp; Ideas from Our Experts</h2><p class="sec-sub" data-reveal>Explore the latest trends, practical guides and technology insights to grow your business.</p><div data-reveal>{btn("insights.html", "View All Insights", "glass")}</div></div>
  <div class="art-grid">{"".join(article_card(b, a, i) for i, a in enumerate(ARTICLES[:3]))}</div>
</div></section>'''

    body = hero + trusted + about + services + why_stack + projects + showcase + ind_proc + insights + cta_band(b)
    return page("index.html", "NexTech Digital | Software, Cloud & AI Technology Company in London",
                "NexTech Digital is a London-based technology company delivering custom software, web and app development, cloud computing, IT consulting, digital transformation and AI automation.",
                body, "index.html", og_img="nx-cube")
