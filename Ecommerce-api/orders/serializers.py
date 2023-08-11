from rest_framework import serializers
from .models import Order_Item, Order
from products.models import Product
from accounts.models import UserData

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
    product_name = serializers.StringRelatedField(source='product', read_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=False)
    order_name = serializers.StringRelatedField(source='order', read_only=True)
    
    class Meta:
        model = Order_Item
        fields = ['id', 'order', 'order_name', 'product_id', 'product_name', 'quantity', 'price', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user','user_email', 'status', 'created_at', 'order_items', 'total_quantity', 'total_price']

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_total_price(self, obj):
        return obj.total_price

    def get_user_email(self,obj):
        return str(obj.user.email)