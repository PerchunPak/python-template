# python-template

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/python-template/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/python-template/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/python-template/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/python-template)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.11 badge](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/)

My own template for any Python project.
Template can be used anywhere, this includes non-my projects.

## Installing

```bash
pip install cookiecutter jinja2-git lice
cookiecutter gh:PerchunPak/python-template
```

### If this doesn't work, try this:

```bash
git clone https://github.com/PerchunPak/python-template.git
cd python-template
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
```

### Run template

```bash
cookiecutter .
```

### If something is not clear

You can always write us!

## Updating

For updating, see `See what updated` diff in generated README.md file, in the end of it.

## Projects using it

[List of open-source projects on GitHub with our mention.](https://github.com/search?q=python-template&type=Code)
