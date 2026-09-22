#!/usr/bin/env python3
"""
Serene Summits — "Northeast India tours, sold to Punjab & Chandigarh" SEO site.

Same product (Northeast India tours out of Guwahati) as the Tamil Nadu,
Goa, West Bengal and Odisha sites. Punjab & Chandigarh sit at the
opposite end of the country from Assam, so unlike West Bengal there's
no overland option here — every route connects through a metro hub.
Districts are grouped by their real regional airport (Amritsar for
Majha, Jalandhar for Doaba, Chandigarh for Malwa + Chandigarh itself)
rather than treated as one undifferentiated block.

Edit CONFIG below, then run:  python3 generate.py
"""
import re
from datetime import date

CONFIG = {
    "business_name": "Serene Summits",
    "phone_display": "+91 86382 26178",
    "phone_tel": "+918638226178",
    "whatsapp": "918638226178",
    # NOTE: placeholder — swap for your real inbox before publishing
    "email": "info@serenesummits.in",
    "hq_city": "Guwahati, Assam",
    # NOTE: placeholder — set this to your real GitHub Pages / custom
    # domain before publishing, then re-run this script.
    "site_url": "https://serenesummits.in/punjab",
    "instagram": "https://instagram.com/serenesummits",
    "facebook": "https://facebook.com/serenesummits",
    "main_site": "https://serenesummits.in/",
}
TODAY = date.today().isoformat()
STATE_NAME = "Punjab & Chandigarh"

# ----------------------------------------------------------------------
# 23 Punjab districts + Chandigarh (a single UT, no sub-districts),
# grouped by the airport a traveller there would actually use.
# ----------------------------------------------------------------------
AIRPORT_ZONES = {
    "Sri Guru Ram Dass Jee International Airport, Amritsar": [
        "Amritsar", "Gurdaspur", "Tarn Taran", "Pathankot",
    ],
    "Jalandhar (Adampur) Airport": [
        "Jalandhar", "Kapurthala", "Hoshiarpur", "Shahid Bhagat Singh Nagar",
    ],
    "Chandigarh International Airport": [
        "Chandigarh", "Sahibzada Ajit Singh Nagar", "Rupnagar", "Fatehgarh Sahib",
        "Ludhiana", "Patiala", "Sangrur", "Barnala", "Malerkotla", "Moga",
        "Bathinda", "Faridkot", "Fazilka", "Ferozepur", "Mansa", "Sri Muktsar Sahib",
    ],
}
NEAREST_AIRPORT = {}
for airport, districts in AIRPORT_ZONES.items():
    for d in districts:
        NEAREST_AIRPORT[d] = airport

ALL_DISTRICTS = [d for districts in AIRPORT_ZONES.values() for d in districts]

def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

DISTRICTS = [(n, slugify(n)) for n in ALL_DISTRICTS]
print(f"Loaded {len(DISTRICTS)} {STATE_NAME} districts across {len(AIRPORT_ZONES)} airport zones.")

def nearest_airport(name):
    return NEAREST_AIRPORT.get(name, "Chandigarh International Airport")

