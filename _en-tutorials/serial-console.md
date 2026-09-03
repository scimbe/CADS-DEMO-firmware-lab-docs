---
title: Serial console and explorer commands
order: 4
description: Open the "CaDS Board Console" terminal, read the self-test and talk to the bring-up explorer with single-letter commands
---

The ST-Link exposes the firmware's USART3 as a virtual COM port. In the lab that port is opened by
your browser (WebSerial) and appears in the container as a terminal named **CaDS Board Console**.
Through it you read the boot self-test and use the firmware's own diagnostic console.

<div class="callout">
Unlike the USB grant, the serial-port grant cannot be pre-seeded: Chrome forgets WebSerial
permissions that were not given through its own dialog. So the console needs <strong>one</strong>
manual chooser click per browser profile; after that the port is reopened across reloads without
a dialog. That click is the one step in this lab that cannot be automated, which is why the
screenshot below was captured a different way - the caption says how.
</div>

## 1. Open the console

Click the status bar item **Board: verbunden …** and choose **Konsole öffnen**, or run
**F1 → CaDS Board: Konsole öffnen**. A terminal opens with a cyan banner:

```
[CaDS Board Console – serielle Konsole des Boards, 115200 Baud. Ctrl-] beendet nicht, Terminal schließen genügt.]
```

If the serial port was not granted yet, the terminal prints a yellow hint instead and you connect
the board first. The status bar then shows `· Konsole` while the port is open.

<figure>
<img src="{{ '/assets/23-console-without-serial-grant.png' | relative_url }}" alt="CaDS Board Console terminal with a cyan banner and a yellow hint that the console is not open and the serial port needs to be granted">
<figcaption>The console before the serial port is granted. The red dot in the gutter is a breakpoint, set in the next tutorial.</figcaption>
</figure>


## 2. Read the boot self-test

Press **Reset** in the board menu. The firmware prints its self-test in TAP format:

```
1..10
ok 1 - SysTick advances at 1 kHz
ok 2 - DWT microsecond clock agrees
...
# flush_pixels: 153600
# flush_us: 448233
# flush_kpixel_per_s: 342
ok 7 - dirty rectangle limits the transfer
# RESULT: PASS
```

<figure>
<img src="{{ '/assets/16-board-console.png' | relative_url }}" alt="Lab terminal showing the board's boot self-test: CaDS Zero v0.1.0 banner, plan 1..10, ten ok lines with diagnostic hash lines, 10/10 passed, RESULT: PASS and EXPLORER ready">
<figcaption>A real boot self-test from the ITSboard, 2026-09-03. Because granting WebSerial needs a manual click that no test harness can perform, this capture was streamed from the host's virtual COM port into a lab terminal rather than through the <strong>CaDS Board Console</strong>; the text is exactly what that console shows once the port is granted.</figcaption>
</figure>

`1..10` is the plan, `ok`/`not ok` are assertions, `#` lines are diagnostics. The tutor's check
`serialExpect` waits for exactly the `RESULT: PASS` line. The number `flush_kpixel_per_s: 342`
is a measurement, not a calculation: a full-screen redraw of 153 600 pixels takes about 448 ms,
because the display's shift-register chain costs 16 SPI clocks per pixel.

## 3. Get to the prompt

A freshly flashed board boots into the touchscreen app tree (`boot.autostart = 1`). That session
**ignores plain typed bytes on purpose**, so a console command does nothing, prints nothing, and
looks like a hung board. Only the reserved quit byte ends it. From the integrated terminal (not
the console) run:

```bash
scripts/board_key.py quit
```

The script needs to know which port to use. In the container the bridge publishes the console as
a raw TCP port `127.0.0.1:3334` and, where `socat` is present, as the PTY link
`/home/coder/board-console`; point the cads-zero scripts at that link:

```bash
CADS_CONSOLE_PORT=/home/coder/board-console scripts/board_key.py quit
```

## 4. Explorer commands

Now the prompt listens. Every command is one character, optionally followed by one or two
arguments. Type into the console terminal:

| Command | What it does |
|---|---|
| `?` | Reprint the help text. The firmware's help string is the ground truth. |
| `i` | Dump the input data register (IDR) of every port once. |
| `w 20` | Watch all ports for changes for 20 s. Press a button on the adapter and see which pin moves. |
| `k` | Task stacks, task count, input counters. |
| `t` | One touch sample from the XPT2046. |
| `p 3` | Draw a test pattern (0 black, 1 blue, 2 green, 3 quadrants, 4 stripes, 5 splash, 6 fonts). |
| `l 100` | Set the on-board LEDs. |
| `e`, `a`, `m` | Ethernet PHY identity and link state, auto-negotiation, MAC counters, all below lwIP. |
| `V` | Re-measure the full-screen flush throughput under scheduler and network load. |
| `d` | Run the app tree live. Ends only with `board_key.py quit`. |

One command, `z FAULT`, is deliberately destructive: it triggers a UsageFault and halts forever
to prove the fault handler works. It demands the literal argument `FAULT`. The full catalogue is
in the workspace at `docs/reference/explorer-console.md`.

From the integrated terminal you can also run a single command non-interactively and capture
its output:

```bash
CADS_CONSOLE_PORT=/home/coder/board-console scripts/board_cmd.py k
```

## 5. What the tutor watches

The tutor subscribes to the console. Three patterns trigger a Socratic note in the step panel
instead of a solution: `HardFault`, `configASSERT` and `RESULT: FAIL`. Each pattern is debounced
for 15 s, so a scrolling fault dump produces one question, not thirty.

## Where you are now

You can read what the firmware says and ask it questions. The last tutorial of this series is
about the tutor itself:
[Learning with the tutor]({{ '/en/tutorials/learning-with-the-tutor/' | relative_url }}).
