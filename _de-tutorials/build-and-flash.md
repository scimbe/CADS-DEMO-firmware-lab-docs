---
title: Bauen und auf das Board flashen
order: 2
description: "Den Task \"CaDS: Build + Flash\" ausführen, das Board im Browser verbinden und deine Firmware auf den Chip bringen"
---

In diesem Tutorial baust du die Firmware im Container und flashst sie auf das Board, das an
**deinem** Rechner steckt. Der Container hat überhaupt keinen USB-Zugriff. Die ST-Link wird aus
deinem Browser gesteuert und in den Container gebrückt; deshalb bittet dich der Browser einmal,
das Gerät auszuwählen.

<div class="callout">
Der Flash-Pfad wurde am 2026-09-03 Ende-zu-Ende mit echtem Chrome, der ST-Link V2-1 und dem
ITSboard verifiziert: ein Image von 327 088 Bytes wird in etwa 13 s geschrieben und verifiziert,
und das Board bootet in seinen Selbsttest. Screenshots des Board-Menüs und des
Flash-Fortschritts mit Hardware folgen; die UI-Texte unten stammen aus der Bridge.
</div>

## Was du brauchst

- Das ITSboard (NUCLEO-F429ZI mit ITS-Adapter und Display-Shield), per USB-Kabel am
  ST-Link-Port mit deinem Rechner verbunden.
- Chrome oder Edge. Siehe [Board anschließen]({{ '/de/how-to/connect-the-board/' | relative_url }})
  für die Hinweise je Betriebssystem (udev-Regel unter Linux, das Laufwerk `NOD_F429ZI` unter macOS).

## 1. Nur bauen

Öffne den Task-Picker mit **F1 → Tasks: Run Task** und tippe `CaDS:`.

<figure>
<img src="{{ '/assets/04-task-picker.png' | relative_url }}" alt="Task-Picker gefiltert auf CaDS: mit Build, Flash, Build + Flash, Host tests, Golden images, RAM budget">
<figcaption>Die Labor-Tasks. „CaDS: Build“ ist zugleich der Standard-Build-Task (Ctrl+Shift+B).</figcaption>
</figure>

Wähle **CaDS: Build**. Der Task führt `cmake --preset itsboard && cmake --build build/itsboard`
mit der ARM-GNU-Toolchain 13.3.rel1 aus und endet mit dem Speicherbericht des Linkers.

<figure>
<img src="{{ '/assets/05-build-task.png' | relative_url }}" alt="Task-Terminal nach CaDS: Build mit der Ninja-Ausgabe und der Tabelle zur Speichernutzung">
<figcaption>Ein fertiger Build. FLASH_FS bleibt bei 0 B; der Linker verweigert Images, die mit dem Dateisystem kollidieren würden.</figcaption>
</figure>

Die Artefakte sind `build/itsboard/cads-zero.elf`, `.bin` und `.hex`. Das Board wurde noch nicht
berührt.

## 2. Das Board verbinden

Klicke auf den Statusleisten-Eintrag **Board: getrennt** (oder führe **F1 → CaDS Board:
Verbinden** aus). Die Bridge bittet den Browser, seinen Geräte-Dialog zu zeigen, gefiltert auf
Geräte von STMicroelectronics (Vendor-ID `0x0483`). Zwei Dialoge erscheinen nacheinander:

1. **USB-Gerät**: wähle *STM32 STLink*. Das ist der SWD-Pfad für Flashen und Debuggen.
2. **Serieller Port**: wähle den virtuellen COM-Port der ST-Link. Das ist die Konsole mit
   115200 Baud.

Beide Freigaben merkt sich der Browser für diesen Origin. Nach einem Aus- und Wiedereinstecken
findet die Bridge die Geräte ohne neuen Dialog wieder.

Steht die Verbindung, zeigt die Statusleiste `Board: verbunden · läuft`, und der Tooltip nennt
die ST-Link-Version, das erkannte Gerät (`STM32F42x_F43x`) und die Flash-Größe. Ein Klick auf den
Eintrag öffnet ein kleines Menü: *Flash*, *Reset*, *Anhalten* / *Weiterlaufen lassen*,
*Konsole öffnen*, *Log anzeigen*, *Trennen*.

Erscheint der Geräte-Dialog gar nicht, lies
[Troubleshooting → Der Geräte-Dialog erscheint nicht]({{ '/de/how-to/troubleshooting/' | relative_url }}#der-geräte-dialog-erscheint-nicht).

## 3. Build + Flash

Führe **F1 → Tasks: Run Task → CaDS: Build + Flash** aus. Er startet den Build-Task und danach:

```bash
st-flash write build/itsboard/cads-zero.bin 0x08000000 && st-flash reset
```

`st-flash` im Container ist nicht das stlink-Werkzeug. Es ist ein kleiner Shim, der mit der
HTTP-API der Bridge auf `127.0.0.1:3335` spricht; die reicht das Image an die ST-Link in deinem
Browser weiter. Eine Benachrichtigung *CaDS: Flash cads-zero.bin* zeigt die Phasen *erase*,
*program* und *verify*; danach zeigt die Statusleiste einige Sekunden lang
`Flash ok: <bytes> Bytes in <ms> ms`, und `st-flash reset` startet das Board neu.

Vor dem Schreiben **hält die Probe den Kern an**, statt ihn zurückzusetzen. Das ist auf diesem
Board wichtig: die Firmware aktiviert den unabhängigen Watchdog, und ein Reset mitten in der
Flash-Sequenz ließe den Watchdog auslösen. Die Bridge verweigert außerdem jeden Schreibzugriff
außerhalb von `0x08000000–0x080FFFFF` und führt nie ein Mass-Erase aus (siehe
[Sicherheitsregeln]({{ '/de/explanation/safety-rules/' | relative_url }})).

Das Board bootet, führt seinen Selbsttest aus und druckt TAP-Zeilen auf die Konsole. Der
Tutor-Step *Flashen und das Hardware-Gate bestehen* prüft genau das: einen Flash seit Beginn des
Steps und ein `RESULT: PASS` auf der seriellen Leitung.

## 4. Wenn der Shim „Board-Bridge nicht aktiv“ meldet

Führst du einen Flash-Task aus, bevor das Board verbunden ist, druckt der Shim

```
Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)
```

und endet mit Status 1. Nichts ist kaputt: der HTTP-Port der Bridge wird nur bedient, während
der Extension-Host läuft und das Board verbunden ist. Verbinde das Board über den
Statusleisten-Eintrag und starte den Task erneut. Den Zustand kannst du jederzeit mit
`st-info --probe` im Terminal prüfen.

<figure>
<img src="{{ '/assets/06-terminal-st-info.png' | relative_url }}" alt="Integriertes Terminal: st-info --probe druckt den deutschen Hinweis, dass die Board-Bridge nicht aktiv ist; arm-none-eabi-gcc meldet Version 13.3.1">
<figcaption>Ohne verbundenes Board sagen es die Shims. Die Toolchain ist trotzdem da.</figcaption>
</figure>

## Wo du jetzt stehst

Dein Build läuft auf dem Chip. Das nächste Tutorial hält ihn an einem Breakpoint an:
[Debuggen mit F5]({{ '/de/tutorials/debug-with-f5/' | relative_url }}).
