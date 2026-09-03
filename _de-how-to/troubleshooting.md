---
title: Troubleshooting / FAQ
order: 9
description: Reale Befunde aus Bau und Test des Labors, jeweils mit Lösung
---

Jeder Eintrag unten ist beim Bauen, Testen oder Betreiben dieses Labors tatsächlich aufgetreten.
Allgemeine Ratschläge fehlen absichtlich.

## Die IDE

### Der Workspace öffnet im „Restricted Mode“ und die Extensions sind aus

Du bist auf einem alten Deployment, dessen `docker run` `--disable-workspace-trust` nicht
übergeben hat. Seit Image-Tag `next-8a20ec9` ist das Flag Teil der Kommandozeile des Images
selbst, zusammen mit `--disable-telemetry` und `--disable-update-check`, sodass ein einfaches
`docker run` korrekt ist. Bitte den Betreiber, das aktuelle Image zu ziehen. Einen
Vertrauens-Dialog gibt es nicht mehr zu bestätigen.

### Eine CMake-Tools-Benachrichtigung sagt „It is recommended to reconfigure after upgrading to a new kits definition“

Beim ersten Start eines frischen Containers aus dem Image `next-8a20ec9` gesehen, wenige
Sekunden nachdem die Workbench geladen war. Schließe sie. Die Labor-Tasks rufen `cmake` selbst
auf und brauchen die Konfiguration von CMake Tools nicht; *Configure Now* schadet auch nicht, es
führt nur das Preset `itsboard` ein zweites Mal aus. Images, die nach dem 2026-09-03 gebaut
wurden, schalten den Kit-Scan ab; dort erscheint die Benachrichtigung nicht mehr.

### Die Statusleiste sagt „No Configure Preset Selected“

So gewollt. `cmake.configureOnOpen` ist im Image aus, damit niemand nach einem Preset gefragt
wird, bevor er irgendetwas getan hat. Die Tasks **CaDS: Build** und **CaDS: Host tests** führen
die Presets selbst aus. Willst du den eigenen Build-Button von CMake Tools, wähle in der
Statusleiste einmal `ITSboard (STM32F429ZI)`.

### Ctrl+Shift+P öffnet die Befehlspalette nicht

Der Browser kann das Tastenkürzel abfangen. **F1** öffnet die Palette in dieser Umgebung immer.
Siehe [Tastenkürzel]({{ '/de/reference/keyboard-shortcuts/' | relative_url }}).

### „Cannot reconnect. Please reload the window.“ nach einem Server-Neustart

Der WebSocket zu code-server ist verloren gegangen, typischerweise weil der Betreiber den
Container neu gestartet hat. Lade die Seite neu. Deine Dateien liegen auf der Platte; ungespeicherte
Editorinhalte stellt VS Code per Hot Exit wieder her, wo möglich, und der Tutor setzt seine
Session aus `session.json` fort.

## Das Board

### Der Geräte-Dialog erscheint nicht

Prüfe in dieser Reihenfolge:

1. **Browser.** Chrome oder Edge. Firefox und Safari haben kein WebUSB/WebSerial; der Befehl
   *Verbinden* scheitert dann mit einem `NO_DEVICE`-Fehler.
2. **HTTPS.** `navigator.usb` existiert nur auf sicheren Origins. Eine selbst gehostete Kopie,
   die über einfaches `http://<hostname>` erreicht wird, bekommt keinen Dialog;
   `http://127.0.0.1` und `localhost` sind ausgenommen.
3. **Richtlinie.** Verwaltete Browser können die Geräte-APIs sperren
   (`DefaultWebUsbGuardSetting`, `DefaultSerialGuardSetting`). Sieh in `chrome://policy` nach.
4. **Fokus.** Der Dialog wird durch eine Nutzergeste im Hauptfenster geöffnet. Klicke den
   Statusleisten-Eintrag oder führe den Befehl aus der Palette aus; ein aus einem Skript
   abgefeuerter Befehl zählt nicht.
