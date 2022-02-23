SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run black .
	poetry run isort .
	poetry run mypy --install-types --non-interactive hooks tests

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit
