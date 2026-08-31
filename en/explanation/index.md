---
layout: default
title: Explanation
lang: en
permalink: /en/explanation/
---

# Explanation

Understand *why* the system is built the way it is.

<div class="index-list">
{% assign items = site.en-explanation | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