5. **Linux.** Ohne die udev-Regel wird das Gerät gelistet, lässt sich aber nicht öffnen; siehe
   [Board anschließen]({{ '/de/how-to/connect-the-board/' | relative_url }}#linux).

### „Das Board wird bereits in einem anderen Tab dieses Labors benutzt.“

Genau das. Ein Board kann in nur einem Browser-Tab geöffnet sein, und das Labor stellt das jetzt
fest, **bevor** es USB anfasst – über eine Sperre, die alle Tabs deines Browserprofils teilen.

Schließe den anderen Tab, oder wähle dort im Board-Menü **Board freigeben**. Danach hier erneut
verbinden. Findest du den anderen Tab nicht: alle Tabs des Labors schließen und einen wieder
öffnen.

### „Ein anderes Programm auf deinem Rechner hält das Board.“

Ein Programm außerhalb des Browsers hat die ST-Link geöffnet: `st-flash`, `st-util`, der
STM32CubeProgrammer, eine IDE oder ein zweiter Browser mit geöffnetem Labor. Der Browser kann
sich ein USB-Gerät nicht mit ihnen teilen – beende das Programm und verbinde erneut.

Diese Meldung und die vorige sehen für den Browser identisch aus: beide erzeugen
`NetworkError: Unable to claim interface`. Das Labor unterscheidet sie daran, ob die Sperre
innerhalb deines eigenen Browserprofils belegt ist – deshalb der unterschiedliche Text.

### „Board freigeben“ – das Board an jemand anderen übergeben

Im Board-Menü steht **Board freigeben**. Es schließt USB-Gerät und seriellen Port und gibt die
Sperre frei, sodass ein anderer Tab, ein anderes Programm oder das lokale `st-flash` den Adapter
benutzen kann. Es ist das höfliche Gegenstück zu *Trennen* und der richtige Schritt, bevor du die
Werkzeuge auf deinem eigenen Rechner benutzt.

Das Labor gibt das Board außerdem von selbst frei, wenn die Extension heruntergefahren wird. Mit
`cads.board.idleReleaseSeconds` kannst du es zusätzlich freigeben lassen, wenn das Fenster eine
Weile im Hintergrund war; standardmäßig ist das aus.

### Das Labor sagt, das Board sei nicht verbunden, obwohl es steckt

<figure>
<img src="{{ '/assets/19-shim-board-not-connected.png' | relative_url }}" alt="Integriertes Terminal: st-info --probe meldet Found 0 stlink programmers, st-flash write endet mit error: flash failed: board not connected; die Statusleiste zeigt Board: getrennt">
<figcaption>Die Shims, wenn das Board im Browser noch nicht verbunden ist. Sie drucken den Grund und den nächsten Schritt jetzt auf Deutsch und Englisch darunter.</figcaption>
</figure>

Verbinde das Board zuerst über die Statusleiste. Die Shims sprechen mit der Bridge, und die
Bridge spricht mit dem Browser; keiner von ihnen erreicht USB von sich aus.

### „Board-Bridge nicht aktiv – Board im Browser verbinden (CaDS Board Panel)“

Gedruckt von `st-flash` und `st-info`, wenn die HTTP-API der Bridge auf `127.0.0.1:3335` nicht
antwortet. Entweder ist das Board im Browser noch nicht verbunden, oder der Extension-Host
startet noch. Verbinde über die Statusleiste und starte den Task erneut.

### `st-flash erase` sagt „not permitted by CaDS lab policy“

Absicht. Ein Mass-Erase nähme das littlefs-Dateisystem in Flash-Bank 2 mit. `st-flash write`
löscht nur die Sektoren, die es schreibt. Siehe
[Sicherheitsregeln]({{ '/de/explanation/safety-rules/' | relative_url }}).

### `st-info --probe` zeigt `chipid 0x000`

Die ST-Link antwortet, der Kern aber nicht. Das ist der Zustand „verklemmte ST-Link“, verursacht
durch einen SWD-Client, der mitten in einer Übertragung aufgehört hat – ein Neuladen der Seite
während eines Flash, eine hart beendete Debug-Sitzung, oder schlicht ein geschlossener Tab, bei
dem überhaupt kein Aufräumen mehr läuft.

**Das Verbinden im Labor versucht das inzwischen selbst zu reparieren.** Es nimmt nie an, dass die
vorige Sitzung sauber endete: es betritt SWD neu, und wenn das Ziel dann immer noch nicht
antwortet, wiederholt es das mit gehaltener Reset-Leitung – genau das, was
`st-info --probe --connect-under-reset` auf der Kommandozeile macht. Zwei Versuche, dann hört es
auf, statt den Adapter weiter zu bearbeiten.

Siehst du danach immer noch *Der Debug-Adapter reagiert nicht mehr*, ist der Adapter auf
USB-Ebene aus dem Tritt, und nur ein Replug hilft: Kabel abziehen, wieder anstecken, unter macOS
`NOD_F429ZI` aushängen, neu verbinden. Siehe
[Wiederverbinden nach Replug]({{ '/de/how-to/reconnect-after-replug/' | relative_url }}).

Beide Fälle lassen sich von einem Terminal auf dem eigenen Rechner sicher unterscheiden: druckt
`st-info --probe` noch eine echte Version wie `V2J33S25`, hat die Reparatur in Software eine
Chance; steht dort nur noch ein nacktes `V2`, hilft ausschließlich der Replug.

### `st-info` auf meinem eigenen Rechner meldet „Found 0 stlink programmers“

Solange der Browser die ST-Link hält, kann kein anderes Programm auf deinem Rechner sie öffnen;
die lokalen stlink-Tools sehen nichts. Das ist exklusiver Zugriff, kein Fehler. Trenne das Board
im Labor (Statusleiste → *Trennen*), dann sehen die lokalen Tools es wieder.

### Kein `st-flash` auf dem eigenen Rechner, solange das Labor verbunden ist

Ein lokales `st-flash reset`, das genau in dem Moment lief, in dem der Browser das Gerät
freigab, hat während der Verifikation die ST-Link aufgehängt (`LIBUSB_ERROR_TIMEOUT`, danach
`chipid 0x000`). Nutze für Reset und Flash das Board-Menü des Labors; brauchst du die lokalen
Tools, trenne zuerst im Labor und warte eine Sekunde.

### Das Laufwerk `NOD_F429ZI` ist das Gefährlichste an diesem Board

Die ST-Link stellt ein MBED-Laufwerk namens `NOD_F429ZI` bereit. Dein Betriebssystem bindet es
bei jeder Enumeration ein und schreibt ungefragt Metadaten darauf – Spotlight-Index, `.fseventsd`,
`._`-Dateien. **Die ST-Link deutet Schreibzugriffe auf dieses Laufwerk als Firmware für
`0x08000000`.** Das hat hier schon einmal ein echtes Image beschädigt: ein einzelnes gekipptes Bit
im initialen SP-Wort der Vektortabelle, wodurch das Board mit wild leuchtenden LEDs im
Reset-Handler hing. Es ist außerdem einer der Wege, auf denen der Adapter mitten in einer Sitzung
aufhört zu antworten.

Ist es passiert, hilft **CaDS: Build + Flash** – ein schlichtes Neuschreiben repariert das Image.
Hör da aber nicht auf, denn nachträgliches Aushängen ist ein Wettlauf mit dem, was zuerst
geschrieben hat. Beseitige die Ursache, beste Möglichkeit zuerst:

1. **Eine Adapter-Firmware ohne Massenspeicher.** STs eigenes Upgrade-Werkzeug (STSW-LINK007)
   bietet eine Variante an, die Debug und den virtuellen COM-Port behält und das MBED-Laufwerk
   weglässt. Das beseitigt die Gefahr vollständig und ist die richtige Wahl für Labor-Boards. Wir
   haben dieses Upgrade auf dem Labor-Board **nicht** durchgeführt – prüfe die genauen Schritte
   deshalb vor dem Flashen gegen STs Dokumentation für deinen Adapter; ein fehlgeschlagenes
   Adapter-Firmware-Update ist schlimmer als das Problem, das es löst.
2. **Das automatische Einbinden abschalten.** Führe unter macOS einmal
   `scripts/setup-host-macos.sh` aus dem Bridge-Repository aus. Es trägt
   `LABEL=NOD_F429ZI none msdos rw,noauto` in `/etc/fstab` ein und nimmt das Volume von Spotlight
   aus, zeigt beide Änderungen vorher an, und `--undo` macht sie rückgängig. Es braucht einmalig
   Administratorrechte. Unter Linux installierst du `scripts/60-cads-stlink.rules`, das dasselbe
   tut und zusätzlich den USB-Zugriff erlaubt, den der Browser braucht.
3. **Jedes Mal aushängen.** Ohne Administratorrechte bleibt `diskutil unmountDisk /dev/diskN` nach
   jedem Einstecken **und nach jedem Reset** – ein Reset enumeriert den Adapter neu, das Laufwerk
   ist also sofort wieder da. Das ist die schwächste Variante, weil sie das Fenster erst schließt,
   wenn möglicherweise schon geschrieben wurde.

### Flashen scheitert mit einem Verify-Fehler

Versuche es einmal erneut, bevor du etwas anderes tust. Das cads-zero-Projekt hat beobachtet,
dass einzelne `st-flash write`-Aufrufe spät in langen Sitzungen an der Verifikation scheitern
und beim Wiederholen gelingen, bei gesunder ST-Link. Scheitert es weiter, neu einstecken und neu
verbinden.

### F5 lädt die Seite neu, statt den Debugger zu starten

Der Tastaturfokus lag außerhalb der Workbench (zum Beispiel in der Adressleiste des Browsers).
Klicke in den Editor und drücke F5 erneut, oder nutze den grünen Start-Button in *Run and Debug*.

### Der Debugger hält bei `main()`, obwohl die Firmware woanders war

`monitor reset halt` in der Launch-Konfiguration setzt das Target zurück; der erste Halt ist der
frühe Boot, nicht der vorherige Live-Zustand. Nutze die Konfiguration **Attach CaDS Zero (Board
im Browser, no flash)**, um eine laufende Firmware ohne Reset anzusehen.

### Ein getippter Konsolenbefehl tut nichts

Das Board ist im Touchscreen-App-Baum, der einfache Bytes absichtlich ignoriert. Sende einmal
das Quit-Byte: `scripts/board_key.py quit` (siehe
[Serielle Konsole]({{ '/de/tutorials/serial-console/' | relative_url }}#3-zum-prompt-kommen)).

## Builds und Tests

### Der Build stirbt mit Exit-Code 137

Dem Container ging der Speicher aus, und der Kernel hat den Compiler beendet. Auf einem
geteilten oder kleinen Host setzt der Betreiber `CMAKE_BUILD_PARALLEL_LEVEL=1` (oder `2`) am
Container; die Labor-Tasks erben es und bauen einfädig. clangd ist bereits auf vier
Indexierungs-Worker mit vorkompilierten Headern auf der Platte begrenzt. Melde das Symptom, statt
in einer Schleife zu wiederholen: jeder Versuch mit voller Parallelität wird genauso beendet.

### Die Golden-Image-Tests scheitern um wenige Pixel

Im Container erwartet: `golden_splash` und `golden_boot_desktop` weichen um +1 an
anti-aliasierten Kantenpixeln ab, weil Debians SDL2 die RGB565-Umrechnung anders rundet als das
SDL, mit dem die Goldens erzeugt wurden. Deshalb schließt **CaDS: Host tests** sie aus, und
**CaDS: Golden images (informativ)** führt sie getrennt mit einem Hinweis aus. Siehe
[Host-Tests]({{ '/de/how-to/host-tests/' | relative_url }}).

### `git status` zeigt nichts, obwohl der Container `.vscode/*.json` geschrieben hat

Beabsichtigt. Die vier `.vscode`-Dateien sind als `skip-worktree` markiert und `.clangd` ist
ausgeschlossen, sodass die Konfiguration des Containers nie als deine Änderung erscheint.

## Der Tutor

### „Frag den Tutor“ sagt, das Sprachmodell sei nicht konfiguriert

Das Deployment läuft ohne `TUTOR_LLM_BASE_URL` / `TUTOR_LLM_API_KEY` / `TUTOR_LLM_MODEL`. Alles
andere funktioniert: Datei-, Task- und Board-Checks laufen; Fragen-Aufgaben fallen auf manuelle
Bestätigung zurück; das Feld listet trotzdem die gefundenen Quellen.

### Der Tutor lehnt eine Frage ab

„Das liegt außerhalb des indizierten Referenzmaterials dieses Kurses“ heißt, dass die Suche
nichts oberhalb der BM25-Schwelle des Kurses gefunden hat. Sehr kurze Fragen erzielen niedrige
Werte. Nenne eine Datei, ein Register oder ein Symptom und frag erneut; der Tutor antwortet
absichtlich nur aus indiziertem Material.

### Ein HTTP 401 vom Sprachmodell

Einmal auf einer selbst gehosteten Kopie gesehen: die Endpunkt-URL benutzte `http://` statt
`https://`. Der Tutor verlangt eine `https`-Basis-URL; korrigiere die URL, bevor du den Key
anfasst.

### Board-Checks sagen „Nicht verfügbar“

Die Board-Bridge ist nicht installiert oder nicht verbunden. `board`-, `flash`- und
`serialExpect`-Checks melden *Nicht verfügbar* statt zu scheitern, damit sie keine Hinweis-Stufe
verbrauchen. Verbinde das Board und drücke erneut *Prüfen*.

## Immer noch festgefahren?

Eröffne ein Issue in
[CADS-DEMO-firmware-lab](https://github.com/scimbe/CADS-DEMO-firmware-lab/issues/new) mit dem,
was du getan und gesehen hast, und der Ausgabe von `st-info --probe`.