# ----------------------------------------------------------------------
# Product: same Northeast India destinations sold on every state site.
# ----------------------------------------------------------------------
NE_HIGHLIGHTS = [
    ("Kaziranga National Park, Assam", "A UNESCO World Heritage site and the best place in the world to see the one-horned rhinoceros in the wild."),
    ("Shillong & Cherrapunji, Meghalaya", "Waterfalls, living root bridges and one of the wettest places on Earth, a short drive from Guwahati."),
    ("Tawang, Arunachal Pradesh", "A high-Himalayan monastery town reached via the Sela Pass, near the Bhutan and Tibet borders."),
    ("Majuli Island, Assam", "The world's largest river island, home to centuries-old Assamese Vaishnavite monasteries."),
    ("Dzukou Valley & Kohima, Nagaland", "A seasonal-flower valley trek and the WWII Kohima War Cemetery."),
    ("Ziro Valley, Arunachal Pradesh", "A pine-fringed valley and home of the Apatani tribe, on UNESCO's tentative heritage list."),
    ("Gangtok & Sikkim", "A hill capital with monasteries, cable cars and views toward Kanchenjunga."),
    ("Mawlynnong, Meghalaya", "Asia's cleanest village, known for its double-decker living root bridge."),
]
SERVICES = [
    ("Northeast India Tour Packages", "Fixed departures and custom itineraries covering Assam, Meghalaya, Arunachal Pradesh, Nagaland and Sikkim."),
    ("Flight + Package Combos", "We coordinate your flight into Guwahati around the tour, not the other way round."),
    ("Inner Line Permits (ILP)", "We handle the paperwork required to enter Arunachal Pradesh, Nagaland and Mizoram."),
    ("Hotel & Homestay Booking", "Stays vetted in advance, from hill-town homestays to Kaziranga resort properties."),
    ("Private Cabs & Local Transport", "Local drivers for hill roads that Google Maps alone won't get you through safely."),
    ("Honeymoon & Group Tours", "Separate itineraries for couples, families and college or corporate groups."),
]
WHY_US = [
    ("Based in Guwahati, not a reseller", f"We run these tours ourselves out of Assam — not a {STATE_NAME} agency subcontracting the trip out."),
    ("Permits handled for you", "Arunachal Pradesh, Nagaland and Mizoram all require an Inner Line Permit — we arrange it before you fly."),
    ("Flights coordinated from your city", "We plan the itinerary around a realistic connection from Punjab or Chandigarh into Guwahati."),
    ("Direct support on WhatsApp", "One point of contact throughout, before you fly and while you're on the ground."),
]

def nav_html(depth=""):
    return f'''<nav class="primary">
        <a href="{depth}index.html">Home</a>
        <a href="{depth}index.html#destinations">Destinations</a>
        <a href="{depth}index.html#services">Services</a>
        <a href="{depth}index.html#contact">Contact</a>
      </nav>'''

def header_html(depth=""):
    return f'''<header class="site-header">
    <div class="wrap">
      <a class="brand" href="{depth}index.html">
        <span class="mark">&#9670;</span> {CONFIG['business_name']}
        <span class="place">NORTHEAST INDIA TOURS</span>
      </a>
      {nav_html(depth)}
      <a class="btn btn-call" href="tel:{CONFIG['phone_tel']}">Call {CONFIG['phone_display']}</a>
    </div>
  </header>'''

def kolam_svg():
    dots, lines = [], []
    for row in range(7):
        for col in range(7):
            dots.append(f'<circle cx="{30+col*55}" cy="{30+row*55}" r="3" fill="#f2e9d4"/>')
    for row in range(6):
        for col in range(6):
            x, y = 30 + col*55 + 27, 30 + row*55 + 27
            lines.append(f'<circle cx="{x}" cy="{y}" r="18" fill="none" stroke="#e4c789" stroke-width="1"/>')
    return f'<svg class="kolam" viewBox="0 0 420 420" xmlns="http://www.w3.org/2000/svg">{"".join(lines)}{"".join(dots)}</svg>'

def footer_html(depth=""):
    return f'''<footer>
    <div class="wrap">
      <div>
        <div class="brand-line">{CONFIG['business_name']}</div>
        <p style="max-width:38ch;color:#c9bca7;">A Guwahati-based tour operator running Assam, Meghalaya, Arunachal Pradesh, Nagaland and Sikkim trips for travellers across Punjab's 23 districts and Chandigarh.</p>
        <ul style="flex-direction:row;gap:16px;margin-top:12px;">
          <li><a href="{CONFIG['instagram']}">Instagram</a></li>
          <li><a href="{CONFIG['facebook']}">Facebook</a></li>
        </ul>
      </div>
      <div>
        <h4>CONTACT</h4>
        <ul>
          <li><a href="tel:{CONFIG['phone_tel']}">{CONFIG['phone_display']}</a></li>
          <li><a href="https://wa.me/{CONFIG['whatsapp']}">WhatsApp us</a></li>
          <li><a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></li>
          <li>Based in {CONFIG['hq_city']}</li>
          <li><a href="{CONFIG['main_site']}">Our main site &rarr;</a></li>
        </ul>
      </div>
      <div>
        <h4>POPULAR DISTRICTS</h4>
        <ul>
          <li><a href="{depth}districts/chandigarh.html">Chandigarh</a></li>
          <li><a href="{depth}districts/amritsar.html">Amritsar</a></li>
          <li><a href="{depth}districts/ludhiana.html">Ludhiana</a></li>
          <li><a href="{depth}districts/jalandhar.html">Jalandhar</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap fine">&copy; {date.today().year} {CONFIG['business_name']}. Northeast India tour packages for travellers across Punjab & Chandigarh.</div>
  </footer>'''

