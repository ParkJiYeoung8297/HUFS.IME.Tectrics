from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order
from Order.models import BoxData
from Login.models import User
from django.http import JsonResponse
import json
from django.http import HttpResponse

class BoxList(APIView):
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
        return render(request,"Box/boxlist.html",context)
    
def getbox(request):
    code = request.GET.get('boxcode', None)  # GET 요청에서 파라미터 추출
    if code:
        boxdata = list(Order.objects.filter(box_code=code).values('name','road_address','detail_address','phone'))
        boxdata2 = list(BoxData.objects.filter(box_code=code).values('length', 'width', 'height'))


        # 파일 읽기
        with open('static/packed_items2.json', 'r') as file:
            data = json.load(file)

        # 데이터 수정
            print(boxdata2[0])
            data[0]['width']=boxdata2[0]['width']/30
            data[0]['height']=boxdata2[0]['height']/30
            data[0]['depth']=boxdata2[0]['length']/30

        # 파일 쓰기
        with open('static/packed_items2.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        return JsonResponse({'boxdata': boxdata,'boxdata2':boxdata2})  # 데이터를 JSON 형식으로 반환
    else:
        return JsonResponse({'error': 'No code provided'}, status=400)
