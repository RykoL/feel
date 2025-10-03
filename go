#!/usr/bin/env bash

UV_RUN="uv run"

function task_run () {
  [ ! -f local.env ] || export $(grep -v '^#' local.env | xargs)
  $UV_RUN ./manage.py runserver --settings feel.settings.base
}

function task_test () {
  $UV_RUN pytest
}

function task_format() {
  $UV_RUN ruff format
}

function task_manage() {
  $UV_RUN ./manage.py $@
}

function help () {
    echo "Usage: ./go task_name"
    echo ""
    echo "Available tasks are:"
    echo "run - run the server in development mode"
    echo "test - runs pytest against the application"
    echo "manage - simple wrapper around ./manage.py"
    echo "format - Format the project using ruff"
}

if [[ $# -lt 1 ]]; then
  help
  exit 1
fi

TARGET=$1
shift
"task_${TARGET}" "$@"
