from django.db import models
from products.models import Product
from accounts.models import UserData

ORDERED = "OR"
DELIVERED = "DE"
TRANSIT = 'TE'
CANCELED = 'CA'

ORDER_CHOICES=[
    (ORDERED,"Ordered"),
    (DELIVERED,'Delivered'),
    (TRANSIT,'In-Transit'),
    (CANCELED,'Canceled')
]
class Order(models.Model):
    
    user = models.ForeignKey(UserData,on_delete=models.CASCADE)
    status = models.CharField(max_length=2,choices=ORDER_CHOICES,default=ORDERED)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        orders = Order_Item.objects.filter(order = self)
        price = 0
        for item in orders:
            price += item.price
        return price
    
    @property
    def total_quantity(self):
        orders = Order_Item.objects.filter(order = self)
        quantity = 0
        for item in orders:
            quantity += item.quantity
        return quantity
    
    def __str__(self) -> str:
        return f"{self.user.name} {self.id}"



class Order_Item(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderitem_set')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return str(self.product)