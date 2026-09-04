---
layout: default
title: When a check will not pass (Rust)
lang: en
permalink: /en/rust/when-a-check-fails/
---

# When a check will not pass

A red check is the normal state of an exercise before you solve it. This page is for the case
where you have tried and it still will not go green.

## First: read the message, not the colour

`cargo` tells you what it wants, and it is unusually good at it. Every compiler error has a code
like `E0382`, a line and column, and often a suggestion. The course is built around these messages
on purpose — several steps exist only so that you meet a particular error under controlled
conditions and learn to read it.

Work from the **first** error downwards. Later errors are frequently just consequences of the
first one and disappear on their own.

## The hint ladder

Every task has hints, and they come in three tiers. Ask for them in order:

1. **A question** that points at the place to look, without saying what is wrong.
2. **A narrower hint** naming the concept or the rule that applies.
3. **A concrete direction**, though never the line to paste.

The tiers exist so that you keep the part of the work that produces the learning. If tier three
still leaves you stuck, that is worth telling your teacher: it usually means the step assumes
something it never taught.

## The five failures that are not your code

| Symptom | Cause | Fix |
|---|---|---|
| `could not find Cargo.toml` | terminal one level above the crate | `cd ~/workspace/rust-foundations` |
| **No matching results** in the palette | palette is in file mode | type `>` before the command name |
| Command seems to hang, nothing prints | it is still running | wait for the prompt to come back |
| Output missing entirely | you are looking at Problems or Output | switch to the **Terminal** tab |
| `cargo` itself not found | toolchain missing in this container | an environment fault — report it, you cannot fix it in the editor |

## When the tutor asks you a question instead of checking

Some tasks want an explanation rather than a command. The tutor grades your reasoning against a
rubric — and it will tell you what does **not** pass, not just what does. A keyword is not an
answer; two or three sentences that connect cause and effect are.

If your installation has no language model configured, the tutor shows you that rubric and asks
you to check yourself. Be honest with it: the result is recorded as self-reported, and the point
of the exercise is your own understanding, not the tick.

## Still stuck

Ask the tutor. It answers from the indexed course material and the toolchain documentation, and it
will refuse a question it cannot ground in a source rather than inventing an answer. Ask in German
or English, whichever you prefer.

## Related

- [Running commands and tasks]({{ '/en/rust/working-the-window/' | relative_url }})
- [Your first session]({{ '/en/rust/first-session/' | relative_url }})
- [Rust Tutor docs]({{ '/en/rust/' | relative_url }})
