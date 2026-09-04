---
layout: default
title: When a check will not pass (JavaScript)
lang: en
permalink: /en/javascript/when-a-check-fails/
---

# When a check will not pass

A red test is the normal state of an exercise before you solve it. This page is for the case where
you have tried and it still will not go green.

## First: read the output, not the colour

Node's test runner names the assertion that failed, what it expected and what it actually got.
That comparison is usually the whole answer. Several steps exist only so that you meet a
particular failure under controlled conditions and learn to read it.

Two shapes of failure are worth telling apart:

- **A test failed.** Your code ran and produced the wrong value. The expected-against-actual lines
  tell you which.
- **The test file could not be loaded at all.** Then nothing in it ran. The usual cause is a
  missing or misspelled export, which is exactly what some exercises ask you to add. The message
  says the file could not be loaded rather than naming a single test.

## The hint ladder

Every task has hints in three tiers. Ask for them in order:

1. **A question** that points at the place to look, without saying what is wrong.
2. **A narrower hint** naming the concept or the rule that applies.
3. **A concrete direction**, though never the line to paste.

The tiers exist so that you keep the part of the work that produces the learning. If tier three
still leaves you stuck, tell your teacher: it usually means the step assumes something it never
taught.

## The five failures that are not your code

| Symptom | Cause | Fix |
|---|---|---|
| `Cannot find module …` | terminal one level above the exercises | `cd ~/workspace/javascript-foundations` |
| **No matching results** in the palette | palette is in file mode | type `>` before the command name |
| Command seems to hang, nothing prints | it is still running | wait for the prompt to come back |
| Output missing entirely | you are looking at Problems or Output | switch to the **Terminal** tab |
| `node` itself not found | runtime missing in this container | an environment fault — report it, you cannot fix it in the editor |

## When the tutor asks you a question instead of checking

Some tasks want an explanation rather than a command. The tutor grades your reasoning against a
rubric — and it will tell you what does **not** pass, not just what does. A keyword is not an
answer; two or three sentences that connect cause and effect are.

If your installation has no language model configured, the tutor shows you that rubric and asks
you to check yourself. Be honest with it: the result is recorded as self-reported, and the point
of the exercise is your own understanding, not the tick.

## Still stuck

Ask the tutor. It answers from the indexed course material and the runtime documentation, and it
will refuse a question it cannot ground in a source rather than inventing an answer. Ask in German
or English, whichever you prefer.

## Related

- [Running commands and tasks]({{ '/en/javascript/working-the-window/' | relative_url }})
- [Your first session]({{ '/en/javascript/first-session/' | relative_url }})
- [JavaScript Tutor docs]({{ '/en/javascript/' | relative_url }})
