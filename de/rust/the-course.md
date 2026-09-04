---
layout: default
title: Was der Rust-Kurs behandelt
lang: de
permalink: /de/rust/the-course/
---

# Was der Kurs behandelt

31 Schritte in acht Modulen. Der Tutor gibt sie der Reihe nach frei, Sie müssen also nie
entscheiden, was als Nächstes kommt. Jeder Schritt nennt sein Lernziel, gibt Ihnen etwas zum
Ausführen und verlangt eine Erklärung, bevor er als verstanden zählt.

## M0 — Werkzeuge und das erste Programm

Das Fenster und die Werkzeugkette, noch nicht die Sprache. Dieses Modul zu überspringen ist der
zuverlässigste Weg, in Modul 1 steckenzubleiben.

| Schritt | Was Sie tun |
|---|---|
| Wo du bist und was du zuerst drückst | Orientierung: was diese Umgebung ist, was schon installiert ist |
| Die Oberfläche bedienen | Die fünf Teile des Fensters, drei Wege zu einem Befehl, ein Terminal schließen |
| Einen Test lesen, dann bestehen lassen | Ihr erstes `cargo test`, und was ein roter Test aussagt |
| Die Ausgabe vorhersagen, dann ausführen | Erst aufschreiben, was Sie erwarten — die Gewohnheit, auf der der ganze Kurs aufbaut |
| Eine Compilerfehlermeldung lesen und die Datei reparieren | Der Compiler als Lehrmittel statt als Hindernis |

## M1 — Eigentümerschaft

| Schritt | Was Sie tun |
|---|---|
| Gültigkeitsbereich, Eigentümer, Move | Wem ein Wert gehört und wann er aufgeräumt wird |
| Move oder Clone: was du wirklich brauchst | Was `clone` kostet und wann es der falsche Reflex ist |
| Copy-Typen: wenn eine Zuweisung kein Move ist | Warum manche Zuweisungen das Original nutzbar lassen |
| Ownership über Funktionsgrenzen hinweg | Werte übergeben und zurückbekommen |

## M2 — Referenzen und Ausleihen

| Schritt | Was Sie tun |
|---|---|
| Leihen statt nehmen | Geteilte Referenzen und was sie erlauben |
| Veränderliche Referenzen | Ein Schreiber, und was der Compiler dazu sagt |
| Die Aliasing-Regel: Leser oder ein Schreiber | Die Regel hinter der Hälfte aller Borrow-Checker-Fehler |
| Slices: eine Leihe auf einen Teil einer Sammlung | Sichten auf Daten, ohne sie zu kopieren |

## M3 — Strukturen und Aufzählungen

| Schritt | Was Sie tun |
|---|---|
| Structs: Werte, die zusammengehören | Daten modellieren, die als Einheit reisen |
| Enums: eine von mehreren Formen | Zustände, die ein Wert annehmen kann, explizit gemacht |
| `match`: jeder Fall, geprüft | Vollständigkeit, und warum der Compiler darauf besteht |
| `if let` und `let … else` | Die Kurzformen und wann sie sich besser lesen |

## M4 — Sammlungen

| Schritt | Was Sie tun |
|---|---|
| Vektoren: eine wachsende Liste | Aufbauen, zugreifen, durchlaufen |
| Strings sind UTF-8, und das ändert einiges | Bytes, Zeichen und die Fallen dazwischen |
| Hash-Maps und das entry-Idiom | Zählen und Gruppieren ohne wiederholtes Nachschlagen |
| Die drei Sammlungen im Zusammenspiel | Die richtige für eine echte Aufgabe wählen |

## M5 — Fehlerbehandlung

| Schritt | Was Sie tun |
|---|---|
| `panic!` ist für Programmfehler | Der Unterschied zwischen Programmfehler und erwartetem Fehlschlag |
| `Result`: Fehlschlag im Rückgabetyp | Fehlschläge für die aufrufende Seite sichtbar machen |
| Der `?`-Operator | Fehler weiterreichen ohne Umstände |
| Ein eigener Fehlertyp | Ein Fehler, der trägt, was die aufrufende Seite braucht |

## M6 — Generik, Traits und Lebensdauern

| Schritt | Was Sie tun |
|---|---|
| Generics: eine Funktion, viele Typen | Code einmal schreiben, für viele Typen |
| Traits: gemeinsames Verhalten mit Namen | Beschreiben, was ein Typ kann |
| Trait-Schranken: genau das verlangen, was du brauchst | Generik einschränken, und die Meldung lesen, wenn man es nicht tut |
| Lifetimes: wie lange eine Leihe gilt | Das letzte Stück des Borrow-Checkers |

## M7 — Abschlussprojekt

| Schritt | Was Sie tun |
|---|---|
| `wordstat` bauen | Ein kleines Werkzeug, das alles Vorherige benutzt |
| Das eigene Werkzeug begutachten | Den eigenen Code an Kriterien messen, die Sie selbst anwenden müssen |

Der letzte Schritt ist bewusst eine Bewertung und keine weitere Übung: Sie begründen Ihre eigenen
Entwurfsentscheidungen und vertreten die Abwägungen, die Sie getroffen haben.

## Verwandtes

- [Die erste Sitzung]({{ '/de/rust/first-session/' | relative_url }})
- [Wenn eine Prüfung nicht bestehen will]({{ '/de/rust/when-a-check-fails/' | relative_url }})
- [Rust-Tutor-Doku]({{ '/de/rust/' | relative_url }})
