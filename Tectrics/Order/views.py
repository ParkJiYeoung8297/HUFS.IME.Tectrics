from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Order
from .models import BoxData
from Login.models import User
from datetime import date


# Create your views here.

class its(APIView):
    def get (self,request):
        tmap_key = open("TmapRestKey.txt", "r").read()
        address_list = Order.objects.values("road_address", "detail_address")
        context = {"address_list": address_list,'tmap_key': tmap_key}
        return render(request,"Order/itsdata.html",context)
    
    def patch (self,request):
        r_address=request.data.get('road_address',None)
        d_address=request.data.get('detail_address',None)
        lat=request.data.get('latitude',None)
        lon=request.data.get('longitude',None)
        lat2=request.data.get('latitude2',None)
        lon2=request.data.get('longitude2',None)
        orders=Order.objects.filter(road_address=r_address,detail_address=d_address)
        
        if not orders.exists():
            return JsonResponse(status=400, data={"message": "해당 주소가 없습니다."})
        
        for order in orders:
            # BoxData 쿼리셋에서 각 객체를 업데이트합니다.
            BoxData.objects.filter(box_code=order.box_code).update(latitude=lat, longitude=lon,latitude2=lat2, longitude2=lon2)

        return JsonResponse({"message": "성공적으로 업데이트되었습니다."})
    





    
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        user=User.objects.filter(dev_ok=1,work_ok=0).first()
        dev_code=user.dev_code

        excel_file = request.FILES['file']
        
        # pandas를 사용하여 엑셀 파일 읽기
        df = pd.read_excel(excel_file)
        
        # DataFrame의 각 행을 데이터베이스에 저장
        for _, row in df.iterrows():
            Order.objects.create(box_code=row['송장코드'],delivery_man_code=dev_code ,name=row['고객명'],road_address=row['도로명 주소'],
                                  detail_address=row['상세 주소'],phone=row['전화번호'],date=date.today())
            BoxData.objects.create(box_code=row['송장코드'],latitude=0,longitude=0,length=row['길이'],width=row['너비'],height=row['높이'],sequence=0)
        dev=User.objects.filter(dev_code=dev_code)
        dev.update(work_ok=1)
        return JsonResponse({'message': 'File successfully uploaded and data stored in DB'})
    else:
        return JsonResponse({'message': 'Please upload a valid excel file.'}, status=400)

            

    