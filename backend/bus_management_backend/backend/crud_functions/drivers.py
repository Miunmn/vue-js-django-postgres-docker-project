
from django.http import JsonResponse
from django.core import serializers


import json
from backend.models import Drivers,Buses
from backend.crud_functions.crud_function_templates import *
from httplib2 import Response

from django.http import JsonResponse



def drivers_get(request):
    available_drivers = request.GET.get('available')

    try:
        if available_drivers:
            buses = Buses.objects.values_list('driver_id', flat=True)
            elements = Drivers.objects.exclude(driver_id__in=buses).all().values()

        else:
            elements = Drivers.objects.values()

    except Exception as e:
        raise e



    dataList = list(elements)


    return JsonResponse({"dataList": json.dumps(dataList)})


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
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    try: 
        driver = Drivers.objects.get(driver_id=body['driver_id'])
    except Exception as e:
        raise e


    driver.first_name = body['first_name'] if body['first_name'] else driver.first_name
    driver.last_name = body['last_name'] if body['last_name'] else driver.last_name
    driver.age = body['age'] if body['age'] else driver.age

    driver.save()

    
    return JsonResponse({"mensaje": "Driver actualizado!"})

    
def drivers_delete(request):
    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Drivers, element_id)