from nis import cat
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

#CRUD Functions 
from backend.crud_functions.buses import *
from backend.crud_functions.journeys import *
from backend.crud_functions.passengers import *
from backend.crud_functions.drivers import *


def crud_template(request, switcher):

    response_data = {}

    funct = switcher.get(request.method, response_data)

    try:
        response_data = funct(request)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Error al consultar db")

    return response_data


@require_http_methods(["GET", "PUT", "DELETE", "POST"])
@csrf_exempt
def buses_crud(request):
    print("request.method", request.method)

    switcher = {
        'POST': buses_post,
        'GET': buses_get,
        'PUT': buses_put,
        'DELETE': buses_delete
    }

    return crud_template(request=request, switcher=switcher)


@require_http_methods(["GET", "PUT", "DELETE", "POST"])
@csrf_exempt
def journeys_crud(request):
    print("request.method", request.method)

    switcher = {
        'POST': journeys_post,
        'GET': journeys_get,
        'PUT': journeys_put,
        'DELETE': journeys_delete
    }
    return crud_template(request=request, switcher=switcher)


@require_http_methods(["GET", "PUT", "DELETE", "POST"])
@csrf_exempt
def passengers_crud(request):
    print("request.method", request.method)

    switcher = {
        'POST': passengers_post,
        'GET': passengers_get,
        'PUT': passengers_put,
        'DELETE': passengers_delete
    }

    return crud_template(request=request, switcher=switcher)


@require_http_methods(["GET", "PUT", "DELETE", "POST"])
@csrf_exempt
def drivers_crud(request):

    print("request.method", request.method)
    switcher = {
        'POST': drivers_post,
        'GET': drivers_get,
        'PUT': drivers_put,
        'DELETE': drivers_delete
    }

    return crud_template(request=request, switcher=switcher)


@require_http_methods(["GET"])
@csrf_exempt
def filter_buses_from_journeys(request):
    try:
        response = journeys_buses_filter(request)
    except Exception as e:
        print(e)
        HttpResponseBadRequest("Error al filtrar buses")

    return response
