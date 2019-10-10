{% extends "base.ahk" %}
{% block body %}
WinSet, {{subcommand}}, {{value}}, ahk_id {{ win.id }}
{% endblock body %}
