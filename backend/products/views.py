from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(UserQuerySetMixin, # Note that its important to inherit from this class first.
                               StaffEditorPermissionMixin,
                               generics.ListCreateAPIView,
                               ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # print(serializer.data)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)

class ProductDetailAPIView(UserQuerySetMixin,
                           StaffEditorPermissionMixin,
                            generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk" the deafult look up field is pk no need to declare it.

class ProductUpdateAPIView(UserQuerySetMixin,
                           StaffEditorPermissionMixin,
                            generics.UpdateAPIView,
                            ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk" the deafult look up field is pk no need to declare it.
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        # print(serializer.data)


class ProductDeleteAPIView(UserQuerySetMixin,
                           StaffEditorPermissionMixin,
                           generics.DestroyAPIView,
                           ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk" the deafult look up field is pk no need to declare it.
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        # print(args, kwargs)
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.destroy(self, *args, **kwargs)
    



@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):

    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)    
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            # print(serializer.data)
            return Response(serializer.data)
