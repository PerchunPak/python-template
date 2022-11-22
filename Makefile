SHELL:=/usr/bin/env bash

.PHONY: package
package:
	poetry check
	pip check
	safety check --full-report

.PHONY: unit
unit:
ifeq ($(ci),1)
	pytest --no-testmon
else
	pytest --no-cov
endif

.PHONY: test
test: package unit
