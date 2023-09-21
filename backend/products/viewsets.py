from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer
 
class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> update
    patch -> PartialUpdate
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
