---
layout: default
title: Wenn eine Prüfung nicht bestehen will (Rust)
lang: de
permalink: /de/rust/when-a-check-fails/
---

# Wenn eine Prüfung nicht bestehen will

Eine rote Prüfung ist der normale Zustand einer Übung, bevor Sie sie lösen. Diese Seite ist für den
Fall, dass Sie es versucht haben und es trotzdem nicht grün wird.

## Zuerst: die Meldung lesen, nicht die Farbe

`cargo` sagt Ihnen, was es will, und zwar ungewöhnlich gut. Jeder Compiler-Fehler hat einen Code wie
`E0382`, eine Zeile mit Spalte und oft einen Vorschlag. Der Kurs ist absichtlich um diese Meldungen
herum gebaut — mehrere Schritte gibt es nur, damit Sie einem bestimmten Fehler unter kontrollierten
Bedingungen begegnen und lernen, ihn zu lesen.

Arbeiten Sie vom **ersten** Fehler abwärts. Spätere Fehler sind häufig nur Folgen des ersten und
verschwinden von selbst.

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
| `could not find Cargo.toml` | Terminal eine Ebene über der Crate | `cd ~/workspace/rust-foundations` |
| **Keine Übereinstimmung** in der Palette | Palette im Dateimodus | ein `>` vor den Befehlsnamen tippen |
| Befehl scheint zu hängen, nichts erscheint | er läuft noch | warten, bis die Eingabeaufforderung zurückkommt |
| Ausgabe fehlt vollständig | Sie sehen auf Probleme oder Ausgabe | auf den Reiter **Terminal** wechseln |
| `cargo` selbst nicht gefunden | Werkzeugkette fehlt im Container | ein Umgebungsfehler — melden, im Editor nicht behebbar |

## Wenn der Tutor eine Frage stellt statt zu prüfen

Manche Aufgaben wollen eine Erklärung statt eines Befehls. Der Tutor bewertet Ihre Begründung gegen
eine Vorgabe — und er sagt Ihnen auch, was **nicht** durchgeht, nicht nur was durchgeht. Ein Stichwort
ist keine Antwort; zwei, drei Sätze, die Ursache und Wirkung verbinden, sind eine.

Ist auf Ihrer Installation kein Sprachmodell hinterlegt, zeigt der Tutor diese Vorgabe und bittet Sie,
sich selbst zu kontrollieren. Seien Sie dabei ehrlich: Das Ergebnis wird als selbst berichtet
vermerkt, und der Zweck der Übung ist Ihr Verständnis, nicht der Haken.

## Immer noch fest

Fragen Sie den Tutor. Er antwortet aus dem erschlossenen Kursmaterial und der Dokumentation der
Werkzeugkette und verweigert lieber eine Antwort, als sich eine auszudenken, wenn er sie nicht auf
eine Quelle stützen kann. Fragen Sie auf Deutsch oder Englisch, wie Sie mögen.

## Verwandtes

- [Befehle und Aufgaben ausführen]({{ '/de/rust/working-the-window/' | relative_url }})
- [Die erste Sitzung]({{ '/de/rust/first-session/' | relative_url }})
- [Rust-Tutor-Doku]({{ '/de/rust/' | relative_url }})
