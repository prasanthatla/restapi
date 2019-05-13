from django.http import HttpResponse

from cfud.models import employee


class employeemixin(object):
    def render_to_Httpresponse(self,json,statuscode):
        return HttpResponse(json,statuscode)
    def getelement_by_id(self, id):
        try:
            emp = employee.objects.get(id=id)
        except employee.DoesNotExist:
            emp = None
        return emp