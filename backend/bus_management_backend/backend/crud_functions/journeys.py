
from sre_constants import JUMP
from httplib2 import Response

from django.http import JsonResponse
from backend.models import Journeys, Drivers, Buses
from backend.crud_functions.crud_function_templates import *


def journeys_get(request):
    try:
        elements = Journeys.objects.all().values()

    except Exception as e:
        raise e

    print(elements)

    dataList = list(elements)

    for element in dataList:
        element['date']=element['date'].strftime("%Y %m %d %H:%m")


    return JsonResponse({"dataList": json.dumps(dataList)}) 


def journeys_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['journey_name', 'assigned_bus', 'from_city', 'to_city', 'assigned_driver', 'date']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""


    print(body)

    driver = Drivers.objects.get(driver_id=body['assigned_driver'])
    bus = Buses.objects.get(bus_id=body['assigned_bus'])

    new_journey = Journeys(
        journey_name=body['journey_name'], assigned_driver=driver, assigned_bus=bus,
        from_city=body['from_city'], to_city=body['to_city'], date=body['date']
    )

    return post_template(new_journey)

def journeys_put():
    pass

def journeys_delete():
    pass
