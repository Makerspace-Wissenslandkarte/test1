# test1
Repo for Testing Django, CI/CD and Docker.

## How to run.
Please don't run this for production yet.

* Check ./src/wissenslandkarte/settings.py:
  * You might want to enable HSTS
  * You might configure a report URI
  * You must set ALLOWED_HOSTS

## Open Tasks (for this small test repo)
* run it from an IDE with an debugger?
* get rid of the redundant "app/ directory?"
* Set up an nginx before Django
* Check out Github CodeQL and https://github.com/marketplace/lgtm
* Check if we can authenticate access to static files with XSendfile.
* Connecting a database
* Create user database
* Allow user authentication and provide session cookie
* User Registration
* Unit Tests
* Automatically running unit tests
* Automatically publishing docker containers
* Check if we can document the API with tools like Swagger or some other postprocessor pushing to Github or Github Pages
* Provide a usable Plain Text API with Django Tools (Authentication via Header?)
* Try out REST or GraphQL?

## Security

* replace dev server from manage.py with nginx
* ensure proper HTTPS Host header in reverse proxy. 
* secret is generated on first start of server, but only if the config has not been loaded before (e.g. within some docker run commands during image creation.)
* Docker is intended as production environment; if you want to just checkout this repo on a production server;
  please ensure to reapply security measures (deleting default secrets) from within the Dockerfile. 

## How to develop?

* install python3.8
* pip install pipenv
* pipenv install
* You might want to create the ./app/wissenslandkarte/data/ACTIVATE_DEBUG_MODE file
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py migrate
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py createsuperuser
* cd ./app/wissenslandkarte/ && pipenv run python ./manage.py runserver