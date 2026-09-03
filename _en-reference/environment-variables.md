---
title: Environment variables of the image
order: 6
description: Variables the image reads at container start, variables it sets for you, and the settings that mirror them
---

## Set by the operator on `docker run`

| Variable | Required | Meaning |
|---|---|---|
| `PASSWORD` | yes (single-user mode) | password of the code-server login page |
| `TUTOR_LLM_BASE_URL` | no | OpenAI-compatible endpoint (`https://…/v1`) for "Ask the tutor", question grading and check-ins |
| `TUTOR_LLM_API_KEY` | no | key for that endpoint; only ever read from the environment, never from a setting |
| `TUTOR_LLM_MODEL` | no | model name |
| `CMAKE_BUILD_PARALLEL_LEVEL` | no | caps `cmake --build` parallelism for every lab task; `1` or `2` on small hosts |

Without the three `TUTOR_LLM_*` variables the tutor runs with checks, hints and sources but
without a language model. In the multi-user stack these variables are injected by the session
broker from its own environment; they are never baked into the image.

## Set by the image

| Variable | Value | Meaning |
|---|---|---|
| `PATH` | `/usr/local/bin:/opt/arm-gnu-toolchain/bin:…` | shims first, then the ARM toolchain |
| `CADS_ARM_TOOLCHAIN_BIN` | `/opt/arm-gnu-toolchain/bin` | read by cads-zero's `scripts/cads_env.sh` and by the tutor for `arm-none-eabi-nm` |
| `CADS_WORKSPACE` | `/home/coder/workspace/cads-zero` | workspace path used by the entrypoint |
| `SDL_VIDEODRIVER`, `SDL_AUDIODRIVER` | `dummy` | headless SDL2 for the host tests |

## Variables the cads-zero scripts understand

| Variable | Meaning in the container |
|---|---|
| `CADS_CONSOLE_PORT` | serial port for `board_cmd.py`, `board_key.py`, `board_test.py`; set it to `/home/coder/board-console` (the bridge's PTY link) |
| `CADS_STLINK_SERIAL` | accepted by `flash.sh`; the shim ignores `--serial` because there is one probe |

## Image build arguments (for operators and developers)

| Argument | Default | Meaning |
|---|---|---|
| `CADS_ZERO_REF` | `e882fab…` | cads-zero commit seeded into the image |
| `CADS_SKIP_HOST_BUILD` | `0` | skip the host build and `ctest` during the image build |
| `CADS_KEEP_HOST_BUILD` | `0` | keep `build/host` in the seed |
| `CADS_PRUNE_MULTILIBS` | `1` | drop unused toolchain multilibs |
| BuildKit secret `gh_token` | – | read-only token for the private cads-zero repository |

## Settings that mirror variables

| Setting | Relation |
|---|---|
| `cadsTutor.llm.baseUrl`, `cadsTutor.llm.model` | fallbacks for `TUTOR_LLM_BASE_URL` / `TUTOR_LLM_MODEL`; there is no setting for the key |
| `cadsTutor.buildTaskLabel` | task label used by `build` checks without a label (`CaDS: Build`) |
| `cadsTutor.extraCourseDirs` | additional course directories |
| `cads.board.*` | ports, baud rate, default image, GDB path of the bridge |
