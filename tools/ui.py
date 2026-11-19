"""Shared layout and components for the NexTech Digital site generator."""
import json
from html import escape as esc
from data import SITE, SERVICES, INDUSTRIES, ARTICLES

# ---------------------------------------------------------------- icons
_P = {
    "code": '<path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>',
    "device": '<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/>',
    "cloud": '<path d="M17.5 19a4.5 4.5 0 0 0 .6-8.96A6 6 0 0 0 6.3 9.2 4 4 0 0 0 6.5 19z"/>',
    "chart": '<path d="M3 21h18"/><rect x="5" y="11" width="3" height="7" rx=".6"/><rect x="10.5" y="7" width="3" height="11" rx=".6"/><rect x="16" y="3" width="3" height="15" rx=".6"/>',
    "layers": '<path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "cpu": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-ur": '<path d="M7 17 17 7M8 7h9v9"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "bulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V17h6v-.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7 .9L21 7.3"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 12h6M9 16h4"/>',
    "headset": '<path d="M3 14v-2a9 9 0 0 1 18 0v2"/><path d="M21 15a2 2 0 0 1-2 2h-1v-6h1a2 2 0 0 1 2 2zM3 15a2 2 0 0 0 2 2h1v-6H5a2 2 0 0 0-2 2z"/><path d="M19 17v1a3 3 0 0 1-3 3h-3"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "bank": '<path d="M3 21h18M3 10h18M5 6l7-3 7 3M5 10v11M19 10v11M9.5 10v11M14.5 10v11"/>',
    "health": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
    "cart": '<circle cx="9" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
    "cap": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/><path d="M22 10v6"/>',
    "factory": '<path d="M2 20V9l6 4V9l6 4V5h3l1 8h4v7z"/><path d="M6 17h2M11 17h2M16 17h2"/>',
    "truck": '<path d="M1 4h14v12H1zM15 9h4l3 3v4h-7"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>',
    "server": '<rect x="3" y="3" width="18" height="7" rx="1.5"/><rect x="3" y="14" width="18" height="7" rx="1.5"/><path d="M7 6.5h.01M7 17.5h.01"/>',
    "database": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "close": '<path d="M18 6 6 18M6 6l12 12"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
    "trend": '<path d="m23 6-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5V22h16"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
    "sparkle": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "palette": '<circle cx="13.5" cy="6.5" r="1"/><circle cx="17.5" cy="10.5" r="1"/><circle cx="8.5" cy="7.5" r="1"/><circle cx="6.5" cy="12.5" r="1"/><path d="M12 2a10 10 0 0 0 0 20c1 0 1.7-.8 1.7-1.7 0-.4-.2-.8-.4-1.1-.3-.3-.4-.7-.4-1.1 0-1 .8-1.7 1.7-1.7h2A5.6 5.6 0 0 0 22 11c0-5-4.5-9-10-9z"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
}
_FILL = {
    "linkedin": '<path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.6V9h3.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/>',
    "x": '<path d="M18.2 2.3h3.4l-7.4 8.4 8.7 11.5h-6.8l-5.3-7-6.1 7H1.3l7.9-9L.9 2.3h7l4.8 6.4zm-1.2 17.9h1.9L7 4.2H5z"/>',
    "facebook": '<path d="M24 12.1C24 5.4 18.6 0 12 0S0 5.4 0 12.1c0 6 4.4 11 10.1 11.9v-8.4H7.1v-3.5h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9v2.3h3.4l-.5 3.5h-2.9V24C19.6 23.1 24 18.1 24 12.1z"/>',
    "instagram": '<path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9-.1-1.3-.1-1.6-.1-4.8s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3c1.2-.1 1.6-.1 4.8-.1zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/>',
    "youtube": '<path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6z"/>',
    "whatsapp": '<path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1c-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.3A11.8 11.8 0 0 0 1.7 17.7L0 24l6.4-1.7A11.8 11.8 0 0 0 23.8 12c0-3.2-1.2-6.2-3.4-8.5z"/>',
}


def icon(name, cls="ic"):
    if name in _FILL:
        return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{_FILL[name]}</svg>'
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>'


def logo_mark(uid="lm"):
    return (f'<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#7AA2FF"/><stop offset=".55" stop-color="#477BFF"/><stop offset="1" stop-color="#8B5CF6"/></linearGradient></defs>'
            f'<path d="M6 40 17 8h7l-9 26h-4z" fill="url(#{uid})" opacity=".9"/><path d="M17 8h7l10 22 5-22h6l-8 32h-7L19 16z" fill="url(#{uid})"/></svg>')


