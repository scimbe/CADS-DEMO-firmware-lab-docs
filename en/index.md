---
layout: default
title: Firmware Lab
lang: en
permalink: /en/
---

# CaDS Firmware Lab — Docs

<p class="tagline">A browser IDE for real STM32 firmware: the ARM toolchain and the course tutor run in a container, the board stays plugged into your own computer, and the browser drives the ST-Link for flashing, debugging and the serial console. Nothing to install.</p>

You open a URL and get VS Code with the [CaDS Zero](https://github.com/scimbe/cads-zero)
firmware for the ITSboard (STM32F429ZI) already cloned and built. A tutor beside your editor
walks you through 41 steps from "connect the board" to "defend a design trade-off", checks your
work against the repository and the board, and answers questions only from indexed material.

## I am a student

<div class="index-list">
  <a class="index-item" href="{{ '/en/tutorials/first-session/' | relative_url }}">
    <strong>1. Your first session →</strong>
    <span>Log in, find your way around, complete step 1 (no board needed)</span>
  </a>
  <a class="index-item" href="{{ '/en/how-to/connect-the-board/' | relative_url }}">
    <strong>2. Connect the board →</strong>
    <span>Browser requirements and the notes for macOS, Windows and Linux</span>
  </a>
  <a class="index-item" href="{{ '/en/tutorials/build-and-flash/' | relative_url }}">
    <strong>3. Build and flash →</strong>
    <span>Task "CaDS: Build + Flash", the device chooser, the first self-test on the board</span>
  </a>
  <a class="index-item" href="{{ '/en/tutorials/debug-with-f5/' | relative_url }}">
    <strong>4. Debug with F5 →</strong>
    <span>Breakpoints, stepping, registers and the peripheral view</span>
  </a>
  <a class="index-item" href="{{ '/en/how-to/troubleshooting/' | relative_url }}">
    <strong>Troubleshooting / FAQ →</strong>
    <span>Real findings, with the fix for each</span>
  </a>
</div>

## I am a course author

<div class="index-list">
  <a class="index-item" href="{{ '/en/how-to/write-a-course/' | relative_url }}">
    <strong>Write your own course →</strong>
    <span>Course pack layout, steps with front matter, loading and validating</span>
  </a>
  <a class="index-item" href="{{ '/en/reference/course-format/' | relative_url }}">
    <strong>Course format →</strong>
    <span>Every field, every check type, every Socratic trigger</span>
  </a>
  <a class="index-item" href="{{ '/en/explanation/tutor-pedagogy/' | relative_url }}">
    <strong>Grounding, Bloom levels, Socratic hints →</strong>
    <span>Why the tutor asks instead of telling</span>
  </a>
</div>

## I operate the lab

<div class="index-list">
  <a class="index-item" href="{{ '/en/reference/environment-variables/' | relative_url }}">
    <strong>Environment variables of the image →</strong>
    <span>PASSWORD, TUTOR_LLM_*, CMAKE_BUILD_PARALLEL_LEVEL and what the image sets itself</span>
  </a>
  <a class="index-item" href="{{ '/en/explanation/board-in-the-browser/' | relative_url }}">
    <strong>Why the board hangs off the browser →</strong>
    <span>Web-worker extension host, GDB server in the bridge, no USB in the container</span>
  </a>
  <a class="index-item" href="https://github.com/scimbe/CADS-DEMO-firmware-lab">
    <strong>Developer documentation →</strong>
    <span>Image, extensions, courses, multi-user stack: the monorepo README and docs/</span>
  </a>
</div>

## How this site is organised

- **Tutorials** — learn by doing, in order.
- **How-to guides** — one task you already know you want to do.
- **Reference** — look up a fact without the narrative.
- **Explanation** — understand why the lab is built the way it is.

This is the [Diátaxis](https://diataxis.fr) framework. Every page exists in English and German;
the toggle in the header switches between them.

## What the screenshots are

Every screenshot was taken with headless Chromium against a container started from the
production image (`ghcr.io/scimbe/cads-firmware-lab:next-8a20ec9`). Pages that describe the
board paths say so where a screenshot with real hardware is still to come.
