from django.shortcuts import render
from django.views import View
from .models import employee
from django.core.serializers import serialize,deserialize
from django.http import JsonResponse, HttpResponse
import json
from app1.mixin import employeemixin


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


class employeecbv2(View):
    def get(self, request, *args, **kwargs):
        quearyset = employee.objects.all()
        json_data = serialize('json', quearyset, fields=('eno', 'ename', 'esal'))
        return HttpResponse(json_data, content_type='application/Json')


class employeecbv3(View):
    def get(self, request, *args, **kwargs):
        quearyset = employee.objects.all()
        json_data = serialize('json', quearyset)
        pdict = json.loads(json_data)
        final_list = []
        for x in pdict:
            final_list.append(x['fields'])
        # json_data = deserialize('json',final_list)
        json_data=json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/Json')

class employeecbv4(employeemixin , View):
    def get(self, request, *args, **kwargs):
        qt = employee.objects.all()

        json_data = self.quearysettojson(qt)
        return HttpResponse(json_data, content_type='application/Json')
