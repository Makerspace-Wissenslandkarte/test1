from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment
from fontawesome_5.templatetags import fontawesome_5
from wissenslandkarte.settings import DEBUG

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'fontawesome_5_static': fontawesome_5.fontawesome_5_static,
        'debug': DEBUG
    })
    return env
