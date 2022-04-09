# autodonate-plugin-template

[![Build Status](https://github.com/fire-squad/autodonate-plugin-template/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-squad/autodonate/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-squad/autodonate-plugin-template/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-squad/autodonate)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.10 badge](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)

Cookiecutter template для плагина [сайта autodonate](https://github.com/fire-squad/autodonate). 
Пожалуйста, используйте этот стиль.

## Установка

```bash
pip install cookiecutter jinja2-git lice
cookiecutter gh:fire-squad/autodonate-plugin-template
```

### Если по какой то причине, это не работает, используйте:

```bash
git clone https://fire-squad/autodonate-plugin-template.git
cd autodonate-plugin-template
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

Внимание: На момент написания текста (03.3.2022), существует баг, который вызывает предупреждение при использовании любой команды. Если вы с таким столкнулись, можете установить poetry другим путем:

```bash
pip install poetry
```

Но учитывайте что это не рекомендованый путь, вы возможно не сможете использовать некоторые функции (например `poetry self update`).

И наконец установим зависимости, а затем запустим темплейт:

```bash
poetry install
cookiecutter .
```

## Проекты использующие это

[Список open-source проектов на GitHub с нашим упоминанием.](https://github.com/search?q=autodonate-plugin-template&type=Code)
