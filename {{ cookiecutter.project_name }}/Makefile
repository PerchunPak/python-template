SHELL:=/usr/bin/env bash

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run pycln .
	poetry run mypy --install-types --non-interactive .
	poetry run flake8 .
	poetry run doc8 -q docs

.PHONY: unit
unit:
ifeq ($(ci),1)
	poetry run pytest --no-testmon
else
	poetry run pytest --no-cov
endif

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

{% if cookiecutter.other_languages_support == 'y' -%}
.PHONY: translate
translate:
	poetry run pybabel extract -o ./locales/base.pot ./{{cookiecutter.project_name.lower().replace('-', '_')}}
	poetry run pybabel update -d ./locales -i ./locales/base.pot
	poetry run pybabel compile -d ./locales

{% endif %}.PHONY: test
test: style package unit
