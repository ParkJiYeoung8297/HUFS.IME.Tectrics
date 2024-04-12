from django.db import models

# Create your models here.
class LoadedBoxData(models.Model):
    box_code=models.TextField(max_length=15)

    width=models.IntegerField()
    height=models.IntegerField()
    depth=models.IntegerField()
    volume=models.IntegerField()
    layer = models.IntegerField()
    deliverySequence = models.IntegerField()
    loadSeuqence = models.IntegerField()
    positionX = models.IntegerField()
    positionY = models.IntegerField()
    positionZ = models.IntegerField()
    