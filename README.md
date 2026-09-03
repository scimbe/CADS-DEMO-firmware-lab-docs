# CADS-DEMO-firmware-lab-docs

User documentation for the [CaDS Firmware Lab](https://github.com/scimbe/CADS-DEMO-firmware-lab):
a browser IDE (code-server) in which students build, flash and debug the
[CaDS Zero](https://github.com/scimbe/cads-zero) firmware on an ITSboard (STM32F429ZI) that is
plugged into their own computer, guided by a course tutor. Published with GitHub Pages
(`.github/workflows/pages.yml`).

Developer documentation (image, extensions, courses, multi-user stack) lives in the monorepo
under `docs/`; operator runbooks live in the private ops-docs repository. This site is for
students, course authors and, for the image's environment, operators.

## Structure

[Diátaxis](https://diataxis.fr) in two languages. Every page exists in English and German with
the **same slug**, because the layout's language toggle replaces `/en/` with `/de/` in the URL.

| Collection | Path | Content |
|---|---|---|
| `_en-tutorials`, `_de-tutorials` | `/en/tutorials/<slug>/`, `/de/tutorials/<slug>/` | first session, build and flash, debug with F5, serial console, learning with the tutor |
| `_en-how-to`, `_de-how-to` | `/en/how-to/<slug>/`, … | connect the board, reconnect after replug, host tests, RAM budget, write a course, switch language, reset progress, troubleshooting |
| `_en-reference`, `_de-reference` | `/en/reference/<slug>/`, … | tasks and launch configurations, bridge ports, shims, course format, keyboard shortcuts, environment variables |
| `_en-explanation`, `_de-explanation` | `/en/explanation/<slug>/`, … | board in the browser, why cads-zero, tutor pedagogy, safety rules, limits |

Landing pages: `index.md` (language chooser), `en/index.md`, `de/index.md` (entry points for
students, course authors, operators); section indexes under `en/<section>/index.md` and
`de/<section>/index.md` list their collection sorted by `order`.

## Adding a page

Create `_<lang>-<section>/<slug>.md` in both languages with this front matter only:

```yaml
---
title: Page title
order: 3
description: One sentence, shown on the section index card.
---
```

`layout`, `section` and `lang` come from the defaults in `_config.yml`. Link to other pages with
`{{ '/en/how-to/<slug>/' | relative_url }}`. Images go flat into `assets/`, numbered
(`00-login.png`, …), and are embedded as

```html
<figure>
<img src="{{ '/assets/04-task-picker.png' | relative_url }}" alt="…">
<figcaption>…</figcaption>
</figure>
```

## Facts and screenshots

Every statement on this site is taken from the specification, the extension sources or a
verified run; nothing is described from memory. Screenshots are captured with headless Chromium
(Playwright) against a container started from the production image, for example:

```sh
docker run -d --name docs-shot -p 127.0.0.1:8087:8080 -e PASSWORD=docs \
  ghcr.io/scimbe/cads-firmware-lab:next-8a20ec9
```

Pages that describe the board paths (flash, debug, console) say so where a screenshot with real
hardware is still to come.

## Build locally

With Ruby 3.x and Bundler:

```sh
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000/CADS-DEMO-firmware-lab-docs/
```

Without a local Ruby, use a container:

```sh
docker run --rm -v "$PWD":/srv/jekyll -w /srv/jekyll ruby:3.3 \
  sh -c 'bundle install && bundle exec jekyll build --trace'
```

`scripts/check-links.py` validates front matter and every internal link and image reference in
the source (no Jekyll needed):

```sh
python3 scripts/check-links.py
```

## Deploy

`.github/workflows/pages.yml` builds the site with Jekyll on every push to `main` and deploys it
to GitHub Pages (source: GitHub Actions). Pages must be enabled once in the repository settings.
