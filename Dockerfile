FROM python:3.8-alpine
RUN pip install pipenv
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
COPY ./app/ /app/
WORKDIR /opt/wissenslandkarte.betreiberverein.de/
WORKDIR /app/
RUN pipenv install --deploy
VOLUME /app/wissenslandkarte/data/
EXPOSE 8000
WORKDIR /app/wissenslandkarte
ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
