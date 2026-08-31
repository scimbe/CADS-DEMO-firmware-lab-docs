---
layout: default
title: Anleitungen
lang: de
permalink: /de/how-to/
---

# Anleitungen

Eine konkrete Aufgabe, die du schon lösen willst.

<div class="index-list">
{% assign items = site.de-how-to | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
