---
title: Ports und Kommandos der Bridge
order: 2
description: Die drei Loopback-Ports der Board-Bridge (3333 GDB, 3334 Seriell, 3335 HTTP), ihre HTTP-Endpunkte, Kommandos und Einstellungen
---

`cads-board-bridge` läuft im Node-Extension-Host des Containers und bedient drei TCP-Ports
ausschließlich auf `127.0.0.1`. Jede Anfrage endet als Kommando an `cads-probe` im Browser,
die die USB- und Seriell-Verbindungen hält.

## Ports

| Port | Protokoll | Client | Einstellung |
|---|---|---|---|
| 3333 | GDB Remote Serial Protocol | cortex-debug (`gdbTarget: 127.0.0.1:3333`), jedes `arm-none-eabi-gdb`/`gdb-multiarch` mit `target extended-remote` | `cads.board.gdbPort` |
| 3334 | rohes TCP, die serielle Leitung des Boards | `socat`, Skripte; die Bridge selbst verknüpft ihn mit dem PTY `/home/coder/board-console`, wo `socat` vorhanden ist | `cads.board.serialPort` |
| 3335 | HTTP | die Shims `st-flash` und `st-info`, Tooling | `cads.board.httpPort` |

## HTTP-API (Port 3335)

| Methode und Pfad | Wirkung |
|---|---|
| `GET /status` | Board-Status als JSON: `connected`, `serialOpen`, `core`, `lastFlash`, `gdbClients` |
| `GET /probe` | Probe-Bericht im Textformat von `st-info --probe` (serial, chipid, flash, sram, descr, pagesize) |
| `POST /flash?addr=0x08000000` | Body: rohe Image-Bytes; löscht, programmiert und verifiziert; 4xx außerhalb des erlaubten Fensters |
| `POST /reset` | Core zurücksetzen |
| `POST /halt` | Core anhalten |
| `POST /op` | eine Probe-Operation als JSON (Tests und Tooling) |
| `POST /command` | ein Bridge-Kommando ausführen (Tests und Tooling); abschaltbar mit `cads.board.httpCommandsEnabled: false` |
| `GET /log`, `GET /serial` | Bridge-Log und die letzten seriellen Zeilen |
| `POST /erase` | immer `403 not permitted` (kein Mass-Erase) |

## GDB-Server (Port 3333)

Implementierte Pakete: `?`, `g`, `G`, `p`, `P`, `m`, `M`, `X`, `c`, `s`, `vCont?`, `vCont;c/s`,
`Z0`–`Z4`/`z*` (Software- und Hardware-Breakpoints, Watchpoints), `k`, `D`, `qSupported`,
`qAttached`, `qXfer:features:read` (Cortex-M4F-Target-Beschreibung),
`qXfer:memory-map:read` (Flash `0x08000000` 2 MB in Sektoren, RAM `0x20000000` 192 KB, CCM
`0x10000000` 64 KB, dazu der Peripherie-Bereich `0x40000000` und PPB/SCS bei `0xE0000000`, als
RAM deklariert, damit GDB Register- und Peripherie-Reads zulässt), `vFlashErase`/`vFlashWrite`/`vFlashDone` (damit `load` in GDB über die
Probe flasht), `qRcmd` (`monitor reset`, `monitor reset halt`, `monitor halt`), Ctrl-C zum
Anhalten, No-Ack-Modus. Speicherlesungen werden gecacht, solange der Core angehalten ist, und
bei run, step oder write verworfen. Alle Probe-Aufrufe sind serialisiert; ein Probe-Fehler
antwortet mit `E01` und erscheint in der Statusleiste.

## Kommandos (F1)

| Kommando | Titel in der Befehlspalette |
|---|---|
| `cads.board.connect` | CaDS Board: Verbinden (USB/Serial freigeben) |
| `cads.board.disconnect` | CaDS Board: Trennen |
| `cads.board.flash` | CaDS Board: Flash (build/itsboard/cads-zero.bin) |
| `cads.board.reset` | CaDS Board: Reset |
| `cads.board.halt` / `cads.board.run` | CaDS Board: Anhalten / Weiterlaufen lassen |
| `cads.board.openConsole` | CaDS Board: Konsole öffnen |
| `cads.board.status` | CaDS Board: Status (JSON) |
| `cads.board.showPanel` | CaDS Board: Log anzeigen (Output-Channel) |
| `cads.board.showMenu` | CaDS Board: Menü (auch am Statusleisten-Element) |
| `cads.probe.requestDevices` | CaDS Probe: Request USB/Serial devices |
| `cads.probe.reconnect` | CaDS Probe: Reconnect granted devices |
| `cads.probe.diag` | CaDS Probe: Diagnose (getDevices/getPorts) |
| `cads.bridge.ping` | CaDS Bridge: Ping probe (host capabilities) |

## Statusleiste

`Board: getrennt`, wenn keine Probe offen ist. Sonst `Board: verbunden · <angehalten|läuft>`,
gefolgt von `· Konsole`, solange der serielle Port offen ist, und `· GDB`, solange ein Debugger
angehängt ist. Ein angehaltener Core ohne Debugger wird mit Warnhintergrund angezeigt. Der
Tooltip nennt ST-Link-Version, Gerätenamen, Flash-Größe und das Ergebnis des letzten Flash.

## Einstellungen

| Einstellung | Standard | Bedeutung |
|---|---|---|
| `cads.board.gdbPort` / `serialPort` / `httpPort` | 3333 / 3334 / 3335 | Loopback-Ports |
| `cads.board.baud` | 115200 | Baudrate der Konsole |
| `cads.board.consoleLink` | `/home/coder/board-console` | mit `socat` erzeugter PTY-Link für die cads-zero-Skripte |
| `cads.board.defaultImage` | `build/itsboard/cads-zero.bin` | Image für *Flash* ohne Argument |
| `cads.board.gdbPath` | `arm-none-eabi-gdb` | GDB, das an cortex-debug übergeben wird |
| `cads.board.verbose` | false | RSP-Pakete und serielle Zeilen loggen |
| `cads.board.httpCommandsEnabled` | true | `POST /command` erlauben |

## Exports für andere Extensions

`vscode.extensions.getExtension('cads.cads-board-bridge').exports` liefert `getStatus()`,
`onDidChangeStatus`, `onSerialLine`, `onEvent` (`flash-done`, `flash-failed`, `reset`,
`debug-start`, `debug-stop`, `debug-end`), `flash(file?)`, `sendSerial(text)` und
`waitForSerial(pattern, timeoutMs)`. Die Board-Checks des Tutors nutzen genau diese API.
