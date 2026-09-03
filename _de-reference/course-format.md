---
title: Kursformat
order: 4
description: course.json, Front-Matter-Felder der Steps, Link-Formen, Check-Typen und sokratische Trigger des Kurs-Pack-Formats v1
---

Der Vertrag ist `docs/SPEC.md` §3.3 im Repository; diese Seite listet die Felder.

## Verzeichnis

```
<course>/course.json
<course>/steps/<stepId>.en.md      Pflicht
<course>/steps/<stepId>.de.md      optional, Fallback en
<course>/assets/**                 Bilder (relativ im Markdown)
<course>/sources/**.md             optional: Grounding-Quellen für „Frag den Tutor“
<course>/curriculum.json           optional: neue Objectives (Array oder {track: [...]})
```

## course.json

| Feld | Typ | Bedeutung |
|---|---|---|
| `id` | string | eindeutige Kurs-ID; bei Kollision gewinnt die zuerst geladene Quelle |
| `version` | string | semantische Version |
| `schema` | number | `1` |
| `title`, `description` | `{de, en}` | in Tree und Panel angezeigt |
| `project.root` | string | Unterordner des Workspace; alle Step-Pfade sind relativ dazu |
| `project.repo` | string | informative URL |
| `prerequisites` | string[] | Kurs-IDs; alle ihre Steps müssen zuerst erledigt sein |
| `grounding.pack` | string | Content-Pack der tutor-platform (`firmware`) |
| `grounding.threshold` | number | BM25-Mindestscore; darunter verweigert der Tutor |
| `modules[]` | `{id, title{de,en}, steps[]}` | geordnete Module und Step-IDs |

## Front Matter eines Steps

| Feld | Typ | Bedeutung |
|---|---|---|
| `id` | string | entspricht dem Dateinamen |
| `title` | string | je Datei lokalisiert (`.en.md` / `.de.md`) |
| `bloom` | `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create` | Bloom-Stufe, als Badge angezeigt |
| `objectives` | string[] | Objective-IDs (Plattform-Curriculum oder `<course>/curriculum.json`) |
| `requires` | string[] | Step-IDs dieses Kurses, die erledigt sein müssen |
| `estimatedMinutes` | number | angezeigt als `~n min` |
| `links[]` | siehe unten | Zeile *Siehe auch* |
| `sources` | string[] | Projektdateien für das Grounding dieses Steps |
| `creates` | string[] | Symbole, die der Student erzeugt (erfüllt `symbolInElf`) |
| `tasks[]` | `{id, title, description?, check}` | die prüfbaren Aufgaben; `title` ist ein String oder `{de, en}` |
| `socratic[]` | `{trigger, question{de,en}, hints[3]{de,en}}` | Fragen und drei Hinweis-Stufen |

### Link-Formen

| Front Matter `links` | Im Markdown-Body |
|---|---|
| `{ step: m0-03-build }` | `[Text](step:m0-03-build)` |
| `{ file: "scripts/cads_env.sh", line: 30, title: {de,en} }` | `[Text](file:core/cads_hal.h#L42)` |
| `{ doc: "docs/how-to/flash.md" }` | `[Text](doc:docs/HARDWARE.md)` |
| `{ url: "https://…", title: "…" }` | gewöhnlicher Markdown-Link |

## Check-Typen

| `type` | Felder | Quelle |
|---|---|---|
| `board` | `state`: `connected` (Standard), `disconnected`, `halted`, `running` | Board-Bridge |
| `task` | `label` (aus tasks.json), `expectExitCode` (0), `timeoutMs` | VS-Code-Tasks |
| `build` | `label` **oder** `preset` (`cmake --preset P && cmake --build --preset P`) oder nichts (Einstellung `cadsTutor.buildTaskLabel`, Standard `CaDS: Build`) | VS-Code-Tasks |
| `fileMatches` / `fileNotMatches` | `file`, `pattern` (RegExp), `flags` | lokal; läuft auch beim Speichern |
| `symbolInElf` | `elf`, `symbol` | `arm-none-eabi-nm`, Fallback eingebauter ELF32-Parser |
| `flash` | `since`: `stepStart` (Standard), `sessionStart`, `any`; `file` | Bridge `getStatus().lastFlash` |
| `serialExpect` | `send`, `pattern`, `timeoutMs` (30 000) | Bridge `waitForSerial` |
| `debugStop` | `file`, `line`, `timeoutMs` (60 000) | Bridge-Event `debug-stop` und der Debug-Adapter-Tracker |
| `question` | `prompt{de,en}`, `rubric`, `bloom`, `minChars` (20) | Sprachmodell mit Grounding; ohne: manuelle Bestätigung |
| `manual` | `label` | Button *Als erledigt markieren* |
| `all` / `any` | `checks: [...]` | Komposition |

Ohne installierte Board-Bridge melden `board`, `flash` und `serialExpect` *Nicht verfügbar*,
was weder bestanden noch fehlgeschlagen ist und keine Hinweis-Stufe verbraucht.

## Sokratische Trigger

| `trigger` | Löst aus |
|---|---|
| `task:<taskId>:failed` | nach einem fehlgeschlagenen Check dieser Aufgabe; Hinweis-Stufe = Zahl der Fehlschläge, maximal 3 |
| `question:<taskId>:weak` | nach einer als schwach bewerteten Antwort |
| `event:hardfault`, `event:assert`, `event:result-fail` | serielle Muster `HardFault`, `configASSERT`, `RESULT: FAIL` |
| `event:flash-failed`, `event:debug-stop` | Bridge-Events |
| `*` | jeder Fehlschlag dieses Steps ohne spezifischeren Eintrag |

Vom Autor geschriebene Einträge haben Vorrang vor den drei generischen Hinweisen des Tutors.

## Ladereihenfolge und Neuladen

1. Extensions mit `contributes.cadsTutorCourses: [{ "path": "courses/<dir>" }]`.
2. `/opt/cads-tutor/courses/*`, `~/.cads-tutor/courses/*`, `<workspace>/.cads-tutor/courses/*`.
3. Einstellung `cadsTutor.extraCourseDirs`.

Änderungen erkennt ein File-Watcher; **CaDS Tutor: Kurse neu laden / Reload courses** erzwingt
das Neuladen. Fehler stehen im Output-Channel *CaDS Tutor* mit Datei und Feldpfad.

## Validator

```bash
scripts/validate-courses.py /path/to/cads-zero --nm /path/to/arm-none-eabi-nm
```