def logo(base, uid="lm"):
    return (f'<a class="logo" href="{base}index.html" aria-label="NexTech Digital home">{logo_mark(uid)}'
            '<span class="logo-text"><b>NexTech</b><small>Digital</small></span></a>')


def src(name):
    return f"{name}.jpg" if name.startswith("nx-") else f"{name}.webp"


def img(base, name, alt, cls="", eager=False, sizes=None):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    wh = 'width="1672" height="941"' if name.startswith("nx-") else 'width="1600" height="1067"'
    return f'<img class="{cls}" src="{base}assets/img/{src(name)}" alt="{esc(alt)}" {load} decoding="async" {wh}>'


def btn(href, label, kind="primary", arrow=True, extra=""):
    a = f'<span class="btn-ic">{icon("arrow")}</span>' if arrow else ""
    return f'<a class="btn btn-{kind}" href="{href}" {extra}><span>{label}</span>{a}</a>'


def eyebrow(t):
    return f'<p class="eyebrow" data-reveal>{t}</p>'


def head_block(eb, title, sub="", center=False, extra=""):
    c = " center" if center else ""
    s = f'<p class="sec-sub" data-reveal style="--d:.12s">{sub}</p>' if sub else ""
    return f'<div class="sec-head{c}">{eyebrow(eb)}<h2 class="sec-title" data-split>{title}</h2>{s}{extra}</div>'


# ---------------------------------------------------------------- nav
NAV = [("index.html", "Home"), ("about.html", "About Us"), ("services.html", "Services"), ("industries.html", "Industries"),
       ("work.html", "Our Work"), ("technology.html", "Technology Stack"), ("insights.html", "Insights"), ("careers.html", "Careers"), ("contact.html", "Contact")]


def header(base, active):
    items = []
    for href, label in NAV:
        cur = ' class="active" aria-current="page"' if href == active else ""
        if label in ("Services", "Industries"):
            if label == "Services":
                links = "".join(f'<li><a href="{base}services.html#{s["id"]}"><span class="dd-ic">{icon(s["icon"])}</span><span><strong>{s["name"]}</strong><small>{s["short"]}</small></span></a></li>' for s in SERVICES)
                cls = "dd dd-wide"
            else:
                links = "".join(f'<li><a href="{base}industries.html#{i["id"]}"><span class="dd-ic">{icon(i["icon"])}</span><span><strong>{i["name"]}</strong></span></a></li>' for i in INDUSTRIES)
                cls = "dd"
            did = "dd-" + label.lower()
            items.append(f'<li class="has-dd"><a href="{base}{href}"{cur}>{label}</a><button class="dd-btn" type="button" aria-expanded="false" aria-controls="{did}" aria-label="Show {label.lower()} menu">{icon("chev")}</button>'
                         f'<div class="{cls}" id="{did}"><ul>{links}</ul><a class="dd-all" href="{base}{href}">View all {label.lower()} {icon("arrow")}</a></div></li>')
        else:
            items.append(f'<li><a href="{base}{href}"{cur}>{label}</a></li>')
    return f'''<header class="site-header" data-header>
  <div class="container hdr">
    {logo(base, "lm-h")}
    <nav class="nav" id="nav" aria-label="Main"><ul class="nav-list">{"".join(items)}</ul>
      <div class="nav-foot">{btn(base + "contact.html?type=project#enquiry", "Start a Project", "primary")}<p><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p></div>
    </nav>
    <a class="btn btn-primary btn-sm hdr-cta" href="{base}contact.html?type=project#enquiry"><span>Start a Project</span><span class="btn-ic">{icon("arrow")}</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>'''


def newsletter_form(cls="nl-form", label="Your email address"):
    return f'''<form class="nl-form {cls}" data-newsletter novalidate>
  <label class="sr-only" for="nl-{cls}">{label}</label>
  <input id="nl-{cls}" type="email" name="email" placeholder="Enter your email address" autocomplete="email" required>
  <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button type="submit" aria-label="Subscribe">{icon("send")}</button>
  <p class="form-msg" role="status" aria-live="polite"></p>
</form>'''


