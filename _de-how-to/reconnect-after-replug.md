---
title: Wiederverbinden nach Replug
order: 2
description: Was passiert, wenn du das Board absteckst, und wie du die ST-Link ohne neuen Geräte-Dialog zurückbekommst
---

## Normalfall: nichts zu tun

Der Browser merkt sich die Geräte, die du für diesen Origin freigegeben hast. Steckst du das
Board ab, springt die Statusleiste zurück auf **Board: getrennt**. Steckst du es wieder an,
erhält die Probe-Extension das `connect`-Ereignis des Browsers, öffnet ST-Link und seriellen
Port erneut, und die Bridge aktualisiert die Statusleiste. Kein Dialog.

Dasselbe passiert beim Start: etwa 1,5 s nachdem der Extension-Host läuft, bittet die Bridge die
Probe, jedes freigegebene Gerät neu zu verbinden, sodass ein Neuladen der Seite das Board
verbunden lässt.

## Wenn die Statusleiste auf „getrennt“ bleibt

1. Führe **F1 → CaDS Probe: Reconnect granted devices** aus. Das zählt die freigegebenen
   USB-Geräte und seriellen Ports ohne Dialog neu auf.
2. Hilft das nicht, führe **F1 → CaDS Board: Verbinden** aus und wähle das Gerät im
   Geräte-Dialog erneut. Eine zweite Auswahl schadet nicht.
3. Unter macOS hänge nach jedem Einstecken das Laufwerk `NOD_F429ZI` aus (siehe
   [Board anschließen]({{ '/de/how-to/connect-the-board/' | relative_url }}#macos)).

## Wenn die ST-Link antwortet, das Target aber nicht

Druckt `st-info --probe` `chipid 0x000`, ist die ST-Link in Ordnung, aber der Kern nicht
erreichbar. So sieht eine „verklemmte“ ST-Link aus; das passiert, nachdem ein SWD-Client mitten
in einer Übertragung beendet wurde, zum Beispiel eine Debug-Sitzung, die mit einem Neuladen der
Seite während eines Flash endete. Erholung, der Reihe nach:

1. **Stecke das USB-Kabel** des Boards neu ein. Das setzt den Protokollautomaten der ST-Link
   zurück; nichts Geringeres tut das.
2. Hänge `NOD_F429ZI` aus (macOS).
3. Verbinde neu (Schritte oben) und drücke **Reset** im Board-Menü.
4. Bootet das Board dann in wild leuchtende LEDs, flashe es mit **CaDS: Build + Flash** neu,
   bevor du etwas anderes vermutest.

## Debug-Sitzung und Replug

Ein Replug während einer Debug-Sitzung beendet die Sitzung; cortex-debug meldet, dass der
GDB-Server verschwunden ist. Beende die Sitzung, verbinde neu, starte mit F5 erneut. Nur ein
Client darf die Probe halten: eine verwaiste Sitzung, die sich noch für angehängt hält,
blockiert die nächste, also drücke immer Stop, bevor du neu startest.
