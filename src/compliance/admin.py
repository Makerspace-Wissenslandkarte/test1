from django.contrib import admin

# Register your models here.
from .models import PrivacyPolicy, Imprint

admin.site.register(PrivacyPolicy)
admin.site.register(Imprint)