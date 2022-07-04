#! /usr/bin/env make

age := $(shell echo $(shell date +%s) - $(shell date -r dict2dot +%s) | bc)


age:
	@echo Running package from ${age}s ago

test: age
	@PYTHONPATH=. PYTHONSTARTUP=tests/repl-modules.py python -B tests/__main__.py

shell: age
	@PYTHONPATH=. PYTHONSTARTUP=tests/repl-modules.py python -B