# from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF Api View
    """
    # if request.method is not "POST":
    #     return Response({"detail": "GET is not allowed"}, status=405) 
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=["id", "title", "price"])
        data = ProductSerializer(instance).data


    return Response(data)




    # return JsonResponse({"message": "Hi there, this is your first django API response!"})
