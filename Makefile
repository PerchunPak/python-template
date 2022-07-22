SHELL:=/usr/bin/env bash

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run mypy --install-types --non-interactive .

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: style package unit
