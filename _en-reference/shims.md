---
title: The st-flash and st-info shims
order: 3
description: What the container's st-flash and st-info accept, refuse and print
---

`/usr/local/bin/st-flash` and `/usr/local/bin/st-info` are Python programs, first on `PATH`,
that talk to the bridge's HTTP API on `127.0.0.1:3335`. They exist so that cads-zero's own
scripts (`scripts/flash.sh`, `scripts/build.sh`, the tasks) run unchanged inside the container,
where the real stlink tools would find no USB device.

## st-flash

| Invocation | Behaviour |
|---|---|
| `st-flash write <file> <addr>` | `POST /flash?addr=<addr>` with the file as body. `.bin` is sent as is; an `.elf` is converted with `objcopy` first. Exit 0 on success. |
| `st-flash reset` | `POST /reset`. |
| `st-flash --serial <id> …` | `--serial` is accepted and ignored: there is exactly one probe, the one in your browser. |
| `st-flash erase` | refused: `error: erase is not permitted by CaDS lab policy (no mass erase, docs/SAFETY.md)`, exit 1. |
| any command without a reachable bridge | `Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)`, exit 1. |

Writes are accepted only inside `0x08000000–0x080FFFFF` (the first megabyte, flash bank 1).
The bridge checks the window again independently of the shim.

## st-info

| Invocation | Output |
|---|---|
| `st-info --probe` | `GET /probe`, printed verbatim in the stlink text format: `serial`, `chipid 0x419`, `descr STM32F42x_F43x`, `flash 2097152 (pagesize: 16384)`, `sram`. |
| `st-info --serial` / `--chipid` / `--flash` / `--sram` / `--descr` / `--pagesize` | one field, parsed from the same report. |
| without a reachable bridge | the German hint above, exit 1. |

## Testing the shims

The repository tests them against a mock HTTP bridge, without Docker:

```bash
python3 -m unittest discover -s tests/shims -v
```
