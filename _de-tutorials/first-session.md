---
title: Deine erste Sitzung
order: 1
description: Einloggen, dich in der Workbench zurechtfinden, das Tutor-Panel öffnen und Step 1 erledigen
---

Dieses Tutorial dauert etwa fünfzehn Minuten und braucht kein Board. Du loggst dich ein, schaust
dir an, was das Labor auf deinen Bildschirm gelegt hat, und erledigst den ersten Step des Kurses
*CaDS Zero – Grundlagen*.

## Was du brauchst

- Einen Chromium-basierten Browser (Chrome oder Edge). Firefox und Safari können später nicht
  mit dem Board sprechen, also starte gleich mit dem richtigen Browser.
- Die Labor-Adresse und das Passwort aus deinem Kurs. Das Labor läuft heute im
  Einzelplatz-Modus: eine Passwortseite, sonst nichts.

## 1. Einloggen

Öffne die Labor-Adresse. code-server zeigt ein einzelnes Passwortfeld.

<figure>
<img src="{{ '/assets/00-login.png' | relative_url }}" alt="Login-Seite von code-server mit einem einzelnen Passwortfeld">
<figcaption>Die Login-Seite. Gib das Passwort aus deinem Kurs ein und drücke Enter.</figcaption>
</figure>

Nach dem richtigen Passwort leitet der Browser in den Workspace
`/home/coder/workspace/cads-zero` weiter. Der Tab-Titel lautet `cads-zero — CaDS Firmware Lab`.

## 2. Was du siehst

<figure>
<img src="{{ '/assets/01-workbench-first-start.png' | relative_url }}" alt="Workbench nach dem ersten Login: Explorer mit dem cads-zero-Baum, Tutor-Step-Panel neben dem Editor, Statusleiste">
<figcaption>Erster Start. Das Tutor-Panel öffnet sich von selbst, weil es noch keine gespeicherte Session gibt.</figcaption>
</figure>

Von links nach rechts:

- **Activity Bar.** Die üblichen VS-Code-Symbole plus ein Doktorhut-Symbol mit dem Titel
  *CaDS Tutor*.
- **Explorer.** Das Firmware-Repository [CaDS Zero](https://github.com/scimbe/cads-zero), bereits
  geklont und einmal gebaut. `build/itsboard/` enthält ein fertiges `cads-zero.elf` und
  `cads-zero.bin`.
- **Editorbereich.** Beim ersten Start leer. Das Tutor-Panel öffnet sich daneben.
- **Statusleiste.** CMake Tools zeigt *No Configure Preset Selected*. Das ist so gewollt: die
  Labor-Tasks rufen CMake selbst auf, du musst kein Preset wählen. Sobald der Tutor einen Step
  hat, zeigt die Statusleiste `🎓 Tutor: <Step-Titel>`. Mit installierter Board-Bridge erscheint
  außerdem ein Eintrag `Board: getrennt` (siehe das
  [nächste Tutorial]({{ '/de/tutorials/build-and-flash/' | relative_url }})).

Nichts fragt dich, ob du dem Workspace vertraust, nichts fragt nach einem CMake-Preset, und
keine Chat-Seitenleiste öffnet sich. Siehst du ein Banner *Restricted Mode*, bist du auf einem
alten Deployment; siehe [Troubleshooting]({{ '/de/how-to/troubleshooting/' | relative_url }}).

## 3. Das Tutor-Panel

<figure>
<img src="{{ '/assets/02-tutor-panel-step1.png' | relative_url }}" alt="Tutor-Step-Panel mit Step 1 von 41, Welcome to the CaDS firmware lab, mit Aufgaben und Check-Buttons">
<figcaption>Step 1 von 41: der Willkommens-Step des Grundlagenkurses.</figcaption>
</figure>

Jeder Step hat dieselbe Form:

1. Eine Kopfzeile mit dem Step-Titel, *Step n von N*, der geschätzten Zeit und der Bloom-Stufe.
2. Das Lernziel und ein kurzer Text.
3. **Aufgaben** mit Status und einem Button *Prüfen*. Manche Checks laufen automatisch
   (Dateien, Builds, ELF-Symbole, Board-Zustand), manche stellen dir eine Frage, und einige
   markierst du selbst mit *Als erledigt markieren*.
4. **Frag den Tutor**, ein Textfeld für Fragen zum aktuellen Step.
5. *← Zurück* und *Weiter →*. Der nächste Step wird freigeschaltet, wenn alle Aufgaben des
   aktuellen bestanden sind.

## 4. Der Kursbaum

Klicke auf das Doktorhut-Symbol in der Activity Bar.

<figure>
<img src="{{ '/assets/03-tutor-tree.png' | relative_url }}" alt="Seitenleiste CaDS Tutor mit dem Kursbaum: Kurs, Module M0 bis M8, Steps mit Schloss-Symbolen">
<figcaption>Die Ansicht Kurse / Courses: Kurs → Modul → Step. Gesperrte Steps zeigen ein Schloss, bis ihre Voraussetzungen erfüllt sind.</figcaption>
</figure>

Zwei Kurse sind installiert: *CaDS Zero – Grundlagen* (Pflicht, neun Module, 41 Steps) und der
Projektkurs cads-zero-projects (Wahl, sechs Projektaufgaben). Die Ansicht *Fortschritt / Progress*
unter dem Baum listet deine Beherrschung je Lernziel. Ein Klick auf einen Step öffnet ihn im Panel.

## 5. Step 1 erledigen

Step 1 hat zwei Aufgaben.

- **Du hast den Tutor geöffnet.** Eine manuelle Aufgabe. Klicke *Als erledigt markieren*.
- **Benenne die drei gestapelten Hardware-Teile.** Eine Frage. Schreib deine Antwort in das
  Feld und klicke *Antwort abgeben*. Auf diesem Deployment bewertet das Sprachmodell die Antwort,
  wenn eines konfiguriert ist. Ohne Sprachmodell speichert der Tutor deine Antwort und bittet
  dich, sie selbst zu bestätigen.

Der Step-Text enthält alles, was die Frage braucht: ein NUCLEO-F429ZI mit dem STM32F429ZI, das
ITS-Adapterboard und das Waveshare-4-Zoll-Touch-Shield. Wenn beide Aufgaben bestanden sind, zeigt
das Panel *Step erledigt!* und Step 2, *Das Board verbinden*, wird freigeschaltet.

## Wo du jetzt stehst

Du hast einen funktionierenden Editor, eine gebaute Firmware und einen offenen Kurs. Das nächste
Tutorial steckt das Board an und bringt deinen ersten Build darauf:
[Bauen und flashen]({{ '/de/tutorials/build-and-flash/' | relative_url }}).
