import json
from django.core.serializers import serialize
from django.http import HttpResponse
class employeemixin(object):
    def render_to_json(self,qs,*args,**kwargs):
        jsondata=serialize('json',qs)
        pdict=json.loads(jsondata)
        finallist=[]
        for x in pdict:
            finallist.append(x['fields'])
        jsondata=json.dumps(finallist)
        return jsondata
    def render_to_httpresponse(self,jsondata,*args,**kwargs):
        return HttpResponse(jsondata,content_type='application/json')

