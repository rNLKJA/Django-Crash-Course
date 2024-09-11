from django.urls import path
from . import views  # from current directory import views

# URLConfig / urlpatterns is a list of URL patterns
urlpatterns = [
    path(route='hello/', view=views.say_hello)  # path() is a function that takes in a route and a view function. http://localhost:8000/playground/hello/
]