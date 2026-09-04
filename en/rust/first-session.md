---
layout: default
title: Your first session (Rust)
lang: en
permalink: /en/rust/first-session/
---

# Your first session

This page takes you from the link in your browser to a first green check. It needs about fifteen
minutes and no preparation at all: no installation, no account beyond the one you were given, no
hardware.

## 1. Open the link you were given

Your teacher hands out one link per track. The Rust link ends in
`?folder=/home/coder/workspace/rust-foundations`.

**That part matters.** It decides which course opens. A bare address without it reopens whatever
that browser had open last, which on a shared machine may well be someone else's course.

Log in with the password you were given. What loads is VS Code, running on a server, in your
browser tab.

## 2. Find the tutor

On the far left is a narrow strip of icons. The one shaped like a **mortarboard** opens the CaDS
Tutor. Click it and the side bar shows the course tree: **Rust – Foundations**, its eight modules,
and the steps inside them.

Click the first step. It opens as a tab of its own in the middle of the window, with its title, an
estimate of how long it takes, the learning goal, the text itself and, at the bottom, the tasks.

## 3. Work the first step

The first step is about the window rather than about Rust, on purpose. Everything after it assumes
you can find a command, start a terminal, read its output and close it again. Fifteen minutes here
save an hour later.

Each task has a **Check** button. Press it and the tutor runs the real command and reports what
happened. A task that asks you to explain something has an answer box instead: write two or three
sentences in your own words and submit.

Some questions are marked as understanding checks. The tutor does not accept a keyword — it wants
your reasoning. If there is no language model configured on your installation, the tutor shows you
the rubric it would have graded against and asks you to check yourself; that result is recorded as
self-reported, not as an independent pass.

## 4. If something does not work

- **The first cargo command says `could not find Cargo.toml`.** Your terminal is one folder above
  the crate. `cd ~/workspace/rust-foundations` fixes it. See
  [Running commands and tasks]({{ '/en/rust/working-the-window/' | relative_url }}).
- **The palette finds nothing.** Type `>` before the command name.
- **A test fails.** That is the normal state of an exercise. The compiler message is the material
  the step wants you to read; see
  [When a check will not pass]({{ '/en/rust/when-a-check-fails/' | relative_url }}).
- **The wrong course opens.** You used the bare address. Go back to the link with the `?folder=`
  part.

## What comes next

Work the modules in order. Each one builds on the last, and the tutor unlocks steps as you go, so
you can always see what to do next rather than having to choose.

## Related

- [Running commands and tasks]({{ '/en/rust/working-the-window/' | relative_url }})
- [What the course covers]({{ '/en/rust/the-course/' | relative_url }})
- [Rust Tutor docs]({{ '/en/rust/' | relative_url }})
