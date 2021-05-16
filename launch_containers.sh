#!/bin/bash
set -euf -o pipefail
COMPOSE="docker-compose -f docker-compose.yml"
$COMPOSE build --parallel
$COMPOSE run python ./manage.py migrate
$COMPOSE up
