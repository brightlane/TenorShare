#!/usr/bin/env python3

import os
import random
import datetime
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================

SITE_NAME = "TenorShare"
BASE_URL = "https://brightlane.github.io/TenorShare"
OUTPUT_DIR = "docs"

# KEEP THIS EXACTLY INTACT
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949102662006847&atid=TenorShare"

TODAY = datetime.date.today().isoformat()

# =========================================================
# SEO DATA
# =========================================================

HEADLINES = [
    "Best TenorShare Recovery Tools 2026",
    "Recover Lost iPhone Data Fast",
    "Fix iPhone Boot Loop Instantly",
    "Unlock Disabled iPhone Without iTunes",
    "Top TenorShare Software Deals",
    "TenorShare Data Recovery & Repair",
]

CTA_TEXT = [
    "👉 Recover Lost iPhone Data Now",
    "👉 Fix Your iPhone Instantly",
    "👉 Unlock Your Device Today",
    "👉 View Live TenorShare Deals",
    "👉 Start iOS System Repair",
]

META_DESCRIPTIONS = [
    "Discover TenorShare recovery, unlock, repair, and WhatsApp transfer tools updated daily.",
    "Find powerful iPhone recovery software and mobile repair utilities with live TenorShare offers.",
    "Compare TenorShare software tools for data recovery, unlock, and system repair.",
]

KEYWORDS = [
    "TenorShare",
    "TenorShare ReiBoot",
    "TenorShare 4uKey",
    "TenorShare iCareFone",
    "iPhone recovery software",
    "recover deleted iPhone files",
    "unlock disabled iPhone",
    "repair iOS system",
    "WhatsApp transfer software",
]

PRODUCTS = [
    {
        "slug": "reiboot",
        "title": "TenorShare ReiBoot",
        "problem": "Fix iPhone boot loops and frozen Apple logo issues.",
    },
    {
        "slug": "4ukey",
        "title": "TenorShare 4uKey",
        "problem": "Unlock disabled iPhone and Android devices.",
    },
    {
        "slug": "icarefone",
        "title": "TenorShare iCareFone",
        "problem": "Transfer WhatsApp and manage mobile files.",
    },
    {
        "slug": "ianygo",
        "title": "TenorShare iAnyGo",
        "problem": "Change GPS location on iPhone and Android.",
    },
]

LONGTAIL_PAGES = [
    {
        "slug": "fix-iphone-boot-loop",
        "title": "How To Fix iPhone Boot Loop",
        "intent": "Users searching for iPhone boot loop fixes.",
    },
    {
        "slug": "recover-deleted-iphone-photos",
        "title": "Recover Deleted iPhone Photos",
        "intent": "Users trying to recover deleted iPhone images.",
    },
    {
        "slug": "unlock-disabled-iphone",
        "title": "Unlock Disabled iPhone Without iTunes",
        "intent": "Users needing iPhone unlock software.",
    },
    {
        "slug": "transfer-whatsapp-android-to-iphone",
        "title": "Transfer WhatsApp Android To iPhone",
        "intent": "Users moving WhatsApp data between devices.",
    },
]

COMPARISON_PAGES = [
    {
        "slug": "tenorshare-vs-drfone",
        "title": "TenorShare vs Dr.Fone",
    },
    {
        "slug": "reiboot-vs-itunes",
        "title": "ReiBoot vs iTunes Recovery",
    },
]

# =========================================================
# HELPERS
# =========================================================

def ensure_dirs():
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    Path(f"{OUTPUT_DIR}/products").mkdir(exist_ok=True)
    Path(f"{OUTPUT_DIR}/guides").mkdir(exist_ok=True)
    Path(f"{OUTPUT_DIR}/compare").mkdir(exist_ok=True)
    Path(f"{OUTPUT_DIR}/blog").mkdir(exist_ok=True)

def rand_headline():
    return random.choice(HEADLINES)

def rand_desc():
    return random.choice(META_DESCRIPTIONS)

def rand_cta():
    return random.choice(CTA_TEXT)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def build_template(title, description, body, canonical):

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">
<meta name="keywords" content="{', '.join(KEYWORDS)}">
<meta name="robots" content="index, follow">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">

<style>

body {{
    font-family: system-ui, sans-serif;
    background: #f4f6f9;
    color: #1a1a1a;
    max-width: 1100px;
    margin: auto;
    padding: 20px;
    line-height: 1.7;
}}

.hero {{
    background: linear-gradient(135deg,#022b55,#011a33);
    color: white;
    padding: 50px;
    border-radius: 20px;
    text-align: center;
}}

.card {{
    background: white;
    padding: 25px;
    border-radius: 16px;
    margin-top: 25px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.08);
}}

