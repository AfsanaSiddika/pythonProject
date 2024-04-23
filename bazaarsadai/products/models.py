# models.py (products app)

from django.db import models
from users.models import User  # Import the User model



class Product(models.Model):
    # Ensure productId is not nullable and provide a default value
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE)

    def create_listing(self):
        pass

    def update_listing(self):
        pass

    def delete_listing(self):
        pass

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.shop.name}"
