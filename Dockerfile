FROM python:3.8-alpine AS python-dependencies
RUN pip install pipenv

WORKDIR /opt/wissenslandkarte.betreiberverein.de/

COPY ./Pipfile .
COPY ./Pipfile.lock .
# We have to enable this to allow the non-root-user to access the write-protected python later on.
# Otherwise, the venv would reside in /root/.local/share/virtualenvs/
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --deploy



FROM python-dependencies AS python-app

COPY src .

# remove all present data, and replace it with the production data
# This should be one of the last steps, to ensure no prepopulated secret gets included in the build.
RUN rm -rf ./data/
RUN mkdir ./data/
COPY src/production-data/ ./data/



FROM python-app as python-static
RUN COLLECTSTATIC_DIR=/opt/static.wissenslandkarte.betreiberverein.de/static pipenv run python manage.py collectstatic
WORKDIR /opt/static.wissenslandkarte.betreiberverein.de/
# RUN ls .



FROM nginx:1-alpine as nginx
RUN rm /etc/nginx/conf.d/default.conf
# Assert there is no other site configured, e.g. after a base image update
RUN test -n "$(find /etc/nginx/conf.d/ -empty -maxdepth 0)"
ADD nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /var/www/web/
COPY --from=python-static /opt/static.wissenslandkarte.betreiberverein.de/static/ ./static/
#RUN pwd ; ls -la ; ls -la static
# no USER directive; nginx will switch to the "nginx" user by itself, as configured by the base image
EXPOSE 80



FROM python-app as python-web
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown appuser:appgroup data
RUN chmod 700 data
USER appuser
VOLUME /opt/wissenslandkarte.betreiberverein.de/data/

EXPOSE 8000
ENTRYPOINT ["pipenv", "run"]
CMD ["gunicorn", "wissenslandkarte.wsgi"]
