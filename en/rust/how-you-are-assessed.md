---
layout: default
title: How the tutor judges your work (Rust)
lang: en
permalink: /en/rust/how-you-are-assessed/
---

# How the tutor judges your work

The tutor keeps no score. It collects **evidence** — and tells you at any point which evidence it
has and which it is missing. This page explains what counts as evidence, why some things
deliberately do not, and what you walk away with.

## Three levels per objective

A course is not really made of steps but of **learning objectives**; the steps are the route. For
each objective the tutor keeps one of three levels:

| Level | How you reach it |
|---|---|
| **touched** | The objective came up and some evidence exists. Unlocks nothing. |
| **practised** | One strong piece of evidence, or two medium ones. A module counts as finished once every objective in it is at least here. |
| **demonstrated** | A strong piece of evidence **and** a recall passed in a **later** module. |

The third level is the one that makes a claim. It does not mean "managed it once"; it means: could
do it again later, from memory, without the exercise in front of you.

## What counts as evidence

| Evidence | Weight |
|---|---|
| Check passed on the **first** attempt with no hint | strong |
| Spaced recall passed | strong |
| Check passed with hints | medium |
| Prediction was right | medium |
| Understanding question passed against its rubric | medium |
| **Self-assessment** | **counts for nothing** |

That last row is deliberate rather than harsh. An answer you marked correct yourself is a useful
step in learning — but it is not evidence to anyone else, and the tutor does not pretend otherwise.

## When no language model is running

Understanding questions are graded by a language model against a stored rubric. When none is
configured, or it cannot be reached, the tutor shows you **the rubric itself** — the criteria your
answer would be measured against — and you confirm whether your answer meets them.

That is the honest fallback: you keep moving, you see the standard, and the step turns green. It is
visibly marked **self-assessed**, and the level "demonstrated" stays out of reach for that
objective until something has actually graded it.

## When the model is busy

The model answers one request at a time. When thirty people answer the same question at once it
gets tight, and one of two things happens:

**Your request runs, but slowly.** The tutor shows you that it is waiting for the grading, and how
long it has been waiting. If it takes unusually long, it offers to stop waiting and use the rubric
as a self-check instead.

**Your request is turned away.** When the model is saturated the tutor says so **immediately**
rather than leaving you to wait: how busy it is, when a new attempt makes sense — and it puts the
same rubric in front of you for a self-check. Being turned away reads worse than a spinner, but it
is better: you know where you stand and you can carry on.

The time shown comes from the model service itself and is an estimate, not a promise.

## What you take away

The command **`CaDS Tutor: Export record of competence`** produces a document listing, per
objective: level, date, **kind of evidence**, and the step the evidence came from. Where a level was
not reachable on this installation at all — because no language model was running, say — it says
so. A badge without criteria and evidence is a sticker; this one is not.

## What is deliberately absent

No points, no levels, no streaks, no leaderboard, no competition between participants. That is a
reasoned decision: reward-and-status mechanics measurably move motivation and belonging, but barely
move **competence** — and competence is what this course should be able to claim.

What you get instead: your level per objective, a "here is what you can do now" card at the end of
each module, and the record to take with you.
