# test1
Repo for Testing Django, CI/CD and Docker.

## Open Tasks (for this small test repo)

* Set up pipenv instead of pip for reproducability and cleanup of installed dependencies.
* Initialize Django
* Containerize this and run it from an IDE
* Create an integration test to confirm it actually runs.
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

* replace dev server with DEBUG mode from manage.py with nginx.
* generate a new secret https://github.com/Makerspace-Wissenslandkarte/test1/blob/main/app/wissenslandkarte/wissenslandkarte/settings.py#L23 for production use
