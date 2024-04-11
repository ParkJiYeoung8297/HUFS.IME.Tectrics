from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order
from Order.models import BoxData
from Login.models import User

class Road(APIView):
    def get(self,request):
        user_id=request.session['user_id']
        print('로그인한 사용자 : ',request.session['user_id'])
        user=User.objects.filter(user_id=user_id).values("dev_code").first()
        if user is not None:
            # dev_code를 사용하여 필터링
            dev_code = user['dev_code']
            box_codes = Order.objects.filter(delivery_man_code=dev_code).values_list("box_code")
            order_list = Order.objects.filter(box_code__in=box_codes).values("box_code","road_address", "detail_address")
            address_list=BoxData.objects.filter(box_code__in=box_codes).values("latitude","longitude","latitude2","longitude2")

        else:
            order_list = []
            address_list=[]
        tmap_key = open("TmapRestKey.txt", "r").read()
        
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key,"user_id":user_id}
        return render(request,"Route/road.html",context)

class Map(APIView):
    def get(self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()

        user_id=request.session['user_id']
        print('로그인한 사용자 : ',request.session['user_id'])
        user=User.objects.filter(user_id=user_id).values("dev_code").first()
        if user is not None:
            # dev_code를 사용하여 필터링
            dev_code = user['dev_code']
            box_codes = Order.objects.filter(delivery_man_code=dev_code).values_list("box_code")
            order_list = Order.objects.filter(box_code__in=box_codes).values("box_code","road_address", "detail_address")
            address_list=BoxData.objects.filter(box_code__in=box_codes).values("latitude","longitude","latitude2","longitude2")
        else:
            order_list = []
            address_list=[]
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key,"user_id":user_id}
        return render(request,"Route/map.html",context)
     
    

