---
title: Tastenkürzel im Browser
order: 5
description: Welche VS-Code-Tastenkürzel in einem Browser-Tab bei der Workbench ankommen, und die sicheren Alternativen
---

code-server ist VS Code in einem Browser-Tab. Der Browser sieht jeden Tastendruck zuerst, und
einige Kürzel gehören ihm. Die Tabelle listet, was im Labor zählt.

| Aktion | Desktop-Kürzel | Im Browser |
|---|---|---|
| Befehlspalette | Ctrl+Shift+P / ⇧⌘P | **F1** funktioniert immer. Ctrl+Shift+P kann der Browser abfangen. |
| Datei schnell öffnen | Ctrl+P / ⌘P | Ctrl+P ist in manchen Browsern *Drucken*; nutze F1 und tippe den Dateinamen ohne `>`. |
| Debuggen starten | F5 | Funktioniert, wenn die Workbench den Fokus hat; mit Fokus in der Adressleiste lädt die Seite neu. Alternative: der grüne Start-Button in *Run and Debug*. |
| Continue / Step Over / Step Into / Step Out | F5 / F10 / F11 / Shift+F11 | Gleiche Regel wie bei F5. F11 schaltet in manchen Browsern auf Vollbild, wenn die Workbench keinen Fokus hat. |
| Build-Task ausführen | Ctrl+Shift+B / ⇧⌘B | Funktioniert. |
| Terminal ein-/ausblenden | Ctrl+` / ⌃` | Funktioniert. |
| Seitenleiste ein-/ausblenden | Ctrl+B / ⌘B | Funktioniert. |
| Tab schließen | Ctrl+W / ⌘W | **Schließt in den meisten Browsern den Browser-Tab.** Nutze das × am Editor-Tab oder F1 → *View: Close Editor*. |
| Neues Fenster | Ctrl+Shift+N | Browser-Fenster, nicht VS Code. |
| Speichern | Ctrl+S / ⌘S | Funktioniert; der Speichern-Dialog des Browsers erscheint nur, wenn der Fokus außerhalb der Workbench liegt. |
| In Dateien suchen | Ctrl+Shift+F / ⇧⌘F | Funktioniert. |
| Zoom | Ctrl+= / Ctrl+- | Zoomt die ganze Seite; nutze *View: Zoom In* nur für die Workbench. |

Die Labor-Kommandos haben kein Standard-Tastenkürzel; öffne sie mit F1:

- `CaDS Board: Verbinden`, `Flash`, `Reset`, `Anhalten`, `Konsole öffnen`, `Menü`
- `CaDS Tutor: Tutor öffnen / Open Tutor`, `Checks … ausführen / Run checks`,
  `Frag den Tutor / Ask the tutor`, `Sprache wählen / Set language`,
  `Fortschritt zurücksetzen / Reset progress`, `Nächster Step / Next step`

<figure>
<img src="{{ '/assets/07-command-palette.png' | relative_url }}" alt="Mit F1 geöffnete Befehlspalette, gefiltert auf CaDS, mit den Kommandos des CaDS Tutors">
<figcaption>F1, dann „CaDS“ tippen, listet jedes Labor-Kommando.</figcaption>
</figure>

Das Board-Konsolen-Terminal ist ein Pseudo-Terminal der Extension: Ctrl+] beendet es nicht,
schließe stattdessen das Terminal.
