# Serene Summits — Northeast India Tours, sold to Punjab & Chandigarh

Static SEO site: one homepage + one page per Punjab district plus
Chandigarh ("Best Travel Agency for Northeast India Tour in
[District]"), 24 pages total, generated from `generate.py`.

Same model as the Tamil Nadu, Goa, West Bengal and Odisha sites: the
destination sold is Northeast India — the 23 Punjab districts and
Chandigarh are the *searcher's* location, not the destination.

## Before you publish — 2 things to fix

Open `generate.py`, edit the `CONFIG` dict, then re-run
`python3 generate.py`:

1. **`email`** — currently a placeholder (`info@serenesummits.in`).
2. **`site_url`** — currently `https://serenesummits.in/punjab`. Set
   this to wherever the site will actually live before publishing —
   it's baked into every canonical tag and the sitemap.

Phone and WhatsApp are already filled in from what you gave me
earlier.

## A judgment call worth checking

Punjab & Chandigarh are far from Assam (unlike West Bengal, which
borders it), so every district page assumes travellers connect
through a metro hub like Delhi rather than flying direct. I avoided
stating specific direct-flight claims since airline routes on this
sector change and conflicting info exists — if you know a reliable
direct or near-direct routing, edit the per-zone airport text in
`AIRPORT_ZONES` and the sentence in `build_district_page()`.

Districts are grouped by real regional airport, not arbitrarily:
- **Amritsar** (Majha): Amritsar, Gurdaspur, Tarn Taran, Pathankot
- **Jalandhar** (Doaba): Jalandhar, Kapurthala, Hoshiarpur, Shahid Bhagat Singh Nagar
- **Chandigarh** (Malwa + Chandigarh UT): everyone else — Ludhiana, Patiala, Sangrur, Barnala, Malerkotla, Moga, Bathinda, Faridkot, Fazilka, Ferozepur, Mansa, Sri Muktsar Sahib, Fatehgarh Sahib, Rupnagar, SAS Nagar (Mohali), and Chandigarh itself

## Hosting on GitHub Pages

Same two options as the other state sites:

**New repo:**
```bash
git init && git add . && git commit -m "Northeast India tours — Punjab & Chandigarh district pages"
git branch -M main
git remote add origin https://github.com/<you>/<repo-name>.git
git push -u origin main
```
Then **Settings → Pages → Source: `main`, `/` (root)**.

**Or** drop this folder into `/punjab/` inside your existing
`serenesummits.in` repo and keep `site_url` as
`https://serenesummits.in/punjab`.

## Editing content

- `AIRPORT_ZONES` — the 24 districts, grouped by airport.
- `NE_HIGHLIGHTS` / `SERVICES` / `WHY_US` — same Northeast India
  product content used across all five state sites.

Then `python3 generate.py` — rewrites everything from scratch, safe
to re-run any time.
