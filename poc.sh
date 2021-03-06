#!/bin/sh
docker build . -f Dockerfile -q | xargs -I{} docker run -i {}
