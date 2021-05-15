import random

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    try:
        context = dict(number=random.randint(10, 20), fruit=random.choice(["apple", "banana", "orange"]),
                       values=["foo", "bar", "baz", "qux", "quux", "quuux", "<span></span>"], )
        # TODO I'm not yet happy with this, this is quite dependant on the CWD.
        return render(request, 'web_homepage/index.html', context=context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Sorry, the administrator has not yet configured an imprint.")
    # return redirect("https://betreiberverein.de/impressum/")
