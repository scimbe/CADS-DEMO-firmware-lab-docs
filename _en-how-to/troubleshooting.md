---
title: Troubleshooting / FAQ
order: 1
description: Something not working? Check here first
---

Every item below is a real problem hit and fixed while building and testing this lab — not a
generic checklist.

## Flashing

**I clicked Flash and nothing happened — no error, nothing.**
Two separate, silent gaps, either of which produces exactly this symptom:
1. The Flash button stays *disabled* until the target has been explicitly **Halted** first. Click
   Halt, then Flash.
2. The click handler no-ops if no file is actually selected in the file picker — check that a
   `.bin` is actually chosen, not just that the picker was opened.

**The board doesn't show up when I try to connect.**
Make sure you're using Chrome or Edge — WebUSB (what this lab uses to talk to the ST-Link) isn't
supported in Safari or Firefox. The first connection attempt should trigger a browser permission
dialog listing the ST-Link device; if you don't see that dialog, the browser or OS may not have
granted USB access at all — check your OS's USB device permissions for the browser.

**I'm running this locally in Docker on a Mac and flashing never works.**
This is a confirmed Docker Desktop for Mac limitation: USB devices cannot be passed through into a
Linux container on that platform. It's not fixable from inside the container. The hosted version
of this lab sidesteps it entirely by flashing straight from your browser via WebUSB rather than
from inside a container — if you're running a local copy, flash from the host, not from Docker.

## The tutor

**The tutor gave me an HTTP 401 / authentication error.**
If you're running a local copy against your own LLM endpoint: double check the endpoint URL uses
`https://`, not `http://`. A plain-HTTP endpoint URL was the actual cause of a real 401 seen while
building this lab — it looked like a credentials problem but wasn't one.

**The tutor won't answer / gives a refusal instead of an answer.**
This is often correct behavior, not a bug: the tutor is built to only answer from indexed
reference material, and returns an honest "I don't have grounded material for that" rather than
guessing when nothing in its index is actually relevant. If you think it should know the answer,
that's worth reporting — it may mean the reference index needs to be extended, not that something
is broken.

## The IDE itself

**A "do you trust the authors of this workspace" dialog appeared.**
That's VS Code's own standard workspace-trust prompt, not specific to this lab — accept it for the
lab's own starter workspace.

**`Ctrl+Shift+P` doesn't open the command palette.**
The browser itself can intercept that shortcut. Use `F1` instead — it always opens the command
palette in this environment.

## Still stuck?

[Open an issue](https://github.com/scimbe/CADS-DEMO-firmware-lab/issues/new) with what you tried
and what you saw — a real report, even a short one, is what keeps this page accurate.
