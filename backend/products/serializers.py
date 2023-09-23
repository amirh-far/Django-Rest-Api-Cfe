from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

# class UserProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(view_name="product-detail",
#                                                 lookup_field="pk", read_only=True)
#     title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                               validators.unique_product_title])
    body = serializers.CharField(source="content")


    class Meta:
        model = Product
        fields = [
            "owner",
            "pk", 
            "title",
            # "content",
            "body",
            "price",
            "sale_price",
            "public",
            "path",
            "endpoint",
        ]


    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     qs = Product.objects.filter(user=request.user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance, validated_data)

    # def get_edit_url(self, obj):
    #     request = self.context.get("request")
    #     if request is None:
    #         return None
    #     return reverse("product-edit-detail", kwargs={"pk": obj.pk},  request=request)
