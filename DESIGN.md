# DESIGN.md – stephan-poetschner.at

Read this before touching `portfolio/templates/index.html` or `portfolio/static/css/main.css`.
Design name: **"Stille in Feld-Farben"** (chosen 2026-11-05 from mock-ups in `mockups/`:
layout of C "Stille", colours of B "Feld"). Made bolder on 2026-11-06 (mock-up `f.html`):
strong green signal, 300/700 weight contrast, serif italic for key words.

Cross-site principles, the "must not look like" list and the redesign process live in
`../pitches/design.md`; this file is how this site applies them.

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

No mood photography. The portrait appears twice: small and round (56px, a tight head crop `me-face-{56,84,112,168}.jpg` via `srcset`, one file per pixel density so the browser never rescales) at the top, larger in
the contact section (`me-{144…720}.jpg`, one width per density 1x/1.5x/2x/3x, via `srcset`/`sizes`, generated from `raw/fotos/_MG_2972 (1).jpg`), where it puts a real person next to the invitation.

## Principles (and why)

1. **Contrast, not variety.** Few type sizes, far apart: a huge statement, large names, normal
   body text, small meta. Nothing in between. A page where everything is medium has no priority.
2. **Weight contrast, plus one italic voice.** The statement is light (300) with its key phrase
   in 700 and a signal underline. Instrument Sans carries everything; single key words (`<i>`)
   are set in Instrument Serif Italic, 1.12em (1.15em in the statement, Vienna lead, contact
   title). Use it for one or two words per heading, never for sentences or running text.
3. **Three levels of space, clearly different.** `--space-in` (inside a group) ≪ `--space-group`
   (between items) ≪ `--space-section` (between sections). Proximity shows what belongs together;
   don't add rules or boxes to do space's job.
4. **Facts are design elements.** Client names are set large (600); figures are huge and in signal green.
   Proof is what builds trust, so proof gets the visual weight, not adjectives.
5. **Label column + content column.** From 1000px each section has a small green label on the left
   (¼) and content on the right (¾). This asymmetry is the page's structure; everything lines up
   on the content edge. Running text never exceeds `--measure` (38rem).
6. **Colour as fields, one accent, one signal.** Cream ground; deep green is the accent (labels,
   bands, footer). Strong green `--signal` marks: the statement's key phrase, link underlines, the
   dot before each label, `<mark>` stripes in the main quote, client-row hover, pill hover. On
   cream it is never text (too light); on green, `--signal-on-green` may be text (figures,
   labels). Full-width bands give rhythm: green for Django-Vienna, sand for testimonials, green
   footer.
7. **One call to action.** The ink pill "Kennenlerngespräch vereinbaren" appears once, at the
   top. The contact section at the end uses large plain links, not a second button.
8. **Vienna, quietly.** Location shows in words (role line, "auf einen Kaffee in Wien") and in one
   signal-green line drawing of the Riesenrad in the footer. No other illustrations, no skyline photos,
   no red-white-red.
9. **Important things are dark.** Names, authors, client names in `--ink`. `--muted` only for
   context (years, captions, descriptions of offers). Nothing below 4.5:1.

## Tokens (`:root` in main.css)

| Token | Value | Use |
|---|---|---|
| `--paper` | `#faf7f0` | page ground (cream) |
| `--ink` | `#1b1d1a` | text (16:1) |
| `--muted` | `#5f5e57` | secondary text (6.2:1; 5.2:1 on sand) |
| `--hair` | `#ddd5c4` | thin dividers inside lists |
| `--green` | `#1d3b31` | the accent: labels, bands, footer |
| `--signal` | `#2fd36b` | lines and fills on cream (**not text**): key-phrase underline, link underlines, label dots, `<mark>` |
| `--signal-on-green` | `#4be38a` | figures, labels, links, Riesenrad, focus ring **on green** (7:1) |
| `--on-green` / `--on-green-muted` | `#eef0e6` / `#a9bdb2` | text on green (10:1 / 6:1) |
| `--sand` | `#e9e2d3` | testimonial band |

Type (Instrument Sans in `static/fonts/instrument-sans/`, Instrument Serif Italic for `<i>` in
`static/fonts/instrument-serif/`; both self-hosted, OFL):

| Token | Size | Use |
|---|---|---|
| `--fs-xl` | 2.3–6rem, capped at 8.5vh so the pill stays above the fold | statement, "Projekt besprechen?" (figures use their own 3–6rem) |
| `--fs-lg` | 1.6–2.75rem | client names, offers, project titles, main quote |
| `--fs-md` | 1.25rem | how-I-work headings, secondary quotes |
| `--fs-base` | 1.125rem / 1.55 | running text |
| `--fs-sm` | .9375rem | years, captions, project facts |

