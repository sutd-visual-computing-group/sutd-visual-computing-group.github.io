---
title: "Visual Computing Group @SUTD - Teaching"
layout: textlay
excerpt: "Visual Computing Group @ SUTD"
sitemap: false
permalink: /teaching
---

# Teaching

{% for publi in site.data.teaching %}
<div class="row">
<div class="col-sm-12 clearfix">
 <div class="well">
  <pubtit>{{ publi.name }}</pubtit>
  <p>{{ publi.description }}</p>
  <p><strong><a href="{{ publi.link. }}">> More Details</a></strong></p>
 </div>
</div>
</div>
{% endfor %}

  