from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import JsonResponse
from django.views import View
from Load.models import LoadedBoxData
from Login.models import User
from Order.models import Order 


class BoxLoad(APIView):
    def get(self,request):
        user_id=request.session['user_id']
        context = {"user_id":user_id}
        return render(request,"Load/boxload.html",context)
    
class Index(APIView):
    def get(self,request):
        
        return render(request,"Load/index.html")
    
class LoadData(APIView):
    def post(self,request):
        data = json.loads(request.body)
        
        LoadedBoxData.objects.create(name=data["name"],width=data["width"],height=data["height"],depth=data["depth"],volume=data["volume"],layer=data["layer"],deliverySequence=data["deliverySequence"],loadSeuqence=data["loadSeuqence"],positionX=data["positionX"],positionY=data["positionY"],positionZ=data["positionZ"])
        
        return JsonResponse({"message":"created"}, status=201)
    
    def get(self,request):
        results = []
        boxdata_list = LoadedBoxData.objects.all()
        
        for i in boxdata_list:
            results.append({"name":i.name,"width":i.width,"height":i.height,"depth":i.depth,"volume":i.volume,"layer":i.layer,"deliverySequence":i.deliverySequence,"loadSeuqence":i.loadSeuqence,"positionX":i.positionX,"positionY":i.positionY,"positionZ":i.positionZ})
            
        return JsonResponse({"results":results}, status=200)

class LoadList(APIView):
    def get(self,request):
        print('로그인한 사용자 : ',request.session['user_id'])
        user_id=request.session['user_id']
        user=User.objects.filter(user_id=user_id).values("dev_code").first()
        if user is not None:
            # dev_code를 사용하여 필터링
            dev_code = user['dev_code']
            order_list = Order.objects.filter(delivery_man_code=dev_code).values("box_code", "name", "road_address", "detail_address", "phone","")
        else:
            order_list = []
        context={"order_list":order_list,"user_id":user_id}
        return render(request,"Box/boxlist.html",context)        