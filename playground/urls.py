"""
urls.py is used to define the URL patterns of the app
"""

from django.urls import path
from . import views

# URLConf module: a module that contains URL patterns for an app
urlpatterns = [
    path('hello/', views.say_hello)
]

# urlpatterns is a list of path objects, each path object is a URL pattern
# path(route, view, name=None)
# route: URL pattern
# view: function that handles the request
# name: name of the URL pattern

# URLConf module: a module that contains URL patterns for an app
# URLConf: a configuration for URL patterns
# URL dispatcher: a component that matches the incoming request to the correct view