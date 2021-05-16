#!/bin/bash
set -euf -o pipefail
# Set unique name to avoid test interfering with a running service
export COMPOSE_PROJECT_NAME="$(basename "$(pwd)")-$(basename "$0")-$(uuidgen)"

function run(){
  COMPOSE="docker-compose -f docker-compose.yml -f docker-compose-integrationtest.yml"
  $COMPOSE build
  $COMPOSE run python ./manage.py migrate
  $COMPOSE up --exit-code-from integration-test1
}
function cleanup(){
  $COMPOSE rm -f
}

trap cleanup EXIT
run