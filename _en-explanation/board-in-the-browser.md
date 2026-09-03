---
title: Why the board hangs off the browser
order: 1
description: The architecture behind flashing and debugging a board that is plugged into the student's computer while the IDE runs on a server
---

## The constraint

The IDE runs in a container on a server. The board is on the student's desk. Server-side USB
pass-through would require the board to be at the server, which it is not, and it does not work
under Docker Desktop on macOS in any case. So the only computer that can touch the ST-Link is
the one running the browser.

Chromium exposes two APIs for exactly that: **WebUSB** (raw USB transfers, enough to implement
the ST-Link protocol) and **WebSerial** (the virtual COM port). Both need a user gesture and a
chooser dialog once per origin, then remember the grant.

## Where the driver runs (ADR-001)

VS Code for the Web has a second extension host that runs in a **web worker** in the browser.
Two facts were verified on code-server 4.135 before anything was built: that worker runs inside
an iframe with `allow="usb; serial; hid"`, so `navigator.usb` and `navigator.serial` are defined
there; and the workbench provides the commands `workbench.experimental.requestUsbDevice` and
`requestSerialPort`, which open the native chooser from the main window and hand the granted
device to the worker.

That is where `cads-probe` lives. It is a web extension with only a `browser` entry point,
containing a TypeScript port of the hardware-verified *webstlink* driver (ST-Link V2 protocol,
STM32 flash algorithm, with the CaDS fix to halt instead of reset before flashing). The driver
code has no VS Code or DOM dependency, so it could also run in a webview; that fallback was
designed but turned out unnecessary.

```
Student's browser                                   Container
┌──────────────────────────────────┐  WebSocket   ┌──────────────────────────────────┐
│ VS Code workbench                │◄────────────►│ Node extension host              │
│  └─ web-worker extension host    │ executeCommand│  ├─ cads-board-bridge            │
│      └─ cads-probe               │  both ways   │  │   ├─ GDB server  127.0.0.1:3333│
│          ├─ WebUSB  → ST-Link    │              │  │   ├─ serial TCP  127.0.0.1:3334│
│          └─ WebSerial → console  │              │  │   └─ HTTP shims  127.0.0.1:3335│
└──────────────────────────────────┘              │  ├─ cads-tutor                   │
        ▲ USB                                     │  └─ cortex-debug (external)      │
   ST-Link + ITSboard                             └──────────────────────────────────┘
```

## How the container reaches it

Extensions in different hosts can call each other with `vscode.commands.executeCommand`. The
bridge in the container sends probe operations (`halt`, `readMem`, `flash`, …) as commands to
the worker; the probe answers with JSON, binary data as base64, and pushes events (`halted`,
`serial-data`, `flash-progress`, `usb-disconnect`) back with a command the bridge registered.
Round trip for a trivial ping, measured in the local container: 16–18 ms.

## Why a GDB server and not a new debugger (ADR-002)

Three options were on the table: write a Debug Adapter over the probe, run OpenOCD or `st-util`
in the container, or put a **GDB remote-protocol server** into the bridge and let cortex-debug
connect to it as an `external` server. The first would have meant reimplementing SVD, memory and
RTOS views; the second needs USB at the server. The third keeps cortex-debug, peripheral-viewer,
memory-view and rtos-views unchanged: F5, breakpoints, stepping, registers and `load` all speak
GDB, and the bridge translates GDB packets into probe operations. `st-flash` and `st-info`
become thin HTTP shims for the same reason: the cads-zero scripts keep working by name.

## What this costs

Every probe operation is one browser ↔ container round trip. The bridge batches operations,
caches memory while the core is halted and serialises everything on one mutex, but a single
step still travels the tunnel. See [Limits]({{ '/en/explanation/limits/' | relative_url }}).
Lifetime is the browser tab: closing it disconnects the board; reopening it reconnects without
a chooser.
