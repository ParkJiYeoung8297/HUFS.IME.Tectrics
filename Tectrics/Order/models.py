from django.db import models

# Create your models here.
# 주문
class Order(models.Model):
    box_code=models.TextField(primary_key=True)
    delivery_man_code = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    road_address=models.TextField(max_length=100)
    detail_address=models.TextField(max_length=100)
    phone=models.TextField(max_length=5)
    date=models.DateField()

# 박스 정보
class BoxData(models.Model):
    box_code=models.TextField(max_length=15)
    latitude=models.IntegerField(null=True)
    longitude=models.IntegerField()
    length=models.IntegerField()
    width=models.IntegerField()
    height=models.IntegerField()
    volume=models.IntegerField()