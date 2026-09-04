---
layout: default
title: Running commands and tasks (Rust)
lang: en
permalink: /en/rust/working-the-window/
---

# Running commands and tasks

Every step of the course asks you to run something. There are three ways to do it and they are
interchangeable — pick whichever you like and stay with it. This page exists because following a
tutorial is genuinely hard if nobody tells you which key to press.

## The window, in five parts

| Part | Where | What it is for |
|---|---|---|
| Activity bar | far left, a column of icons | switches the side bar; the mortarboard icon opens the tutor |
| Side bar | left | Explorer (your files) or the tutor's course tree |
| Editor | middle | your code, and the step you are working on, as tabs |
| Panel | bottom, closed until needed | the tabs **Terminal**, **Problems** and **Output** |
| Status bar | very bottom | language mode, and which language server is running |

The panel matters more than it looks. **A command you type prints in Terminal.** Problems holds
what the compiler reports about your open files, Output holds messages from the editor's own
machinery. Neither of those will ever show the result of a command you ran — a surprising amount
of confusion comes from looking in the wrong tab.

## Three ways to run the same thing

**1. The button on the task card.** Each task in the tutor has a button that runs exactly the
command the task asks for. Under it you will find the line *same as: open a terminal and type …*,
so you can always see what it actually did.

**2. The terminal.** Open it with **Terminal → New Terminal** in the menu, or press
<kbd>Ctrl</kbd>+<kbd>`</kbd> (the backtick key, above Tab on most layouts). Then type the command
and press <kbd>Enter</kbd>.

**3. The command palette.** Press <kbd>F1</kbd>. Then type the command name.

## The palette detail that trips everyone up

The palette remembers the mode you used last, and it opens in *file* mode by default: what you
type is treated as a filename. Typing `Terminal: Create New Terminal` there gives you
**No matching results**, which looks like the command does not exist.

**Type `>` first.** The leading angle bracket switches the palette to command mode, and the same
text now finds the command. If a step tells you to run a command from the palette, the `>` is
part of the instruction.

## Two more things worth knowing early

**A new terminal does not start in the crate.** The lab window holds two workspaces side by side,
so a fresh terminal starts one level above, in `~/workspace`. The first cargo command then answers
`could not find Cargo.toml`, which reads like a broken exercise but is only the wrong folder. Every
step in the course starts by putting you in the right place:

```
cd ~/workspace/rust-foundations
```

`pwd` prints where you are, if you want to be sure.

**A command is finished when the prompt comes back.** Until then it is still running, even if
nothing new appears on screen. Closing the terminal with the bin icon does not just hide it — it
ends whatever was running inside.

## Related

- [Your first session]({{ '/en/rust/first-session/' | relative_url }})
- [When a check will not pass]({{ '/en/rust/when-a-check-fails/' | relative_url }})
- [Rust Tutor docs]({{ '/en/rust/' | relative_url }})
