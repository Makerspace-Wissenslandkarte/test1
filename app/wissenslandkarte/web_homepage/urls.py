from django.urls import path

from . import views

from django.db import models
from django.core.exceptions import ValidationError


urlpatterns = [
    path('', views.home, name='home'),
]
