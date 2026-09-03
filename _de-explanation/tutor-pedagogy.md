---
title: Wie Grounding, Bloom-Stufen und sokratische Hinweise funktionieren
order: 3
description: Die drei Ideen hinter dem Tutor, und warum er Fragen stellt und Quellen nennt, statt zu chatten
---

## Grounding: nur aus indiziertem Material antworten

Der Tutor beantwortet eine Frage nie allein aus dem Allgemeinwissen des Sprachmodells. Bevor er
das Modell aufruft, führt er eine BM25-Suche über einen Index aus Chunks aus: das Content-Pack
`firmware` (die cads-zero-Dokumentation, 155 Chunks) plus die eigenen `sources/` des Kurses und
die Projektdateien, die der Step nennt (das Grundlagen-Pack indiziert rund 70 Projektdateien,
insgesamt 2 884 Chunks). Passagen über der Schwelle des Kurses gehen als Kontext an das Modell
und werden mit der Antwort unter **Quellen** aufgelistet. Erreicht nichts die Schwelle,
verweigert der Tutor mit *Das liegt außerhalb des indizierten Referenzmaterials dieses Kurses –
formuliere um oder frag zum aktuellen Step.*, statt zu raten.

Die Schwelle ist bewusst streng. Eine vage Frage wie „Wie flashe ich?“ kann darunter liegen,
während „Was verweigert `st-flash write` und warum?“ gut punktet. Kursautoren senken
`grounding.threshold` oder ergänzen Quellen, wenn ein Kurs gesprächiger ist als das Firmware-Pack.

Dasselbe Grounding speist die Bewertung von `question`-Aufgaben: Das Modell sieht die Rubrik,
die Antwort des Studierenden und die gefundenen Passagen und gibt eine Urteilszeile zurück.
Ohne Sprachmodell wird die Antwort gespeichert und der Studierende bestätigt sie manuell.

## Bloom-Stufen: benennen, was ein Step von dir verlangt

Jeder Step trägt eine Stufe der Bloom-Taxonomie: *remember*, *understand*, *apply*, *analyze*,
*evaluate*, *create*. Der Grundlagenkurs steigt gezielt auf: Erinnern und Verstehen in M0–M1,
Anwenden und Analysieren in der Mitte, Bewerten und Erschaffen oben. Die Stufe ist keine
Dekoration:

- `apply`- und `create`-Steps ändern echte Firmware und prüfen genau diese Änderung (ein
  Dateimuster, ein ELF-Symbol, einen Flash, eine serielle Zeile).
- `evaluate`-Steps verlangen ein begründetes Urteil, das gegen eine Rubrik bewertet wird.
- „Frag den Tutor“ schickt die Stufe des Steps mit der Frage, sodass eine Antwort zu einem
  *remember*-Step eine Definition ist und eine Antwort zu einem *analyze*-Step ein Vergleich.

Die Ansicht *Fortschritt / Progress* verdichtet Lernereignisse je Objective zu einer
Beherrschungsschätzung. Objectives sind IDs aus dem Plattform-Curriculum oder aus der
`curriculum.json` des Kurses.

## Sokratische Hinweise: zuerst eine Frage, später Eskalation

Schlägt ein Check fehl, zeigt der Tutor nicht die Lösung. Er zeigt die Frage, die der
Kursautor für diesen Fehlschlag geschrieben hat, zum Beispiel *Der Build sucht zuerst einen
Compiler. Wo sucht er?* Erst dann deckt *Hinweis anzeigen* **Hinweis 1 von 3** auf. Jeder
weitere Fehlschlag derselben Aufgabe schaltet die nächste Stufe frei; die dritte Stufe ist
konkret. Danach sagt der Tutor das und verweist dich auf die Fragebox. Ohne Autoren-Eintrag
gelten drei generische Hinweise (Meldung lesen, Muster vergleichen, referenzierte Datei öffnen).

Derselbe Mechanismus reagiert auf das, was das Board tut. Ein `HardFault` oder `configASSERT`
auf der Konsole, ein fehlgeschlagener Flash oder ein Debugger-Halt stellt eine Kontextfrage ins
Panel: *Welches Register verrät dir die fehlerhafte Adresse, und wie liest du es im Debugger?*
Notizen sind entprellt (15 s je Muster, höchstens eine Check-in-Benachrichtigung pro Minute)
und nie modal.

## Proaktiv, aber leise

Das Speichern einer Datei führt nach zwei Sekunden die lokalen Checks des Steps erneut aus,
sodass eine `fileMatches`-Aufgabe ohne Klick grün wird. Gehört die Datei zum Step und ist ein
Sprachmodell konfiguriert, fordert der Tutor zusätzlich ein kurzes Check-in zur Änderung an
und zeigt es als Benachrichtigung mit *Zeigen* / *Später*. Alles, was der Tutor über dich
lernt, wird lokal gespeichert: die Session im Workspace, Lernereignisse in
`~/.cads-tutor/events.sqlite`, das Dialog-Log als JSONL. Nichts verlässt den Container außer
dem geerdeten Prompt an das konfigurierte Modell.
