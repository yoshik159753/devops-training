#!/bin/bash

HOST_PORT=5432
CONTAINER_PORT=5432
CONTAINER_NAME=rails-postgres
IMAGE_TAG_NAME=postgres

usage() {
  cat 1>&2 <<EOF
USAGE:
    sh app.sh [-h] xxx
POSITIONAL ARGUMENTS:
    db                        exec docker start $CONTAINER_NAME &
    db-first                  exec docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME -e POSTGRES_PASSWORD=mysecretpassword $IMAGE_TAG_NAME &
    app                       PIPENV_DOTENV_LOCATION=/path/to/.env pipenv run run.py
    test                      PIPENV_DOTENV_LOCATION=/path/to/.env pipenv run pytest
    stop                      exec docker stop $CONTAINER_NAME &
FLAGS:
    -h, --help                Prints help information
EOF
}

die() {
  err_msg="$1"
  echo "$err_msg" >&2
  exit 1
}

handle() {
  while test $# -gt 0; do
    key="$1"
    case "$key" in

    db)
      exec docker start $CONTAINER_NAME &
      exit 0
      ;;
    db-first)
      exec docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME -e POSTGRES_PASSWORD=mysecretpassword $IMAGE_TAG_NAME &
      exit 0
      ;;
    app)
      export PIPENV_DOTENV_LOCATION=.env.it
      exec pipenv run python run.py
      exit 0
      ;;
    test)
      export PIPENV_DOTENV_LOCATION=.env.ut
      exec pipenv run pytest
      exit 0
      ;;
    stop)
      exec docker stop $CONTAINER_NAME &
      exit 0
      ;;
    -h | --help)
      usage
      exit 0
      ;;
    *)
      die "Got an unexpected argument: $1"
      ;;
    esac
    shift
  done
}

main() {
  handle "$@"
  exit 0
}

main "$@" || exit 1
