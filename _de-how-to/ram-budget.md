---
title: RAM-Budget prüfen
order: 4
description: Das RAM-Budget-Skript gegen die gelinkte ELF ausführen und seine Reserve lesen
---

CaDS Zero betreibt FreeRTOS ohne Heap für Task-Stacks: sie liegen im 64 KB großen CCM, und lwIP
plus GUI brauchen mindestens 48 KB Heap im Haupt-SRAM. Das Projekt hält ein Skript bereit, das
die gelinkte ELF liest und diese Zahlen gegen ein Budget prüft, sodass eine Änderung, die zu
viel RAM frisst, hier scheitert statt auf dem Board.

## Ausführen

**F1 → Tasks: Run Task → CaDS: RAM budget**, oder im Terminal:

```bash
python3 scripts/check_ram_budget.py build/itsboard/cads-zero.elf
```

Die ELF muss existieren, also zuerst bauen (**CaDS: Build**). Auf dem geseedeten Commit druckt
das Skript:

```
PASS: 928 B of margin, budget is 256 B
```

Die Reserve (margin) ist, was oberhalb der geforderten Rücklage übrig bleibt; das Budget ist die
kleinste Reserve, die das Projekt akzeptiert. Ein `FAIL` nennt die Sektion, die gewachsen ist.

## Den Linker-Bericht lesen

Jeder Firmware-Link druckt außerdem am Ende des Build-Tasks den Speicherbericht:

```
Memory region         Used Size  Region Size  %age Used
       FLASH_APP:      ...            1 MB       ...
        FLASH_FS:          0 B      896 KB       0.00%
             RAM:      ...          192 KB       ...
             CCM:      ...           64 KB       ...
```

`FLASH_FS` muss bei 0 B bleiben: alles dort würde mit dem littlefs-Dateisystem in Flash-Bank 2
kollidieren. Der Linker verweigert ein Image, das diese Regel bricht, ein fehlschlagender Link
ist also das beabsichtigte Ergebnis, keine kaputte Toolchain.

Der RAM-Budget-Step in Modul M4 nutzt dasselbe Skript als Check.
