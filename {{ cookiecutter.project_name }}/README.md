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

## Пример

```py
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.example import some_function

print(some_function(3, 4))
# => 7
```

## Спасибо

Этот проект был сгенерирован с помощью [`autodonate-plugin-template`](https://github.com/fire-squad/autodonate-plugin-template).
Текущая версия примера: [{% gitcommit %}](https://github.com/fire-squad/autodonate-plugin-template/tree/{% gitcommit %}).
Смотрите что [обновилось](https://github.com/fire-squad/autodonate-plugin-template/compare/{% gitcommit %}...master) с того времени.
