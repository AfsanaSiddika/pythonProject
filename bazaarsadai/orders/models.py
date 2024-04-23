from django.db import models

# Create your models here.
class Orde(models.Model):
    productId = models.IntegerField
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shopName = models.TextField(max_length=100)

    def __str__(self):
        return self.name,self.price,self.shopName
