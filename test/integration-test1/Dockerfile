FROM python:3.8-alpine 
RUN apk add curl
COPY . /test
WORKDIR /test
CMD sh test.sh
