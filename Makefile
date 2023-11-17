SHELL:=/usr/bin/env bash

.PHONY: package
package:
	poetry check
	pip check

.PHONY: unit
unit:
	pytest

.PHONY: test
test: package unit
