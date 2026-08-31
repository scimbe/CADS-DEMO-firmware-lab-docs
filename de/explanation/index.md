---
layout: default
title: Hintergrund
lang: de
permalink: /de/explanation/
---

# Hintergrund

Verstehen, *warum* das System so gebaut ist, wie es ist.

<div class="index-list">
{% assign items = site.de-explanation | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
