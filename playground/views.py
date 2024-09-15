"""
views.py is used to define the logic of the app
request handler: function that takes a request and returns a response
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
# request -> response or action

# def say_hello(request: HttpRequest) -> HttpResponse:
#     return HttpResponse("Hello World")

def say_hello(request: HttpRequest):
    return render(request=request, 
                  template_name='hello.html', 
                  context= {'name': 'Rin'})