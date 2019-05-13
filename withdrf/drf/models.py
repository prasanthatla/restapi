from django.db import models

class employee(models.Model):
    eno=models.CharField(max_length=50)
    ename=models.CharField(max_length=50)
    eaddr=models.CharField(max_length=50)
    esal= models.FloatField()
