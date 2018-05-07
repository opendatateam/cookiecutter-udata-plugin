#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

TO_REMOVE = [
    {% if cookiecutter.has_harvester == 'no' %}'harvesters.py',{% endif %}
    {% if cookiecutter.has_theme == 'no' %}'theme',{% endif %}
    {% if cookiecutter.has_views == 'no' %}'views.py',{% endif %}
    {% if cookiecutter.has_metrics == 'no' %}'metrics.py',{% endif %}
    {% if cookiecutter.has_models == 'no' %}'models.py',{% endif %}
    {% if cookiecutter.has_linkchecker == 'no' %}'linkchecker.py',{% endif %}
    {% if cookiecutter.has_tasks == 'no' %}'tasks.py',{% endif %}
    {% if cookiecutter.has_preview == 'no' %}'preview.py',{% endif %}
]


if __name__ == '__main__':

    # Remove unnecessary files
    for name in TO_REMOVE:
        path = os.path.join(PROJECT_DIRECTORY,
                            # '{{ cookiecutter.project_slug }}',
                            '{{ cookiecutter.pypackage }}',
                            name)
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)
