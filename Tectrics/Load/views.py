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
import os
from django.db.models import F


# class BoxLoad(APIView):
#     def get(self,request):
#         user_id=request.session['user_id']
#         context = {"user_id":user_id}
#         return render(request,"Load/boxload.html",context)
class BoxLoad(APIView):
    def get(self,request):
        print('로그인한 사용자 : ',request.session['user_id'])
        user_id=request.session['user_id']
        user=User.objects.filter(user_id=user_id).values("dev_code").first()
        if user is not None:
            # dev_code를 사용하여 필터링
            dev_code = user['dev_code']
            orders = Order.objects.filter(delivery_man_code=dev_code).values("box_code", "name", "road_address", "detail_address", "phone")
            
            combined_list = []
            for order in orders:
                box_code = order['box_code']
                load_data = LoadedBoxData.objects.filter(box_code=box_code).values(
                    "deliverySequence", "loadSequence", "layer"
                ).first()
                
                # 결합된 딕셔너리 생성
                combined_entry = {
                    "box_code": order['box_code'],
                    "name": order['name'],
                    "road_address": order['road_address'],
                    "detail_address": order['detail_address'],
                    "phone": order['phone'],
                    "deliverySequence": load_data['deliverySequence'] if load_data else None,
                    "loadSequence": load_data['loadSequence'] if load_data else None,
                    "layer": load_data['layer'] if load_data else None
                }
                combined_list.append(combined_entry)
            
            combined_list = sorted(
                combined_list,
                key=lambda x: (x['loadSequence'] is None, x['loadSequence']),
                reverse=False
            )
        else:
            combined_list = []
        
        # 하나의 리스트로 병합된 결과를 템플릿에 전달
        context = {"combined_list": combined_list, "user_id": user_id}
        return render(request, "Load/boxload.html", context)
    
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
            order_list = Order.objects.filter(delivery_man_code=dev_code).values("box_code", "name", "road_address", "detail_address", "phone")
        else:
            order_list = []
        context={"order_list":order_list,"user_id":user_id}
        return render(request,"Load/boxload.html",context) 
    
# @login_required
# @api_view(['POST'])
def load_sequence(request):
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
        # BoxData를 sequence 기준 내림차순 정렬
        box_data_sorted = BoxData.objects.filter(
            box_code__in=[order.box_code for order in orders]
        ).order_by('-sequence')
        
        # 새로운 순서를 부여하고 loadsequence 필드에 저장
        loadsequence = 1
        for index, box in enumerate(box_data_sorted, start=1):
            box.loadsequence = loadsequence
            box.save()
            # 10번째 항목마다 loadsequence를 증가
            if index % 5 == 0:
                loadsequence += 1
        
        # 새로운 loadsequence를 기반으로 아이템 생성
        items = [
            Item(partno=item.id, name=item.box_code, typeof='cube', weight=1, loadbear=100, updown=True, color=generate_random_color(),
                 WHD=[item.length, item.width, item.height], level=item.loadsequence, sequence=item.sequence)
            for item in box_data_sorted
        ]
        
        
        # 필요한 데이터 JSON 응답으로 반환
        response_data = [
            {
                "partno": item.partno,
                "name": item.name,
                "typeof": item.typeof,
                "weight": item.weight,
                "loadbear": item.loadbear,
                "updown": item.updown,
                "color": item.color,
                "level": item.level,
                "loadsequence": index + 1  # 새로운 순서
            }
            for index, item in enumerate(items)
        ]
        
        return JsonResponse({"data": response_data}, status=200, safe=False)
    
    
    
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
                 level=item.loadsequence, sequence=item.sequence)
            for item in BoxData.objects.filter(box_code__in=[order.box_code for order in orders])
        ]

        # 가정: 한 개의 빈만 사용
        packer = Packer()
        box = Bin('example', (2700, 1600, 1600), 500, 0, 0)
        packer.addBin(box)
        for item in items:
            packer.addItem(item)


        packer.pack(bigger_first=True, distribute_items=True, fix_point=True, check_stable=True, support_surface_ratio=0.6)
        
        results = []
        for bin in packer.bins:
            for item in bin.items:
                # 필요한 필드를 결과 목록에 추가
                results.append({
                    "id": item.partno,
                    "box_code": item.name,
                    "width": item.width,
                    "height": item.height,
                    "depth": item.depth,
                    "volume": item.getVolume(),
                    "layer": 1,
                    "deliverySequence": item.sequence,
                    "loadSequence": item.level,
                    "positionX": item.position[0],
                    "positionY": item.position[1],
                    "positionZ": item.position[2],
                    "color": item.color,
                })

        # JSON 파일 생성 경로 설정
        if results:
                try:
                    with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items.json', 'w') as json_file:
                            json.dump(results, json_file, indent=4)
                            print("JSON 파일로 저장되었습니다.")
                except Exception as e:
                        print("JSON 파일 저장 중 오류가 발생했습니다.")
                        print(e)    
        else:
                    print("JSON 파일로 저장할 데이터가 없습니다.")    
         # 데이터베이스 트랜잭션 시작
    with transaction.atomic():
        LoadedBoxData.objects.all().delete()
        
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
                    deliverySequence=item.sequence, # level을 deliverySequence로 설정
                    loadSequence=item.level,  # loadbear 값으로 loadSequence 설정
                    positionX=item.position[0],
                    positionY=item.position[1],
                    positionZ=item.position[2],
                    color=item.color
                )
                loaded_box_data.save()

    
        results = [{'bin': bin.partno, 'items': [item.name for item in bin.items]} for bin in packer.bins]
        return JsonResponse({'results': results})
            