def page_shell(*, title, description, canonical, depth, body, schema_json):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{depth}css/style.css">
<script type="application/ld+json">{schema_json}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(depth)}
<main id="main">
{body}
</main>
{footer_html(depth)}
</body>
</html>'''

def business_schema(name, url, area_served):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "TravelAgency",
  "name": "{CONFIG['business_name']} - {name}",
  "url": "{url}",
  "telephone": "{CONFIG['phone_tel']}",
  "email": "{CONFIG['email']}",
  "areaServed": "{area_served}",
  "address": {{
    "@type": "PostalAddress",
    "addressRegion": "Assam",
    "addressCountry": "IN"
  }}
}}'''

def build_homepage():
    district_links = "\n".join(f'<a href="districts/{slug}.html">{name}</a>' for name, slug in DISTRICTS)
    services_cards = "\n".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in SERVICES)
    why_items = "\n".join(f'<li><strong>{t}</strong>{d}</li>' for t, d in WHY_US)
    highlight_cards = "\n".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in NE_HIGHLIGHTS[:4])

    body = f'''
  <section class="hero">
    {kolam_svg()}
    <div class="wrap">
      <div class="eyebrow">Assam &middot; Meghalaya &middot; Arunachal &middot; Nagaland &middot; Sikkim</div>
      <h1>Best Travel Agency for Northeast India Tours — Serving Punjab &amp; Chandigarh</h1>
      <p class="lede">{CONFIG['business_name']} is based in {CONFIG['hq_city']} and runs Northeast India tours for travellers across all 23 districts of Punjab and Chandigarh — flights, permits, stays and local transport, planned as one trip.</p>
      <div class="cta-row">
        <a class="btn btn-call" href="tel:{CONFIG['phone_tel']}">Call {CONFIG['phone_display']}</a>
        <a class="btn btn-outline" href="https://wa.me/{CONFIG['whatsapp']}">Message on WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="section" id="services">
    <div class="wrap">
      <div class="kicker">What we handle</div>
      <h2>One booking, from Punjab to the hills of the Northeast</h2>
      <p class="intro">Northeast India isn't a walk-in destination from this side of the country — permits, hill roads and a long onward journey all need planning. We do that planning.</p>
      <div class="grid cols-3">
        {services_cards}
      </div>
    </div>
  </section>

  <section class="section alt">
    <div class="wrap">
      <div class="kicker">Where you'll go</div>
      <h2>The Northeast India circuit, at a glance</h2>
      <div class="grid cols-2">
        {highlight_cards}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="kicker">Why travellers choose us</div>
      <h2>Run from Guwahati, not resold from a Punjab call centre</h2>
      <ul class="why-list">
        {why_items}
      </ul>
    </div>
  </section>

  <section class="section alt" id="destinations">
    <div class="wrap">
      <div class="kicker">All 23 districts + Chandigarh</div>
      <h2>Find your district</h2>
      <p class="intro">Each page below reflects the regional airport nearest to you — Amritsar for Majha, Jalandhar for Doaba, Chandigarh for Malwa and Chandigarh itself.</p>
      <div class="district-links">
        {district_links}
      </div>
    </div>
  </section>

  <section class="cta-band" id="contact">
    <div class="wrap">
      <h2>Planning a Northeast India trip?</h2>
      <p>Tell us your city and travel dates — we'll send a route and price the same day.</p>
      <a class="btn btn-call" href="tel:{CONFIG['phone_tel']}">Call {CONFIG['phone_display']}</a>
    </div>
  </section>
'''
    title = f"Best Travel Agency for Northeast India Tours in Punjab & Chandigarh | {CONFIG['business_name']}"
    description = f"{CONFIG['business_name']} is a Guwahati-based agency running Assam, Meghalaya, Arunachal Pradesh, Nagaland and Sikkim tours for travellers across Punjab's 23 districts and Chandigarh. Call {CONFIG['phone_display']}."
    html = page_shell(
        title=title, description=description,
        canonical=f"{CONFIG['site_url']}/index.html", depth="",
        body=body, schema_json=business_schema("Punjab & Chandigarh", f"{CONFIG['site_url']}/index.html", "Punjab & Chandigarh, India")
    )
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

