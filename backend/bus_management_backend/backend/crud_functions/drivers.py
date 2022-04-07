
from django.http import JsonResponse
from django.core import serializers


import json
from backend.models import Drivers
from backend.crud_functions.crud_function_templates import *
from httplib2 import Response

from django.http import JsonResponse



def drivers_get(request):
    return get_template(Drivers)

def drivers_post(request):

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['first_name', 'last_name', 'age']

    for field in field_list:
        if field not in body:
            raise "Missing Field"

    new_driver = Drivers(first_name=body['first_name'],
        last_name=body['last_name'], age=body['age']         
    )

    return post_template(new_driver)


def drivers_put(request):
    print(request.POST)

    return {}
def drivers_delete(request):
    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Drivers, element_id)