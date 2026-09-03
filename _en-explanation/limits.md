---
title: Limits
order: 5
description: What the browser-bridged architecture cannot do as well as a desktop setup, and what is still being verified
---

## Latency on every probe operation

Each GDB packet that needs the target (read memory, read registers, step) becomes at least one
command round trip from the container to the web worker in your browser and back, over the
WebSocket and, in production, over the TLS tunnel. Measured with a local container and real
hardware on 2026-09-03:

| Path | Measured |
|---|---|
| container ↔ web worker command round trip, no USB | 16–23 ms |
| one probe operation end to end (HTTP shim → bridge → worker → WebUSB → ST-Link → back) | 94–115 ms |
| one debugger step | about 100 ms |
| flash of 327 088 bytes with verify | 13.2–13.3 s (about 24 KB/s over WebUSB) |

Over the internet add your round-trip time to the tunnel. The bridge batches operations and
caches memory while the core is halted, so opening a call stack is one burst rather than dozens
of trips, but single-stepping through a loop is noticeably slower than with a probe on the
desktop.

## One board, one browser tab

The probe lives in the web worker of the tab you opened. Closing the tab disconnects the board;
a second tab does not see the grant of the first. Only one GDB client may be attached at a
time, and the tutor's board checks, the console terminal and the debugger all share the same
serialised probe.

## Golden-image tests differ in the container

The host test suite passes in the container except for two golden-image comparisons, which
differ by +1 on anti-aliased edge pixels because Debian's SDL2 rounds RGB565 conversion
differently from the SDL the goldens were generated with. The lab excludes them from the
default test task and runs them in a labelled informational task; regenerating the goldens in
the container is the cads-zero maintainer's call.

## Memory on shared hosts

A cads-zero build peaks at about 1 GB of RAM; extension host, clangd and CMake Tools add a few
hundred MB. On a small host the operator caps `CMAKE_BUILD_PARALLEL_LEVEL`; on the multi-user
stack each container gets 2 GB and 2 CPUs by default.

## The language model is optional

"Ask the tutor", question grading and proactive check-ins need an OpenAI-compatible endpoint
configured by the operator. Without it the tutor still runs every check and shows every hint
and source, but questions fall back to manual confirmation.

## Browser support

WebUSB and WebSerial exist in Chromium-based browsers only. Firefox and Safari can use the
editor, the build tasks and the tutor, but not the board.

## Serial console needs one chooser click

WebUSB grants can be restored by the browser without a dialog; WebSerial grants cannot be
pre-seeded, and the Chrome policy that would allow it needs a managed (MDM) profile. Flash and
debug therefore run without a dialog after the first grant, but the serial console asks once
per browser profile.

## Do not use local ST-Link tools while the lab holds the board

While the browser has the ST-Link open, a locally installed `st-info --probe` reports *Found 0
stlink programmers*; that is exclusive access, not a fault. Running `st-flash` from your own
machine at the moment the browser releases the device can wedge the ST-Link's protocol state
machine (observed once during verification); only a physical replug recovers it.

## What is verified and what is not

The board bridge passed its end-to-end hardware run on 2026-09-03 (connect, flash with verify
and boot, F5 with stop, step, registers and breakpoint, replug, shim path) in a test workspace.
Screenshots of these paths inside the lab workspace are still to be taken; the pages say so
where one is missing.
