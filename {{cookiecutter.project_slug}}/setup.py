#!/usr/bin/env python

import os
import io
import re

from setuptools import setup, find_packages

RE_BADGE = re.compile(r'^\[\!\[(?P<text>.*?)\]\[(?P<badge>.*?)\]\]\[(?P<target>.*?)\]$', re.M)

BADGES_TO_KEEP = []


def md(filename):
    '''
    Load .md (markdown) file and sanitize it for PyPI.
    '''
    content = io.open(filename).read()

    for match in RE_BADGE.finditer(content):
        if match.group('badge') not in BADGES_TO_KEEP:
            content = content.replace(match.group(0), '')

    return content


def pip(filename):
    """Parse pip reqs file and transform it to setuptools requirements."""
    return open(os.path.join('requirements', filename)).readlines()


long_description = '\n'.join((
    md('README.md'),
    md('CHANGELOG.md'),
    ''
))

install_requires = pip('install.pip')
tests_require = pip('test.pip')


setup(
    name='{{cookiecutter.project_slug}}',
    version=__import__('{{cookiecutter.pypackage}}').__version__,
    description=__import__('{{cookiecutter.pypackage}}').__description__,
    long_description=long_description,
    url='{{cookiecutter.website}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        {% if cookiecutter.has_harvester == 'yes' -%}
        'udata.harvesters': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.harvesters:{{ cookiecutter.identifier.title().replace('-', '') }}Backend',
        ],
        {%- endif %}
        {% if cookiecutter.has_theme == 'yes' -%}
        'udata.theme': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.theme',
        ],
        {%- endif %}
        {% if cookiecutter.has_views == 'yes' -%}
        'udata.views': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.views',
        ],
        {%- endif %}
        {% if cookiecutter.has_metrics == 'yes' -%}
        'udata.metrics': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.metrics',
        ],
        {%- endif %}
        {% if cookiecutter.has_models == 'yes' -%}
        'udata.models': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.models',
        ],
        {%- endif %}
        {% if cookiecutter.has_linkchecker == 'yes' -%}
        'udata.linkcheckers': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.linkchecker:{{ cookiecutter.identifier.title().replace('-', '') }}LinkChecker',
        ],
        {%- endif %}
        {% if cookiecutter.has_tasks == 'yes' -%}
        'udata.tasks': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.tasks',
        ],
        {%- endif %}
        {% if cookiecutter.has_preview == 'yes' -%}
        'udata.preview': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}.preview:{{ cookiecutter.identifier.title().replace('-', '') }}Preview',
        ],
        {%- endif %}
        {% if cookiecutter.has_generic_plugin == 'yes' -%}
        'udata.plugins': [
            '{{cookiecutter.identifier}} = {{cookiecutter.pypackage}}',
        ],
        {%- endif %}
    },
    license='{{ cookiecutter.license }}',
    zip_safe=False,
    keywords='udata, {{cookiecutter.project_name}}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
