FROM python:3.8-alpine
RUN pip install pipenv
COPY ./src/ /app/
WORKDIR /opt/wissenslandkarte.betreiberverein.de/
WORKDIR /app/
RUN pipenv install --deploy
VOLUME /app/data/
ENTRYPOINT echo "Hello World!"
