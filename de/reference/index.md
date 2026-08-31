---
layout: default
title: Referenz
lang: de
permalink: /de/reference/
---

# Referenz

Einen Fakt nachschlagen — Tastenkürzel, Datei, Befehl — ohne Drumherum.

<div class="index-list">
{% assign items = site.de-reference | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
