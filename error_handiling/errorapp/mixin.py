from django.core.serializers import serialize
import json

class employeemixin(object):
    def return_to_json(self,qs):
        json_data=serialize('json',qs)
        pdict=json.loads(json_data)
        final_list=[]
        for x in pdict:
            final_list.append(x['fields'])
        json_data=json.dumps(final_list)
        return json_data
