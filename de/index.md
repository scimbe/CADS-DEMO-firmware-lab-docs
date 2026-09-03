---
layout: default
title: Firmware Lab
lang: de
permalink: /de/
---

# CaDS Firmware Lab — Dokumentation

<p class="tagline">Eine Browser-IDE für echte STM32-Firmware: ARM-Toolchain und Kurs-Tutor laufen in einem Container, das Board bleibt an deinem eigenen Rechner, und der Browser steuert die ST-Link für Flashen, Debuggen und die serielle Konsole. Nichts zu installieren.</p>

Du öffnest eine URL und bekommst VS Code mit der Firmware
[CaDS Zero](https://github.com/scimbe/cads-zero) für das ITSboard (STM32F429ZI), bereits geklont
und gebaut. Ein Tutor neben deinem Editor führt dich durch 41 Steps von „Board verbinden“ bis
„eine Design-Entscheidung verteidigen“, prüft deine Arbeit gegen Repository und Board und
beantwortet Fragen nur aus indiziertem Material.

## Ich bin Student

<div class="index-list">
  <a class="index-item" href="{{ '/de/tutorials/first-session/' | relative_url }}">
    <strong>1. Deine erste Sitzung →</strong>
    <span>Einloggen, orientieren, Step 1 erledigen (ohne Board)</span>
  </a>
  <a class="index-item" href="{{ '/de/how-to/connect-the-board/' | relative_url }}">
    <strong>2. Board anschließen →</strong>
    <span>Browser-Voraussetzungen und die Hinweise für macOS, Windows und Linux</span>
  </a>
  <a class="index-item" href="{{ '/de/tutorials/build-and-flash/' | relative_url }}">
    <strong>3. Bauen und flashen →</strong>
    <span>Task „CaDS: Build + Flash“, der Geräte-Dialog, der erste Selbsttest auf dem Board</span>
  </a>
  <a class="index-item" href="{{ '/de/tutorials/debug-with-f5/' | relative_url }}">
    <strong>4. Debuggen mit F5 →</strong>
    <span>Breakpoints, Stepping, Register und die Peripherie-Ansicht</span>
  </a>
  <a class="index-item" href="{{ '/de/how-to/troubleshooting/' | relative_url }}">
    <strong>Troubleshooting / FAQ →</strong>
    <span>Reale Befunde, jeweils mit Lösung</span>
  </a>
</div>

## Ich bin Kursautor

<div class="index-list">
  <a class="index-item" href="{{ '/de/how-to/write-a-course/' | relative_url }}">
    <strong>Eigenen Kurs schreiben →</strong>
    <span>Aufbau eines Kurs-Packs, Steps mit Front Matter, Laden und Validieren</span>
  </a>
  <a class="index-item" href="{{ '/de/reference/course-format/' | relative_url }}">
    <strong>Kursformat →</strong>
    <span>Jedes Feld, jeder Check-Typ, jeder sokratische Trigger</span>
  </a>
  <a class="index-item" href="{{ '/de/explanation/tutor-pedagogy/' | relative_url }}">
    <strong>Grounding, Bloom-Stufen, sokratische Hinweise →</strong>
    <span>Warum der Tutor fragt statt zu erklären</span>
  </a>
</div>

## Ich betreibe das Labor

<div class="index-list">
  <a class="index-item" href="{{ '/de/reference/environment-variables/' | relative_url }}">
    <strong>Umgebungsvariablen des Images →</strong>
    <span>PASSWORD, TUTOR_LLM_*, CMAKE_BUILD_PARALLEL_LEVEL und was das Image selbst setzt</span>
  </a>
  <a class="index-item" href="{{ '/de/explanation/board-in-the-browser/' | relative_url }}">
    <strong>Warum das Board am Browser hängt →</strong>
    <span>Web-Worker-Extension-Host, GDB-Server in der Bridge, kein USB im Container</span>
  </a>
  <a class="index-item" href="https://github.com/scimbe/CADS-DEMO-firmware-lab">
    <strong>Entwicklerdokumentation →</strong>
    <span>Image, Extensions, Kurse, Multi-User-Stack: README und docs/ des Monorepos</span>
  </a>
</div>

## Wie diese Seite aufgebaut ist

- **Tutorials** — der Reihe nach lernen, durch Tun.
- **Anleitungen (How-to)** — eine konkrete Aufgabe, die du schon lösen willst.
- **Referenz** — einen Fakt nachschlagen, ohne Erzählung.
- **Hintergrund (Explanation)** — verstehen, warum das Labor so gebaut ist.

Das ist das [Diátaxis](https://diataxis.fr)-Framework. Jede Seite gibt es auf Deutsch und
Englisch; der Umschalter in der Kopfzeile wechselt.

## Woher die Screenshots stammen

Jeder Screenshot wurde mit Headless-Chromium gegen einen Container aus dem produktiven Image
(`ghcr.io/scimbe/cads-firmware-lab:next-8a20ec9`) aufgenommen. Seiten zu den Board-Pfaden
sagen es, wo ein Screenshot mit echter Hardware noch folgt.
