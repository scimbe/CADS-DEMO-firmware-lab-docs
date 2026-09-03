---
title: Why cads-zero is the workspace
order: 2
description: Why the lab opens a real firmware repository instead of a toy example, and how the seed, the toolchain and your copy fit together
---

## A real repository, not an example

Earlier iterations of this lab shipped a small example firmware. The current lab opens
[CaDS Zero](https://github.com/scimbe/cads-zero) directly: a clean-room firmware for the
ITSboard with a kernel, a GUI framework, FreeRTOS, littlefs, lwIP, a bring-up explorer console,
unit and golden-image tests, and a documented history of every hardware problem the project hit.
The courses are grounded in that repository; every register, path, symbol and measured number a
step mentions can be checked in the tree you have open. A toy example could not carry a course
that climbs from "which pin is the LED" to "defend a dirty-rectangle trade-off".

## The seed and your copy (ADR-003)

The image contains a shallow clone of cads-zero with its submodules at a pinned commit under
`/opt/cads-seed/cads-zero`, **built once during the image build**: `cmake --preset itsboard`
produces `cads-zero.bin` and `compile_commands.json`, and the host preset runs `ctest` as a
second smoke test. A build that fails fails the image.

On the first start of a container the entrypoint copies the seed to
`/home/coder/workspace/cads-zero` if no `.git` exists there. That copy lives in your workspace
volume; later starts leave it alone, so your edits, your builds and your tutor session survive
restarts and image updates. The seed is checked out on a local branch `cads-lab` rather than a
detached HEAD, because a detached HEAD confuses students and nothing depends on the name.

Only the container configuration is refreshed on every start: `.vscode/{settings,tasks,launch,
extensions}.json` and `.clangd`. They are marked `skip-worktree` so `git status` stays clean, and
`extensions.json` replaces cads-zero's own recommendation of `ms-vscode.cpptools` (not on Open
VSX) with `clangd`, the IntelliSense engine of the image.

## The toolchain

cads-zero is developed with ARM GNU 13.3.1 via vcpkg. The image installs the official
**13.3.rel1** tarball for its architecture rather than Debian's 12.2 package, so students build
with the same compiler as the maintainer and the linker's memory report matches the numbers in
the docs. `CADS_ARM_TOOLCHAIN_BIN` points at it, which is how `scripts/cads_env.sh` finds it
without vcpkg.

One deviation: the toolchain's `arm-none-eabi-gdb` needs ncurses 5, which Debian 13 no longer
ships. A wrapper of the same name executes `gdb-multiarch` 16.3 instead; cortex-debug and the
scripts do not notice.

## Why IntelliSense works without configuring anything

CMake Tools does not configure on open (it would ask every student for a preset before they
have done anything). Instead, clangd reads the seeded `build/itsboard/compile_commands.json`
and asks the toolchain driver for its include paths, so cross-compiled headers resolve from the
first click. The lab tasks run CMake themselves. Students who prefer CMake Tools pick the
`ITSboard` preset in the status bar and get the same result.
