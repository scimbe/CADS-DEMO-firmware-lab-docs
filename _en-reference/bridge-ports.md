---
title: Bridge ports and commands
order: 2
description: The three loopback ports of the board bridge (3333 GDB, 3334 serial, 3335 HTTP), its HTTP endpoints, commands and settings
---

`cads-board-bridge` runs in the container's Node extension host and serves three TCP ports on
`127.0.0.1` only. Every request ends up as a command to `cads-probe` in the browser, which owns
the USB and serial connections.

## Ports

| Port | Protocol | Client | Setting |
|---|---|---|---|
| 3333 | GDB remote serial protocol | cortex-debug (`gdbTarget: 127.0.0.1:3333`), any `arm-none-eabi-gdb`/`gdb-multiarch` with `target extended-remote` | `cads.board.gdbPort` |
| 3334 | raw TCP, the board's serial line | `socat`, scripts; the bridge itself links it to the PTY `/home/coder/board-console` where `socat` is present | `cads.board.serialPort` |
| 3335 | HTTP | the shims `st-flash` and `st-info`, tooling | `cads.board.httpPort` |

## HTTP API (port 3335)

| Method and path | Effect |
|---|---|
| `GET /status` | board status as JSON: `connected`, `serialOpen`, `core`, `lastFlash`, `gdbClients` |
| `GET /probe` | probe report in `st-info --probe` text format (serial, chipid, flash, sram, descr, pagesize) |
| `POST /flash?addr=0x08000000` | body: raw image bytes; erases, programs and verifies; 4xx outside the allowed window |
| `POST /reset` | reset the core |
| `POST /halt` | halt the core |
| `POST /op` | one probe operation as JSON (tests and tooling) |
| `POST /command` | run a bridge command (tests and tooling); can be disabled with `cads.board.httpCommandsEnabled: false` |
| `GET /log`, `GET /serial` | bridge log and recent serial lines |
| `POST /erase` | always `403 not permitted` (no mass erase) |

## GDB server (port 3333)

Implemented packets: `?`, `g`, `G`, `p`, `P`, `m`, `M`, `X`, `c`, `s`, `vCont?`, `vCont;c/s`,
`Z0`–`Z4`/`z*` (software and hardware breakpoints, watchpoints), `k`, `D`, `qSupported`,
`qAttached`, `qXfer:features:read` (Cortex-M4F target description),
`qXfer:memory-map:read` (flash `0x08000000` 2 MB in sectors, RAM `0x20000000` 192 KB, CCM
`0x10000000` 64 KB, plus the peripheral space `0x40000000` and the PPB/SCS at `0xE0000000`
declared as RAM so GDB allows register and peripheral reads), `vFlashErase`/`vFlashWrite`/`vFlashDone` (so `load` in GDB flashes through
the probe), `qRcmd` (`monitor reset`, `monitor reset halt`, `monitor halt`), Ctrl-C to halt,
no-ack mode. Memory reads are cached while the core is halted and invalidated on run, step or
write. All probe calls are serialised; a probe error answers `E01` and shows in the status bar.

## Commands (F1)

| Command | Title in the palette |
|---|---|
| `cads.board.connect` | CaDS Board: Verbinden (USB/Serial freigeben) |
| `cads.board.disconnect` | CaDS Board: Trennen |
| `cads.board.flash` | CaDS Board: Flash (build/itsboard/cads-zero.bin) |
| `cads.board.reset` | CaDS Board: Reset |
| `cads.board.halt` / `cads.board.run` | CaDS Board: Anhalten / Weiterlaufen lassen |
| `cads.board.openConsole` | CaDS Board: Konsole öffnen |
| `cads.board.status` | CaDS Board: Status (JSON) |
| `cads.board.showPanel` | CaDS Board: Log anzeigen (output channel) |
| `cads.board.showMenu` | CaDS Board: Menü (also bound to the status bar item) |
| `cads.probe.requestDevices` | CaDS Probe: Request USB/Serial devices |
| `cads.probe.reconnect` | CaDS Probe: Reconnect granted devices |
| `cads.probe.diag` | CaDS Probe: Diagnose (getDevices/getPorts) |
| `cads.bridge.ping` | CaDS Bridge: Ping probe (host capabilities) |

## Status bar

`Board: getrennt` when no probe is open. Otherwise `Board: verbunden · <angehalten|läuft>`
followed by `· Konsole` while the serial port is open and `· GDB` while a debugger is attached.
A halted core without a debugger is shown with a warning background. The tooltip lists the
ST-Link version, device name, flash size and the last flash result.

## Settings

| Setting | Default | Meaning |
|---|---|---|
| `cads.board.gdbPort` / `serialPort` / `httpPort` | 3333 / 3334 / 3335 | loopback ports |
| `cads.board.baud` | 115200 | console baud rate |
| `cads.board.consoleLink` | `/home/coder/board-console` | PTY link created with `socat` for the cads-zero scripts |
| `cads.board.defaultImage` | `build/itsboard/cads-zero.bin` | image for *Flash* without argument |
| `cads.board.gdbPath` | `arm-none-eabi-gdb` | GDB handed to cortex-debug |
| `cads.board.verbose` | false | log RSP packets and serial lines |
| `cads.board.httpCommandsEnabled` | true | allow `POST /command` |

## Exports for other extensions

`vscode.extensions.getExtension('cads.cads-board-bridge').exports` provides `getStatus()`,
`onDidChangeStatus`, `onSerialLine`, `onEvent` (`flash-done`, `flash-failed`, `reset`,
`debug-start`, `debug-stop`, `debug-end`), `flash(file?)`, `sendSerial(text)` and
`waitForSerial(pattern, timeoutMs)`. The tutor's board checks use exactly this API.
