---
title: Switch the language
order: 6
description: Change the course language between German and English in the panel, by command or by setting
---

All course content ships in English and German. The tutor picks the language in this order:

1. The setting `cadsTutor.language` (`auto`, `de`, `en`). Default `auto`.
2. With `auto`: the VS Code display language of your browser session.
3. Whatever you last chose in the panel; that choice is stored in your session and survives a
   reload.

## In the panel

The step panel header has a button labelled **Deutsch** (on the English UI) or **English** (on
the German UI). One click switches panel, course tree, progress view and status bar together.

## By command

**F1 → CaDS Tutor: Sprache wählen / Set language**, then pick `Deutsch` or `English`. The
Courses view has the same command behind its globe icon.

## By setting

Open *Settings* (F1 → *Preferences: Open User Settings*), search for `cadsTutor.language` and set
it to `de` or `en`. This overrides the panel choice for every new session.

## What does not change

- The VS Code UI itself stays in the display language of your browser profile. The lab does not
  install language packs.
- Command titles of the lab extensions are bilingual by design, for example
  *Tutor öffnen / Open Tutor*, so you find them in the palette in either language.
- Messages of the board bridge (status bar, flash notifications) are German in the current
  release.
