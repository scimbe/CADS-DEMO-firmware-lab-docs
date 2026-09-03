---
title: Tasks und Launch-Konfigurationen
order: 1
description: Jeder Labor-Task in tasks.json und beide cortex-debug-Konfigurationen in launch.json, so wie der Container sie beim Start schreibt
---

Der Container schreibt `.vscode/tasks.json`, `launch.json`, `settings.json`, `extensions.json`
und `.clangd` bei jedem Start in den Workspace (`/entrypoint.d/10-seed-workspace.sh`).
Änderungen an diesen Dateien werden überschrieben; sie sind als `skip-worktree` markiert und
tauchen deshalb nie in `git status` auf.

## Tasks

Ausführen mit **F1 → Tasks: Run Task**, Filter `CaDS:`. Arbeitsverzeichnis ist die Wurzel des
Workspace.

| Task | Befehl | Gruppe |
|---|---|---|
| `CaDS: Build` | `cmake --preset itsboard && cmake --build build/itsboard` | build (Standard, Ctrl+Shift+B) |
| `CaDS: Flash` | `st-flash write build/itsboard/cads-zero.bin 0x08000000 && st-flash reset` | – |
| `CaDS: Build + Flash` | die beiden oben nacheinander (`dependsOn`, `dependsOrder: sequence`) | – |
| `CaDS: Host tests` | `cmake --preset host && cmake --build build/host && ctest --test-dir build/host --output-on-failure -E '^golden_'` mit `SDL_VIDEODRIVER=dummy`, `SDL_AUDIODRIVER=dummy` | test (Standard) |
| `CaDS: Golden images (informativ)` | derselbe Host-Build, dann `ctest … -R '^golden_'` und ein erklärendes echo | test |
| `CaDS: RAM budget` | `python3 scripts/check_ram_budget.py build/itsboard/cads-zero.elf` | – |

`CaDS: Build` und `CaDS: Host tests` nutzen den Problem-Matcher `$gcc`; Compilerfehler
erscheinen deshalb in der Ansicht *Problems* und sind anklickbar.

## Launch-Konfigurationen

Beide sind vom Typ `cortex-debug` mit `servertype: external` und `gdbTarget: 127.0.0.1:3333`,
dem GDB-Server der Bridge. Keine Konfiguration spricht mit USB.

| Feld | Debug CaDS Zero (Board im Browser) | Attach CaDS Zero (Board im Browser, no flash) |
|---|---|---|
| `request` | `launch` | `attach` |
| `executable` | `${workspaceFolder}/build/itsboard/cads-zero.elf` | gleich |
| `device` | `STM32F429ZI` | gleich |
| `svdFile` | `${workspaceFolder}/targets/itsboard/STM32F429.svd` | gleich |
| `armToolchainPath` | `/opt/arm-gnu-toolchain/bin` | gleich |
| `gdbPath` | wird beim Start eingesetzt: Toolchain-`arm-none-eabi-gdb`, falls es läuft, sonst `/usr/bin/gdb-multiarch` | gleich |
| `preLaunchTask` | `CaDS: Build + Flash` | – |
| `overrideLaunchCommands` | `["monitor reset halt"]` | – |
| `runToEntryPoint` | `main` | – |
| `showDevDebugOutput` | `none` | `none` |

Die Bridge registriert außerdem einen dynamischen Konfigurations-Provider: F5 ohne
`launch.json` liefert dieselbe *Debug*-Konfiguration, und ist das Board nicht verbunden, fragt
der Provider vor dem Start *Das Board ist nicht verbunden. Jetzt verbinden?*.

## GDB im Image

Das `arm-none-eabi-gdb` der ARM GNU 13.3.rel1 läuft nicht auf Debian 13 (es braucht ncurses 5).
`/usr/local/bin/arm-none-eabi-gdb` ist deshalb ein Wrapper, der `gdb-multiarch` 16.3 ausführt,
sodass Skripte, die GDB beim Namen aufrufen, weiter funktionieren. Compiler, binutils,
`objcopy`, `nm` und `size` kommen unverändert aus der Toolchain.

## Workspace-Einstellungen, die der Container schreibt

`clangd` nutzt `build/itsboard/compile_commands.json` (`--compile-commands-dir`), fragt den
Toolchain-Treiber nach seinen Include-Pfaden, indiziert im Hintergrund mit vier Workern und
legt vorkompilierte Header auf der Platte ab. CMake-Presets werden immer verwendet;
`cmake.configureOnOpen` und `cmake.automaticReconfigure` sind aus.
