from .models import Product,Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only = True, allow_null=True)
    category_name = serializers.StringRelatedField(source='category',read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image_url', 'price', 'category','category_name']




