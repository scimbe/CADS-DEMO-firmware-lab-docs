---
layout: default
title: Befehle und Aufgaben ausführen (JavaScript)
lang: de
permalink: /de/javascript/working-the-window/
---

# Befehle und Aufgaben ausführen

Jeder Schritt des Kurses verlangt, etwas auszuführen. Dafür gibt es drei gleichwertige Wege —
suchen Sie sich einen aus und bleiben Sie dabei. Diese Seite gibt es, weil einem Tutorial zu folgen
wirklich schwer ist, wenn niemand sagt, welche Taste zu drücken ist.

## Das Fenster in fünf Teilen

| Teil | Wo | Wofür |
|---|---|---|
| Aktivitätsleiste | ganz links, eine Spalte mit Symbolen | schaltet die Seitenleiste um; das Doktorhut-Symbol öffnet den Tutor |
| Seitenleiste | links | Explorer (Ihre Dateien) oder der Kursbaum des Tutors |
| Editor | Mitte | Ihr Code und der Schritt, an dem Sie arbeiten, als Reiter |
| Panel | unten, geschlossen bis man es braucht | die Reiter **Terminal**, **Probleme** und **Ausgabe** |
| Statusleiste | ganz unten | Sprachmodus und der laufende Sprachdienst |

**Ein Befehl, den Sie tippen, gibt im Terminal aus.** Unter Probleme steht, was der Editor über Ihre
geöffneten Dateien meldet, unter Ausgabe stehen Meldungen des Editors selbst. Keiner der beiden
zeigt jemals das Ergebnis eines Befehls — erstaunlich viel Verwirrung entsteht dadurch, im falschen
Reiter zu suchen.

## Drei Wege zum selben Ergebnis

**1. Die Schaltfläche auf der Aufgabenkarte.** Jede Aufgabe im Tutor hat eine Schaltfläche, die
genau den verlangten Befehl ausführt. Darunter steht die Zeile *entspricht: ein Terminal öffnen und
… eingeben*, damit immer sichtbar ist, was tatsächlich geschah.

**2. Das Terminal.** Öffnen über **Terminal → Neues Terminal** oder mit
<kbd>Strg</kbd>+<kbd>`</kbd> (die Taste über Tab). Dann den Befehl eingeben und
<kbd>Eingabetaste</kbd> drücken.

**3. Die Befehlspalette.** <kbd>F1</kbd> drücken, dann **vor dem Befehlsnamen ein `>` tippen**.

## Die Eigenheit der Palette, über die alle stolpern

Die Palette merkt sich die zuletzt benutzte Eingabeart und öffnet standardmäßig im *Datei*-Modus:
Getipptes gilt dann als Dateiname. `Terminal: Neues Terminal` liefert dort **Keine Übereinstimmung**,
was aussieht, als gäbe es den Befehl nicht. Das vorangestellte `>` schaltet in den Befehlsmodus, und
derselbe Text findet den Befehl sofort.

## Zwei Dinge, die man früh wissen sollte

**Ein neues Terminal startet nicht im Übungsordner.** Das Laborfenster hält zwei Arbeitsbereiche
nebeneinander, ein frisches Terminal startet deshalb eine Ebene darüber. Jeder Schritt des Kurses
beginnt damit, Sie an die richtige Stelle zu setzen:

```
cd ~/workspace/javascript-foundations
```

`pwd` zeigt, wo Sie stehen, falls Sie sichergehen wollen.

**Ein Befehl ist fertig, wenn die Eingabeaufforderung zurückkommt.** Bis dahin läuft er noch, auch
wenn nichts Neues erscheint. Das Terminal über das Papierkorbsymbol zu schließen versteckt es nicht
nur — es beendet, was darin lief.

## Wie ein Testlauf aussieht

Der Kurs prüft Ihre Arbeit mit dem Testläufer von Node:

```
node --test test/m0-02-first-run.test.js
```

Ein fehlschlagender Test ist der normale Zustand einer Übung, bevor Sie sie lösen. Die Ausgabe nennt
die fehlgeschlagene Zusicherung und was sie erwartet hat — genau diese Angabe sollen Sie lesen, sie
ist kein Zeichen dafür, dass etwas kaputt ist.

## Verwandtes

- [Die erste Sitzung]({{ '/de/javascript/first-session/' | relative_url }})
- [Wenn eine Prüfung nicht bestehen will]({{ '/de/javascript/when-a-check-fails/' | relative_url }})
- [JavaScript-Tutor-Doku]({{ '/de/javascript/' | relative_url }})
