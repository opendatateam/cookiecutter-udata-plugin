# -*- coding: utf-8 -*-
'''
{{ cookiecutter.project_name }}

{{ cookiecutter.description }}
'''
from __future__ import unicode_literals

__version__ = '{{ cookiecutter.version }}'
__description__ = '{{ cookiecutter.description }}'
{% if cookiecutter.has_generic_plugin == 'yes' %}


def init_app(app):
    # Do whatever you want to initialize your plugin
    pass
{% endif %}
