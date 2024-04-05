from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order
from Order.models import BoxData
from django.http import JsonResponse

class BoxList(APIView):
    def get(self,request):
        order_list=Order.objects.values("box_code","name","road_address","detail_address","phone")
        context={"order_list":order_list}
        return render(request,"Box/boxlist.html",context)
    
def getbox(request):
    code = request.GET.get('boxcode', None)  # GET 요청에서 파라미터 추출
    if code:
        boxdata = list(BoxData.objects.filter(box_code=code).values('length', 'width', 'height'))
        return JsonResponse({'boxdata': boxdata})  # 데이터를 JSON 형식으로 반환
    else:
        return JsonResponse({'error': 'No code provided'}, status=400)
        
