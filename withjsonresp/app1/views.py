from django.shortcuts import render
from django.http import JsonResponse

def employee_data_view(request):
    employee_data={"eno":100,"ename":"prasanth"}
    return JsonResponse(employee_data)