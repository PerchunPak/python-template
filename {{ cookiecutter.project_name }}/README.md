# {{ cookiecutter.project_name }}

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})
[![Documentation Build Status](https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest)](https://{{ cookiecutter.project_name }}.readthedocs.io/)
{% if cookiecutter.other_languages_support == 'y' -%}
[![Supported languages](https://img.shields.io/badge/languages-en{% if cookiecutter.ukrainian_language_support == 'y' -%}%20%7C%20uk{% endif %}{% if cookiecutter.russian_language_support == 'y' -%}%20%7C%20ru{% endif %}-brightgreen)](https://{{ cookiecutter.project_name }}.readthedocs.io)
{% endif %}[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }})](https://www.python.org/downloads/)

{{ cookiecutter.project_description }}
{% if cookiecutter.other_languages_support == 'y' -%}
{% if cookiecutter.ukrainian_language_support == 'y' -%}
- [Документація українською](https://{{ cookiecutter.project_name }}.readthedocs.io/uk_UA/latest){% endif %}
{% if cookiecutter.russian_language_support == 'y' -%}
- [Документация на русском](https://{{ cookiecutter.project_name }}.readthedocs.io/ru/latest){% endif %}
{% endif %}
## Features

- Free! We don't want any money from you!
- Add yours!

## Installing

```bash
pip install {{ cookiecutter.project_name }}
```

## Installing for local developing

```bash
git clone https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
```

### Installing `poetry`

Next we need install `poetry` with [recomended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install --no-dev
```{% if cookiecutter.other_languages_support == 'y' -%}

### Compiling translations

This requered even if you want just use english.

```bash
poetry run pybabel compile -d locales
```{% endif %}

### Configuration

All configuration happends in `config.yml`, or with enviroment variables.

### If something is not clear

You can always write me!

## Example

```py
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.example import some_function

print(some_function(3, 4))
# => 7
```

## Updating

For updating, just re-download repository (do not forget save config),
if you used `git` for downloading, just run `git pull`.
{% if cookiecutter.other_languages_support == 'y' -%}
After that, you need update translations, commands the same as in installing section:

```bash
poetry run pybabel compile -d locales
```
{% endif %}
## Thanks

This project was generated with [fire-square-style](https://github.com/fire-square/fire-square-style).
Current template version: [{% gitcommit %}](https://github.com/fire-square/fire-square-style/tree/{% gitcommit %}).
See what [updated](https://github.com/fire-square/fire-square-style/compare/{% gitcommit %}...master).
