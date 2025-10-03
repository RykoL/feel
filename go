#!/usr/bin/env bash

UV_RUN="uv run"

function task_run () {
  $UV_RUN ./manage.py runserver --settings feel.settings.base
}

function task_test () {
  $UV_RUN pytest
}

function help () {
    echo "Usage: ./go task_name"
    echo ""
    echo "Available tasks are:"
    echo "run - run the server in development mode"
    echo "test - runs pytest against the application"
}

if [[ $# -lt 1 ]]; then
  help
  exit 1
fi

TARGET=$1
shift
"task_${TARGET}" "$@"
