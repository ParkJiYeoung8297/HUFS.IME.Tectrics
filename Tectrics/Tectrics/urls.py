"""
URL configuration for Tectrics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Main
from Route.views import Road
from Load.views import BoxLoad
from Box.views import BoxList
from Order.views import its
from Order.views import upload_file 
from Route.views import Map
from Login.views import Join
from Login.views import UserLogin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",Main.as_view()),
    path("Route/road",Road.as_view()),
    path("Load/boxload",BoxLoad.as_view()),
    path("Box/boxlist",BoxList.as_view()),
    path('Route/map', Map.as_view()),
    path('upload/', upload_file, name='upload_file'),
    path("Order/itsdata",its.as_view()),
    path("Login/join",Join.as_view()),
    path("Login/userlogin",UserLogin.as_view())
]
