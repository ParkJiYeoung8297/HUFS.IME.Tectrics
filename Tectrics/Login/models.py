from django.db import models

# Create your models here.
class User(models.Model):

    dev_name = models.CharField(max_length=24)
    dev_phone = models.IntegerField()
    user_id = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=24, unique=True)
    dev_ok = models.BinaryField()
    work_ok = models.BinaryField()
