---
title: Course format
order: 4
description: course.json, step front matter fields, link forms, check types and Socratic triggers of the course pack format v1
---

The contract is `docs/SPEC.md` §3.3 in the repository; this page lists the fields.

## Directory

```
<course>/course.json
<course>/steps/<stepId>.en.md      required
<course>/steps/<stepId>.de.md      optional, falls back to en
<course>/assets/**                 images (relative in Markdown)
<course>/sources/**.md             optional grounding sources for "Ask the tutor"
<course>/curriculum.json           optional new objectives (array or {track: [...]})
```

## course.json

| Field | Type | Meaning |
|---|---|---|
| `id` | string | unique course id; first loaded source wins on collision |
| `version` | string | semantic version |
| `schema` | number | `1` |
| `title`, `description` | `{de, en}` | shown in tree and panel |
| `project.root` | string | sub-folder of the workspace; all step paths are relative to it |
| `project.repo` | string | informational URL |
| `prerequisites` | string[] | course ids; all their steps must be done first |
| `grounding.pack` | string | tutor-platform content pack (`firmware`) |
| `grounding.threshold` | number | BM25 minimum score; below it the tutor refuses |
| `modules[]` | `{id, title{de,en}, steps[]}` | ordered modules and step ids |

## Step front matter

| Field | Type | Meaning |
|---|---|---|
| `id` | string | equals the file name |
| `title` | string | localised by file (`.en.md` / `.de.md`) |
| `bloom` | `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create` | Bloom level, shown as a badge |
| `objectives` | string[] | objective ids (platform curriculum or `<course>/curriculum.json`) |
| `requires` | string[] | step ids of this course that must be done |
| `estimatedMinutes` | number | shown as `~n min` |
| `links[]` | see below | *See also* row |
| `sources` | string[] | project files used for grounding this step |
| `creates` | string[] | symbols the student creates (satisfies `symbolInElf`) |
| `tasks[]` | `{id, title, description?, check}` | the checkable tasks; `title` is a string or `{de, en}` |
| `socratic[]` | `{trigger, question{de,en}, hints[3]{de,en}}` | questions and three hint tiers |

### Link forms

| Front matter `links` | In the Markdown body |
|---|---|
| `{ step: m0-03-build }` | `[text](step:m0-03-build)` |
| `{ file: "scripts/cads_env.sh", line: 30, title: {de,en} }` | `[text](file:core/cads_hal.h#L42)` |
| `{ doc: "docs/how-to/flash.md" }` | `[text](doc:docs/HARDWARE.md)` |
| `{ url: "https://…", title: "…" }` | ordinary Markdown link |

## Check types

| `type` | Fields | Source |
|---|---|---|
| `board` | `state`: `connected` (default), `disconnected`, `halted`, `running` | board bridge |
| `task` | `label` (from tasks.json), `expectExitCode` (0), `timeoutMs` | VS Code tasks |
| `build` | `label` **or** `preset` (`cmake --preset P && cmake --build --preset P`) or nothing (setting `cadsTutor.buildTaskLabel`, default `CaDS: Build`) | VS Code tasks |
| `fileMatches` / `fileNotMatches` | `file`, `pattern` (RegExp), `flags` | local; also runs on save |
| `symbolInElf` | `elf`, `symbol` | `arm-none-eabi-nm`, fallback built-in ELF32 parser |
| `flash` | `since`: `stepStart` (default), `sessionStart`, `any`; `file` | bridge `getStatus().lastFlash` |
| `serialExpect` | `send`, `pattern`, `timeoutMs` (30 000) | bridge `waitForSerial` |
| `debugStop` | `file`, `line`, `timeoutMs` (60 000) | bridge event `debug-stop` and the debug adapter tracker |
| `question` | `prompt{de,en}`, `rubric`, `bloom`, `minChars` (20) | language model with grounding; without one: manual confirmation |
| `manual` | `label` | button *Mark as done* |
| `all` / `any` | `checks: [...]` | composition |

Without an installed board bridge, `board`, `flash` and `serialExpect` report *Unavailable*,
which is neither a pass nor a failure and consumes no hint tier.

## Socratic triggers

| `trigger` | Fires |
|---|---|
| `task:<taskId>:failed` | after a failed check of that task; hint tier = number of failures, capped at 3 |
| `question:<taskId>:weak` | after a question answer graded weak |
| `event:hardfault`, `event:assert`, `event:result-fail` | serial patterns `HardFault`, `configASSERT`, `RESULT: FAIL` |
| `event:flash-failed`, `event:debug-stop` | bridge events |
| `*` | any failure of this step without a more specific entry |

Authored entries take precedence over the tutor's generic three hints.

## Load order and reload

1. Extensions with `contributes.cadsTutorCourses: [{ "path": "courses/<dir>" }]`.
2. `/opt/cads-tutor/courses/*`, `~/.cads-tutor/courses/*`, `<workspace>/.cads-tutor/courses/*`.
3. Setting `cadsTutor.extraCourseDirs`.

Changes are picked up by a file watcher; **CaDS Tutor: Kurse neu laden / Reload courses** forces
a reload. Errors are listed in the output channel *CaDS Tutor* with file and field path.

## Validator

```bash
scripts/validate-courses.py /path/to/cads-zero --nm /path/to/arm-none-eabi-nm
```
