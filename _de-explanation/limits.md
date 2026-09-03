---
title: Grenzen
order: 5
description: Was die browser-gebrückte Architektur weniger gut kann als ein Desktop-Aufbau, und was noch verifiziert wird
---

## Latenz auf jeder Probe-Operation

Jedes GDB-Paket, das das Target braucht (Speicher lesen, Register lesen, Schritt), wird zu
mindestens einem Kommando-Round-Trip vom Container zum Web Worker in deinem Browser und
zurück, über den WebSocket und in Produktion über den TLS-Tunnel. Gemessen am 2026-09-03 mit
einem lokalen Container und echter Hardware:

| Pfad | Gemessen |
|---|---|
| Kommando-Round-Trip Container ↔ Web Worker, ohne USB | 16–23 ms |
| eine Probe-Operation Ende-zu-Ende (HTTP-Shim → Bridge → Worker → WebUSB → ST-Link → zurück) | 94–115 ms |
| ein Debugger-Schritt | etwa 100 ms |
| Flash von 327 088 Bytes mit Verify | 13,2–13,3 s (etwa 24 KB/s über WebUSB) |

Über das Internet kommt deine Round-Trip-Zeit zum Tunnel hinzu. Die Bridge bündelt Operationen
und cacht Speicher, solange der Core angehalten ist, sodass das Öffnen eines Call-Stacks ein
Schub ist statt Dutzende Fahrten, aber das Einzelschritten durch eine Schleife ist spürbar
langsamer als mit einer Probe am Desktop.

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

## Serielle Konsole braucht einen Klick im Dialog

WebUSB-Freigaben stellt der Browser ohne Dialog wieder her; WebSerial-Freigaben lassen sich
nicht vorab hinterlegen, und die Chrome-Policy, die das erlauben würde, braucht ein verwaltetes
Profil (MDM). Flash und Debug laufen deshalb nach der ersten Freigabe ohne Dialog, die serielle
Konsole fragt einmal je Browser-Profil.

## Keine lokalen ST-Link-Tools, solange das Labor das Board hält

Solange der Browser die ST-Link geöffnet hat, meldet ein lokal installiertes `st-info --probe`
*Found 0 stlink programmers*; das ist exklusiver Zugriff, kein Fehler. Ein `st-flash` auf dem
eigenen Rechner genau in dem Moment, in dem der Browser das Gerät freigibt, kann die
Protokoll-Zustandsmaschine der ST-Link aufhängen (einmal während der Verifikation beobachtet);
nur ein physisches Aus- und Wiedereinstecken hilft dann.

## Was verifiziert ist und was nicht

Die Board-Bridge hat ihren Ende-zu-Ende-Hardware-Lauf am 2026-09-03 bestanden (Verbinden, Flash
mit Verify und Boot, F5 mit Halt, Schritt, Registern und Breakpoint, Replug, Shim-Pfad) in einem
Test-Workspace. Screenshots dieser Pfade im Labor-Workspace stehen noch aus; die Seiten sagen
es, wo einer fehlt.
