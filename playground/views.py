from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler / action -> django view function

def say_hello(request) -> HttpResponse:
    return HttpResponse('Hello world!')
