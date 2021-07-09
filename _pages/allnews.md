---
title: "Visual Computing Group @ SUTD - News"
layout: textlay
excerpt: "Visual Computing Group @ SUTD"
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
