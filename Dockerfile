FROM python:3.8-alpine
RUN pip install pipenv

WORKDIR /opt/wissenslandkarte.betreiberverein.de/

COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --deploy

COPY src .

# remove all present data, and replace it with the production data
# This should be one of the last steps, to ensure no prepopulated secret gets included in the build.
RUN rm -rf ./data/
RUN mkdir ./data/
COPY src/production-data/ ./data/
VOLUME /opt/wissenslandkarte.betreiberverein.de/data/

EXPOSE 8000
ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
