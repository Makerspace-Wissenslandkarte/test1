"""
Django settings for wissenslandkarte project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.core.management.utils import get_random_secret_key
import pickle
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

DEBUG_FILE = BASE_DIR.joinpath("./data/ACTIVATE_DEBUG_MODE")
# If you want to debug; create a file in the directory indicated above.
DEBUG = DEBUG_FILE.exists()
# this allows to use {% if debug %} in django templates.
INTERNAL_IPS = ['127.0.0.1', '::1']

SECRET_KEY_FILE = BASE_DIR.joinpath("./data/django-secret-key.pickle")


def load_or_create_secret_key() -> str:
    # TODO we might want to record hostname and time of the secret creation in this pickle, to allow us to recognize if
    #  it becomes a constant during docker builds. Also, we might want to delete/recreate it explicitly during
    #  first startup.
    try:
        secret = pickle.load(open(SECRET_KEY_FILE, "rb"))
        return secret
    except FileNotFoundError:
        secret = get_random_secret_key()
        pickle.dump(secret, open(SECRET_KEY_FILE, "wb"))
        return secret


SECRET_KEY = load_or_create_secret_key()

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    'python',
    # 'wissenslandkarte.betreiberverein.de',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
    'django.contrib.auth',  # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
    'django.contrib.contenttypes',  # https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/
    'django.contrib.sessions',  # https://docs.djangoproject.com/en/3.2/topics/http/sessions/
    'django.contrib.messages',  # https://docs.djangoproject.com/en/3.2/ref/contrib/messages/
    'django.contrib.staticfiles',  # https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/
    'fontawesome_5',
    'api',
    'compliance',
    'web_homepage',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # TODO both of these are not active for static files, and have to be configured in nginx again.
    #  this applies especially to:
    #  * CSP on static html files that are served to be displayed
    #  * User Uploads, e.g. images.
    #  * HSTS on every ressource.
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'wissenslandkarte.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wissenslandkarte.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data' / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # TODO we should use a german list for our target group, however, these are difficult to find.
        #  Use Duden, given names, surnames, sports clubs and qwertz-Keywalks?
        # https://docs.djangoproject.com/en/3.1/topics/auth/passwords/#password-validation
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # 'password_list_path' : '...'
        # This file should contain one lowercase password per line and may be plain text or gzipped.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = ["static"]
STATIC_ROOT = os.getenv("COLLECTSTATIC_DIR", None)

# TODO decide how to handle development environments.
# SECURE_HSTS_SECONDS = 0

CSP_DEFAULT_SRC = ("'self'")
CSP_IMG_SRC = ("'self'", "https://betreiberverein.de")
if DEBUG:
    # this is required for live.js.
    CSP_DEFAULT_SRC = ("'self'","'unsafe-inline'","'unsafe-eval'")
    CSP_SCRIPT_SRC = ("'self'","'unsafe-inline'","'unsafe-eval'")
if not DEBUG:
    # This should only be enabled from certain docker container builds, due to a quota; and should be configurable by the admin.
    # CSP_REPORT_URI = "https://p.report-uri.com/r/d/csp/enforce"
    pass
#CSP_REPORT_TO = "default"
