from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http import JsonResponse
from django.views import View
from Load.models import LoadedBoxData
from Login.models import User
from Order.models import Order
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from Order.models import Order
from Order.models import BoxData
from Load.models import LoadedBoxData
from Login.models import User
from datetime import date
from .main import Packer, Item, Bin
import random
from django.db import transaction
from django.core.paginator import Paginator 


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
            Load_list = Order.objects.filter(delivery_man_code=dev_code).values("box_code", "name", "road_address", "detail_address", "phone","")
        else:
            Load_list = []
        context={"order_list":Load_list,"user_id":user_id}
        return render(request,"Box/boxlist.html",context)       

def generate_random_color():
    """ RGB 형식의 랜덤 색상 생성 """
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))           

def pack_items(request):
    user_id = request.session.get("user_id")
    
    if not user_id:
        return JsonResponse({"error": "User not authenticated"}, status=400)
    
    # User 테이블에서 user_id를 기반으로 dev_code 가져오기
    user = User.objects.filter(user_id=user_id).values("dev_code").first()
    
    if not user:
        return JsonResponse({"error": "User not found"}, status=404)
    
    dev_code = user["dev_code"]
    orders = Order.objects.filter(delivery_man_code=dev_code)
    
    if request.method == 'POST':
        items = [
            Item(partno=item.id, name=item.box_code, typeof='cube', weight=1, loadbear=100, updown=True, color=generate_random_color(),
                 WHD=[item.length, item.width, item.height],
                 level=item.sequence)
            for item in BoxData.objects.filter(box_code__in=[order.box_code for order in orders])
        ]

        # 가정: 한 개의 빈만 사용
        

        packer = Packer()
        box = Bin('example', (2700, 1600, 1600), 500, 0, 0)
        packer.addBin(box)
        for item in items:
            packer.addItem(item)

        packer.pack(bigger_first=True, distribute_items=True, fix_point=True, check_stable=True, support_surface_ratio=0.75)
        
         # 데이터베이스 트랜잭션 시작
    with transaction.atomic():
        for bin in packer.bins:
            for item in bin.items:
                # 로드된 박스 데이터 저장
                loaded_box_data = LoadedBoxData(
                    box_code=item.name,
                    width=item.width,
                    height=item.height,
                    depth=item.depth,
                    volume=item.width * item.height * item.depth,
                    layer=1,
                    deliverySequence=item.level, # level을 deliverySequence로 설정
                    loadSequence=1,  # loadbear 값으로 loadSequence 설정
                    positionX=item.position[0],
                    positionY=item.position[1],
                    positionZ=item.position[2],
                    color=item.color
                )
                loaded_box_data.save()

    
        results = [{'bin': bin.partno, 'items': [item.name for item in bin.items]} for bin in packer.bins]
        return JsonResponse({'results': results})
            
    # 각 레이어 별로 박스를 분류하는 함수
# def classify_boxes_by_layers(data):
#     layer1 = []  # 0 ~ 900
#     layer2 = []  # 900 ~ 1800
#     layer3 = []  # 1800 ~ 2700

#     for box in data:
#         center_x = box['positionX'] + box['width'] / 2  # 중심점 X 좌표 계산

#         if 0 <= center_x < 900:
#             layer1.append(box)
#         elif 900 <= center_x < 1800:
#             layer2.append(box)
#         elif 1800 <= center_x < 2700:
#             layer3.append(box)

#     return layer1, layer2, layer3

# # 함수 실행
# layer1, layer2, layer3 = classify_boxes_by_layers(data)
# for box in layer2:
#   print(box['id'])
  
  

# #결과 출력
# print("Layer 1:", json.dumps(layer1, indent=4))
# print("Layer 2:", json.dumps(layer2, indent=4))
# print("Layer 3:", json.dumps(layer3, indent=4))

    results = [{'bin': bin.partno, 'items': [item.name for item in bin.items]} for bin in packer.bins]
    return JsonResponse({'results': results})

def assign_load_sequence(request):
    all_boxes = LoadedBoxData.objects.order_by('deliverySequence')
    paginator = Paginator(all_boxes, 10)

    with transaction.atomic():
        try:
            for page_num in range(1, paginator.num_pages + 1):
                page = paginator.page(page_num)
                
                for idx, box in enumerate(page.object_list):
                    box.loadSequence = idx + 1
                    box.save()

                    print(f"Updated box {box.id} with loadSequence {box.loadSequence}")

        except Exception as e:
            print(f"An error occurred: {e}")
            raise