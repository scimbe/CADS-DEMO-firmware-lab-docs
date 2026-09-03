---
title: Troubleshooting / FAQ
order: 9
description: Real findings from building and testing the lab, with the fix for each
---

Every entry below was hit while building, testing or operating this lab. Generic advice is left
out on purpose.

## The IDE

### The workspace opens in "Restricted Mode" and the extensions are off

You are on an old deployment whose `docker run` did not pass `--disable-workspace-trust`. Since
image tag `next-8a20ec9` the flag is part of the image's own command line, together with
`--disable-telemetry` and `--disable-update-check`, so a plain `docker run` is correct. Ask the
operator to pull the current image. There is no trust dialog to accept any more.

### A CMake Tools notification says "It is recommended to reconfigure after upgrading to a new kits definition"

Seen on the first start of a fresh container from image `next-8a20ec9`, a few seconds after
the workbench loaded. Close it. The lab tasks call `cmake` themselves and do not need CMake
Tools' configuration; *Configure Now* does no harm either, it just runs the `itsboard` preset a
second time. Images built after 2026-09-03 disable the kit scan, so the notification is gone
there.

### The status bar says "No Configure Preset Selected"

Expected. `cmake.configureOnOpen` is off in the image so that nobody is asked for a preset
before doing anything. The tasks **CaDS: Build** and **CaDS: Host tests** run the presets on
their own. If you want CMake Tools' own build button, pick `ITSboard (STM32F429ZI)` in the
status bar once.

### Ctrl+Shift+P does not open the command palette

The browser may intercept the shortcut. **F1** always opens the palette in this environment.
See [Keyboard shortcuts]({{ '/en/reference/keyboard-shortcuts/' | relative_url }}).

### "Cannot reconnect. Please reload the window." after a server restart

The WebSocket to code-server was lost, typically because the operator restarted the container.
Reload the page. Your files are on disk; unsaved editor contents are restored by VS Code's hot
exit where possible, and the tutor resumes its session from `session.json`.

## The board

### The device chooser does not appear

Check in this order:

1. **Browser.** Chrome or Edge. Firefox and Safari have no WebUSB/WebSerial; the *Verbinden*
   command then fails with a `NO_DEVICE` error.
2. **HTTPS.** `navigator.usb` exists only on secure origins. A self-hosted copy reached over
   plain `http://<hostname>` gets no chooser; `http://127.0.0.1` and `localhost` are exempt.
3. **Policy.** Managed browsers can block the device APIs (`DefaultWebUsbGuardSetting`,
   `DefaultSerialGuardSetting`). Look at `chrome://policy`.
4. **Focus.** The chooser is opened by a user gesture in the main window. Click the status bar
   item or run the command from the palette; a command fired from a script does not count.
