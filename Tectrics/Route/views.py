from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order
from Order.models import BoxData

class Road(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        order_list = Order.objects.values("box_code","road_address", "detail_address")
        address_list=BoxData.objects.values("latitude","longitude","latitude2","longitude2")
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key}
        return render(request,"Route/road.html",context)

class Map(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        order_list = Order.objects.values("box_code","road_address", "detail_address")
        address_list=BoxData.objects.values("latitude","longitude","latitude2","longitude2")
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key}
        return render(request,"Route/map.html",context)
     
    

