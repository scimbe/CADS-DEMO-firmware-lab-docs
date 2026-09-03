---
layout: default
title: Firmware Lab Docs
lang: en
---

<h1>CaDS Firmware Lab — Docs</h1>
<p class="tagline">Real STM32 firmware in a browser IDE: the toolchain and the course tutor run in a container, the board stays on your desk, the browser drives the ST-Link. Nothing to install.</p>

<p>Choose a language / Sprache wählen:</p>

<div class="index-list">
  <a class="index-item" href="{{ '/en/' | relative_url }}">
    <strong>English →</strong>
    <span>Start the docs in English</span>
  </a>
  <a class="index-item" href="{{ '/de/' | relative_url }}">
    <strong>Deutsch →</strong>
    <span>Dokumentation auf Deutsch starten</span>
  </a>
</div>
<script>
// Best-effort redirect straight to the browser's preferred language on first load;
// the manual links above always work regardless (no-JS, wrong guess, etc.).
(function () {
  var prefers = (navigator.language || navigator.userLanguage || "en").toLowerCase();
  var target = prefers.indexOf("de") === 0 ? "{{ '/de/' | relative_url }}" : "{{ '/en/' | relative_url }}";
  if (!window.location.search.includes("nolang")) {
    window.location.replace(target);
  }
})();
</script>
