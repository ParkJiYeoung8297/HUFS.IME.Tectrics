from rest_framework.response import Response
from rest_framework.decorators import api_view
from Order.models import BoxData
from .serializers import BoxSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from Order.models import Order
from .serializers import AddressSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')


@api_view(['GET', 'PATCH'])
def BoxApi(request, box_code=None):
    if request.method == 'GET':
        if box_code:
            #box_code로 호출하면 해당 박스의 정보 출력
            box = get_object_or_404(BoxData, box_code=box_code)
            serializer = BoxSerializer(box)
            return Response(serializer.data)
        else: 
            #box_code 입력 없으면 전체 리스트 출력
            Boxs = BoxData.objects.all()
            serializer = BoxSerializer(Boxs, many=True)
            return Response(serializer.data)

    elif request.method == 'PATCH':
        box = get_object_or_404(BoxData, box_code=box_code)
        serializer = BoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PATCH'])
def AddressApi(request, box_code=None):
    if request.method == 'GET':
        if box_code:
            #box_code로 호출하면 해당 박스의 정보 출력
            box = get_object_or_404(Order, box_code=box_code)
            serializer = AddressSerializer(box)
            return Response(serializer.data)
        else: 
            #box_code 입력 없으면 전체 리스트 출력
            Boxs = Order.objects.all()
            serializer = AddressSerializer(Boxs, many=True)
            return Response(serializer.data)

    elif request.method == 'PATCH':
        box = get_object_or_404(Order, box_code=box_code)
        serializer = AddressSerializer(box, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)