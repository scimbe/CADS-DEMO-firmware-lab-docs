---
title: Safety rules
order: 4
description: No mass erase, a fixed flash window, halt before flash, never option bytes, and why each rule exists
---

The board is the student's own, the flash holds a file system, and the ST-Link protocol is easy
to break. The lab therefore enforces cads-zero's `docs/SAFETY.md` at three layers: the shims,
the bridge and the probe driver. A student cannot switch any of them off.

## No mass erase, ever

`st-flash erase` is refused by the shim with *erase is not permitted by CaDS lab policy*. The
GDB server does not implement a mass-erase monitor command, and the probe driver contains no
mass-erase operation at all. Reason: a chip erase would take the littlefs volume in flash bank 2
with it, and on a board configured for it could touch option bytes. `st-flash write` erases only
the sectors it writes; a typical image touches the first few sectors of bank 1 and nothing else.

## A fixed flash window

Writes are accepted only inside **`0x08000000–0x080FFFFF`**, the first megabyte. The shim
checks the address and size, the bridge checks again independently, and cads-zero's own linker
script refuses to place anything into `FLASH_FS` (`0x08120000` onwards). An image that grew
past the window fails at link time, not on the board.

## Halt, do not reset, before flashing

The firmware arms the independent watchdog (IWDG). The stock ST-Link flow resets the core
before programming, which on this board lets the watchdog fire in the middle of the sequence.
The probe driver carries the hardware-verified CaDS fix: it **halts** the core, programs,
verifies, and resets afterwards. This is the reason the lab ports its own driver instead of
using an unmodified one.

## Option bytes are never written

Read-protection is either annoying or permanent. No layer of the lab has a code path that
writes option bytes.

## One client on the probe, operations serialised

The ST-Link's protocol state machine desyncs when a client is killed mid-transfer; every later
command then times out until a physical replug. The probe serialises every operation behind a
mutex and puts a timeout on every USB transaction, the bridge serialises all probe calls, and
only one GDB session may be attached. A debug session that ends cleanly resumes the target;
a page reload in the middle of a flash is the one thing the lab cannot protect against, which
is why the *Reconnect after a replug* page exists.

## macOS and the `NOD_F429ZI` drive

Not a lab layer but a documented hazard: macOS mounts the Nucleo's mass-storage drive on every
plug-in and writes metadata to it; the ST-Link treats such writes as firmware for
`0x08000000`. The cads-zero project recorded a real corruption of the initial stack pointer
word from this. Unmount the drive after every replug.
