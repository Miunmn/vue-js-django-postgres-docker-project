
from django.http import JsonResponse
from django.core import serializers
import json
# from httplib2 import Response

def get_template(model):
    try:
        elements = model.objects.all().values()

    except Exception as e:
        raise e

    # print(elements)

    dataList = list(elements)


    return JsonResponse({"dataList": json.dumps(dataList)}) 

def post_template(new_entity):

    try:
        new_entity.save()
    except Exception as e:
        raise e 

    return JsonResponse({"message": "Elemento guardado!"})

def delete_template(model,  element_id):
    try:
        model.objects.get(pk=element_id).delete()
    except Exception as e:
        raise e

    return JsonResponse({"message": "Elemento Eliminado"})



