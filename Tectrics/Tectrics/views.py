from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self,request):
        return render(request,"Tectrics/main.html")
    
def layer_view(request):
    # 여기에 필요한 로직을 추가하세요. 예를 들어, 데이터베이스에서 정보를 가져오거나,
    # 단순히 템플릿을 렌더링할 수 있습니다.
    return render(request, 'Load/layer.html')