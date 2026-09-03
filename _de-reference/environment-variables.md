---
title: Umgebungsvariablen des Images
order: 6
description: Variablen, die das Image beim Containerstart liest, Variablen, die es für dich setzt, und die Einstellungen, die sie spiegeln
---

## Vom Betreiber bei `docker run` gesetzt

| Variable | Pflicht | Bedeutung |
|---|---|---|
| `PASSWORD` | ja (Einzelplatz-Modus) | Passwort der code-server-Login-Seite |
| `TUTOR_LLM_BASE_URL` | nein | OpenAI-kompatibler Endpunkt (`https://…/v1`) für „Frag den Tutor“, Fragenbewertung und Check-ins |
| `TUTOR_LLM_API_KEY` | nein | Schlüssel für diesen Endpunkt; wird ausschließlich aus der Umgebung gelesen, nie aus einer Einstellung |
| `TUTOR_LLM_MODEL` | nein | Modellname |
| `CMAKE_BUILD_PARALLEL_LEVEL` | nein | begrenzt die Parallelität von `cmake --build` für jeden Labor-Task; `1` oder `2` auf schwachen Hosts |

Ohne die drei `TUTOR_LLM_*`-Variablen läuft der Tutor mit Checks, Hinweisen und Quellen, aber
ohne Sprachmodell. Im Multi-User-Stack injiziert der Session-Broker diese Variablen aus seiner
eigenen Umgebung; sie werden nie ins Image gebacken.

## Vom Image gesetzt

| Variable | Wert | Bedeutung |
|---|---|---|
| `PATH` | `/usr/local/bin:/opt/arm-gnu-toolchain/bin:…` | zuerst die Shims, dann die ARM-Toolchain |
| `CADS_ARM_TOOLCHAIN_BIN` | `/opt/arm-gnu-toolchain/bin` | gelesen von cads-zeros `scripts/cads_env.sh` und vom Tutor für `arm-none-eabi-nm` |
| `CADS_WORKSPACE` | `/home/coder/workspace/cads-zero` | Workspace-Pfad, den der Entrypoint nutzt |
| `SDL_VIDEODRIVER`, `SDL_AUDIODRIVER` | `dummy` | headless SDL2 für die Host-Tests |

## Variablen, die die cads-zero-Skripte verstehen

| Variable | Bedeutung im Container |
|---|---|
| `CADS_CONSOLE_PORT` | serieller Port für `board_cmd.py`, `board_key.py`, `board_test.py`; setze ihn auf `/home/coder/board-console` (den PTY-Link der Bridge) |
| `CADS_STLINK_SERIAL` | von `flash.sh` akzeptiert; das Shim ignoriert `--serial`, weil es eine Probe gibt |

## Build-Argumente des Images (für Betreiber und Entwickler)

| Argument | Standard | Bedeutung |
|---|---|---|
| `CADS_ZERO_REF` | `e882fab…` | cads-zero-Commit, der ins Image geseedet wird |
| `CADS_SKIP_HOST_BUILD` | `0` | Host-Build und `ctest` beim Image-Build überspringen |
| `CADS_KEEP_HOST_BUILD` | `0` | `build/host` im Seed behalten |
| `CADS_PRUNE_MULTILIBS` | `1` | ungenutzte Multilibs der Toolchain entfernen |
| BuildKit-Secret `gh_token` | – | Nur-Lese-Token für das private cads-zero-Repository |

## Einstellungen, die Variablen spiegeln

| Einstellung | Bezug |
|---|---|
| `cadsTutor.llm.baseUrl`, `cadsTutor.llm.model` | Fallbacks für `TUTOR_LLM_BASE_URL` / `TUTOR_LLM_MODEL`; für den Schlüssel gibt es keine Einstellung |
| `cadsTutor.buildTaskLabel` | Task-Label für `build`-Checks ohne Label (`CaDS: Build`) |
| `cadsTutor.extraCourseDirs` | zusätzliche Kursverzeichnisse |
| `cads.board.*` | Ports, Baudrate, Standard-Image, GDB-Pfad der Bridge |
