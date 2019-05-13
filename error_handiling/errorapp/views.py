from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import employee
from errorapp.mixin import employeemixin
import json

class employeecbv(employeemixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            employeeinfo=employee.objects.get(id=id)
        except employee.DoesNotExist:
            json_data=json.dumps({"msg":"not found"})
        else:
            json_data=self.return_to_json([employeeinfo,])
        return HttpResponse(json_data,content_type='applcation/json')