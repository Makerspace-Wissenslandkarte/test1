#!/bin/bash
set -euf -o pipefail

function run(){
  docker build . -f selenium.dockerfile
}

function cleanup(){
  true
}

trap cleanup EXIT
run