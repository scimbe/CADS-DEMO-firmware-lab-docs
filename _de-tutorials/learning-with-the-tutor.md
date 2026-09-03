---
title: Mit dem Tutor lernen
order: 5
description: Kurse, automatische Checks, "Frag den Tutor", Hinweis-Stufen, der Sprachumschalter und dein Fortschritt
---

Der Tutor ist kein Chatbot, der an einen Editor geschraubt wurde. Er ist eine Kurs-Runtime: er
weiß, in welchem Step du bist, prüft deine Arbeit gegen das echte Repository und das echte Board,
stellt Fragen, statt Lösungen auszugeben, und antwortet nur aus indiziertem Referenzmaterial.
Dieses Tutorial zeigt jeden dieser Teile einmal.

## 1. Kurse

Zwei Kurs-Packs liegen im Image:

| Kurs | Art | Umfang |
|---|---|---|
| CaDS Zero – Grundlagen | Pflicht, 41 Steps, etwa 10 h | M0 Orientierung → M1 Architektur → M2 Memory-mapped I/O → M3 Debugging → M4 FreeRTOS → M5 Display und GUI → M6 Storage und Konfiguration → M7 Netzwerk → M8 Qualität |
| Projektkurs cads-zero-projects | Wahl, 6 Projektaufgaben | eine eigene App, ein Netzwerk-Tool, eine Konfigurationsoption, ein Test mit Golden Image, eine Treibererweiterung, eine Performance-Messung |

Jeder Grundlagen-Step setzt den vorherigen voraus, der Baum schaltet also Step für Step frei. Die
Projektaufgaben sind unabhängig; sie nennen die vorausgesetzten Grundlagen-Steps im Text. Jeder
Step trägt eine Bloom-Stufe (*Erinnern* … *Erschaffen*), ein Lernziel und eine Zeitschätzung.

## 2. Checks

Aufgaben in einem Step werden geprüft, nicht abgehakt. Die Check-Typen, denen du begegnest:

- **Datei-Checks** laufen beim Speichern (`fileMatches`, `fileNotMatches`) und geben innerhalb
  von zwei Sekunden Feedback, ohne dass du etwas drückst.
- **Task- und Build-Checks** führen einen Labor-Task aus, zum Beispiel *CaDS: Build*, und
  erwarten Exit-Code 0.
- **ELF-Checks** (`symbolInElf`) suchen ein Symbol in `build/itsboard/cads-zero.elf` mit
  `arm-none-eabi-nm`.
- **Board-Checks** (`board`, `flash`, `serialExpect`, `debugStop`) fragen die Board-Bridge: ist
  das Board verbunden, gab es einen Flash seit Beginn des Steps, hat die Konsole ein Muster
  gedruckt, hat der Debugger bei Datei und Zeile angehalten. Ohne verbundenes Board melden sie
  *Nicht verfügbar* statt *Fehlgeschlagen*.
- **Fragen** (`question`) nehmen eine Freitext-Antwort entgegen, die das Sprachmodell gegen eine
  Rubrik bewertet, gegründet auf den Kursquellen. Ohne Sprachmodell bestätigst du die Antwort
  selbst.
- **Manuelle** Aufgaben haben einen Button *Als erledigt markieren*.

*Prüfen* führt eine Aufgabe aus, *Alle Checks ausführen* den ganzen Step. Ein bestandener Step
zeigt *Step erledigt!*, und eine Benachrichtigung nennt, was freigeschaltet wurde.

## 3. Hinweise, in drei Stufen

Schlägt ein Check fehl, zeigt das Panel zuerst eine Frage, zum Beispiel nach einem
fehlgeschlagenen Build: *Der Build sucht zuerst einen Compiler. Wo sucht er, und hat das zu einem
arm-none-eabi-gcc geführt?* Darunter zeigt *Hinweis anzeigen* den **Hinweis 1 von 3**. Der zweite
Fehlschlag schaltet Hinweis 2 frei, der dritte Hinweis 3. Hinweis 3 ist konkret; danach sagt das
Panel *Keine weiteren Hinweise – stell dem Tutor eine konkrete Frage.* Kursautoren schreiben
diese Hinweise je Aufgabe; wo keine existieren, greift der Tutor auf drei generische zurück.

<figure>
<img src="{{ '/assets/12-hint-tier.png' | relative_url }}" alt="Tutor-Panel mit der ersten Hinweis-Stufe unter einer Aufgabe: Hinweis 1 von 3 mit dem generischen ersten Hinweis">
<figcaption>Hinweis 1 von 3 nach dem ersten fehlgeschlagenen Check. Die nächste Stufe wird mit dem nächsten Fehlschlag frei.</figcaption>
</figure>

