# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Usage

Install the plugin package in you udata environment:

```bash
pip install {{ cookiecutter.project_slug }}
```

Then activate it in your `udata.cfg`:

```python
PLUGINS = ['{{cookiecutter.identifier}}']
```
