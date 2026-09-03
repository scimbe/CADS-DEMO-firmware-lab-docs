---
title: How grounding, Bloom levels and Socratic hints work
order: 3
description: The three ideas behind the tutor, and why it asks questions and cites sources instead of chatting
---

## Grounding: answer only from indexed material

The tutor never answers a question from the language model's general knowledge alone. Before
it calls the model, it runs a BM25 search over an index of chunks: the content pack `firmware`
(the cads-zero documentation, 155 chunks) plus the course's own `sources/` and the project files
the step names (the foundations pack indexes about 70 project files, 2 884 chunks in total).
Passages above the course's threshold are handed to the model as context and are listed under
**Sources** with the answer. If nothing scores above the threshold, the tutor refuses with
*That is outside the indexed reference material for this course* rather than guessing.

The threshold is deliberately strict. A vague question such as "How do I flash?" can score
below it while "What does `st-flash write` refuse and why?" scores well. Course authors lower
`grounding.threshold` or add sources when a course is chattier than the firmware pack.

The same grounding feeds the grading of `question` tasks: the model sees the rubric, the
student's answer and retrieved passages and returns a verdict line. Without a language model,
the answer is stored and the student confirms it manually.

## Bloom levels: name what a step asks of you

Every step carries one level of Bloom's taxonomy: *remember*, *understand*, *apply*, *analyze*,
*evaluate*, *create*. The foundations course climbs deliberately: recall and comprehension in
M0–M1, application and analysis through the middle, evaluation and creation at the top. The
level is not decoration:

- `apply` and `create` steps change real firmware and check exactly that change (a file pattern,
  an ELF symbol, a flash, a serial line).
- `evaluate` steps ask for a defended judgement graded against a rubric.
- "Ask the tutor" sends the step's level with the question, so an answer to a *remember* step
  is a definition and an answer to an *analyze* step is a comparison.

The *Progress* view aggregates learning events per objective into a mastery estimate. Objectives
are ids from the platform curriculum or from the course's `curriculum.json`.

## Socratic hints: a question first, escalation later

When a check fails, the tutor does not show the solution. It shows the question the course
author wrote for that failure, for example *The build looks for a compiler before it does
anything. Where does it look?* Only then does *Show hint* reveal **Hint 1 of 3**. Each further
failure of the same task unlocks the next tier; the third tier is concrete. After that the tutor
says so and points you to the question box. Without an authored entry, three generic hints
apply (read the message, compare the pattern, open the referenced file).

The same mechanism reacts to what the board does. A `HardFault` or `configASSERT` on the
console, a failed flash or a debugger stop posts a context question into the panel: *Which
register tells you the faulting address, and how would you read it in the debugger?* Notes are
debounced (15 s per pattern, at most one check-in notification per minute) and never modal.

## Proactive, but quiet

Saving a file re-runs the step's local checks after two seconds, so a `fileMatches` task turns
green without a click. If the file belongs to the step and a language model is configured, the
tutor additionally asks for a short check-in on the change and shows it as a notification with
*Show* / *Later*. Everything the tutor learns about you is stored locally: the session in the
workspace, learning events in `~/.cads-tutor/events.sqlite`, the dialog log as JSONL. Nothing
leaves the container except the grounded prompt to the configured model.
