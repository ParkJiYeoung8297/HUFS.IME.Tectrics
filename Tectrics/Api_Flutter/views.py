from rest_framework.response import Response
from rest_framework.decorators import api_view
from Order.models import BoxData
from .serializers import BoxSerializer


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')


@api_view(['GET'])
def BoxApi(request):
    Boxs=BoxData.objects.all()
    totalBoxs=list(Boxs)
    serializer=BoxSerializer(totalBoxs, many=True)
    return Response(serializer.data)