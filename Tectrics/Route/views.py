from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order

class Road(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        return render(request,"Route/road.html",{'tmap_key': tmap_key})
    

class Map(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        address_list = Order.objects.values("road_address", "detail_address")
        context = {"address_list": address_list,'tmap_key': tmap_key}
        return render(request,"Route/map.html",context)


