from django.http import JsonResponse
import json
import requests

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    print(request.GET)
    body = request.body
    # print(body) #  byte string of JSON data
    data = {}
    try:
        data = json.loads(body) 
    except:
        pass
    print(data.keys())
    data["headers"] = dict(request.headers)
    print(request.headers)
    data["content_type"] = request.content_type
    data["params"] = dict(request.GET)


    # return JsonResponse({"message": "Hi there, this is your first django API response!"})
    return JsonResponse(data)