def layer(request):
        # Layer 1: (0,0) ~ (900,800)
        boxes_layer_1 = LoadedBoxData.objects.filter(
            positionX__gte=0,
            positionX__lte=900 - F('width') / 2,
            positionY__gte=0,
            positionY__lte=800 - F('height') / 2
        )
        boxes_layer_1.update(layer=1)

        # Layer 2: (0,800) ~ (900,1600)
        boxes_layer_2 = LoadedBoxData.objects.filter(
            positionX__gte=0,
            positionX__lte=900 - F('width') / 2,
            positionY__gte=800,
            positionY__lte=1600 - F('height') / 2
        )
        boxes_layer_2.update(layer=2)

        # Layer 3: (900,0) ~ (1800,800)
        boxes_layer_3 = LoadedBoxData.objects.filter(
            positionX__gte=900,
            positionX__lte=1800 - F('width') / 2,
            positionY__gte=0,
            positionY__lte=800 - F('height') / 2
        )
        boxes_layer_3.update(layer=3)

        # Layer 4: (900,800) ~ (1800,1600)
        boxes_layer_4 = LoadedBoxData.objects.filter(
            positionX__gte=900,
            positionX__lte=1800 - F('width') / 2,
            positionY__gte=800,
            positionY__lte=1600 - F('height') / 2
        )
        boxes_layer_4.update(layer=4)

        # Layer 5: (1800,0) ~ (2700,800)
        boxes_layer_5 = LoadedBoxData.objects.filter(
            positionX__gte=1800,
            positionX__lte=2700 - F('width') / 2,
            positionY__gte=0,
            positionY__lte=800 - F('height') / 2
        )
        boxes_layer_5.update(layer=5)

        # Layer 6: (1800,800) ~ (2700,1600)
        boxes_layer_6 = LoadedBoxData.objects.filter(
            positionX__gte=1800,
            positionX__lte=2700 - F('width') / 2,
            positionY__gte=800,
            positionY__lte=1600 - F('height') / 2
        )
        boxes_layer_6.update(layer=6)

        # 총 업데이트된 박스 수를 계산
        updated_count = sum([
            boxes_layer_1.count(),
            boxes_layer_2.count(),
            boxes_layer_3.count(),
            boxes_layer_4.count(),
            boxes_layer_5.count(),
            boxes_layer_6.count()
        ])

        return JsonResponse({"message": f"Updated {updated_count} boxes across six layers."}, status=200)
