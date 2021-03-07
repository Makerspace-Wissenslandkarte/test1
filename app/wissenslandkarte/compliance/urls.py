from django.urls import path

from . import views

from django.db import models
from django.core.exceptions import ValidationError


urlpatterns = [
    path('impressum/', views.imprint, name='imprint'),
    path('datenschutz/', views.privacy_policy, name='privacy policy'),
]
