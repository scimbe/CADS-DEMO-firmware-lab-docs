---
title: Tasks and launch configurations
order: 1
description: Every lab task in tasks.json and both cortex-debug configurations in launch.json, as written by the container on start
---

The container writes `.vscode/tasks.json`, `launch.json`, `settings.json`, `extensions.json` and
`.clangd` into the workspace on every start (`/entrypoint.d/10-seed-workspace.sh`). Edits to
these files are overwritten; they are marked `skip-worktree` so they never appear in `git
status`.

## Tasks

Run with **F1 → Tasks: Run Task**, filter `CaDS:`. Working directory is the workspace root.

| Task | Command | Group |
|---|---|---|
| `CaDS: Build` | `cmake --preset itsboard && cmake --build build/itsboard` | build (default, Ctrl+Shift+B) |
| `CaDS: Flash` | `st-flash write build/itsboard/cads-zero.bin 0x08000000 && st-flash reset` | – |
| `CaDS: Build + Flash` | the two above in sequence (`dependsOn`, `dependsOrder: sequence`) | – |
| `CaDS: Host tests` | `cmake --preset host && cmake --build build/host && ctest --test-dir build/host --output-on-failure -E '^golden_'` with `SDL_VIDEODRIVER=dummy`, `SDL_AUDIODRIVER=dummy` | test (default) |
| `CaDS: Golden images (informativ)` | same host build, then `ctest … -R '^golden_'` and an explanatory echo | test |
| `CaDS: RAM budget` | `python3 scripts/check_ram_budget.py build/itsboard/cads-zero.elf` | – |

`CaDS: Build` and `CaDS: Host tests` use the `$gcc` problem matcher, so compiler errors appear in
the *Problems* view and are clickable.

## Launch configurations

Both are of type `cortex-debug` with `servertype: external` and `gdbTarget: 127.0.0.1:3333`,
the bridge's GDB server. No configuration talks to USB.

| Field | Debug CaDS Zero (Board im Browser) | Attach CaDS Zero (Board im Browser, no flash) |
|---|---|---|
| `request` | `launch` | `attach` |
| `executable` | `${workspaceFolder}/build/itsboard/cads-zero.elf` | same |
| `device` | `STM32F429ZI` | same |
| `svdFile` | `${workspaceFolder}/targets/itsboard/STM32F429.svd` | same |
| `armToolchainPath` | `/opt/arm-gnu-toolchain/bin` | same |
| `gdbPath` | filled in at start: toolchain `arm-none-eabi-gdb` if it runs, else `/usr/bin/gdb-multiarch` | same |
| `preLaunchTask` | `CaDS: Build + Flash` | – |
| `overrideLaunchCommands` | `["monitor reset halt"]` | – |
| `runToEntryPoint` | `main` | – |
| `showDevDebugOutput` | `none` | `none` |

The bridge also registers a dynamic configuration provider: pressing F5 without a `launch.json`
yields the same *Debug* configuration, and if the board is not connected the provider asks
*Das Board ist nicht verbunden. Jetzt verbinden?* before starting.

## GDB in the image

The ARM GNU 13.3.rel1 `arm-none-eabi-gdb` does not run on Debian 13 (it needs ncurses 5).
`/usr/local/bin/arm-none-eabi-gdb` is therefore a wrapper that executes `gdb-multiarch` 16.3,
so scripts that call GDB by name keep working. Compiler, binutils, `objcopy`, `nm` and `size`
come from the toolchain unchanged.

## Workspace settings written by the container

`clangd` uses `build/itsboard/compile_commands.json` (`--compile-commands-dir`), queries the
toolchain driver for its include paths, indexes in the background with four workers and keeps
precompiled headers on disk. CMake presets are always used; `cmake.configureOnOpen` and
`cmake.automaticReconfigure` are off.
