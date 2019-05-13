from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

class jsoncbv(View):
    def get(self,request):
        emp_data={"en":100,"ename":"kittu loves pravallika"}
        return JsonResponse(emp_data)
