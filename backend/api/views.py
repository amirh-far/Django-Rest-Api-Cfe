# from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF Api View
    """
    if request.method is not "POST":
        return Response({"detail": "GET is not allowed"}, status=405) 
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    # return JsonResponse({"message": "Hi there, this is your first django API response!"})
    return Response(data)