---
title: Warum das Board am Browser hängt
order: 1
description: Die Architektur hinter Flashen und Debuggen eines Boards, das am Rechner des Studierenden steckt, während die IDE auf einem Server läuft
---

## Die Randbedingung

Die IDE läuft in einem Container auf einem Server. Das Board liegt auf dem Schreibtisch des
Studierenden. Serverseitiges USB-Passthrough würde verlangen, dass das Board am Server hängt,
was es nicht tut, und unter Docker Desktop auf macOS funktioniert es ohnehin nicht. Der einzige
Rechner, der die ST-Link anfassen kann, ist also der, auf dem der Browser läuft.

Chromium bietet genau dafür zwei APIs: **WebUSB** (rohe USB-Transfers, genug, um das
ST-Link-Protokoll zu implementieren) und **WebSerial** (den virtuellen COM-Port). Beide brauchen
einmal je Origin eine Nutzergeste und einen Geräte-Dialog und merken sich die Freigabe danach.

## Wo der Treiber läuft (ADR-001)

VS Code for the Web hat einen zweiten Extension-Host, der in einem **Web Worker** im Browser
läuft. Zwei Fakten wurden auf code-server 4.135 verifiziert, bevor irgendetwas gebaut wurde:
Dieser Worker läuft in einem iframe mit `allow="usb; serial; hid"`, sodass `navigator.usb` und
`navigator.serial` dort definiert sind; und die Workbench stellt die Kommandos
`workbench.experimental.requestUsbDevice` und `requestSerialPort` bereit, die den nativen
Geräte-Dialog aus dem Hauptfenster öffnen und das freigegebene Gerät an den Worker durchreichen.

Dort lebt `cads-probe`. Es ist eine Web-Extension mit ausschließlich einem `browser`-Einstieg
und enthält eine TypeScript-Portierung des hardware-verifizierten Treibers *webstlink*
(ST-Link-V2-Protokoll, STM32-Flash-Algorithmus, mit dem CaDS-Fix, vor dem Flashen anzuhalten
statt zurückzusetzen). Der Treiber-Code hat keine Abhängigkeit von VS Code oder dem DOM und
könnte deshalb auch in einer Webview laufen; dieser Fallback wurde entworfen, erwies sich aber
als unnötig.

```
Browser des Studierenden                            Container
┌──────────────────────────────────┐  WebSocket   ┌──────────────────────────────────┐
│ VS-Code-Workbench                │◄────────────►│ Node-Extension-Host              │
│  └─ Web-Worker-Extension-Host    │ executeCommand│  ├─ cads-board-bridge            │
│      └─ cads-probe               │ beide Richt. │  │   ├─ GDB-Server  127.0.0.1:3333│
│          ├─ WebUSB  → ST-Link    │              │  │   ├─ Seriell-TCP 127.0.0.1:3334│
│          └─ WebSerial → Konsole  │              │  │   └─ HTTP-Shims  127.0.0.1:3335│
└──────────────────────────────────┘              │  ├─ cads-tutor                   │
        ▲ USB                                     │  └─ cortex-debug (external)      │
   ST-Link + ITSboard                             └──────────────────────────────────┘
```

## Wie der Container sie erreicht

Extensions in verschiedenen Hosts können sich gegenseitig mit `vscode.commands.executeCommand`
aufrufen. Die Bridge im Container schickt Probe-Operationen (`halt`, `readMem`, `flash`, …) als
Kommandos an den Worker; die Probe antwortet mit JSON, Binärdaten als base64, und schiebt
Events (`halted`, `serial-data`, `flash-progress`, `usb-disconnect`) über ein Kommando zurück,
das die Bridge registriert hat. Round-Trip für einen trivialen Ping, im lokalen Container
gemessen: 16–18 ms.

## Warum ein GDB-Server und kein neuer Debugger (ADR-002)

Drei Optionen standen zur Wahl: einen Debug-Adapter über die Probe schreiben, OpenOCD oder
`st-util` im Container betreiben, oder einen **GDB-Remote-Protocol-Server** in die Bridge legen
und cortex-debug als `external`-Server daran anbinden. Die erste hätte bedeutet, SVD-, Memory-
und RTOS-Ansichten neu zu implementieren; die zweite braucht USB am Server. Die dritte lässt
cortex-debug, peripheral-viewer, memory-view und rtos-views unverändert: F5, Breakpoints,
Stepping, Register und `load` sprechen alle GDB, und die Bridge übersetzt GDB-Pakete in
Probe-Operationen. `st-flash` und `st-info` werden aus demselben Grund dünne HTTP-Shims: Die
cads-zero-Skripte funktionieren weiter beim Namen.

## Was das kostet

Jede Probe-Operation ist ein Round-Trip Browser ↔ Container. Die Bridge bündelt Operationen,
cacht Speicher, solange der Core angehalten ist, und serialisiert alles über einen Mutex, aber
ein einzelner Schritt reist trotzdem durch den Tunnel. Siehe
[Grenzen]({{ '/de/explanation/limits/' | relative_url }}). Die Lebensdauer ist der Browser-Tab:
Ihn zu schließen trennt das Board; ihn neu zu öffnen verbindet ohne Geräte-Dialog wieder.
