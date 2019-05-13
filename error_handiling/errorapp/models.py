from django.db import models

# Create your models here.
class employee(models.Model):
    eno=models.CharField(max_length=50)
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=50)
