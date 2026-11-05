# CLAUDE.md

Stephan's portfolio site (http://stephan-poetschner.at): Frozen-Flask, static output.
Its job is to convince people who already heard Stephan's name (meetup, network, referral).

## Before changing copy

- `../pitches/positioning.md`: target clients, offers (order, what is not promoted), role of this site.
- `../pitches/profile.md`: the only source for facts about Stephan. Add new facts there first.
- `../pitches/copy.md`: copy principles and the checklist to run before publishing.

Copy is German, informal "du"; common English IT terms are fine. No hourly rate.

## Structure

- `portfolio/templates/index.html`: header, about, offers, "Warum mit mir arbeiten?", testimonials
- `portfolio/content/projects/*.md`: one file per project, sorted by `date` (newest first)
- `portfolio/static/`: CSS, images

## Commands

```bash
./runserver.py   # dev server at http://localhost:8000/
./freeze.py      # build into ./build/
./deploy.sh      # freeze + rsync to the server; only with Stephan's explicit OK
```

`build/` uses absolute `/static/` paths: serve it over HTTP (e.g. `python3 -m http.server`
in `build/`) to check it, `file://` shows it unstyled.
