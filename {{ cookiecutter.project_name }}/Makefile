SHELL:=/usr/bin/env bash

.PHONY: format
format:
	black .
	isort .
	pycln .

.PHONY: lint
lint:
	mypy .

.PHONY: style
style: format lint

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	pip check

{% if cookiecutter.other_languages_support == 'y' -%}
.PHONY: translate
translate:
	pybabel extract -o ./locales/base.pot ./{{cookiecutter.project_name.lower().replace('-', '_')}}
	pybabel update -d ./locales -i ./locales/base.pot
	pybabel compile -d ./locales

{% endif %}.PHONY: test
test: style package unit
