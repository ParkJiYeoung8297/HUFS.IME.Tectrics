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
    
# Python 코드에서 JSON 파일 읽기
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

json_data = read_json_file('./graduation_project-main/packed_items_layer.json')

# Python 코드에서 JSON 데이터를 Django 모델로 변환하고 저장하기
from Load.models import LoadedBoxData

def save_to_database(json_data):
    for item in json_data:
        obj = LoadedBoxData(
            box_code=item['box_code'],
            width=item['width'],
            height=item['height'],
            depth=item['depth'],
            volume=item['volume'],
            layer=item['layer'],
            deliverySequence=item['deliverySequence'],
            loadSequence=item['loadSequence'],
            positionX=item['positionX'],
            positionY=item['positionY'],
            positionZ=item['positionZ'],
            color=item['color']
            # 필요한 경우 다른 필드들도 여기에 추가합니다.
        )
        obj.save()

# 위에서 읽은 JSON 데이터를 데이터베이스에 저장합니다.
save_to_database(json_data)
