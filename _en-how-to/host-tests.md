---
title: Run the host tests in the container
order: 3
description: Build the simulator preset and run the unit tests with ctest, and why the two golden-image tests are a separate task
---

CaDS Zero builds for two targets from one tree: `itsboard` (the firmware) and `host` (the SDL2
simulator plus the unit and golden-image tests). Everything above the HAL must build for both.
The container carries a native compiler and SDL2, so the host tests run there, headless.

## Run

**F1 → Tasks: Run Task → CaDS: Host tests** (it is also the default test task). It runs:

```bash
cmake --preset host && cmake --build build/host && \
  ctest --test-dir build/host --output-on-failure -E '^golden_'
```

with `SDL_VIDEODRIVER=dummy` and `SDL_AUDIODRIVER=dummy` set, so no display is needed. The first
run configures and compiles the host tree (a few minutes on a small host); later runs only
rebuild what changed. The suite passes completely on the seeded commit.

From the terminal the same command works verbatim.

## Golden images

Two tests, `golden_splash` and `golden_boot_desktop`, compare rendered frames pixel by pixel
against `targets/sim/golden/*.png`. In the container they differ by +1 on anti-aliased edge
pixels, because Debian's SDL2 rounds the RGB565→24-bit conversion differently from the SDL the
goldens were generated with. The cads-zero project root-caused this in its ROADMAP on
2026-09-01; it is not a bug in your code.

That is why the default task excludes them (`-E '^golden_'`) and a separate task
**CaDS: Golden images (informativ)** runs exactly these two with an explanatory note at the end.
Run it when you work on the display code and want to see the diff, and expect it to report the
rounding difference.

## Only one test

```bash
ctest --test-dir build/host -R canvas --output-on-failure
```

`ctest -N --test-dir build/host` lists the test names.

## Memory on small hosts

A host build compiles with as many jobs as the container has CPUs. On a shared or small host the
operator can cap this with the environment variable `CMAKE_BUILD_PARALLEL_LEVEL` on the
container; the tasks inherit it. If a build is killed with exit code 137, that is the
out-of-memory killer, not a compiler error; see
[Troubleshooting]({{ '/en/how-to/troubleshooting/' | relative_url }}#the-build-dies-with-exit-code-137).
