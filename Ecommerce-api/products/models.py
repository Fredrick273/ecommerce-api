from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.IntegerField(null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
