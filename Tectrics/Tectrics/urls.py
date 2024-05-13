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
#from .views import Main
from Route.views import Road
from Load.views import BoxLoad, LoadData, LayerLoad
from Box.views import BoxList
from Order.views import its
from Order.views import upload_file 
from Route.views import Map
from Login.views import Join
from Login.views import UserLogin
from Box.views import getbox
from django.conf.urls.static import static  
from django.conf import settings 
from Load.views import Index  
from Load.views import pack_items
from Route.views import getmapbox
from Route.views import getaddress
from Load.views import load_sequence#추가
from Load.views import layer
from Load.views import LoadList
from Load.views import getloaddata
from . import views
from Load.views import save_row_data




urlpatterns = [
    path("admin/", admin.site.urls),
    #path("",Main.as_view()),
    path("",UserLogin.as_view()),
    path("Route/road",Road.as_view()),
    path("Load/boxload",BoxLoad.as_view()),
    path("Load/layer",LayerLoad.as_view()),
    path("Box/boxlist",BoxList.as_view()),
    path('Route/map', Map.as_view()),
    path('upload/', upload_file, name='upload_file'),
    path("Order/itsdata",its.as_view()),
    path("Login/join",Join.as_view()),
    path("Login/userlogin",UserLogin.as_view()),
    path("getbox/",getbox,name='getbox'),
    path("Load/index",Index.as_view()),
    path('Load/loaddata',LoadData.as_view()), 
    path("getmapbox/",getmapbox,name='getmapbox'),
    path('pack-items/', pack_items, name='pack-items'), 
    path("getaddress/",getaddress,name='getaddress'), 
    path("load_sequence/",load_sequence,name='load_sequence'), # 적재순서 변환
    path("layer/",layer,name='layer'),
    path("Load/boxload",LoadList.as_view()),
    path("getloaddata/",getloaddata,name='getloaddata'), 
    path("layer_view/",views.layer_view,name='layer_view'),
    path("save_row_data/",save_row_data,name='save_row_data'),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 