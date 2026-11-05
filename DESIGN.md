# DESIGN.md – stephan-poetschner.at

Read this before touching `portfolio/templates/index.html` or `portfolio/static/css/main.css`.
Design name: **"Stille in Feld-Farben"** (chosen 2026-11-05 from mock-ups in `mockups/`:
layout of C "Stille", colours of B "Feld").

## Goal

Referred visitors (KMU owners, founders) are about to trust one person with an important,
expensive decision. The page must earn that trust in 30 seconds, with text alone: who and where,
for whom he worked, what he offers, how to start (`../pitches/positioning.md`).

It must **not** look like:
- **Bootstrap / a template:** no stock blue, no `#333/#eee` greys, no 8/4 grid with sidebar,
  no cards with shadows, no icon buttons.
- **A newspaper or blog:** no serif reading column with a sidebar, no bylines, no article look.
- **Something technical / a terminal:** no monospace, no "01/02" indices, no code aesthetics,
  no dark-mode-hacker look.

No mood photography. One small round portrait (48px) as proof of a real person.

## Principles (and why)

1. **Contrast, not variety.** Few type sizes, far apart: a huge statement, large names, normal
   body text, small meta. Nothing in between. A page where everything is medium has no priority.
2. **Weight contrast within one typeface.** The statement is light (400) with its key phrase in
   600. One family (Instrument Sans) keeps it calm; contrast comes from size and weight.
3. **Three levels of space, clearly different.** `--space-in` (inside a group) ≪ `--space-group`
   (between items) ≪ `--space-section` (between sections). Proximity shows what belongs together;
   don't add rules or boxes to do space's job.
4. **Facts are design elements.** Client names are set large; figures are huge and in leaf green.
   Proof is what builds trust, so proof gets the visual weight, not adjectives.
5. **Label column + content column.** From 1000px each section has a small green label on the left
   (¼) and content on the right (¾). This asymmetry is the page's structure; everything lines up
   on the content edge. Running text never exceeds `--measure` (38rem).
6. **Colour as fields, one accent.** Cream ground; deep green is the only accent colour (labels,
   links, pill, bands). Full-width bands give rhythm: green for figures, sand for testimonials,
   green footer. Leaf is only ever used on green.
7. **One call to action.** The green pill "Kennenlerngespräch vereinbaren" appears once, at the
   top. The contact section at the end uses large plain links, not a second button.
8. **Important things are dark.** Names, authors, client names in `--ink`. `--muted` only for
   context (years, captions, descriptions of offers). Nothing below 4.5:1.

## Tokens (`:root` in main.css)

| Token | Value | Use |
|---|---|---|
| `--paper` | `#faf7f0` | page ground (cream) |
| `--ink` | `#1b1d1a` | text (16:1) |
| `--muted` | `#5f5e57` | secondary text (6.2:1; 5.2:1 on sand) |
| `--hair` | `#ddd5c4` | thin dividers inside lists |
| `--green` | `#1d3b31` | the accent: labels, link underlines, pill, bands, footer |
| `--leaf` | `#c8e06a` | figures, labels and links **on green only** (8.6:1) |
| `--on-green` / `--on-green-muted` | `#eef0e6` / `#a9bdb2` | text on green (10:1 / 6:1) |
| `--sand` | `#e9e2d3` | testimonial band |

Type (Instrument Sans, self-hosted in `static/fonts/instrument-sans/`, OFL; no italic, so don't
use italics):

| Token | Size | Use |
|---|---|---|
| `--fs-xl` | 2.3–6.5rem | statement, "Projekt besprechen?" (figures use their own 3–6rem) |
| `--fs-lg` | 1.6–2.75rem | client names, offers, project titles, main quote |
| `--fs-md` | 1.25rem | how-I-work headings, secondary quotes |
| `--fs-base` | 1.125rem / 1.55 | running text |
| `--fs-sm` | .9375rem | years, captions, project facts |

Large sizes use negative tracking (−.03 to −.05em) and tight leading (1–1.1).
Weights: 400 and 500 for large type, 600 for emphasis and small headings.

## Page order and components

1. **Top** – portrait + name + "Django-Entwickler in Wien, selbständig seit 2008"; statement;
   pill + "Kostenlos. Ich melde mich meist am selben Tag."
2. **Für wen ich gearbeitet habe** – `.client-list`: name (large) · one line · years.
   Names only for clients that may be named (`profile.md`).
3. **In Zahlen** (green band) – three `<dt>` figures with a small prefix (`<small>seit</small>`).
4. **Was ich für dich tun kann** – the three offers in the order of `positioning.md`.
5. **Wie ich arbeite** – three values, three columns.
6. **Was Kunden sagen** (sand band) – one large quote, two smaller, author in ink.
7. **Projekte im Detail** – from `content/projects/*.md`; facts (Kunde/Zeitraum/Technik) in the
   label column, title + text right. Markdown `#` headings render as small bold labels.
8. **Was erfolgreiche Teams ausmacht** – prose.
9. **Projekt besprechen?** – large heading, email / phone / LinkedIn as large links.
10. **Footer** (green) – imprint and privacy; legally required, keep the content.

Adding a section: `<section class="section">` with `<h2 class="label">` first; add `band
band-green` or `band band-sand` only if the rhythm needs it (never two bands in a row).

## Copy

Copy rules live in `../pitches/copy.md`, facts in `../pitches/profile.md`. Figures on this page
(Django-Vienna: 59 Treffen, 838 Mitglieder, 4,9/5) are from 2026-11; the meetup ends in
November 2026, so keep the wording tense-proof ("mitorganisiert").

## Checking changes

Run `./runserver.py` (restart it after changing `content/`, it loads Markdown at startup), then:

```bash
for w in 1440 390; do
  google-chrome --headless=new --hide-scrollbars --window-size=$w,12000 \
    --screenshot=/tmp/sp-$w.png http://localhost:8000/
done
```

Check: the three space levels are visible; labels and content edges line up; nothing important
is grey; leaf appears only on green; only one pill; phone layout reads top to bottom with
project titles before their facts; it looks like none of: template, blog, terminal.