.btn {{
    display:inline-block;
    margin-top:20px;
    background:#021f3f;
    color:white;
    text-decoration:none;
    padding:18px 34px;
    border-radius:14px;
    font-weight:bold;
    font-size:1.1rem;
}}

.btn:hover {{
    opacity:0.92;
}}

footer {{
    margin-top:50px;
    text-align:center;
    color:#777;
}}

table {{
    width:100%;
    border-collapse: collapse;
}}

td, th {{
    border:1px solid #ddd;
    padding:12px;
}}

nav a {{
    margin-right:15px;
}}

</style>

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {{
      "@type":"Question",
      "name":"Is TenorShare safe?",
      "acceptedAnswer":{{
        "@type":"Answer",
        "text":"TenorShare is widely used for iPhone recovery, unlock, repair, and transfer tools."
      }}
    }},
    {{
      "@type":"Question",
      "name":"Can TenorShare recover deleted files?",
      "acceptedAnswer":{{
        "@type":"Answer",
        "text":"TenorShare software includes tools for recovering deleted photos, videos, WhatsApp data, and files."
      }}
    }}
  ]
}}
</script>

</head>

<body>

<nav>
<a href="/">Home</a>
<a href="/products/reiboot.html">ReiBoot</a>
<a href="/products/4ukey.html">4uKey</a>
<a href="/guides/fix-iphone-boot-loop.html">Guides</a>
<a href="/compare/tenorshare-vs-drfone.html">Comparisons</a>
</nav>

{body}

<footer>
<p>© 2026 Benny “Palmo Kid” Palmarino</p>
</footer>

</body>
</html>
"""

# =========================================================
# HOMEPAGE
# =========================================================

def build_homepage():

    title = rand_headline()
    description = rand_desc()

    body = f"""
<section class="hero">

<h1>{title}</h1>

<p>
Recover deleted files, unlock phones, repair iOS systems,
transfer WhatsApp, and fix Apple device problems.
</p>

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>

<section class="card">

<h2>Best TenorShare Software</h2>

<ul>
<li>ReiBoot — iOS system repair</li>
<li>4uKey — device unlock</li>
<li>iCareFone — WhatsApp transfer</li>
<li>iAnyGo — GPS changer</li>
</ul>

</section>

<section class="card">

<h2>Popular Guides</h2>

<ul>
<li><a href="guides/fix-iphone-boot-loop.html">Fix iPhone Boot Loop</a></li>
<li><a href="guides/recover-deleted-iphone-photos.html">Recover Deleted Photos</a></li>
<li><a href="guides/unlock-disabled-iphone.html">Unlock Disabled iPhone</a></li>
</ul>

</section>

<section class="card">

<h2>Comparison Pages</h2>

<ul>
<li><a href="compare/tenorshare-vs-drfone.html">TenorShare vs Dr.Fone</a></li>
<li><a href="compare/reiboot-vs-itunes.html">ReiBoot vs iTunes</a></li>
</ul>

</section>
"""

    html = build_template(
        title,
        description,
        body,
        f"{BASE_URL}/"
    )

    write_file(f"{OUTPUT_DIR}/index.html", html)

# =========================================================
# PRODUCT PAGES
# =========================================================

def build_products():

    for p in PRODUCTS:

        body = f"""
<section class="hero">

<h1>{p['title']}</h1>

<p>{p['problem']}</p>

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>

<section class="card">

<h2>Why Use {p['title']}</h2>

<p>
{p['problem']}
TenorShare tools are popular for recovering files,
repairing iOS systems, unlocking devices,
and transferring data safely.
</p>

</section>

<section class="card">

<h2>Benefits</h2>

<table>
<tr><th>Feature</th><th>Benefit</th></tr>
<tr><td>Fast Repair</td><td>Quickly fixes iOS issues</td></tr>
<tr><td>User Friendly</td><td>Simple beginner workflow</td></tr>
<tr><td>Recovery Tools</td><td>Restore lost mobile data</td></tr>
</table>

</section>

<section class="card">

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>
"""

        html = build_template(
            p["title"],
            rand_desc(),
            body,
            f"{BASE_URL}/products/{p['slug']}.html"
        )

        write_file(
            f"{OUTPUT_DIR}/products/{p['slug']}.html",
            html
        )

# =========================================================
# LONGTAIL GUIDES
# =========================================================

def build_guides():

    for g in LONGTAIL_PAGES:

        body = f"""
<section class="hero">

<h1>{g['title']}</h1>

<p>{g['intent']}</p>

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>

<section class="card">

<h2>Step-by-Step Solution</h2>

<p>
This guide explains how to solve the issue safely using
modern iPhone recovery and repair software.
</p>

<p>
TenorShare tools help recover deleted data,
repair system crashes, and unlock disabled devices.
</p>

