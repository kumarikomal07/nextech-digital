"""Build the NexTech Digital static site.

Usage (from the project root):  python3 tools/build.py
Writes all HTML pages, sitemap.xml and robots.txt into the project root.
Edit content in tools/data.py, layout in tools/ui.py and pages in tools/pages_*.py.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from data import SITE, ARTICLES  # noqa: E402
import pages_home as H  # noqa: E402
import pages_inner as P  # noqa: E402


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return rel


def main():
    out = [
        write("index.html", H.home()),
        write("about.html", P.about()),
        write("services.html", P.services()),
        write("industries.html", P.industries()),
        write("work.html", P.work()),
        write("technology.html", P.technology()),
        write("insights.html", P.insights()),
        write("careers.html", P.careers()),
        write("contact.html", P.contact()),
        write("privacy-policy.html", P.privacy()),
        write("terms.html", P.terms()),
        write("cookie-policy.html", P.cookie_policy()),
        write("cookie-preferences.html", P.cookie_prefs()),
        write("disclaimer.html", P.disclaimer()),
        write("404.html", P.not_found()),
    ]
    for a in ARTICLES:
        out.append(write(f"insights/{a['slug']}.html", P.article(a)))

    urls = "".join(f"  <url><loc>{SITE['domain']}/{'' if r == 'index.html' else r}</loc><lastmod>2026-11-19</lastmod></url>\n" for r in out if r != "404.html")
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_archive/\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    print(f"Built {len(out)} pages.")


if __name__ == "__main__":
    main()
