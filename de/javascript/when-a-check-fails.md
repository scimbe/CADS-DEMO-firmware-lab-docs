---
layout: default
title: Wenn eine Prüfung nicht bestehen will (JavaScript)
lang: de
permalink: /de/javascript/when-a-check-fails/
---

# Wenn eine Prüfung nicht bestehen will

Ein roter Test ist der normale Zustand einer Übung, bevor Sie sie lösen. Diese Seite ist für den
Fall, dass Sie es versucht haben und es trotzdem nicht grün wird.

## Zuerst: die Ausgabe lesen, nicht die Farbe

Der Testläufer von Node nennt die fehlgeschlagene Zusicherung, was sie erwartet hat und was
tatsächlich herauskam. Dieser Vergleich ist meist die ganze Antwort. Mehrere Schritte gibt es nur,
damit Sie einem bestimmten Fehlschlag unter kontrollierten Bedingungen begegnen und lernen, ihn zu
lesen.

Zwei Arten von Fehlschlag lohnt es zu unterscheiden:

- **Ein Test ist fehlgeschlagen.** Ihr Code lief und lieferte den falschen Wert. Die Zeilen mit
  Erwartung und Ergebnis sagen, welchen.
- **Die Testdatei ließ sich gar nicht laden.** Dann lief nichts darin. Üblicher Grund ist ein
  fehlender oder falsch geschriebener Export — genau das, was manche Übungen von Ihnen verlangen.
  Die Meldung sagt dann, dass die Datei nicht geladen werden konnte, statt einen einzelnen Test zu
  nennen.

## Die Hinweisleiter

Jede Aufgabe hat Hinweise in drei Stufen. Fragen Sie sie der Reihe nach ab:

1. **Eine Frage**, die auf die Stelle zeigt, ohne zu sagen, was falsch ist.
2. **Ein engerer Hinweis**, der das Konzept oder die geltende Regel benennt.
3. **Eine konkrete Richtung**, aber nie die einzusetzende Zeile.

Die Stufen sind so geschnitten, dass der Teil der Arbeit bei Ihnen bleibt, der den Lernerfolg
erzeugt. Wenn auch die dritte Stufe Sie stecken lässt, sagen Sie das Ihrer Lehrperson: Meist setzt
der Schritt dann etwas voraus, was er nie vermittelt hat.

## Die fünf Fehlschläge, die nicht an Ihrem Code liegen

| Symptom | Ursache | Behebung |
|---|---|---|
| `Cannot find module …` | Terminal eine Ebene über den Übungen | `cd ~/workspace/javascript-foundations` |
| **Keine Übereinstimmung** in der Palette | Palette im Dateimodus | ein `>` vor den Befehlsnamen tippen |
| Befehl scheint zu hängen, nichts erscheint | er läuft noch | warten, bis die Eingabeaufforderung zurückkommt |
| Ausgabe fehlt vollständig | Sie sehen auf Probleme oder Ausgabe | auf den Reiter **Terminal** wechseln |
| `node` selbst nicht gefunden | Laufzeit fehlt im Container | ein Umgebungsfehler — melden, im Editor nicht behebbar |

## Wenn der Tutor eine Frage stellt statt zu prüfen

Manche Aufgaben wollen eine Erklärung statt eines Befehls. Der Tutor bewertet Ihre Begründung gegen
eine Vorgabe — und er sagt Ihnen auch, was **nicht** durchgeht, nicht nur was durchgeht. Ein Stichwort
ist keine Antwort; zwei, drei Sätze, die Ursache und Wirkung verbinden, sind eine.

Ist auf Ihrer Installation kein Sprachmodell hinterlegt, zeigt der Tutor diese Vorgabe und bittet Sie,
sich selbst zu kontrollieren. Seien Sie dabei ehrlich: Das Ergebnis wird als selbst berichtet
vermerkt, und der Zweck der Übung ist Ihr Verständnis, nicht der Haken.

## Immer noch fest

Fragen Sie den Tutor. Er antwortet aus dem erschlossenen Kursmaterial und der Dokumentation der
Laufzeit und verweigert lieber eine Antwort, als sich eine auszudenken, wenn er sie nicht auf eine
Quelle stützen kann. Fragen Sie auf Deutsch oder Englisch, wie Sie mögen.

## Verwandtes

- [Befehle und Aufgaben ausführen]({{ '/de/javascript/working-the-window/' | relative_url }})
- [Die erste Sitzung]({{ '/de/javascript/first-session/' | relative_url }})
- [JavaScript-Tutor-Doku]({{ '/de/javascript/' | relative_url }})
