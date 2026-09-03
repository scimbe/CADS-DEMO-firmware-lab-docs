---
title: Host-Tests im Container ausführen
order: 3
description: Das Simulator-Preset bauen und die Unit-Tests mit ctest laufen lassen, und warum die zwei Golden-Image-Tests ein eigener Task sind
---

CaDS Zero baut aus einem Quellbaum für zwei Targets: `itsboard` (die Firmware) und `host` (den
SDL2-Simulator plus die Unit- und Golden-Image-Tests). Alles oberhalb der HAL muss für beide
bauen. Der Container trägt einen nativen Compiler und SDL2, die Host-Tests laufen dort also,
headless.

## Ausführen

**F1 → Tasks: Run Task → CaDS: Host tests** (zugleich der Standard-Test-Task). Er führt aus:

```bash
cmake --preset host && cmake --build build/host && \
  ctest --test-dir build/host --output-on-failure -E '^golden_'
```

mit gesetztem `SDL_VIDEODRIVER=dummy` und `SDL_AUDIODRIVER=dummy`, es wird also kein Display
gebraucht. Der erste Lauf konfiguriert und kompiliert den Host-Baum (einige Minuten auf einem
kleinen Host); spätere Läufe bauen nur neu, was sich geändert hat. Die Suite besteht auf dem
geseedeten Commit vollständig.

Im Terminal funktioniert derselbe Befehl wörtlich.

## Golden Images

Zwei Tests, `golden_splash` und `golden_boot_desktop`, vergleichen gerenderte Frames Pixel für
Pixel mit `targets/sim/golden/*.png`. Im Container weichen sie um +1 an anti-aliasierten
Kantenpixeln ab, weil Debians SDL2 die RGB565→24-Bit-Umrechnung anders rundet als das SDL, mit
dem die Goldens erzeugt wurden. Das cads-zero-Projekt hat das am 2026-09-01 in seiner ROADMAP
auf die Ursache zurückgeführt; es ist kein Fehler in deinem Code.

Deshalb schließt der Standard-Task sie aus (`-E '^golden_'`), und ein eigener Task
**CaDS: Golden images (informativ)** führt genau diese zwei mit einem erklärenden Hinweis am Ende
aus. Starte ihn, wenn du am Display-Code arbeitest und den Diff sehen willst, und erwarte, dass
er den Rundungsunterschied meldet.

## Nur ein Test

```bash
ctest --test-dir build/host -R canvas --output-on-failure
```

`ctest -N --test-dir build/host` listet die Testnamen.

## Speicher auf kleinen Hosts

Ein Host-Build kompiliert mit so vielen Jobs, wie der Container CPUs hat. Auf einem geteilten
oder kleinen Host kann der Betreiber das mit der Umgebungsvariablen `CMAKE_BUILD_PARALLEL_LEVEL`
am Container begrenzen; die Tasks erben sie. Wird ein Build mit Exit-Code 137 beendet, ist das
der Out-of-Memory-Killer, kein Compilerfehler; siehe
[Troubleshooting]({{ '/de/how-to/troubleshooting/' | relative_url }}#der-build-stirbt-mit-exit-code-137).
