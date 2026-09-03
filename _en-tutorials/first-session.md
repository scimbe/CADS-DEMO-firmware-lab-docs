---
title: Your first session
order: 1
description: Log in, find your way around the workbench, open the tutor panel and complete step 1
---

This tutorial takes about fifteen minutes and needs no board. You log in, look at what the lab
put on your screen, and complete the first step of the course *CaDS Zero – Foundations*.

## What you need

- A Chromium-based browser (Chrome or Edge). Firefox and Safari cannot talk to the board later on,
  so start with the right browser now.
- The lab address and the password from your course. The lab runs in single-user mode today: one
  password page, nothing else.

## 1. Log in

Open the lab address. code-server shows a single password field.

<figure>
<img src="{{ '/assets/00-login.png' | relative_url }}" alt="code-server login page with a single password field">
<figcaption>The login page. Enter the password from your course and press Enter.</figcaption>
</figure>

After a correct password the browser is redirected to the workspace
`/home/coder/workspace/cads-zero`. The tab title reads `cads-zero — CaDS Firmware Lab`.

## 2. What you see

<figure>
<img src="{{ '/assets/01-workbench-first-start.png' | relative_url }}" alt="Workbench after the first login: explorer with the cads-zero tree, tutor step panel beside the editor, status bar">
<figcaption>First start. The tutor panel opens on its own because there is no saved session yet.</figcaption>
</figure>

From left to right:

- **Activity bar.** The usual VS Code icons plus a mortarboard icon labelled *CaDS Tutor*.
- **Explorer.** The firmware repository [CaDS Zero](https://github.com/scimbe/cads-zero), already
  cloned and built once. `build/itsboard/` contains a ready `cads-zero.elf` and `cads-zero.bin`.
- **Editor area.** Empty on the first start. The tutor panel opens beside it.
- **Status bar.** CMake Tools shows *No Configure Preset Selected*. That is expected: the lab tasks
  run CMake themselves, you do not need to pick a preset. Once the tutor has a step, the status bar
  shows `🎓 Tutor: <step title>`. With the board bridge installed, a `Board: getrennt` item appears
  as well (see the [next tutorial]({{ '/en/tutorials/build-and-flash/' | relative_url }})).

Nothing asks you to trust the workspace, nothing asks for a CMake preset, and no chat side bar
opens. If you see a *Restricted Mode* banner, you are on an old deployment; see
[Troubleshooting]({{ '/en/how-to/troubleshooting/' | relative_url }}).

## 3. The tutor panel

<figure>
<img src="{{ '/assets/02-tutor-panel-step1.png' | relative_url }}" alt="Tutor step panel showing step 1 of 41, Welcome to the CaDS firmware lab, with tasks and check buttons">
<figcaption>Step 1 of 41: the welcome step of the foundations course.</figcaption>
</figure>

Every step has the same shape:

1. A header with the step title, *Step n of N*, the estimated time and the Bloom level.
2. The learning objective and a short text.
3. **Tasks** with a status and a *Check* button. Some checks are automatic (files, builds, ELF
   symbols, board state), some ask you a question, and a few are marked done by you with
   *Mark as done*.
4. **Ask the tutor**, a text box for questions about the current step.
5. *← Back* and *Next →*. The next step unlocks when all tasks of the current one pass.

## 4. The course tree

Click the mortarboard icon in the activity bar.

<figure>
<img src="{{ '/assets/03-tutor-tree.png' | relative_url }}" alt="CaDS Tutor side bar with the course tree: course, modules M0 to M8, steps with lock icons">
<figcaption>The Courses view: course → module → step. Locked steps show a lock icon until their prerequisites pass.</figcaption>
</figure>

Two courses are installed: *CaDS Zero – Foundations* (required, nine modules, 41 steps) and
*CaDS Zero – Projects* (elective, six project tasks). The *Progress* view below the tree lists
your mastery per learning objective. Clicking a step opens it in the panel.

## 5. Complete step 1

Step 1 has two tasks.

- **You opened the tutor.** A manual task. Click *Mark as done*.
- **Name the three stacked hardware parts.** A question. Write your answer into the box and click
  *Submit answer*. On this deployment the answer is graded by the language model when one is
  configured. Without one, the tutor stores your answer and asks you to confirm it yourself.

The step text tells you everything the question needs: a NUCLEO-F429ZI with the STM32F429ZI, the
ITS adapter board, and the Waveshare 4-inch touch shield. When both tasks pass, the panel shows
*Step completed!* and step 2, *Connect the board*, unlocks.

## Where you are now

You have a working editor, a built firmware, and an open course. The next tutorial plugs in the
board and puts your first build on it:
[Build and flash]({{ '/en/tutorials/build-and-flash/' | relative_url }}).
