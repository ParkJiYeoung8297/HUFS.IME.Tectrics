from django.shortcuts import render
from rest_framework.views import APIView


class BoxLoad(APIView):
    def get(self,request):
        return render(request,"Load/boxload.html")