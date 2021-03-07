from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.http import HttpResponseNotFound

from django.http import HttpResponse
from .models import Imprint, PrivacyPolicy


def imprint(request):
    try:
        return redirect(Imprint.objects.get().url)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Sorry, the administrator has not yet configured an imprint.")
    #return redirect("https://betreiberverein.de/impressum/")


def privacy_policy(request):
    try:
        return redirect(PrivacyPolicy.objects.get().url)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Sorry, the administrator has not yet configured a privacy policy.")
    #return redirect("https://betreiberverein.de/datenschutzerklaerung/")
