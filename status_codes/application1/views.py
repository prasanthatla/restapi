from django.shortcuts import render
from .models import employee

# Create your views here.
from django.views import View
from application1.mixin import employeemixin
import json


class employeecbv(employeemixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            quearyset=employee.objects.get(id=id)
        except employee.DoesNotExist:
            return self.render_to_httpresponse(json.dumps({'msg':"not found"}))
        else:
            jsondata=self.render_to_json([quearyset])
            return self.render_to_httpresponse(jsondata)