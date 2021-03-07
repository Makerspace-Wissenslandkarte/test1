FROM python:3.8-alpine
RUN pip install pipenv
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
COPY ./app/ /app/
WORKDIR /opt/wissenslandkarte.betreiberverein.de/
WORKDIR /app/
RUN pipenv install --deploy





# remove all present data, and replace it with the production data
# This should be one of the last steps, to ensure no prepopulated secret gets included in the build.
RUN rm -rf /app/wissenslandkarte/data/
COPY ./app/wissenslandkarte/production-data/ /app/wissenslandkarte/data/
VOLUME /app/wissenslandkarte/data/

EXPOSE 8000
WORKDIR /app/wissenslandkarte
ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
