#! /usr/bin/env make
#.PHONY:
SHELL := $(shell type bash | sed "s/.*is //")
PROJECT_DIR := $(shell realpath .)
include .env


self-test:
	@echo -e "\
		Project: ${PROJECT_NAME} (${PROJECT_DESCRIPTION})\n\
		Source files path: ${PROJECT_DIR}/${SRC_DIR}\n\
		Virtual env: $(shell poetry env info -p 2>/dev/null || echo 'No Poetry venv (may be in production or requires install: \`make install-dev\`)')\n\
		Application: ${APP_NAME} v${APP_VERSION}\n\
	" | sed "s,^\t,," | column -t -s:


install-dev:
	@git init
	@[ -f .python-version ] && poetry env use $(shell cat .python-version) >/dev/null || true
	@poetry install -v #-E psycopg2-binary
	@poetry run pre-commit install
	@sed -i "/^INSTALL_PYTHON=.*/a PATH=$(shell dirname $(shell which poetry)):\$$INSTALL_PYTHON/bin:\$$PATH" .git/hooks/pre-commit
#	@run=dev poetry run python3 setup/dotenv-from-toml.py > .env
#	@${SHELL} setup/create-dirs-from-env.sh

test-unit:
	poetry run python -m pytest tests/unit --exitfirst --verbose  # --capture=no

test-unit-cov: test-unit-coverage
test-unit-coverage:
	@PYTHONPATH=${SRC_DIR} poetry run python -m pytest tests/ --cov --cov-branch --cov-report term-missing

test-pre-commit:
	@poetry run pre-commit run --all-files  # -v

test-code: test-unit test-pre-commit test-unit-coverage


install-build:
	@poetry install -v --all-extras


export-requirements:
	@python3 setup/export-requirements.py


shell:
	@cd ${SRC_DIR} && poetry run python3

clean-project:
	@[ -f .python-version ] && mv -f .python-version .python-version-saved || true
	@git clean -Xdf  # Delete all files in .gitignore: pycache, compile, build, dist, setup/requirements.txt...
	@[ -f .python-version-saved ] && mv -f .python-version-saved .python-version || true
	@rm -rf $(shell poetry env info -p) ${LOGS_DIR}
	@rm -rf /tmp/pytest

clean-all: clean-project
