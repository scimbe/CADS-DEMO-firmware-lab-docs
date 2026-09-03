---
title: Write your own course
order: 5
description: Create a course pack (course.json plus Markdown steps with front matter), load it into the tutor and validate it before you commit
---

A course is a directory of data: one `course.json`, one Markdown file per step and language, and
optional assets and sources. The tutor runtime is course-independent, so a new course needs no
code. The complete schema is in [Course format]({{ '/en/reference/course-format/' | relative_url }});
this page is the working path.

## 1. Start from the example

The extension repository ships a fixture pack `extensions/cads-tutor/courses/_example` and the two
real packs under `courses/`. Copy one of them:

```
my-course/
  course.json
  steps/
    m0-01-hello.en.md      required (front matter + Markdown)
    m0-01-hello.de.md      optional; falls back to en
  assets/                  images, referenced relatively from the Markdown
  sources/                 optional Markdown for "Ask the tutor" grounding
  curriculum.json          optional: new learning objectives
```

## 2. Write course.json

```json
{
  "id": "my-course", "version": "1.0.0", "schema": 1,
  "title": { "de": "Mein Kurs", "en": "My course" },
  "description": { "de": "…", "en": "…" },
  "project": { "root": "cads-zero", "repo": "https://github.com/scimbe/cads-zero" },
  "prerequisites": [],
  "grounding": { "pack": "firmware", "threshold": 8.0 },
  "modules": [
    { "id": "m0", "title": { "de": "Start", "en": "Start" }, "steps": ["m0-01-hello"] }
  ]
}
```

`project.root` is a sub-folder of the workspace; if it does not exist the workspace itself is the
project root. All `file`, `elf` and `doc` paths in steps are relative to it and must not leave it.
`prerequisites` lists other course ids; every step stays locked until those courses are complete.

## 3. Write a step

```yaml
---
id: m0-01-hello                    # must equal the file name
title: Say hello
bloom: apply                       # remember|understand|apply|analyze|evaluate|create
objectives: [firmware-how-to-build]
requires: []                       # step ids of this course
estimatedMinutes: 10
links:
  - { file: "apps/desktop/cads_desktop.c", line: 24 }
  - { doc: "docs/HARDWARE.md" }
tasks:
  - id: edit
    title: Change the splash text
    check: { type: fileMatches, file: "apps/desktop/cads_desktop.c", pattern: "Hello ITS" }
  - id: build
    title: Firmware builds
    check: { type: task, label: "CaDS: Build", expectExitCode: 0 }
socratic:
  - trigger: "task:build:failed"
    question: { en: "Which line did the compiler name first?", de: "Welche Zeile nennt der Compiler zuerst?" }
    hints:
      - { en: "Read the first error, not the last line.", de: "Lies den ersten Fehler, nicht die letzte Zeile." }
      - { en: "…", de: "…" }
      - { en: "…", de: "…" }
---
## Learning goal

Markdown body (GFM). Links: [next](step:m0-02-next), [source](file:core/cads_hal.h#L42), [doc](doc:docs/HARDWARE.md).
```

Rules the real packs settled on:

- Quote titles containing `: ` in YAML.
- The task list of the `.en.md` file is authoritative; the `.de.md` provides German titles,
  descriptions and body. Keep the front matter identical otherwise.
- A step without tasks counts as done as soon as it is opened.
- `symbolInElf` needs a symbol that exists after the student's build. If the student creates
  it, declare it under `creates:` so the check passes once they build.
- `step:` links stay within one course; cross-course references use `doc:`/`file:` and prose.
- Prefer automatic checks; use `manual` only where no source edit exists to match.

The three `hints` are the tiers shown after the first, second and third failure.

## 4. Load it

The tutor merges courses from, in this order (first wins on id collision):

1. Extensions contributing `contributes.cadsTutorCourses: [{ "path": "courses/<dir>" }]` in
   their `package.json` (a real plugin, installable as VSIX).
2. `/opt/cads-tutor/courses/*` (image), `~/.cads-tutor/courses/*` (user),
   `<workspace>/.cads-tutor/courses/*` (project).
3. The setting `cadsTutor.extraCourseDirs`.

For development, put the directory under `<workspace>/.cads-tutor/courses/my-course`. Changes to
`course.json` and the step files are reloaded automatically (a file watcher); the command
**CaDS Tutor: Kurse neu laden / Reload courses** forces it. Load errors appear in the output
channel **CaDS Tutor** with file and field path.

## 5. Validate

The repository has a validator that checks schema, cross-links, repository paths, ELF symbols
against the built ELF, bilingual coverage and Bloom levels:

```bash
scripts/validate-courses.py /path/to/cads-zero --nm /path/to/arm-none-eabi-nm
```

It runs on standard-library Python and uses PyYAML when available. Run it before every commit.

## 6. Grounding for "Ask the tutor"

`grounding.pack` selects the platform content pack (`firmware`: the cads-zero docs, 155 chunks).
Files under `sources/**.md` are chunked and indexed in addition and cited as
`<course title>`. The BM25 threshold of the firmware pack (8.0) is strict; a course can lower
`grounding.threshold` or ship its own sources. Objectives that the platform does not know are
allowed but get no proactive check-in until you define them in `<course>/curriculum.json`.
