import json

from django.core.serializers import serialize
from django.http import JsonResponse
class employeemixin(object,):
    def quearysettojson(self,qt):
        json_data = serialize('json', qt)
        pdict = json.loads(json_data)
        final_list = []
        for x in pdict:
            final_list.append(x['fields'])
        # json_data = serialize('json',final_list)
        json_data = json.dumps(final_list)
        return json_data