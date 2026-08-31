---
layout: default
title: How-to guides
lang: en
permalink: /en/how-to/
---

# How-to guides

A specific task you already know you want to do.

<div class="index-list">
{% assign items = site.en-how-to | sort: "order" %}
{% for p in items %}
  <a class="index-item" href="{{ p.url | relative_url }}">
    <strong>{{ p.title }} →</strong>
    <span>{{ p.description }}</span>
  </a>
{% endfor %}
</div>
