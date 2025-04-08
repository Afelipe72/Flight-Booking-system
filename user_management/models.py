from django.db import models
# Create your models here.
from django.db import models
# for the custom user we have to inherit from the AbstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Email must be unique
    identification = models.BigIntegerField(unique=True) # Identification must be unique
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    
    # Set email as the login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'identification']  # Username is still required