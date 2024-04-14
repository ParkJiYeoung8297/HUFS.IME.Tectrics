from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order
from Order.models import BoxData
from Login.models import User
from django.db.models import Count
from django.http import JsonResponse

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
            address_list=BoxData.objects.filter(box_code__in=box_codes).values("box_code","latitude","longitude","latitude2","longitude2")
            unique_latlon=BoxData.objects.filter(box_code__in=box_codes).values("latitude","longitude").distinct()
            unique_latlon2=BoxData.objects.filter(box_code__in=box_codes).values("latitude2","longitude2").distinct()

        else:
            order_list = []
            address_list=[]
        tmap_key = open("TmapRestKey.txt", "r").read()
        
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key,"user_id":user_id,"unique_latlon":unique_latlon,"unique_latlon2":unique_latlon2}
        return render(request,"Route/road.html",context)
    
    def patch(self,request):
        box_code=request.data.get('box_code',None)
        sequence=request.data.get('sequence',None)
        lat2=request.data.get('latitude2',None)
        lon2=request.data.get('longitude2',None)
        
        box_list=BoxData.objects.filter(latitude2=lat2,longitude2=lon2).update(sequence=sequence)
               
        if not box_list.exists():
            return JsonResponse(status=400, data={"message": "해당 주소가 없습니다."})
        return JsonResponse({"message": "성공적으로 업데이트되었습니다."})



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
            unique_latlon=BoxData.objects.filter(box_code__in=box_codes).values("latitude","longitude").distinct()
            unique_latlon2=BoxData.objects.filter(box_code__in=box_codes).values("latitude2","longitude2").distinct()
        else:
            order_list = []
            address_list=[]
        context = {"order_list":order_list,"address_list": address_list,'tmap_key': tmap_key,"user_id":user_id,"unique_latlon":unique_latlon,"unique_latlon2":unique_latlon2}
        return render(request,"Route/map.html",context)
     
    

