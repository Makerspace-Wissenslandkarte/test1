#!/bin/bash
set -euf -o pipefail
COMPOSE="docker-compose -f docker-compose.yml"
$COMPOSE build
$COMPOSE run python migrate
$COMPOSE up
