from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Order
from .models import BoxData
from datetime import date


# Create your views here.

class its(APIView):
    def get (self,request):
        return render(request,"Order/itsdata.html")
    
#@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        
        # pandas를 사용하여 엑셀 파일 읽기
        df = pd.read_excel(excel_file)
        
        # DataFrame의 각 행을 데이터베이스에 저장
        for _, row in df.iterrows():
            Order.objects.create(box_code=row['송장코드'],delivery_man_code=42739 ,name=row['고객명'],road_address=row['도로명 주소'],
                                  detail_address=row['상세 주소'],phone=row['전화번호'],date=date.today())
            BoxData.objects.create(box_code=row['송장코드'],latitude=0,longitude=0,length=row['길이'],width=row['너비'],height=row['높이'],volume=0)
        
        return JsonResponse({'message': 'File successfully uploaded and data stored in DB'})
    else:
        return JsonResponse({'message': 'Please upload a valid excel file.'}, status=400)
    