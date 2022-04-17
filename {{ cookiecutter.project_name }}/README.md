# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})
[![Documentation Build Status](https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest)](https://{{ cookiecutter.project_name }}.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }})](https://www.python.org/downloads/)

{{ cookiecutter.project_description }}

## Особенности

- Бесплатно! Мы не попросим ни копейки за использование!
- Добавьте свое!


## Установка

```bash
pip install {{ cookiecutter.project_name }}
```

## Установка для локальной разработки

```bash
git clone https://https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
```

Затем установите `poetry` [рекомендованым путем](https://python-poetry.org/docs/master/#installation).

Если вы на платформе Linux, используйте команду:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Если вы на Windows, откройте PowerShell от имени администратора и используйте:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Внимание: На момент написания текста (03.3.2022), существует баг, который вызывает предупреждение при использовании любой команды. 
Если вы с таким столкнулись, можете установить poetry другим путем:

```bash
pip install poetry
```

Но учитывайте что это не рекомендованый путь, вы возможно не сможете использовать некоторые функции (например `poetry self update`).

И наконец установим зависимости:

```bash
poetry install
```

## Пример

```py
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.example import some_function

print(some_function(3, 4))
# => 7
```

## Спасибо

Этот проект был сгенерирован с помощью [`fire-square-style`](https://github.com/fire-square/fire-square-style).
Текущая версия примера: [{% gitcommit %}](https://github.com/fire-square/fire-square-style/tree/{% gitcommit %}).
Смотрите что [обновилось](https://github.com/fire-square/fire-square-style/compare/{% gitcommit %}...master) с того времени.
