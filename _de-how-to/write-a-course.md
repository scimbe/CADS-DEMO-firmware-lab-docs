---
title: Eigenen Kurs schreiben
order: 5
description: Ein Kurs-Pack anlegen (course.json plus Markdown-Steps mit Front Matter), in den Tutor laden und vor dem Commit validieren
---

Ein Kurs ist ein Verzeichnis aus Daten: eine `course.json`, eine Markdown-Datei je Step und
Sprache sowie optionale Assets und Quellen. Die Tutor-Runtime ist kursunabhängig, ein neuer Kurs
braucht also keinen Code. Das vollständige Schema steht im
[Kursformat]({{ '/de/reference/course-format/' | relative_url }}); diese Seite ist der Arbeitsweg.

## 1. Vom Beispiel ausgehen

Das Extension-Repository liefert ein Fixture-Pack `extensions/cads-tutor/courses/_example` und
die zwei echten Packs unter `courses/`. Kopiere eines davon:

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

## 2. course.json schreiben

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

`project.root` ist ein Unterordner des Workspace; existiert er nicht, gilt der Workspace selbst
als Projekt-Root. Alle `file`-, `elf`- und `doc`-Pfade in Steps sind relativ dazu und dürfen ihn
nicht verlassen. `prerequisites` listet andere Kurs-IDs; jeder Step bleibt gesperrt, bis diese
Kurse abgeschlossen sind.

## 3. Einen Step schreiben

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

Regeln, auf die sich die echten Packs geeinigt haben:

- Titel mit `: ` in YAML quoten.
- Die Aufgabenliste der `.en.md` ist maßgeblich; die `.de.md` liefert deutsche Titel,
  Beschreibungen und Body. Das Front Matter ansonsten identisch halten.
- Ein Step ohne Aufgaben gilt als erledigt, sobald er geöffnet wurde.
- `symbolInElf` braucht ein Symbol, das nach dem Build des Studierenden existiert. Erzeugt es
  der Studierende selbst, deklariere es unter `creates:`, damit der Check besteht, sobald gebaut
  wurde.
- `step:`-Links bleiben innerhalb eines Kurses; kursübergreifende Verweise nutzen `doc:`/`file:`
  und Fließtext.
- Bevorzuge automatische Checks; nutze `manual` nur, wo keine passende Quelländerung existiert.

Die drei `hints` sind die Stufen, die nach dem ersten, zweiten und dritten Fehlschlag gezeigt
werden.

## 4. Laden

Der Tutor vereinigt Kurse aus diesen Quellen, in dieser Reihenfolge (bei gleicher ID gewinnt die
erste):

1. Extensions, die in ihrer `package.json` `contributes.cadsTutorCourses: [{ "path":
   "courses/<dir>" }]` beitragen (ein echtes Plugin, als VSIX installierbar).
2. `/opt/cads-tutor/courses/*` (Image), `~/.cads-tutor/courses/*` (Nutzer),
   `<workspace>/.cads-tutor/courses/*` (Projekt).
3. Die Einstellung `cadsTutor.extraCourseDirs`.

Zur Entwicklung lege das Verzeichnis unter `<workspace>/.cads-tutor/courses/my-course` ab.
Änderungen an `course.json` und den Step-Dateien werden automatisch neu geladen (ein
FileSystemWatcher); der Befehl **CaDS Tutor: Kurse neu laden / Reload courses** erzwingt es.
Ladefehler erscheinen im Output-Channel **CaDS Tutor** mit Datei und Feldpfad.

## 5. Validieren

Das Repository hat einen Validator, der Schema, Querverweise, Repository-Pfade, ELF-Symbole
gegen die gebaute ELF, zweisprachige Abdeckung und Bloom-Stufen prüft:

```bash
scripts/validate-courses.py /path/to/cads-zero --nm /path/to/arm-none-eabi-nm
```

Er läuft auf Standardbibliotheks-Python und nutzt PyYAML, wenn verfügbar. Führe ihn vor jedem
Commit aus.

## 6. Grounding für „Frag den Tutor“

`grounding.pack` wählt das Content-Pack der Plattform (`firmware`: die cads-zero-Docs, 155
Chunks). Dateien unter `sources/**.md` werden zusätzlich gechunkt und indiziert und als
`<Kurstitel>` zitiert. Die BM25-Schwelle des Firmware-Packs (8.0) ist streng; ein Kurs kann
`grounding.threshold` senken oder eigene Quellen mitliefern. Lernziele, die die Plattform nicht
kennt, sind erlaubt, bekommen aber kein proaktives Check-in, bis du sie in
`<course>/curriculum.json` definierst.