Large sizes use negative tracking (−.03 to −.05em) and tight leading (1–1.1).
Weights: 300 for the statement, 600 for names and titles, 700 for the key phrase and labels.

## Page order and components

1. **Top** – portrait + name + "Django-Entwickler in Wien, selbständig seit 2008"; statement;
   pill + "Kostenlos. Ich melde mich meist am selben Tag."
2. **Für wen ich gearbeitet habe** – `.client-list`: name (large) · one line · years.
   Names only for clients that may be named (`profile.md`).
3. **Django-Vienna** (green band) – the strongest differentiator after the clients: founded 2013,
   organised for years, a network for referrals. Lead sentence in `--fs-lg`; two short paragraphs
   (founding story with co-founders Anton Pirker and Florian Demmer, linked; then what it means
   for the client, hedged: "kenne ich wahrscheinlich jemanden"); three
   signal-green figures (Treffen, Mitglieder, Bewertung), link to meetup.com. Wording is tense-proof
   ("gegründet", "organisiert") because the group ends in November 2026; never "Community
   aufgebaut".
4. **Was ich für dich tun kann** – the three offers in the order of `positioning.md`.
5. **Wie ich arbeite** – three values, three columns.
6. **Was Kunden sagen** (sand band) – one large quote, two smaller, author in ink.
7. **Projekte im Detail** – from `content/projects/*.md`; facts (Kunde/Zeitraum/Technik) in the
   label column, title + text right. Markdown `#` headings render as small bold labels.
8. **Was erfolgreiche Teams ausmacht** – prose.
9. **Projekt besprechen?** – portrait in the label column (above on phones), large heading,
   email / phone / LinkedIn as large links, offer to meet in person.
10. **Footer** (green) – Riesenrad mark + "Aus Wien.", imprint and privacy (legally required,
   keep the content). Privacy is a `<details>`: on desktop its text opens as a full-width row
   below the three bottom-aligned columns, so nothing above it moves when it opens.

Favicon: italic "p" (Pötschner, Python), `--ink` on `--signal` (a dark tile vanished among other
tabs). A scaled serif glyph blurs at 16px, so small sizes get hand-drawn pixel art:
`favicon.svg` holds both drawings and switches with `@media (max-width: 24px)` inside the SVG
(pixel "p" with `crispEdges` for tabs, Instrument Serif glyph, thickened with a stroke, above).
`favicon.ico` is the fallback (pixel 16px, glyph 32/48px); `apple-touch-icon.png` is 180px, square.
To change the pixel "p", edit the 16×16 grid in both the SVG and the ICO.

Adding a section: `<section class="section">` with `<h2 class="label">` first; add `band
band-green` or `band band-sand` only if the rhythm needs it (never two bands in a row).

## Copy

Copy rules live in `../pitches/copy.md`, facts in `../pitches/profile.md`. Django-Vienna figures
(59 Treffen, 838 Mitglieder, 4,9/5 bei 166 Bewertungen) are from 2026-11.

## Checking changes

Run `./runserver.py` (restart it after changing `content/`, it loads Markdown at startup), then:

```bash
for w in 1440 390; do
  google-chrome --headless=new --hide-scrollbars --window-size=$w,12000 \
    --screenshot=/tmp/sp-$w.png http://localhost:8000/
done
```

Check: the three space levels are visible; labels and content edges line up; nothing important
is grey; signal is never text on cream; serif italic only on single words; the pill is visible
without scrolling at 1280×720 and 375×667; only one pill; phone layout reads top to bottom with
project titles before their facts; it looks like none of: template, blog, terminal.

## References

Where the direction came from, for when the design needs to evolve:

- Books: Matthew Butterick, *Practical Typography* (free online); Adam Wathan & Steve Schoger,
  *Refactoring UI*; Josef Müller-Brockmann, *Grid Systems in Graphic Design* (asymmetric grids,
  contrast); Jost Hochuli, *Detail in Typography*.
- Sites built from type, not images: type foundries (klim.co.nz, commercialtype.com,
  grillitype.com, abcdinamo.com), ia.net, press.stripe.com, oxide.computer.
- Galleries: typewolf.com, fontsinuse.com, siteinspire.com (filter "Typographic"),
  minimal.gallery.
- Rejected directions and why: `mockups/README.md` (A Raster, B Feld, C Stille) and the
  "must not look like" list above.
