---
title: Limits
order: 5
description: What the browser-bridged architecture cannot do as well as a desktop setup, and what is still being verified
---

## Latency on every probe operation

Each GDB packet that needs the target (read memory, read registers, step) becomes at least one
command round trip from the container to the web worker in your browser and back, over the
WebSocket and, in production, over the TLS tunnel. A local container measures 16–18 ms for a
trivial ping; over the internet it is your round-trip time plus the USB transaction. The bridge
batches operations and caches memory while the core is halted, so opening a call stack is one
burst rather than dozens of trips, but single-stepping through a loop is noticeably slower than
with a probe on the desktop. Exact numbers over the tunnel are being recorded with real
hardware and will be added here.

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

## What is still in verification

At the time of writing, the board bridge (`cads-probe`, `cads-board-bridge`) has passed its
feasibility test in the local container (web extension in the worker, USB and serial reachable,
container ↔ worker round trip) and its driver port is unit-tested, while the end-to-end flash,
debug and console paths are being verified against the real ITSboard. Pages that describe these
paths carry a note and get their screenshots once the hardware run is recorded.
