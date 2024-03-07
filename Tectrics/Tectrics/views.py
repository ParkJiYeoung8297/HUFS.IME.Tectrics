from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self,request):
        kakao_key = open("kakaoRestKey.txt", "r").read()
        return render(request,"Tectrics/main.html",{'kakao_key': kakao_key})