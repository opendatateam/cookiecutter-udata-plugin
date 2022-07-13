'''
{{ cookiecutter.project_name }}

{{ cookiecutter.description }}
'''

import os

tag = os.environ.get('CIRCLE_TAG')
build_num = os.environ.get('CIRCLE_BUILD_NUM')

__version__ = '{{ cookiecutter.version }}' + (str(build_num) if not tag and build_num else '0')
__description__ = '{{ cookiecutter.description }}'
{% if cookiecutter.has_generic_plugin == 'yes' %}


def init_app(app):
    # Do whatever you want to initialize your plugin
    pass
{% endif %}
