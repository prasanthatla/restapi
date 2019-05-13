from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from cfud.utils import is_json
from cfud.mixin import employeemixin
import json
from cfud.forms import empoyee_form
from .models import employee


@method_decorator(csrf_exempt, name='dispatch')
class employeecbv(employeemixin, View):
    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return self.render_to_Httpresponse(json.dumps({'msg': 'plzz send the data in json format only'}),
                                               statuscode=400)
        emp_data = json.loads(request.body)
        form = empoyee_form(emp_data)
        if form.is_valid():
            object = form.save(commit=True)
            return self.render_to_Httpresponse(json.dumps({'msg': 'successfully created'}), statuscode=200)
        if form.errors:
            return self.render_to_Httpresponse(json.dumps(form.errors), statuscode=400)

    def put(self, request, id, *args, **kwargs):
        obj = self.getelement_by_id(id)
        if obj is None:
            return self.render_to_Httpresponse(json.dumps({'msg': 'no record found'}), statuscode=400)
