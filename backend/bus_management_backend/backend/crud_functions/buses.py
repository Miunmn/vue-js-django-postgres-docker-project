from httplib2 import Response

from django.http import JsonResponse
from backend.models import Buses
from backend.crud_functions.crud_function_templates import *



def buses_get(request):
    return get_template(Buses)

def buses_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['plate', 'years_of_service']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""

    new_bus = Buses(plate=body['plate'], years_of_service=body['years_of_service'])

    return post_template(new_bus)

def buses_put():
    pass

def buses_delete(request):

    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Buses, element_id)
