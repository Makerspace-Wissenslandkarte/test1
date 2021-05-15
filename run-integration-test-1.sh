#!/bin/bash
docker-compose -f docker-compose.yml -f docker-compose-integrationtest.yml build
docker-compose -f docker-compose.yml -f docker-compose-integrationtest.yml run python migrate
docker-compose -f docker-compose.yml -f docker-compose-integrationtest.yml up --exit-code-from integration-test1
