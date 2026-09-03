---
title: Sicherheitsregeln
order: 4
description: Kein Mass-Erase, ein festes Flash-Fenster, Anhalten vor dem Flashen, nie Option-Bytes, und warum es jede Regel gibt
---

Das Board gehört dem Studierenden, der Flash trägt ein Dateisystem, und das ST-Link-Protokoll
ist leicht zu zerstören. Das Labor setzt cads-zeros `docs/SAFETY.md` deshalb auf drei Ebenen
durch: in den Shims, in der Bridge und im Probe-Treiber. Ein Studierender kann keine davon
abschalten.

## Kein Mass-Erase, niemals

`st-flash erase` verweigert das Shim mit *erase is not permitted by CaDS lab policy*. Der
GDB-Server implementiert kein Monitor-Kommando für Mass-Erase, und der Probe-Treiber enthält
überhaupt keine Mass-Erase-Operation. Grund: Ein Chip-Erase nähme das littlefs-Volume in
Flash-Bank 2 mit und könnte auf einem dafür konfigurierten Board Option-Bytes berühren.
`st-flash write` löscht nur die Sektoren, die es schreibt; ein typisches Image berührt die
ersten Sektoren von Bank 1 und sonst nichts.

## Ein festes Flash-Fenster

Schreibvorgänge werden nur innerhalb von **`0x08000000–0x080FFFFF`** angenommen, dem ersten
Megabyte. Das Shim prüft Adresse und Größe, die Bridge prüft unabhängig noch einmal, und das
Linker-Skript von cads-zero weigert sich, irgendetwas in `FLASH_FS` (ab `0x08120000`) zu legen.
Ein Image, das über das Fenster hinausgewachsen ist, scheitert beim Linken, nicht auf dem Board.

## Anhalten statt zurücksetzen vor dem Flashen

Die Firmware aktiviert den unabhängigen Watchdog (IWDG). Der übliche ST-Link-Ablauf setzt den
Core vor dem Programmieren zurück, was auf diesem Board den Watchdog mitten in der Sequenz
auslösen lässt. Der Probe-Treiber trägt den hardware-verifizierten CaDS-Fix: Er **hält** den
Core an, programmiert, verifiziert und setzt danach zurück. Das ist der Grund, warum das Labor
einen eigenen Treiber portiert, statt einen unveränderten zu nutzen.

## Option-Bytes werden nie geschrieben

Read-Protection ist entweder lästig oder dauerhaft. Keine Ebene des Labors hat einen Codepfad,
der Option-Bytes schreibt.

## Ein Client an der Probe, serialisierte Operationen

Die Protokoll-Zustandsmaschine der ST-Link desynchronisiert, wenn ein Client mitten im Transfer
abgeschossen wird; jedes spätere Kommando läuft dann bis zum physischen Neu-Einstecken in ein
Timeout. Die Probe serialisiert jede Operation hinter einem Mutex und setzt auf jede
USB-Transaktion ein Timeout, die Bridge serialisiert alle Probe-Aufrufe, und nur eine
GDB-Sitzung darf angehängt sein. Eine Debug-Sitzung, die sauber endet, lässt das Target
weiterlaufen; ein Neuladen der Seite mitten im Flash ist das eine, wovor das Labor nicht
schützen kann, und deshalb gibt es die Seite *Wiederverbinden nach Replug*.

## macOS und das Laufwerk `NOD_F429ZI`

Keine Labor-Ebene, aber eine dokumentierte Gefahr: macOS mountet das Massenspeicher-Laufwerk
des Nucleo bei jedem Einstecken und schreibt ungefragt Metadaten darauf; die ST-Link behandelt
solche Schreibvorgänge als Firmware für `0x08000000`. Das cads-zero-Projekt hat daraus eine
echte Beschädigung des Initial-Stackpointer-Worts protokolliert. Wirf das Laufwerk nach jedem
Neu-Einstecken aus.
