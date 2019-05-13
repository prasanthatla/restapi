from django.shortcuts import render
from django.views import View
from crud.utils import is_json
from crud.mixin import employeemixin
import json
from .models import employee
from crud.forms import employee_form
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class employeecbv(employeemixin,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_httpresponse(json.dumps({'msg':'please send the data in json format only'}),status=400)
        data = json.loads(request.body)
        id = data.get('id',None)
        if id is not None:
            obj=self.get_element_by_id(id)
            if obj is None:
                return self.render_to_httpresponse(json.dumps({'msg': 'no matched data found '}),
                                                   status=400)
            json_data=self.serializersmixin([obj,])
            return self.render_to_httpresponse(json_data,status=200)
        qs=employee.objects.all()
        json_data=self.serializersmixin(qs)
        return self.render_to_httpresponse(json_data, status=200)
    def post(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_httpresponse(json.dumps({'msg':'please send the data in json format only'}),status=400)
        data = json.loads(request.body)
        form=employee_form(data)
        if form.is_valid():
            obj=form.save(commit=True)
            return self.render_to_httpresponse(json.dumps({'msg':'successfully created'}),status=200)
        if form.errors:
            return self.render_to_httpresponse(json.dumps(form.errors),status=400)

    def put(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            return self.render_to_httpresponse(json.dumps({'msg': 'please send the data in json format only'}),
                                               status=400)
        data = json.loads(request.body)
        id = data.get('id', None)
        if id is  None:
            return self.render_to_httpresponse(json.dumps({'msg':'to perform update operation id is mandatory'}),status=200)
        obj = self.get_element_by_id(id)
        if obj is None:
            json_data=json.dumps({'msg':'No matched record found, Not possible to perform updataion'})
            return self.render_to_http_response(json_data,status=404)
        new_data=data
        old_data={
            'eno':obj.eno,
            'ename':obj.ename,
            'esal':obj.esal,
            'eaddr':obj.eaddr
        }
        old_data.update(new_data)
        form=employee_form(old_data,instance=obj)
        if form.is_valid():
            obj=form.save(commit=True)
            return self.render_to_httpresponse(json.dumps({'msg':'successfully updated'}),status=200)
        if form.errors:
            return self.render_to_httpresponse(json.dumps(form.errors),status=400)
    def delete(self,request,*args,**kwargs):
        data = request.body
        if not is_json(data):
            return self.render_to_httpresponse(json.dumps({'msg': 'please send the data in json format only'}),
                                               status=400)
        data = json.loads(request.body)
        id = data.get('id', None)
        if id is  None:
            return self.render_to_httpresponse(json.dumps({'msg': 'to perform delete operation id is mandatory'}),
                                               status=400)
        obj=self.get_element_by_id(id)
        if obj is None:
            return self.render_to_httpresponse(json.dumps({'msg':'no matched record found '}),status=400)
        status,deleted_item=obj.delete()
        if status==1:
            return self.render_to_httpresponse(json.dumps({'msg':'succesfully deleted'}),status=200)
        json_data = json.dumps({'msg': 'unable to delete ...plz try again'})
        return self.render_to_http_response(json_data, status=500)







