SHELL:=/usr/bin/env bash

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: unit
unit:
ifeq ($(ci),1)
	poetry run pytest --no-testmon
else
	poetry run pytest --no-cov
endif

.PHONY: test
test: package unit
