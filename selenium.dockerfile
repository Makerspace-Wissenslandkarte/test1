FROM ubuntu:groovy AS python-dependencies
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install firefox-geckodriver -y
RUN pip install pipenv

WORKDIR /opt/wissenslandkarte.betreiberverein.de/

COPY ./Pipfile .
COPY ./Pipfile.lock .
# We have to enable this to allow the non-root-user to access the write-protected python later on.
# Otherwise, the venv would reside in /root/.local/share/virtualenvs/
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --deploy --dev



FROM python-dependencies AS python-app

COPY src .

# remove all present data, and replace it with the production data
# This should be one of the last steps, to ensure no prepopulated secret gets included in the build.
RUN rm -rf ./data/
RUN mkdir ./data/
COPY src/production-data/ ./data/


FROM python-app as python-web
VOLUME /opt/wissenslandkarte.betreiberverein.de/data/

RUN ["pipenv", "run", "./manage.py", "test"]

