from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk" the deafult look up field is pk no need to declare it.