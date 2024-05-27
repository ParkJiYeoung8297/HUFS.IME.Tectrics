from rest_framework import serializers
from Order.models import BoxData
from Order.models import Order

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=BoxData
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'