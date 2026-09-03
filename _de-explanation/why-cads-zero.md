---
title: Warum cads-zero der Workspace ist
order: 2
description: Warum das Labor ein echtes Firmware-Repository statt eines Spielzeugbeispiels öffnet, und wie Seed, Toolchain und deine Kopie zusammenpassen
---

## Ein echtes Repository, kein Beispiel

Frühere Iterationen dieses Labors lieferten eine kleine Beispiel-Firmware mit. Das aktuelle
Labor öffnet direkt [CaDS Zero](https://github.com/scimbe/cads-zero): eine Clean-Room-Firmware
für das ITSboard mit Kernel, GUI-Framework, FreeRTOS, littlefs, lwIP, einer
Bring-up-Explorer-Konsole, Unit- und Golden-Image-Tests und einer dokumentierten Geschichte
jedes Hardwareproblems, auf das das Projekt gestoßen ist. Die Kurse sind in diesem Repository
verankert; jedes Register, jeder Pfad, jedes Symbol und jede gemessene Zahl, die ein Step nennt,
lässt sich in dem Baum prüfen, den du offen hast. Ein Spielzeugbeispiel könnte keinen Kurs
tragen, der von „an welchem Pin hängt die LED“ bis „verteidige einen Dirty-Rectangle-Kompromiss“
aufsteigt.

## Der Seed und deine Kopie (ADR-003)

Das Image enthält einen flachen Clone von cads-zero mit seinen Submodulen an einem festgelegten
Commit unter `/opt/cads-seed/cads-zero`, **einmal während des Image-Builds gebaut**:
`cmake --preset itsboard` erzeugt `cads-zero.bin` und `compile_commands.json`, und das
Host-Preset führt `ctest` als zweiten Smoke-Test aus. Ein Build, der fehlschlägt, lässt das
Image fehlschlagen.

Beim ersten Start eines Containers kopiert der Entrypoint den Seed nach
`/home/coder/workspace/cads-zero`, falls dort kein `.git` existiert. Diese Kopie liegt in deinem
Workspace-Volume; spätere Starts lassen sie in Ruhe, sodass deine Änderungen, deine Builds und
deine Tutor-Session Neustarts und Image-Updates überleben. Der Seed ist auf einem lokalen
Branch `cads-lab` ausgecheckt statt als Detached HEAD, weil ein Detached HEAD Studierende
verwirrt und nichts vom Namen abhängt.

Nur die Container-Konfiguration wird bei jedem Start erneuert: `.vscode/{settings,tasks,launch,
extensions}.json` und `.clangd`. Sie sind als `skip-worktree` markiert, damit `git status` sauber
bleibt, und `extensions.json` ersetzt die Empfehlung von cads-zero für `ms-vscode.cpptools`
(nicht auf Open VSX) durch `clangd`, die IntelliSense-Engine des Images.

## Die Toolchain

cads-zero wird mit ARM GNU 13.3.1 über vcpkg entwickelt. Das Image installiert den offiziellen
Tarball **13.3.rel1** für seine Architektur statt des Debian-Pakets 12.2, sodass Studierende mit
demselben Compiler bauen wie der Maintainer und der Speicherbericht des Linkers zu den Zahlen
in der Doku passt. `CADS_ARM_TOOLCHAIN_BIN` zeigt darauf; so findet `scripts/cads_env.sh` die
Toolchain ohne vcpkg.

Eine Abweichung: Das `arm-none-eabi-gdb` der Toolchain braucht ncurses 5, das Debian 13 nicht
mehr ausliefert. Ein Wrapper gleichen Namens führt stattdessen `gdb-multiarch` 16.3 aus;
cortex-debug und die Skripte merken davon nichts.

## Warum IntelliSense ohne Konfiguration funktioniert

CMake Tools konfiguriert beim Öffnen nicht (es würde jeden Studierenden nach einem Preset
fragen, bevor er irgendetwas getan hat). Stattdessen liest clangd die geseedete
`build/itsboard/compile_commands.json` und fragt den Toolchain-Treiber nach seinen
Include-Pfaden, sodass cross-kompilierte Header ab dem ersten Klick aufgelöst werden. Die
Labor-Tasks führen CMake selbst aus. Wer CMake Tools bevorzugt, wählt das Preset `ITSboard` in
der Statusleiste und bekommt dasselbe Ergebnis.