def build_district_page(name, slug):
    airport = nearest_airport(name)
    is_ut = name == "Chandigarh"
    place_label = "Union Territory" if is_ut else "district"
    highlight_items = "\n".join(
        f'<li><span class="dot">&#9670;</span><div><strong>{a}</strong><br>{b}</div></li>'
        for a, b in NE_HIGHLIGHTS
    )
    services_cards = "\n".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in SERVICES[:4])

    others = [d for d in DISTRICTS if d[0] != name]
    sample = others[::4][:6]
    related_links = "\n".join(f'<a href="{s}.html">{n}</a>' for n, s in sample)

    body = f'''
  <section class="hero">
    {kolam_svg()}
    <div class="wrap">
      <div class="eyebrow">For travellers in {name}, {STATE_NAME}</div>
      <h1>Best Travel Agency for Northeast India Tour in {name}</h1>
      <p class="lede">Booking a Northeast India trip from {name}? {CONFIG['business_name']} is based in {CONFIG['hq_city']} and plans the whole journey — flights out of {airport}, permits for Arunachal Pradesh and Nagaland, hill transport and stays — as one itinerary.</p>
      <div class="cta-row">
        <a class="btn btn-call" href="tel:{CONFIG['phone_tel']}">Call {CONFIG['phone_display']}</a>
        <a class="btn btn-outline" href="https://wa.me/{CONFIG['whatsapp']}">Message on WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="kicker">Getting there from {name}</div>
      <h2>We plan the trip around {airport}</h2>
      <p class="intro">Northeast India sits at the opposite end of the country from Punjab, so most journeys connect through a metro hub such as Delhi before reaching Guwahati. We build your itinerary around the realistic connection from {airport} rather than assuming a direct flight exists, and coordinate pickup in Guwahati the moment you land.</p>
      <div class="grid cols-2">
        {services_cards}
      </div>
    </div>
  </section>

  <section class="section alt">
    <div class="wrap">
      <div class="kicker">The destination</div>
      <h2>Where a Northeast India tour from {name} can take you</h2>
      <ul class="attractions">
        {highlight_items}
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="kicker">Also serving</div>
      <h2>Booking from elsewhere in {STATE_NAME}?</h2>
      <p class="intro">We run the same planning process for every {place_label} — here are a few other pages you might want.</p>
      <div class="related">
        {related_links}
        <a href="../index.html#destinations">See all districts &rarr;</a>
      </div>
    </div>
  </section>

  <section class="cta-band" id="contact">
    <div class="wrap">
      <h2>Plan your Northeast India trip from {name}</h2>
      <p>Call or WhatsApp your travel dates — we'll reply with a route and price the same day.</p>
      <a class="btn btn-call" href="tel:{CONFIG['phone_tel']}">Call {CONFIG['phone_display']}</a>
    </div>
  </section>
'''
    title = f"Best Travel Agency for Northeast India Tour in {name} | {CONFIG['business_name']}"
    description = f"Looking for the best travel agency for a Northeast India tour in {name}? {CONFIG['business_name']}, based in Guwahati, plans Assam, Meghalaya, Arunachal Pradesh and Nagaland trips for travellers from {name}. Call {CONFIG['phone_display']}."
    canonical = f"{CONFIG['site_url']}/districts/{slug}.html"
    html = page_shell(
        title=title, description=description, canonical=canonical, depth="../",
        body=body, schema_json=business_schema(f"Northeast India Tours for {name}", canonical, f"{name}, {STATE_NAME}")
    )
    with open(f"districts/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)

def build_all_districts():
    for name, slug in DISTRICTS:
        build_district_page(name, slug)

def build_sitemap():
    urls = [f"{CONFIG['site_url']}/index.html"]
    urls += [f"{CONFIG['site_url']}/districts/{slug}.html" for _n, slug in DISTRICTS]
    entries = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq></url>"
        for u in urls
    )
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>'''
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)

def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {CONFIG['site_url']}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)

if __name__ == "__main__":
    import os
    os.makedirs("districts", exist_ok=True)
    build_homepage()
    build_all_districts()
    build_sitemap()
    build_robots()
    print(f"Done: index.html, {len(DISTRICTS)} district pages, sitemap.xml, robots.txt")
