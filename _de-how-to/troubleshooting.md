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

Beim ersten Start eines frischen Containers gesehen, wenige Sekunden nachdem die Workbench geladen
war. Schließe sie. Die Labor-Tasks rufen `cmake` selbst auf und brauchen die Konfiguration von
CMake Tools nicht; *Configure Now* schadet auch nicht, es führt nur das Preset `itsboard` ein
zweites Mal aus.

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
durch einen SWD-Client, der mitten in einer Übertragung beendet wurde (ein Neuladen der Seite
während eines Flash, eine hart beendete Debug-Sitzung). USB-Kabel ab- und wieder anstecken,
unter macOS `NOD_F429ZI` aushängen, neu verbinden. Siehe
[Wiederverbinden nach Replug]({{ '/de/how-to/reconnect-after-replug/' | relative_url }}).

### `st-info` auf meinem eigenen Rechner meldet „Found 0 stlink programmers“

Solange der Browser die ST-Link hält, kann kein anderes Programm auf deinem Rechner sie öffnen;
die lokalen stlink-Tools sehen nichts. Das ist exklusiver Zugriff, kein Fehler. Trenne das Board
im Labor (Statusleiste → *Trennen*), dann sehen die lokalen Tools es wieder.

### Kein `st-flash` auf dem eigenen Rechner, solange das Labor verbunden ist

Ein lokales `st-flash reset`, das genau in dem Moment lief, in dem der Browser das Gerät
freigab, hat während der Verifikation die ST-Link aufgehängt (`LIBUSB_ERROR_TIMEOUT`, danach
`chipid 0x000`). Nutze für Reset und Flash das Board-Menü des Labors; brauchst du die lokalen
Tools, trenne zuerst im Labor und warte eine Sekunde.

### Das Board zeigt nach einem Replug wild leuchtende LEDs (macOS)

macOS hat Metadaten auf das Massenspeicher-Laufwerk `NOD_F429ZI` geschrieben, und die ST-Link
hat sie als Firmware genommen. Mit **CaDS: Build + Flash** neu flashen; danach das Laufwerk nach
jedem Einstecken aushängen.

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
