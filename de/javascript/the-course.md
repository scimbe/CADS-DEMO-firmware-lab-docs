---
layout: default
title: Was der JavaScript-Kurs behandelt
lang: de
permalink: /de/javascript/the-course/
---

# Was der Kurs behandelt

31 Schritte in acht Modulen. Der Tutor gibt sie der Reihe nach frei, Sie müssen also nie
entscheiden, was als Nächstes kommt. Jeder Schritt nennt sein Lernziel, gibt Ihnen etwas zum
Ausführen und verlangt eine Erklärung, bevor er als verstanden zählt. Programmiererfahrung wird
nicht vorausgesetzt.

## M0 — Werkzeuge

Das Fenster und die Laufzeit, noch nicht die Sprache. Dieses Modul zu überspringen ist der
zuverlässigste Weg, in Modul 1 steckenzubleiben.

| Schritt | Was Sie tun |
|---|---|
| Die Oberfläche bedienen | Die fünf Teile des Fensters, drei Wege zu einem Befehl, ein Terminal schließen |
| Dein erster Lauf | Eine Datei mit Node ausführen, und was die zurückkehrende Eingabeaufforderung bedeutet |
| Einen Test lesen | Was eine fehlgeschlagene Zusicherung sagt, und warum Rot der normale Anfang ist |
| Module, Exporte und Importe | Warum ein fehlender Export eine ganze Testdatei am Laden hindert |
| Erst vorhersagen, dann ausführen | Aufschreiben, was Sie erwarten — die Gewohnheit, auf der der ganze Kurs aufbaut |

## M1 — Werte und Typen

| Schritt | Was Sie tun |
|---|---|
| `let`, `const` und die Temporal Dead Zone | Wo ein Name existiert und wo es nur so aussieht |
| Typen und was `typeof` dir nicht sagt | Die ehrlichen und die unehrlichen Antworten des Typsystems |
| Typumwandlung, `+` und der Wert, der nichts gleicht | Warum `+` mal addiert und mal aneinanderhängt |
| `==` gegen `===`, und der eine Fall, den `===` falsch beantwortet | Die Vergleichsregeln samt Ausnahme |

## M2 — Ablaufsteuerung und Fehlerbehandlung

| Schritt | Was Sie tun |
|---|---|
| `if`, `else` und ein switch, der durchfällt | Verzweigen, und das fehlende `break` |
| Truthy, falsy und Standardwerte, die deine Werte auffressen | Warum `0` und `""` dort verschwinden, wo man es nicht erwartet |
| `try`, `catch`, `finally` und wer den Fehler bekommt | Wohin ein Fehler geht, wenn man ihn nicht fängt |
| Fehlerobjekte und eine eigene Fehlerklasse | Fehler, die tragen, was die aufrufende Seite braucht |

## M3 — Schleifen und Iteration

| Schritt | Was Sie tun |
|---|---|
| `for` und `while`, und welche wozu passt | Die Schleife danach wählen, was man vorher wirklich weiß |
| Off by one und der Fehler, den es dir gibt | Der klassische Zählfehler und wie die Ausgabe ihn verrät |
| `for…of` gegen `for…in` | Werte gegen Schlüssel, und der Fehler aus der Verwechslung |
| `break`, `continue` und ein benannter Ausgang | Eine Schleife bewusst verlassen |

## M4 — Funktionen und Closures

| Schritt | Was Sie tun |
|---|---|
| Deklarationen, Ausdrücke und wann ein Name existiert | Hoisting in der Form, die in der Praxis zählt |
| Standard- und Rest-Parameter | Funktionen, die nehmen, was sie bekommen |
| Closures und was eine Schleifenvariable einfängt | Die klassische Closure-Falle, ausgeführt statt beschrieben |
| Pfeilfunktionen und der Verlust von `this` | Zwei Funktionsformen und der Unterschied, der beißt |

## M5 — Objekte und Arrays

| Schritt | Was Sie tun |
|---|---|
| Objekte, Referenzen und Kopien | Wer sonst noch das hält, was Sie gerade geändert haben |
| Durch Ebenen lesen, die es vielleicht nicht gibt | Optionale Verkettung statt einer Kette von Abfragen |
| Arrays, `length` und wem die Daten gehören | An Ort und Stelle ändern gegen Neues erzeugen |
| `map`, `filter`, `reduce` und ein sort, das lügt | Die Transformationen, und die Überraschung der Standardsortierung |

## M6 — Nebenläufigkeit

| Schritt | Was Sie tun |
|---|---|
| Promises und was ein ausstehender Wert ist | Ein Wert, der noch nicht da ist |
| `async`, `await` und das fehlende `await` | Der Fehler, der ein Promise liefert, wo ein Ergebnis erwartet wurde |
| Fehler, die spät ankommen | Fehlschläge, die kein `try` um den Aufruf herum fängt |
| Nacheinander oder gleichzeitig, und was ein Aufrufer erfahren muss | Bewusst wählen und die Wahl dokumentieren |

## M7 — Abschlussprojekt

| Schritt | Was Sie tun |
|---|---|
| Das Report-Werkzeug entwerfen | Die Struktur festlegen, bevor Code entsteht |
| Das Report-Werkzeug bauen und selbst testen | Umsetzen und eigene Testfälle erfinden |

Der letzte Schritt verlangt, die Tests selbst zu schreiben statt sie nur zu bestehen: Sie müssen
entscheiden, was prüfenswert ist, und das ist eine andere Fähigkeit, als einen vorgegebenen Test
grün zu bekommen.

## Verwandtes

- [Die erste Sitzung]({{ '/de/javascript/first-session/' | relative_url }})
- [Wenn eine Prüfung nicht bestehen will]({{ '/de/javascript/when-a-check-fails/' | relative_url }})
- [JavaScript-Tutor-Doku]({{ '/de/javascript/' | relative_url }})
