---
title: Reset your progress
order: 7
description: Start the course from step 1 again, and what the reset keeps
---

## What is stored where

| Data | Location | Reset by the command |
|---|---|---|
| Current course and step, task status, your answers | `<workspace>/.cads-tutor/session.json` | yes |
| Learning events (checks passed and failed, questions asked) | `~/.cads-tutor/events.sqlite` (or `events.json` where SQLite is unavailable) | no |
| Dialog log of "Ask the tutor" | `~/.cads-tutor/dialog.jsonl` | no |
| Your edits in the firmware | the workspace `cads-zero` | no |

Everything lives in the workspace volume of your container. A container restart or a new image
keeps it; only the operator can wipe the volume.

## Reset the session

**F1 → CaDS Tutor: Fortschritt zurücksetzen / Reset progress**. A confirmation asks:

> Reset all tutor progress in this workspace? Learning events are kept.

Confirm with *Reset*. The tree locks every step except the first, the status bar shows the
first step, and the panel opens step 1. Mastery in the *Progress* view stays, because it is
derived from the learning events.

## Reset the firmware too

The tutor does not touch your code. If you also want the repository back at the seeded state,
run in the terminal:

```bash
git status                      # see what you changed
git checkout -- .               # discard uncommitted edits
git clean -fd                   # remove new untracked files (keeps build/)
```

The seeded checkout sits on a local branch `cads-lab` at the pinned commit; `git log -1` shows
it. Your edits to `.vscode/*.json` and `.clangd` are overwritten on every container start
anyway, so keep personal tasks elsewhere.

There is no per-step reset; the command always resets the whole session.
