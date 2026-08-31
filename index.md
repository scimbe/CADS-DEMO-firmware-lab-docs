---
layout: default
title: Firmware Lab Docs
lang: en
---

<h1>Firmware Lab — Docs</h1>
<p class="tagline">Learn real STM32 firmware with an AI tutor that walks you through it one register at a time — nothing to install, just a browser.</p>

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
