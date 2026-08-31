---
title: Troubleshooting / FAQ
order: 1
description: Funktioniert etwas nicht? Zuerst hier nachschauen
---

Jeder Punkt unten ist ein echtes Problem, das beim Bauen und Testen dieses Labs tatsächlich
aufgetreten und behoben wurde — keine generische Checkliste.

## Flashen

**Ich habe Flash geklickt und nichts ist passiert — kein Fehler, nichts.**
Zwei getrennte, stille Lücken, die beide genau dieses Symptom erzeugen:
1. Der Flash-Button bleibt *deaktiviert*, bis das Ziel vorher explizit **Halted** wurde. Erst
   Halt klicken, dann Flash.
2. Der Klick-Handler tut still nichts, wenn im Dateiauswahl-Dialog gar keine Datei ausgewählt
   ist — prüfe, ob wirklich eine `.bin`-Datei ausgewählt ist, nicht nur, dass der Dialog geöffnet
   wurde.

**Das Board taucht beim Verbinden nicht auf.**
Stelle sicher, dass du Chrome oder Edge nutzt — WebUSB (worüber dieses Lab mit dem ST-Link
spricht) wird in Safari oder Firefox nicht unterstützt. Der erste Verbindungsversuch sollte einen
Browser-Berechtigungsdialog mit dem ST-Link-Gerät zeigen; falls der nicht erscheint, hat der
Browser oder das Betriebssystem eventuell gar keinen USB-Zugriff erlaubt — prüfe die
USB-Geräteberechtigungen deines Betriebssystems für den Browser.

**Ich betreibe das lokal in Docker auf einem Mac, und Flashen funktioniert nie.**
Das ist eine bestätigte Docker-Desktop-für-Mac-Einschränkung: USB-Geräte können auf dieser
Plattform nicht in einen Linux-Container durchgereicht werden. Das lässt sich nicht aus dem
Container heraus beheben. Die gehostete Version dieses Labs umgeht das komplett, indem sie direkt
aus deinem Browser per WebUSB flasht statt aus einem Container heraus — falls du eine lokale Kopie
betreibst, flashe vom Host aus, nicht aus Docker heraus.

## Der Tutor

**Der Tutor hat mir einen HTTP-401-/Authentifizierungsfehler gegeben.**
Falls du eine lokale Kopie gegen deinen eigenen LLM-Endpunkt betreibst: prüfe, ob die
Endpunkt-URL wirklich `https://` nutzt, nicht `http://`. Eine reine HTTP-Endpunkt-URL war die
tatsächliche Ursache eines echten 401-Fehlers beim Bauen dieses Labs — sah nach einem
Credentials-Problem aus, war aber keins.

**Der Tutor antwortet nicht / gibt eine Ablehnung statt einer Antwort.**
Das ist oft korrektes Verhalten, kein Bug: der Tutor ist so gebaut, dass er nur aus indizierten
Referenzquellen antwortet, und gibt lieber ehrlich "dazu habe ich keine belegte Quelle" zurück,
statt zu raten, wenn nichts im Index wirklich relevant ist. Falls du denkst, er sollte die Antwort
kennen, ist das eine Meldung wert — es kann bedeuten, dass der Referenz-Index erweitert werden
muss, nicht dass etwas kaputt ist.

## Die IDE selbst

**Ein "Vertraust du den Autoren dieses Workspace"-Dialog erschien.**
Das ist VS Codes eigener Standard-Workspace-Vertrauen-Dialog, nichts Lab-Spezifisches — bestätige
ihn für den Starter-Workspace des Labs.

**`Ctrl+Shift+P` öffnet die Command Palette nicht.**
Der Browser selbst kann dieses Tastenkürzel abfangen. Nutze stattdessen `F1` — das öffnet in
dieser Umgebung immer die Command Palette.

## Immer noch festgefahren?

[Öffne ein Issue](https://github.com/scimbe/CADS-DEMO-firmware-lab/issues/new) mit dem, was du
versucht hast und was du gesehen hast — eine echte Meldung, auch eine kurze, ist das, was diese
Seite genau hält.
