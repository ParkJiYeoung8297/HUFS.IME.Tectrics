from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
class UserLogin(APIView):
    def get (self,request):
        return render(request,"Login/userlogin.html")
    
class Join(APIView):
    def get (self,request):
        return render(request,"Login/join.html")