from django.urls import path, include
from .views import helloAPI
from .views import BoxApi

urlpatterns = [
    path("hello/",helloAPI),
    path("box/",BoxApi),
]