from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import employee
from django.http import JsonResponse


class employeecbv(View):
    def get(self, request, *args, **kwargs):
        emp = employee.objects.get(id=2)
        data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }
        return JsonResponse(data)


class employeecbv1(View):
    def get(self, request, id, *args, **kwargs):
        emp = employee.objects.get(id=id)
        data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }
        return JsonResponse(data)