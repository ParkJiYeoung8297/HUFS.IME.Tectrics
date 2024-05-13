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
    loadSequence = models.IntegerField()
    positionX = models.IntegerField()
    positionY = models.IntegerField()
    positionZ = models.IntegerField()
    color   = models.TextField(max_length=15)
    layerColor = models.TextField(max_length=15,null=True, blank=True)
    