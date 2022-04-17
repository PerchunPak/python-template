# fire-square-style

[![Build Status](https://github.com/fire-square/fire-square-style/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/fire-square/fire-square-style/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/fire-square/fire-square-style/branch/master/graph/badge.svg)](https://codecov.io/gh/fire-square/fire-square-style)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.10 badge](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)

Пример стиля кода для всех Python проектов организации [Fire Square](https://github.com/fire-square).
Пример можно использовать где угодно, теперь он не зависит от определенных проектов.

## Установка

```bash
pip install cookiecutter jinja2-git lice
cookiecutter gh:fire-square/fire-square-style
```

### Если по какой то причине, это не работает, используйте:

```bash
git clone https://fire-square/fire-square-style.git
cd fire-square-style
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

И наконец установим зависимости, а затем запустим темплейт:

```bash
poetry install
cookiecutter .
```

## Проекты использующие это

[Список open-source проектов на GitHub с нашим упоминанием.](https://github.com/search?q=fire-square-style&type=Code)
