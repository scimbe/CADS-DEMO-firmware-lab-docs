---
title: Vorbereitung
order: 1
description: Was du vorher brauchst (Spoiler — fast nichts)
---

## Was du brauchst

- Einen modernen Browser (Chrome oder Edge — die ST-Link-Verbindung läuft über WebUSB, das
  Safari und Firefox noch nicht unterstützen).
- Einen GitHub-Account zum Einloggen.
- Sonst nichts. Kein Compiler, kein Debugger, keine Treiber zu installieren. Die IDE, die
  ARM-Toolchain und der ST-Link-Debug-Server laufen alle serverseitig; dein Browser muss sie nur
  *anzeigen* und per WebUSB mit dem Board sprechen.

<div class="callout warn">
<strong>Falls du Docker Desktop für Mac nutzt:</strong> USB-Passthrough in einen Container
funktioniert auf dieser Plattform nicht — das ist eine bestätigte Docker-für-Mac-Einschränkung,
kein Bug dieses Projekts. Die gehostete Version dieses Labs umgeht das, indem sie direkt aus
deinem Browser per WebUSB flasht statt aus einem Container heraus. Falls du eine eigene lokale
Kopie in einem Mac-Container betreibst: plane, vom Host aus zu flashen, nicht aus Docker heraus.
</div>

## Hardware (nur falls du echte Hardware nutzt)

- Ein NUCLEO-F429ZI + ITS-Adapter + Waveshare-4"-Shield ("ITSboard"), oder nutze einfach den
  eingebauten Simulator — alles in diesem Lab läuft auf beiden.
- Ein USB-Kabel vom ST-Link-Port des Boards zu deinem Rechner.
- Beim ersten Anstecken fragt dein Browser, welches ST-Link-Gerät du aus einer Liste auswählen
  willst — das ist der WebUSB-Berechtigungsdialog, und das ist normal.

## Vor deiner ersten Sitzung

1. Öffne die Lab-URL und logge dich mit GitHub ein.
2. Der Browser zeigt beim ersten Laden eines neuen Workspace vermutlich einen
   **Workspace-Vertrauen**-Dialog — das ist VS Codes eigener Standard-Prompt ("vertraust du den
   Autoren dieses Ordners"), nichts Lab-Spezifisches. Bestätige ihn; der Workspace ist das
   Starter-Projekt dieses Labs.
3. Das war's — weiter geht's mit [deiner ersten Lektion]({{ '/de/tutorials/erste-lektion/' | relative_url }}).

<p class="tagline">Falls hier etwas nicht mit dem übereinstimmt, was du tatsächlich siehst: schau als Nächstes in die <a href="{{ '/de/how-to/troubleshooting/' | relative_url }}">Troubleshooting-Anleitung</a>.</p>
