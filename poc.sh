#!/bin/bash
IIDFILE="$(mktemp)"
docker build . -f Dockerfile --iidfile "$IIDFILE"
IMAGE="$(cat $IIDFILE)"
rm "$IIDFILE"
docker run -it "$IMAGE"
