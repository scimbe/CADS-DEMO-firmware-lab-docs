---
title: Grenzen
order: 5
description: Was die browser-gebrückte Architektur weniger gut kann als ein Desktop-Aufbau, und was noch verifiziert wird
---

## Latenz auf jeder Probe-Operation

Jedes GDB-Paket, das das Target braucht (Speicher lesen, Register lesen, Schritt), wird zu
mindestens einem Kommando-Round-Trip vom Container zum Web Worker in deinem Browser und
zurück, über den WebSocket und in Produktion über den TLS-Tunnel. Ein lokaler Container misst
16–18 ms für einen trivialen Ping; über das Internet ist es deine Round-Trip-Zeit plus die
USB-Transaktion. Die Bridge bündelt Operationen und cacht Speicher, solange der Core
angehalten ist, sodass das Öffnen eines Call-Stacks ein Schub ist statt Dutzende Fahrten, aber
das Einzelschritten durch eine Schleife ist spürbar langsamer als mit einer Probe am Desktop.
Genaue Zahlen über den Tunnel werden mit echter Hardware aufgezeichnet und hier ergänzt.

## Ein Board, ein Browser-Tab

Die Probe lebt im Web Worker des Tabs, den du geöffnet hast. Den Tab zu schließen trennt das
Board; ein zweiter Tab sieht die Freigabe des ersten nicht. Nur ein GDB-Client darf gleichzeitig
angehängt sein, und die Board-Checks des Tutors, das Konsolen-Terminal und der Debugger teilen
sich dieselbe serialisierte Probe.

## Golden-Image-Tests weichen im Container ab

Die Host-Testsuite besteht im Container bis auf zwei Golden-Image-Vergleiche, die an
antialiasierten Kantenpixeln um +1 abweichen, weil Debians SDL2 die RGB565-Umwandlung anders
rundet als das SDL, mit dem die Goldens erzeugt wurden. Das Labor nimmt sie aus dem
Standard-Test-Task heraus und führt sie in einem gekennzeichneten, informativen Task aus; die
Goldens im Container neu zu erzeugen ist Sache des cads-zero-Maintainers.

## Speicher auf geteilten Hosts

Ein cads-zero-Build erreicht Spitzen von etwa 1 GB RAM; Extension-Host, clangd und CMake Tools
kommen mit einigen hundert MB dazu. Auf einem schwachen Host begrenzt der Betreiber
`CMAKE_BUILD_PARALLEL_LEVEL`; im Multi-User-Stack bekommt jeder Container standardmäßig 2 GB
und 2 CPUs.

## Das Sprachmodell ist optional

„Frag den Tutor“, die Fragenbewertung und proaktive Check-ins brauchen einen OpenAI-kompatiblen
Endpunkt, den der Betreiber konfiguriert. Ohne ihn führt der Tutor trotzdem jeden Check aus
und zeigt jeden Hinweis und jede Quelle, aber Fragen fallen auf manuelle Bestätigung zurück.

## Browser-Unterstützung

WebUSB und WebSerial gibt es nur in Chromium-basierten Browsern. Firefox und Safari können
Editor, Build-Tasks und Tutor nutzen, aber nicht das Board.

## Was noch in Verifikation ist

Zum Zeitpunkt des Schreibens hat die Board-Bridge (`cads-probe`, `cads-board-bridge`) ihren
Machbarkeitstest im lokalen Container bestanden (Web-Extension im Worker, USB und Seriell
erreichbar, Round-Trip Container ↔ Worker) und ihre Treiber-Portierung ist unit-getestet,
während die Ende-zu-Ende-Pfade für Flash, Debug und Konsole gegen das echte ITSboard verifiziert
werden. Seiten, die diese Pfade beschreiben, tragen einen Hinweis und bekommen ihre Screenshots,
sobald der Hardware-Durchlauf aufgezeichnet ist.
