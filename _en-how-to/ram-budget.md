---
title: Check the RAM budget
order: 4
description: Run the RAM budget script against the linked ELF and read its margin
---

CaDS Zero runs FreeRTOS without a heap for task stacks: they live in the 64 KB CCM, and lwIP
plus the GUI need at least 48 KB of heap in the main SRAM. The project keeps a script that
reads the linked ELF and checks these numbers against a budget, so a change that eats too much
RAM fails here instead of on the board.

## Run

**F1 → Tasks: Run Task → CaDS: RAM budget**, or in the terminal:

```bash
python3 scripts/check_ram_budget.py build/itsboard/cads-zero.elf
```

The ELF must exist, so build first (**CaDS: Build**). On the seeded commit the script prints:

```
PASS: 928 B of margin, budget is 256 B
```

The margin is what is left above the required reserve; the budget is the minimum margin the
project accepts. A `FAIL` names the section that grew.

## Read the linker report

Every firmware link also prints the memory report at the end of the build task:

```
Memory region         Used Size  Region Size  %age Used
       FLASH_APP:      ...            1 MB       ...
        FLASH_FS:          0 B      896 KB       0.00%
             RAM:      ...          192 KB       ...
             CCM:      ...           64 KB       ...
```

`FLASH_FS` must stay at 0 B: anything there would collide with the littlefs file system in flash
bank 2. The linker refuses an image that breaks this, so a failing link is the intended outcome,
not a broken toolchain.

The tutor step *The RAM budget and the 48 KB floor* (module M4) uses the same script as its
check.
