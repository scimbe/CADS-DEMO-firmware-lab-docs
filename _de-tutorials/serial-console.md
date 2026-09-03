---
title: Serielle Konsole und Explorer-Befehle
order: 4
description: Das Terminal "CaDS Board Console" öffnen, den Selbsttest lesen und mit dem Bring-up-Explorer über Ein-Buchstaben-Befehle sprechen
---

Die ST-Link stellt die USART3 der Firmware als virtuellen COM-Port bereit. Im Labor öffnet dein
Browser diesen Port (WebSerial), und im Container erscheint er als Terminal mit dem Namen
**CaDS Board Console**. Darüber liest du den Boot-Selbsttest und nutzt die firmwareeigene
Diagnosekonsole.

<div class="callout warn">
Der Konsolen-Pfad (WebSerial im Browser, serielles TCP und das Terminal im Container) gehört zur
Board-Bridge, die zum Zeitpunkt dieser Seite gegen echte Hardware verifiziert wird. Ein
Screenshot des Konsolen-Terminals folgt, sobald er aufgezeichnet ist.
</div>

## 1. Die Konsole öffnen

Klicke den Statusleisten-Eintrag **Board: verbunden …** und wähle **Konsole öffnen**, oder führe
**F1 → CaDS Board: Konsole öffnen** aus. Ein Terminal öffnet sich mit einem cyanfarbenen Banner:

```
[CaDS Board Console – serielle Konsole des Boards, 115200 Baud. Ctrl-] beendet nicht, Terminal schließen genügt.]
```

Wurde der serielle Port noch nicht freigegeben, druckt das Terminal stattdessen einen gelben
Hinweis, und du verbindest zuerst das Board. Die Statusleiste zeigt dann `· Konsole`, solange der
Port offen ist.

## 2. Den Boot-Selbsttest lesen

Drücke **Reset** im Board-Menü. Die Firmware druckt ihren Selbsttest im TAP-Format:

```
1..9
ok 1 - SysTick advances at 1 kHz
ok 2 - DWT microsecond clock agrees
...
# flush_pixels: 153600
# flush_us: 448233
# flush_kpixel_per_s: 342
ok 7 - dirty rectangle limits the transfer
# RESULT: PASS
```

`1..9` ist der Plan, `ok`/`not ok` sind Zusicherungen, `#`-Zeilen sind Diagnosen. Der
Tutor-Check `serialExpect` wartet auf genau die Zeile `RESULT: PASS`. Die Zahl
`flush_kpixel_per_s: 342` ist gemessen, nicht gerechnet: ein Vollbild-Neuaufbau mit 153 600 Pixeln
dauert etwa 448 ms, weil die Schieberegisterkette des Displays 16 SPI-Takte pro Pixel kostet.

## 3. Zum Prompt kommen

Ein frisch geflashtes Board bootet in den Touchscreen-App-Baum (`boot.autostart = 1`). Diese
Sitzung **ignoriert einfache getippte Bytes mit Absicht**, ein Konsolenbefehl tut also nichts,
druckt nichts und sieht aus wie ein hängendes Board. Nur das reservierte Quit-Byte beendet sie.
Führe im integrierten Terminal (nicht in der Konsole) aus:

```bash
scripts/board_key.py quit
```

Das Skript muss wissen, welchen Port es nutzen soll. Im Container veröffentlicht die Bridge die
Konsole als rohen TCP-Port `127.0.0.1:3334` und, wo `socat` vorhanden ist, als PTY-Link
`/home/coder/board-console`; richte die cads-zero-Skripte auf diesen Link:

```bash
CADS_CONSOLE_PORT=/home/coder/board-console scripts/board_key.py quit
```

## 4. Explorer-Befehle

Jetzt hört der Prompt zu. Jeder Befehl ist ein Zeichen, optional gefolgt von ein oder zwei
Argumenten. Tippe in das Konsolen-Terminal:

| Befehl | Was er tut |
|---|---|
| `?` | Hilfetext erneut ausgeben. Die Hilfezeichenkette der Firmware ist die maßgebliche Wahrheit. |
| `i` | Das Eingaberegister (IDR) jedes Ports einmal ausgeben. |
| `w 20` | Alle Ports 20 s lang auf Änderungen beobachten. Drücke einen Taster am Adapter und sieh, welcher Pin sich bewegt. |
| `k` | Task-Stacks, Task-Anzahl, Eingabezähler. |
| `t` | Eine Touch-Abtastung vom XPT2046. |
| `p 3` | Ein Testmuster zeichnen (0 schwarz, 1 blau, 2 grün, 3 Quadranten, 4 Streifen, 5 Splash, 6 Fonts). |
| `l 100` | Die On-Board-LEDs setzen. |
| `e`, `a`, `m` | Ethernet-PHY-Identität und Link-Zustand, Auto-Negotiation, MAC-Zähler, alles unterhalb von lwIP. |
| `V` | Den Vollbild-Flush-Durchsatz unter Scheduler- und Netzwerklast neu messen. |
| `d` | Den App-Baum live ausführen. Endet nur mit `board_key.py quit`. |

Ein Befehl, `z FAULT`, ist absichtlich destruktiv: er löst einen UsageFault aus und hält für
immer an, um zu beweisen, dass der Fault-Handler funktioniert. Er verlangt das wörtliche Argument
`FAULT`. Der vollständige Katalog liegt im Workspace unter `docs/reference/explorer-console.md`.

Aus dem integrierten Terminal kannst du einen einzelnen Befehl auch nicht-interaktiv ausführen
und seine Ausgabe einfangen:

```bash
CADS_CONSOLE_PORT=/home/coder/board-console scripts/board_cmd.py k
```

## 5. Was der Tutor beobachtet

Der Tutor liest die Konsole mit. Drei Muster lösen im Step-Panel eine sokratische Notiz statt
einer Lösung aus: `HardFault`, `configASSERT` und `RESULT: FAIL`. Jedes Muster ist 15 s lang
entprellt, ein durchlaufender Fault-Dump erzeugt also eine Frage, nicht dreißig.

## Wo du jetzt stehst

Du kannst lesen, was die Firmware sagt, und ihr Fragen stellen. Das letzte Tutorial dieser Reihe
handelt vom Tutor selbst:
[Mit dem Tutor lernen]({{ '/de/tutorials/learning-with-the-tutor/' | relative_url }}).
