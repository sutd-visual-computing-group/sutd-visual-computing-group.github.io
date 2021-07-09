---
title: "Visual Computing Group @ SUTD - Team"
layout: gridlay
excerpt: "Visual Computing Group @ SUTD: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **22 June 2021: We currently have Postdoc and Research Assistant positions** [(see openings)](https://sites.google.com/site/mancheung0407/researcher-position-available)


Jump to [Principal Investigator](#principal-investigator), [Researchers](#researchers), [Graduate and Masters Students](#graduate-and-masters-students), [Undergraduate Students](#undergraduate-students), [Alumni](#alumni), [Former Visitors and Students](#former-visitors-and-students)
## Principal Investigator
{% assign number_printed = 0 %}
{% for member in site.data.pi %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: left"  />
  <h4>{{ member.name }}</h4>
  <h5>{{ member.info }}</h5>
  
  <div style="overflow: auto">
  <a class="btn btn-primary " href="mailto:{{ member.email }}" target="_blank" ><i class="glyphicon glyphicon-envelope"></i></a>
  <a class="btn btn-primary" href="{{ member.website }}" target="_blank"><i class="glyphicon glyphicon-home"></i></a>
  <a class="btn btn-primary" href="{{ member.google_scholar_link }}" target="_blank" ><i class="fab fa-google"></i></a>
  </div>

  <!-- {% if member.number_educ == 1 %} -->
  <!-- {{ member.education1 }} -->
  <!-- {% endif %} -->
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}




## Researchers
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="35%" height="35%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <h5>{{ member.info }}</h5>
  <div style="overflow: auto">
  <a class="btn btn-primary" href="mailto:{{ member.email }}" target="_blank"><i class="glyphicon glyphicon-envelope"></i></a>
  <a class="btn btn-primary" href="{{ member.website }}" target="_blank"><i class="glyphicon glyphicon-home"></i></a>
  <a class="btn btn-primary" href="{{ member.google_scholar_link }}" target="_blank" ><i class="fab fa-google"></i></a>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}



## Graduate and Masters Students

{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="35%" height="35%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <h5>{{ member.info }}</h5>
  <div style="overflow: auto">
  <a class="btn btn-primary" href="mailto:{{ member.email }}" target="_blank"><i class="glyphicon glyphicon-envelope"></i></a>
  <a class="btn btn-primary" href="{{ member.website }}" target="_blank"><i class="glyphicon glyphicon-home"></i></a>
  <a class="btn btn-primary" href="{{ member.google_scholar_link }}" target="_blank" ><i class="fab fa-google"></i></a>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Undergraduate Students

{% assign number_printed = 0 %}
{% for member in site.data.ug_students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="35%" height="35%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <h5>{{ member.info }}</h5>
  <div style="overflow: auto">
  <a class="btn btn-primary" href="mailto:{{ member.email }}" target="_blank"><i class="glyphicon glyphicon-envelope"></i></a>
  <a class="btn btn-primary" href="{{ member.website }}" target="_blank"><i class="glyphicon glyphicon-home"></i></a>
  <a class="btn btn-primary" href="{{ member.google_scholar_link }}" target="_blank" ><i class="fab fa-google"></i></a>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="35%" height="35%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <h5>{{ member.info }}<br>
  {{ member.current }}</h5>
  <div style="overflow: auto">
  <a class="btn btn-primary" href="mailto:{{ member.email }}" target="_blank"><i class="glyphicon glyphicon-envelope"></i></a>
  <a class="btn btn-primary" href="{{ member.website }}" target="_blank"><i class="glyphicon glyphicon-home"></i></a>
  <a class="btn btn-primary" href="{{ member.google_scholar_link }}" target="_blank" ><i class="fab fa-google"></i></a>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}



## Former Visitors and Students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Graduate and Masters students</h4>
{% for member in site.data.alumni_graduate_and_masters %}
{{ member.name }}<br>
{{ member.current }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Undergraduate Students</h4>
{% for member in site.data.alumni_ug %}
{{ member.name }}
{% endfor %}
</div>

</div>
