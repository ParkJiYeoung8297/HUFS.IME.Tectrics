from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        return render(request,"Tectrics/main.html",{'tmap_key': tmap_key})