from django.db import models
from users.models import User  # Import User model from users app
from addresses.models import Address  # Import the Address model if needed

class Shop(models.Model):
    shopId = models.AutoField(primary_key=True)  # Auto-incrementing primary key for the shop
    name = models.CharField(max_length=100)  # Name of the shop
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Owner of the shop
    address = models.OneToOneField(Address, on_delete=models.CASCADE)   # Use ForeignKey for address

    def __str__(self):
        return self.name
