---
title: Reconnect after a replug
order: 2
description: What happens when you unplug the board, and how to get the ST-Link back without a new chooser dialog
---

## Normal case: nothing to do

The browser remembers the devices you granted for this origin. When you unplug the board, the
status bar goes back to **Board: getrennt**. When you plug it in again, the probe extension
receives the browser's `connect` event, reopens the ST-Link and the serial port, and the bridge
refreshes the status bar. No dialog.

The same happens at startup: about 1.5 s after the extension host is up, the bridge asks the
probe to reconnect any granted device, so a page reload keeps the board connected.

## If the status bar stays "getrennt"

1. Run **F1 → CaDS Probe: Reconnect granted devices**. This re-enumerates the granted USB
   devices and serial ports without a chooser.
2. If that does not help, run **F1 → CaDS Board: Verbinden** and pick the device again in the
   chooser. Choosing it a second time does no harm.
3. On macOS, unmount the `NOD_F429ZI` drive after each replug (see
   [Connect the board]({{ '/en/how-to/connect-the-board/' | relative_url }}#macos)).

## If the ST-Link answers but the target does not

`st-info --probe` printing `chipid 0x000` means the ST-Link is fine but the core is not
reachable. This is what a "wedged" ST-Link looks like; it happens after an SWD client was killed
mid-transfer, for example a debug session that ended in a page reload during a flash. Recovery,
in order:

1. **Replug** the board's USB cable. This resets the ST-Link's protocol state machine; nothing
   short of that does.
2. Unmount `NOD_F429ZI` (macOS).
3. Reconnect (steps above) and press **Reset** in the board menu.
4. If the board then boots into wild LEDs, reflash it with **CaDS: Build + Flash** before
   assuming anything else is wrong.

## Debug session and replug

A replug during a debug session ends the session; cortex-debug reports that the GDB server went
away. Stop the session, reconnect, start again with F5. Only one client may hold the probe: a
stale session that still thinks it is attached blocks the next one, so always press Stop before
starting over.
