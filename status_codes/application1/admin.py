from django.contrib import admin
from .models import employee


class employeeadmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eadd']


admin.site.register(employee, employeeadmin)