5. **Linux.** Without the udev rule the device is listed but cannot be opened; see
   [Connect the board]({{ '/en/how-to/connect-the-board/' | relative_url }}#linux).

### "Das Board wird bereits in einem anderen Tab dieses Labors benutzt."

Exactly what it says. A board can be open in one browser tab at a time, and the lab now finds
that out before it touches USB, using a lock shared across every tab of your browser profile.

Close the other tab, or in that tab open the board menu and choose **Board freigeben**. Then
connect again here. If you cannot find the other tab, close every lab tab and reopen one.

### "Ein anderes Programm auf deinem Rechner hält das Board."

A program outside the browser has the ST-Link open: `st-flash`, `st-util`, STM32CubeProgrammer,
an IDE, or a second browser with the lab open. The browser cannot share a USB device with them,
so quit that program and connect again.

This message and the previous one look identical to the browser: both produce
`NetworkError: Unable to claim interface`. The lab tells them apart by whether the lock inside
your own browser profile is taken, which is why the wording differs.

### "Board freigeben" – handing the board to someone else

The board menu has **Board freigeben**. It closes the USB device and the serial port and drops
the lock, so another tab, another program, or the local `st-flash` can use the adapter. It is
the polite counterpart to *Trennen* and the thing to do before you use the host tools.

The lab also releases the board on its own when the extension shuts down. Set
`cads.board.idleReleaseSeconds` if you want it released after the window has been in the
background for a while; it is off by default.

### The lab says the board is not connected, but it is plugged in

<figure>
<img src="{{ '/assets/19-shim-board-not-connected.png' | relative_url }}" alt="Integrated terminal: st-info --probe prints Found 0 stlink programmers, st-flash write ends with error: flash failed: board not connected; the status bar reads Board: getrennt">
<figcaption>The shims when the board has not been connected in the browser. They now print the reason and the next step in German and English underneath.</figcaption>
</figure>

Connect the board from the status bar first. The shims talk to the bridge, and the bridge talks
to the browser; none of them can reach USB on their own.

### "Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)"

Printed by `st-flash` and `st-info` when the bridge's HTTP API on `127.0.0.1:3335` does not
answer. Either the board is not connected in the browser yet, or the extension host is still
starting. Connect via the status bar and run the task again.

### `st-flash erase` says "not permitted by CaDS lab policy"

By design. A mass erase would take the littlefs file system in flash bank 2 with it. `st-flash
write` erases only the sectors it writes. See
[Safety rules]({{ '/en/explanation/safety-rules/' | relative_url }}).

### `st-info --probe` shows `chipid 0x000`

The ST-Link answers but the core does not. This is the "wedged ST-Link" state, caused by an SWD
client that stopped mid-transfer - a page reload during a flash, a debug session that ended hard,
or simply a tab that was closed, which runs no teardown at all.

**Connecting in the lab now tries to repair this by itself.** It never assumes the previous
session ended cleanly: it re-enters SWD, and if the target still does not answer it repeats that
with the reset line held low, which is what `st-info --probe --connect-under-reset` does on the
command line. Two attempts, then it stops rather than hammering the adapter.

If you still see *Der Debug-Adapter reagiert nicht mehr*, the adapter is desynchronised at the USB
level and only a replug fixes it: unplug the cable, plug it back in, unmount `NOD_F429ZI` on
macOS, and connect again. See
[Reconnect after a replug]({{ '/en/how-to/reconnect-after-replug/' | relative_url }}).

There is a reliable way to tell the two apart from a terminal on your own computer: if
`st-info --probe` still prints a real version such as `V2J33S25`, the software recovery has a
chance; if the version line degrades to a bare `V2`, only a replug will do.

### `st-info` on my own computer says "Found 0 stlink programmers"

While the browser holds the ST-Link, no other program on your computer can open it; the local
stlink tools see nothing. That is exclusive access, not a fault. Disconnect the board in the lab
(status bar → *Trennen*) and the local tools see it again.

### Do not run `st-flash` on your own computer while the lab is connected

A local `st-flash reset` fired at the moment the browser released the device wedged the ST-Link
during verification (`LIBUSB_ERROR_TIMEOUT`, then `chipid 0x000`). Use the lab's board menu for
reset and flash; if you need the local tools, disconnect in the lab first and wait a second.

### The `NOD_F429ZI` drive is the single most damaging thing on this board

The ST-Link exposes an MBED drive called `NOD_F429ZI`. Your operating system mounts it whenever
the adapter enumerates and writes metadata to it without being asked - Spotlight indexes,
`.fseventsd`, `._` files. **The ST-Link interprets writes to that drive as firmware for
`0x08000000`.** That has corrupted a real image once here, a single cleared bit in the vector
table's initial-SP word, which left the board hanging in the reset handler with wild LEDs. It is
also one of the ways the adapter stops responding in the middle of a session.

If it already happened, reflash with **CaDS: Build + Flash** - the image is repaired by a plain
rewrite. But do not stop there, because unmounting after the fact is a race with whatever wrote
first. Fix it at the source, best option first:

1. **An adapter firmware without mass storage.** ST's own upgrade tool (STSW-LINK007) offers a
   variant that keeps debug and the virtual COM port but drops the MBED drive. That removes the
   hazard completely and is the right choice for lab-owned boards. We have not run this upgrade
   on the lab board, so treat the exact steps as something to verify against ST's documentation
   for your adapter before you flash it - a failed adapter firmware update is worse than the
   problem it solves.
2. **Stop the automatic mount.** On macOS run `scripts/setup-host-macos.sh` from the bridge
   repository once. It adds `LABEL=NOD_F429ZI none msdos rw,noauto` to `/etc/fstab` and excludes
   the volume from Spotlight, shows you both changes first, and `--undo` reverses them. It needs
   administrator rights once. On Linux install `scripts/60-cads-stlink.rules`, which does the
   same and also grants the USB access the browser needs.
3. **Unmount it every time.** Without administrator rights, run
   `diskutil unmountDisk /dev/diskN` after every replug *and* after every reset - a reset
   re-enumerates the adapter, so the drive comes straight back. This is the weakest option
   because it only closes the window after something may already have written.

### Flashing fails with a verify error

Retry once before anything else. The cads-zero project has observed individual `st-flash write`
calls failing verification late in long sessions and succeeding on retry, with the ST-Link
itself healthy. If it keeps failing, replug and reconnect.

### F5 reloads the page instead of starting the debugger

The keyboard focus was outside the workbench (for example in the browser's address bar). Click
into the editor and press F5 again, or use the green start button in *Run and Debug*.

### The debugger stops at `main()` although the firmware was somewhere else

`monitor reset halt` in the launch configuration resets the target; the first stop is early
boot, not the previous live state. Use the configuration **Attach CaDS Zero (Board im Browser,
no flash)** to look at a running firmware without reset.

### A typed console command does nothing

The board is in the touchscreen app tree, which ignores plain bytes on purpose. Send the quit
byte once: `scripts/board_key.py quit` (see
[Serial console]({{ '/en/tutorials/serial-console/' | relative_url }}#3-get-to-the-prompt)).

## Builds and tests

### The build dies with exit code 137

The container ran out of memory and the kernel killed the compiler. On a shared or small host
the operator sets `CMAKE_BUILD_PARALLEL_LEVEL=1` (or `2`) on the container; the lab tasks inherit
it and build single-threaded. clangd is already capped to four indexing workers with on-disk
precompiled headers. Report the symptom rather than retrying in a loop: every retry at full
parallelism gets killed the same way.

### The golden-image tests fail by a few pixels

Expected in the container: `golden_splash` and `golden_boot_desktop` differ by +1 on
anti-aliased edge pixels because Debian's SDL2 rounds the RGB565 conversion differently from
the SDL the goldens were made with. That is why **CaDS: Host tests** excludes them and
**CaDS: Golden images (informativ)** runs them separately with a note. See
[Host tests]({{ '/en/how-to/host-tests/' | relative_url }}).

### `git status` shows nothing although the container wrote `.vscode/*.json`

Intended. The four `.vscode` files are marked `skip-worktree` and `.clangd` is excluded, so the
container's own configuration never shows up as your change.

## The tutor

### "Ask the tutor" says the language model is not configured

The deployment runs without `TUTOR_LLM_BASE_URL` / `TUTOR_LLM_API_KEY` / `TUTOR_LLM_MODEL`.
Everything else works: file, task and board checks run; question tasks fall back to manual
confirmation; the box still lists the grounded sources it found.

### The tutor refuses a question

"That is outside the indexed reference material for this course" means the retrieval found
nothing above the course's BM25 threshold. Very short questions score low. Name a file, a
register or a symptom and ask again; the tutor answers only from indexed material by design.

### An HTTP 401 from the language model

Seen once on a self-hosted copy: the endpoint URL used `http://` instead of `https://`. The
tutor requires an `https` base URL; fix the URL before touching the key.

### Board checks say "Unavailable"

The board bridge is not installed or not connected. `board`, `flash` and `serialExpect` checks
report *Unavailable* instead of failing so they do not burn a hint tier. Connect the board and
press *Check* again.

## Still stuck?

Open an issue in
[CADS-DEMO-firmware-lab](https://github.com/scimbe/CADS-DEMO-firmware-lab/issues/new) with what
you did, what you saw and the output of `st-info --probe`.
