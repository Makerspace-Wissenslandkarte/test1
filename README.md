# test1
Repo for Testing Django, CI/CD and Docker.

## Open Tasks (for this small test repo)
* run it from an IDE with an debugger?
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
* secret is generated on first start of server, but only if the config has not been loaded before (e.g. within some docker run commands during image creation.)
