# test1
Repo for Testing Django, CI/CD and Docker.

## How to run.
Please don't run this for production yet.

* Check ./src/wissenslandkarte/settings.py:
  * You might want to enable HSTS
  * You might configure a report URI
  * You must set ALLOWED_HOST
* Check ./nginx/default.conf
  * You must set the server_name under which the server will be reachable, otherwise all requests will be refused (421) 
## Open Tasks (for this small test repo)
* Check out Github CodeQL and https://github.com/marketplace/lgtm
* Check if we can authenticate access to static files with XSendfile.
* Connecting a database
* User Registration
* Check if we can document the API with tools like Swagger or some other postprocessor pushing to Github or Github Pages
* Provide a usable Plain Text API with Django Tools (Authentication via Header?)
* Try out REST or GraphQL?

## Security

* Docker is intended as production environment; if you want to just checkout this repo on a production server;
  please ensure to reapply security measures (deleting default secrets) from within the Dockerfile. 
* The debug mode is currently enabled via a flag file in the data dir, where the application itself still has write permissions
  * Permissions can be removed when a PGSQL DB is present instead of sqlite
  * Dynaconf or environment variables loaded by pipenv from an env file can be used
    instead of the flag file; this would allow automated configuration changes, too.
* SESSION_COOKIE_SECURE and SESSION_COOKIE_SECURE are not set, this should be activated when a HTTPS reverse proxy is present.
* Connections between Docker Containers are not encrypted yet.
* unsafe-eval is still enabled in Production mode due to standalone Vue.js requirements -- see settings.py.

## How to develop?

* install python3.8
* pip install pipenv
* pipenv install
* You might want to create the ./app/wissenslandkarte/data/ACTIVATE_DEBUG_MODE file
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py migrate
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py createsuperuser
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py runserver
