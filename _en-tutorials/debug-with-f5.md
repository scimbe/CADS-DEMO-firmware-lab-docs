---
title: Debug with F5
order: 3
description: Start the configuration "Debug CaDS Zero (Board im Browser)", stop on a breakpoint, step, read registers and peripherals
---

Debugging in the lab works like in a desktop IDE: F5, breakpoints in the gutter, a debug toolbar,
the call stack, registers and the peripheral view from the SVD file. The GDB server behind it is
the board bridge inside the container, which drives the ST-Link in your browser.

<div class="callout">
The debug path was verified on 2026-09-03 with real Chrome and the ITSboard: stop at
<code>main</code>, registers, Step Over into <code>cads_bringup_run</code> with a two-frame call
stack and locals, a breakpoint hit during boot, a read of the CPUID register, Continue and Stop.
One step takes about 100 ms end to end, and the screenshot below is from that session.
</div>

## What you need

- A connected board (see [Build and flash]({{ '/en/tutorials/build-and-flash/' | relative_url }})).
  If the board is not connected when you press F5, the bridge asks
  *Das Board ist nicht verbunden. Jetzt verbinden?* and opens the chooser for you.
- No other client on the probe: end a running debug session before starting a new one.

## 1. Set a breakpoint

Open `targets/itsboard/main.c`. It is tiny:

```c
int main(void) {
    cads_hal_init();
    cads_bringup_run();
    for(;;) { __asm volatile("wfi"); }
}
```

Click into the gutter left of the line with `cads_bringup_run();` (line 14). A red dot appears.
This spot sits exactly between "hardware initialised" and "application running".

## 2. Press F5

Open *Run and Debug* (the play icon with the bug in the activity bar). The configuration
**Debug CaDS Zero (Board im Browser)** is preselected.

<figure>
<img src="{{ '/assets/11-run-and-debug.png' | relative_url }}" alt="Run and Debug view with the launch configuration Debug CaDS Zero (Board im Browser) selected">
<figcaption>The launch configuration comes with the workspace; you do not edit launch.json.</figcaption>
</figure>

Press **F5** while the editor has focus. In a browser, F5 only reaches VS Code when the workbench
has keyboard focus; if the page reloads instead, click into the editor first or use the green
start button. What happens then, in order:

1. The `preLaunchTask` **CaDS: Build + Flash** runs, so the ELF you debug is the image on the board.
2. cortex-debug starts `arm-none-eabi-gdb` (a wrapper for `gdb-multiarch` in this image) and
   connects to `127.0.0.1:3333`, the bridge's GDB server (`servertype: external`).
3. The launch command `monitor reset halt` resets and halts the core, then the session runs to
   `main` (`runToEntryPoint`).
4. Execution continues to your breakpoint and stops there.

The debug toolbar appears at the top: Continue, Step Over, Step Into, Step Out, Restart, Stop.
The status bar shows `Board: verbunden · angehalten · GDB`.

## 3. Step and look around

- **Step Over (F10)** executes `cads_bringup_run()` as a unit. It never returns on this firmware,
  so the session keeps running until you pause.
- **Step Into (F11)** enters the function.
- **Call Stack** shows the frames from `main()` upwards. Right after the reset that is a short
  stack: the first stop is a few milliseconds into boot, not where the firmware was before F5.
  That is normal, not a hang.
- **Variables** shows the locals of the selected frame and a **Registers** section with
  `r0`–`r12`, `sp`, `lr`, `pc` and `xPSR`.

Every step and every memory read travels browser ↔ container once. Expect single steps to take
noticeably longer than on a desktop with a local probe; see
[Limits]({{ '/en/explanation/limits/' | relative_url }}).

## 4. Peripherals from the SVD file

The launch configuration loads `targets/itsboard/STM32F429.svd`. While the target is halted, the
*Run and Debug* side bar has a section **XPeripherals** (extension mcu-debug.peripheral-viewer)
listing every peripheral with its base address. Expand `RCC → CR` to see `HSERDY`, or
`GPIOD → ODR` to read what the last output write left on PD0–PD7. Outside a session the section
says *No active debug session*.

<figure>
<img src="{{ '/assets/15-debug-session.png' | relative_url }}" alt="Live debug session: debug toolbar above main.c stopped at line 13, Variables with Local, Global, Static and Registers, Call Stack showing Paused on breakpoint at main, XPeripherals listing ADC1 and CAN1 with their base addresses, and GDB output in the debug console">
<figcaption>A session stopped at <code>main</code>. Call stack, variables and the SVD peripherals all read the real chip; the status bar shows <code>Board: verbunden · angehalten · GDB</code>.</figcaption>
</figure>

Also available from the same extension family: *Memory* (mcu-debug.memory-view) and the RTOS
task list (mcu-debug.rtos-views) once the FreeRTOS scheduler is running.

## 5. Stop

Click the red **Stop** button (Shift+F5). GDB detaches, the bridge resumes the target, and the
firmware keeps running on the board; the status bar drops the `GDB` marker and shows `läuft`.
If you halted the core yourself from the board menu, it stays halted with a warning colour
until you choose *Weiterlaufen lassen* or *Reset* there.

The second configuration, **Attach CaDS Zero (Board im Browser, no flash)**, connects without a
build and without a reset. Use it to look at a running or crashed firmware where it is.

## Where you are now

You can stop the real firmware at a line, step and read its registers. Next: the serial console
and the explorer commands, the fastest way to ask a subsystem what it is doing:
[Serial console and explorer commands]({{ '/en/tutorials/serial-console/' | relative_url }}).
