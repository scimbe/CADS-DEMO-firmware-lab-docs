---
title: Learning with the tutor
order: 5
description: Courses, automatic checks, "Ask the tutor", hint tiers, the language switch and your progress
---

The tutor is not a chat bot bolted onto an editor. It is a course runtime: it knows which step you
are on, checks your work against the real repository and the real board, asks questions instead of
handing out solutions, and answers only from indexed reference material. This tutorial shows each
of those parts once.

## 1. Courses

Two course packs ship with the image:

| Course | Kind | Scope |
|---|---|---|
| CaDS Zero – Foundations | required, 41 steps, about 10 h | M0 orientation → M1 architecture → M2 memory-mapped I/O → M3 debugging → M4 FreeRTOS → M5 display and GUI → M6 storage and configuration → M7 networking → M8 quality |
| CaDS Zero – Projects | elective, 6 project tasks | your own app, a network tool, a configuration option, a test with golden image, a driver extension, a performance measurement |

Every foundations step requires the one before it, so the tree unlocks one step at a time. The
project tasks are independent; they name the foundations steps they assume in prose. Each step
carries a Bloom level (*remember* … *create*), a learning objective and a time estimate.

## 2. Checks

Tasks in a step are verified, not ticked. The check types you will meet:

- **File checks** run when you save (`fileMatches`, `fileNotMatches`) and give feedback within
  two seconds, without pressing anything.
- **Task and build checks** run a lab task, for example *CaDS: Build*, and expect exit code 0.
- **ELF checks** (`symbolInElf`) look up a symbol in `build/itsboard/cads-zero.elf` with
  `arm-none-eabi-nm`.
- **Board checks** (`board`, `flash`, `serialExpect`, `debugStop`) ask the board bridge: is the
  board connected, was there a flash since the step started, did the console print a pattern,
  did the debugger stop at file and line. Without a connected board they report *Unavailable*
  rather than *Failed*.
- **Questions** (`question`) take a free-text answer, graded against a rubric by the language
  model, grounded in the course sources. Without a language model you confirm the answer yourself.
- **Manual** tasks have a *Mark as done* button.

*Check* runs one task, *Run all checks* the whole step. A passing step shows *Step completed!*
and a notification names what got unlocked.

## 3. Hints, in three tiers

When a check fails, the panel shows a question first, for example after a failed build:
*The build looks for a compiler before it does anything. Where does it look, and did that resolve
to an arm-none-eabi-gcc?* Below it, *Show hint* reveals **Hint 1 of 3**. The second failure
unlocks hint 2, the third hint 3. Hint 3 is concrete; after it the panel says *No further hints –
ask the tutor a concrete question.* Course authors write these hints per task; where none exist
the tutor falls back to three generic ones.

<figure>
<img src="{{ '/assets/12-hint-tier.png' | relative_url }}" alt="Tutor panel with the first hint tier opened under a task: Hinweis 1 von 3 with the generic first hint">
<figcaption>Hint 1 of 3 after the first failed check. The next tier unlocks with the next failure.</figcaption>
</figure>

The same mechanism reacts to events: a failed flash, a debugger stop, a `HardFault` or
`configASSERT` on the console. The tutor posts a question in the panel, never a modal dialog.

## 4. Ask the tutor

<figure>
<img src="{{ '/assets/09-ask-tutor.png' | relative_url }}" alt="Tutor panel, German, with the question box filled and the answer area listing the grounded sources">
<figcaption>"Frag den Tutor" on a deployment without a language model: the box explains that the model is not configured and still lists the sources it found.</figcaption>
</figure>

The text box at the bottom of every step sends your question together with the step context to
the language model of the deployment. Before it answers, the tutor retrieves passages from the
indexed sources (the cads-zero documentation plus the course's own `sources/`) with a BM25
search. If nothing scores above the course threshold, you get a refusal:
*That is outside the indexed reference material for this course – rephrase, or ask about the
current step.* That is intended. Short questions such as "How do I flash?" can fall under the
threshold; ask about a concrete file, register or symptom instead.

Answers cite their **Sources**. On a deployment without a language model the box says so and
still shows the sources it would have used, which is often enough to find the answer yourself.

## 5. Proactive check-ins

When you save a file that the current step references, and a language model is configured, the
tutor asks it for a short check-in on your change. The result arrives as a notification
*CaDS Tutor has feedback on your last save* with *Show* / *Later*, at most once per minute.
Turn this off with the setting `cadsTutor.checkInOnSave`.

## 6. Language

<figure>
<img src="{{ '/assets/08-tutor-panel-german.png' | relative_url }}" alt="Tutor panel in German: Willkommen im CaDS-Firmware-Labor, Aufgaben with Prüfen buttons">
<figcaption>Every step exists in English and German. The switch in the panel header changes panel, tree and status bar.</figcaption>
</figure>

The panel header has a *Deutsch* / *English* switch; the command palette offers
**CaDS Tutor: Sprache wählen / Set language**. The choice is stored in your session. By default
the tutor follows the VS Code display language (`cadsTutor.language: auto`).

## 7. Progress

<figure>
<img src="{{ '/assets/10-progress-view.png' | relative_url }}" alt="Progress view in the CaDS Tutor side bar listing learning objectives with mastery">
<figcaption>The Progress view: mastery per learning objective, derived from your learning events.</figcaption>
</figure>

Two things are stored, both inside the container:

- `<workspace>/.cads-tutor/session.json`: current course and step, task status, your answers.
- `~/.cads-tutor/events.sqlite`: learning events (checks passed and failed, questions asked),
  from which the *Progress* view derives mastery per objective.

Both live in your workspace volume and survive a container restart. To start over, run
**CaDS Tutor: Fortschritt zurücksetzen / Reset progress**; it clears the session and keeps the
learning events (see [Reset your progress]({{ '/en/how-to/reset-progress/' | relative_url }})).

## Where you are now

You know every control of the tutor. From here the course carries you: open the next step and
work through it. When something behaves differently from these pages, that is worth an issue.
