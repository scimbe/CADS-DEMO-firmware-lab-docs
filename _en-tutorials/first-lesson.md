---
title: Your first lesson
order: 1
description: Log in, build, flash, and ask the tutor a real question — start to finish
---

This walks through one complete session end to end: sign in, look around the IDE, build the
starter firmware, flash it to a real chip, and ask the built-in tutor a question about what just
happened. Every screenshot below is from an actual run.

## 1. Sign in

Open the lab URL and sign in with your GitHub account.

<figure>
<img src="{{ '/assets/00-login.png' | relative_url }}" alt="Sign-in screen">
<figcaption>The sign-in screen — GitHub OAuth, nothing else to configure.</figcaption>
</figure>

## 2. Look around

You land in a full VS Code workspace running in your browser: a file tree on the left, an editor
in the middle, and a terminal at the bottom.

<figure>
<img src="{{ '/assets/01-ide-workspace.png' | relative_url }}" alt="IDE workspace">
<figcaption>The starter workspace — this is real VS Code for the Web, not a lookalike.</figcaption>
</figure>

## 3. Build

Open the terminal and build the firmware:

```bash
cmake --build build/itsboard
```

<figure>
<img src="{{ '/assets/02-build-terminal.png' | relative_url }}" alt="Build output in terminal">
<figcaption>A real ARM GCC build, running server-side, streamed into your terminal.</figcaption>
</figure>

## 4. Flash

Connect the board over WebUSB and flash the binary you just built. This uses the browser's own
ST-Link driver — no local tools.

<div class="callout warn">
The <strong>Flash</strong> button stays disabled until the target is explicitly <strong>Halted</strong>
first — click Halt before Flash if the button looks greyed out. And if you click Flash and nothing
visibly happens, check that a file is actually selected in the file picker first; an empty
selection silently does nothing rather than showing an error.
</div>

## 5. Ask the tutor

Open the command palette and find the tutor command.

<div class="callout">
On some keyboard layouts, <code>Ctrl+Shift+P</code> may not open the command palette in the
browser (the browser itself can intercept it) — <code>F1</code> always works as a fallback.
</div>

<figure>
<img src="{{ '/assets/03-command-palette-tutor.png' | relative_url }}" alt="Command palette showing the tutor command">
<figcaption>The tutor is a command, not a separate app — invoke it from wherever you're working.</figcaption>
</figure>

Ask it something real about the code you just flashed — for example, why a specific register
write in the startup code does what it does.

<figure>
<img src="{{ '/assets/04-tutor-step1.png' | relative_url }}" alt="Tutor asking a clarifying question">
<figcaption>The tutor introduces itself as CaDS Tutor and asks a clarifying question before answering.</figcaption>
</figure>

<figure>
<img src="{{ '/assets/05-tutor-llm-answer.png' | relative_url }}" alt="Tutor giving a grounded answer with citations">
<figcaption>A real answer, grounded in cited reference material — not a guess.</figcaption>
</figure>

## What you just did

You built and flashed real firmware onto a real chip from nothing but a browser tab, and got a
real, cited explanation of what it does. That's the whole lab in miniature — everything else is
more of this, on harder problems.

Next: if anything above didn't match what you saw, check the
[troubleshooting guide]({{ '/en/how-to/troubleshooting/' | relative_url }}).
