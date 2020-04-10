from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import json

from .models import json_table


def index(request):
    param = {'name': 'raj', 'address': 'New Railway Colony', 'age': 24}
    param_json = json.dumps(param)
    obj = json_table(name='Rocky', json_item=param_json)
    obj.save()
    return render(request, 'index.html', {'param': param})

# Single Dictionary
def json_data(request):
    obj = json_table.objects.get(Q(name='Rocky'))
    param_dict = {}
    param_dict[0] = obj.name
    param_dict[1] = json.loads(obj.json_item)

    # 2d dictionary
    param_2d = dict()
    param_2d[0] = param_dict
    print(param_2d[0][1])

    #convert 2d dictionary into JSON
    json_2d = json.dumps(param_2d)
    print(json_2d)

    return render(request, 'index.html', {'param': param_dict, 'param2d': param_2d, 'json_2d': json_2d})
