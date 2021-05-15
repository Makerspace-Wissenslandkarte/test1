from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


# TODO this is proof of concept code and should be removed.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

