from math import floor
from django.http import JsonResponse
from backend.models import Journeys, Buses, Passengers
from backend.crud_functions.crud_function_templates import *
from django.http import HttpResponseBadRequest



def journeys_get(request):
    journey_id_val = request.GET.get('element_id')
    try:
        if journey_id_val:
            journeys = Journeys.objects.filter(pk=journey_id_val).all() 
        else: 
            journeys = Journeys.objects.all()
    except Exception as e:
        raise e

    try:
        passengers = Passengers.objects.values("journey")
    except Exception as e:
        raise e 

    listOfJourneys = list(journeys.values())

    for journey in listOfJourneys:
        journey_id = journey['journey_id'] 
        
        journeyModelObject = journeys.get(pk=journey_id)

        busList =  list(journeyModelObject.buses.all().values())

        cant_passengers = 0
        for bus in busList:
            bus_passengers = passengers.filter(bus_id=bus.get('bus_id')).count()
            bus['number_passengers'] = bus_passengers
            cant_passengers += bus_passengers



        
        journey['buses'] = busList
        
        cant_buses = len(busList)


        journey['date']=journey['date'].strftime("%Y %m %d %H:%m")
        journey['passengers'] = floor(cant_passengers/cant_buses)

    return JsonResponse({"dataList": json.dumps(listOfJourneys)}) 


def journeys_post(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    
    field_list = ['journey_name', 'busList', 'from_city', 'to_city', 'date']

    for field in field_list:
        if field not in body:
            raise f"""Missing field {field}"""

    new_journey = Journeys(
        journey_name=body['journey_name'], from_city=body['from_city'], to_city=body['to_city'], date=body['date']
    )

    response = post_template(new_journey)

    try:
        for bus_ in body['busList']:
            bus = Buses.objects.get(bus_id=bus_.get('bus_id'))
            new_journey.buses.add(bus)
    except Exception as e:
        raise e

    return response

def journeys_put():
    pass

def journeys_delete(request):
    element_id = request.GET.get('element_id')
    if element_id is None:
        raise "Falta element id"

    return delete_template(Journeys, element_id)


def journeys_buses_filter(request):
    percentage = float(request.GET.get('percentage'))
    journey_id = int(request.GET.get('journey_id'))
    if (0.0 > percentage or percentage > 100.0):  
        return HttpResponseBadRequest("Valores ingresados incorrectos")

    try:
        journey = Journeys.objects.get(pk=journey_id)
        buses = journey.buses.all()


    except Exception as e:
        raise e

    if buses.count() == 0:
        return HttpResponseBadRequest("No hay buses con ese journey id")
    
    print(list(buses))

    buses_response =  []

    for bus in buses:
        cantidad_pasajeros = Passengers.objects.filter(bus_id=bus.bus_id).count()
        capacity = bus.capacity

        try:
            capacity = Buses.objects.get(pk=bus.bus_id).capacity
        except Exception as e:
            raise e


        real_percentage = (100 * cantidad_pasajeros)/capacity 

        if float(real_percentage) >= percentage:
            bus_obj = {
                'bus_id': bus.bus_id,
                'plate': bus.plate,
                'capacity': bus.capacity,
                'years_of_service': bus.years_of_service,
                'passengers': cantidad_pasajeros,
            }
            buses_response.append(bus_obj)

    dataList = list(buses_response)
    
    return JsonResponse({"dataList": json.dumps(dataList)})

