from django.urls import path, include
from .views import helloAPI
from .views import BoxApi
from .views import AddressApi

urlpatterns = [
    path("hello/",helloAPI),
    path("box/",BoxApi),
    path('box/<str:box_code>/', BoxApi, name='box-api-detail'),
    path("address/",AddressApi),
    path('address/<str:box_code>/', AddressApi, name='address-api-detail'),

]