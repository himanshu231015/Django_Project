from django.db import models

# Create your models here.
class Registration(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    esalr=models.FloatField()
    eadd=models.CharField(max_length=30)
    unm=models.CharField(max_length=30)
    pw=models.CharField(max_length=30)