from django.shortcuts import render
from rest_framework.views import APIView
from Order.models import Order

class BoxList(APIView):
    def get(self,request):
        order_list=Order.objects.values("box_code","name","road_address","detail_address","phone")
        context={"order_list":order_list}
        return render(request,"Box/boxlist.html",context)
    
