


from django.http import HttpResponseBadRequest, JsonResponse
from backend.models import Buses, Passengers, Journeys
from backend.crud_functions.crud_function_templates import *

def passengers_get(request):
    try:
        elements = Passengers.objects.all().values()
    except Exception as e:
        raise e

    # print(elements)

    dataList = list(elements)


    for i in range(len(dataList)):
        try:
            journey = Journeys.objects.filter(journey_id=dataList[i].get('journey_id')).values_list('journey_name',flat=True)
            bus = Buses.objects.filter(bus_id=dataList[i].get('bus_id')).values_list('plate',flat=True)
        except Exception as e:
            raise e

        bus = list(bus)[0]
        journey = list(journey)[0]
        dataList[i]['bus_plate']=bus
        dataList[i]['journey_name']=journey

    # print(dataList)


    return JsonResponse({"dataList": json.dumps(dataList)})



def passengers_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['first_name', 'last_name', 'assigned_journey']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""

    print(body)
    try:
        journey = Journeys.objects.get(journey_id=body['assigned_journey'])
        bus = Buses.objects.get(bus_id=body['bus'])

    except Exception as e:
        print(e)
        raise e

    current_passengers = Passengers.objects.filter(bus_id=bus.bus_id).count()

    print(bus.capacity, current_passengers)
    if bus.capacity == current_passengers:
        return HttpResponseBadRequest("No se pudo registrar al pasajero porque la cantidad maxima ya ha sido alcanzada")


    new_passenger = Passengers(first_name=body['first_name'], last_name=body['last_name'], journey=journey, bus=bus)
    
    
    return post_template(new_passenger)

def passengers_put(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    # print(body)

    try: 
        passenger = Passengers.objects.get(pk=body['passenger_id'])
    except Exception as e:
        raise e

    passenger.first_name = body['first_name'] if body['first_name'] else passenger.first_name
    passenger.last_name = body['last_name'] if body['last_name'] else passenger.last_name

    try:
        journey = Journeys.objects.get(pk=body['assigned_journey'])
        bus = Buses.objects.get(pk=body['bus'])
    except Exception as e:
        print(e)
        raise e
    passenger.journey = journey
    passenger.bus = bus


    return JsonResponse({"mensaje": "Pasajero actualizado!"})

def passengers_delete(request):
    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"
    
    return delete_template(Passengers, element_id)
