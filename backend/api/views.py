from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF Api View
    """

    serializer = ProductSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        # Just like this code : instance = form.save()
        print(instance)
        return Response(serializer.data)

    # return JsonResponse({"message": "Hi there, this is your first django API response!"})
