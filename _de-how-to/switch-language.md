---
title: Sprache wechseln
order: 6
description: Die Kurssprache zwischen Deutsch und Englisch umschalten, im Panel, per Befehl oder per Einstellung
---

Alle Kursinhalte gibt es auf Englisch und Deutsch. Der Tutor wählt die Sprache in dieser
Reihenfolge:

1. Die Einstellung `cadsTutor.language` (`auto`, `de`, `en`). Standard `auto`.
2. Bei `auto`: die Anzeigesprache von VS Code in deiner Browser-Sitzung.
3. Was du zuletzt im Panel gewählt hast; diese Wahl wird in deiner Session gespeichert und
   überlebt ein Neuladen.

## Im Panel

Der Kopf des Step-Panels hat einen Button mit der Beschriftung **Deutsch** (auf der englischen
Oberfläche) oder **English** (auf der deutschen). Ein Klick schaltet Panel, Kursbaum,
Fortschrittsansicht und Statusleiste gemeinsam um.

## Per Befehl

**F1 → CaDS Tutor: Sprache wählen / Set language**, dann `Deutsch` oder `English` wählen. Die
Ansicht Kurse / Courses hat denselben Befehl hinter ihrem Globus-Symbol.

## Per Einstellung

Öffne die *Settings* (F1 → *Preferences: Open User Settings*), suche nach `cadsTutor.language`
und setze es auf `de` oder `en`. Das überschreibt die Panel-Wahl für jede neue Session.

## Was sich nicht ändert

- Die VS-Code-Oberfläche selbst bleibt in der Anzeigesprache deines Browser-Profils. Das Labor
  installiert keine Sprachpakete.
- Die Befehlstitel der Labor-Extensions sind absichtlich zweisprachig, zum Beispiel
  *Tutor öffnen / Open Tutor*, du findest sie in der Befehlspalette also in beiden Sprachen.
- Meldungen der Board-Bridge (Statusleiste, Flash-Benachrichtigungen) sind in der aktuellen
  Version deutsch.
