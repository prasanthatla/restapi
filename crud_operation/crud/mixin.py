from django.http  import HttpResponse
import json
from .models import employee
from django.core.serializers import serialize
class employeemixin(object):
    def render_to_httpresponse(self,json,status):
        return HttpResponse(json,status)
    def get_element_by_id(self,id):
        try:
            emp = employee.objects.get(id=id)
        except employee.DoesNotExist:
            emp=None
        return emp
    def serializersmixin(self,obj):
        json_data=serialize('json',obj)
        pdic=json.loads(json_data)
        final_dict=[]
        for x in pdic:
            final_dict.append(x['fields'])
        json_data=json.dumps(final_dict)
        return json_data