Derselbe Mechanismus reagiert auf Ereignisse: ein fehlgeschlagener Flash, ein Debugger-Halt, ein
`HardFault` oder `configASSERT` auf der Konsole. Der Tutor stellt eine Frage im Panel, nie in
einem modalen Dialog.

## 4. Frag den Tutor

<figure>
<img src="{{ '/assets/09-ask-tutor.png' | relative_url }}" alt="Tutor-Panel auf Deutsch mit ausgefülltem Fragefeld und dem Antwortbereich, der die gefundenen Quellen listet">
<figcaption>„Frag den Tutor“ auf einem Deployment ohne Sprachmodell: das Feld erklärt, dass das Modell nicht konfiguriert ist, und listet trotzdem die gefundenen Quellen.</figcaption>
</figure>

Das Textfeld am Ende jedes Steps sendet deine Frage zusammen mit dem Step-Kontext an das
Sprachmodell des Deployments. Bevor es antwortet, holt der Tutor Passagen aus den indizierten
Quellen (die cads-zero-Dokumentation plus die eigenen `sources/` des Kurses) per BM25-Suche.
Erreicht nichts die Schwelle des Kurses, bekommst du eine Ablehnung:
*Das liegt außerhalb des indizierten Referenzmaterials dieses Kurses – formuliere um oder frag zum
aktuellen Step.* Das ist beabsichtigt. Kurze Fragen wie „Wie flashe ich?“ können unter die
Schwelle fallen; frag stattdessen nach einer konkreten Datei, einem Register oder einem Symptom.

Antworten zitieren ihre **Quellen**. Auf einem Deployment ohne Sprachmodell sagt das Feld das und
zeigt trotzdem die Quellen, die es genutzt hätte, was oft reicht, um die Antwort selbst zu finden.

## 5. Proaktive Check-ins

Wenn du eine Datei speicherst, auf die der aktuelle Step verweist, und ein Sprachmodell
konfiguriert ist, bittet der Tutor es um ein kurzes Check-in zu deiner Änderung. Das Ergebnis
kommt als Benachrichtigung *CaDS Tutor hat Feedback zu deiner letzten Änderung.* mit
*Zeigen* / *Später*, höchstens einmal pro Minute. Abschalten kannst du das mit der Einstellung
`cadsTutor.checkInOnSave`.

## 6. Sprache

<figure>
<img src="{{ '/assets/08-tutor-panel-german.png' | relative_url }}" alt="Tutor-Panel auf Deutsch: Willkommen im CaDS-Firmware-Labor, Aufgaben mit Prüfen-Buttons">
<figcaption>Jeder Step existiert auf Deutsch und Englisch. Der Umschalter im Panel-Kopf wechselt Panel, Baum und Statusleiste.</figcaption>
</figure>

Der Panel-Kopf hat einen Umschalter *Deutsch* / *English*; die Befehlspalette bietet
**CaDS Tutor: Sprache wählen / Set language**. Die Wahl wird in deiner Session gespeichert.
Standardmäßig folgt der Tutor der Anzeigesprache von VS Code (`cadsTutor.language: auto`).

## 7. Fortschritt

<figure>
<img src="{{ '/assets/10-progress-view.png' | relative_url }}" alt="Ansicht Fortschritt in der Seitenleiste CaDS Tutor mit Lernzielen und Beherrschung">
<figcaption>Die Ansicht Fortschritt / Progress: Beherrschung je Lernziel, abgeleitet aus deinen Lernereignissen.</figcaption>
</figure>

Zwei Dinge werden gespeichert, beide im Container:

- `<workspace>/.cads-tutor/session.json`: aktueller Kurs und Step, Aufgabenstatus, deine Antworten.
- `~/.cads-tutor/events.sqlite`: Lernereignisse (bestandene und fehlgeschlagene Checks, gestellte
  Fragen), aus denen die Ansicht *Fortschritt / Progress* die Beherrschung je Lernziel ableitet.

Beides liegt in deinem Workspace-Volume und überlebt einen Container-Neustart. Zum Neustart des
Kurses führe **CaDS Tutor: Fortschritt zurücksetzen / Reset progress** aus; das löscht die Session
und behält die Lernereignisse (siehe
[Fortschritt zurücksetzen]({{ '/de/how-to/reset-progress/' | relative_url }})).

## Wo du jetzt stehst

Du kennst jedes Bedienelement des Tutors. Von hier an trägt dich der Kurs: öffne den nächsten
Step und arbeite ihn durch. Verhält sich etwas anders als auf diesen Seiten beschrieben, ist das
ein Issue wert.
