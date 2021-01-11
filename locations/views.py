from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Index page for locations")


def view_with_parameter(request, parameter):
    return HttpResponse(f"String parameter : {parameter}")


def view_with_int_parameter(request, parameter):
    return HttpResponse(f"Integer parameter : {parameter}")