def footer(base):
    svc = "".join(f'<li><a href="{base}services.html#{s["id"]}">{s["name"]}</a></li>' for s in SERVICES)
    ind = "".join(f'<li><a href="{base}industries.html#{i["id"]}">{i["name"]}</a></li>' for i in INDUSTRIES[:6])
    quick = "".join(f'<li><a href="{base}{h}">{l}</a></li>' for h, l in NAV if h != "services.html" and h != "industries.html")
    soc = "".join(f'<a href="#" aria-label="NexTech Digital on {n} (link to be added)" data-social>{icon(k, "ic")}</a>' for k, n in [("linkedin", "LinkedIn"), ("x", "X"), ("facebook", "Facebook"), ("instagram", "Instagram"), ("youtube", "YouTube")])
    return f'''<footer class="site-footer">
  <div class="ft-glow" aria-hidden="true"></div>
  <div class="container ft-grid">
    <div class="ft-brand">{logo(base, "lm-f")}<p>A London-based technology company building innovative, reliable and scalable digital solutions for modern businesses.</p><div class="social">{soc}</div></div>
    <div><h3>Quick Links</h3><ul>{quick}</ul></div>
    <div><h3>Our Services</h3><ul>{svc}</ul></div>
    <div><h3>Industries</h3><ul>{ind}</ul></div>
    <div><h3>Contact Us</h3><ul class="ft-contact">
      <li>{icon("pin")}<span>{SITE["city"]}</span></li>
      <li>{icon("mail")}<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
      <li>{icon("phone")}<a href="tel:{SITE["phone_href"]}">{SITE["phone"]}</a></li>
      <li class="wa">{icon("whatsapp")}<a href="#" data-wa>Chat on WhatsApp</a></li></ul></div>
    <div class="ft-nl"><h3>Newsletter</h3><p>Get the latest insights, updates and technology trends from NexTech Digital.</p>{newsletter_form("nl-foot", "Email address for newsletter")}</div>
  </div>
  <div class="container ft-bottom">
    <p>&copy; <span data-year>2026</span> NexTech Digital. All rights reserved.</p>
    <ul><li><a href="{base}privacy-policy.html">Privacy Policy</a></li><li><a href="{base}terms.html">Terms &amp; Conditions</a></li><li><a href="{base}cookie-policy.html">Cookie Policy</a></li><li><a href="{base}cookie-preferences.html">Cookie Preferences</a></li><li><a href="{base}disclaimer.html">Website Disclaimer</a></li></ul>
  </div>
</footer>'''


def chrome_extras(base):
    return f'''<a class="wa-float" href="#" data-wa aria-label="Chat with NexTech Digital on WhatsApp">{icon("whatsapp")}<span>Chat with us</span></a>
<button class="to-top" type="button" aria-label="Back to top">{icon("arrow")}</button>
<div class="cookie" role="dialog" aria-live="polite" aria-label="Cookie consent" hidden data-cookie>
  <div class="cookie-in"><div><strong>We value your privacy</strong><p>We use essential cookies to run this site and, with your consent, analytics cookies to understand how it is used. See our <a href="{base}cookie-policy.html">Cookie Policy</a>.</p></div>
  <div class="cookie-btns"><a class="btn btn-ghost-dark btn-sm" href="{base}cookie-preferences.html"><span>Preferences</span></a><button class="btn btn-ghost-dark btn-sm" type="button" data-consent="reject"><span>Reject optional</span></button><button class="btn btn-primary btn-sm" type="button" data-consent="accept"><span>Accept all</span></button></div></div>
</div>
<script>window.NT_SITE={json.dumps({"whatsapp": SITE["whatsapp"]})};</script>
<script src="{base}js/main.js" defer></script>'''


def page(path, title, desc, body, active="", base="", schema=None, og_img="office-tower"):
    url = SITE["domain"] + "/" + (path if path != "index.html" else "")
    org = {"@context": "https://schema.org", "@type": "Organization", "name": SITE["name"], "url": SITE["domain"] + "/",
           "logo": SITE["domain"] + "/assets/favicon.svg", "foundingDate": SITE["founded"], "email": SITE["email"],
           "address": {"@type": "PostalAddress", "addressLocality": "London", "addressCountry": "GB"}}
    ld = [org] + ([schema] if schema else [])
    full = title if "NexTech" in title else f"{title} | NexTech Digital"
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#101B3C">
<meta property="og:type" content="{"article" if schema and schema.get("@type") == "BlogPosting" else "website"}">
<meta property="og:site_name" content="NexTech Digital">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE["domain"]}/assets/img/{src(og_img)}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}css/styles.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else org)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
{header(base, active)}
<main id="main">
{body}
</main>
{footer(base)}
{chrome_extras(base)}
</body>
</html>
'''


def page_hero(base, eb, title, sub, crumb, image, extra=""):
    return f'''<section class="phero">
  <div class="phero-bg kb" data-parallax=".25">{img(base, image, "", "", True)}</div>
  <canvas class="net" aria-hidden="true"></canvas><div class="phero-grid" aria-hidden="true"></div>
  <div class="container phero-in">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{base}index.html">Home</a>{icon("chev")}<span aria-current="page">{crumb}</span></nav>
    <p class="pill" data-reveal>{eb}</p>
    <h1 data-split>{title}</h1>
    <p class="phero-sub" data-reveal style="--d:.2s">{sub}</p>{extra}
  </div>
  <div class="blend" aria-hidden="true"></div>
