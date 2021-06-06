from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment
from fontawesome_5.templatetags import fontawesome_5

from wissenslandkarte.settings import DEBUG, ENABLE_LIVE_JS


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'fontawesome_5_static': fontawesome_5.fontawesome_5_static,
        'debug': DEBUG,
        'setting_enable_livejs' : ENABLE_LIVE_JS
    })
    return env
