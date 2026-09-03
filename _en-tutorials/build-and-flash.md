---
title: Build and flash the board
order: 2
description: Run the task "CaDS: Build + Flash", connect the board in the browser and put your firmware on the chip
---

In this tutorial you build the firmware in the container and flash it to the board that is
plugged into **your** computer. The container has no USB access at all. The ST-Link is driven
from your browser and bridged into the container; that is why the browser asks you to pick the
device once.

<div class="callout warn">
The board bridge (the extensions <code>cads-probe</code> and <code>cads-board-bridge</code>) is being
verified against real hardware while this page is written. Behaviour below follows the
specification and the bridge's own code; screenshots of the board panel and the flash progress
follow once the hardware run is recorded.
</div>

## What you need

- The ITSboard (NUCLEO-F429ZI with the ITS adapter and the display shield) connected to your
  computer with a USB cable on the ST-Link port.
- Chrome or Edge. See [Connect the board]({{ '/en/how-to/connect-the-board/' | relative_url }})
  for operating-system notes (udev rule on Linux, the `NOD_F429ZI` drive on macOS).

## 1. Build only

Open the task picker with **F1 → Tasks: Run Task** and type `CaDS:`.

<figure>
<img src="{{ '/assets/04-task-picker.png' | relative_url }}" alt="Task picker filtered to CaDS: with Build, Flash, Build + Flash, Host tests, Golden images, RAM budget">
<figcaption>The lab tasks. "CaDS: Build" is also the default build task (Ctrl+Shift+B).</figcaption>
</figure>

Pick **CaDS: Build**. The task runs `cmake --preset itsboard && cmake --build build/itsboard`
with the ARM GNU toolchain 13.3.rel1 and ends with the linker's memory report.

<figure>
<img src="{{ '/assets/05-build-task.png' | relative_url }}" alt="Task terminal after CaDS: Build with the ninja output and the memory usage table">
<figcaption>A finished build. FLASH_FS stays at 0 B; the linker refuses images that would collide with the file system.</figcaption>
</figure>

The artefacts are `build/itsboard/cads-zero.elf`, `.bin` and `.hex`. Nothing has touched the
board yet.

## 2. Connect the board

Click the status bar item **Board: getrennt** (or run **F1 → CaDS Board: Verbinden**). The
bridge asks the browser to show its device chooser, filtered to STMicroelectronics devices
(vendor id `0x0483`). Two dialogs appear one after the other:

1. **USB device**: pick *STM32 STLink*. This is the SWD path for flashing and debugging.
2. **Serial port**: pick the ST-Link's virtual COM port. This is the console at 115200 baud.

Both choices are remembered by the browser for this origin. After a replug the bridge picks the
devices up again without a new chooser.

When the connection is up, the status bar reads `Board: verbunden · läuft` and the tooltip shows
the ST-Link version, the detected device (`STM32F42x_F43x`) and the flash size. Clicking the item
opens a small menu: *Flash*, *Reset*, *Anhalten* / *Weiterlaufen lassen*, *Konsole öffnen*,
*Log anzeigen*, *Trennen*.

If the chooser does not appear at all, read
[Troubleshooting → The chooser does not appear]({{ '/en/how-to/troubleshooting/' | relative_url }}#the-device-chooser-does-not-appear).

## 3. Build + Flash

Run **F1 → Tasks: Run Task → CaDS: Build + Flash**. It runs the build task and then:

```bash
st-flash write build/itsboard/cads-zero.bin 0x08000000 && st-flash reset
```

`st-flash` in the container is not the stlink tool. It is a small shim that talks to the bridge's
HTTP API on `127.0.0.1:3335`, which forwards the image to the ST-Link in your browser. A
notification *CaDS: Flash cads-zero.bin* shows the phases *erase*, *program* and *verify*;
afterwards the status bar shows `Flash ok: <bytes> Bytes in <ms> ms` for a few seconds, and
`st-flash reset` restarts the board.

Before writing, the probe **halts** the core instead of resetting it. That matters on this board:
the firmware arms the independent watchdog, and a reset in the middle of a flash sequence would
let the watchdog fire. The bridge also refuses any write outside `0x08000000–0x080FFFFF` and
never performs a mass erase (see [Safety rules]({{ '/en/explanation/safety-rules/' | relative_url }})).

The board boots, runs its self-test and prints TAP lines on the console. The tutor step
*Flash and pass the hardware gate* checks exactly this: a flash since the step started and a
`RESULT: PASS` on the serial line.

## 4. When the shim says "Board-Bridge nicht aktiv"

If you run a flash task before the board is connected, the shim prints

```
Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)
```

and exits with status 1. Nothing is broken: the bridge's HTTP port is only served while the
extension host is running and the board is connected. Connect the board via the status bar item
and run the task again. You can check the state at any time with `st-info --probe` in the
terminal.

<figure>
<img src="{{ '/assets/06-terminal-st-info.png' | relative_url }}" alt="Integrated terminal: st-info --probe prints the German hint that the board bridge is not active; arm-none-eabi-gcc reports version 13.3.1">
<figcaption>Without a connected board the shims say so. The toolchain is there regardless.</figcaption>
</figure>

## Where you are now

Your build runs on the chip. The next tutorial stops it on a breakpoint:
[Debug with F5]({{ '/en/tutorials/debug-with-f5/' | relative_url }}).
