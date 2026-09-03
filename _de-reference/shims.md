---
title: Die Shims st-flash und st-info
order: 3
description: Was st-flash und st-info im Container akzeptieren, verweigern und ausgeben
---

`/usr/local/bin/st-flash` und `/usr/local/bin/st-info` sind Python-Programme, die zuerst auf
dem `PATH` liegen und mit der HTTP-API der Bridge auf `127.0.0.1:3335` sprechen. Sie existieren,
damit die eigenen Skripte von cads-zero (`scripts/flash.sh`, `scripts/build.sh`, die Tasks)
unverändert im Container laufen, wo die echten stlink-Werkzeuge kein USB-Gerät fänden.

## st-flash

| Aufruf | Verhalten |
|---|---|
| `st-flash write <file> <addr>` | `POST /flash?addr=<addr>` mit der Datei als Body. `.bin` wird unverändert gesendet; eine `.elf` wird vorher mit `objcopy` umgewandelt. Exit 0 bei Erfolg. |
| `st-flash reset` | `POST /reset`. |
| `st-flash --serial <id> …` | `--serial` wird akzeptiert und ignoriert: es gibt genau eine Probe, die in deinem Browser. |
| `st-flash erase` | verweigert: `error: erase is not permitted by CaDS lab policy (no mass erase, docs/SAFETY.md)`, Exit 1. |
| jedes Kommando ohne erreichbare Bridge | `Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)`, Exit 1. |

Schreibvorgänge werden nur innerhalb von `0x08000000–0x080FFFFF` angenommen (das erste
Megabyte, Flash-Bank 1). Die Bridge prüft das Fenster unabhängig vom Shim noch einmal.

## st-info

| Aufruf | Ausgabe |
|---|---|
| `st-info --probe` | `GET /probe`, wörtlich ausgegeben im stlink-Textformat: `serial`, `chipid 0x419`, `descr STM32F42x_F43x`, `flash 2097152 (pagesize: 16384)`, `sram`. |
| `st-info --serial` / `--chipid` / `--flash` / `--sram` / `--descr` / `--pagesize` | ein Feld, aus demselben Bericht geparst. |
| ohne erreichbare Bridge | der deutsche Hinweis oben, Exit 1. |

## Die Shims testen

Das Repository testet sie gegen eine simulierte HTTP-Bridge, ohne Docker:

```bash
python3 -m unittest discover -s tests/shims -v
```
