from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)  # Provide a default value
    postal_code = models.CharField(max_length=20, default='00000')  # Default value provided here

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} - {self.postal_code}"
