---
title: Prepare
order: 1
description: What you need before you start (spoiler — almost nothing)
---

## What you need

- A modern browser (Chrome or Edge — the ST-Link connection uses WebUSB, which Safari and
  Firefox don't support yet).
- A GitHub account, to sign in.
- Nothing else. No compiler, no debugger, no drivers to install. The IDE, the ARM toolchain, and
  the ST-Link debug server all run server-side; your browser just needs to *display* them and talk
  to the board over WebUSB.

<div class="callout warn">
<strong>If you're on Docker Desktop for Mac:</strong> USB passthrough to a container does not work
on that platform — this is a confirmed Docker-for-Mac limitation, not a bug in this project. The
hosted version of this lab avoids it by flashing from your own browser via WebUSB instead of from
inside a container. If you're running your own local copy in a Mac container, plan to flash from
the host, not from inside Docker.
</div>

## Hardware (only if you're using a real board)

- A NUCLEO-F429ZI + ITS adapter + Waveshare 4" shield ("ITSboard"), or just use the built-in
  simulator target — everything in this lab runs on both.
- A USB cable from the board's ST-Link port to your computer.
- The first time you plug it in, your browser will ask you to pick the ST-Link device from a list —
  that's the WebUSB permission prompt, and it's expected.

## Before your first session

1. Open the lab URL and sign in with GitHub.
2. The browser will likely show a **workspace trust** dialog the first time a new workspace loads —
   this is VS Code's own standard "do you trust the authors of this folder" prompt, not specific to
   this lab. Accept it; the workspace is this lab's own starter project.
3. That's it — you're ready for [your first lesson]({{ '/en/tutorials/first-lesson/' | relative_url }}).

<p class="tagline">If something here doesn't match what you actually see, check the <a href="{{ '/en/how-to/troubleshooting/' | relative_url }}">troubleshooting guide</a> next.</p>