</section>

<section class="card">

<h2>Recommended Fix</h2>

<ul>
<li>Recover lost files</li>
<li>Repair frozen iPhone screens</li>
<li>Unlock disabled devices</li>
<li>Transfer WhatsApp safely</li>
</ul>

</section>

<section class="card">

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>
"""

        html = build_template(
            g["title"],
            rand_desc(),
            body,
            f"{BASE_URL}/guides/{g['slug']}.html"
        )

        write_file(
            f"{OUTPUT_DIR}/guides/{g['slug']}.html",
            html
        )

# =========================================================
# COMPARISON PAGES
# =========================================================

def build_comparisons():

    for c in COMPARISON_PAGES:

        body = f"""
<section class="hero">

<h1>{c['title']}</h1>

<p>
Compare features, recovery tools,
repair workflows, and usability.
</p>

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>

<section class="card">

<h2>Feature Comparison</h2>

<table>
<tr>
<th>Feature</th>
<th>TenorShare</th>
<th>Competitor</th>
</tr>

<tr>
<td>iPhone Recovery</td>
<td>Yes</td>
<td>Yes</td>
</tr>

<tr>
<td>WhatsApp Transfer</td>
<td>Yes</td>
<td>Limited</td>
</tr>

<tr>
<td>Boot Loop Repair</td>
<td>Advanced</td>
<td>Basic</td>
</tr>

</table>

</section>

<section class="card">

<p>
TenorShare tools are frequently used for
repairing iPhones, recovering files,
unlocking devices, and transferring data.
</p>

</section>
"""

        html = build_template(
            c["title"],
            rand_desc(),
            body,
            f"{BASE_URL}/compare/{c['slug']}.html"
        )

        write_file(
            f"{OUTPUT_DIR}/compare/{c['slug']}.html",
            html
        )

# =========================================================
# BLOG POSTS
# =========================================================

def build_blog():

    for i in range(10):

        slug = f"{TODAY}-{i}.html"

        title = random.choice([
            "Recover Lost iPhone Photos",
            "Fix Frozen Apple Logo",
            "Transfer WhatsApp Safely",
            "Repair iOS Boot Loop",
            "Unlock Disabled iPhone",
        ])

        body = f"""
<section class="hero">

<h1>{title}</h1>

<p>
Daily updated mobile repair and recovery guide.
</p>

<a class="btn"
href="{AFFILIATE_URL}"
target="_blank"
rel="nofollow noopener sponsored">

{rand_cta()}

</a>

</section>

<section class="card">

<p>
This article explains modern methods for repairing
mobile devices, recovering deleted files,
and transferring important data safely.
</p>

</section>
"""

        html = build_template(
            title,
            rand_desc(),
            body,
            f"{BASE_URL}/blog/{slug}"
        )

        write_file(
            f"{OUTPUT_DIR}/blog/{slug}",
            html
        )

# =========================================================
# SITEMAP
# =========================================================

def build_sitemap():

    urls = [f"{BASE_URL}/"]

    for p in PRODUCTS:
        urls.append(f"{BASE_URL}/products/{p['slug']}.html")

    for g in LONGTAIL_PAGES:
        urls.append(f"{BASE_URL}/guides/{g['slug']}.html")

    for c in COMPARISON_PAGES:
        urls.append(f"{BASE_URL}/compare/{c['slug']}.html")

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        sitemap.append(f"""
<url>
<loc>{url}</loc>
<lastmod>{TODAY}</lastmod>
<changefreq>daily</changefreq>
<priority>0.9</priority>
</url>
""")

    sitemap.append("</urlset>")

    write_file(
        f"{OUTPUT_DIR}/sitemap.xml",
        "\n".join(sitemap)
    )

# =========================================================
# ROBOTS
# =========================================================

def build_robots():

    robots = f"""
User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

    write_file(
        f"{OUTPUT_DIR}/robots.txt",
        robots
    )

# =========================================================
# LLMS
# =========================================================

def build_llms():

    text = f"""
# {SITE_NAME}

AI-readable affiliate landing pages for:
- iPhone recovery
- iOS repair
- phone unlock
- WhatsApp transfer
- mobile recovery tools

Primary URL:
{BASE_URL}

Affiliate destination:
{AFFILIATE_URL}
"""

    write_file(
        f"{OUTPUT_DIR}/llms.txt",
        text
    )

# =========================================================
# MAIN
# =========================================================

def main():

    ensure_dirs()

    build_homepage()

    build_products()

    build_guides()

    build_comparisons()

    build_blog()

    build_sitemap()

    build_robots()

    build_llms()

    print("✅ TenorShare Super SEO Engine Complete")
    print("✅ Affiliate URL preserved")
    print(f"✅ Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
