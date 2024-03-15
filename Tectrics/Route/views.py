from django.shortcuts import render
from rest_framework.views import APIView


class Road(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        return render(request,"Route/road.html",{'tmap_key': tmap_key})