</section>'''


# ---------------------------------------------------------------- cards
def svc_card(base, s, i):
    return f'''<a class="svc-card" href="{base}services.html#{s["id"]}" data-reveal data-glow style="--d:{i * .07:.2f}s">
  <span class="svc-ic">{icon(s["icon"])}</span>
  <h3>{s["name"]}</h3><p>{s["short"]}</p>
  <span class="circ">{icon("arrow")}</span>
</a>'''


def project_card(base, p, i, btn_mode=False):
    inner = f'''<div class="pc-media">{img(base, p["img"], p["title"] + " illustrative project")}<span class="tag">{p["tag"]}</span></div>
  <div class="pc-body"><div><h3>{p["title"]}</h3><p>{p["summary"]}</p></div><span class="circ">{icon("arrow")}</span></div>'''
    if btn_mode:
        return f'<button class="proj-card" type="button" data-open="dlg-{p["id"]}" data-cat="{p["cat"]}" data-reveal style="--d:{(i % 3) * .08:.2f}s">{inner}</button>'
    return f'<a class="proj-card" href="{base}work.html#{p["id"]}" data-reveal style="--d:{i * .08:.2f}s">{inner}</a>'


def article_card(base, a, i, prefix=""):
    return f'''<a class="art-card" href="{base}insights/{a["slug"]}.html" data-cat="{a["cat"]}" data-reveal style="--d:{(i % 3) * .08:.2f}s">
  <div class="ac-media">{img(base, a["img"], a["title"])}<span class="tag">{a["cat"]}</span></div>
  <div class="ac-body"><h3>{a["title"]}</h3><p>{a["summary"]}</p>
  <div class="meta"><span>{icon("calendar")}<time datetime="{a["date"]}">{a["date_h"]}</time></span><span>{icon("clock")}{a["read"]} min read</span></div></div>
</a>'''


def cta_band(base, title="Have a Project in Mind?", accent="Let&#8217;s Build It Together.", sub="Turn your ideas into powerful digital solutions with NexTech Digital.", label="Start a Project", href="contact.html?type=project#enquiry"):
    return f'''<section class="cta-wrap"><div class="container">
  <div class="cta" data-reveal="zoom">
    <div class="cta-art" aria-hidden="true"><img src="{base}assets/img/nx-cube.jpg" alt="" loading="lazy" width="1672" height="941"></div>
    <div class="cta-txt"><h2>{title}<br><span class="grad">{accent}</span></h2></div>
    <p class="cta-sub">{sub}</p>
    {btn(base + href, label, "white")}
    <div class="cta-shine" aria-hidden="true"></div>
  </div></div></section>'''


def faq(items):
    return "".join(f'<details class="faq" data-reveal style="--d:{i * .05:.2f}s"><summary><span>{q}</span><i>{icon("plus")}</i></summary><div class="faq-a"><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))


def flag(text):
    return f'<div class="flag">{icon("bulb")}<p><strong>To review before launch:</strong> {text}</p></div>'


def showcase_band(base, image, eb, title, text, feats, cta):
    fl = "".join(f'<li data-reveal style="--d:{.15 + i * .08:.2f}s">{icon(ic)}<span>{t}</span></li>' for i, (ic, t) in enumerate(feats))
    return f'''<section class="showcase">
  <div class="sc-bg kb" data-parallax=".18">{img(base, image, "")}</div><div class="sc-shade" aria-hidden="true"></div><canvas class="net net-dim" aria-hidden="true"></canvas>
  <div class="container sc-in">
    <div class="sc-copy">{eyebrow(eb)}<h2 class="sec-title" data-split>{title}</h2><p class="sec-sub" data-reveal style="--d:.1s">{text}</p>
      <ul class="sc-feats">{fl}</ul><div data-reveal style="--d:.4s">{cta}</div></div>
  </div>
</section>'''
