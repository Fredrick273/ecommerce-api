from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id','name','description','image_url','price']