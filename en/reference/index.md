---
layout: default
title: Reference
lang: en
permalink: /en/reference/
---

# Reference

Look up a fact — a shortcut, a file, a command — without the narrative.

<div class="index-list">
{% assign items = site.en-reference | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
