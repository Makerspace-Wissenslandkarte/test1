import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.shortcuts import render

from django.http import HttpResponse


def profiles(request):
    try:
        profile = dict(tags=["Holz","Schreinern", "Hobeln", "Drechseln", "Zimmern", "Möbelbau"],
        knowlages=[["3D-Druck",5,1],["Sprechen",4,2],["Schach",3,3],["Erste Hilfe",2,4],["Brettspiele",1,5]],
        profileindex=0, skillindex=0,skill=["Holz",2,1])
        # TODO I'm not yet happy with this, this is quite dependant on the CWD.
        return render(request, 'profiles/index.html',context=profile)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Sorry, the administrator has not yet configured an profile edit.")
    # return redirect("https://betreiberverein.de/impressum/")
