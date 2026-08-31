---
title: Deine erste Lektion
order: 1
description: Einloggen, bauen, flashen und dem Tutor eine echte Frage stellen — von Anfang bis Ende
---

Das hier geht eine komplette Sitzung von Anfang bis Ende durch: einloggen, sich in der IDE
umsehen, die Starter-Firmware bauen, sie auf einen echten Chip flashen und dem eingebauten Tutor
eine Frage zu dem stellen, was gerade passiert ist. Jeder Screenshot unten stammt aus einem
echten Durchlauf.

## 1. Einloggen

Öffne die Lab-URL und logge dich mit deinem GitHub-Account ein.

<figure>
<img src="{{ '/assets/00-login.png' | relative_url }}" alt="Login-Bildschirm">
<figcaption>Der Login-Bildschirm — GitHub-OAuth, sonst nichts zu konfigurieren.</figcaption>
</figure>

## 2. Umsehen

Du landest in einem vollständigen VS-Code-Workspace, der im Browser läuft: ein Dateibaum links,
ein Editor in der Mitte, ein Terminal unten.

<figure>
<img src="{{ '/assets/01-ide-workspace.png' | relative_url }}" alt="IDE-Workspace">
<figcaption>Der Starter-Workspace — das ist echtes VS Code for the Web, kein Nachbau.</figcaption>
</figure>

## 3. Bauen

Öffne das Terminal und baue die Firmware:

```bash
cmake --build build/itsboard
```

<figure>
<img src="{{ '/assets/02-build-terminal.png' | relative_url }}" alt="Build-Ausgabe im Terminal">
<figcaption>Ein echter ARM-GCC-Build, serverseitig ausgeführt, live ins Terminal gestreamt.</figcaption>
</figure>

## 4. Flashen

Verbinde das Board per WebUSB und flashe das Binary, das du gerade gebaut hast. Das nutzt den
eigenen ST-Link-Treiber des Browsers — keine lokalen Tools nötig.

<div class="callout warn">
Der <strong>Flash</strong>-Button bleibt deaktiviert, bis das Ziel vorher explizit
<strong>Halted</strong> wurde — klicke also erst Halt, dann Flash, falls der Button ausgegraut
wirkt. Und falls du Flash klickst und sichtbar nichts passiert: prüfe, ob im Dateiauswahl-Dialog
wirklich eine Datei ausgewählt ist — eine leere Auswahl tut still nichts, statt einen Fehler zu
zeigen.
</div>

## 5. Den Tutor fragen

Öffne die Command Palette und suche den Tutor-Befehl.

<div class="callout">
Auf manchen Tastaturlayouts öffnet <code>Ctrl+Shift+P</code> im Browser eventuell nicht die
Command Palette (der Browser selbst kann das abfangen) — <code>F1</code> funktioniert immer als
Fallback.
</div>

<figure>
<img src="{{ '/assets/03-command-palette-tutor.png' | relative_url }}" alt="Command Palette mit Tutor-Befehl">
<figcaption>Der Tutor ist ein Befehl, keine separate App — ruf ihn auf, wo immer du gerade arbeitest.</figcaption>
</figure>

Frag ihn etwas Echtes zu dem Code, den du gerade geflasht hast — zum Beispiel, warum ein
bestimmter Registerzugriff im Startup-Code genau das tut, was er tut.

<figure>
<img src="{{ '/assets/04-tutor-step1.png' | relative_url }}" alt="Tutor stellt eine Rückfrage">
<figcaption>Der Tutor stellt sich als CaDS Tutor vor und stellt vor der Antwort eine Rückfrage.</figcaption>
</figure>

<figure>
<img src="{{ '/assets/05-tutor-llm-answer.png' | relative_url }}" alt="Tutor gibt eine belegte Antwort mit Quellenangaben">
<figcaption>Eine echte Antwort, belegt mit zitierten Quellen — kein Raten.</figcaption>
</figure>

## Was du gerade gemacht hast

Du hast echte Firmware aus nichts als einem Browser-Tab heraus auf einen echten Chip gebaut und
geflasht, und eine echte, belegte Erklärung bekommen, was sie tut. Das ist das ganze Lab im
Kleinen — alles Weitere ist mehr davon, an schwierigeren Aufgaben.

Weiter geht's: falls oben etwas nicht mit dem übereinstimmt, was du gesehen hast, schau in die
[Troubleshooting-Anleitung]({{ '/de/how-to/troubleshooting/' | relative_url }}).
