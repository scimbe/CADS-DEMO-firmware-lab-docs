---
layout: default
title: Befehle und Aufgaben ausführen (Rust)
lang: de
permalink: /de/rust/working-the-window/
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

Das Panel ist wichtiger, als es aussieht. **Ein Befehl, den Sie tippen, gibt im Terminal aus.**
Unter Probleme steht, was der Compiler über Ihre geöffneten Dateien meldet, unter Ausgabe stehen
Meldungen des Editors selbst. Keiner der beiden zeigt jemals das Ergebnis eines Befehls, den Sie
ausgeführt haben — erstaunlich viel Verwirrung entsteht dadurch, im falschen Reiter zu suchen.

## Drei Wege zum selben Ergebnis

**1. Die Schaltfläche auf der Aufgabenkarte.** Jede Aufgabe im Tutor hat eine Schaltfläche, die
genau den verlangten Befehl ausführt. Darunter steht die Zeile *entspricht: ein Terminal öffnen und
… eingeben*, damit immer sichtbar ist, was tatsächlich geschah.

**2. Das Terminal.** Öffnen über das Menü **Terminal → Neues Terminal** oder mit
<kbd>Strg</kbd>+<kbd>`</kbd> (die Taste über Tab). Dann den Befehl eingeben und
<kbd>Eingabetaste</kbd> drücken.

**3. Die Befehlspalette.** <kbd>F1</kbd> drücken, dann den Namen des Befehls tippen.

## Die Eigenheit der Palette, über die alle stolpern

Die Palette merkt sich die zuletzt benutzte Eingabeart und öffnet standardmäßig im *Datei*-Modus:
Getipptes gilt dann als Dateiname. `Terminal: Neues Terminal` liefert dort **Keine Übereinstimmung**,
was aussieht, als gäbe es den Befehl nicht.

**Tippen Sie zuerst ein `>`.** Das vorangestellte Zeichen schaltet die Palette in den Befehlsmodus,
und derselbe Text findet den Befehl sofort. Wenn ein Schritt sagt, ein Befehl sei über die Palette
auszuführen, gehört das `>` zur Anweisung.

## Zwei Dinge, die man früh wissen sollte

**Ein neues Terminal startet nicht im Projektordner.** Das Laborfenster hält zwei Arbeitsbereiche
nebeneinander, ein frisches Terminal startet deshalb eine Ebene darüber, in `~/workspace`. Der erste
cargo-Befehl antwortet dann `could not find Cargo.toml`, was nach einer kaputten Übung aussieht, aber
nur der falsche Ordner ist. Jeder Schritt des Kurses beginnt deshalb damit, Sie an die richtige
Stelle zu setzen:

```
cd ~/workspace/rust-foundations
```

`pwd` zeigt, wo Sie gerade stehen, falls Sie sichergehen wollen.

**Ein Befehl ist fertig, wenn die Eingabeaufforderung zurückkommt.** Bis dahin läuft er noch, auch
wenn nichts Neues erscheint. Das Terminal über das Papierkorbsymbol zu schließen versteckt es nicht
nur — es beendet, was darin lief.

## Verwandtes

- [Die erste Sitzung]({{ '/de/rust/first-session/' | relative_url }})
- [Wenn eine Prüfung nicht bestehen will]({{ '/de/rust/when-a-check-fails/' | relative_url }})
- [Rust-Tutor-Doku]({{ '/de/rust/' | relative_url }})
