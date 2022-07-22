API Reference
=============

This page contains auto-generated API reference documentation.

{% if cookiecutter.other_languages_support == 'y' -%}
.. warning::
    Currently, API Reference is only available `in English <https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/>`_\ .
{% endif %}.. toctree::
   :titlesonly:
{% raw %}
   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}{% endraw %}
