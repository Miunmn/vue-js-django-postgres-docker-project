from httplib2 import Response

from django.http import JsonResponse
from backend.models import Buses, Drivers, Journeys
from backend.crud_functions.crud_function_templates import *


def buses_get(request):
    available_buses = request.GET.get('available')

    try:
        if available_buses:
            black_list = []
            journeys_ = Journeys.objects.all()
            for journey_ in journeys_:
                id_list = list(journey_.buses.values_list('bus_id', flat=True))
                black_list += id_list

            # print(black_list)
            elements = Buses.objects.exclude(bus_id__in=black_list).all()
        else:
            elements = Buses.objects.all()
    except Exception as e:
        raise e

    # print(elements)
    dataList = list(elements.values())

    for bus in elements:
        # print(bus)
        driver = f"""{bus.driver.first_name } {bus.driver.last_name}"""
        for bus_ in dataList:
            if bus.bus_id == bus_.get('bus_id'):
                bus_['driver'] = driver


    return JsonResponse({"dataList": json.dumps(dataList)}) 

def buses_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['plate', 'years_of_service', 'driver', 'capacity']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""

    try:
        driver = Drivers.objects.get(driver_id=body['driver'])
    except Exception as e:
        raise e

    new_bus = Buses(plate=body['plate'], driver= driver , capacity=body['capacity'], years_of_service=body['years_of_service'])


    response = post_template(new_bus)


    return response

def buses_put(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    try: 
        bus = Buses.objects.get(plate=body['plate'])
    except Exception as e:
        raise e


    bus.capacity = body['capacity'] if body['capacity'] else bus.capacity
    bus.plate = body['plate'] if body['plate'] else bus.capacity
    bus.years_of_service = body['years_of_service'] if body['years_of_service'] else bus.years_of_service
    bus.driver_id = body['driver'] if body['driver'] else bus.driver_id

    bus.save()

    
    return JsonResponse({"data": "Bus actualizado!"})

def buses_delete(request):

    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Buses, element_id)
