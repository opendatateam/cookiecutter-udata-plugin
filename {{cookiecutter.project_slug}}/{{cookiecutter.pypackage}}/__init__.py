'''
{{ cookiecutter.project_name }}

{{ cookiecutter.description }}
'''

__version__ = '{{ cookiecutter.version }}'
__description__ = '{{ cookiecutter.description }}'
{% if cookiecutter.has_generic_plugin == 'yes' %}


def init_app(app):
    # Do whatever you want to initialize your plugin
    pass
{% endif %}
