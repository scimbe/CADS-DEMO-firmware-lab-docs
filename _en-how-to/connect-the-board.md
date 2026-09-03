---
title: Connect the board
order: 1
description: Browser requirements, the device chooser, and what macOS, Windows and Linux need before the ST-Link is usable from the browser
---

The board is plugged into your own computer, and the browser talks to it with WebUSB (ST-Link,
flashing and debugging) and WebSerial (the console). The container never sees the USB device.

## Browser

| Browser | Works | Note |
|---|---|---|
| Google Chrome | yes | WebUSB and WebSerial are available. |
| Microsoft Edge | yes | Same engine as Chrome. |
| Chromium, Brave, Vivaldi, Opera | usually | Chromium-based; some builds disable the device APIs. Test with `chrome://device-log` if in doubt. |
| Firefox | no | No WebUSB, no WebSerial. |
| Safari | no | No WebUSB, no WebSerial. |

The lab must be served over **HTTPS** (or from `localhost`/`127.0.0.1` for a local container).
Chromium exposes `navigator.usb` and `navigator.serial` only on secure origins. The production
lab sits behind a TLS edge, so this is only a concern for self-hosted copies.

Company or school-managed browsers may block the APIs by policy (`DefaultWebUsbGuardSetting`,
`DefaultSerialGuardSetting`). Symptom: the chooser never opens. Check `chrome://policy`.

## Cable and port

Use the **ST-Link USB port** of the NUCLEO board (the Micro-USB connector on the ST-Link part
of the board, at the opposite end from the Ethernet jack), not the user USB port. The one cable
carries both the SWD debug link and the virtual COM port.

The device the chooser shows is *STM32 STLink*, vendor id `0x0483`, product id `0x374B`
(ST-Link/V2-1).

## Connect

1. Log in and open the workspace.
2. Click the status bar item **Board: getrennt** and choose *Board verbinden (USB/Serial
   freigeben)*, or run **F1 → CaDS Board: Verbinden**.
3. In the USB dialog select *STM32 STLink*, then in the serial dialog the ST-Link's COM port.
4. The status bar changes to **Board: verbunden · läuft**.

The chooser is a browser dialog and needs a click from you; nothing in the lab can open it on
its own. Both grants are stored per origin, so the next session and every replug reconnect
without a dialog (see [Reconnect after a replug]({{ '/en/how-to/reconnect-after-replug/' | relative_url }})).

## macOS

- No driver is needed. The ST-Link shows up as a USB device and a `/dev/cu.usbmodem…` port.
- macOS mounts the Nucleo's mass-storage drive **`NOD_F429ZI`** on every plug-in and writes
  metadata files to it unasked. The ST-Link interprets writes to that drive as firmware for
  `0x08000000`; the cads-zero project has recorded a real flash corruption from this (a cleared
  bit in the initial stack pointer, board hung in `Reset_Handler`). Unmount it after every
  replug:

  ```bash
  diskutil list external            # find the disk number N
  diskutil unmountDisk /dev/diskN
  ```

  A permanent fix is an `/etc/fstab` entry `LABEL=NOD_F429ZI none msdos rw,noauto` (needs sudo).
  If the board ever shows wild LEDs after a replug, reflash it before theorising.

## Windows

- WebUSB on Windows can only open devices bound to the generic WinUSB driver. If Chrome's
  chooser does not list the ST-Link, a vendor driver (ST-Link, STM32CubeProgrammer) has claimed
  the debug interface; switch that interface to WinUSB with Zadig or Device Manager.
- The COM port appears as `STMicroelectronics STLink Virtual COM Port (COMx)`.

## Linux

- The browser needs read/write access to the USB device node. Install the standard stlink udev
  rule and replug:

  ```bash
  sudo tee /etc/udev/rules.d/49-stlinkv2-1.rules >/dev/null <<'EOF'
  SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="374b", MODE:="0666", TAG+="uaccess"
  EOF
  sudo udevadm control --reload-rules && sudo udevadm trigger
  ```

- The serial port is `/dev/ttyACM0` (or higher). Your user must be in the `dialout` group
  (`plugdev` on some distributions) to open it. Log out and in after adding yourself.
- Snap- or Flatpak-packaged browsers may not see USB devices at all; use the distribution
  package or the vendor `.deb`.

## Check

`st-info --probe` in the integrated terminal prints the ST-Link serial, `chipid 0x419`
(STM32F42x/F43x) and the flash size when the board is connected, and the hint
`Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)` when it is not.
