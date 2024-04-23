from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)  # For example purposes only. Use Django's built-in User model for real projects because it handles passwords securely.
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=50)  # You could use choices or a separate model if needed

    def __str__(self):
        return self.username
