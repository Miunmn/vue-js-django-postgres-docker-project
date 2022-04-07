
from httplib2 import Response

from django.http import JsonResponse
from backend.models import Passengers, Journeys
from backend.crud_functions.crud_function_templates import *

def passengers_get(request):
    return get_template(Passengers)

def passengers_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['first_name', 'last_name', 'assigned_journey']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""

    journey = Journeys.objects.get(journey_id=body['assigned_journey'])

    new_passenger = Passengers(first_name=body['first_name'], last_name=body['last_name'], assigned_journey=journey)

    return post_template(new_passenger)

def passengers_put():
    pass

def passengers_delete(request):
    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Passengers, element_id)
