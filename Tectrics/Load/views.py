from django.shortcuts import render
from networkx import is_path
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
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# class BoxLoad(APIView):
#     def get(self,request):
#         user_id=request.session['user_id']
#         context = {"user_id":user_id}
#         return render(request,"Load/boxload.html",context)

def get_box_data(request):
    boxes = LoadedBoxData.objects.all().values()
    return JsonResponse(list(boxes), safe=False)

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
                load_data = LoadedBoxData.objects.filter(box_code=box_code).values( "width", "height", "depth", 
                    "deliverySequence", "loadSequence", "layer", "positionX", "positionY", "positionZ"
                ).first()
                
                # 결합된 딕셔너리 생성
                combined_entry = {
                    "box_code": order['box_code'],
                    "name": order['name'],
                    "road_address": order['road_address'],
                    "detail_address": order['detail_address'],
                    "phone": order['phone'],
                    "width": load_data['width'] if load_data else None,
                    "height": load_data['height'] if load_data else None,
                    "depth": load_data['depth'] if load_data else None,
                    "deliverySequence": load_data['deliverySequence'] if load_data else None,
                    "loadSequence": load_data['loadSequence'] if load_data else None,
                    "layer": load_data['layer'] if load_data else None,
                    "positionX": load_data['positionX'] if load_data else None,
                    "positionY": load_data['positionY'] if load_data else None,
                    "positionZ": load_data['positionZ'] if load_data else None
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
    
class LayerLoad(APIView):
    def get(self,request):
        print('로그인한 사용자 : ',request.session['user_id'])
        user_id=request.session['user_id']
        user=User.objects.filter(user_id=user_id).values("dev_code").first()
        if user is not None:
            # dev_code를 사용하여 필터링
            dev_code = user['dev_code']
            orders2 = Order.objects.filter(delivery_man_code=dev_code).values("box_code", "name", "road_address", "detail_address", "phone")
            
            combined_list2 = []
            for order2 in orders2:
                box_code2 = order2['box_code']
                load_data2 = LoadedBoxData.objects.filter(box_code=box_code2).values(
                    "width", "height", "depth", 
                    "deliverySequence", "loadSequence", "layer", "positionX", "positionY", "positionZ"
                ).first()
                
                # 결합된 딕셔너리 생성
                combined_entry2 = {
                    "box_code": order2['box_code'],
                    "name": order2['name'],
                    "road_address": order2['road_address'],
                    "detail_address": order2['detail_address'],
                    "phone": order2['phone'],
                    "width": load_data2['width'] if load_data2 else None,
                    "height": load_data2['height'] if load_data2 else None,
                    "depth": load_data2['depth'] if load_data2 else None,
                    "deliverySequence": load_data2['deliverySequence'] if load_data2 else None,
                    "loadSequence": load_data2['loadSequence'] if load_data2 else None,
                    "layer": load_data2['layer'] if load_data2 else None,
                    "positionX": load_data2['positionX'] if load_data2 else None,
                    "positionY": load_data2['positionY'] if load_data2 else None,
                    "positionZ": load_data2['positionZ'] if load_data2 else None
                }
                combined_list2.append(combined_entry2)
            
            combined_list2 = sorted(
                combined_list2,
                key=lambda x: (x['loadSequence'] is None, x['loadSequence']),
                reverse=False
            )
        else:
            combined_list2 = []
        
        # 하나의 리스트로 병합된 결과를 템플릿에 전달
        context2 = {"combined_list2": combined_list2, "user_id": user_id}
        return render(request, "Load/layer.html", context2)
        
# def getloaddata(request):
#     boxcode = request.GET.get('boxcode')
#     if boxcode:
#         try:
#             order = Order.objects.filter(box_code=boxcode).values(
#                 'box_code', 'name', 'road_address', 'detail_address', 'phone'
#             ).first()
#             load_data = LoadedBoxData.objects.filter(box_code=boxcode).values(
#                 'deliverySequence', 'loadSequence', 'layer', 'positionX', 'positionY', 'positionZ'
#             ).first()
#             if order and load_data:
#                 data = {**order, **load_data}
#                 return JsonResponse({'data': data}, safe=False)
#             else:
#                 return JsonResponse({'error': 'No data found for provided box code'}, status=404)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'No boxcode provided'}, status=400)
def getloaddata(request):
    code = request.GET.get('boxcode', None)  # GET 요청에서 파라미터 추출
    if code:
        boxdata = list(Order.objects.filter(box_code=code).values('name','road_address','detail_address','phone'))
        boxdata2 = list(LoadedBoxData.objects.filter(box_code=code).values('deliverySequence', 'loadSequence', 'layer','positionX','positionY','positionZ' ))


        # 파일 읽기
        # with open('static/packed_items.json', 'r') as file:
        #     data = json.load(file)

        # # 데이터 수정
        #     # print(boxdata2[0])
        #     # data[0]['width']=boxdata2[0]['width']/30
        #     # data[0]['height']=boxdata2[0]['height']/30
        #     # data[0]['depth']=boxdata2[0]['length']/30

        # # 파일 쓰기
        # with open('static/packed_items.json', 'w') as file:
        #     json.dump(data, file, indent=4)
        
        return JsonResponse({'boxdata': boxdata,'boxdata2':boxdata2})  # 데이터를 JSON 형식으로 반환
    else:
        return JsonResponse({'error': 'No code provided'}, status=400)
        
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

# 메인함수 실행 버튼 클릭 시 실행
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

# 레이어 입력 버튼 클릭 시 실행            
def layer(request):
        layer_colors = {
            1: 'red',    # 레이어 1: 빨강
            2: 'blue',   # 레이어 2: 파랑
            3: 'green',  # 레이어 3: 초록
            4: 'yellow', # 레이어 4: 노랑
            5: 'purple', # 레이어 5: 보라
            6: 'orange'  # 레이어 6: 오렌지 
        }
        # Layer 1: (0,0) ~ (900,800)
        boxes = LoadedBoxData.objects.all()
        boxes_data = []
    # 각 박스를 반복하면서 중심점을 기준으로 레이어 할당
        for box in boxes:
            center_x = box.positionX + box.width / 2
            center_y = box.positionY + box.height / 2

        # 중심점을 기준으로 레이어 결정
            if 0 <= center_x < 900:
                if 0 <= center_y < 800:
                    layer = 1
                elif 800 <= center_y < 1600:
                    layer = 2
            elif 900 <= center_x < 1800:
                if 0 <= center_y < 800:
                    layer = 3
                elif 800 <= center_y < 1600:
                    layer = 4
            elif 1800 <= center_x < 2700:
                if 0 <= center_y < 800:
                    layer = 5
                elif 800 <= center_y < 1600:
                    layer = 6
            
            # 레이어 및 색상 업데이트
            box.layer = layer
            box.layerColor = layer_colors[layer]
            box.save()

    # 총 업데이트된 박스 수 반환
            boxes_data.append({
                "id": box.id,
                "positionX": box.positionX,
                "positionY": box.positionY,
                "positionZ": box.positionZ,
                "width": box.width,
                "height": box.height,
                "depth": box.depth,
                "layer": box.layer,
                "layerColor": box.layerColor
            })

        # 파일로 저장
        
        if settings.STATIC_ROOT:
            file_path = os.path.join(settings.STATIC_ROOT, 'packed_boxes_layer.json')
        else:
                # STATIC_ROOT가 설정되어 있지 않은 경우 대체 경로 사용
                file_path = os.path.join(settings.BASE_DIR, 'static', 'packed_boxes_layer.json')

            # 파일로 저장
        with open(file_path, 'w') as json_file:
            json.dump(boxes_data, json_file, indent=4)

        updated_count = len(boxes)
        return JsonResponse({"message": f"Updated {updated_count} boxes across six layers, data saved to {file_path}."}, status=200)

def layer_view(request):
    return render(request, 'Load/layer.html')

# 표의 행 클릭스 행 정보 json 파일로 생성하여 static 폴더에 저장
def save_row_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        with open('static/saved_data.json', 'w') as f:
            json.dump(data, f)
        return JsonResponse({'status': 'success', 'message': 'Data saved successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)