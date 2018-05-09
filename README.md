# cookiecutter-udata-plugin

A cookiecutter template for a uData package (containing one or more plugin)

## Usage

```
pip install cookiecutter
cookiecutter gh:opendatateam/cookiecutter-udata-plugin
```

Provide the requested informations and then you can go in the newly created directory
(which will be the `project_slug` that you provided).


## Fields

These are the fields used by this cookiecutter template:

- **`project_name`**: The project name that will also serve as Backend display name (ex: `My Harvester`)
- **`project_slug`**: The project slug used as root folder name (ex: `udata-my-harvester`)
- **`pypackage`**: The project root package name (ex: `udata_my_harvester`)
- **`identifier`**: The backend entrypoint identifier (ex: `mine`)
- **`license`**: The license under which the project is published (ex: `AGPL`)
- **`author`**: The project author (ex: `OpenDataTeam`)
- **`email`**: The project contact email (ex: `contact@opendata.team`)
- **`description`**: The project short description (ex: `My awesome uData harvester`)
- **`version`**: The initial version (ex: `0.1.0.dev`)
- **`website`**: The project website (ex: `https://github.com/opendatateam/udata-my-harvester`)
- **`has_harvester`**`: Adds a harvester skeleton (see the [udata harvesting documention](https://udata.readthedocs.io/en/stable/harvesting/))
- **`has_theme`**: Adds a theme skeleton (see the [udata theming documention](https://udata.readthedocs.io/en/stable/creating-theme/))
- **`has_views`**: Adds a views skeleton
- **`has_metrics`**: Adds a metrics skeleton
- **`has_models`**: Adds a models skeleton
- **`has_linkchecker`**: Adds a linkchecker skeleton
- **`has_tasks`**: Adds a tasks skeleton
- **`has_preview`**`: Adds a preview plugin skeleton
- **`has_generic_plugin`**: Adds a generic plugin skeleton
