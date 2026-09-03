---
title: Fortschritt zurücksetzen
order: 7
description: Den Kurs wieder bei Step 1 beginnen, und was das Zurücksetzen behält
---

## Was wo gespeichert ist

| Daten | Ort | Vom Befehl zurückgesetzt |
|---|---|---|
| Aktueller Kurs und Step, Aufgabenstatus, deine Antworten | `<workspace>/.cads-tutor/session.json` | ja |
| Lernereignisse (bestandene und fehlgeschlagene Checks, gestellte Fragen) | `~/.cads-tutor/events.sqlite` (oder `events.json`, wo SQLite nicht verfügbar ist) | nein |
| Dialogprotokoll von „Frag den Tutor“ | `~/.cads-tutor/dialog.jsonl` | nein |
| Deine Änderungen an der Firmware | der Workspace `cads-zero` | nein |

Alles liegt im Workspace-Volume deines Containers. Ein Container-Neustart oder ein neues Image
behält es; nur der Betreiber kann das Volume löschen.

## Die Session zurücksetzen

**F1 → CaDS Tutor: Fortschritt zurücksetzen / Reset progress**. Eine Rückfrage lautet:

> Gesamten Tutor-Fortschritt in diesem Workspace zurücksetzen? Lernereignisse bleiben erhalten.

Bestätige mit *Zurücksetzen*. Der Baum sperrt jeden Step außer dem ersten, die Statusleiste
zeigt den ersten Step, und das Panel öffnet Step 1. Die Beherrschung in der Ansicht
*Fortschritt / Progress* bleibt, weil sie aus den Lernereignissen abgeleitet wird.

## Auch die Firmware zurücksetzen

Der Tutor rührt deinen Code nicht an. Willst du auch das Repository zurück in den geseedeten
Zustand bringen, führe im Terminal aus:

```bash
git status                      # see what you changed
git checkout -- .               # discard uncommitted edits
git clean -fd                   # remove new untracked files (keeps build/)
```

Der geseedete Checkout sitzt auf einem lokalen Branch `cads-lab` am gepinnten Commit;
`git log -1` zeigt ihn. Deine Änderungen an `.vscode/*.json` und `.clangd` werden ohnehin bei
jedem Container-Start überschrieben, lege persönliche Tasks also woanders ab.

Ein Zurücksetzen je Step gibt es nicht; der Befehl setzt immer die ganze Session zurück.
