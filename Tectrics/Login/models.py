from django.db import models

# Create your models here.
class User(models.Model):
    dev_code = models.AutoField(primary_key=True)
    dev_name = models.CharField(max_length=24)
    dev_phone = models.CharField(max_length=12)
    user_id = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=24, unique=True)
    dev_ok = models.IntegerField()
    work_ok = models.IntegerField()
