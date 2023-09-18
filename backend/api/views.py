from django.http import JsonResponse
import json
import requests
from products.models import Product
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price

    # return JsonResponse({"message": "Hi there, this is your first django API response!"})
    return JsonResponse(data)