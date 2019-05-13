from django.contrib import admin

# Register your models here.
from .models import employee

class employeeadmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

admin.site.register(employee,employeeadmin)