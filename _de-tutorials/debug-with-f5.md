---
title: Debuggen mit F5
order: 3
description: Die Konfiguration "Debug CaDS Zero (Board im Browser)" starten, an einem Breakpoint anhalten, steppen, Register und Peripherie lesen
---

Debuggen funktioniert im Labor wie in einer Desktop-IDE: F5, Breakpoints in der Randspalte, eine
Debug-Toolbar, der Call-Stack, Register und die Peripherie-Ansicht aus der SVD-Datei. Der
GDB-Server dahinter ist die Board-Bridge im Container, die die ST-Link in deinem Browser steuert.

<div class="callout">
Der Debug-Pfad wurde am 2026-09-03 mit echtem Chrome und dem ITSboard verifiziert: Halt an
<code>main</code>, Register, Step Over nach <code>cads_bringup_run</code> mit zwei Frames im
Call-Stack und lokalen Variablen, ein beim Boot getroffener Breakpoint, das Lesen des
CPUID-Registers, Continue und Stop. Ein Schritt dauert Ende-zu-Ende etwa 100 ms. Screenshots
einer laufenden Sitzung im Labor-Workspace (Debug-Toolbar, XPeripherals mit Werten) folgen.
</div>

## Was du brauchst

- Ein verbundenes Board (siehe [Bauen und flashen]({{ '/de/tutorials/build-and-flash/' | relative_url }})).
  Ist das Board beim Drücken von F5 nicht verbunden, fragt die Bridge
  *Das Board ist nicht verbunden. Jetzt verbinden?* und öffnet den Geräte-Dialog für dich.
- Keinen anderen Client an der Probe: beende eine laufende Debug-Sitzung, bevor du eine neue
  startest.

## 1. Einen Breakpoint setzen

Öffne `targets/itsboard/main.c`. Die Datei ist winzig:

```c
int main(void) {
    cads_hal_init();
    cads_bringup_run();
    for(;;) { __asm volatile("wfi"); }
}
```

Klicke in die Randspalte links neben der Zeile mit `cads_bringup_run();` (Zeile 14). Ein roter
Punkt erscheint. Diese Stelle liegt genau zwischen „Hardware initialisiert“ und „Anwendung läuft“.

## 2. F5 drücken

Öffne *Run and Debug* (das Play-Symbol mit dem Käfer in der Activity Bar). Die Konfiguration
**Debug CaDS Zero (Board im Browser)** ist vorausgewählt.

<figure>
<img src="{{ '/assets/11-run-and-debug.png' | relative_url }}" alt="Ansicht Run and Debug mit der ausgewählten Launch-Konfiguration Debug CaDS Zero (Board im Browser)">
<figcaption>Die Launch-Konfiguration kommt mit dem Workspace; du bearbeitest launch.json nicht.</figcaption>
</figure>

Drücke **F5**, während der Editor den Fokus hat. Im Browser erreicht F5 VS Code nur, wenn die
Workbench den Tastaturfokus hat; lädt stattdessen die Seite neu, klicke erst in den Editor oder
nutze den grünen Start-Button. Was dann passiert, der Reihe nach:

1. Der `preLaunchTask` **CaDS: Build + Flash** läuft, damit die ELF, die du debuggst, das Image
   auf dem Board ist.
2. cortex-debug startet `arm-none-eabi-gdb` (in diesem Image ein Wrapper für `gdb-multiarch`)
   und verbindet sich mit `127.0.0.1:3333`, dem GDB-Server der Bridge (`servertype: external`).
3. Das Launch-Kommando `monitor reset halt` setzt den Kern zurück und hält ihn an, dann läuft
   die Sitzung bis `main` (`runToEntryPoint`).
4. Die Ausführung läuft weiter bis zu deinem Breakpoint und hält dort.

Oben erscheint die Debug-Toolbar: Continue, Step Over, Step Into, Step Out, Restart, Stop. Die
Statusleiste zeigt `Board: verbunden · angehalten · GDB`.

## 3. Steppen und umsehen

- **Step Over (F10)** führt `cads_bringup_run()` als Einheit aus. Auf dieser Firmware kehrt die
  Funktion nie zurück, die Sitzung läuft also weiter, bis du pausierst.
- **Step Into (F11)** steigt in die Funktion ein.
- **Call Stack** zeigt die Frames von `main()` aufwärts. Direkt nach dem Reset ist das ein
  kurzer Stack: der erste Halt liegt wenige Millisekunden nach dem Boot, nicht dort, wo die
  Firmware vor F5 war. Das ist normal, kein Hänger.
- **Variables** zeigt die lokalen Variablen des gewählten Frames und einen Abschnitt
  **Registers** mit `r0`–`r12`, `sp`, `lr`, `pc` und `xPSR`.

Jeder Schritt und jedes Speicherlesen reist einmal Browser ↔ Container. Rechne damit, dass
Einzelschritte spürbar länger dauern als am Desktop mit lokaler Probe; siehe
[Grenzen]({{ '/de/explanation/limits/' | relative_url }}).

## 4. Peripherie aus der SVD-Datei

Die Launch-Konfiguration lädt `targets/itsboard/STM32F429.svd`. Während das Target angehalten
ist, hat die Seitenleiste *Run and Debug* einen Abschnitt **XPeripherals** (Extension
mcu-debug.peripheral-viewer), der jedes Peripheriegerät mit seiner Basisadresse listet. Klappe
`RCC → CR` auf, um `HSERDY` zu sehen, oder `GPIOD → ODR`, um zu lesen, was der letzte
Ausgangsschreibvorgang auf PD0–PD7 hinterlassen hat. Außerhalb einer Sitzung steht dort
*No active debug session*.

Aus derselben Extension-Familie sind außerdem verfügbar: *Memory* (mcu-debug.memory-view) und
die RTOS-Task-Liste (mcu-debug.rtos-views), sobald der FreeRTOS-Scheduler läuft.

## 5. Beenden

Klicke den roten **Stop**-Button (Shift+F5). GDB hängt sich ab, die Bridge lässt das Target
weiterlaufen, und die Firmware läuft auf dem Board weiter; die Statusleiste verliert die
Markierung `GDB` und zeigt `läuft`. Nur wenn du den Kern selbst über das Board-Menü angehalten
hast, bleibt er mit Warnfarbe angehalten, bis du dort *Weiterlaufen lassen* oder *Reset* wählst.

Die zweite Konfiguration, **Attach CaDS Zero (Board im Browser, no flash)**, verbindet sich ohne
Build und ohne Reset. Nutze sie, um eine laufende oder abgestürzte Firmware dort anzusehen, wo
sie ist.

## Wo du jetzt stehst

Du kannst die echte Firmware an einer Zeile anhalten, steppen und ihre Register lesen. Als
Nächstes: die serielle Konsole und die Explorer-Befehle, der schnellste Weg, ein Subsystem zu
fragen, was es tut:
[Serielle Konsole und Explorer-Befehle]({{ '/de/tutorials/serial-console/' | relative_url }}).
