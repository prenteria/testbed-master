
{% block content %}
<h1>Username: {{ email }} :</h1>
<p>Password:
{{ password }}
</p>
<a href="{{ url_for('home') }}"> Go home</a>
{% endblock %}